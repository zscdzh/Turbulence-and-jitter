# 项目状态——UAV-FSO deterministic transmit fields 的 turbulence–jitter failure map

**更新日期：2026-08-07**  
**当前主分支：main**  
**当前阶段：Paper 1 / GAUSSIAN NUMERICAL QUALIFICATION**  
**最新外部短审：PASS — AUTHORIZE GAUSSIAN-ONLY IMPLEMENTATION**  
**Scientific Contract：v0.3.2，Gaussian-only code gate OPEN**  
**structured-field implementation：未授权**  
**正式 structured-beam 数值结果：无**

## 1. 当前科学问题

Paper 1 已冻结为：

> coherent、deterministic、single-aperture scalar transmit fields 在 direct-detection finite-aperture UAV-FSO 链路中的跨机制 turbulence–jitter sensitivity / failure map。

目标不是寻找 joint-optimum beam，而是判断既有 turbulence-resistant mechanisms 在 independent post-PAT residual jitter 下的优势保持、压缩、排序反转与失效；并判断这些差异在 optimized Gaussian、receiver `r80` scale control 与资源账本之后是否仍有结构意义。

Paper 2 才是条件性的 turbulence–jitter co-design。

## 2. 第一轮 core set

冻结为：

1. Gaussian G0 / optimized G1；
2. circular-truncated zeroth-order Bessel `J0`；
3. continuum radial-phase OPB；
4. nested multi-Gaussian flat-top。

讨论层保留但不进入首轮数值：Airy path diversity、partial coherence、vector/mode diversity。

## 3. 外审 blocker 状态

### OPB finite-aperture feasibility — PASS

- `rho_s=4 beta L^2`；
- `w_A=0.65a_T`，aperture 后 `r95_T≈0.775a_T`；
- primary `omega_OPB=0.55`；
- primary scene 下 `rho_s≈17.94 mm < r95_T≈19.37 mm`；
- Level-B OPB `omega in [0.55,0.90]` 且强制 `rho_s<=r95_T`。

### G1 lower-tail optimization — PASS

- 35 Gaussian candidates 共享 256 common random realizations；
- Top-5 再补 768，finalist `N_opt=1024`；
- `N_eval=1024` 与 optimization 完全 disjoint；
- near-boundary evaluation 可扩至 4096。

### phase-spectrum / Fourier normalization — PASS

v0.3.2 显式分开：

\[
\Phi_\phi^{(atm)}=2\pi k^2\Delta z\,\Phi_n^{(atm)},
\]

\[
\boxed{
\Phi_\phi^{(math)}
=(2\pi)^2\Phi_\phi^{(atm)}
=(2\pi)^3k^2\Delta z\,\Phi_n^{(atm)}
}.
\]

在 mathematical Fourier measure `d^2kappa/(2pi)^2` 下，两种 structure-function integral 完全等价。

Kolmogorov absolute gate：

\[
D_\phi(\rho)=6.88(\rho/r_{0,screen})^{5/3},
\qquad
r_{0,screen}=[0.423k^2C_n^2\Delta z]^{-3/5}.
\]

最终复核确认 V4 / V5 / V6 / V7 构成闭合的 screen-level + propagation-level validation chain。

## 4. primary physical scene

保持已通过的 scene：

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

\[
j=L\sigma_\theta/w_{ref}.
\]

第一版：zero-mean isotropic Gaussian；补一个 anisotropic case 和一个 nonzero boresight-bias case。

现实锚点：fixed-wing actual-flight `~8–10 urad (1sigma)`；Trinh multirotor retro-FSO `~27–42 urad/axis` 仅作 double-pass stress anchor。

不模拟第一版 jitter PSD / temporal controller。

## 7. 文献状态

Stage A broad search 已关闭。三条定向链已完成：Nelson 2014、Jiang 2022/2026、Lane 1992。不再因为出现新的 beam name 重启广撒网。

## 8. 当前 code gate

当前决定：

> **PASS — AUTHORIZE GAUSSIAN-ONLY IMPLEMENTATION.**

现在允许且仅允许按以下顺序实施：

1. Gaussian free-space；
2. finite-aperture displacement / capture；
3. analytic jitter benchmark；
4. Gaussian phase-screen / multi-screen validation V0–V12。

该阶段的目标是验证共同传播链和数值归一化，不产生 structured-beam 优劣结论。

### 仍未授权

- Bessel implementation / production comparison；
- OPB implementation / production comparison；
- flat-top implementation / production comparison；
- structured-field Monte Carlo；
- Paper-2 joint beam optimization。

只有 Gaussian chain 通过全部 V0–V12 后，才允许重新打开 structured-field implementation gate。

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

## 10. 当前权威审查链

- `docs/review/EXTERNAL_REVIEW_DECISION_2026-08-07.md`
- `docs/review/SCIENTIFIC_CONTRACT_V03_SHORT_REVIEW_DECISION.md`
- `docs/review/SCIENTIFIC_CONTRACT_V031_SHORT_REVIEW_DECISION.md`
- `docs/review/SCIENTIFIC_CONTRACT_V032_FINAL_REVIEW_DECISION.md`
