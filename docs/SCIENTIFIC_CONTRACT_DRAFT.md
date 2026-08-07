# SCIENTIFIC_CONTRACT_DRAFT

**状态：Scientific Contract v0.3 candidate — CONTRACT FREEZE GATE；短审通过前不授权 structured-beam 代码。**  
**日期：2026-08-07**  
**外部审查决策：REVISE**  
**审查输入：** `docs/review/EXTERNAL_REVIEW_DECISION_2026-08-07.md`  
**阶段边界：** `docs/RESEARCH_STAGE_BOUNDARY.md`

---

## 1. Paper 1 正式 scope

Paper 1 收窄为：

> **coherent、deterministic、single-aperture transmit fields 在 direct-detection finite-aperture UAV-FSO 链路中的跨机制 turbulence–jitter sensitivity / failure map。**

研究目标不是证明某一种 structured beam 普适更好，而是回答：

> 已有 turbulence-resistant deterministic transmit-field mechanisms 在加入 independent post-PAT residual pointing jitter 后，哪些 turbulence-only 优势能够保持、哪些压缩、哪些反转、哪些失效；这些变化是否能用少量尺度、capture 与 resource descriptors 形成可解释的 applicability / failure map？

### scope 内

- coherent deterministic scalar complex fields；
- single circular transmitter aperture；
- single circular finite receiver aperture；
- direct-detection received power；
- distributed atmospheric turbulence；
- turbulence-induced beam wander；
- independent post-PAT residual angular jitter；
- 一个 anisotropic-jitter sensitivity case；
- 一个 nonzero boresight-bias sensitivity case。

### scope 外

- partially coherent / source-ensemble optimization；
- multi-beam path-diversity architecture；
- vector / polarization / mode-diversity receiver task；
- coherent receiver / mode demultiplexing；
- single-mode-fiber coupling；
- AO instantaneous correction；
- full UAV 6-DOF / PAT/FSM time-domain controller；
- jitter PSD / temporal correlation in Paper 1 primary model；
- high-dimensional inverse design / neural network。

Airy path-diversity、partial coherence、vector/mode-diversity 可在文献讨论中保留，但不构成“数值集合不完整”的遗漏，因为它们被明确排除在本 scope 外。

---

## 2. Paper 2 边界

Paper 2 仍为 **CONDITIONAL GO**：只有 Paper 1 出现稳定、跨连续区域、且不能被 optimized Gaussian / receiver-scale matching 完全解释的 turbulence–jitter trade-off 后，才允许构造少参数 co-robust beam。

flattened-/super-Gaussian、Gaussian–LG/annular-like 目前仅为 Paper 2 设计种子，不得反向定义 Paper 1。

---

## 3. 第一轮 core field set — FROZEN

### 3.1 Gaussian G0 / G1

common-resource Gaussian：

\[
U_G(r)=C_G\exp(-r^2/w_G^2)
\exp\left[-i\frac{k r^2}{2f_G}\right]\Pi(r/a_T).
\]

G0：固定 common-resource reference。  
G1：预注册低维 optimized-Gaussian envelope。

### 3.2 zeroth-order Bessel — FROZEN FORM

主代表：circular-truncated `J0`

\[
U_B(r)=C_BJ_0\left(\chi_B\frac{r}{a_T}\right)\Pi(r/a_T).
\]

第一轮 representative：

\[
\chi_B=10.
\]

理由：位于 Eyyuboğlu 2013 文献映射得到的约 `O(5–20)` 主结构范围内部；这是 representative choice，不是文献 optimum claim。

在正式 common comparison 前必须先做一次 Eyyuboğlu square-window Bessel reproduction sanity case。Bessel–Gaussian 只有在结论对 hard truncation 敏感时才增加。

### 3.3 OPB — FROZEN FORM

第一版使用 continuum radial phase：

\[
U_{OPB}(r)=C_{OPB}A(r)
\exp\left[-i\frac{4}{3}k\sqrt{\beta}\,r^{3/2}\right]
\Pi(r/a_T).
\]

冻结 amplitude：

\[
A(r)=\exp(-r^2/w_A^2),
\qquad
w_A=0.65a_T.
\]

这与 G0 使用相同 Gaussian source occupation，使 OPB 第一层差异主要来自 radial phase，而不是额外 amplitude footprint。

正确 pin-width relation：

\[
\boxed{W(z)=\frac{1}{4k\beta z}}.
\]

定义 primary target pin scale：

\[
\omega_{OPB}=\frac{W(L)}{a_T}=0.35,
\]

因此：

\[
\beta=\frac{1}{4kLa_T\omega_{OPB}}.
\]

`omega_OPB=0.35` 是 literature-inspired representative choice，不声称是 Zhang 2019 或 joint channel 的 optimum。

不实现 32-filament / etched-mask discretization。

### 3.4 flat-top — FROZEN FAMILY

采用 nested multi-Gaussian family：

\[
U_N(r)=C_N\left[\frac{1}{N}\sum_{n=1}^{N}(-1)^{n-1}\binom{N}{n}
\exp\left(-n\frac{r^2}{w_F^2}\right)\right]\Pi(r/a_T).
\]

冻结：

- `N=1`：nested-Gaussian sanity；
- `N=4`：moderate representative；
- `N=8`：optional high-order stress only；
- Level A primary `w_F=0.65a_T`。

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

这些量原则上**报告而不全部硬匹配**。

---

## 5. secondary Level B — FROZEN AS `r80_R` MATCHING

唯一 secondary diagnostic：

> **receiver-plane no-turbulence/no-jitter `r80_R`-matched one-scale retuning。**

目标为与 G0 `r80_R` 匹配到：

\[
|r_{80,R}^{field}/r_{80,R}^{G0}-1|\le1\%.
\]

若预注册参数范围内没有唯一稳定解，标记 `NO R80 MATCH`，不得扩大搜索范围救结果。

### 每个 family 只开放一个 scale

- Bessel：`chi_B`，允许 `[6,18]`；
- OPB：`omega_OPB=W(L)/a_T`，允许 `[0.20,0.70]`；
- flat-top：固定 `N=4`，只调 `gamma_F=w_F/a_T`，允许 `[0.40,0.90]`。

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

定义 Paper 1 主 reference scale：

\[
w_{ref}=r_{80,R}^{G0}
\]

其中 `r80_R^G0` 在 primary physical scene、no-turbulence/no-jitter 条件下由 validated free-space propagator 计算。

Gaussian analytic jitter sanity check 仍单独使用 `1/e^2` intensity radius `W`，不得把 `r80` 与 `W` 混用。

### 6.2 G1 search space

定义：

\[
\gamma_G=w_G/a_T\in[0.35,0.95].
\]

第一版离散候选：

`0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95`。

quadratic focusing 用：

\[
u_f=L/f_G
\]

参数化，搜索：

`u_f = 0, 0.5, 1.0, 1.5, 2.0`，

其中 `u_f=0` 表示 collimated / `f_G=infinity`。

### 6.3 G1 objective

唯一主优化指标：

\[
\boxed{Q_{5\%}(H)}.
\]

G1 在每个正式场景点 `(tau,j,alpha_R)` 独立选择最佳 `(gamma_G,u_f)`，形成较强 Gaussian envelope。

不得换用 mean power、scintillation 或看完 structured-field 结果后改变优化目标。

### 6.4 optimization / evaluation independence

- `N_opt = 256` independent realizations，仅用于 G1 parameter selection；
- `N_eval = 1024` disjoint realizations，用于正式 common comparison；
- near-boundary / ranking-reversal point 若 bootstrap uncertainty 仍与零差异重叠，可增加到 `N_confirm = 4096`；不得默认对全参数面跑 4096。

`optimization seeds ∩ evaluation seeds = empty`。

所有 fields 在正式 evaluation 中使用 paired common turbulence/jitter realizations。

---

## 7. primary physical scene — FROZEN FOR v0.3

### 7.1 geometry

- `lambda = 1550 nm`；
- `L = 1000 m`；
- `D_T = 50 mm`，`a_T=25 mm`；
- `D_R = 50 mm`，`a_R=25 mm`；
- normalized `P_T=1` for simulation；absolute power not needed for direct received-fraction study。

该场景是**代表性 near-ground UAV-FSO mechanism scene**，不是声称所有 UAV terminal 都使用 50-mm apertures。

### 7.2 turbulence

primary atmosphere：constant-`Cn2` horizontal path，modified/von-Kármán spectrum。

baseline：

- `Cn2 = 1e-14 m^(-2/3)`；
- `L0 = 10 m`；
- `l0 = 5 mm`。

primary turbulence sweep：

- `Cn2 = 3e-15`；
- `1e-14`；
- `3e-14 m^(-2/3)`。

使用 plane-wave `r0=[0.423 k^2 Cn2 L]^(-3/5)` 作为 turbulence scale diagnostic 时，对本 scene 约对应：

- `r0≈162 mm`, `tau=D_T/r0≈0.31`；
- `r0≈78.5 mm`, `tau≈0.64`；
- `r0≈40.6 mm`, `tau≈1.23`。

这些 `r0/tau` 为该冻结 scene 的派生量，不是额外拟合参数。

outer/inner-scale sensitivity：

- `L0 = 5, 10, 20 m`；
- `l0 = 3, 5, 10 mm`。

依据边界：near-ground optical-turbulence literature 支持 inner scale 为毫米量级、outer scale 为数米到数十米量级；`10 m / 5 mm` 仅作为 baseline，不宣称唯一真实值。

`Cn2=1e-13` 可在 production module 通过验证后作为 optional strong stress，不属于第一轮主图必跑点。

### 7.3 phase-screen placement

primary constant-`Cn2` horizontal path：equal-spacing screens 起步。

screen number 由 convergence 决定，不冻结“固定 10/20 张”。候选 validation ladder：`4 -> 8 -> 16 -> 32`。

高度依赖 `Cn2(z)` 与 non-uniform placement 只作为 secondary extension。

---

## 8. jitter / boresight contract — FROZEN

### 8.1 primary residual model

transmitter angular tilt：

\[
U_0'(x,y)=U_0(x,y)
\exp[ik(\theta_xx+\theta_yy)].
\]

primary：

\[
\theta_x,\theta_y\sim\mathcal N(0,\sigma_\theta^2).
\]

`σ_theta` 是单轴 post-PAT residual LOS angular standard deviation。

主科学坐标：

\[
\boxed{j=\frac{L\sigma_\theta}{w_{ref}}}.
\]

primary jitter sweep：

`j = 0, 0.25, 0.5, 1.0, 1.5`。

现实 physical anchors 只映射到该 axis：

- fixed-wing high-performance actual-flight：约 `8–10 urad (1sigma)`；
- Trinh 2021 multirotor retro-FSO residual：约 `27–42 urad/axis`，只作 double-pass stress anchor。

不定义唯一“典型 UAV sigma_theta”。

### 8.2 anisotropic sensitivity

增加一个 `sigma_y/sigma_x=2` case，并保持总 per-axis-average variance 与 isotropic reference 相同：

\[
(\sigma_x^2+\sigma_y^2)/2=\sigma_\theta^2.
\]

因此：

\[
\sigma_x=\sigma_\theta/\sqrt{2.5},
\qquad
\sigma_y=2\sigma_x.
\]

只在一个代表 `tau,j` 条件验证 ranking sensitivity。

### 8.3 boresight sensitivity

增加一个 x-direction nonzero bias：

\[
\rho_b=0.5w_{ref},
\qquad
\theta_b=\rho_b/L.
\]

只作 secondary sensitivity，不加入全参数扫描。

### 8.4 turbulence beam wander separate ledger

必须分别记录：

- `rho_bw`：turbulence-only centroid wander；
- `rho_j=L theta_j`：independent residual jitter；
- `rho_b`：boresight bias。

不得把 phase-screen 已包含的 beam wander 再作为额外 statistical pointing loss 重复叠加。

---

## 9. receiver observable and statistics — FROZEN

realization-level finite-aperture power：

\[
P_R=\iint_{r\le a_R}|U_L|^2dA,
\qquad
H=P_R/P_T.
\]

### primary output

- full ECDF of `H`；
- `Q5%(H)`；
- paired difference distributions against G1；
- confidence interval / bootstrap uncertainty at claimed boundaries。

### secondary

- outage at explicitly stated threshold；
- mean `H`；
- scintillation；
- centroid / beam radius / profile descriptors。

point irradiance、peak intensity、scintillation、shape fidelity 不得单独证明 communication gain。

---

## 10. turbulence production numerical-validation table — FROZEN

在任何 structured-field multi-screen production run 前，Gaussian module 必须依次通过以下验证。

| Gate | 验证量 | v0.3 acceptance |
|---|---|---|
| V0 | full-grid power conservation, free space | relative drift `<=1e-4` |
| V1 | unclipped Gaussian free-space radius / phase | analytic disagreement `<=1%` |
| V2 | displaced Gaussian finite-aperture capture | analytic/high-accuracy quadrature disagreement `<=0.5%` |
| V3 | Gaussian jitter broadening | `W_eff^2=W^2+4L^2 sigma_theta^2`, radius disagreement `<=1%` |
| V4 | phase-screen PSD | resolved inertial-range spectral slope / level consistent with target; median relative level error `<=10%` over preregistered resolved band |
| V5 | phase structure function `D_phi(rho)` | median relative error `<=10%` over resolved inertial interval; recovered log-slope within `±0.10` of target inertial slope |
| V6 | low-frequency treatment | enabling/refining subharmonics or equivalent must converge `Var(rho_bw)`; production choice changes beam-wander variance `<5%` on further refinement |
| V7 | long-term radius | further low-frequency/grid refinement changes `W_LT <2%` |
| V8 | scintillation auxiliary | further screen/grid refinement changes scintillation `<5%` |
| V9 | screen-number ladder | choose smallest of `4/8/16/32` for which V6–V8 all pass on next refinement |
| V10 | grid/window | one grid/window refinement changes `W_LT <2%`, beam-wander variance `<5%`, scintillation `<5%` |
| V11 | maximum tilt aliasing | centroid shift linearity vs vacuum prediction within `1%`; full-grid power drift `<=1e-4`; no wrap-around contamination at max `j+bias` |
| V12 | propagation sampling | one longitudinal/transverse sampling refinement satisfies same observable tolerances as V10 |

### screen-level + propagation-level 双层验收

Lane 1992：正式 low-frequency / subharmonic anchor。  
Chen 2020：beam-wander / long-term-radius consequence anchor。  
Chahine 2020：non-uniform longitudinal placement secondary anchor。

生产模块不要求固定使用某一种 phase-screen algorithm；任何算法只要同时通过 screen-level PSD/structure-function 与 propagation-level observables 即可。

---

## 11. three targeted literature chains — CLOSED

### Nelson 2014

`docs/literature/NELSON_2014_BESSEL_AIRY_FAILURE_BOUNDARY_ANCHOR.md`

接受：Bessel/Airy quasi-nondiffracting robustness 在 `r0` 接近初始 aperture scale 时会明显失效；`D_T/r0` 是重要 mechanism-failure coordinate。不得把 `r0=D_T` 写成严格 universal threshold。

### Jiang 2022/2026

`docs/literature/JIANG_2022_2026_FLAT_TOP_DIRECT_COMPETITOR_AUDIT.md`

接受：flat-top + turbulence + jitter/bias + average irradiance/received power 已存在；2026 又有 pointing + gamma–gamma + average BER。Paper 1 novelty 只能落在 distributed wave optics、realization-level low-tail、optimized Gaussian、resource matching 与 cross-mechanism failure map。

### Lane 1992

`docs/literature/LANE_1992_SUBHARMONIC_LOW_FREQUENCY_ANCHOR.md`

接受：subharmonic / low-frequency handling 必须正式进入 validation；screen-level PSD/structure function 与 propagation-level beam wander 必须同时通过。

**Stage A broad literature search is CLOSED。** 后续仅在出现结果冲突或审稿所需时定向补文献。

---

## 12. Paper 1 hypotheses — FROZEN AS TESTS, NOT CLAIMS

- H1：turbulence-only superiority 不足以预测 turbulence+jitter low-tail reliability；
- H2：Bessel angular-spectrum redundancy 不自动提供 common lateral-displacement correction；
- H3：OPB narrow pin / autofocusing 可以保持 propagation structure，同时对 common tilt 产生 receiver loss；
- H4：flat-top broad capture 可能降低 jitter sensitivity，但收益可能被 source/receiver scale 与 peripheral energy 解释；
- H5：Nelson-type turbulence failure 与 mechanical-jitter failure 是两个不同机制层；
- H6：经过 G1 optimized Gaussian 与 Level B `r80` control 后，structured-beam ranking 可能压缩、反转或退化为无显著机制收益；
- H7：如果所有差异都可由 receiver-plane scale / optimized Gaussian 解释，则 Paper 1 必须接受负结果，不增加高维设计自由度救结论。

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
- “N=4 flat-top / chi_B=10 / omega_OPB=0.35 是文献证明的 optimum”。

---

## 14. code authorization gate

当前：

> **NO STRUCTURED-BEAM CODE AUTHORIZED YET。**

v0.3 candidate 需要一次短审，只检查：

1. field definitions / dimensions 是否自洽；
2. primary scene 是否合理；
3. G1 fairness 是否预注册完整；
4. numerical-validation tolerance 是否过松/过严；
5. 是否还存在会改变核心集合或 novelty 的 blocker。

若短审通过，代码顺序严格为：

1. Gaussian free-space；
2. finite-aperture displacement；
3. analytic Gaussian jitter；
4. Gaussian multi-screen validation；
5. Eyyuboğlu Bessel reproduction sanity；
6. 最后才加入 circular `J0` / OPB / flat-top common comparison。

不得跳过 Gaussian validation 直接跑 structured-field Monte Carlo。

---

## 15. Paper 2 启动条件

只有 Paper 1 证明存在稳定 mechanism trade-off，且该 trade-off：

- 跨连续 `(tau,j,alpha_R)` 区域存在；
- 经过 G1 optimized Gaussian 后仍存在；
- 经过 Level B `r80_R` control 后仍存在；
- 不是简单 Tx/Rx aperture、halo power 或 source-scale 交换；
- 可以转化成少参数设计原则；

才允许冻结 Paper 2 co-design contract。

否则 Paper 2 暂停，而 Paper 1 仍可作为机制失效/负结果论文推进。
