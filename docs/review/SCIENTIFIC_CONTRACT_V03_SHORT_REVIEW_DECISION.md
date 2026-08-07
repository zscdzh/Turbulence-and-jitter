# Scientific Contract v0.3 短审结论

**日期：2026-08-07**  
**Decision：REVISE — KEEP CODE GATE CLOSED**

本文件记录 v0.3 candidate 的第二轮短审。除下列三项外，scope、核心四场、primary physical scene、Level A、`r80_R` secondary matching、jitter evidence 与总体 numerical-validation 结构均接受。

## Blocker 1 — OPB finite-aperture feasibility

Zhang 2019 的渐近场包含 `A(4 beta z^2)`；目标距离 `L` 对应的 stationary source radius 为

\[
\rho_s=4\beta L^2.
\]

结合

\[
W(L)=\frac{1}{4k\beta L},\qquad
\omega_{OPB}=W(L)/a_T,
\]

得到

\[
\rho_s=\frac{L}{k a_T\omega_{OPB}}.
\]

v0.3 的 `omega_OPB=0.35` 导致 `rho_s>a_T`，因此不能在冻结发射孔径内完整实现所引用的渐近 pin-width 关系。

修订要求：

- 至少满足 hard-aperture constraint `rho_s<=a_T`；
- 第一版进一步采用 `rho_s<=r95_T` 作为 Gaussian-illuminated OPB 的代表性可实现性准则；
- 删除 Level-B 中不可实现的 `omega_OPB` 区间。

## Blocker 2 — G1 lower-tail optimization stability

`N_opt=256` 对 5% 分位数不足。35 个 Gaussian 候选中每个只有约 13 个尾部样本，存在 noise-driven winner 风险。

修订要求：

- 所有 G1 候选共享 common random numbers；
- 允许 `256` realizations 对全部候选粗筛；
- Top-5 候选使用额外 realizations 补到总计 `N_opt=1024`；
- 最终赢家只由 1024-sample optimization set 决定；
- 正式 `N_eval=1024` 与 optimization set 完全 disjoint；临界点按原规则增至 4096。

## Blocker 3 — turbulence absolute validation

现有 V6–V8 以自收敛为主，仍可能自洽地收敛到错误归一化。

修订要求：

1. 冻结 exact modified-von-Karman refractive-index PSD、`kappa_0`、`kappa_m` 与 phase-screen PSD/Fourier normalization convention；
2. 增加至少一个 Gaussian propagation absolute reference，不只检查进一步加密的相对变化；
3. grid resolution 与 physical window size 分开收敛，禁止一次同时改变两者；
4. 保留 maximum-tilt wrap-around / aliasing 验收。

## 已接受且无需重开的问题

- Paper 1 scope：coherent deterministic single-aperture transmit fields；
- core set：Gaussian + circular-truncated J0 + continuum OPB + flat-top；
- Airy path diversity / partial coherence 不进入第一轮数值；
- primary scene：1550 nm / 1 km / 50-mm Tx / 50-mm Rx / constant-Cn2；
- Level A common resources；
- Level B `r80_R`-matched one-scale retuning；
- dimensionless jitter 主坐标及现有 fixed-wing / Trinh anchors；
- ensemble/static reliability scope，不要求第一版 jitter PSD/time-domain controller。

## 当前 code gate

> **CLOSED.**

只有上述三项进入下一版 contract candidate 并通过一次短复核后，才允许 Gaussian-only implementation。structured-beam implementation 仍需排在 Gaussian validation 之后。
