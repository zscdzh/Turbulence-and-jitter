# PAPER1_COMMON_RESOURCE_GATE_DRAFT

**状态：外部审查后修订；作为 Scientific Contract v0.3 candidate 的输入，不是代码授权。**

本文件把 `PAPER1_PARAMETER_MAPPING_MATRIX.md` 中仍需人工裁决的内容压缩成最小 Gate。外部审查 Decision 为 **REVISE**：Level A 接受，Level B 改为 receiver-plane `r80_R`-matched one-scale diagnostic；核心集合冻结为 Gaussian + zeroth-order Bessel + OPB + flat-top。

## Gate A — common physical resources

第一版统一：

1. transmitter：single circular hard aperture；
2. equal post-aperture transmitted power `P_T`；
3. receiver：single circular finite aperture，direct detection；
4. all fields share exactly the same turbulence and jitter realizations；
5. source-plane field after aperture is numerically renormalized to equal `P_T`；
6. common `lambda, L, D_T, D_R`。

这一级是正式主比较，不通过任何 receiver-plane matching 人为调平各结构。

## Gate B — resource ledger：报告但不全部硬匹配

所有场同时报告：

- `r50_T, r80_T, r95_T`；
- peripheral / halo energy fraction；
- transverse-frequency / angular-spectrum cost；
- no-disturbance finite-aperture capture `H0`；
- receiver-plane `r50_R, r80_R`；
- source / receiver second moment，如数值稳定；
- generation efficiency / conversion loss if literature-supported。

这些量用于解释收益来源，而不是在 Level A 中全部配平。否则会把结构机制本身一并归一掉。

## Gate C — secondary scale-control：冻结为 `r80_R`-matched

唯一 secondary diagnostic 为：

> **receiver-plane no-turbulence/no-jitter `r80_R`-matched one-scale retuning。**

理由：

- `H0` 强依赖 receiver aperture，对 ring / halo / autofocusing field 可能多解；
- `r50_R` 对 Bessel / OPB 等外围能量结构过于偏向核心；
- `r80_R` 更能暴露 peripheral-energy cost，同时仍然是清楚的 receiver-plane scale descriptor。

`H0` 必须继续报告，但**不作为 matching constraint**。

每个 structured family 只能开放一个预注册尺度变量：

- Bessel：`chi_B = k_r a_T`；
- OPB：`beta` 的等价单尺度表示，优先使用 target pin-scale `W(L)/a_T`；
- flat-top：固定 order `N`，只调 common radial scale `gamma_F`。

禁止在 Level B 同时改变 family order 与 radial scale，禁止形成隐性多参数优化。

## Gate D — Gaussian reference and G1 optimization

### G0

common-resource Gaussian 用于定义固定参考尺度：

\[
j=\frac{L\sigma_\theta}{w_{ref}}.
\]

`w_ref` 在 v0.3 中冻结为 G0 无湍流、无抖动 receiver-plane 的固定 beam-radius convention；若 hard clipping 使 `1/e^2` radius 不稳定，则改用 G0 的 `r80_R`，且全文只使用一种 convention。

### G1 optimized-Gaussian envelope

G1 必须预注册以下四项后才允许执行：

1. `w_G` 搜索边界；
2. quadratic-phase / equivalent focus `f_G` 搜索边界；
3. 唯一主优化指标；
4. optimization ensemble 与 final evaluation ensemble 完全分离。

当前推荐主优化指标：

\[
Q_{5\%}(H).
\]

完整 ECDF 为核心展示；outage 仅作为给定阈值下的辅助结果。

是否逐 `(tau,j,alpha_R)` 独立优化必须在 v0.3 中预注册，不能看完 structured-beam 结果后再决定。

## Gate E — frozen first-round numerical scope

Paper 1 第一轮数值 scope 限定为：

> **coherent、deterministic、single-aperture transmit fields + direct-detection finite-aperture receiver。**

核心集合冻结为：

- Gaussian G0 / G1；
- zeroth-order Bessel；
- OPB continuum radial phase；
- flat-top representative。

不进入首轮数值集合：

- Airy path-diversity array：multi-beam architecture，只保留文献/架构讨论；
- partial coherence：source ensemble / statistical beam family，已有成熟 turbulence+pointing joint optimization，只保留讨论层成熟对照；
- vector / mode-diversity：超出当前 direct-detection single-aperture scope。

## Gate F — field-specific freezes

### Bessel

主代表冻结为 **circular-truncated `J0`**：

\[
U_B(r)=C_B J_0\left(\chi_B\frac{r}{a_T}\right)\Pi(r/a_T).
\]

进入正式比较前先做一次 Eyyuboğlu 2013 square-window reproduction sanity check。只有结论对 hard truncation 形式敏感时，才增加 Bessel-Gaussian sensitivity check。

### OPB

第一版冻结：

- continuum radial phase；
- 不实现真实 32-filament / etched-mask discretization；
- pin-width 关系必须使用

\[
W(z)=\frac{1}{4k\beta z},
\]

不得出现 `beta^2`；
- `A(r)`、phase-strength / target pin-scale 的最终代表值仍需在 v0.3 physical-scene freeze 中写明。

### flat-top

第一版冻结为：

- `N=1` nested Gaussian sanity；
- 一个 moderate-order representative；
- 一个 high-order point 仅作为可选 stress case；
- 每个 order 在 common circular aperture 后重新 equal-power normalization。

moderate `N` 的具体数值由 Jiang 2022/2026 direct-competitor audit + 2006/2008 resource chain 冻结；不做大范围 order optimization。

## Gate G — jitter scope

现有证据足以启动 dimensionless study，不再要求代码前必须找到 one-way active-transmitter multirotor residual。

主坐标：

\[
j=\frac{L\sigma_\theta}{w_{ref}}.
\]

现实映射只作为 evidence-labelled anchors：

- fixed-wing high-performance flight：约 `8–10 urad (1sigma)`；
- Trinh 2021 multirotor retro-FSO：`27–42 urad/axis`，仅作 double-pass compact-tracker stress anchor。

第一版 jitter cases：

- zero-mean isotropic Gaussian 为主；
- 一个 anisotropic covariance sensitivity；
- 一个 nonzero boresight-bias sensitivity。

Paper 1 定位为 ensemble/static reliability study，因此 PSD、correlation time、FSM/controller dynamics 暂不进入主模型。

## Gate H — production turbulence validation

正式 multi-screen 之前，Gaussian turbulence module 至少需要：

1. phase-screen PSD / phase-structure-function validation；
2. low-frequency treatment / subharmonic validation；
3. turbulence-induced beam-wander variance；
4. long-term beam radius；
5. scintillation / short-term diagnostics；
6. phase-screen number convergence；
7. grid/window convergence；
8. propagation sampling convergence；
9. 最大 mechanical tilt 下的 wrap-around / aliasing convergence；
10. von Karman `L0/l0` baseline 与 sensitivity range。

constant-`Cn2` horizontal primary scene 可优先使用 equal-spacing screens；高度依赖 `Cn2(z)` 只作为 secondary case。

## 当前 Gate 决策

**NO CODE YET / CONTRACT FREEZE GATE。**

进入代码前只剩：

1. 完成 Nelson、Jiang 2022/2026、Lane 1992 三条定向文献链；
2. 修正 OPB 锚点公式并冻结 OPB amplitude / scale；
3. 冻结 flat-top canonical expression / moderate order；
4. 冻结一个 primary physical scene、G1 搜索边界与 Gaussian validation tolerance table；
5. 形成并短审 Scientific Contract v0.3 candidate。
