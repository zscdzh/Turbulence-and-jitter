#!/usr/bin/env python3
"""Run the authorized fresh Gate-B v0.2.1 formal V5 rerun.

This runner follows docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V021.md.  It uses a
new seed family, never overwrites the historical v0.2/P=6 results, stores only
per-screen structure-function observables, and stops at Gate B.
"""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
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
P_LADDER = tuple(range(13))
MEDIAN_GUARD = 0.06
POINTWISE_GUARD = 0.10
SLOPE_GUARD = 0.08
FORMAL_ENSEMBLE = 512
DIAGNOSTIC_PREFIXES = (128, 256, 512)
B_BOOT = 2000

# New v0.2.1 family. These integers are registered in metadata before any
# formal screen is generated and must never be changed after observing results.
SEEDS = {
    "v4_screen_seed": 2026080830,
    "finite_formal_screen_seed": 2026080831,
    "kolmogorov_formal_screen_seed": 2026080832,
    "finite_bootstrap_seed": 2026080833,
    "kolmogorov_bootstrap_seed": 2026080834,
}

OUTPUT_DIR = REPO_ROOT / "results" / "gate_b_v5_formal_v021"
RESULT_DOC = REPO_ROOT / "docs" / "results" / "GATE_B_V4_V5_FORMAL_V021_RESULTS.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def git_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
        ).strip()
    except Exception:
        return "UNAVAILABLE"


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def rel_median(values: np.ndarray, reference: np.ndarray) -> float:
    return float(np.median(np.abs(values - reference) / reference))


def rel_max(values: np.ndarray, reference: np.ndarray) -> float:
    return float(np.max(np.abs(values - reference) / reference))


def radial_separations(grid, shifts) -> np.ndarray:
    return np.array(
        [np.hypot(sx * grid.dx, sy * grid.dx) for sx, sy in shifts], dtype=float
    )


def fitted_slope(rho: np.ndarray, values: np.ndarray) -> float:
    return float(np.polyfit(np.log(rho), np.log(values), 1)[0])


def continuous_references(grid, spec, directions):
    finite = {}
    kolmogorov = {}
    quadrature_check = {}
    for name, shifts in directions.items():
        rho = radial_separations(grid, shifts)
        finite_values = []
        convergence = []
        for separation in rho:
            loose, _ = finite_structure_reference(
                float(separation), spec, epsrel=1e-8
            )
            tight, _ = finite_structure_reference(
                float(separation), spec, epsrel=1e-10
            )
            finite_values.append(tight)
            convergence.append(abs(loose - tight) / tight)
        finite[name] = np.asarray(finite_values)
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

    rows = []
    values_by_p = {}
    for p_depth in P_LADDER:
        row = {"P": p_depth, "finite": {}, "kolmogorov": {}}
        values_for_p = {"finite": {}, "kolmogorov": {}}
        passes = True
        for name, shifts in directions.items():
            rho = radial_separations(grid, shifts)
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

            finite_median = rel_median(finite_values, finite_ref[name])
            finite_max = rel_max(finite_values, finite_ref[name])
            kolm_median = rel_median(kolm_values, kolm_ref[name])
            kolm_max = rel_max(kolm_values, kolm_ref[name])
            kolm_slope = fitted_slope(rho, kolm_values)
            slope_error = abs(kolm_slope - 5.0 / 3.0)

            row["finite"][name] = {
                "median_relative_error": finite_median,
                "max_relative_error": finite_max,
                "D_disc_rad2": finite_values.tolist(),
            }
            row["kolmogorov"][name] = {
                "median_relative_error": kolm_median,
                "max_relative_error": kolm_max,
                "slope": kolm_slope,
                "slope_error": slope_error,
                "D_disc_rad2": kolm_values.tolist(),
            }
            values_for_p["finite"][name] = finite_values
            values_for_p["kolmogorov"][name] = kolm_values

            passes &= finite_median <= MEDIAN_GUARD
            passes &= finite_max <= POINTWISE_GUARD
            passes &= kolm_median <= MEDIAN_GUARD
            passes &= kolm_max <= POINTWISE_GUARD
            passes &= slope_error <= SLOPE_GUARD

        row["passes_v021_headroom_policy"] = bool(passes)
        rows.append(row)
        values_by_p[p_depth] = values_for_p

    passing = [row["P"] for row in rows if row["passes_v021_headroom_policy"]]
    if not passing:
        raise RuntimeError(
            "REVISE — LOW-FREQUENCY REPRESENTATION: no P<=12 passes v0.2.1."
        )
    p_star = min(passing)
    return rows, p_star, values_by_p[p_star], finite_grid, kolm_grid


def register_pre_run_metadata(spec, grid, directions) -> dict:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / "metadata.json"
    if path.exists():
        prior = json.loads(path.read_text(encoding="utf-8"))
        if prior.get("seeds") != SEEDS:
            raise RuntimeError("Existing v0.2.1 metadata uses different seeds.")
    metadata = {
        "contract": "Numerical Implementation Contract v0.2.1 / Gate B",
        "run_state": "seeds_registered_before_formal_screen_generation",
        "registered_utc": utc_now(),
        "git_sha_at_run_start": git_head(),
        "seeds": SEEDS,
        "historical_v02_results_preserved": True,
        "formal_ensemble": FORMAL_ENSEMBLE,
        "diagnostic_prefixes": list(DIAGNOSTIC_PREFIXES),
        "bootstrap_resamples": B_BOOT,
        "bootstrap_unit": "screen_id",
        "bootstrap_rule": "shared resample-count weights across directions per case",
        "percentile_method": "numpy linear",
        "selection": {
            "P_ladder": list(P_LADDER),
            "median_guard": MEDIAN_GUARD,
            "pointwise_guard": POINTWISE_GUARD,
            "slope_guard": SLOPE_GUARD,
            "policy": "minimum-depth deterministic bias-headroom",
        },
        "qualification_slab": {
            "wavelength_m": spec.wavelength,
            "Cn2_m_minus_2_over_3": spec.cn2,
            "delta_z_m": spec.delta_z,
            "L0_m": spec.outer_scale,
            "l0_m": spec.inner_scale,
            "r0_screen_m": spec.r0_screen,
            "N": grid.n,
            "dx_m": grid.dx,
            "window_m": grid.window,
        },
        "directions": {
            name: [list(shift) for shift in shifts]
            for name, shifts in directions.items()
        },
        "raw_phase_screens_saved": False,
    }
    write_json(path, metadata)
    return metadata


def generate_observables(
    *, grid, directions, psd_grid, psd_fun, p_depth, seed, basis, label
) -> np.ndarray:
    layout = build_hermitian_layout(grid.n)
    rng = np.random.default_rng(seed)
    observables = np.empty(
        (FORMAL_ENSEMBLE, len(directions), 12), dtype=np.float64
    )
    for screen_id in range(FORMAL_ENSEMBLE):
        base, _ = generate_base_phase_screen(psd_grid, grid, layout, rng)
        subharmonic = generate_subharmonic_phase(
            psd_fun, grid, p_depth, rng, basis=basis
        )
        phase = base + subharmonic
        for direction_index, shifts in enumerate(directions.values()):
            observables[screen_id, direction_index] = [
                structure_function_valid_pairs(phase, sx, sy)
                for sx, sy in shifts
            ]
        if (screen_id + 1) % 64 == 0:
            print(f"{label}: {screen_id + 1}/{FORMAL_ENSEMBLE}", flush=True)
    return observables


def save_observables(path, observables, grid, directions, case, seed, p_depth):
    np.savez_compressed(
        path,
        D_phi_rad2=observables,
        screen_id=np.arange(FORMAL_ENSEMBLE, dtype=np.int32),
        case=np.asarray(case),
        direction=np.asarray(list(directions), dtype="U2"),
        shift_pixels=np.asarray(list(directions.values()), dtype=np.int16),
        rho_m=np.stack(
            [radial_separations(grid, shifts) for shifts in directions.values()]
        ),
        screen_seed=np.asarray(seed, dtype=np.int64),
        p_depth=np.asarray(p_depth, dtype=np.int16),
    )


def point_summary(observables, deterministic, reference, grid, directions, n):
    result = {}
    for direction_index, (name, shifts) in enumerate(directions.items()):
        mean_values = np.mean(observables[:n, direction_index, :], axis=0)
        rho = radial_separations(grid, shifts)
        result[name] = {
            "implementation_recovery_median_relative_error": rel_median(
                mean_values, deterministic[name]
            ),
            "continuous_reference_median_relative_error": rel_median(
                mean_values, reference[name]
            ),
            "fitted_slope": fitted_slope(rho, mean_values),
        }
    return result


def bootstrap_case(
    observables, deterministic, reference, grid, directions, seed
):
    rng = np.random.default_rng(seed)
    weights = np.empty((B_BOOT, FORMAL_ENSEMBLE), dtype=np.int16)
    for bootstrap_id in range(B_BOOT):
        sampled = rng.integers(0, FORMAL_ENSEMBLE, FORMAL_ENSEMBLE)
        weights[bootstrap_id] = np.bincount(
            sampled, minlength=FORMAL_ENSEMBLE
        )

    summary = {}
    for direction_index, (name, shifts) in enumerate(directions.items()):
        values = observables[:, direction_index, :]
        point_mean = np.mean(values, axis=0)
        boot_means = weights @ values / FORMAL_ENSEMBLE
        impl_statistics = np.median(
            np.abs(boot_means - deterministic[name]) / deterministic[name], axis=1
        )
        amplitude_statistics = np.median(
            np.abs(boot_means - reference[name]) / reference[name], axis=1
        )
        rho = radial_separations(grid, shifts)
        log_rho_centered = np.log(rho) - np.mean(np.log(rho))
        slope_denominator = np.sum(log_rho_centered**2)
        slopes = np.log(boot_means) @ log_rho_centered / slope_denominator
        summary[name] = {
            "implementation_recovery": {
                "point_estimate": rel_median(point_mean, deterministic[name]),
                "bootstrap_95pct_upper_bound": float(
                    np.percentile(impl_statistics, 95.0)
                ),
            },
            "continuous_amplitude": {
                "point_estimate": rel_median(point_mean, reference[name]),
                "bootstrap_95pct_upper_bound": float(
                    np.percentile(amplitude_statistics, 95.0)
                ),
            },
            "slope": {
                "point_estimate": fitted_slope(rho, point_mean),
                "bootstrap_95pct_interval": [
                    float(np.percentile(slopes, 2.5)),
                    float(np.percentile(slopes, 97.5)),
                ],
            },
        }
    return summary


def formal_pass(finite_summary, kolm_summary) -> bool:
    for name in ("x", "y", "45"):
        if finite_summary[name]["implementation_recovery"]["bootstrap_95pct_upper_bound"] > 0.05:
            return False
        if finite_summary[name]["continuous_amplitude"]["bootstrap_95pct_upper_bound"] > 0.10:
            return False
        if kolm_summary[name]["implementation_recovery"]["bootstrap_95pct_upper_bound"] > 0.05:
            return False
        if kolm_summary[name]["continuous_amplitude"]["bootstrap_95pct_upper_bound"] > 0.10:
            return False
        low, high = kolm_summary[name]["slope"]["bootstrap_95pct_interval"]
        if low < 5.0 / 3.0 - 0.10 or high > 5.0 / 3.0 + 0.10:
            return False
    return True


def run() -> dict:
    spec = PhaseScreenSpec()
    grid = make_centered_grid(N, DX)
    directions = frozen_direction_shifts()

    # Register all fresh seeds before any formal phase screen is generated.
    metadata = register_pre_run_metadata(spec, grid, directions)

    v4 = qualify_v4_psd(grid, spec, V4_ENSEMBLE, SEEDS["v4_screen_seed"])
    if v4["median_level_relative_error"] > 0.10 or v4["slope_difference"] > 0.10:
        raise RuntimeError("REVISE — V4 regression sanity failed.")

    finite_ref, kolm_ref, quad_check = continuous_references(grid, spec, directions)
    if max(quad_check.values()) >= 1e-4:
        raise RuntimeError("Independent finite-scale reference failed convergence.")

    ladder, p_star, selected, finite_grid, kolm_grid = deterministic_ladder(
        grid, spec, directions, finite_ref, kolm_ref
    )
    write_json(
        OUTPUT_DIR / "deterministic_ladder.json",
        {"P_star": p_star, "ladder": ladder, "quadrature_check": quad_check},
    )
    write_json(OUTPUT_DIR / "v4_summary.json", v4)

    basis = precompute_subharmonic_basis(grid, p_star)
    finite_fun = lambda fx, fy: float(finite_phase_psd_cycles(fx, fy, spec))
    kolm_fun = lambda fx, fy: float(kolmogorov_phase_psd_cycles(fx, fy, spec))

    finite_obs = generate_observables(
        grid=grid,
        directions=directions,
        psd_grid=finite_grid,
        psd_fun=finite_fun,
        p_depth=p_star,
        seed=SEEDS["finite_formal_screen_seed"],
        basis=basis,
        label="finite",
    )
    save_observables(
        OUTPUT_DIR / "finite_screen_observables.npz",
        finite_obs,
        grid,
        directions,
        "finite",
        SEEDS["finite_formal_screen_seed"],
        p_star,
    )

    kolm_obs = generate_observables(
        grid=grid,
        directions=directions,
        psd_grid=kolm_grid,
        psd_fun=kolm_fun,
        p_depth=p_star,
        seed=SEEDS["kolmogorov_formal_screen_seed"],
        basis=basis,
        label="kolmogorov",
    )
    save_observables(
        OUTPUT_DIR / "kolmogorov_screen_observables.npz",
        kolm_obs,
        grid,
        directions,
        "kolmogorov",
        SEEDS["kolmogorov_formal_screen_seed"],
        p_star,
    )

    convergence = {"finite": {}, "kolmogorov": {}}
    for n in DIAGNOSTIC_PREFIXES:
        convergence["finite"][str(n)] = point_summary(
            finite_obs, selected["finite"], finite_ref, grid, directions, n
        )
        convergence["kolmogorov"][str(n)] = point_summary(
            kolm_obs, selected["kolmogorov"], kolm_ref, grid, directions, n
        )

    finite_boot = bootstrap_case(
        finite_obs,
        selected["finite"],
        finite_ref,
        grid,
        directions,
        SEEDS["finite_bootstrap_seed"],
    )
    kolm_boot = bootstrap_case(
        kolm_obs,
        selected["kolmogorov"],
        kolm_ref,
        grid,
        directions,
        SEEDS["kolmogorov_bootstrap_seed"],
    )
    passed = formal_pass(finite_boot, kolm_boot)
    decision = (
        "PASS — GATE B V4–V5 QUALIFIED"
        if passed
        else "REVISE — GATE B NOT YET QUALIFIED"
    )

    summary = {
        "contract": "Numerical Implementation Contract v0.2.1 / Gate B",
        "metadata": metadata,
        "V4": v4,
        "P_star": p_star,
        "convergence": convergence,
        "formal_bootstrap": {"finite": finite_boot, "kolmogorov": kolm_boot},
        "decision": decision,
        "v6_authorized": False,
    }
    write_json(OUTPUT_DIR / "bootstrap_summary.json", summary)

    metadata["run_state"] = "formal_v021_completed"
    metadata["P_star"] = p_star
    metadata["decision"] = decision
    metadata["completed_utc"] = utc_now()
    write_json(OUTPUT_DIR / "metadata.json", metadata)

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return summary


if __name__ == "__main__":
    run()
