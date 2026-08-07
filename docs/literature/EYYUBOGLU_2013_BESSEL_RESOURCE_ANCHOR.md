# Eyyuboğlu / Voelz / Xiao 2013：Bessel turbulence robustness 与资源公平性锚点

## 文献身份

- Halil T. Eyyuboğlu, David Voelz, Xifeng Xiao
- *Scintillation analysis of truncated Bessel beams via numerical turbulence propagation simulation*
- Applied Optics 52(33), 8032–8039 (2013)
- DOI: `10.1364/AO.52.008032`
- 证据角色：**Paper 1 的 Bessel / self-healing 类 turbulence-only 机制与资源公平性锚点**；不是 pointing-jitter 文献，也不是最终 multi-screen 数值实现锚点。

## 1. 该文献真正研究了什么

论文使用 random phase-screen wave-optics simulation 研究**有限截断 Bessel beams 在大气湍流下的 scintillation**，并与 classical Gaussian beam 做比较。

它的核心价值不只是“Bessel scintillation 更低”，而是作者进一步加入了 received-power criterion，发现此前看起来广泛存在的 Bessel 优势大幅收缩。这一点直接支持本项目 Paper 1 的资源公平性护栏。

## 2. 发射场定义与资源

论文采用

\[
u_s(s,\phi)=J_n(a_B s)\exp(i n\phi),
\]

其中：

- `n`：Bessel beam order；
- `a_B`：横向尺度 / width parameter，单位 `cm^-1`；
- 理想 Bessel beam 无限能量，因此论文用**方形源平面硬截断**实现有限能量：

\[
-S/2\le s_x\le S/2,\qquad -S/2\le s_y\le S/2.
\]

作者使用：

- `S = 10 cm` 与 `40 cm` 两档 square source-plane side length；
- `n = 0,1,2,3,4,5`；
- `S=10 cm` 时 `a_B = 1–5 cm^-1`；
- `S=40 cm` 时 `a_B = 0.2–1 cm^-1`。

因此该文献的 Bessel 光束不是 Gaussian-apodized Bessel-Gaussian，而是**square-window truncated Bessel field**。

### 对本项目的影响

这一定义不能不经讨论直接变成 Paper 1 最终代表场，因为我们的实际 UAV-FSO 发射硬件更自然是 circular clear aperture。后续需要决定：

1. 为忠实复现该 turbulence claim，先保留 square-truncated field；或
2. 用 circular-truncated / Bessel-Gaussian 作为机制代表，但明确这已经不是该文献的逐参数复现。

在 Stage A 结束前暂不冻结。

## 3. turbulence propagation 方法

作者采用 split-step random phase-screen propagation：

\[
u_{m+1}=\mathcal F^{-1}\left\{\mathcal F[u_m\exp(i\phi_m)]H_m\right\}.
\]

相位屏使用 von Kármán spectrum，正文给出 inner scale `l0`、outer scale `L0` 进入 PSD 的表达式。

正式数值设置包括：

- propagation path 分成 **21 intervals**；
- associated phase screens：`512 × 512` grid；
- 各 transverse plane 使用相同 grid-point 数量；
- 使用 scaled multistep propagation 处理随传播增长的 beam size；
- 每个绘图点平均 **500 turbulence realizations**；
- propagation length 扫描到约 `5.5 km`。

### 对本项目的边界

该论文说明：多屏 distributed propagation 用于比较 structured beams 在 2013 年就已存在，因此本项目不能把 multi-screen 本身作为创新。

但该文献没有建立我们当前需要的 low-frequency / subharmonic beam-wander accuracy 契约，也没有把 `rho_bw` 单独提取出来。因此它不能替代 Lane 1992、phase-screen precision 2020 等数值方法锚点。

## 4. 三种 scintillation 指标

### 4.1 point scintillation

\[
b(\mathbf r,L)=\frac{\langle I^2(\mathbf r,L)\rangle}{\langle I(\mathbf r,L)\rangle^2}-1.
\]

### 4.2 aperture-averaged scintillation

对圆形 receiver aperture 半径 `R_a` 内接收功率：

\[
P_R=\int_0^{R_a}\int_0^{2\pi} rI(r,\theta;L)\,d\theta\,dr,
\]

作者使用

\[
b(L)=\frac{\langle P_R^2\rangle}{\langle P_R\rangle^2}-1.
\]

这已经是 finite-aperture power fluctuation，而不是 point intensity fluctuation。

### 4.3 scintillation per unit received power

作者进一步定义

\[
b_P(L)=\frac{b(L)}{\langle P_R\rangle}.
\]

并用 Gaussian / Bessel 的比值比较：

\[
b_R=\frac{b_B}{b_G},\qquad b_{PR}=\frac{b_{PB}}{b_{PG}}.
\]

这一步是本文最值得我们保留的思想，但**不应原样继承这个指标**。

原因是 `b_P` 是“scintillation 除以平均功率”的复合量，量纲依赖功率归一化，也不是直接的通信 reliability metric。它只能说明：单看 normalized fluctuation 会掩盖平均接收功率损失。

本项目应采用更直接的处理：

> 固定 / 报告 equal transmitted resource → 对每个 realization 直接比较 finite-aperture `P_R` → 使用 ECDF、低分位功率、outage；scintillation 只保留为辅助机制量。

## 5. equal-source-power comparison 的真正含义

作者专门构造了 equal source power 的 Gaussian / Bessel 组。Table 1 中典型设置为：

- `S=10 cm, P_s≈0.3 mW`；
- `S=40 cm, P_s≈10.8 mW`；
- `S=40 cm, P_s≈21.1 mW`；
- Bessel 通过调整 `a_B` 匹配 source power；
- Gaussian 通过调整 source-size parameter `alpha_s` 匹配 source power。

这比“各画一张归一化光强图”严格得多，但仍然不是完整的资源等价，因为：

- source-plane spatial extent / aperture usage 不一定相同；
- Bessel 的大量能量位于外围 ring；
- Gaussian 与 Bessel 的 diffraction / receiver-plane scale 未被统一匹配；
- optical-generation efficiency 未进入比较。

论文自己发现剩余 Bessel 优势更容易出现在**larger source plane dimensions**，说明 aperture resource 本身就在影响结论。

因此 Paper 1 的公平比较至少需要同时报告：

- total transmitted power；
- actual transmitter clear aperture；
- source-plane encircled-energy / peripheral-energy distribution；
- receiver aperture；
- no-disturbance received power；
- receiver-plane characteristic scale；
- 必要时 generation loss。

equal power 是必要条件之一，但不是唯一公平口径。

## 6. 最关键结果：加入 received-power criterion 后优势大幅收缩

作者得到：

1. 在其扫描条件下，`n=0` Bessel 的 on-axis scintillation 几乎一直最低；
2. equal source power 下，如果只看 aperture-averaged scintillation，Bessel 尤其在小 receiver aperture 与低 beam order 下经常优于 Gaussian；
3. 但一旦使用 `scintillation per unit received power`，这些 advantageous regions **大部分消失**；
4. 仅 `n=0,1` 在部分条件下仍保留一些优势，主要对应：较小 receiver aperture、较大 source power、较大 source-plane dimensions 与中等 propagation length。

这说明一个非常重要的 Paper 1 原则：

> **“扰动后形状更稳定 / scintillation 更低”不等于“通信收到的有效功率更可靠”。**

## 7. higher-order Bessel 的 metric artifact

作者发现较高 order `n=1,2,3...` 往往有更高 scintillation，并给出一个很重要的解释：高阶场更趋向 annular pattern，on-axis mean intensity 很低；scintillation index 是归一化方差，因此当 denominator 很小时，会对很小的绝对 intensity change 显得非常敏感。

这再次支持本项目：

- 不用 point scintillation 排 structured beams；
- 不用 normalized variance 单独证明通信优势；
- 主链必须回到 finite-aperture absolute / normalized received power distribution。

## 8. 不能把这篇论文写成“self-healing 已被证明导致低 scintillation”

这是一个需要特别防止的过度解释。

论文 introduction 会提到 Bessel 的 nondiffracting / truncated propagation 特性，结论也推测 low-order Bessel 的 reduced diffraction 可能对小 aperture 有帮助；但作者明确写道：

> 小接收孔径下 reduced scintillation 的具体机制在当时仍不清楚。

因此这篇文献支持：

- low-order truncated Bessel 在特定 turbulence-only 条件下的低 scintillation claim；
- receiver aperture / source aperture / received power 会强烈改写该 claim；

但**不能单独支持**：

- self-healing 就是其低 scintillation 的确定原因；
- self-healing 自动提高 finite-aperture reliability；
- Bessel 自动抗 independent pointing jitter。

Paper 1 后续正应该对这些机制表述进行拆分验证。

## 9. 对 independent jitter 的证据状态

本文没有把 independent mechanical pointing jitter 加入 turbulence propagation。

虽然 introduction 引用了 Bessel-Gaussian misalignment 的自由空间前序，但本研究本身是 turbulence-only。

因此它非常适合作为我们的 Paper 1 输入：

> 已有 turbulence-only 优势在文献中成立到什么程度？加入 independent lateral displacement 后是否保持？

而不是作为 jitter 参数来源。

## 10. 对 Paper 1 的直接裁决

### ACCEPTED

1. Bessel 类保留为 Paper 1 候选机制；优先考虑低阶、尤其 `n=0` 作为直接探测代表，避免无必要的 OAM/order 模式动物园。
2. scintillation 只能作为辅助机制指标，不能作为通信主评价。
3. equal transmitted power 必须报告，但还需要 aperture / spatial-scale / peripheral-energy resource ledger。
4. Paper 1 应专门检查：turbulence-only Bessel advantage 加入 independent jitter 后是保持、压缩还是反转。

### NOT YET FROZEN

- 最终采用 square-truncated Bessel、circular-truncated Bessel 还是 Bessel-Gaussian；
- `a_B` 或 equivalent core/ring scale 如何与 Gaussian 匹配；
- 最终 physical aperture / wavelength / turbulence parameters；
- Bessel jitter sensitivity 的方向与阈值。

## 11. 该文献没有回答的问题

- independent mechanical jitter；
- boresight bias；
- turbulence-induced beam wander 与 jitter 的分账；
- received-power ECDF / low-tail quantile / outage；
- optimized Gaussian for the same reliability target；
- modern circular transmitter-aperture resource matching；
- optical beam-generation loss；
- 为什么低阶 Bessel 在小 receiver aperture 下出现低 scintillation 的确定物理机制。

因此该文献对 Paper 1 的价值是**建立一个值得被重新审查的 turbulence-only claim，并提供资源公平性的历史证据**，而不是直接给出我们的结论。
