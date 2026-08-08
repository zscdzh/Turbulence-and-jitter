# Gate B v0.2.1 Post-Failure External Audit Package

**日期：2026-08-08**  
**状态：READY FOR EXTERNAL AUDIT**  
**当前正式裁决：REVISE — GATE B NOT YET QUALIFIED**  
**V6：CLOSED**

本目录作为本轮外部审计的统一入口。外审只需从本文件所列材料读取即可。

## 1. 主审查材料

- `docs/review/GATE_B_V021_POSTFAILURE_ENSEMBLE_REVIEW_PROPOSAL.md`
  - 审查核心问题：formal ensemble 是否应由 512 提高到 1024，还是应修改 low-frequency representation。
  - 包含原 v0.2 / P=6 failure、v0.2.1 remediation、P*=9 fresh formal failure、post-failure 1024 convergence diagnostic、项目当前判断和两种备选方案。

## 2. 正式结果

- `docs/results/GATE_B_V4_V5_FORMAL_V021_RESULTS.md`
  - v0.2.1 全新 seeds 的正式 512-screen + 2000-bootstrap 结果。
  - 正式结果仍为 `REVISE — GATE B NOT YET QUALIFIED`。

## 3. 机器统计摘要

- `results/gate_b_v5_formal_v021/bootstrap_summary.json`
  - formal 512-screen bootstrap summary。
- `results/gate_b_v5_formal_v021/postfailure_1024_bootstrap2000.json`
  - post-failure 1024-screen diagnostic bootstrap summary；仅作诊断，不是资格证据。
- `results/gate_b_v5_formal_v021/deterministic_ladder.json`
  - v0.2.1 deterministic P-selection evidence。
- `results/gate_b_v5_formal_v021/metadata.json`
  - formal seeds、ensemble、bootstrap 等运行元数据。
- `results/gate_b_v5_formal_v021/v4_summary.json`
  - fresh V4 regression summary。

## 4. 执行代码

- `scripts/run_gate_b_formal_v021.py`
- `scripts/run_gate_b_p_depth_diagnostic.py`
- `src/turbulence_jitter/gate_b.py`

## 5. 权威合同

- `docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V021.md`
- `docs/SCIENTIFIC_CONTRACT_DRAFT.md`

Scientific Contract v0.3.2 保持冻结。本轮不重开 PSD normalization、FFT、Hermitian、subharmonic coefficient formula，也不授权 V6。

## 6. 建议外审读取顺序

1. 本 README；
2. `docs/review/GATE_B_V021_POSTFAILURE_ENSEMBLE_REVIEW_PROPOSAL.md`；
3. `docs/results/GATE_B_V4_V5_FORMAL_V021_RESULTS.md`；
4. `results/gate_b_v5_formal_v021/bootstrap_summary.json`；
5. 如需复核，再读取 deterministic ladder、metadata、runner。
