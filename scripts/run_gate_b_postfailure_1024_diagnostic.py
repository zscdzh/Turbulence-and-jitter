#!/usr/bin/env python3
"""Reproduce the post-failure 1024-screen Gate-B v0.2.1 diagnostic.

DIAGNOSTIC ONLY. This script deliberately continues the *historical failed*
Kolmogorov v0.2.1 RNG sequence (screen seed 2026080832) from its first 512
screens to 1024 cumulative screens. It does not qualify Gate B and must never
be used as the fresh v0.2.2 formal run.

The bootstrap implementation is intentionally isomorphic to the v0.2.1 formal
runner: one screen-ID resample-weight matrix is shared across x/y/45 degrees.
"""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import platform
import subprocess
import sys

import numpy as np
import scipy

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import run_gate_b_formal_v021 as v021  # noqa: E402
from turbulence_jitter.gate_a import make_centered_grid  # noqa: E402
from turbulence_jitter.gate_b import (  # noqa: E402
    PhaseScreenSpec,
    build_hermitian_layout,
    frozen_direction_shifts,
    generate_base_phase_screen,
    generate_subharmonic_phase,
    kolmogorov_phase_psd_cycles,
    phase_psd_grid,
    precompute_subharmonic_basis,
    structure_function_valid_pairs,
)

N_DIAGNOSTIC = 1024
PREFIXES = (512, 640, 768, 896, 1024)
SCREEN_SEED = 2026080832
BOOTSTRAP_SEED = 2026080841
B_BOOT = 2000
EXPECTED_P_STAR = 9

OUTPUT_DIR = REPO_ROOT / "results" / "gate_b_v5_formal_v021" / "postfailure_1024_diagnostic"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def git_output(*args: str) -> str:
    try:
        return subprocess.check_output(
            ["git", *args], cwd=REPO_ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        return "UNAVAILABLE"


def source_hash(path: Path) -> str:
    return git_output("hash-object", str(path.relative_to(REPO_ROOT)))


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def generate_kolmogorov_observables(
    grid,
    directions,
    psd_grid,
    p_depth: int,
    basis,
) -> np.ndarray:
    layout = build_hermitian_layout(grid.n)
    rng = np.random.default_rng(SCREEN_SEED)
    psd_fun = lambda fx, fy: float(kolmogorov_phase_psd_cycles(fx, fy, PhaseScreenSpec()))
    observables = np.empty((N_DIAGNOSTIC, len(directions), 12), dtype=np.float64)

    for screen_id in range(N_DIAGNOSTIC):
        base, _ = generate_base_phase_screen(psd_grid, grid, layout, rng)
        subharmonic = generate_subharmonic_phase(
            psd_fun, grid, p_depth, rng, basis=basis
        )
        phase = base + subharmonic
        for direction_index, shifts in enumerate(directions.values()):
            observables[screen_id, direction_index] = [
                structure_function_valid_pairs(phase, sx, sy) for sx, sy in shifts
            ]
        if (screen_id + 1) % 128 == 0:
            print(f"kolmogorov diagnostic: {screen_id + 1}/{N_DIAGNOSTIC}", flush=True)
    return observables


def bootstrap_1024(observables, deterministic, reference, grid, directions) -> dict:
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    weights = np.empty((B_BOOT, N_DIAGNOSTIC), dtype=np.int16)
    for bootstrap_id in range(B_BOOT):
        sampled = rng.integers(0, N_DIAGNOSTIC, N_DIAGNOSTIC)
        weights[bootstrap_id] = np.bincount(sampled, minlength=N_DIAGNOSTIC)

    summary = {}
    for direction_index, (name, shifts) in enumerate(directions.items()):
        values = observables[:, direction_index, :]
        point_mean = np.mean(values, axis=0)
        boot_means = weights @ values / N_DIAGNOSTIC

        impl_statistics = np.median(
            np.abs(boot_means - deterministic[name]) / deterministic[name], axis=1
        )
        amplitude_statistics = np.median(
            np.abs(boot_means - reference[name]) / reference[name], axis=1
        )
        rho = v021.radial_separations(grid, shifts)
        log_rho_centered = np.log(rho) - np.mean(np.log(rho))
        slope_denominator = np.sum(log_rho_centered**2)
        slopes = np.log(boot_means) @ log_rho_centered / slope_denominator

        summary[name] = {
            "implementation_recovery": {
                "point_estimate": v021.rel_median(point_mean, deterministic[name]),
                "bootstrap_95pct_upper_bound": float(np.percentile(impl_statistics, 95.0)),
            },
            "continuous_amplitude": {
                "point_estimate": v021.rel_median(point_mean, reference[name]),
                "bootstrap_95pct_upper_bound": float(np.percentile(amplitude_statistics, 95.0)),
            },
            "slope": {
                "point_estimate": v021.fitted_slope(rho, point_mean),
                "bootstrap_95pct_interval": [
                    float(np.percentile(slopes, 2.5)),
                    float(np.percentile(slopes, 97.5)),
                ],
            },
        }
    return summary


def run() -> dict:
    spec = PhaseScreenSpec()
    grid = make_centered_grid(v021.N, v021.DX)
    directions = frozen_direction_shifts()

    finite_ref, kolm_ref, quad_check = v021.continuous_references(grid, spec, directions)
    ladder, p_star, selected, _, kolm_grid = v021.deterministic_ladder(
        grid, spec, directions, finite_ref, kolm_ref
    )
    if p_star != EXPECTED_P_STAR:
        raise RuntimeError(f"Expected historical v0.2.1 P*=9, got P*={p_star}.")

    metadata = {
        "status": "DIAGNOSTIC ONLY — NOT FORMAL QUALIFICATION",
        "purpose": "reproduce the same-seed post-failure 512->1024 Kolmogorov continuation",
        "created_utc": utc_now(),
        "git_head": git_output("rev-parse", "HEAD"),
        "source_hashes": {
            "this_runner": source_hash(Path(__file__)),
            "formal_v021_runner": source_hash(REPO_ROOT / "scripts" / "run_gate_b_formal_v021.py"),
            "gate_b": source_hash(REPO_ROOT / "src" / "turbulence_jitter" / "gate_b.py"),
            "gate_a": source_hash(REPO_ROOT / "src" / "turbulence_jitter" / "gate_a.py"),
        },
        "environment": {
            "python": sys.version,
            "python_implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "P_star": p_star,
        "screen_seed": SCREEN_SEED,
        "bootstrap_seed": BOOTSTRAP_SEED,
        "screen_count": N_DIAGNOSTIC,
        "prefixes": list(PREFIXES),
        "bootstrap_resamples": B_BOOT,
        "bootstrap_unit": "screen_id",
        "bootstrap_rule": "shared resample-count weights across directions",
        "percentile_method": "numpy linear",
        "historical_first_512_are_the_failed_formal_sequence": True,
        "may_be_used_as_formal_v022_evidence": False,
        "quadrature_check": quad_check,
    }
    write_json(OUTPUT_DIR / "metadata.json", metadata)

    basis = precompute_subharmonic_basis(grid, p_star)
    observations = generate_kolmogorov_observables(
        grid, directions, kolm_grid, p_star, basis
    )
    np.savez_compressed(
        OUTPUT_DIR / "kolmogorov_screen_observables_1024.npz",
        D_phi_rad2=observations,
        screen_id=np.arange(N_DIAGNOSTIC, dtype=np.int32),
        direction=np.asarray(list(directions), dtype="U2"),
        shift_pixels=np.asarray(list(directions.values()), dtype=np.int16),
        rho_m=np.stack([v021.radial_separations(grid, s) for s in directions.values()]),
        screen_seed=np.asarray(SCREEN_SEED, dtype=np.int64),
        p_depth=np.asarray(p_star, dtype=np.int16),
    )

    prefix_summary = {}
    for n in PREFIXES:
        prefix_summary[str(n)] = v021.point_summary(
            observations, selected["kolmogorov"], kolm_ref, grid, directions, n
        )

    boot = bootstrap_1024(
        observations, selected["kolmogorov"], kolm_ref, grid, directions
    )
    summary = {
        "status": "DIAGNOSTIC ONLY — NOT FORMAL QUALIFICATION",
        "P_star": p_star,
        "screen_seed": SCREEN_SEED,
        "bootstrap_seed": BOOTSTRAP_SEED,
        "prefix_summary": prefix_summary,
        "bootstrap_1024": boot,
    }
    write_json(OUTPUT_DIR / "summary.json", summary)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return summary


if __name__ == "__main__":
    run()
