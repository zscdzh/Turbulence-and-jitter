#!/usr/bin/env python3
"""Run the one-shot fresh Gate-B v0.2.2 1024-screen formal V5 rerun.

Authorized by docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V022.md.

This runner freezes exactly one fresh seed family before any v0.2.2 formal
screen is generated. Prefixes are diagnostic only. Formal PASS/FAIL uses the
full 1024-screen ensemble. If the fresh 1024 run fails, the contract forbids
seed replacement or escalation to larger ensembles.
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
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import run_gate_b_formal_v021 as v021  # noqa: E402
from turbulence_jitter.gate_a import make_centered_grid  # noqa: E402
from turbulence_jitter.gate_b import (  # noqa: E402
    PhaseScreenSpec,
    build_hermitian_layout,
    finite_phase_psd_cycles,
    frozen_direction_shifts,
    generate_base_phase_screen,
    generate_subharmonic_phase,
    kolmogorov_phase_psd_cycles,
    precompute_subharmonic_basis,
    qualify_v4_psd,
    structure_function_valid_pairs,
)

FORMAL_ENSEMBLE = 1024
DIAGNOSTIC_PREFIXES = (256, 512, 768, 1024)
B_BOOT = 2000

# ONE-SHOT v0.2.2 formal family. These values are committed before any v0.2.2
# formal screen generation and may not be changed after observing results.
SEEDS = {
    "v4_screen_seed": 2026080860,
    "finite_formal_screen_seed": 2026080861,
    "kolmogorov_formal_screen_seed": 2026080862,
    "finite_bootstrap_seed": 2026080863,
    "kolmogorov_bootstrap_seed": 2026080864,
}

OUTPUT_DIR = REPO_ROOT / "results" / "gate_b_v5_formal_v022"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def git_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
        ).strip()
    except Exception:
        return "UNAVAILABLE"


def git_blob(path: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "hash-object", str(path.relative_to(REPO_ROOT))],
            cwd=REPO_ROOT,
            text=True,
        ).strip()
    except Exception:
        return "UNAVAILABLE"


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def register_pre_run_metadata(spec, grid, directions) -> dict:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / "metadata.json"
    if path.exists():
        prior = json.loads(path.read_text(encoding="utf-8"))
        if prior.get("seeds") != SEEDS:
            raise RuntimeError(
                "Existing v0.2.2 metadata uses a different seed family; stop-loss rule forbids replacement."
            )
        if prior.get("run_state") not in {
            "seeds_registered_before_formal_screen_generation",
            "formal_v022_completed",
        }:
            raise RuntimeError("Unexpected existing v0.2.2 metadata state.")

    metadata = {
        "contract": "Numerical Implementation Contract v0.2.2 / Gate B",
        "contract_path": "docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V022.md",
        "run_state": "seeds_registered_before_formal_screen_generation",
        "registered_utc": utc_now(),
        "git_sha_at_run_start": git_head(),
        "runner_blob_sha": git_blob(Path(__file__)),
        "seeds": SEEDS,
        "one_shot_seed_family": True,
        "seed_replacement_after_result_forbidden": True,
        "ensemble_escalation_after_failure_forbidden": True,
        "historical_v02_p6_failure_preserved": True,
        "historical_v021_512_failure_preserved": True,
        "historical_v021_postfailure_1024_diagnostic_preserved": True,
        "formal_ensemble": FORMAL_ENSEMBLE,
        "diagnostic_prefixes": list(DIAGNOSTIC_PREFIXES),
        "bootstrap_resamples": B_BOOT,
        "bootstrap_unit": "screen_id",
        "bootstrap_rule": "shared resample-count weights across directions per case",
        "percentile_method": "numpy linear",
        "selection": {
            "P_ladder": list(v021.P_LADDER),
            "median_guard": v021.MEDIAN_GUARD,
            "pointwise_guard": v021.POINTWISE_GUARD,
            "slope_guard": v021.SLOPE_GUARD,
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
    observables = np.empty((FORMAL_ENSEMBLE, len(directions), 12), dtype=np.float64)
    for screen_id in range(FORMAL_ENSEMBLE):
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
            [v021.radial_separations(grid, shifts) for shifts in directions.values()]
        ),
        screen_seed=np.asarray(seed, dtype=np.int64),
        p_depth=np.asarray(p_depth, dtype=np.int16),
    )


def bootstrap_case(observables, deterministic, reference, grid, directions, seed):
    rng = np.random.default_rng(seed)
    weights = np.empty((B_BOOT, FORMAL_ENSEMBLE), dtype=np.int16)
    for bootstrap_id in range(B_BOOT):
        sampled = rng.integers(0, FORMAL_ENSEMBLE, FORMAL_ENSEMBLE)
        weights[bootstrap_id] = np.bincount(sampled, minlength=FORMAL_ENSEMBLE)

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
    grid = make_centered_grid(v021.N, v021.DX)
    directions = frozen_direction_shifts()

    # This write occurs before any v0.2.2 formal screen is generated.
    metadata = register_pre_run_metadata(spec, grid, directions)

    v4 = qualify_v4_psd(grid, spec, v021.V4_ENSEMBLE, SEEDS["v4_screen_seed"])
    if v4["median_level_relative_error"] > 0.10 or v4["slope_difference"] > 0.10:
        raise RuntimeError("REVISE — V4 regression sanity failed.")

    finite_ref, kolm_ref, quad_check = v021.continuous_references(grid, spec, directions)
    if max(quad_check.values()) >= 1e-4:
        raise RuntimeError("Independent finite-scale reference failed convergence.")

    ladder, p_star, selected, finite_grid, kolm_grid = v021.deterministic_ladder(
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
        convergence["finite"][str(n)] = v021.point_summary(
            finite_obs, selected["finite"], finite_ref, grid, directions, n
        )
        convergence["kolmogorov"][str(n)] = v021.point_summary(
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
        else "REVISE — GATE B NOT QUALIFIED AFTER v0.2.2 ENSEMBLE REMEDIATION"
    )

    summary = {
        "contract": "Numerical Implementation Contract v0.2.2 / Gate B",
        "metadata": metadata,
        "V4": v4,
        "P_star": p_star,
        "convergence": convergence,
        "formal_bootstrap": {"finite": finite_boot, "kolmogorov": kolm_boot},
        "decision": decision,
        "v6_authorized": False,
        "stop_loss_if_failed": (
            "No seed replacement and no ensemble escalation; review low-frequency representation / qualification statistic."
        ),
    }
    write_json(OUTPUT_DIR / "bootstrap_summary.json", summary)

    metadata["run_state"] = "formal_v022_completed"
    metadata["P_star"] = p_star
    metadata["decision"] = decision
    metadata["completed_utc"] = utc_now()
    write_json(OUTPUT_DIR / "metadata.json", metadata)

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return summary


if __name__ == "__main__":
    run()
