# Turbulence-and-jitter

面向 UAV-FSO 的**抗湍流 deterministic transmit fields 抖动敏感性**与后续 turbulence–jitter co-design 研究。

## Paper 1 当前科学问题

外部审查后，Paper 1 正式收窄为：

> **coherent、deterministic、single-aperture scalar transmit fields 在 direct-detection finite-aperture UAV-FSO 链路中的跨机制 turbulence–jitter sensitivity / failure map。**

研究重点不是设计 joint-optimum beam，而是判断已有 turbulence-resistant mechanisms 在 independent post-PAT residual jitter 下的优势保持、压缩、排序反转与失效；并检查这些差异经过 optimized Gaussian、receiver `r80` scale control 与透明 resource accounting 后是否仍具有机制意义。

Paper 2 才是条件性的 turbulence–jitter co-design。

## 第一轮 core fields

Scientific Contract v0.3.1 candidate：

- Gaussian G0 / optimized G1；
- circular-truncated zeroth-order Bessel `J0`；
- continuum radial-phase optical pin beam (OPB)；
- nested multi-Gaussian flat-top。

讨论层保留、首轮不进入数值：

- Airy path diversity；
- partial coherence；
- vector / mode diversity。

## Fairness contract

### Level A — primary

统一：

- wavelength / distance；
- Tx / Rx circular aperture；
- post-aperture transmitted power；
- paired turbulence and jitter realizations；
- complete source/receiver resource ledger。

### Level B — only secondary diagnostic

采用 no-turbulence/no-jitter receiver-plane `r80_R`-matched one-scale retuning。

`H0` 只报告，不作为 matching constraint。

Gaussian G1 以 `Q5%(H)` 为唯一优化目标。35 个候选先共享 256 common random realizations 粗筛，Top-5 再补至最终 `N_opt=1024`；正式 `N_eval=1024` 与 optimization set 完全 disjoint。

## Primary physical scene

- `lambda = 1550 nm`；
- `L = 1 km`；
- `D_T = D_R = 50 mm`；
- constant-`Cn2` horizontal path；
- `Cn2 = 3e-15, 1e-14, 3e-14 m^(-2/3)`；
- baseline `L0=10 m`, `l0=5 mm`；
- dimensionless jitter `j=L sigma_theta/w_ref = 0,0.25,0.5,1.0,1.5`。

该 scene 是 representative mechanism scene，不声称为 universal UAV terminal。

## OPB finite-aperture correction

v0.3 短审发现原 primary `omega_OPB=0.35` 对有限 Tx aperture 不自洽。v0.3.1 正式加入：

\[
W(L)=\frac{1}{4k\beta L},
\qquad
\rho_s=4\beta L^2,
\qquad
\rho_s\le r_{95,T}.
\]

对 `w_A=0.65a_T`，`r95_T≈0.775a_T`。primary scene 下冻结：

- `omega_OPB=0.55`；
- `beta≈4.49e-9 m^-1`；
- `rho_s≈17.94 mm < r95_T≈19.37 mm`；
- Level-B `omega_OPB in [0.55,0.90]`。

## Turbulence numerical contract

v0.3.1 冻结 modified-von-Karman convention：

\[
\Phi_n(\kappa)=0.033C_n^2
\frac{\exp[-(\kappa/\kappa_m)^2]}
{(\kappa^2+\kappa_0^2)^{11/6}},
\]

\[
\kappa_0=2\pi/L_0,
\qquad
\kappa_m=5.92/l_0,
\]

以及 thin-screen `Phi_phi=2pi k^2 Delta-z Phi_n` 和明确的 continuous Fourier convention。

Gaussian production chain 必须通过 V0–V12，包括：

- screen PSD / structure function；
- weak-turbulence long-term-radius absolute reference；
- independent beam-wander spectral reference；
- low-frequency refinement；
- screen-number convergence；
- fixed-window grid-resolution convergence；
- fixed-`Delta x` physical-window convergence；
- maximum-tilt wrap-around / aliasing。

## 当前状态

**Stage A broad literature search: CLOSED**  
**Latest short review: REVISE — KEEP CODE GATE CLOSED**  
**Scientific Contract: v0.3.1 CANDIDATE / NEED SHORT RE-REVIEW**  
**Scientific code: NONE**  
**Formal numerical results: NONE**

下一步只做 `docs/review/SCIENTIFIC_CONTRACT_V03_SHORT_REVIEW_CHECKLIST.md` 的最终短复核。

若 PASS，只授权 Gaussian-only implementation：

1. free-space；
2. finite-aperture displacement；
3. analytic jitter；
4. Gaussian phase-screen / multi-screen V0–V12 validation。

只有 Gaussian chain 全部通过后，才允许 Bessel / OPB / flat-top production comparison。

## 关键入口

- `PROJECT_STATE.md`
- `docs/RESEARCH_STAGE_BOUNDARY.md`
- `docs/SCIENTIFIC_CONTRACT_DRAFT.md`
- `docs/PAPER1_PARAMETER_MAPPING_MATRIX.md`
- `docs/review/SCIENTIFIC_CONTRACT_V03_SHORT_REVIEW_DECISION.md`
- `docs/review/SCIENTIFIC_CONTRACT_V03_SHORT_REVIEW_CHECKLIST.md`
