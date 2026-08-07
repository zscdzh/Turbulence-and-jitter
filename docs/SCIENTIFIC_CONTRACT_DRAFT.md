# SCIENTIFIC_CONTRACT_DRAFT

**状态：Scientific Contract v0.3.2 candidate — CONTRACT FREEZE GATE；最终极短复核通过前保持 code gate CLOSED。**  
**日期：2026-08-07**  
**外部审查链：** `docs/review/EXTERNAL_REVIEW_DECISION_2026-08-07.md` → `docs/review/SCIENTIFIC_CONTRACT_V03_SHORT_REVIEW_DECISION.md` → `docs/review/SCIENTIFIC_CONTRACT_V031_SHORT_REVIEW_DECISION.md`  
**阶段边界：** `docs/RESEARCH_STAGE_BOUNDARY.md`

---

## 1. Paper 1 正式 scope — FROZEN

Paper 1 研究：

> **coherent、deterministic、single-aperture scalar transmit fields 在 direct-detection finite-aperture UAV-FSO 链路中的跨机制 turbulence–jitter sensitivity / failure map。**

核心问题：已有 turbulence-resistant deterministic transmit-field mechanisms 在加入 independent post-PAT residual pointing jitter 后，哪些 turbulence-only 优势能够保持、压缩、反转或失效；这些变化经过 optimized Gaussian、receiver-scale control 与完整 resource ledger 后，是否仍具有机制意义并能形成 applicability / failure map。

### scope 内

- coherent deterministic scalar complex fields；
- single circular Tx clear aperture；
- single circular finite Rx aperture；
- direct-detection finite-aperture received power；
- distributed atmospheric turbulence；
- turbulence-induced beam wander；
- independent post-PAT residual angular jitter；
- 一个 anisotropic-jitter sensitivity case；
- 一个 nonzero boresight-bias sensitivity case。

### scope 外

- partially coherent / source-ensemble optimization；
- Airy multi-beam path-diversity architecture；
- vector / polarization / mode-diversity receiver architecture；
- AO instantaneous correction；
- full UAV 6-DOF / PAT/FSM time-domain controller；
- jitter PSD / temporal correlation in Paper 1 primary model；
- high-dimensional inverse design / neural network。

Airy path diversity、partial coherence、vector/mode diversity 只保留在讨论层，不属于本 Paper 1 首轮数值 scope。

---

## 2. Paper 2 边界 — FROZEN

Paper 2 为 **CONDITIONAL GO**。只有 Paper 1 出现稳定、跨连续区域、且不能被 optimized Gaussian / receiver-scale matching 完全解释的 turbulence–jitter trade-off 后，才允许构造少参数 co-robust beam。

flattened-/super-Gaussian、Gaussian–LG/annular-like 当前仅为 Paper 2 设计种子，不得反向定义 Paper 1。

---

## 3. 第一轮 core field set — FROZEN

### 3.1 Gaussian G0 / G1

\[
U_G(r)=C_G\exp(-r^2/w_G^2)
\exp\left[-i\frac{k r^2}{2f_G}\right]\Pi(r/a_T).
\]

G0 是 common-resource reference；G1 是预注册 optimized-Gaussian envelope。

### 3.2 zeroth-order Bessel

主代表采用 circular-truncated `J0`：

\[
U_B(r)=C_BJ_0\left(\chi_B\frac{r}{a_T}\right)\Pi(r/a_T).
\]

第一轮 representative：

\[
\chi_B=10.
\]

该值位于 Eyyuboğlu 2013 映射得到的约 `O(5–20)` 结构范围内部，只是 representative choice，不是文献 optimum claim。

正式 common comparison 前必须做一次 Eyyuboğlu 2013 square-window reproduction sanity case。只有结论明显依赖 hard truncation 时，才增加 Bessel–Gaussian sensitivity check。

### 3.3 OPB — finite-aperture feasible form

采用 continuum radial phase：

\[
U_{OPB}(r)=C_{OPB}A(r)
\exp\left[-i\frac{4}{3}k\sqrt{\beta}\,r^{3/2}\right]
\Pi(r/a_T),
\]

\[
A(r)=\exp(-r^2/w_A^2),\qquad w_A=0.65a_T.
\]

正确 pin-width relation：

\[
\boxed{W(z)=\frac{1}{4k\beta z}}.
\]

stationary source radius：

\[
\boxed{\rho_s=4\beta z^2}.
\]

在目标距离 `L`：

\[
\omega_{OPB}=\frac{W(L)}{a_T},
\qquad
\beta=\frac{1}{4kLa_T\omega_{OPB}},
\qquad
\rho_s(L)=\frac{L}{ka_T\omega_{OPB}}.
\]

至少要求：

\[
\rho_s\le a_T.
\]

本项目进一步采用代表性可实现性准则：

\[
\rho_s\le r_{95,T}^{OPB}.
\]

对 `w_A=0.65a_T`、aperture 后 Gaussian intensity：

\[
r_{95,T}^{OPB}\approx0.775a_T.
\]

primary scene 下：

- hard-aperture lower bound：`omega_OPB >= 0.395`；
- `rho_s<=r95_T` lower bound：`omega_OPB >= 0.509`。

冻结：

\[
\boxed{\omega_{OPB}=0.55}.
\]

对应：

- `W(L)=13.75 mm`；
- `beta≈4.485e-9 m^-1`；
- `rho_s≈17.94 mm`；
- `r95_T≈19.37 mm`。

不实现 32-filament / etched-mask discretization。

### 3.4 flat-top

采用 nested multi-Gaussian family：

\[
U_N(r)=C_N\left[\frac{1}{N}\sum_{n=1}^{N}(-1)^{n-1}\binom{N}{n}
\exp\left(-n\frac{r^2}{w_F^2}\right)\right]\Pi(r/a_T).
\]

`1/N` 可被 `C_N` 吸收；`N=1` 正确退化为 Gaussian。

冻结：

- `N=1`：nested-Gaussian sanity；
- `N=4`：moderate representative；
- `N=8`：optional high-order stress only；
- Level-A primary `w_F=0.65a_T`。

`N=4/8` 不声称是 Jiang 2022/2026 的 joint optimum。

---

## 4. common-resource Level A — FROZEN

所有 core fields 使用完全相同：

- `lambda, L`；
- circular Tx clear aperture `D_T=2a_T`；
- circular Rx aperture `D_R=2a_R`；
- post-aperture transmitted power `P_T`；
- paired turbulence realizations；
- paired jitter realizations；
- nominal receiver axis。

所有 source fields 经 common aperture 后重新归一：

\[
\iint_{r\le a_T}|U_0|^2dA=P_T.
\]

Level A 是论文主结果。

### 必须报告的 resource ledger

- `r50_T,r80_T,r95_T`；
- peripheral / halo power fraction；
- source second moment；
- angular-spectrum / transverse-frequency descriptor；
- no-disturbance `H0`；
- receiver-plane `r50_R,r80_R`；
- receiver second moment；
- literature-supported generation efficiency / conversion loss。

这些量报告而不全部硬匹配。

---

## 5. secondary Level B — FROZEN AS `r80_R` MATCHING

唯一 secondary diagnostic：

> **receiver-plane no-turbulence/no-jitter `r80_R`-matched one-scale retuning。**

\[
|r_{80,R}^{field}/r_{80,R}^{G0}-1|\le1\%.
\]

若预注册范围内没有唯一稳定解，标记 `NO R80 MATCH`，不得扩大范围救结果。

每个 family 只开放一个 scale：

- Bessel：`chi_B in [6,18]`；
- OPB：`omega_OPB in [0.55,0.90]`；
- flat-top：固定 `N=4`，只调 `gamma_F=w_F/a_T in [0.40,0.90]`。

OPB 每个候选必须同时满足 `rho_s<=r95_T`。

禁止同时改变 family order 和 radial scale。`H0` 只报告，不作为 matching constraint。

---

## 6. Gaussian G0 / G1 — FROZEN RULES

### 6.1 G0 reference

\[
w_G=0.65a_T,\qquad f_G=\infty.
\]

定义：

\[
w_{ref}=r_{80,R}^{G0}.
\]

Gaussian analytic jitter benchmark 单独使用 `1/e^2` intensity radius `W`，不得把 `r80` 与 `W` 混用。

### 6.2 G1 search space

\[
\gamma_G=w_G/a_T\in
\{0.35,0.45,0.55,0.65,0.75,0.85,0.95\},
\]

\[
u_f=L/f_G\in\{0,0.5,1.0,1.5,2.0\}.
\]

共 35 candidates。

### 6.3 唯一优化目标

\[
\boxed{Q_{5\%}(H)}.
\]

G1 在每个正式场景点 `(tau,j,alpha_R)` 独立选择最佳 `(gamma_G,u_f)`。

### 6.4 common-random-number staged optimization

**Stage G1-A**

- 35 candidates 使用同一组 256 common random realizations；
- 按 `Q5%(H)` 排序；
- 保留 Top-5。

**Stage G1-B**

- Top-5 共享额外 768 realizations；
- finalist 的最终 `N_opt=1024`；
- winner 只由完整 1024 optimization set 决定。

**正式评价**

- `N_eval=1024`，与 optimization 完全 disjoint；
- 所有 fields 使用 paired common evaluation realizations；
- near-boundary / ranking-reversal point 可扩展到 `N_confirm=4096`。

\[
\text{optimization seeds}\cap\text{evaluation seeds}=\varnothing.
\]

---

## 7. primary physical scene — FROZEN FOR v0.3.2

### 7.1 geometry

- `lambda = 1550 nm`；
- `L = 1000 m`；
- `D_T = 50 mm`, `a_T=25 mm`；
- `D_R = 50 mm`, `a_R=25 mm`；
- normalized `P_T=1`。

这是 representative near-ground UAV-FSO mechanism scene，不是 universal UAV terminal claim。

### 7.2 turbulence strength and finite scales

primary atmosphere：constant-`Cn2` horizontal path。

baseline：

- `Cn2 = 1e-14 m^(-2/3)`；
- `L0 = 10 m`；
- `l0 = 5 mm`。

primary sweep：

- `Cn2 = 3e-15`；
- `1e-14`；
- `3e-14 m^(-2/3)`。

plane-wave diagnostic：

\[
r_0=[0.423k^2C_n^2L]^{-3/5},
\qquad
\tau=D_T/r_0.
\]

约对应：

- `r0≈162 mm, tau≈0.31`；
- `r0≈78.5 mm, tau≈0.64`；
- `r0≈40.6 mm, tau≈1.23`。

finite-scale sensitivity：

- `L0 = 5,10,20 m`；
- `l0 = 3,5,10 mm`。

`Cn2=1e-13` 仅作为 production validation 后的 optional strong stress。

### 7.3 modified-von-Kármán spectrum + Fourier normalization — FROZEN

本项目显式区分 atmospheric PSD 与 mathematical Fourier PSD。

#### atmospheric refractive-index spectrum

采用 angular spatial frequency `kappa [rad/m]`：

\[
\boxed{
\Phi_n^{(\mathrm{atm})}(\kappa)=0.033C_n^2
\frac{\exp[-(\kappa/\kappa_m)^2]}
{(\kappa^2+\kappa_0^2)^{11/6}}
}
\]

\[
\kappa_0=\frac{2\pi}{L_0},
\qquad
\kappa_m=\frac{5.92}{l_0}.
\]

atmospheric thin-screen phase spectrum：

\[
\boxed{
\Phi_{\phi,m}^{(\mathrm{atm})}(\kappa)
=2\pi k^2\Delta z_m\,\Phi_n^{(\mathrm{atm})}(\kappa)
}.
\]

这里的 atmospheric spectrum integral **不额外带** `(2pi)^-2` measure。

#### mathematical Fourier convention

冻结：

\[
\phi(\mathbf r)=
\int\frac{d^2\kappa}{(2\pi)^2}
\tilde\phi(\boldsymbol\kappa)e^{i\boldsymbol\kappa\cdot\mathbf r},
\]

\[
\langle\tilde\phi(\boldsymbol\kappa)
\tilde\phi^*(\boldsymbol\kappa')\rangle
=(2\pi)^2\delta^{(2)}(\boldsymbol\kappa-\boldsymbol\kappa')
\Phi_\phi^{(\mathrm{math})}(\boldsymbol\kappa).
\]

因此进入该 mathematical convention 的 phase PSD 必须为：

\[
\boxed{
\Phi_{\phi,m}^{(\mathrm{math})}(\kappa)
=(2\pi)^2\Phi_{\phi,m}^{(\mathrm{atm})}(\kappa)
=(2\pi)^3k^2\Delta z_m\,\Phi_n^{(\mathrm{atm})}(\kappa)
}.
\]

phase structure function：

\[
\boxed{
D_\phi(\rho)
=2\int\frac{d^2\kappa}{(2\pi)^2}
\Phi_\phi^{(\mathrm{math})}(\kappa)
[1-\cos(\boldsymbol\kappa\cdot\boldsymbol\rho)]
}.
\]

等价 atmospheric 写法：

\[
D_\phi(\rho)
=2\int d^2\kappa\,
\Phi_\phi^{(\mathrm{atm})}(\kappa)
[1-\cos(\boldsymbol\kappa\cdot\boldsymbol\rho)].
\]

两种形式必须数值一致。

#### Kolmogorov-limit absolute amplitude

screen-level validation limit 必须恢复：

\[
\boxed{
D_\phi(\rho)
=2.91k^2C_n^2\Delta z\,\rho^{5/3}
=6.88\left(\frac{\rho}{r_{0,\mathrm{screen}}}\right)^{5/3}
}.
\]

\[
\boxed{
r_{0,\mathrm{screen}}
=[0.423k^2C_n^2\Delta z]^{-3/5}
}.
\]

离散 FFT / subharmonic 实现内部可以使用 `cycles/m` 或其他一致 convention，但必须显式记录 frequency unit、spectral-cell measure、PSD coefficient、IFFT normalization 和 complex-coefficient variance，并通过 V4/V5。

### 7.4 phase-screen placement

primary constant-`Cn2` path：equal-spacing screens 起步。screen number 由 convergence 决定，validation ladder：`4 -> 8 -> 16 -> 32`。

高度依赖 `Cn2(z)` 与 non-uniform placement 只作为 secondary extension。

---

## 8. jitter / boresight contract — FROZEN

transmitter angular tilt：

\[
U_0'(x,y)=U_0(x,y)
\exp[ik(\theta_xx+\theta_yy)].
\]

primary：

\[
\theta_x,\theta_y\sim\mathcal N(0,\sigma_\theta^2).
\]

`σ_theta` 为单轴 post-PAT residual LOS angular standard deviation。

主坐标：

\[
\boxed{j=\frac{L\sigma_\theta}{w_{ref}}}.
\]

primary sweep：`j = 0,0.25,0.5,1.0,1.5`。

physical anchors 只用于场景映射：

- fixed-wing high-performance actual flight：约 `8–10 urad (1sigma)`；
- Trinh 2021 multirotor retro-FSO：约 `27–42 urad/axis`，仅 double-pass stress anchor。

不定义唯一 typical UAV `sigma_theta`。

### anisotropic sensitivity

一个 `sigma_y/sigma_x=2` case，并保持：

\[
(\sigma_x^2+\sigma_y^2)/2=\sigma_\theta^2.
\]

因此：

\[
\sigma_x=\sigma_\theta/\sqrt{2.5},
\qquad
\sigma_y=2\sigma_x.
\]

### boresight sensitivity

\[
\rho_b=0.5w_{ref},
\qquad
\theta_b=\rho_b/L.
\]

### 三类横向运动独立记账

- `rho_bw`：turbulence-only centroid wander；
- `rho_j=L theta_j`：independent residual jitter；
- `rho_b`：boresight bias。

不得 double count turbulence beam wander。

---

## 9. receiver observable and statistics — FROZEN

\[
P_R=\iint_{r\le a_R}|U_L|^2dA,
\qquad
H=P_R/P_T.
\]

primary outputs：

- full ECDF of `H`；
- `Q5%(H)`；
- paired difference distributions against G1；
- confidence interval / bootstrap uncertainty at claimed boundaries。

secondary：

- outage at explicitly stated threshold；
- mean `H`；
- scintillation；
- centroid / beam radius / profile descriptors。

point irradiance、peak intensity、scintillation、shape fidelity 不得单独证明 communication gain。

---

## 10. Gaussian production numerical-validation table — v0.3.2 CANDIDATE

任何 structured-field multi-screen production run 前，Gaussian chain 必须通过以下 gates。

| Gate | 验证量 | acceptance |
|---|---|---|
| V0 | full-grid power conservation, free space | relative drift `<=1e-4` |
| V1 | unclipped Gaussian free-space radius / phase | analytic disagreement `<=1%` |
| V2 | displaced Gaussian finite-aperture capture | analytic/high-accuracy quadrature disagreement `<=0.5%` |
| V3 | Gaussian jitter broadening | `W_eff^2=W^2+4L^2 sigma_theta^2`, disagreement `<=1%` |
| V4 | phase-screen PSD | compare to frozen **mathematical PSD** after explicit convention mapping；median relative level error `<=10%` over preregistered resolved band，且 slope 正确 |
| V5 | phase structure function | finite-scale continuous integral median relative error `<=10%`；**Kolmogorov-limit absolute amplitude** vs `6.88(rho/r0_screen)^(5/3)` median relative error `<=10%` over preregistered resolved inertial interval；slope `5/3 ±0.10` |
| V6a | absolute beam-wander reference | weakest-turbulence G0: `Var(rho_bw)` vs independently implemented spectral beam-wander quadrature `<=10%` |
| V6b | low-frequency refinement | further subharmonic/equivalent refinement changes `Var(rho_bw) <5%` |
| V7a | absolute long-term-radius reference | weak-Kolmogorov validation case: `W_LT` vs analytic weak-fluctuation reference `<=5%` |
| V7b | production finite-scale refinement | further low-frequency/grid refinement changes `W_LT <2%` |
| V8 | scintillation auxiliary | further screen/grid refinement changes scintillation `<5%`; weak case also checked against independent weak-fluctuation reference where applicable |
| V9 | screen-number ladder | choose smallest of `4/8/16/32` for which V6–V8 pass on next refinement |
| V10a | grid resolution only | fixed physical window，refine `Delta x`；`W_LT <2%`, wander variance `<5%`, scintillation `<5%` |
| V10b | physical window only | keep `Delta x` approximately fixed，enlarge window；same tolerances |
| V11 | maximum tilt aliasing / wrap-around | centroid shift linearity vs vacuum within `1%`; full-grid power drift `<=1e-4`; no boundary contamination at max `j+bias` |
| V12 | propagation / split-step sampling | one longitudinal refinement satisfies same observable tolerances as V10 |

### 10.1 absolute long-term Gaussian reference

validation-only weak-Kolmogorov case：

\[
\sigma_R^2=1.23C_n^2k^{7/6}L^{11/6},
\]

\[
\Lambda=\frac{2L}{kW^2},
\]

\[
\boxed{
W_{LT}^2=W^2
\left[1+1.33\sigma_R^2\Lambda^{5/6}\right]
}.
\]

这里只用于 weak-fluctuation absolute validation，不要求 production finite-`L0/l0` 结果机械服从。

### 10.2 absolute beam-wander spectral reference

V6a 使用与 phase-screen propagator 独立实现的 spectral quadrature，不共享 screen generator 或 FFT normalization。

\[
\langle r_c^2\rangle_{ref}
=4\pi^2k^2W_R^2
\int_0^L dz\int_0^\infty d\kappa\,
\kappa\Phi_n^{(\mathrm{atm})}(\kappa)
\exp[-\kappa^2W^2(z)]
\left[1-\exp\left(-\frac{\Lambda_RL\kappa^2(1-z/L)^2}{k}\right)\right].
\]

其中 `W(z)` 是 no-turbulence G0 `1/e^2` intensity radius，`W_R=W(L)`，`Lambda_R=2L/(kW_R^2)`。

V6a 只作为弱/中弱条件 absolute normalization check。

### 10.3 双层验收

- Lane 1992：subharmonic / low-frequency anchor；
- Chen 2020：beam-wander / long-term-radius consequence anchor；
- Chahine 2020：longitudinal placement secondary anchor；
- `MODIFIED_VON_KARMAN_PSD_CONVENTION_ANCHOR.md`：唯一 spectrum/Fourier normalization contract。

任何 phase-screen algorithm 只有同时通过 screen-level absolute PSD/structure-function 与 propagation-level absolute/convergence observables 才可进入 production。

---

## 11. targeted literature chains — CLOSED

### Nelson 2014

Bessel/Airy quasi-nondiffracting robustness 在 `r0` 接近初始 aperture scale 时会明显失效；`D_T/r0` 是重要 failure coordinate，但 `r0=D_T` 不是 universal hard threshold。

### Jiang 2022/2026

flat-top + turbulence + pointing/bias + average irradiance/received power 已存在；Paper 1 novelty 只能落在 distributed wave optics、realization-level low-tail、optimized Gaussian、resource matching 与 cross-mechanism failure map。

### Lane 1992

低频补偿必须进入 formal validation；screen-level PSD/structure function 与 propagation-level beam wander 必须同时通过。

**Stage A broad literature search is CLOSED。**

---

## 12. Paper 1 hypotheses — FROZEN AS TESTS, NOT CLAIMS

- H1：turbulence-only superiority 不足以预测 turbulence+jitter low-tail reliability；
- H2：Bessel angular-spectrum redundancy 不自动提供 common lateral-displacement correction；
- H3：OPB narrow pin / autofocusing 可以保持 propagation structure，同时对 common tilt 产生 receiver loss；
- H4：flat-top broad capture 可能降低 jitter sensitivity，但收益可能被 source/receiver scale 与 peripheral energy 解释；
- H5：Nelson-type turbulence failure 与 mechanical-jitter failure 是不同机制层；
- H6：经过 G1 optimized Gaussian 与 Level-B `r80` control 后，structured-beam ranking 可能压缩、反转或退化为无显著机制收益；
- H7：如果所有差异都可由 receiver-plane scale / optimized Gaussian 解释，则接受负结果，不增加高维自由度救结论。

---

## 13. claims prohibited — FROZEN

禁止：

- “首次联合 turbulence 与 pointing error”；
- “首次 structured beam + joint channel”；
- “self-healing 等于自动回正”；
- “27–42 urad 是典型 UAV one-way transmitter residual”；
- “flat-top 或 OPB 已被证明 turbulence–jitter joint-optimal”；
- “multi-screen / subharmonic 本身是创新”；
- “低 scintillation 等价于更高 `Q5%` / lower outage”；
- “Nelson `r0~D` 是精确 universal threshold”；
- “N=4 / chi_B=10 / omega_OPB=0.55 是文献证明的 optimum”。

---

## 14. code authorization gate

当前：

> **REVISE — KEEP CODE GATE CLOSED.**

v0.3.2 candidate 只剩一次极短复核，唯一重点是确认：

1. `Phi_n^(atm)`、`Phi_phi^(atm)` 与 `Phi_phi^(math)` 的 `(2pi)` conversion 自洽；
2. Kolmogorov limit 正确恢复 `D_phi=6.88(rho/r0_screen)^(5/3)`；
3. V4/V5 不再可能因 reference 与 generator 共用同一错误 normalization 而假通过。

若极短复核 PASS，则只授权：

1. Gaussian free-space；
2. finite-aperture displacement；
3. analytic jitter；
4. Gaussian phase-screen / multi-screen validation。

**即使 v0.3.2 PASS，也不立即授权 Bessel / OPB / flat-top production comparison。** 只有 Gaussian numerical chain 完成并通过 V0–V12 后，才进入 structured-field implementation。