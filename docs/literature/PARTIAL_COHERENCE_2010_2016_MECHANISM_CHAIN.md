# Partial coherence 2010–2016：从抗湍流机制到 turbulence–pointing 联合优化的成熟链条

## 1. 文献链与证据角色

本笔记把以下工作作为一个连续证据链，而不是孤立阅读：

1. Deva K. Borah, David G. Voelz, *Spatially partially coherent beam parameter optimization for free space optical communications*, Optics Express 18, 20746–20758 (2010), DOI `10.1364/OE.18.020746`；
2. It Ee Lee, Zabih Ghassemlooy, Wai Pang Ng, Mohammad-Ali Khalighi, *Joint optimization of a partially coherent Gaussian beam for free-space optical communication over turbulent channels with pointing errors*, Optics Letters 38, 350–352 (2013), DOI `10.1364/OL.38.000350`；
3. Xianlong Liu, Fei Wang, Cun Wei, Yangjian Cai, *Experimental study of turbulence-induced beam wander and deformation of a partially coherent beam*, Optics Letters 39, 3336–3339 (2014), DOI `10.1364/OL.39.003336`；
4. It Ee Lee et al., *Effects of aperture averaging and beam width on a partially coherent Gaussian beam over free-space optical links with turbulence and pointing errors*, Applied Optics 55, 1–9 (2016), DOI `10.1364/AO.55.000001`。

综合证据角色：

> **成熟抗湍流机制 + 已存在 turbulence–pointing 联合设计的对照链。**

因此 partial coherence 不宜作为 Paper 1 的“主要未研究交叉机制”来包装；更适合作为成熟机制/正对照，约束 Paper 1 的创新边界和统一评价逻辑。

---

## 2. 基本物理机制：降低相干性并不是免费收益

Gaussian Schell-model (GSM) beam 的 source mutual coherence function 可写成

\[
\Gamma(\mathbf r_1,\mathbf r_2)
=
\exp\left[-\frac{r_1^2+r_2^2}{w_0^2}
-\frac{|\mathbf r_1-\mathbf r_2|^2}{2\sigma_g^2}\right],
\]

其中：

- `w0`：source transverse beam width；
- `sigma_g` / `l_c`：transverse spatial coherence width / coherence length。

降低 spatial coherence 的直观作用是减少长距离传播中相干干涉形成的强 intensity fluctuation，使不同局部/模态贡献产生一定统计平均；但代价是 beam divergence / long-term spot size 往往增大，平均接收强度下降。

Borah & Voelz 2010 在论文引言中已经非常明确地把问题定义为：

> **scintillation reduction 与 mean received signal reduction 之间的 trade-off。**

因此 partial coherence 从一开始就不是“相干性越低越好”。

---

## 3. Borah & Voelz 2010：coherence length optimization 已经存在

### 3.1 科学问题

该文在 weak-turbulence regime 下研究 spatial coherence length 的优化，并用 outage probability 而不是只用 scintillation 评价通信性能。

其主要工作包括：

- 推导 partially coherent beam 的 scintillation-index series expression；
- 建立 finite optimum coherence length 存在的条件；
- 研究 phase-front radius of curvature、distance、wavelength、beam width 对 optimum 的影响；
- 直接讨论 outage probability 改善。

### 3.2 重要结论

作者显示：

- 较小传播距离、较大 beam width 时，partial coherence optimization 更可能产生明显收益；
- 某些配置中 outage probability 可以改善数个数量级；
- 但在另外的 beam-width / propagation region 中，coherence length 对 scintillation 的影响很小，而 mean intensity 会随着 coherence 增大而提高，此时 fully coherent beam 更有利。

因此，partial coherence 的抗湍流收益本身已经具有明显 **applicability regime**，并非单调规则。

### 3.3 对本项目的意义

Paper 1 不得把“降低 spatial coherence 减小 scintillation”当作新的机制发现；也不能只比较固定 coherence settings 后再声称存在最佳 partially coherent beam。

若将 partial coherence 留作对照，至少应承认 coherence length optimization 是成熟前序。

---

## 4. Lee et al. 2013：已经完成 turbulence + pointing 下的 joint beam-width / coherence optimization

### 4.1 研究对象

该文明确研究：

> `beam width w0 + spatial coherence length l_c`

在 atmospheric turbulence + pointing errors + receiver aperture averaging 下的联合优化，目标为最大化 average channel capacity。

这意味着“partial coherence 是抗湍流机制，但没有针对 pointing 优化”这一叙述对该家族已经不成立。

### 4.2 pointing 模型

作者采用经典 finite-aperture pointing-loss statistical model，其中

\[
\xi=\frac{w_{z,eq}}{2\sigma_{pe}},
\]

`σ_pe` 是 receiver-plane pointing displacement standard deviation，而不是 UAV transmitter angular RMS。

论文默认示例使用：

- `lambda = 1550 nm`；
- `L = 7.5 km`；
- `D = 40 mm` receiver diameter；
- `w0 = 0.05 m` nominal beam width；
- `sigma_pe = 30 cm` receiver-plane displacement standard deviation。

这些均是作者模型参数，**不得继承为 UAV post-PAT residual jitter 场景值**。

作者还用

\[
2\sigma_{pe}/D
\]

作为 normalized pointing severity。这一量说明 receiver aperture 与 pointing displacement 必须共同考虑，但不等同于本项目最终的 `j=L sigma_theta/w_ref`。

### 4.3 一个非常重要的非单调结果

该文的结果不是“越不相干越好”。

在其离散参数搜索中：

- weak turbulence (`sigma_R^2 = 0.25`) 的 joint optimum 大致为 `[w0, l_c] = [0.10 m, 0.0012 m]`；
- very strong turbulence (`sigma_R^2 = 36`) 的 optimum 大致迁移到 `[0.05 m, 0.0600 m]`，即更接近高相干状态。

论文进一步报告：

- weak-to-moderate turbulence 下 partially coherent beams 更有吸引力；
- turbulence 很强时，最佳 beam-spreading gain 向 `~1` 回落，更 coherent 的高功率 laser beam 反而更合适；
- receiver aperture 增大同时缓解 pointing loss 和 aperture-averaged scintillation。

这个结果对 Paper 1 很重要，因为它说明：

> **一种经典“抗湍流手段”的 optimum 本身会随 turbulence/pointing 区域迁移甚至回到 coherent limit。**

但这个问题在 partially coherent Gaussian 家族中已经被研究过，因此不能作为本项目的新主张。

---

## 5. Liu et al. 2014：实验上确认降低 coherence 可减小 turbulence-induced beam wander 与 deformation

### 5.1 实验结构

作者使用：

- He–Ne laser，`lambda = 632.8 nm`；
- rotating ground-glass disk (RGGD) 生成 partially coherent light；
- Gaussian amplitude filter 形成 GSM intensity profile；
- 改变照射 RGGD 的 spot size 来调节 spatial coherence width；
- thermally induced laboratory turbulence。

该实验不是 UAV 场景，也不是 mechanical pointing-jitter 实验。

### 5.2 测量量

论文把 beam wander 定义为 receiver-plane beam centroid random displacement 的 RMS，并直接测量 beam wander 与 beam deformation。

实验结论：

> spatial coherence 越低，turbulence-induced beam wander 和 deformation 越小。

这给 partial-coherence turbulence mechanism 提供了实验支持，而不只是 scintillation 理论。

### 5.3 不能越界的解释

它研究的是：

\[
\text{turbulence-induced centroid wander}
\]

不是：

\[
\text{independent platform/PAT mechanical jitter}.
\]

因此不能把“降低 coherence 减少 turbulence beam wander”直接改写成“降低 coherence 抗 UAV mechanical jitter”。

---

## 6. Lee et al. 2016：joint line 已进一步扩展到 aperture / beam-width / channel-capacity analysis

2016 Applied Optics 工作进一步明确考虑：

- spatially partially coherent Gaussian beam；
- atmospheric loss；
- turbulence；
- scintillation；
- turbulence-induced beam wander；
- pointing errors；
- receiver aperture averaging；
- beam width optimization；
- average channel capacity。

公开 Table 1 的 simulation/system values 包括：

- `lambda = 1550 nm`；
- spatial coherence length `1.38 mm`；
- nominal beam width `5 cm`；
- link distances `1.0, 4.5, 7.5 km`；
- receiver diameters `40, 80, 200, 400 mm`；
- pointing-error displacement standard deviation `30 cm`。

仍然必须标记为 paper-specific model values，而非 UAV residual-jitter evidence。

作者的主要结论之一是：optimum beam width depends on combined turbulence + PE conditions；强 turbulence 时，pointing loss 不同时，最佳 beam width 对 Rytov variance 的变化规律也显著不同。

所以 partially coherent Gaussian 的“turbulence + pointing + aperture + beam width”问题已经非常成熟。

---

## 7. 对 Paper 1 的角色裁决

### 7.1 不建议作为 Paper 1 的主创新机制

理由：

1. `coherence length` turbulence optimization 已在 2010 年明确建立；
2. 2013 年已经做 beam width + coherence length 的 turbulence + pointing joint optimization；
3. 2014 年已有 beam-wander/deformation 实验；
4. 2016 年已把 turbulence、beam wander、pointing、aperture averaging、capacity 和 beam-width optimization 放在一起。

因此，如果 Paper 1 用 partially coherent Gaussian 作为核心“以前只抗湍流、现在我们第一次加 jitter”的例子，创新叙事不成立。

### 7.2 建议角色：成熟联合机制对照 / positive control

它仍然很有价值，因为它可以作为一个已知 reference case：

> 一个 turbulence robustness mechanism 如果已经认真把 pointing 与 aperture 加入设计，应该表现出怎样的 trade-off / optimum migration？

这样它可用于对照 Bessel、OPB、single/ring Airy 等“主要围绕 turbulence 设计、但 independent jitter 尚未系统审查”的机制。

### 7.3 如果最终 common-evaluation set 需要压缩

优先顺序建议：

- **保留在文献和讨论层**：高优先级；
- **保留为数值 validation/control case**：可选；
- **占据 3–5 个 Paper-1 主代表名额之一**：当前倾向 NO，除非后续机制设计需要一个明确的“已 joint-optimized positive control”。

---

## 8. 对统一评价协议的新增启示

该文献链支持以下原则：

1. **不能只比较 turbulence-only claim。** 对具有可调 coherence / divergence 的家族，参数本身已经可能针对 joint channel 迁移；
2. **降低 scintillation 与降低 mean received power 是明确 trade-off。** 这一点与 Bessel 的 resource-fairness 警告相呼应；
3. **turbulence-induced beam wander 与 independent pointing 必须分开。** Liu 2014 只支持前者；Lee 2013/2016 用独立 statistical PE 模型处理后者；
4. **receiver aperture 是机制的一部分。** 更大 aperture 可同时压 pointing loss 和 scintillation，但属于 receiver resource，不应隐藏；
5. **joint optimum 可能退回简单端点。** Lee 2013 在强 turbulence 下 optimum 向 coherent beam 回落，说明 Paper 1 / Paper 2 都必须允许负结果或 endpoint optimum；
6. **Paper 1 的主要新空间应集中在那些尚未经历如此成熟 joint optimization 的 anti-turbulence structured-beam mechanisms。**

## 9. 当前结论

**状态：READ AS A MECHANISM CHAIN / MATURE JOINT-OPTIMIZATION CONTROL。**

partial coherence 机制本身应继续进入 Paper 1 的文献综述和理论比较框架，但当前不建议把它作为最核心的 3–5 个“未审查 jitter 的新光束”之一。

这条文献链反而帮助我们把 Paper 1 的选择标准收紧为：

> 优先选择具有明确 anti-turbulence mechanism、通信资源可比、且 independent mechanical jitter 尚未被系统纳入该机制评价的 structured fields。