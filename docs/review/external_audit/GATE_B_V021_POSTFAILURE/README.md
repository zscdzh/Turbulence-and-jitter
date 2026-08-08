# Gate B v0.2.1 Post-Failure External Audit Package

**日期：2026-08-08**  
**审计状态：CLOSED — OPTION A SUPPORTED**  
**remediation decision：PASS — AUTHORIZE N_ens=1024 GATE-B v0.2.2 REMEDIATION**  
**Gate B qualification：NOT YET QUALIFIED**  
**V6：CLOSED**

本目录保留 v0.2.1 post-failure 外部审计的完整入口。外审最终实质支持 Option A，但要求补齐两个程序性条件；两项现已关闭。

## 1. 原主审查材料

- `docs/review/GATE_B_V021_POSTFAILURE_ENSEMBLE_REVIEW_PROPOSAL.md`
  - 审查 formal ensemble 是否由 512 提高到 1024，或修改 low-frequency representation。
  - 包含 v0.2 / P=6 failure、v0.2.1 remediation、P*=9 fresh 512-screen failure 与 post-failure 1024 convergence diagnostic。

## 2. v0.2.1 正式结果

- `docs/results/GATE_B_V4_V5_FORMAL_V021_RESULTS.md`
  - fresh 512-screen + 2000-bootstrap 结果；正式结果保持 `REVISE — GATE B NOT YET QUALIFIED`。

## 3. 1024 post-failure diagnostic 可复现入口

新增并冻结：

- `scripts/run_gate_b_postfailure_1024_diagnostic.py`
- `results/gate_b_v5_formal_v021/postfailure_1024_diagnostic/metadata.json`
- `results/gate_b_v5_formal_v021/postfailure_1024_diagnostic/summary.json`

该 runner 使用历史失败序列：

- screen seed `2026080832`；
- bootstrap seed `2026080841`；
- 1024 cumulative screens；
- 2000 screen-ID bootstrap；
- x/y/45° 共享同一套 resample-count weights。

它只用于复现历史 post-failure diagnostic，不能作为 v0.2.2 formal evidence。

## 4. 机器统计摘要

- `results/gate_b_v5_formal_v021/bootstrap_summary.json`
- `results/gate_b_v5_formal_v021/postfailure_1024_bootstrap2000.json`
- `results/gate_b_v5_formal_v021/deterministic_ladder.json`
- `results/gate_b_v5_formal_v021/metadata.json`
- `results/gate_b_v5_formal_v021/v4_summary.json`

## 5. 审计后新的权威治理

`main` 已新增：

- `docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V022.md`
- `docs/review/GATE_B_V022_ENSEMBLE_REMEDIATION_DECISION.md`

v0.2.2 冻结：

- 唯一 formal ensemble `N_ens=1024`；
- `B_boot=2000` 与所有 v0.2.1 thresholds 不变；
- P-selection 保持 minimum-depth deterministic bias-headroom policy；
- 只允许一套全新预注册 1024-screen formal seeds；
- 若 fresh 1024 FAIL，禁止换 seed 或扩大到 2048，必须转入 low-frequency representation / qualification-statistic review；
- V6 在 Gate B 正式 PASS 前继续关闭。

## 6. v0.2.2 formal runner — prepared, not executed here

PR 分支已准备：

- `scripts/run_gate_b_formal_v022.py`

其唯一 fresh seed family 已在运行前提交冻结：

- V4 `2026080860`；
- finite screen/bootstrap `2026080861 / 2026080863`；
- Kolmogorov screen/bootstrap `2026080862 / 2026080864`。

当前 README 更新时尚未用该 runner 生成任何 v0.2.2 formal screen。

## 7. 当前边界

本轮外审已经结束，不需要重开 Scientific Contract、PSD normalization、FFT、Hermitian 或 low-frequency generator。

当前状态：

> **CONTINUE — ONE FRESH 1024-SCREEN v0.2.2 FORMAL RERUN AUTHORIZED; V6 REMAINS CLOSED.**
