# Zhang et al. 2019：Optical Pin Beam 的 turbulence mechanism 与 Paper-1 jitter 假设

## 文献身份

- Ze Zhang, Xinli Liang, Mihalis Goutsoulas, et al.
- *Robust propagation of pin-like optical beam through atmospheric turbulence*
- APL Photonics 4, 076103 (2019)
- DOI: `10.1063/1.5095996`
- CC BY 4.0
- 证据角色：**Paper 1 的 self-focusing / pin-like turbulence-resistance 机制锚点与实验锚点**；不是 quantitative UAV-jitter 文献，也不是正式 turbulence-model 锚点。

## 1. 为什么这篇对 Paper 1 特别重要

这篇论文提出 optical pin beam (OPB)，其主要卖点不是普通 Bessel self-healing，而是：

- 通过方向截断的 Airy-like fragments 组成径向相位结构；
- 成对的相反 transverse wavevectors 在传播过程中逐步抵消；
- side-lobe energy 持续向 central main lobe 汇聚；
- 光束表现为无非线性的 autofocusing / self-focusing；
- 在长距离传播中形成窄的 Bessel-like central structure。

因此它代表一种与普通 Bessel angular-spectrum redundancy 不同的 turbulence-resistant 机制。

更重要的是，该机制天然给出 Paper 1 的一个可证伪问题：

> 内部 transverse-wavevector cancellation 能否抵抗一个施加给整个发射场的 common-mode mechanical tilt？

原论文没有研究该问题。

## 2. 实验发射与实现资源

主实验使用：

- CW laser：`lambda = 532 nm`；
- laser output power：约 `2 W`；
- engineered photoetched phase mask；
- mask diameter：约 `5 cm`；
- mask measured modulation efficiency：约 `90%`，作者定义为 10 m 处生成 OPB 的功率与 incident Gaussian beam 功率之比。

phase mask 由同心环形台阶构成，沿任意 radial direction 实现近似 Airy-type cubic phase。作者指出，当 phase fragments 数量超过约 32 时，生成场接近 radially symmetric Airy / autofocusing field。

这说明 OPB 不是“零代价的新光束”：它使用明确的 phase mask、有限 transmitter diameter，并把相当多能量放在 side-lobe / inward-flow reservoir 中。Paper 1 必须记录这些资源。

## 3. 机制：不是静态窄光斑，而是纵向能量汇聚

作者的物理图像是：

1. 每对 Airy-like fragment 从相反方向向中心弯曲；
2. 不同 fragment 在不同 z 位置逐步汇聚；
3. side-lobe energy 向 central lobe 输运；
4. main lobe 的 inward / outward transverse energy flow 最终趋于平衡。

论文通过 Poynting-vector 分布说明：在其实验设计中，大约 60 m 后 central lobe 已出现较好的 inward/outward flow balance，90 m 时 main-lobe transverse energy flow 更接近 quasi-steady。

因此 OPB 的“稳定”不是简单的静态 Gaussian narrow spot，而是一种持续的 distributed transverse-energy replenishment。

## 4. 理论尺度关系

在 radial-continuum 极限，作者写出 Fresnel/Hankel propagation，并取 Airy-type radial phase：

\[
\psi_0(\rho)=A(\rho)\exp\left[-i\frac{4}{3}k\beta^{1/2}\rho^{3/2}\right],
\]

其中 `beta` 是带 inverse-length dimension 的 phase-frequency 参数。

stationary-phase 近似得到 Bessel-like propagation form，并给出其 characteristic width 随传播距离近似：

\[
W(z)\propto \frac{1}{4k\beta^2 z}.
\]

核心物理含义是：在其设计区间内 OPB 不像普通 Gaussian 那样随 z 扩展，反而可以随传播逐渐变窄 / autofocusing。

这也是为什么 OPB 可能同时具有很高 aligned peak intensity 和非常窄的 capture core。

## 5. turbulence 实验结果到底证明了什么

### 5.1 kilometer-scale outdoor experiment

作者在 open-country real atmosphere 中比较 OPB 与没有 phase mask 的 Gaussian：

- OPB main-lobe width 从 mask 附近约 `6 mm` 变到 1 km 后约 `9 mm`；
- 对照 Gaussian 在 1 km 后扩展到约 `17 cm`，并明显起伏；
- 作者称 Gaussian 与 OPB 来自同一 laser output size/power condition。

这是很强的**真实大气传播展示**，证明 OPB 在该设置下能保持窄 central structure。

但它没有给出：

- `Cn2` / `r0` / Rytov variance；
- finite receiver aperture power；
- received-power ECDF；
- outage / BER；
- turbulence-induced beam-wander statistics；
- independent mechanical jitter。

因此它不能直接作为我们最终 quantitative channel benchmark。

### 5.2 45 m indoor turbulent-air stability experiment

作者用 central air conditioner 产生 turbulent air，记录 45 m 后图样：

- 290 frames；
- observation time：20 s；
- 定义一个 integrated relative intensity-variation metric：

\[
\Delta I_t=
\frac{\int |I(x,y,t)-I_{mean}(x,y)|dxdy}
{\int I_{mean}(x,y)dxdy}.
\]

OPB 的该指标明显低于 Gaussian。

但图中 intensity 使用 arbitrary units，并明确用于 stability analysis，不是 absolute-power measurement。

因此本实验支持：

> OPB spatial-pattern / temporal-intensity stability 在该人工 turbulence 条件下优于其 Gaussian 对照。

不能直接升级为：

> OPB finite-aperture communication reliability 更高。

## 6. 一个非常重要的 Gaussian baseline 问题

原论文中的 Gaussian 对照是**没有 phase mask 的 normal Gaussian beam**。

OPB phase mask 本身同时执行了强烈的 radial phase engineering / autofocusing；作者在 60 m 实验中报告 OPB FWHM 小于 3 mm，而 Gaussian 仍约 17 mm 宽，OPB peak intensity 超过 Gaussian 约一个数量级。

因此这并不是“针对同一 receiver-distance objective 优化过的 focused Gaussian”与 OPB 的严格公平比较。

Paper 1 必须避免复制这种 baseline：

- Gaussian 应允许合理 quadratic phase / focusing；
- 至少匹配相同 transmitter clear aperture 和 total power；
- 报告 no-turbulence receiver-plane spot / encircled-energy / collected power；
- 再判断 OPB turbulence benefit 有多少来自结构机制，有多少来自其本身的 autofocus design。

这一点是该论文对我们非常重要的**竞争基线警告**。

## 7. 作者自己承认 turbulence 理论并不严格

论文在结论前明确说明：

- 本文重点是 OPB experimental generation 与 robust free-space propagation；
- **没有给出 rigorous numerical/theoretical modeling of Kolmogorov turbulence**；
- phase-screen turbulence simulations 被放在 supplementary material；
- 更严格的 statistical-turbulence dependence 需要 future studies。

因此本论文是机制 / 实验锚点，而不是我们 formal multi-screen model 的参数依据。

## 8. 原论文对 turbulence robustness 的机制解释

作者提出一个定性解释：

- turbulence 会给 beam 引入 random transverse wavevectors；
- OPB 内部设计存在成对 opposite transverse wavevectors；
- 这些横向成分在不同 propagation distances 上持续 cancellation；
- 因此 central intensity distribution 能保持稳定。

这是合理的 mechanism hypothesis，但原文没有用严谨的 stochastic-wave-optics decomposition 证明“随机 turbulence k-vector cancellation”是 observed robustness 的唯一原因。

Paper 1 应把它视为**待检验机制主张**，而不是先验事实。

## 9. Paper 1 的关键新推论：common-mode mechanical tilt 不会被内部 cancellation 消掉

这是本项目基于原论文机制做出的**理论先验，不是原文结论**。

若 OPB 内部一对 transverse wavevectors 近似为

\[
+\mathbf q,\qquad -\mathbf q,
\]

则 ideal pairing 的 common transverse component 为零。

但 independent platform pointing tilt 等价于在整个 source field 上乘

\[
\exp(i k\boldsymbol\theta\cdot\mathbf r),
\]

从 angular-spectrum 角度，它给**所有**组成分量加入相同 common shift `k theta`：

\[
+\mathbf q\rightarrow +\mathbf q+k\boldsymbol\theta,
\]

\[
-\mathbf q\rightarrow -\mathbf q+k\boldsymbol\theta.
\]

因此内部 ±q 可以相互抵消，但 common-mode tilt 不会消失。两分量的 common component 仍指向同一个 tilted axis。

物理上更直观地说：

> OPB 可能仍然围绕“被机械倾斜后的传播轴”完成 autofocusing / pin formation，但固定在名义轴上的 receiver aperture 并不会被 OPB 的内部 self-focusing 自动拉回。

这正是 Paper 1 要验证的：

- **propagation robustness**：光束自身是否仍形成稳定 pin；
- **receiver robustness**：这个 pin 是否仍落在固定接收孔径里。

两者不能混为一谈。

## 10. 为什么 OPB 可能是最强的 Paper-1 机制对照之一

OPB 在原论文中呈现：

- turbulence-only 下很强的 narrow-core / shape stability；
- real-atmosphere kilometer-scale demonstration；
- 明确的 inward-energy-flow 与 transverse-wavevector mechanism；
- 高 phase-mask efficiency；

同时它的 aligned core 很窄，这恰好意味着：如果 global pointing displacement 不被内部机制抵消，则 fixed-aperture capture 可能对 jitter 很敏感。

因此它可能成为 Paper 1 最典型的命题：

> **一种对 turbulence propagation 很强的结构，并不自动对 independent LOS jitter 强。**

注意：当前仍只是高价值待证伪假设，尚无联合模拟支持。

## 11. 当前接受与不接受

### ACCEPTED AS LITERATURE EVIDENCE

- OPB 代表 self-focusing / inward-energy-flow 类 turbulence-resistant mechanism；
- 2019 论文提供真实大气 kilometer-scale qualitative/experimental robustness evidence；
- Gaussian baseline 未针对相同 receiver objective 做充分优化，因此不能直接继承 reported OPB-vs-Gaussian effect size；
- 原文 turbulence modeling 不是 formal numerical anchor；
- intensity stability / narrow spot 不等价于 finite-aperture low-tail communication reliability。

### PAPER-1 HYPOTHESIS, NOT YET EVIDENCE

- common-mode mechanical tilt 不会被 OPB 内部 opposite-wavevector cancellation 自动消除；
- OPB 可能在保持自身 pin structure 的同时整体偏离 receiver；
- narrow pin core 可能使其出现明显 turbulence–jitter trade-off。

### NOT FROZEN

- Paper 1 最终采用哪一种 OPB phase parameter；
- mask/aperture 尺度；
- 与 optimized Gaussian 的 exact matching protocol；
- jitter sensitivity threshold；
- OPB 是否最终优于或劣于 Bessel / Airy / flat-top。

## 12. 对后续精读的影响

读完本论文后，OPB 应继续保留为 Paper 1 高优先级代表机制。

下一步需要用 Airy / path-diversity 文献判断：

> OPB 的 inward-flow / opposite-wavevector cancellation 与 Airy self-bending/path-diversity 到底是同一机制的径向变体，还是在 Paper 1 中值得保留为两个独立机制。

这将直接决定 Paper 1 最终是否保留 Bessel、Airy、OPB 三个 separate families，还是将 Airy/OPB 合并成一个 broader caustic/autofocusing mechanism family。
