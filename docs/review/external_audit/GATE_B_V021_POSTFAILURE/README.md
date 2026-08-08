# Gate B External-Audit History and v0.2.2 Outcome

**日期：2026-08-08**  
**历史审计对象：Gate B v0.2.1 post-failure remediation**  
**最新正式结果：PASS — GATE B V4–V5 QUALIFIED**  
**V6：CLOSED pending project-lead/final review authorization**

本目录最初用于审查 v0.2.1 的 512-screen post-failure ensemble 问题。该审查最终支持 Option A：冻结一次性 `N_ens=1024` v0.2.2 remediation，不修改 low-frequency generator。

## Historical chain

1. v0.2 / `P*=6`：Kolmogorov y/45° amplitude formal FAIL；
2. v0.2.1：deterministic policy 修订后自动选择 `P*=9`，但 fresh 512-screen Kolmogorov x recovery/amplitude formal FAIL；
3. post-failure same-seed 1024 continuation：diagnostic only，支持 ensemble-size remediation；
4. 外审要求补齐 diagnostic runner 与一次性止损规则；
5. `docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V022.md` 冻结唯一 fresh 1024 formal rerun；
6. fresh v0.2.2 1024-screen formal rerun：**全部 V4/V5 gates PASS**。

## Latest formal evidence

- `docs/results/GATE_B_V4_V5_FORMAL_V022_RESULTS.md`
- `results/gate_b_v5_formal_v022/bootstrap_summary.json`
- `results/gate_b_v5_formal_v022/metadata.json`
- `results/gate_b_v5_formal_v022/deterministic_selection_summary.json`
- `scripts/run_gate_b_formal_v022.py`
- `docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V022.md`

## Historical evidence retained

- `docs/results/GATE_B_V4_V5_FORMAL_RESULTS.md` — v0.2 / P=6 FAIL；
- `docs/results/GATE_B_V4_V5_FORMAL_V021_RESULTS.md` — v0.2.1 / 512 FAIL；
- `docs/review/GATE_B_V021_POSTFAILURE_ENSEMBLE_REVIEW_PROPOSAL.md`；
- `results/gate_b_v5_formal_v021/postfailure_1024_bootstrap2000.json` — diagnostic only；
- `scripts/run_gate_b_postfailure_1024_diagnostic.py`。

历史失败不得被删除或解释为无效；它们构成 remediation policy 的审计链。

## Current boundary

最新 formal result 支持 screen-level Gate B V4–V5 qualification。它不自动支持 V6 beam wander、V7 long-term radius、V8 scintillation、production multi-screen convergence 或 structured-field comparisons。

> **Current state: GATE B V4–V5 QUALIFIED; V6 awaits explicit authorization.**
