#!/usr/bin/env python3
"""Reproduce post-failure Gate-B P-depth diagnostics.

Diagnostic only: this script does not qualify Gate B and its seeds must never be
reused by a formal v0.2.1 rerun.  It intentionally mirrors the formal runner's
screen-ID bootstrap algorithm: one resample-weight matrix per P is shared by
x/y/45-degree directions.
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
    frozen_direction_shifts,
    generate_base_phase_screen,
    generate_subharmonic_phase,
    kolmogorov_phase_psd_cycles,
    kolmogorov_structure_reference,
    phase_psd_grid,
    precompute_subharmonic_basis,
    structure_function_valid_pairs,
)

N = 512
DX = 1.015625e-3
N_SCREENS = 512
B_BOOT = 1000
P_VALUES = (8, 9, 12)
SEEDS = {
    8: {"screen": 2026080821, "bootstrap": 2026080822},
    9: {"screen": 2026080823, "bootstrap": 2026080824},
    12: {"screen": 2026080825, "bootstrap": 2026080826},
}
OUTPUT_DIR = REPO_ROOT / "results" / "gate_b_p_depth_diagnostic"


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def radial_separations(grid, shifts) -> np.ndarray:
    return np.array(
        [np.hypot(sx * grid.dx, sy * grid.dx) for sx, sy in shifts],
        dtype=float,
    )


def rel_median(values: np.ndarray, reference: np.ndarray) -> float:
    return float(np.median(np.abs(values - reference) / reference))


def fitted_slope(rho: np.ndarray, values: np.ndarray) -> float:
    return float(np.polyfit(np.log(rho), np.log(values), 1)[0])


def deterministic_values(grid, spec, directions, psd_grid, psd_fun, p_depth):
    values = {}
    for name, shifts in directions.items():
        values[name] = np.array(
            [
                deterministic_structure_function(
                    psd_grid,
                    psd_fun,
                    grid,
                    sx * grid.dx,
                    sy * grid.dx,
                    p_depth,
                )
                for sx, sy in shifts
            ],
            dtype=float,
        )
    return values


def generate_observables(
    grid,
    directions,
    psd_grid,
    psd_fun,
    p_depth,
    seed,
    basis,
) -> np.ndarray:
    layout = build_hermitian_layout(grid.n)
    rng = np.random.default_rng(seed)
    observables = np.empty((N_SCREENS, len(directions), 12), dtype=np.float64)

    for screen_id in range(N_SCREENS):
        base, _ = generate_base_phase_screen(psd_grid, grid, layout, rng)
        subharmonic = generate_subharmonic_phase(
            psd_fun,
            grid,
            p_depth,
            rng,
            basis=basis,
        )
        phase = base + subharmonic
        for direction_index, shifts in enumerate(directions.values()):
            observables[screen_id, direction_index] = [
                structure_function_valid_pairs(phase, sx, sy)
                for sx, sy in shifts
            ]
        if (screen_id + 1) % 64 == 0:
            print(f"P={p_depth}: {screen_id + 1}/{N_SCREENS}", flush=True)
    return observables


def bootstrap_summary(
    observables,
    deterministic,
    reference,
    grid,
    directions,
    seed,
) -> dict:
    # This is intentionally the same resampling structure as run_gate_b_formal.py.
    rng = np.random.default_rng(seed)
    weights = np.empty((B_BOOT, N_SCREENS), dtype=np.int16)
    for bootstrap_id in range(B_BOOT):
        sampled = rng.integers(0, N_SCREENS, N_SCREENS)
        weights[bootstrap_id] = np.bincount(sampled, minlength=N_SCREENS)

    summary = {}
    for direction_index, (name, shifts) in enumerate(directions.items()):
        values = observables[:, direction_index, :]
        point_mean = np.mean(values, axis=0)
        boot_means = weights @ values / N_SCREENS

        impl_statistics = np.median(
            np.abs(boot_means - deterministic[name]) / deterministic[name],
            axis=1,
        )
        amplitude_statistics = np.median(
            np.abs(boot_means - reference[name]) / reference[name],
            axis=1,
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
            "kolmogorov_amplitude": {
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


def save_observables(path, observables, grid, directions, p_depth, seeds):
    np.savez_compressed(
        path,
        D_phi_rad2=observables,
        screen_id=np.arange(N_SCREENS, dtype=np.int32),
        direction=np.asarray(list(directions), dtype="U2"),
        shift_pixels=np.asarray(list(directions.values()), dtype=np.int16),
        rho_m=np.stack(
            [radial_separations(grid, shifts) for shifts in directions.values()]
        ),
        screen_seed=np.asarray(seeds["screen"], dtype=np.int64),
        bootstrap_seed=np.asarray(seeds["bootstrap"], dtype=np.int64),
        p_depth=np.asarray(p_depth, dtype=np.int16),
    )


def run() -> dict:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    grid = make_centered_grid(N, DX)
    spec = PhaseScreenSpec()
    directions = frozen_direction_shifts()
    psd_grid = phase_psd_grid(grid, spec, "kolmogorov")
    psd_fun = lambda fx, fy: float(kolmogorov_phase_psd_cycles(fx, fy, spec))
    basis = precompute_subharmonic_basis(grid, max(P_VALUES))

    reference = {
        name: np.array(
            [
                kolmogorov_structure_reference(float(rho), spec)
                for rho in radial_separations(grid, shifts)
            ]
        )
        for name, shifts in directions.items()
    }

    metadata = {
        "diagnostic_only": True,
        "purpose": "post-P=6-failure remediation evidence; not formal qualification",
        "P_values": list(P_VALUES),
        "seeds": {str(p): SEEDS[p] for p in P_VALUES},
        "screens_per_P": N_SCREENS,
        "bootstrap_resamples": B_BOOT,
        "bootstrap_unit": "screen_id",
        "bootstrap_rule": (
            "one precomputed resample-count matrix per P, shared across x/y/45"
        ),
        "percentile_method": "numpy linear",
        "raw_phase_screens_saved": False,
        "grid": {"N": N, "dx_m": DX, "window_m": grid.window},
    }
    write_json(OUTPUT_DIR / "metadata.json", metadata)

    result = {"metadata": metadata, "P": {}}
    for p_depth in P_VALUES:
        deterministic = deterministic_values(
            grid, spec, directions, psd_grid, psd_fun, p_depth
        )
        observables = generate_observables(
            grid,
            directions,
            psd_grid,
            psd_fun,
            p_depth,
            SEEDS[p_depth]["screen"],
            basis,
        )
        save_observables(
            OUTPUT_DIR / f"p{p_depth}_screen_observables.npz",
            observables,
            grid,
            directions,
            p_depth,
            SEEDS[p_depth],
        )

        deterministic_summary = {}
        for name, shifts in directions.items():
            rho = radial_separations(grid, shifts)
            rel = np.abs(deterministic[name] - reference[name]) / reference[name]
            deterministic_summary[name] = {
                "median_relative_error": float(np.median(rel)),
                "max_relative_error": float(np.max(rel)),
                "slope": fitted_slope(rho, deterministic[name]),
            }

        result["P"][str(p_depth)] = {
            "deterministic": deterministic_summary,
            "bootstrap": bootstrap_summary(
                observables,
                deterministic,
                reference,
                grid,
                directions,
                SEEDS[p_depth]["bootstrap"],
            ),
        }

    write_json(OUTPUT_DIR / "diagnostic_summary.json", result)
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, ensure_ascii=False))
