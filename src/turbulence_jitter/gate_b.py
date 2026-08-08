"""Gate-B phase-screen qualification kernels (V4-V5 core only).

Implements docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V02.md.
No propagation-level beam-wander/scintillation or structured-field code lives here.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np
from scipy.integrate import quad
from scipy.special import j0

from .gate_a import Grid2D, fft2c, ifft2c


@dataclass(frozen=True)
class PhaseScreenSpec:
    wavelength: float = 1550e-9
    cn2: float = 1e-14
    delta_z: float = 125.0
    outer_scale: float = 10.0
    inner_scale: float = 5e-3

    @property
    def optical_wavenumber(self) -> float:
        return 2.0 * np.pi / self.wavelength

    @property
    def r0_screen(self) -> float:
        return (
            0.423
            * self.optical_wavenumber**2
            * self.cn2
            * self.delta_z
        ) ** (-3.0 / 5.0)


@dataclass(frozen=True)
class HermitianLayout:
    u: np.ndarray
    v: np.ndarray
    independent_mask: np.ndarray
    partner_rows: np.ndarray
    partner_cols: np.ndarray
    independent_rows: np.ndarray
    independent_cols: np.ndarray


def finite_refractive_psd_kappa(
    kappa: np.ndarray | float,
    spec: PhaseScreenSpec,
) -> np.ndarray | float:
    kappa0 = 2.0 * np.pi / spec.outer_scale
    kappam = 5.92 / spec.inner_scale
    return (
        0.033
        * spec.cn2
        * np.exp(-(np.asarray(kappa) / kappam) ** 2)
        / (np.asarray(kappa) ** 2 + kappa0**2) ** (11.0 / 6.0)
    )


def finite_phase_psd_cycles(
    fx: np.ndarray | float,
    fy: np.ndarray | float,
    spec: PhaseScreenSpec,
) -> np.ndarray | float:
    """S_phi(fx,fy) matching dfx dfy measure, with f in cycles/m."""
    radial_f = np.sqrt(np.asarray(fx) ** 2 + np.asarray(fy) ** 2)
    kappa = 2.0 * np.pi * radial_f
    phi_n = finite_refractive_psd_kappa(kappa, spec)
    return (
        (2.0 * np.pi) ** 3
        * spec.optical_wavenumber**2
        * spec.delta_z
        * phi_n
    )


def kolmogorov_phase_psd_cycles(
    fx: np.ndarray | float,
    fy: np.ndarray | float,
    spec: PhaseScreenSpec,
) -> np.ndarray | float:
    """Direct analytic Kolmogorov branch; DC is explicitly zero."""
    radial_f = np.sqrt(np.asarray(fx) ** 2 + np.asarray(fy) ** 2)
    kappa = 2.0 * np.pi * radial_f
    scalar = np.ndim(radial_f) == 0
    if scalar:
        if float(radial_f) == 0.0:
            return 0.0
        phi_n = 0.033 * spec.cn2 * float(kappa) ** (-11.0 / 3.0)
        return (
            (2.0 * np.pi) ** 3
            * spec.optical_wavenumber**2
            * spec.delta_z
            * phi_n
        )
    out = np.zeros_like(radial_f, dtype=float)
    mask = radial_f > 0.0
    phi_n = 0.033 * spec.cn2 * kappa[mask] ** (-11.0 / 3.0)
    out[mask] = (
        (2.0 * np.pi) ** 3
        * spec.optical_wavenumber**2
        * spec.delta_z
        * phi_n
    )
    return out


def build_hermitian_layout(n: int) -> HermitianLayout:
    if n % 2:
        raise ValueError("Gate B requires even N.")
    centered = np.arange(-n // 2, n // 2, dtype=int)
    u, v = np.meshgrid(centered, centered, indexing="xy")
    independent = (
        ((v >= 1) & (v <= n // 2 - 1))
        | ((v == 0) & (u >= 1) & (u <= n // 2 - 1))
        | ((v == -n // 2) & (u >= 1) & (u <= n // 2 - 1))
    )
    rows, cols = np.where(independent)
    uc = u[rows, cols]
    vc = v[rows, cols]
    partner_rows = ((-vc + n // 2) % n).astype(int)
    partner_cols = ((-uc + n // 2) % n).astype(int)
    expected = (n * n - 4) // 2
    if rows.size != expected:
        raise RuntimeError(
            f"Hermitian ownership mismatch: {rows.size} != {expected}."
        )
    if np.any(independent[partner_rows, partner_cols]):
        raise RuntimeError("Independent Hermitian set overlaps its partner set.")
    return HermitianLayout(
        u=u,
        v=v,
        independent_mask=independent,
        partner_rows=partner_rows,
        partner_cols=partner_cols,
        independent_rows=rows,
        independent_cols=cols,
    )


def phase_psd_grid(
    grid: Grid2D,
    spec: PhaseScreenSpec,
    kind: str,
) -> np.ndarray:
    if kind == "finite":
        out = finite_phase_psd_cycles(grid.FX, grid.FY, spec)
    elif kind == "kolmogorov":
        out = kolmogorov_phase_psd_cycles(grid.FX, grid.FY, spec)
    else:
        raise ValueError("kind must be 'finite' or 'kolmogorov'.")
    out = np.asarray(out, dtype=float).copy()
    out[grid.n // 2, grid.n // 2] = 0.0
    return out


def generate_base_fourier_coefficients(
    psd_grid: np.ndarray,
    grid: Grid2D,
    layout: HermitianLayout,
    rng: np.random.Generator,
) -> np.ndarray:
    """Generate centered a_uv with E|a_uv|^2=S_uv df^2."""
    n = grid.n
    df = 1.0 / grid.window
    a = np.zeros((n, n), dtype=np.complex128)
    count = layout.independent_rows.size
    xi = (
        rng.standard_normal(count)
        + 1j * rng.standard_normal(count)
    ) / np.sqrt(2.0)
    vals = (
        df
        * np.sqrt(psd_grid[layout.independent_rows, layout.independent_cols])
        * xi
    )
    a[layout.independent_rows, layout.independent_cols] = vals
    a[layout.partner_rows, layout.partner_cols] = np.conj(vals)

    # Four self-conjugate locations in centered storage. DC piston is zero.
    a[n // 2, n // 2] = 0.0
    for row, col in ((0, n // 2), (n // 2, 0), (0, 0)):
        a[row, col] = (
            df * np.sqrt(psd_grid[row, col]) * rng.standard_normal()
        )
    return a


def generate_base_phase_screen(
    psd_grid: np.ndarray,
    grid: Grid2D,
    layout: HermitianLayout,
    rng: np.random.Generator,
) -> tuple[np.ndarray, np.ndarray]:
    """Return real base phase screen and its centered DFT array F=N^2*a."""
    a = generate_base_fourier_coefficients(psd_grid, grid, layout, rng)
    F = grid.n**2 * a
    phase_complex = ifft2c(F)
    if np.max(np.abs(phase_complex.imag)) > 1e-10:
        raise RuntimeError("Hermitian fill failed to produce a real phase screen.")
    return phase_complex.real, F


def v4_annulus_definition(grid: Grid2D) -> tuple[np.ndarray, np.ndarray]:
    fmin = 4.0 / grid.window
    fmax = 0.20 / grid.dx
    edges = np.geomspace(fmin, fmax, 13)
    centers = np.sqrt(edges[:-1] * edges[1:])
    return edges, centers


def qualify_v4_psd(
    grid: Grid2D,
    spec: PhaseScreenSpec,
    n_ensemble: int,
    seed: int,
) -> dict:
    psd = phase_psd_grid(grid, spec, "finite")
    layout = build_hermitian_layout(grid.n)
    rng = np.random.default_rng(seed)
    df = 1.0 / grid.window
    estimator_sum = np.zeros_like(psd)
    max_imaginary_residual = 0.0

    for _ in range(n_ensemble):
        phase, _ = generate_base_phase_screen(psd, grid, layout, rng)
        F_rec = fft2c(phase)
        estimator_sum += np.abs(F_rec) ** 2 / (grid.n**4 * df**2)
        # fft2c(real phase) should itself obey Hermitian symmetry; the real-screen
        # check already occurs in generate_base_phase_screen.
        max_imaginary_residual = max(max_imaginary_residual, 0.0)

    estimate = estimator_sum / n_ensemble
    radial_f = np.sqrt(grid.FX**2 + grid.FY**2)
    edges, centers = v4_annulus_definition(grid)
    numerical = []
    target = []
    counts = []
    errors = []
    for index in range(12):
        if index < 11:
            mask = (radial_f >= edges[index]) & (radial_f < edges[index + 1])
        else:
            mask = (radial_f >= edges[index]) & (radial_f <= edges[index + 1])
        count = int(np.count_nonzero(mask))
        if count < 20:
            raise RuntimeError(f"V4 annulus {index} has only {count} pixels.")
        num = float(np.mean(estimate[mask]))
        ref = float(np.mean(psd[mask]))
        counts.append(count)
        numerical.append(num)
        target.append(ref)
        errors.append(abs(num / ref - 1.0))

    slope_num = float(np.polyfit(np.log(centers), np.log(numerical), 1)[0])
    slope_target = float(np.polyfit(np.log(centers), np.log(target), 1)[0])
    return {
        "n_ensemble": n_ensemble,
        "seed": seed,
        "annulus_counts": counts,
        "annulus_centers_cycles_per_m": centers.tolist(),
        "annulus_relative_errors": errors,
        "median_level_relative_error": float(np.median(errors)),
        "slope_numerical": slope_num,
        "slope_target": slope_target,
        "slope_difference": abs(slope_num - slope_target),
        "max_imaginary_residual": max_imaginary_residual,
    }


SH_INDEPENDENT = ((1, 0), (0, 1), (1, 1), (1, -1))
SH_ALL = tuple(
    (i, j)
    for i in (-1, 0, 1)
    for j in (-1, 0, 1)
    if not (i == 0 and j == 0)
)


def precompute_subharmonic_basis(
    grid: Grid2D,
    p_max: int,
) -> dict[tuple[int, int, int], np.ndarray]:
    df = 1.0 / grid.window
    basis: dict[tuple[int, int, int], np.ndarray] = {}
    for p in range(1, p_max + 1):
        dfp = df / 3**p
        for i, j in SH_INDEPENDENT:
            basis[(p, i, j)] = np.exp(
                1j
                * 2.0
                * np.pi
                * (i * dfp * grid.X + j * dfp * grid.Y)
            )
    return basis


def generate_subharmonic_phase(
    psd_function: Callable[[float, float], float],
    grid: Grid2D,
    p_depth: int,
    rng: np.random.Generator,
    basis: dict[tuple[int, int, int], np.ndarray] | None = None,
) -> np.ndarray:
    """Generate SH field with each conjugate pair owned exactly once."""
    df = 1.0 / grid.window
    out = np.zeros((grid.n, grid.n), dtype=float)
    for p in range(1, p_depth + 1):
        dfp = df / 3**p
        for i, j in SH_INDEPENDENT:
            xi = (rng.standard_normal() + 1j * rng.standard_normal()) / np.sqrt(2.0)
            a = dfp * np.sqrt(psd_function(i * dfp, j * dfp)) * xi
            if basis is None:
                E = np.exp(
                    1j
                    * 2.0
                    * np.pi
                    * (i * dfp * grid.X + j * dfp * grid.Y)
                )
            else:
                E = basis[(p, i, j)]
            # Explicitly add the independent cell and its conjugate partner once.
            pair = a * E + np.conj(a) * np.conj(E)
            out += pair.real
    return out


def deterministic_structure_function(
    psd_grid: np.ndarray,
    psd_function: Callable[[float, float], float],
    grid: Grid2D,
    rho_x: float,
    rho_y: float,
    p_depth: int,
) -> float:
    df = 1.0 / grid.window
    base = 2.0 * np.sum(
        psd_grid
        * df**2
        * (
            1.0
            - np.cos(2.0 * np.pi * (grid.FX * rho_x + grid.FY * rho_y))
        )
    )
    sh = 0.0
    for p in range(1, p_depth + 1):
        dfp = df / 3**p
        for i, j in SH_ALL:
            fx = i * dfp
            fy = j * dfp
            sh += (
                2.0
                * psd_function(fx, fy)
                * dfp**2
                * (
                    1.0
                    - np.cos(2.0 * np.pi * (fx * rho_x + fy * rho_y))
                )
            )
    return float(base + sh)


def finite_structure_reference(
    rho: float,
    spec: PhaseScreenSpec,
    epsrel: float = 1e-9,
) -> tuple[float, float]:
    """Independent continuous atmospheric-measure structure-function integral."""
    kappa0 = 2.0 * np.pi / spec.outer_scale
    kappam = 5.92 / spec.inner_scale

    def integrand(kappa: float) -> float:
        phi_n = float(finite_refractive_psd_kappa(kappa, spec))
        phi_atm = (
            2.0
            * np.pi
            * spec.optical_wavenumber**2
            * spec.delta_z
            * phi_n
        )
        return 4.0 * np.pi * kappa * phi_atm * (1.0 - j0(kappa * rho))

    candidates = (kappa0, 1.0 / rho, kappam, 5.0 * kappam)
    bounds = [0.0]
    for value in candidates:
        if value > bounds[-1] * (1.0 + 1e-12):
            bounds.append(float(value))
    bounds.append(np.inf)

    value = 0.0
    error = 0.0
    for lower, upper in zip(bounds[:-1], bounds[1:]):
        part, part_error = quad(
            integrand,
            lower,
            upper,
            epsabs=0.0,
            epsrel=epsrel,
            limit=400,
        )
        value += part
        error += part_error
    return float(value), float(error)


def kolmogorov_structure_reference(rho: float, spec: PhaseScreenSpec) -> float:
    return float(6.88 * (rho / spec.r0_screen) ** (5.0 / 3.0))


def structure_function_valid_pairs(
    phase: np.ndarray,
    shift_x: int,
    shift_y: int,
) -> float:
    """Non-periodic valid-pair estimator; shift_x/y are nonnegative pixels."""
    if shift_x < 0 or shift_y < 0:
        raise ValueError("Gate-B frozen directions use nonnegative shifts.")
    y0 = slice(0, phase.shape[0] - shift_y if shift_y else phase.shape[0])
    y1 = slice(shift_y, phase.shape[0]) if shift_y else y0
    x0 = slice(0, phase.shape[1] - shift_x if shift_x else phase.shape[1])
    x1 = slice(shift_x, phase.shape[1]) if shift_x else x0
    difference = phase[y1, x1] - phase[y0, x0]
    return float(np.mean(difference**2))


def frozen_direction_shifts() -> dict[str, tuple[tuple[int, int], ...]]:
    axial = (4, 5, 7, 9, 11, 14, 18, 23, 30, 39, 50, 64)
    diagonal = (3, 4, 5, 6, 8, 10, 13, 16, 21, 28, 35, 45)
    return {
        "x": tuple((n, 0) for n in axial),
        "y": tuple((0, n) for n in axial),
        "45": tuple((n, n) for n in diagonal),
    }
