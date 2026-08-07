# Zhang et al. 2019：Optical Pin Beam turbulence mechanism 与 Paper-1 jitter 假设

## 文献身份

- Ze Zhang, Xinli Liang, Mihalis Goutsoulas, et al.
- *Robust propagation of pin-like optical beam through atmospheric turbulence*
- APL Photonics 4, 076103 (2019)
- DOI: `10.1063/1.5095996`
- CC BY 4.0
- 证据角色：**Paper 1 的 radial-autofocusing / inward-energy-flow mechanism + real-atmosphere experiment anchor**；不是 UAV-jitter 参数来源，也不是 production turbulence-model anchor。

## 1. 机制定位

OPB 的主要机制不是普通 Bessel self-healing，而是：

- 方向截断的 Airy-like radial fragments；
- 成对 opposite transverse wavevectors；
- side-lobe / peripheral energy 持续向 central region 输运；
- free-space autofocusing / self-focusing；
- 在设计传播区间形成窄的 Bessel-like pin。

因此 Paper 1 将 OPB 与 Bessel-like angular-spectrum redundancy 分开处理。

## 2. 实验资源

原论文主实验包括：

- `lambda = 532 nm` CW laser；
- output power约 `2 W`；
- engineered photoetched phase mask；
- mask diameter约 `5 cm`；
- measured modulation efficiency约 `90%`。

原论文真实 mask / wavelength / aperture 只作为实验实现背景，不直接继承到 1550-nm UAV-FSO primary scene。

## 3. continuum radial representation

外部审查后，Paper 1 第一版冻结使用 continuum radial phase，不实现真实 32-filament 或 etched-mask discretization。

source field 表示为：

\[
U_{OPB}(r)=C_{OPB}A(r)
\exp\left[-i\frac{4}{3}k\sqrt{\beta}\,r^{3/2}\right]
\Pi(r/a_T).
\]

其中：

- `A(r)`：待 v0.3 physical-scene freeze 给出明确 amplitude envelope；
- `beta`：inverse-length parameter，控制 radial phase / target pin scale；
- `C_OPB`：common aperture 后 equal-`P_T` normalization；
- `a_T`：common circular transmitter aperture radius。

## 4. 重要更正：pin-width scaling

原论文 Eq. (5) 对 characteristic pin width 的关系为：

\[
\boxed{W(z)=\frac{1}{4k\beta z}}.
\]

**此前本文件错误写成 `1/(4 k beta^2 z)`，现已更正。**

错误版本量纲不成立，也会错误地改变 `beta` 与 target pin width 的映射。

参数映射必须使用：

\[
\beta=\frac{1}{4kzW(z)}.
\]

如在 primary range `L` 定义 target scale：

\[
\omega_{OPB}=\frac{W(L)}{a_T},
\]

则

\[
\beta=\frac{1}{4kLa_T\omega_{OPB}}.
\]

可选的 aperture-edge phase-strength descriptor 为：

\[
\chi_{OPB}=\frac{4}{3}k\sqrt{\beta}\,a_T^{3/2}.
\]

Paper 1 只选择 `omega_OPB` 或 `chi_OPB` 中一个作为实现自由度，避免重复参数化。

## 5. 原论文 real-atmosphere evidence

原论文在 open-country atmosphere 中展示约 kilometer-scale propagation：

- OPB central main-lobe width 从 source 附近约 `6 mm` 到 1 km 后约 `9 mm`；
- 原文 ordinary Gaussian comparison 在 1 km 后扩展到约 `17 cm`。

这支持 OPB 在该实验设置下维持 narrow central structure，但不能直接继承其 effect size，因为原 Gaussian 没有针对相同 receiver-distance objective 做 optimized focusing。

原论文还用 laboratory turbulent air 做 temporal intensity-stability comparison，但主指标不是本项目的 finite-aperture low-tail received power。

## 6. Gaussian baseline warning

OPB phase engineering 本身包含很强的 autofocusing / radial phase design，而原论文 Gaussian 是没有对应优化的普通 Gaussian。

因此 Paper 1 必须使用：

- common-resource G0；
- 预注册 `w_G/f_G` 搜索的 optimized G1；
- common aperture / equal transmitted power；
- no-disturbance `H0` 和 `r80_R` resource ledger。

不得直接引用原文 OPB-vs-Gaussian 光斑或峰值差作为本项目预期 structural gain。

## 7. turbulence-model evidence boundary

Zhang 2019 是 mechanism / experiment anchor，不是 production distributed-turbulence numerical anchor。

它不提供本项目所需的：

- validated low-frequency beam-wander statistics；
- formal multi-screen convergence；
- realization-level finite-aperture ECDF / `Q5%`；
- independent mechanical residual jitter。

因此 production turbulence contract 仍由 Lane 1992、Chen 2020、Chahine 2020 等数值方法链约束。

## 8. Paper-1 jitter hypothesis

以下是本项目机制推论，不是 Zhang 2019 已验证结论。

若 OPB 内部一对 transverse wavevectors 近似为：

\[
+\mathbf q,\qquad-\mathbf q,
\]

而 transmitter common mechanical tilt 使整个 source field 乘以：

\[
\exp(i k\boldsymbol\theta\cdot\mathbf r),
\]

则 angular spectrum 中两分量变成：

\[
+\mathbf q+k\boldsymbol\theta,
\qquad
-\mathbf q+k\boldsymbol\theta.
\]

内部 `±q` pairing 仍可能支持 pin formation，但共同的 `k theta` 不会被抵消。

因此待验证假设是：

> **OPB 可以保持 propagation-side pin formation，同时整个 useful pin region 围绕 tilted axis 偏移，从而对固定 receiver aperture 产生明显 pointing loss。**

这正是 Paper 1 要区分的：

\[
\text{propagation robustness}
\neq
\text{receiver pointing robustness}.
\]

## 9. v0.3 field freeze

### 已冻结

- OPB 进入第一轮 core set；
- 使用 continuum radial phase；
- 不实现 32-filament / etched-mask details；
- 使用正确关系 `W(z)=1/(4 k beta z)`；
- common circular aperture 后 equal-`P_T` normalization；
- Level B 只允许一个 scale parameter 做 receiver-plane `r80_R` matching。

### 仍需在 v0.3 physical-scene table 中给出

- `A(r)` 的具体 canonical choice；
- representative `omega_OPB=W(L)/a_T` 或等价 phase strength；
- 允许的 one-scale retuning interval。

## 10. 禁止表述

- OPB self-focusing 会自动把 common pointing error 拉回 nominal receiver；
- Zhang 2019 已证明 OPB 抗 UAV residual jitter；
- 原论文 ordinary Gaussian comparison 等价于 optimized Gaussian；
- 2019 实验已证明 finite-aperture low-tail reliability 增益；
- 错误公式 `W(z) ~ 1/(4 k beta^2 z)`。

## 当前状态

**READ / CORRECTED MECHANISM ANCHOR / CORE-SET REPRESENTATIVE。**

OPB 文献机制链对 Scientific Contract v0.3 已足够；下一步不继续横向扩展 OPB 文献，而是冻结 `A(r)` 与 representative pin scale 后进入合同短审。
