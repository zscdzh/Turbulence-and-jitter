"""Gate-A Gaussian qualification kernels (V0-V3 only).

This module implements the numerical conventions frozen in
docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V01.md.

It intentionally contains no turbulence or structured-field code.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from numpy.polynomial.hermite import hermgauss


@dataclass(frozen=True)
class Grid2D:
    """Centered square Cartesian grid and its cycles/m Fourier grid."""

    n: int
    dx: float
    x: np.ndarray
    f: np.ndarray
    X: np.ndarray
    Y: np.ndarray
    FX: np.ndarray
    FY: np.ndarray

    @property
    def window(self) -> float:
        return self.n * self.dx


def make_centered_grid(n: int, dx: float) -> Grid2D:
    if n % 2:
        raise ValueError("Gate-A contract requires even n.")
    x = (np.arange(n, dtype=float) - n / 2.0) * dx
    f = (np.arange(n, dtype=float) - n / 2.0) / (n * dx)
    X, Y = np.meshgrid(x, x, indexing="xy")
    FX, FY = np.meshgrid(f, f, indexing="xy")
    return Grid2D(n=n, dx=dx, x=x, f=f, X=X, Y=Y, FX=FX, FY=FY)


def fft2c(u: np.ndarray) -> np.ndarray:
    """Centered 2-D forward FFT with explicit NumPy backward normalization."""
    return np.fft.fftshift(
        np.fft.fft2(np.fft.ifftshift(u), norm="backward")
    )


def ifft2c(U: np.ndarray) -> np.ndarray:
    """Centered 2-D inverse FFT with explicit NumPy backward normalization."""
    return np.fft.fftshift(
        np.fft.ifft2(np.fft.ifftshift(U), norm="backward")
    )


def grid_power(u: np.ndarray, dx: float) -> float:
    return float(dx * dx * np.sum(np.abs(u) ** 2))


def normalize_grid_power(u: np.ndarray, dx: float, target: float = 1.0) -> np.ndarray:
    p = grid_power(u, dx)
    if p <= 0:
        raise ValueError("Field power must be positive.")
    return u * np.sqrt(target / p)


def gaussian_field(grid: Grid2D, w: float) -> np.ndarray:
    """Unclipped Gaussian amplitude U=exp[-r^2/w^2]."""
    return np.exp(-(grid.X**2 + grid.Y**2) / w**2).astype(np.complex128)


def fresnel_propagate(
    u0: np.ndarray,
    grid: Grid2D,
    wavelength: float,
    distance: float,
) -> np.ndarray:
    """Paraxial Fresnel transfer-function propagation with carrier removed."""
    H = np.exp(
        -1j
        * np.pi
        * wavelength
        * distance
        * (grid.FX**2 + grid.FY**2)
    )
    return ifft2c(fft2c(u0) * H)


def apply_tilt(
    u0: np.ndarray,
    grid: Grid2D,
    wavelength: float,
    theta_x: float,
    theta_y: float,
) -> np.ndarray:
    """Apply transmitter angular tilt exp[i k0(theta_x x + theta_y y)]."""
    k0 = 2.0 * np.pi / wavelength
    return u0 * np.exp(
        1j * k0 * (theta_x * grid.X + theta_y * grid.Y)
    )


def centroid_and_radius(
    intensity: np.ndarray,
    grid: Grid2D,
) -> tuple[float, float, float]:
    """Return centroid and Gaussian 1/e^2 radius from the frozen 2nd moment."""
    total = float(np.sum(intensity))
    if total <= 0:
        raise ValueError("Intensity sum must be positive.")
    xc = float(np.sum(grid.X * intensity) / total)
    yc = float(np.sum(grid.Y * intensity) / total)
    radius_sq = 2.0 * np.sum(
        ((grid.X - xc) ** 2 + (grid.Y - yc) ** 2) * intensity
    ) / total
    return xc, yc, float(np.sqrt(radius_sq))


def gaussian_references(
    wavelength: float,
    w0: float,
    distance: float,
) -> tuple[float, float, float]:
    """Return z_R, W(z), and c=k0/(2R) for an ideal Gaussian."""
    z_r = np.pi * w0**2 / wavelength
    w = w0 * np.sqrt(1.0 + (distance / z_r) ** 2)
    R = distance * (1.0 + (z_r / distance) ** 2)
    k0 = 2.0 * np.pi / wavelength
    c = k0 / (2.0 * R)
    return float(z_r), float(w), float(c)


def phase_curvature_coefficient(
    u: np.ndarray,
    grid: Grid2D,
    intensity_threshold: float = 1e-3,
    phase_guard: float = np.pi / 2.0,
) -> tuple[float, float]:
    """Fit c in phi=c(x^2+y^2)+piston using wrapped local gradients.

    Gradients are assigned to half-pixel locations. Both endpoints must
    satisfy I/Imax >= intensity_threshold. Geometric-mean intensity weights
    are frozen by the Gate-A contract.
    """
    I = np.abs(u) ** 2
    mask = I / np.max(I) >= intensity_threshold

    # x-directed links live at x_{m+1/2}
    link_x = u[:, 1:] * np.conj(u[:, :-1])
    dphi_x = np.angle(link_x)
    valid_x = mask[:, 1:] & mask[:, :-1]
    x_mid = 0.5 * (grid.x[1:] + grid.x[:-1])
    X_mid = np.broadcast_to(x_mid, (grid.n, grid.n - 1))
    gx = dphi_x / grid.dx
    wx = np.sqrt(I[:, 1:] * I[:, :-1])

    # y-directed links live at y_{n+1/2}
    link_y = u[1:, :] * np.conj(u[:-1, :])
    dphi_y = np.angle(link_y)
    valid_y = mask[1:, :] & mask[:-1, :]
    y_mid = 0.5 * (grid.x[1:] + grid.x[:-1])
    Y_mid = np.broadcast_to(y_mid[:, None], (grid.n - 1, grid.n))
    gy = dphi_y / grid.dx
    wy = np.sqrt(I[1:, :] * I[:-1, :])

    max_adjacent_phase = max(
        float(np.max(np.abs(dphi_x[valid_x]), initial=0.0)),
        float(np.max(np.abs(dphi_y[valid_y]), initial=0.0)),
    )
    if max_adjacent_phase >= phase_guard:
        raise ValueError(
            "V1 phase-gradient guard violated: adjacent wrapped phase "
            f"{max_adjacent_phase:.6g} >= {phase_guard:.6g} rad."
        )

    coord = np.concatenate((X_mid[valid_x], Y_mid[valid_y]))
    grad = np.concatenate((gx[valid_x], gy[valid_y]))
    weight = np.concatenate((wx[valid_x], wy[valid_y]))

    # Zero-intercept WLS for grad = 2*c*coord.
    basis = 2.0 * coord
    c_num = np.sum(weight * basis * grad) / np.sum(weight * basis**2)
    return float(c_num), max_adjacent_phase


def displaced_gaussian_intensity(
    grid: Grid2D,
    w: float,
    displacement_x: float,
) -> np.ndarray:
    """Unit-power continuous Gaussian sampled at pixel centers."""
    return (
        2.0
        / (np.pi * w**2)
        * np.exp(
            -2.0
            * ((grid.X - displacement_x) ** 2 + grid.Y**2)
            / w**2
        )
    )


def circular_capture(
    intensity: np.ndarray,
    grid: Grid2D,
    aperture_radius: float,
) -> float:
    """Pixel-center circular-aperture integration."""
    mask = grid.X**2 + grid.Y**2 <= aperture_radius**2
    return float(grid.dx**2 * np.sum(intensity[mask]))


def displaced_gaussian_capture_reference(
    w: float,
    aperture_radius: float,
    displacement_x: float,
) -> float:
    """Continuous Marcum-Q-equivalent reference via noncentral chi-square CDF."""
    try:
        from scipy.stats import ncx2
    except ImportError as exc:
        raise ImportError(
            "SciPy is required only for the independent V2 continuous reference."
        ) from exc
    alpha = 2.0 * displacement_x / w
    beta = 2.0 * aperture_radius / w
    return float(ncx2.cdf(beta**2, df=2, nc=alpha**2))


def gauss_hermite_long_exposure(
    u0: np.ndarray,
    grid: Grid2D,
    wavelength: float,
    distance: float,
    sigma_theta: float,
    n_gh: int = 9,
) -> np.ndarray:
    """Deterministic isotropic Gaussian-jitter long-exposure intensity."""
    nodes, weights = hermgauss(n_gh)
    out = np.zeros_like(np.abs(u0) ** 2, dtype=float)
    for i, xi in enumerate(nodes):
        theta_x = np.sqrt(2.0) * sigma_theta * xi
        for j, yj in enumerate(nodes):
            theta_y = np.sqrt(2.0) * sigma_theta * yj
            weight = weights[i] * weights[j] / np.pi
            tilted = apply_tilt(
                u0, grid, wavelength, theta_x, theta_y
            )
            propagated = fresnel_propagate(
                tilted, grid, wavelength, distance
            )
            out += weight * np.abs(propagated) ** 2
    return out
