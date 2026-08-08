#!/usr/bin/env python3
"""Run authorized Gate-B core qualification (V4 + deterministic/minimal V5).

This runner intentionally stops before the formal 512-screen V5 bootstrap gate.
That larger empirical confirmation is an extension after the core implementation
has been inspected.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from turbulence_jitter.gate_a import make_centered_grid  # noqa: E402
from turbulence_jitter.gate_b import (  # noqa: E402
    PhaseScreenSpec,
    build_hermitian_layout,
    deterministic_structure_function,
    finite_phase_psd_cycles,
    finite_structure_reference,
    frozen_direction_shifts,
    generate_base_phase_screen,
    generate_subharmonic_phase,
    kolmogorov_phase_psd_cycles,
    kolmogorov_structure_reference,
    phase_psd_grid,
    precompute_subharmonic_basis,
    qualify_v4_psd,
    structure_function_valid_pairs,
)

N = 512
DX = 1.015625e-3
V4_ENSEMBLE = 128
V4_SEED = 2026080801
P_LADDER = tuple(range(8))
P_GUARD = 0.08
SLOPE_GUARD = 0.08
EMPIRICAL_DIAGNOSTIC_ENSEMBLE = 128
FINITE_EMPIRICAL_SEED = 2026080803
KOLMOGOROV_EMPIRICAL_SEED = 2026080804


def rel_median(values: np.ndarray, reference: np.ndarray) -> float:
    return float(np.median(np.abs(values - reference) / reference))


def radial_separations(grid, shifts):
    return np.array(
        [np.hypot(sx * grid.dx, sy * grid.dx) for sx, sy in shifts],
        dtype=float,
    )


def continuous_references(grid, spec, directions):
    finite = {}
    kolmogorov = {}
    quadrature_check = {}
    for name, shifts in directions.items():
        rho = radial_separations(grid, shifts)
        finite_values = []
        convergence = []
        for r in rho:
            loose, _ = finite_structure_reference(float(r), spec, epsrel=1e-8)
            tight, _ = finite_structure_reference(float(r), spec, epsrel=1e-10)
            finite_values.append(tight)
            convergence.append(abs(loose - tight) / tight)
        finite[name] = np.array(finite_values)
        kolmogorov[name] = np.array(
            [kolmogorov_structure_reference(float(r), spec) for r in rho]
        )
        quadrature_check[name] = float(max(convergence))
    return finite, kolmogorov, quadrature_check


def deterministic_ladder(grid, spec, directions, finite_ref, kolm_ref):
    finite_grid = phase_psd_grid(grid, spec, "finite")
    kolm_grid = phase_psd_grid(grid, spec, "kolmogorov")

    finite_fun = lambda fx, fy: float(finite_phase_psd_cycles(fx, fy, spec))
    kolm_fun = lambda fx, fy: float(kolmogorov_phase_psd_cycles(fx, fy, spec))

    table = []
    selected = None
    selected_values = None
    for p_depth in P_LADDER:
        row = {"P": p_depth, "finite": {}, "kolmogorov": {}}
        passes = True
        values_for_p = {"finite": {}, "kolmogorov": {}}
        for name, shifts in directions.items():
            finite_values = np.array(
                [
                    deterministic_structure_function(
                        finite_grid,
                        finite_fun,
                        grid,
                        sx * grid.dx,
                        sy * grid.dx,
                        p_depth,
                    )
                    for sx, sy in shifts
                ]
            )
            kolm_values = np.array(
                [
                    deterministic_structure_function(
                        kolm_grid,
                        kolm_fun,
                        grid,
                        sx * grid.dx,
                        sy * grid.dx,
                        p_depth,
                    )
                    for sx, sy in shifts
                ]
            )
            rho = radial_separations(grid, shifts)
            finite_error = rel_median(finite_values, finite_ref[name])
            kolm_error = rel_median(kolm_values, kolm_ref[name])
            kolm_slope = float(np.polyfit(np.log(rho), np.log(kolm_values), 1)[0])
            slope_error = abs(kolm_slope - 5.0 / 3.0)
            row["finite"][name] = {"median_relative_error": finite_error}
            row["kolmogorov"][name] = {
                "median_relative_error": kolm_error,
                "slope": kolm_slope,
                "slope_error": slope_error,
            }
            values_for_p["finite"][name] = finite_values
            values_for_p["kolmogorov"][name] = kolm_values
            passes = passes and finite_error <= P_GUARD
            passes = passes and kolm_error <= P_GUARD
            passes = passes and slope_error <= SLOPE_GUARD
        row["passes_8pct_guard"] = passes
        table.append(row)
        if selected is None and passes:
            selected = p_depth
            selected_values = values_for_p

    if selected is None:
        raise RuntimeError("No P<=7 passes the deterministic Gate-B guard.")
    return table, selected, selected_values, finite_grid, kolm_grid


def empirical_diagnostic(
    grid,
    spec,
    directions,
    psd_grid,
    psd_fun,
    p_depth,
    deterministic_values,
    continuous_reference,
    n_ensemble,
    seed,
    basis,
):
    layout = build_hermitian_layout(grid.n)
    rng = np.random.default_rng(seed)
    all_values = {name: [] for name in directions}
    for _ in range(n_ensemble):
        base, _ = generate_base_phase_screen(psd_grid, grid, layout, rng)
        sh = generate_subharmonic_phase(
            psd_fun,
            grid,
            p_depth,
            rng,
            basis=basis,
        )
        phase = base + sh
        for name, shifts in directions.items():
            all_values[name].append(
                np.array(
                    [
                        structure_function_valid_pairs(phase, sx, sy)
                        for sx, sy in shifts
                    ]
                )
            )

    summary = {}
    for name, shifts in directions.items():
        empirical = np.mean(np.asarray(all_values[name]), axis=0)
        rho = radial_separations(grid, shifts)
        summary[name] = {
            "implementation_recovery_median_relative_error": rel_median(
                empirical,
                deterministic_values[name],
            ),
            "continuous_reference_median_relative_error": rel_median(
                empirical,
                continuous_reference[name],
            ),
            "fitted_slope": float(np.polyfit(np.log(rho), np.log(empirical), 1)[0]),
        }
    return summary


def run() -> dict:
    spec = PhaseScreenSpec()
    grid = make_centered_grid(N, DX)
    directions = frozen_direction_shifts()

    v4 = qualify_v4_psd(grid, spec, V4_ENSEMBLE, V4_SEED)
    if v4["median_level_relative_error"] > 0.10:
        raise AssertionError("V4 PSD level gate failed.")
    if v4["slope_difference"] > 0.10:
        raise AssertionError("V4 target-slope gate failed.")

    finite_ref, kolm_ref, quad_check = continuous_references(
        grid,
        spec,
        directions,
    )
    if max(quad_check.values()) >= 1e-4:
        raise AssertionError("Independent finite-scale quadrature did not converge.")

    ladder, p_star, selected, finite_grid, kolm_grid = deterministic_ladder(
        grid,
        spec,
        directions,
        finite_ref,
        kolm_ref,
    )

    # 128 screens are diagnostic only; formal V5 remains 512 + bootstrap.
    basis = precompute_subharmonic_basis(grid, p_star)
    finite_fun = lambda fx, fy: float(finite_phase_psd_cycles(fx, fy, spec))
    kolm_fun = lambda fx, fy: float(kolmogorov_phase_psd_cycles(fx, fy, spec))
    empirical_finite = empirical_diagnostic(
        grid,
        spec,
        directions,
        finite_grid,
        finite_fun,
        p_star,
        selected["finite"],
        finite_ref,
        EMPIRICAL_DIAGNOSTIC_ENSEMBLE,
        FINITE_EMPIRICAL_SEED,
        basis,
    )
    empirical_kolm = empirical_diagnostic(
        grid,
        spec,
        directions,
        kolm_grid,
        kolm_fun,
        p_star,
        selected["kolmogorov"],
        kolm_ref,
        EMPIRICAL_DIAGNOSTIC_ENSEMBLE,
        KOLMOGOROV_EMPIRICAL_SEED,
        basis,
    )

    return {
        "contract": "Numerical Implementation Contract v0.2 / Gate B",
        "status_boundary": (
            "Core V4 and deterministic/minimal empirical V5 only; "
            "formal 512-screen bootstrap V5 not executed here."
        ),
        "parameters": {
            "N": N,
            "dx_m": DX,
            "window_m": grid.window,
            "df_cycles_per_m": 1.0 / grid.window,
            "wavelength_m": spec.wavelength,
            "Cn2_m_minus_2_over_3": spec.cn2,
            "delta_z_m": spec.delta_z,
            "L0_m": spec.outer_scale,
            "l0_m": spec.inner_scale,
            "r0_screen_m": spec.r0_screen,
        },
        "V4": v4,
        "finite_reference_quadrature_max_relative_change": quad_check,
        "deterministic_P_ladder": ladder,
        "P_star": p_star,
        "empirical_128_diagnostic": {
            "finite": empirical_finite,
            "kolmogorov": empirical_kolm,
        },
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
