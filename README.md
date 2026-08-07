# Turbulence-and-jitter

面向无人机自由空间光通信（UAV-FSO）的**抗湍流 deterministic transmit fields 抖动敏感性**与后续 turbulence–jitter co-design 研究。

## 当前主问题：Paper 1

Paper 1 已在外部审查后正式收窄为：

> **coherent、deterministic、single-aperture transmit fields 在 direct-detection finite-aperture UAV-FSO 链路中的跨机制 turbulence–jitter sensitivity / failure map。**

核心问题：已有 turbulence-resistant transmit-field mechanisms 在加入 independent post-PAT residual pointing jitter 后，哪些 turbulence-only 优势能够保持、压缩、反转或失效；这些差异经过 optimized Gaussian、receiver-scale control 与 transparent resource accounting 后是否仍具有机制意义。

Paper 1 不是 joint-beam-design 论文，也不以“首次同时考虑 turbulence 与 pointing”为创新。

## 第一轮 core fields

Scientific Contract v0.3 candidate 冻结：

- Gaussian G0 / optimized G1；
- circular-truncated zeroth-order Bessel `J0`；
- continuum radial-phase optical pin beam (OPB)；
- nested multi-Gaussian flat-top。

只保留在文献/讨论层：

- Airy path diversity；
- partial coherence；
- vector / mode diversity。

这些方案不是被否定，而是超出当前 coherent deterministic single-aperture direct-detection scope。

## 两层公平比较

### Level A — 主结果

统一：

- wavelength / distance；
- Tx / Rx circular aperture；
- post-aperture transmitted power；
- paired turbulence and jitter realizations；
- transparent resource ledger。

### Level B — secondary diagnostic

唯一采用 no-turbulence/no-jitter receiver-plane `r80_R`-matched one-scale retuning。

`H0` 报告但不作为 matching constraint。

Gaussian G1 允许预注册的 `w_G + quadratic focus` 二维搜索，并以 `Q5%(H)` 为唯一主优化指标；optimization 与 final evaluation 使用独立 random ensembles。

## Primary scene — v0.3 candidate

- `lambda = 1550 nm`；
- `L = 1 km`；
- `D_T = 50 mm`；
- `D_R = 50 mm`；
- constant-`Cn2` horizontal path；
- primary `Cn2 = 3e-15, 1e-14, 3e-14 m^(-2/3)`；
- baseline `L0=10 m`, `l0=5 mm`；
- dimensionless jitter `j=L sigma_theta/w_ref = 0, 0.25, 0.5, 1.0, 1.5`。

physical jitter values only serve as evidence-labelled mapping anchors, not a universal UAV residual parameter.

## 当前阶段

**External Review: REVISE**  
**Stage A broad literature search: CLOSED**  
**Scientific Contract: v0.3 CANDIDATE / NEED SHORT REVIEW**  
**Structured-beam code: NOT AUTHORIZED**  
**Formal numerical results: NONE**

三条外审指定文献链已关闭：

- Nelson 2014：Bessel/Airy turbulence failure boundary；
- Jiang 2022/2026：flat-top direct competitors；
- Lane 1992：subharmonic / low-frequency phase-screen method。

OPB pin-width 公式已修正为：

\[
W(z)=\frac{1}{4k\beta z}.
\]

## 代码授权顺序

v0.3 短审通过后才允许：

1. Gaussian free-space；
2. finite-aperture displacement；
3. analytic Gaussian jitter；
4. Gaussian multi-screen validation；
5. Eyyuboğlu Bessel literature-reproduction sanity；
6. Bessel / OPB / flat-top common comparison。

不得跳过 Gaussian validation 直接运行 structured-beam Monte Carlo。

## Paper 2

Paper 2 是条件性的 turbulence–jitter co-robust beam design。

只有 Paper 1 找到跨连续参数区、且经过 G1 optimized Gaussian 与 `r80_R` control 后仍存在的机制 trade-off，才允许启动。

## 关键文档

- `PROJECT_STATE.md`：当前负责人状态；
- `docs/RESEARCH_STAGE_BOUNDARY.md`：Paper 1 / Paper 2 权威边界；
- `docs/SCIENTIFIC_CONTRACT_DRAFT.md`：Scientific Contract v0.3 candidate；
- `docs/review/EXTERNAL_REVIEW_DECISION_2026-08-07.md`：正式外审 REVISE 结论；
- `docs/PAPER1_PARAMETER_MAPPING_MATRIX.md`：参数映射；
- `docs/literature/PAPER1_COMMON_RESOURCE_GATE_DRAFT.md`：公平比较 gate；
- `docs/literature/`：关键文献与 direct-competitor 审计；
- `docs/review/`：外部审查材料。

## 禁止表述

- “首次联合 turbulence 与 pointing”；
- “首次 structured beam + joint channel”；
- “self-healing 会自动回正”；
- “27–42 urad 是典型 UAV one-way transmitter residual”；
- “OPB / flat-top 已经证明 joint-optimal”；
- “multi-screen / subharmonic 本身是创新”；
- “低 scintillation 等于高 low-tail received power”。
