# 项目状态——UAV-FSO deterministic transmit fields 的 turbulence–jitter failure map

**更新日期：2026-08-07**  
**当前主分支：main**  
**当前阶段：Paper 1 / CONTRACT FREEZE GATE**  
**最新外部短审：REVISE — KEEP CODE GATE CLOSED**  
**Scientific Contract：v0.3.1 candidate，等待短复核**  
**正式科学代码：未建立**  
**正式数值结果：无**

## 1. 当前科学问题

Paper 1 已收窄为：

> coherent、deterministic、single-aperture scalar transmit fields 在 direct-detection finite-aperture UAV-FSO 链路中的跨机制 turbulence–jitter sensitivity / failure map。

目标不是寻找 joint-optimum beam，而是判断既有 turbulence-resistant mechanisms 在 independent post-PAT residual jitter 下的优势保持、压缩、排序反转与失效；并判断这些差异在 optimized Gaussian、receiver `r80` scale control 与资源账本之后是否仍有结构意义。

Paper 2 才是条件性的 turbulence–jitter co-design。

## 2. 第一轮 core set

冻结为：

1. Gaussian G0 / optimized G1；
2. circular-truncated zeroth-order Bessel `J0`；
3. continuum radial-phase OPB；
4. nested multi-Gaussian flat-top。

讨论层保留但不进入首轮数值：

- Airy path diversity；
- partial coherence；
- vector / mode diversity。

## 3. v0.3 短审暴露的三个 blocker

### Blocker A — OPB finite-aperture feasibility

已在 v0.3.1 candidate 修订：

- `rho_s=4 beta L^2` 正式进入约束；
- `w_A=0.65a_T` 下 `r95_T≈0.775a_T`；
- primary `omega_OPB` 从 `0.35` 改为 `0.55`；
- primary scene 下 `rho_s≈17.94 mm < r95_T≈19.37 mm`；
- Level-B OPB 范围改为 `[0.55,0.90]`，同时强制 `rho_s<=r95_T`。

### Blocker B — G1 tail optimization stability

已在 v0.3.1 candidate 修订：

- 35 个 Gaussian 候选共享 common random numbers；
- 256 realizations 全候选粗筛；
- Top-5 再补 768，最终每个 finalist `N_opt=1024`；
- `N_eval=1024` 与 optimization 完全 disjoint；
- near-boundary evaluation 可扩至 4096。

### Blocker C — turbulence absolute validation

已在 v0.3.1 candidate 修订：

- 冻结 exact modified-von-Karman `Phi_n(kappa)`；
- 冻结 `kappa0=2pi/L0`, `kappam=5.92/l0`；
- 冻结 thin-screen `Phi_phi=2pi k^2 Delta-z Phi_n` 与连续 Fourier convention；
- 新增 Gaussian weak-turbulence long-term-radius absolute reference；
- 新增独立 spectral beam-wander quadrature reference；
- grid-resolution 与 physical-window convergence 拆成 V10a/V10b；
- 保留 maximum-tilt wrap-around / aliasing gate。

## 4. primary physical scene

保持短审已通过的 scene：

- `lambda=1550 nm`；
- `L=1 km`；
- `D_T=D_R=50 mm`；
- normalized `P_T=1`；
- constant-`Cn2` horizontal path；
- `Cn2=3e-15, 1e-14, 3e-14 m^-2/3`；
- baseline `L0=10 m`, `l0=5 mm`；
- sensitivity `L0=5/20 m`, `l0=3/10 mm`。

该 scene 只作为 representative mechanism scene，不声称是 universal UAV terminal。

## 5. fairness contract

### Level A — primary

相同 `lambda/L/D_T/D_R/P_T`，aperture 后 equal-power normalization，paired turbulence/jitter realizations，完整 resource ledger。

### Level B — only secondary diagnostic

no-turbulence/no-jitter receiver `r80_R`-matched one-scale retuning。

- Bessel：只调 `chi_B`；
- OPB：只调 `omega_OPB`；
- flat-top：固定 `N=4`，只调 `w_F/a_T`；
- `H0` 只报告。

### Gaussian G1

唯一优化目标 `Q5%(H)`；预注册 `w_G/a_T` 和 `L/f_G`；CRN staged optimization；optimization/evaluation 完全分离。

## 6. jitter contract

主坐标：

\[
j=L\sigma_\theta/w_{ref}.
\]

第一版：zero-mean isotropic Gaussian；补一个 anisotropic case 和一个 nonzero boresight-bias case。

现实锚点：

- fixed-wing actual-flight `~8–10 urad (1sigma)`；
- Trinh multirotor retro-FSO `~27–42 urad/axis` 仅作 double-pass stress anchor。

不模拟第一版 jitter PSD / temporal controller。

## 7. 文献状态

Stage A broad search 已关闭。三条定向链已完成：

- Nelson 2014：Bessel/Airy turbulence failure boundary；
- Jiang 2022/2026：flat-top direct competitors；
- Lane 1992：subharmonic/low-frequency anchor。

不再因为出现新的 beam name 重启广撒网。

## 8. 当前 code gate

当前决定：

> **REVISE — KEEP CODE GATE CLOSED.**

下一步只做 v0.3.1 短复核。若短审 PASS，只授权以下 Gaussian-only 顺序：

1. Gaussian free-space；
2. finite-aperture displacement；
3. analytic jitter benchmark；
4. Gaussian phase-screen / multi-screen validation V0–V12。

只有 Gaussian chain 通过全部 numerical gates 后，才允许实现 Bessel / OPB / flat-top common comparison。

## 9. 禁止表述

继续禁止：

- “首次联合 turbulence 与 pointing”；
- “首次 structured beam + joint channel”；
- “self-healing 等于自动回正”；
- “27–42 urad 是典型 UAV one-way residual”；
- “flat-top / OPB 已证明 joint-optimal”；
- “multi-screen / subharmonic 本身是创新”；
- “低 scintillation 等于高低分位 received power”；
- “omega_OPB=0.55 / chi_B=10 / N=4 是文献证明 optimum”。
