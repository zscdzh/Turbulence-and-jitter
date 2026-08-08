#!/usr/bin/env python3
"""Run the frozen formal Gate-B V4-V5 empirical qualification.

The runner follows docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V02.md. It stores
only per-screen structure-function observables, never full phase screens.
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
P_LADDER = tuple(range(8))
P_GUARD = 0.08
SLOPE_GUARD = 0.08
FORMAL_ENSEMBLE = 512
DIAGNOSTIC_PREFIXES = (128, 256, 512)
B_BOOT = 2000

# These seeds are registered in metadata before any formal phase screen exists.
# Families are disjoint from Gate A (deterministic), V4, the core diagnostic,
# and any future production run.
SEEDS = {
    "v4_screen_seed": 2026080801,
    "finite_formal_screen_seed": 2026080811,
    "kolmogorov_formal_screen_seed": 2026080812,
    "finite_bootstrap_seed": 2026080813,
    "kolmogorov_bootstrap_seed": 2026080814,
}

OUTPUT_DIR = REPO_ROOT / "results" / "gate_b_v5_formal"
RESULT_DOC = REPO_ROOT / "docs" / "results" / "GATE_B_V4_V5_FORMAL_RESULTS.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def git_head() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
    ).strip()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def rel_median(values: np.ndarray, reference: np.ndarray) -> float:
    return float(np.median(np.abs(values - reference) / reference))


def radial_separations(grid, shifts) -> np.ndarray:
    return np.array(
        [np.hypot(sx * grid.dx, sy * grid.dx) for sx, sy in shifts],
        dtype=float,
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
            [
                kolmogorov_structure_reference(float(separation), spec)
                for separation in rho
            ]
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
            finite_error = rel_median(finite_values, finite_ref[name])
            kolm_error = rel_median(kolm_values, kolm_ref[name])
            kolm_slope = fitted_slope(rho, kolm_values)
            slope_error = abs(kolm_slope - 5.0 / 3.0)
            row["finite"][name] = {
                "median_relative_error": finite_error,
                "D_disc_rad2": finite_values.tolist(),
            }
            row["kolmogorov"][name] = {
                "median_relative_error": kolm_error,
                "slope": kolm_slope,
                "slope_error": slope_error,
                "D_disc_rad2": kolm_values.tolist(),
            }
            values_for_p["finite"][name] = finite_values
            values_for_p["kolmogorov"][name] = kolm_values
            passes &= finite_error <= P_GUARD
            passes &= kolm_error <= P_GUARD
            passes &= slope_error <= SLOPE_GUARD
        row["passes_8pct_guard"] = bool(passes)
        rows.append(row)
        values_by_p[p_depth] = values_for_p

    passing = [row["P"] for row in rows if row["passes_8pct_guard"]]
    if not passing:
        raise RuntimeError(
            "REVISE — LOW-FREQUENCY REPRESENTATION: no P<=7 passes."
        )
    p_star = min(passing)
    return rows, p_star, values_by_p[p_star], finite_grid, kolm_grid


def register_pre_run_metadata(spec, grid, directions) -> dict:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    metadata_path = OUTPUT_DIR / "metadata.json"
    if metadata_path.exists():
        prior = json.loads(metadata_path.read_text(encoding="utf-8"))
        if prior.get("seeds") != SEEDS:
            raise RuntimeError(
                "Existing formal metadata uses different seeds; refusing to replace it."
            )
    metadata = {
        "contract": "Numerical Implementation Contract v0.2 / Gate B",
        "run_state": "seeds_registered_before_formal_screen_generation",
        "registered_utc": utc_now(),
        "git_sha_at_run_start": git_head(),
        "seeds": SEEDS,
        "formal_ensemble": FORMAL_ENSEMBLE,
        "diagnostic_prefixes": list(DIAGNOSTIC_PREFIXES),
        "bootstrap_resamples": B_BOOT,
        "bootstrap_unit": "screen_id",
        "percentile_method": "numpy linear",
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
            "df_cycles_per_m": 1.0 / grid.window,
        },
        "directions": {
            name: [list(shift) for shift in shifts]
            for name, shifts in directions.items()
        },
        "raw_phase_screens_saved": False,
    }
    write_json(metadata_path, metadata)
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
        if (screen_id + 1) % 32 == 0:
            print(
                f"{label}: generated {screen_id + 1}/{FORMAL_ENSEMBLE} screens",
                flush=True,
            )
    return observables


def save_observables(
    path, observables, grid, directions, case, seed, p_depth
):
    direction_names = np.asarray(list(directions), dtype="U2")
    shift_pixels = np.array(list(directions.values()), dtype=np.int16)
    rho_m = np.stack(
        [radial_separations(grid, shifts) for shifts in directions.values()]
    )
    np.savez_compressed(
        path,
        D_phi_rad2=observables,
        screen_id=np.arange(FORMAL_ENSEMBLE, dtype=np.int32),
        case=np.asarray(case),
        direction=direction_names,
        shift_pixels=shift_pixels,
        rho_m=rho_m,
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
            np.abs(boot_means - deterministic[name]) / deterministic[name],
            axis=1,
        )
        continuous_statistics = np.median(
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
                    np.percentile(continuous_statistics, 95.0)
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


def pct(value: float) -> str:
    return f"{100.0 * value:.3f}%"


def markdown_report(
    metadata,
    v4,
    ladder,
    p_star,
    convergence,
    bootstrap,
    decision,
):
    all_pass = decision.startswith("PASS")
    lines = [
        "# Gate B V4–V5 Formal Empirical Qualification",
        "",
        f"**运行日期：** {metadata['registered_utc'][:10]}",
        "**权威合同：** `docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V02.md`",
        f"**最终裁决：** **{decision}**",
        "",
        "## 1. 负责人摘要",
        "",
        "本轮用于回答冻结的单屏 phase-screen generator 是否在频谱归一化、低频补偿和空间结构函数三个层面通过 V4–V5 absolute qualification。实际测试包含 128-screen V4、完整 P=0–7 deterministic ladder、finite/Kolmogorov 各 512 个独立 screens、nested 128/256/512 点估计，以及按 screen ID 重采样的 2000 次 bootstrap。",
        "",
        f"最终结果：**{decision}**。",
        "",
        (
            "本结果只允许项目进入 V6–V8 implementation review；V6 本身仍未授权，必须等待项目负责人另行决定。"
            if all_pass
            else "Gate B 尚未合格，不允许进入 V6，必须先修订 phase-screen implementation。"
        ),
        "",
        "## 2. 数学定义",
        "",
        "- `S_phi(fx,fy)`：以 cycles/m 为频率坐标、与 `dfx dfy` 配套的二维相位 PSD，单位 `rad² m²`。",
        "- `a_uv`：离散 Fourier cell 的复随机系数，满足 `E|a_uv|²=S_phi df²`，单位 rad。",
        "- `D_disc,P(rho)`：base FFT 加 P 层 subharmonics 的精确离散期望结构函数，单位 `rad²`。",
        "- `D_emp(rho)`：逐 screen 用 non-wrapped valid pairs 计算后再作 ensemble mean 的经验结构函数，单位 `rad²`。",
        "- `D_finite,ref(rho)`：独立 atmospheric-measure 连续积分得到的 finite-scale reference，单位 `rad²`。",
        "- `D_K(rho)=6.88(rho/r0_screen)^(5/3)`：解析 Kolmogorov absolute reference，单位 `rad²`。",
        "- `P_*`：P=0–7 中同时通过三方向 8% amplitude guard 与 0.08 slope guard 的最小 subharmonic depth。",
        "- bootstrap 95% UB：2000 个 screen-ID bootstrap statistics 的第 95 百分位；slope 95% CI 为第 2.5–97.5 百分位。",
        "",
        "## 3. 关键代码链",
        "",
        "`finite_phase_psd_cycles` / `kolmogorov_phase_psd_cycles` → `generate_base_fourier_coefficients` → `build_hermitian_layout` → `ifft2c` phase screen → `generate_subharmonic_phase` → `structure_function_valid_pairs` → per-screen `D_phi` observable → ensemble mean → `bootstrap_case` → frozen PASS/FAIL rules。",
        "",
        "## 4. 实际结果",
        "",
        "### V4",
        "",
        "| metric | numerical | target / limit | result |",
        "|---|---:|---:|:---:|",
        f"| median annular PSD level error | {pct(v4['median_level_relative_error'])} | <=10% | {'PASS' if v4['median_level_relative_error'] <= 0.10 else 'FAIL'} |",
        f"| log-log slope | {v4['slope_numerical']:.6f} | target {v4['slope_target']:.6f} | — |",
        f"| slope difference | {v4['slope_difference']:.6f} | <=0.10 | {'PASS' if v4['slope_difference'] <= 0.10 else 'FAIL'} |",
        "",
        "### Deterministic P ladder",
        "",
        "| P | finite x | finite y | finite 45° | K x | K y | K 45° | K slope x | K slope y | K slope 45° | guard |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|",
    ]
    for row in ladder:
        lines.append(
            "| {P} | {fx} | {fy} | {f45} | {kx} | {ky} | {k45} | {sx:.5f} | {sy:.5f} | {s45:.5f} | {guard} |".format(
                P=row["P"],
                fx=pct(row["finite"]["x"]["median_relative_error"]),
                fy=pct(row["finite"]["y"]["median_relative_error"]),
                f45=pct(row["finite"]["45"]["median_relative_error"]),
                kx=pct(row["kolmogorov"]["x"]["median_relative_error"]),
                ky=pct(row["kolmogorov"]["y"]["median_relative_error"]),
                k45=pct(row["kolmogorov"]["45"]["median_relative_error"]),
                sx=row["kolmogorov"]["x"]["slope"],
                sy=row["kolmogorov"]["y"]["slope"],
                s45=row["kolmogorov"]["45"]["slope"],
                guard=("SELECTED" if row["P"] == p_star else ("PASS" if row["passes_8pct_guard"] else "FAIL")),
            )
        )
    lines.extend(
        [
            "",
            f"实际计算选择最小通过值 `P_*={p_star}`；该值不是输入参数。",
            "",
            "### Empirical convergence（128/256 仅 diagnostic）",
            "",
            "| case | N | direction | implementation error | continuous-reference error | fitted slope |",
            "|---|---:|:---:|---:|---:|---:|",
        ]
    )
    for case in ("finite", "kolmogorov"):
        for n in DIAGNOSTIC_PREFIXES:
            for name in ("x", "y", "45"):
                row = convergence[case][str(n)][name]
                lines.append(
                    f"| {case} | {n} | {name} | {pct(row['implementation_recovery_median_relative_error'])} | {pct(row['continuous_reference_median_relative_error'])} | {row['fitted_slope']:.5f} |"
                )
    lines.extend(
        [
            "",
            "### Formal 512-screen bootstrap",
            "",
            "| case | direction | impl point | impl 95% UB | amplitude point | amplitude 95% UB | slope point | slope 95% CI | result |",
            "|---|:---:|---:|---:|---:|---:|---:|---:|:---:|",
        ]
    )
    for case in ("finite", "kolmogorov"):
        for name in ("x", "y", "45"):
            row = bootstrap[case][name]
            impl = row["implementation_recovery"]
            amplitude = row["continuous_amplitude"]
            slope = row["slope"]
            slope_low, slope_high = slope["bootstrap_95pct_interval"]
            row_pass = impl["bootstrap_95pct_upper_bound"] <= 0.05
            row_pass &= amplitude["bootstrap_95pct_upper_bound"] <= 0.10
            if case == "kolmogorov":
                row_pass &= slope_low >= 5.0 / 3.0 - 0.10
                row_pass &= slope_high <= 5.0 / 3.0 + 0.10
            lines.append(
                f"| {case} | {name} | {pct(impl['point_estimate'])} | {pct(impl['bootstrap_95pct_upper_bound'])} | {pct(amplitude['point_estimate'])} | {pct(amplitude['bootstrap_95pct_upper_bound'])} | {slope['point_estimate']:.5f} | [{slope_low:.5f}, {slope_high:.5f}] | {'PASS' if row_pass else 'FAIL'} |"
            )
    lines.extend(
        [
            "",
            "finite slope 仅为 diagnostic；冻结的 formal slope criterion 只适用于 Kolmogorov case。",
            "",
            "## 5. 证据入口",
            "",
            "- 权威合同：`docs/SCIENTIFIC_CONTRACT_DRAFT.md`、`docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V01.md`、`docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V02.md`。",
            "- 代码：`src/turbulence_jitter/gate_b.py`、`scripts/run_gate_b_core.py`、`scripts/run_gate_b_formal.py`。",
            f"- seeds：`{json.dumps(SEEDS, sort_keys=True)}`；均在 formal screens 生成前写入 `metadata.json`。",
            "- 机器结果：`results/gate_b_v5_formal/metadata.json`、`deterministic_ladder.json`、`v4_summary.json`、两份 `*_screen_observables.npz`、`bootstrap_summary.json`。",
            f"- 运行起始 commit SHA：`{metadata['git_sha_at_run_start']}`；Draft PR #5。",
            "",
            "## 6. 结论边界",
            "",
            "- 已支持：V4 base-FFT PSD absolute level/slope；deterministic low-frequency depth；V5 empirical implementation recovery；finite-scale 与 Kolmogorov screen-level structure-function amplitude；Kolmogorov slope。",
            "- 部分支持：仅在冻结的 512×512 qualification slab、冻结 separation points 和本次预注册 ensembles 上支持。",
            "- 仍开放：V6–V12 propagation-level beam wander、long-term radius、scintillation、screen-number、production grid 与 split-step validation。",
            "- 禁止宣称：完整 turbulence simulation 已正确、production multi-screen 已收敛、structured fields 已实现或任何 beam family 已获得性能优势。",
            "",
            "## 7. 项目决策",
            "",
            (
                "**CONTINUE — GATE B QUALIFIED; WAIT FOR AUTHORIZATION BEFORE V6**"
                if all_pass
                else "**REVISE — GATE B NOT YET QUALIFIED**"
            ),
            "",
        ]
    )
    RESULT_DOC.write_text("\n".join(lines), encoding="utf-8")


def run() -> dict:
    spec = PhaseScreenSpec()
    grid = make_centered_grid(N, DX)
    directions = frozen_direction_shifts()
    metadata = register_pre_run_metadata(spec, grid, directions)
    print("Formal seeds registered in metadata before screen generation.", flush=True)

    v4 = qualify_v4_psd(grid, spec, V4_ENSEMBLE, SEEDS["v4_screen_seed"])
    write_json(OUTPUT_DIR / "v4_summary.json", v4)
    if v4["median_level_relative_error"] > 0.10:
        raise RuntimeError("REVISE — PHASE-SCREEN IMPLEMENTATION: V4 level FAIL.")
    if v4["slope_difference"] > 0.10:
        raise RuntimeError("REVISE — PHASE-SCREEN IMPLEMENTATION: V4 slope FAIL.")

    finite_ref, kolm_ref, quadrature_check = continuous_references(
        grid, spec, directions
    )
    if max(quadrature_check.values()) >= 1e-4:
        raise RuntimeError("Continuous finite reference failed 1e-4 convergence.")

    ladder, p_star, selected, finite_grid, kolm_grid = deterministic_ladder(
        grid, spec, directions, finite_ref, kolm_ref
    )
    ladder_payload = {
        "P_guard": P_GUARD,
        "slope_guard": SLOPE_GUARD,
        "P_star": p_star,
        "quadrature_max_relative_change": quadrature_check,
        "rho_m": {
            name: radial_separations(grid, shifts).tolist()
            for name, shifts in directions.items()
        },
        "finite_reference_rad2": {
            name: values.tolist() for name, values in finite_ref.items()
        },
        "kolmogorov_reference_rad2": {
            name: values.tolist() for name, values in kolm_ref.items()
        },
        "ladder": ladder,
    }
    write_json(OUTPUT_DIR / "deterministic_ladder.json", ladder_payload)

    basis = precompute_subharmonic_basis(grid, p_star)
    finite_fun = lambda fx, fy: float(finite_phase_psd_cycles(fx, fy, spec))
    kolm_fun = lambda fx, fy: float(kolmogorov_phase_psd_cycles(fx, fy, spec))
    finite_observables = generate_observables(
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
        finite_observables,
        grid,
        directions,
        "finite",
        SEEDS["finite_formal_screen_seed"],
        p_star,
    )
    kolm_observables = generate_observables(
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
        kolm_observables,
        grid,
        directions,
        "kolmogorov",
        SEEDS["kolmogorov_formal_screen_seed"],
        p_star,
    )

    convergence = {"finite": {}, "kolmogorov": {}}
    for prefix in DIAGNOSTIC_PREFIXES:
        convergence["finite"][str(prefix)] = point_summary(
            finite_observables,
            selected["finite"],
            finite_ref,
            grid,
            directions,
            prefix,
        )
        convergence["kolmogorov"][str(prefix)] = point_summary(
            kolm_observables,
            selected["kolmogorov"],
            kolm_ref,
            grid,
            directions,
            prefix,
        )

    bootstrap = {
        "finite": bootstrap_case(
            finite_observables,
            selected["finite"],
            finite_ref,
            grid,
            directions,
            SEEDS["finite_bootstrap_seed"],
        ),
        "kolmogorov": bootstrap_case(
            kolm_observables,
            selected["kolmogorov"],
            kolm_ref,
            grid,
            directions,
            SEEDS["kolmogorov_bootstrap_seed"],
        ),
    }

    formal_pass = True
    for name in directions:
        finite_row = bootstrap["finite"][name]
        kolm_row = bootstrap["kolmogorov"][name]
        formal_pass &= (
            finite_row["implementation_recovery"][
                "bootstrap_95pct_upper_bound"
            ]
            <= 0.05
        )
        formal_pass &= (
            finite_row["continuous_amplitude"][
                "bootstrap_95pct_upper_bound"
            ]
            <= 0.10
        )
        formal_pass &= (
            kolm_row["implementation_recovery"][
                "bootstrap_95pct_upper_bound"
            ]
            <= 0.05
        )
        formal_pass &= (
            kolm_row["continuous_amplitude"][
                "bootstrap_95pct_upper_bound"
            ]
            <= 0.10
        )
        slope_low, slope_high = kolm_row["slope"][
            "bootstrap_95pct_interval"
        ]
        formal_pass &= slope_low >= 5.0 / 3.0 - 0.10
        formal_pass &= slope_high <= 5.0 / 3.0 + 0.10

    decision = (
        "PASS — GATE B V4–V5 QUALIFIED"
        if formal_pass
        else "REVISE — PHASE-SCREEN IMPLEMENTATION"
    )
    bootstrap_payload = {
        "formal_ensemble": FORMAL_ENSEMBLE,
        "bootstrap_resamples": B_BOOT,
        "bootstrap_unit": "screen_id",
        "diagnostic_convergence": convergence,
        "formal_bootstrap": bootstrap,
        "decision": decision,
    }
    write_json(OUTPUT_DIR / "bootstrap_summary.json", bootstrap_payload)

    metadata.update(
        {
            "run_state": "completed",
            "completed_utc": utc_now(),
            "P_star": p_star,
            "decision": decision,
        }
    )
    write_json(OUTPUT_DIR / "metadata.json", metadata)
    markdown_report(
        metadata,
        v4,
        ladder,
        p_star,
        convergence,
        bootstrap,
        decision,
    )
    result = {
        "decision": decision,
        "P_star": p_star,
        "V4": {
            "median_level_relative_error": v4[
                "median_level_relative_error"
            ],
            "slope_difference": v4["slope_difference"],
        },
        "bootstrap": bootstrap,
    }
    print(json.dumps(result, indent=2), flush=True)
    return result


if __name__ == "__main__":
    run()
