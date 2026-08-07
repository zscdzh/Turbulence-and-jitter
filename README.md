# Turbulence-and-jitter

面向 UAV-FSO 的**抗湍流 deterministic transmit fields 抖动敏感性**与后续 turbulence–jitter co-design 研究。

## Paper 1 当前科学问题

> **coherent、deterministic、single-aperture scalar transmit fields 在 direct-detection finite-aperture UAV-FSO 链路中的跨机制 turbulence–jitter sensitivity / failure map。**

研究重点不是设计 joint-optimum beam，而是判断已有 turbulence-resistant mechanisms 在 independent post-PAT residual jitter 下的优势保持、压缩、排序反转与失效；并检查这些差异经过 optimized Gaussian、receiver `r80` scale control 与透明 resource accounting 后是否仍具有机制意义。

Paper 2 才是条件性的 turbulence–jitter co-design。

## 第一轮 core fields

Scientific Contract v0.3.2：

- Gaussian G0 / optimized G1；
- circular-truncated zeroth-order Bessel `J0`；
- continuum radial-phase OPB；
- nested multi-Gaussian flat-top。

Airy path diversity、partial coherence、vector/mode diversity 只保留在讨论层。

## Fairness contract

### Level A — primary

相同 `lambda/L/D_T/D_R/P_T`，aperture 后 equal-power normalization，paired turbulence/jitter realizations，完整 resource ledger。

### Level B — secondary diagnostic

no-turbulence/no-jitter receiver-plane `r80_R`-matched one-scale retuning。`H0` 只报告。

Gaussian G1 以 `Q5%(H)` 为唯一目标；35 candidates 用 256 common random realizations 粗筛，Top-5 补至 `N_opt=1024`；正式 `N_eval=1024` 与 optimization 完全独立。

## Primary physical scene

- `lambda = 1550 nm`；
- `L = 1 km`；
- `D_T = D_R = 50 mm`；
- constant-`Cn2` horizontal path；
- `Cn2 = 3e-15, 1e-14, 3e-14 m^(-2/3)`；
- baseline `L0=10 m`, `l0=5 mm`；
- dimensionless jitter `j = 0,0.25,0.5,1.0,1.5`。

这是 representative mechanism scene，不是 universal UAV terminal claim。

## OPB finite-aperture freeze

\[
W(L)=\frac{1}{4k\beta L},
\qquad
\rho_s=4\beta L^2,
\qquad
\rho_s\le r_{95,T}.
\]

对 `w_A=0.65a_T`，冻结：

- `omega_OPB=0.55`；
- `beta≈4.485e-9 m^-1`；
- `rho_s≈17.94 mm < r95_T≈19.37 mm`；
- Level-B `omega_OPB in [0.55,0.90]`。

该项已通过短复核。

## Turbulence spectrum normalization

v0.3.2 显式区分 atmospheric 与 mathematical Fourier PSD：

\[
\Phi_\phi^{(atm)}=2\pi k^2\Delta z\,\Phi_n^{(atm)},
\]

\[
\boxed{
\Phi_\phi^{(math)}=(2\pi)^2\Phi_\phi^{(atm)}
=(2\pi)^3k^2\Delta z\,\Phi_n^{(atm)}
}.
\]

在 mathematical measure `d^2kappa/(2pi)^2` 下必须恢复：

\[
D_\phi(\rho)=6.88(\rho/r_{0,screen})^{5/3}.
\]

最终复核已 PASS。

## 当前状态

**Stage A broad literature search: CLOSED**  
**Scientific Contract: v0.3.2 PASS**  
**Gaussian-only implementation gate: OPEN**  
**Structured-field implementation gate: CLOSED**  
**Formal structured-beam numerical results: NONE**

当前只授权 Gaussian numerical qualification：

1. Gaussian free-space；
2. finite-aperture displacement / capture；
3. analytic jitter；
4. Gaussian phase-screen / multi-screen V0–V12 validation。

只有 Gaussian chain 全部通过后，才允许 Bessel / OPB / flat-top implementation / production comparison。

## 关键入口

- `PROJECT_STATE.md`
- `docs/RESEARCH_STAGE_BOUNDARY.md`
- `docs/SCIENTIFIC_CONTRACT_DRAFT.md`
- `docs/literature/MODIFIED_VON_KARMAN_PSD_CONVENTION_ANCHOR.md`
- `docs/review/SCIENTIFIC_CONTRACT_V032_FINAL_REVIEW_DECISION.md`
