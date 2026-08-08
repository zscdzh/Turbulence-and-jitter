# Gate B v0.2.2 Final External Review Decision

**日期：2026-08-08**  
**最终裁决：PASS — GATE B V4–V5 QUALIFIED; AUTHORIZE PREPARATION OF V6 IMPLEMENTATION CONTRACT**

该裁决只授权 V6 implementation contract 的编写与审核；不授权 V6 simulation、production propagation、V7–V12 或 structured fields。

## Review binding

外审绑定：

- PR #5 reviewed head：`9d4b20646c1a5a37cde1f817ba5f0ad790d3c8cd`；
- formal v0.2.2 runner blob：`d1ff27c347e37a68a9ca0d9bb111433aa3136d65`。

## Review findings

外审独立执行完整：

- 1024 finite-scale screens；
- 1024 Kolmogorov screens；
- `B_boot=2000` screen-ID bootstrap。

独立复算逐项恢复：

- V4 PASS；
- deterministic `P*=9`；
- finite-scale x/y/45° PASS；
- Kolmogorov implementation recovery PASS；
- Kolmogorov amplitude PASS；
- Kolmogorov slope PASS。

与 committed machine summary 的数值差异仅为约 `1e-11` 浮点末位，因此：

> **PASS — GATE B V4–V5 QUALIFIED**

## Execution interruption ruling

外审接受 finite screen 384 处的第一次外部工具超时，不构成 one-shot violation：

- 中断前没有完整 ensemble；
- 没有 formal statistic；
- 重启使用完全相同的 preregistered seed family；
- 从 screen 1 确定性重放同一随机序列；
- 没有 seed selection、threshold adjustment 或 ensemble escalation。

## Integration follow-up

外审指出 reviewed head 当时比 `main` 落后 3 commits，并缺少 main 上已经先于正式运行存在的：

- `docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V022.md`；
- `docs/review/GATE_B_V022_ENSEMBLE_REMEDIATION_DECISION.md`。

该事项在外审后通过临时 PR #6 将 `main` 正式 merge 回 `agent/gaussian-gate-a-v0-v3` 关闭。

同步后核对：

- PR #5 `behind_by = 0`；
- PR #5 `mergeable = true`；
- `scripts/run_gate_b_formal_v022.py` blob 仍为 `d1ff27c347e37a68a9ca0d9bb111433aa3136d65`；
- `docs/results/GATE_B_V4_V5_FORMAL_V022_RESULTS.md` blob 仍为 `aa506312f2cd869aa22d5d22bc8418fe991ce95d`。

因此 integration 处理未改变外审绑定的正式 runner 或结果。

## Current boundary

已授权：

- 编写 V6 implementation contract proposal；
- 对该合同进行外部审核。

仍未授权：

- V6 simulation；
- V7–V12；
- production multi-screen propagation；
- G1 production optimization；
- Bessel / OPB / flat-top；
- structured-field comparison。

当前项目状态：

> **CONTINUE — PREPARE AND REVIEW V6 IMPLEMENTATION CONTRACT ONLY.**
