# Liu et al. 2022：aircraft HG + turbulence + pointing 的 direct-competitor 审计

## 1. 文献身份

- Xin Liu, Yu Zhang, Dagang Jiang, Kaiyu Qin
- *Fade probability simulation analysis for aircraft platform wireless optical communication based on Hermite-Gaussian beam*
- Journal of Physics: Conference Series 2252 (2022) 012043
- DOI: `10.1088/1742-6596/2252/1/012043`
- License: CC BY 3.0
- 证据角色：**Paper 1 direct competitor / novelty-boundary anchor**。

该文的重要性不是它已经建立了一个可信的 HG 工程最优方案，而是它明确证明：

> `structured beam + aircraft motivation + atmospheric turbulence + independent pointing error + fade probability`

这一宽泛组合在 2022 年已经被研究，因此本项目不能把“第一次把 structured beam 放入 turbulence + pointing”作为创新主张。

---

## 2. HG 光场与 Gaussian 基线

论文使用 Hermite-Gaussian family：

\[
U_{mn}(x,y,0)
\propto
H_m\!\left(\frac{\sqrt2 x}{W_0}\right)
H_n\!\left(\frac{\sqrt2 y}{W_0}\right)
\exp\!\left[-\frac{x^2+y^2}{W_0^2}\right].
\]

其中：

- `m=n=0` 为 TEM00 Gaussian；
- 论文比较 `TEM01`, `TEM02`, `TEM03` 与 `TEM00`；
- 所有模式使用同一个 nominal `W0 = 20 mm`。

必须注意：对 HG family 来说，同一个 `W0` 并不意味着同一个物理 transverse extent。随着 mode order 增加，二阶矩、外围 lobe extent 和 angular-spectrum content 都增加。因此 higher-order HG 对 displacement 更宽容时，可能包含明显的 **beam-scale / spatial-coverage resource exchange**。

论文没有对 Gaussian 的 `W0`、divergence 或 quadratic phase 针对同一 fade objective 做优化。

因此它不能证明：

> higher-order HG 的优势不能被一个更合适尺度的 Gaussian 解释。

---

## 3. turbulence 与 pointing 模型

### 3.1 turbulence

该文继承 Liu/Jiang 2021 single-layer method：

- 自由传播到 `0.36L`；
- 一层 Kolmogorov phase screen；
- 再传播 `0.64L` 到 receiver；
- 采用 Rytov / weak-turbulence motivation。

因此它不是 distributed multi-screen production model，也没有冻结 low-frequency beam-wander accuracy。

### 3.2 independent pointing

pointing error 采用：

\[
\theta_x,\theta_y\sim\mathcal N(0,\sigma^2)
\]

且 x/y 使用相同 `sigma`。论文文字称其为“standard variance”，但从 PDF 公式形式可知 `sigma` 实际扮演标准差。

几何位移：

\[
r_x=L\theta_x,\qquad r_y=L\theta_y.
\]

在 numerical propagation 中通过两个 Fourier shift factors 把 pointing tilt / displacement 分配到 `0.36L` 和 `0.64L` 两段传播。

这属于与 turbulence 随机相位独立的 pointing variable，因此足以证明“independent pointing + structured wave-optics field”不是本项目空白。

但论文没有像本项目计划那样分别保存：

- turbulence-induced centroid wander；
- independent mechanical pointing displacement；
- static/slow bias。

---

## 4. paper-specific simulation values：不能继承为 UAV 场景参数

Table 1：

- `W0 = 20 mm`；
- `lambda = 850 nm`；
- `L = 1000 m`；
- `receiver diameter D = 40 mm`；
- HG modes `(0,1),(0,2),(0,3)`；
- baseline `Cn² = 1e-15 m^(-2/3)`；
- pointing `sigma = 10–50 microrad`；
- later comparison also uses `Cn² = 1e-14 m^(-2/3)`；
- transmitted power uniformly set to `30 mW`；
- 1000 pointing / turbulence groups used to construct PDFs。

论文把 10–50 μrad 的选择理由写成 aircraft-platform pointing magnitude 通常为 several tens of microradian，并引用 ATP survey / general references，而非 UAV post-PAT/FSM flight residual measurement。

因此：

> `10–50 microrad = scenario assumption / simulation scan`，不得冻结为本项目 UAV residual-jitter range。

---

## 5. 最重要的审计问题：所谓“received power”与公式不一致

论文文字写道：

> 在某一 receiving aperture 内的 irradiance fluctuation PDF 称为 received-power fluctuation PDF，并为方便后续计算进行了 normalization。

Table 1 也给出 receiver diameter `D = 40 mm`。

但是论文可审计的 Eq. (9)–(10) 是：

\[
I_{mn}^{(j)}(x,y,L)=|U_{mn}^{(j)}(x,y,L)|^2
\]

然后通过 kernel / histogram 从 irradiance samples 构造 PDF；Eq. (10) 的区间描述明确使用：

\[
I_{mn}^{(j)}(0,0,L).
\]

全文没有给出本项目所要求的有限孔径积分：

\[
P_R^{(j)}=\iint_{A_R}I_{mn}^{(j)}(x,y,L)\,dA.
\]

并且在正文可追踪公式中，`D = 40 mm` 没有进入 received-power / fade calculation。

因此当前只能做如下谨慎裁决：

> **论文文字把评价量称为 received power，但公开公式更像 on-axis irradiance statistic；finite receiver aperture 是否真正执行积分在文中没有得到可复现定义。**

不能把该文直接归类为“已完成 rigorous finite-aperture received-power outage comparison”。

这反而强化本项目使用 explicit aperture integral 的必要性，但仍不能声称“第一次考虑 receiver aperture”，因为其他文献（Liu/Jiang 2021、Jiang 2022、Airy/partial-coherence work）已有真正有限孔径功率研究。

---

## 6. normalization 与 fade threshold 存在第二层不确定性

论文明确写：

- received-power fluctuation PDF “for simplicity ... has been normalized”；
- 假设 binary unipolar code；
- fade threshold 固定为 `0.5`：

\[
P_{fade}=\int_0^{0.5}p(I)\,dI.
\]

但论文没有清楚给出跨模式 normalization reference：

- 是否除以每个 mode 自己的无扰动峰值？
- 是否除以各自 mean？
- 是否以 transmitted 30 mW 归一？
- 是否以同一个 absolute receiver threshold 归一？

这对 `TEM00` vs `TEM01/02/03` 的 fade comparison 是关键问题。

如果每个 mode 的 irradiance / “received power”先按自己的 characteristic level 独立缩放，再统一使用 `0.5` threshold，那么 cross-mode fade probability 不再代表同一个 absolute communication threshold。

因此论文报告的“higher-order HG has better fade probability”应视为：

> **paper-specific normalized-metric result，不能直接继承为 absolute-link advantage。**

本项目必须明确：

\[
H=P_R/P_T
\]

或其他唯一、跨光场一致的 normalization，并把 outage threshold 的物理含义写清楚。

---

## 7. 为什么 higher-order HG 可能显得更抗 pointing：必须排除 beam-scale explanation

论文在 `W0 = 20 mm` 固定时比较不同 HG order，并报告 higher-order HG fade probability 较低，`TEM02` 与 `TEM03` 接近。

但对标准 HG modes，order 增大天然带来：

- 更大的 transverse second moment；
- 更多 / 更远的 lobes；
- 更宽的 spatial coverage；
- 不同的 diffraction / angular-spectrum distribution。

因此一个非常合理的 alternative explanation 是：

> higher-order HG 的 normalized fade 改善主要来自更大的空间覆盖 / 有效 beam scale，而不是某种独立 anti-turbulence mechanism。

论文没有提供：

- equal receiver-plane second-moment comparison；
- equal encircled-energy scale；
- optimized Gaussian beam-width control；
- transmitter clear-aperture / clipping ledger；
- halo / lobe power cost。

所以它不能排除该解释。

这正是 Paper 1 需要比它更严格的地方。

---

## 8. 该文真正支持什么

### 支持

1. aircraft / moving-platform motivation 下，把 independent Gaussian pointing error 加到 HG phase-screen propagation 是已有工作；
2. 在其 single-layer + normalized fade metric 下，pointing severity 增大后 fade probability 显著上升；
3. 在其扫描范围内，当 pointing sigma 较大时，改变 `Cn²` 对 fade 的影响相对变小，说明 disturbance dominance 可以随区域迁移；
4. structured-beam ranking 在 joint disturbance 下确实是一个已有先例的科学问题。

### 不支持

1. higher-order HG 在 equal hardware/resource/absolute-power conditions 下真正优于 optimized Gaussian；
2. higher-order HG 的优势来自某种已识别 anti-turbulence mechanism；
3. 40 mm receiver aperture 已通过明确积分进入 fade calculation；
4. 10–50 μrad 是真实 UAV post-loop residual-jitter range；
5. single-layer weak-turbulence result 可代表 distributed medium/strong turbulence；
6. `threshold=0.5` 对不同模式对应同一 absolute receiver/SNR threshold。

---

## 9. 对 Paper 1 创新边界的直接影响

这篇把本项目能说的话进一步收窄。

### 明确禁止

不得声称：

- “首次研究 structured beam 在 turbulence + pointing 下的 fade”；
- “首次研究 aircraft structured-beam turbulence–pointing joint channel”；
- “此前高阶结构光只研究 turbulence，从未加入 pointing”。

### 仍然存在的空间

Paper 1 可以强调的是：

> 现有 individual structured-beam studies 已经零散加入 pointing，但缺少一个机制驱动、resource-transparent、finite-aperture absolute-power、optimized-Gaussian-controlled 的统一框架，去回答不同 anti-turbulence mechanisms 在 independent mechanical jitter 下为什么保持、压缩或失效。

与 Liu 2022 相比，本项目至少需要明确做到：

1. explicit finite-aperture integral；
2. common physical normalization；
3. optimized Gaussian baseline；
4. transmitter aperture / beam-scale / peripheral-energy resource ledger；
5. turbulence-only / jitter-only / joint 三条件机制分解；
6. distributed multi-screen turbulence；
7. turbulence beam wander 与 independent jitter 独立记账；
8. common-random-number paired comparison；
9. 不只给单 mode result，而是比较少量真正不同的 anti-turbulence mechanisms；
10. 输出 sensitivity / failure boundary，而不是只给 one-family fade curves。

---

## 10. 当前裁决

**状态：READ / DIRECT-COMPETITOR + METHODOLOGICAL LIMITATION ANCHOR。**

它不会吃掉 Paper 1，但会禁止一个过宽的新颖性说法，并帮助明确我们的贡献不应是“加入 pointing”，而应是：

> **把零散、归一化和资源口径不一致的 structured-beam joint analyses，提升成机制可解释、资源透明、有限孔径绝对功率一致的跨机制 robustness/failure map。**

此外，这篇目前没有充分理由让 HG 成为 Paper 1 的主 3–5 个 representative mechanisms；HG 更适合作为 direct-competitor context，除非后续 literature review 发现其 turbulence robustness 有独立、清晰且不等同于 beam-scale 的物理机制。