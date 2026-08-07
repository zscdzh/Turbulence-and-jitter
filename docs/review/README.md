# Review Entry Point

Stage-A broad review 已结束。v0.3.1 最新短复核结论为：

> **REVISE — KEEP CODE GATE CLOSED**

OPB finite-aperture feasibility 与 G1 lower-tail optimization 已 PASS；当前只剩一个确定 blocker：phase-spectrum / Fourier `2pi` normalization。

## 当前最短阅读路径

1. `SCIENTIFIC_CONTRACT_V031_SHORT_REVIEW_DECISION.md` —— 最新短复核与唯一 remaining blocker；
2. `../SCIENTIFIC_CONTRACT_DRAFT.md` —— v0.3.2 candidate；
3. `../literature/MODIFIED_VON_KARMAN_PSD_CONVENTION_ANCHOR.md` —— 唯一 spectrum/Fourier normalization anchor；
4. `SCIENTIFIC_CONTRACT_V03_SHORT_REVIEW_CHECKLIST.md` —— final ultra-short normalization review。

背景材料按需读取：

- `SCIENTIFIC_CONTRACT_V03_SHORT_REVIEW_DECISION.md`；
- `EXTERNAL_REVIEW_DECISION_2026-08-07.md`；
- `../RESEARCH_STAGE_BOUNDARY.md`。

## v0.3.2 本轮只检查

1. `Phi_n^(atm)` / `Phi_phi^(atm)` / `Phi_phi^(math)` 的 `(2pi)` conversion；
2. mathematical Fourier measure `d^2kappa/(2pi)^2` 是否与 phase PSD 完全匹配；
3. Kolmogorov limit 是否恢复 `D_phi=6.88(rho/r0_screen)^(5/3)`；
4. V4/V5 是否能发现 absolute normalization 错误。

不要重新审查已经 PASS 的：

- OPB `omega_OPB=0.55` finite-aperture feasibility；
- G1 CRN staged `Q5%` optimization；
- primary scene；
- mechanism set / novelty route。

## 当前状态

- Stage A broad literature expansion: `CLOSED`；
- Paper 1 scope: coherent deterministic single-aperture direct-detection；
- core set: Gaussian + Bessel + OPB + flat-top；
- latest decision: `REVISE — KEEP CODE GATE CLOSED`；
- scientific contract: `v0.3.2 CANDIDATE / FINAL ULTRA-SHORT REVIEW`；
- scientific code: none；
- formal numerical results: none。

若 v0.3.2 极短复核通过，只打开 **Gaussian-only implementation gate**。structured fields 仍需等待 Gaussian V0–V12 全部通过。

旧 review package / questions 仅保留为审查历史。