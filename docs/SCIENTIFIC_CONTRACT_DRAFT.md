# SCIENTIFIC_CONTRACT_DRAFT

**状态：Scientific Contract v0.3.1 candidate — CONTRACT FREEZE GATE；短审通过前保持 code gate CLOSED。**  
**日期：2026-08-07**  
**外部审查链：** `docs/review/EXTERNAL_REVIEW_DECISION_2026-08-07.md` → `docs/review/SCIENTIFIC_CONTRACT_V03_SHORT_REVIEW_DECISION.md`  
**阶段边界：** `docs/RESEARCH_STAGE_BOUNDARY.md`

---

## 1. Paper 1 正式 scope — FROZEN

Paper 1 收窄为：

> **coherent、deterministic、single-aperture scalar transmit fields 在 direct-detection finite-aperture UAV-FSO 链路中的跨机制 turbulence–jitter sensitivity / failure map。**

核心问题：

> 已有 turbulence-resistant deterministic transmit-field mechanisms 在加入 independent post-PAT residual pointing jitter 后，哪些 turbulence-only 优势能够保持、压缩、反转或失效；这些变化经过 optimized Gaussian、receiver-scale control 与完整 resource ledger 后，是否仍具有机制意义并能形成 applicability / failure map？

### scope 内

- coherent deterministic scalar complex fields；
- single circular transmitter clear aperture；
- single circular finite receiver aperture；
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

因此，Airy path diversity、partial coherence、vector/mode diversity 可保留在文献讨论中，但不属于本 Paper 1 数值 scope。

---

## 2. Paper 2 边界 — FROZEN

Paper 2 仍为 **CONDITIONAL GO**。只有 Paper 1 出现稳定、跨连续区域、且不能被 optimized Gaussian / receiver-scale matching 完全解释的 turbulence–jitter trade-off 后，才允许构造少参数 co-robust beam。

flattened-/super-Gaussian、Gaussian–LG/annular-like 当前仅为 Paper 2 设计种子，不得反向定义 Paper 1。

---

## 3. 第一轮 core field set — FROZEN

### 3.1 Gaussian G0 / G1

\[
U_G(r)=C_G\exp(-r^2/w_G^2)
\exp\left[-i\frac{k r^2}{2f_G}\right]\Pi(r/a_T).
\]

G0 是 common-resource reference；G1 是预注册 optimized-Gaussian envelope。

### 3.2 zeroth-order Bessel — FROZEN FORM

主代表采用 circular-truncated `J0`：

\[
U_B(r)=C_BJ_0\left(\chi_B\frac{r}{a_T}\right)\Pi(r/a_T).
\]

第一轮 representative：

\[
\chi_B=10.
\]

该值位于 Eyyuboğlu 2013 文献映射得到的约 `O(5–20)` 结构范围内部，只是 representative choice，不是文献 optimum claim。

在正式 common comparison 前，必须做一次 Eyyuboğlu 2013 square-window reproduction sanity case。只有结论明显依赖 hard truncation 时，才增加 Bessel–Gaussian sensitivity check。

### 3.3 OPB — FROZEN FORM + FINITE-APERTURE FEASIBILITY

采用 continuum radial phase：

\[
U_{OPB}(r)=C_{OPB}A(r)
\exp\left[-i\frac{4}{3}k\sqrt{\beta}\,r^{3/2}\right]
\Pi(r/a_T),
\]

其中

\[
A(r)=\exp(-r^2/w_A^2),\qquad w_A=0.65a_T.
\]

正确 pin-width relation：

\[
\boxed{W(z)=\frac{1}{4k\beta z}}.
\]

Zhang 2019 渐近场中的 stationary source radius 为：

\[
\boxed{\rho_s=4\beta z^2}.
\]

在目标距离 `L` 定义：

\[
\omega_{OPB}=\frac{W(L)}{a_T},
\qquad
\beta=\frac{1}{4kLa_T\omega_{OPB}},
\]

因此

\[
\rho_s(L)=\frac{L}{k a_T\omega_{OPB}}.
\]

有限发射孔径至少要求：

\[
\rho_s\le a_T
\quad\Rightarrow\quad
\omega_{OPB}\ge\frac{L}{ka_T^2}.
\]

本项目进一步采用 Gaussian-illuminated OPB 的代表性可实现性准则：

\[
\rho_s\le r_{95,T}^{OPB},
\]

其中 `r95_T` 由 aperture 后实际 intensity 的 encircled energy 定义。对于 `w_A=0.65a_T`：

\[
\frac{1-\exp[-2r_{95,T}^2/w_A^2]}
{1-\exp[-2a_T^2/w_A^2]}=0.95,
\]

得到

\[
r_{95,T}^{OPB}\approx0.775a_T.
\]

在 primary scene `L=1 km, a_T=25 mm, lambda=1550 nm` 下：

- hard-aperture lower bound：`omega_OPB >= 0.395`；
- `rho_s<=r95_T` lower bound：`omega_OPB >= 0.509`。

因此第一版 primary OPB 冻结为：

\[
\boxed{\omega_{OPB}=0.55}.
\]

对应：

- `W(L)=13.75 mm`；
- `beta≈4.49e-9 m^-1`；
- `rho_s≈17.94 mm`；
- `r95_T≈19.37 mm`。

因此 stationary contribution 位于主要发射能量支持区内，而不是落在硬孔径外。

不实现 32-filament / etched-mask discretization。

### 3.4 flat-top — FROZEN FAMILY

采用 nested multi-Gaussian family：

\[
U_N(r)=C_N\left[\frac{1}{N}\sum_{n=1}^{N}(-1)^{n-1}\binom{N}{n}
\exp\left(-n\frac{r^2}{w_F^2}\right)\right]\Pi(r/a_T).
\]

`1/N` 可被 normalization constant `C_N` 吸收，不改变归一化后形状；`N=1` 正确退化为 Gaussian。

冻结：

- `N=1`：nested-Gaussian sanity；
- `N=4`：moderate representative；
- `N=8`：optional high-order stress only；
- Level-A primary `w_F=0.65a_T`。

`N=4/8` 是项目代表性采样，不声称是 Jiang 2022/2026 的 joint optimum。

### 3.5 不进入首轮数值集合

- Airy path-diversity array：文献/架构讨论 only；
- partial coherence：成熟 turbulence+pointing joint-optimization control，discussion only；
- vector / mode diversity：out of scope。

---

## 4. common-resource Level A — FROZEN

所有 core fields 使用完全相同：

- wavelength `lambda`；
- propagation distance `L`；
- circular Tx clear aperture `D_T=2a_T`；
- circular Rx aperture `D_R=2a_R`；
- post-aperture transmitted power `P_T`；
- turbulence realizations；
- jitter realizations；
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

这些量原则上报告而不全部硬匹配。

---

## 5. secondary Level B — FROZEN AS `r80_R` MATCHING

唯一 secondary diagnostic：

> **receiver-plane no-turbulence/no-jitter `r80_R`-matched one-scale retuning。**

匹配条件：

\[
|r_{80,R}^{field}/r_{80,R}^{G0}-1|\le1\%.
\]

若预注册参数范围内没有唯一稳定解，标记 `NO R80 MATCH`，不得扩大范围救结果。

每个 family 只开放一个 scale：

- Bessel：`chi_B in [6,18]`；
- OPB：`omega_OPB in [0.55,0.90]`；
- flat-top：固定 `N=4`，只调 `gamma_F=w_F/a_T in [0.40,0.90]`。

OPB Level-B 下每个候选同时必须满足 `rho_s<=r95_T`；若不满足，即使能匹配 `r80_R` 也判为物理不可接受。

禁止同时改变 family order 和 radial scale。

`H0` 只报告，不作为 matching constraint。

---

## 6. Gaussian G0 / G1 — FROZEN RULES

### 6.1 G0 reference

primary G0：

\[
w_G=0.65a_T,
\qquad
f_G=\infty.
\]

定义主 reference scale：

\[
w_{ref}=r_{80,R}^{G0}
\]

其中 `r80_R^G0` 在 primary physical scene、no-turbulence/no-jitter 条件下由 validated free-space propagator 计算。

Gaussian analytic jitter benchmark 单独使用 `1/e^2` intensity radius `W`，不得把 `r80` 与 `W` 混用。

### 6.2 G1 search space

\[
\gamma_G=w_G/a_T\in
\{0.35,0.45,0.55,0.65,0.75,0.85,0.95\}.
\]

quadratic focusing 用

\[
u_f=L/f_G\in\{0,0.5,1.0,1.5,2.0\},
\]

其中 `u_f=0` 表示 `f_G=infinity`。

共 35 个候选。

### 6.3 G1 唯一优化目标

\[
\boxed{Q_{5\%}(H)}.
\]

G1 在每个正式场景点 `(tau,j,alpha_R)` 独立选择最佳 `(gamma_G,u_f)`，形成较强 Gaussian envelope。不得看完 structured-field 结果后切换到 mean power、scintillation 或其他目标。

### 6.4 G1 common-random-number staged optimization

为避免 5% tail 的 noise-driven winner：

**Stage G1-A — coarse screen**

- 全部 35 个候选使用**完全相同的 256 组 turbulence/jitter common random realizations**；
- 按 `Q5%(H)` 排序；
- 仅保留 Top-5。

**Stage G1-B — final selection**

- Top-5 继续共享额外 768 组 common random realizations；
- 因而每个 Top-5 候选的最终 optimization sample 总数为 `N_opt=1024`；
- 最终 G1 winner 只由完整 1024-sample optimization set 决定。

**正式评价**

- `N_eval=1024`，与 optimization realizations 完全 disjoint；
- 所有 fields 在 evaluation 中使用 paired common turbulence/jitter realizations；
- near-boundary / ranking-reversal point 若 uncertainty 与零差异重叠，可将 evaluation 扩展至 `N_confirm=4096`；不默认全参数面使用 4096。

严格要求：

\[
\text{optimization seeds}\cap\text{evaluation seeds}=\varnothing.
\]

---

## 7. primary physical scene — FROZEN FOR v0.3.1

### 7.1 geometry

- `lambda = 1550 nm`；
- `L = 1000 m`；
- `D_T = 50 mm`, `a_T=25 mm`；
- `D_R = 50 mm`, `a_R=25 mm`；
- simulation normalized `P_T=1`。

该场景是 representative near-ground UAV-FSO mechanism scene，不宣称所有 UAV terminals 均使用 50-mm apertures。

### 7.2 turbulence strength and finite scales

primary atmosphere：constant-`Cn2` horizontal path。

baseline：

- `Cn2 = 1e-14 m^(-2/3)`；
- `L0 = 10 m`；
- `l0 = 5 mm`。

primary turbulence sweep：

- `Cn2 = 3e-15`；
- `1e-14`；
- `3e-14 m^(-2/3)`。

plane-wave diagnostic：

\[
r_0=[0.423k^2C_n^2L]^{-3/5},
\qquad
\tau=D_T/r_0.
\]

对本 scene 约对应：

- `r0≈162 mm, tau≈0.31`；
- `r0≈78.5 mm, tau≈0.64`；
- `r0≈40.6 mm, tau≈1.23`。

outer/inner-scale sensitivity：

- `L0 = 5,10,20 m`；
- `l0 = 3,5,10 mm`。

`Cn2=1e-13` 仅可在 production module 验证通过后作为 optional strong stress。

### 7.3 exact modified-von-Karman PSD convention — FROZEN

采用**angular spatial frequency** `kappa`，单位 `rad/m`。三维 refractive-index PSD 定义为：

\[
\boxed{
\Phi_n(\kappa)
=0.033C_n^2
\frac{\exp[-(\kappa/\kappa_m)^2]}
{(\kappa^2+\kappa_0^2)^{11/6}}
}
\]

其中：

\[
\kappa_0=\frac{2\pi}{L_0},
\qquad
\kappa_m=\frac{5.92}{l_0}.
\]

对厚度 `Delta z_m` 的 thin phase screen，冻结连续二维 phase PSD：

\[
\boxed{
\Phi_{\phi,m}(\boldsymbol\kappa)
=2\pi k^2\Delta z_m\,\Phi_n(|\boldsymbol\kappa|)
}
\]

其中 optical wavenumber `k=2pi/lambda`。

为消除 `2pi` normalization 歧义，冻结 Fourier convention：

\[
\phi(\mathbf r)=
\int\frac{d^2\kappa}{(2\pi)^2}
\tilde\phi(\boldsymbol\kappa)e^{i\boldsymbol\kappa\cdot\mathbf r},
\]

\[
\langle\tilde\phi(\boldsymbol\kappa)
\tilde\phi^*(\boldsymbol\kappa')\rangle
=(2\pi)^2\delta^{(2)}(\boldsymbol\kappa-\boldsymbol\kappa')
\Phi_\phi(\boldsymbol\kappa).
\]

因此 phase structure function 的连续参考为：

\[
\boxed{
D_\phi(\rho)
=2\int\frac{d^2\kappa}{(2\pi)^2}
\Phi_\phi(\kappa)
[1-\cos(\boldsymbol\kappa\cdot\boldsymbol\rho)]
}.
\]

离散 FFT / subharmonic 实现可以采用任意等价 convention，但必须数值映射回以上连续定义，并通过 V4/V5；不得仅因调用某个库函数而假设 normalization 正确。

### 7.4 phase-screen placement

primary constant-`Cn2` horizontal path：equal-spacing screens 起步。

screen number 由 convergence 决定，不冻结固定数量。validation ladder：`4 -> 8 -> 16 -> 32`。

高度依赖 `Cn2(z)` 与 non-uniform placement 只作为 secondary extension。

---

## 8. jitter / boresight contract — FROZEN

### 8.1 primary residual model

\[
U_0'(x,y)=U_0(x,y)
\exp[ik(\theta_xx+\theta_yy)].
\]

primary：

\[
\theta_x,\theta_y\sim\mathcal N(0,\sigma_\theta^2).
\]

`σ_theta` 定义为单轴 post-PAT residual LOS angular standard deviation。

主科学坐标：

\[
\boxed{j=\frac{L\sigma_\theta}{w_{ref}}}.
\]

primary jitter sweep：

`j = 0,0.25,0.5,1.0,1.5`。

physical anchors 只用于场景映射：

- fixed-wing high-performance actual-flight：约 `8–10 urad (1sigma)`；
- Trinh 2021 multirotor retro-FSO：约 `27–42 urad/axis`，仅 double-pass stress anchor。

不定义唯一“typical UAV sigma_theta”。

### 8.2 anisotropic sensitivity

增加一个 `sigma_y/sigma_x=2` case，并保持平均单轴 variance 与 isotropic reference 相同：

\[
(\sigma_x^2+\sigma_y^2)/2=\sigma_\theta^2.
\]

因此：

\[
\sigma_x=\sigma_\theta/\sqrt{2.5},
\qquad
\sigma_y=2\sigma_x.
\]

只在一个代表 `(tau,j)` 条件验证 ranking sensitivity。

### 8.3 boresight sensitivity

增加一个 x-direction nonzero bias：

\[
\rho_b=0.5w_{ref},
\qquad
\theta_b=\rho_b/L.
\]

只作 secondary sensitivity。

### 8.4 三类横向运动独立记账

- `rho_bw`：turbulence-only centroid wander；
- `rho_j=L theta_j`：independent residual jitter；
- `rho_b`：boresight bias。

不得把 phase-screen 已包含的 beam wander 再作为额外 statistical pointing loss 叠加。

---

## 9. receiver observable and statistics — FROZEN

realization-level finite-aperture power：

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

## 10. Gaussian production numerical-validation table — v0.3.1 FROZEN CANDIDATE

任何 structured-field multi-screen production run 前，Gaussian chain 必须通过以下验证。

| Gate | 验证量 | acceptance |
|---|---|---|
| V0 | full-grid power conservation, free space | relative drift `<=1e-4` |
| V1 | unclipped Gaussian free-space radius / phase | analytic disagreement `<=1%` |
| V2 | displaced Gaussian finite-aperture capture | analytic/high-accuracy quadrature disagreement `<=0.5%` |
| V3 | Gaussian jitter broadening | `W_eff^2=W^2+4L^2 sigma_theta^2`, disagreement `<=1%` |
| V4 | phase-screen PSD | target spectrum level + slope；median relative level error `<=10%` over preregistered resolved band |
| V5 | phase structure function | vs continuous integral from frozen `Phi_phi`; median relative error `<=10%` over resolved interval；Kolmogorov-limit slope sanity `5/3 ±0.10` |
| V6a | **absolute beam-wander reference** | weakest-turbulence G0: phase-screen `Var(rho_bw)` agrees with an independently implemented spectral beam-wander quadrature within `<=10%` |
| V6b | low-frequency refinement | subharmonic/equivalent further refinement changes `Var(rho_bw) <5%` |
| V7a | **absolute long-term-radius reference** | weak-Kolmogorov validation case: `W_LT` agrees with weak-fluctuation analytic reference within `<=5%` |
| V7b | production finite-scale refinement | further low-frequency/grid refinement changes `W_LT <2%` |
| V8 | scintillation auxiliary | further screen/grid refinement changes scintillation `<5%`; weak case also checked against independent weak-fluctuation reference where applicable |
| V9 | screen-number ladder | choose smallest of `4/8/16/32` for which V6–V8 pass on next refinement |
| V10a | **grid resolution only** | keep physical window fixed, refine `Delta x`; `W_LT <2%`, wander variance `<5%`, scintillation `<5%` |
| V10b | **physical window only** | keep `Delta x` approximately fixed, enlarge window; same observable tolerances |
| V11 | maximum tilt aliasing / wrap-around | centroid shift linearity vs vacuum prediction within `1%`; full-grid power drift `<=1e-4`; no boundary contamination at max `j+bias` |
| V12 | propagation / split-step sampling | one longitudinal refinement satisfies same observable tolerances as V10 |

### 10.1 absolute long-term Gaussian reference

单独建立 **validation-only weak-Kolmogorov case**，不把它误当 production finite-`L0/l0` model。对 weak fluctuation：

\[
\sigma_R^2=1.23C_n^2k^{7/6}L^{11/6},
\]

\[
\Lambda=\frac{2L}{kW^2},
\]

其中 `W` 是 no-turbulence receiver-plane Gaussian `1/e^2` intensity radius。采用标准 weak-fluctuation long-term-radius reference：

\[
\boxed{
W_{LT}^2=W^2
\left[1+1.33\sigma_R^2\Lambda^{5/6}\right]
}.
\]

该 gate 只在满足 weak-fluctuation applicability 的 validation case 使用；production finite-outer/inner-scale结果不要求机械服从此式。

### 10.2 absolute beam-wander spectral reference

V6a 使用与 phase-screen propagator **独立实现**的一维/二维数值积分作为 reference，不共享 screen generator 或 FFT normalization。

对 G0 free-space Gaussian，采用文献中的 large-scale spectral beam-wander integral形式：

\[
\boxed{
\langle r_c^2\rangle_{ref}
=4\pi^2k^2W_R^2
\int_0^L dz\int_0^\infty d\kappa\,
\kappa\Phi_n(\kappa)
\exp[-\kappa^2W^2(z)]
\left[1-\exp\left(-\frac{\Lambda_RL\kappa^2(1-z/L)^2}{k}\right)\right]
}
\]

其中：

- `W(z)`：no-turbulence G0 `1/e^2` intensity radius；
- `W_R=W(L)`；
- `Lambda_R=2L/(kW_R^2)`；
- `Phi_n` 使用与 production 相同的冻结 modified-von-Karman convention。

V6a 只作为弱/中弱条件的 absolute normalization check；强湍流下仍以 convergence + literature-bounded diagnostics 为主。

### 10.3 screen-level + propagation-level 双层验收

- Lane 1992：subharmonic / low-frequency anchor；
- Chen 2020：beam-wander / long-term-radius consequence anchor；
- Chahine 2020：longitudinal placement secondary anchor；
- modified-von-Karman exact PSD convention：`0.033 Cn2`, `kappa0=2pi/L0`, `kappam=5.92/l0`；
- weak Gaussian `W_LT` / beam-wander spectral references：只用于绝对归一化与 physics sanity，不替代 production finite-scale convergence。

任何 phase-screen algorithm 只有同时通过 screen-level PSD/structure-function 和 propagation-level absolute/convergence observables 才可进入 production。

---

## 11. targeted literature chains — CLOSED

### Nelson 2014

`docs/literature/NELSON_2014_BESSEL_AIRY_FAILURE_BOUNDARY_ANCHOR.md`

接受：Bessel/Airy quasi-nondiffracting robustness 在 `r0` 接近初始 aperture scale 时会明显失效；`D_T/r0` 是重要 failure coordinate，但 `r0=D_T` 不是 universal hard threshold。

### Jiang 2022/2026

`docs/literature/JIANG_2022_2026_FLAT_TOP_DIRECT_COMPETITOR_AUDIT.md`

接受：flat-top + turbulence + pointing/bias + average irradiance/received power 已存在；Paper 1 novelty 只能落在 distributed wave optics、realization-level low-tail、optimized Gaussian、resource matching 与 cross-mechanism failure map。

### Lane 1992

`docs/literature/LANE_1992_SUBHARMONIC_LOW_FREQUENCY_ANCHOR.md`

接受：低频补偿必须进入 formal validation；screen-level PSD/structure function 与 propagation-level beam wander 必须同时通过。

**Stage A broad literature search is CLOSED。** 后续只在结果冲突或审稿所需时定向补文献。

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

v0.3.1 candidate 只需再做一次短复核，检查：

1. OPB `rho_s / r95_T / omega_OPB=0.55` 是否自洽；
2. G1 CRN staged optimization 是否足以稳定 `Q5%` winner；
3. exact modified-von-Karman PSD/Fourier convention 是否可执行；
4. V6a/V7a absolute references 与 V10a/V10b split convergence 是否足以排除“自收敛到错误答案”。

若短审 PASS，则只授权：

1. Gaussian free-space；
2. finite-aperture displacement；
3. analytic jitter；
4. Gaussian phase-screen / multi-screen validation。

**即使 v0.3.1 PASS，也不立即授权 Bessel / OPB / flat-top production comparison。** 只有 Gaussian numerical chain 完成并通过 V0–V12 后，才进入 structured-field implementation。
