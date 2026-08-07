# Paper 1 抗湍流机制文献初筛——Round 1

**日期：** 2026-08-07  
**状态：** Stage A 文献筛选，不构成最终机制集合或性能结论  
**目标：** 为 Paper 1 建立第一版“机制—代表文献—抗湍流主张—对 independent jitter 的待检验敏感性”地图。

## 1. 当前负责人结论

Paper 1 不宜按“Bessel、Airy、OPB、flat-top……”逐个堆模式，而应按**抗湍流物理机制**组织。第一轮检索后，至少有五类机制值得继续保留：

1. self-healing / angular-spectrum redundancy；
2. caustic / self-accelerating / path diversity；
3. self-focusing / pin-like longitudinal concentration；
4. partial coherence / incoherent averaging；
5. flat-top / reduced-gradient / reduced-spreading。

vector / modal-diversity 类存在重要前序，但它们往往改变接收任务、编码方式或模态检测方式，因此当前只保留为可选补充，不作为 Paper 1 默认直接探测家族。

当前所有“对 jitter 可能敏感/不敏感”的判断都只是 **PHYSICS PRIOR**，必须在后续统一有限孔径评价中验证。

---

## 2. Mechanism A — Bessel / Bessel–Gaussian：self-healing 与 angular-spectrum redundancy

### A1. Eyyuboğlu, Voelz, Xiao, Applied Optics 2013

**题目：** *Scintillation analysis of truncated Bessel beams via numerical turbulence propagation simulation*  
**DOI：** `10.1364/AO.52.008032`  
**状态：** `ANCHOR_TO_READ / HIGH PRIORITY`

**为什么重要：**

- 使用 random phase-screen wave-optics 研究 truncated Bessel beams；
- 同时报告 on-axis scintillation、aperture-averaged scintillation；
- 不只做 equal source power，还专门讨论 **scintillation per unit received power**；
- 论文明确显示：Bessel 在 equal source power 下常有较低 scintillation，但加入 received-power 资源口径后，优势大幅缩小，只在部分区域保留。

**对 Paper 1 的价值：**

这篇几乎就是“结构抗湍流优势 vs 外围能量/接收资源交换”的一级锚点。后续精读应重点提取：

- truncated Bessel source definition；
- source-window / aperture；
- Bessel order；
- Gaussian baseline；
- received-power normalization；
- receiver aperture；
- turbulence phase-screen model；
- 其优势消失的参数区。

### A2. Yuan et al., Scientific Reports 2017

**题目：** *Beam wander relieved orbital angular momentum communication in turbulent atmosphere using Bessel beams*  
**状态：** `ANCHOR_TO_READ / EXPERIMENTAL PERFORMANCE`

**为什么重要：**

- 理论 + 实验研究 Bessel beam 的 turbulence-induced beam wander；
- 报告高阶 Bessel beams 的 beam wander 较小；
- 1550 nm、10-Gbit/s OOK 的 turbulence-emulation communication experiment；
- 直接把“抗湍流”主张落在 beam wander 与 BER 上。

**Paper 1 需警惕：**

该文献包含 OAM multiplexing / modal detection，不等于我们当前 finite-aperture direct-detection 任务。应把其 beam-wander 机制证据与其通信接收任务分开继承。

### A3. Nelson et al., 2013/2014

**题目：** *Propagation of Bessel and Airy beams through atmospheric turbulence*  
**预印本：** arXiv:1312.0620  
**状态：** `ANCHOR_TO_READ / FAILURE-BOUNDARY`

**为什么重要：**

这项工作并不只是证明 Bessel/Airy 鲁棒，反而指出当 Fried coherence length 接近初始 aperture 尺度时，turbulence 会破坏其 quasi-nondiffracting 性质。

**Paper 1 价值：**

非常适合建立“抗湍流新光束并非无限鲁棒”的失效边界。

### Mechanism A 的 jitter 先验

**PHYSICS PRIOR：** self-healing 能在局部遮挡/局部场畸变后利用外围 angular spectrum 重建中心结构，但 independent mechanical pointing jitter 会把整个 angular spectrum / reconstructed core 一起相对固定接收孔径偏移。因此：

- self-healing 不应自动推出抗整体 lateral displacement；
- 窄 central core 可能增加固定孔径对 jitter 的敏感性；
- 环形外围能量可能提供 coverage，也可能只是额外资源；
- 需要同时检查 `beam wander reduction` 和 `mechanical jitter tolerance`，不能混用。

---

## 3. Mechanism B — Airy / caustic：self-accelerating、self-healing 与 path diversity

### B1. Gu & Gbur, Optics Letters 2010

**题目：** *Scintillation of Airy beam arrays in atmospheric turbulence*  
**DOI：** `10.1364/OL.35.003456`  
**状态：** `ANCHOR_TO_READ / MECHANISM`

**为什么重要：**

论文的核心不是简单“Airy self-healing”，而是利用 Airy beamlets 的 self-bending，使不同分量通过相对独立的 turbulence regions，最终在 detector 附近重叠，从而获得一种 **path-diversity / incoherent-like averaging** 的 scintillation reduction。

**Paper 1 价值：**

Airy 类不应只被归入“self-healing”。这篇揭示其抗湍流可能来自几何路径多样性，意味着对 independent pointing jitter 的敏感性可能与 Bessel 不同。

### B2. Zhu et al., Optics Express 2021

**题目：** *Free-space optical communication with quasi-ring Airy vortex beam under limited-size receiving aperture and atmospheric turbulence*  
**DOI：** `10.1364/OE.435863`  
**状态：** `ANCHOR_TO_READ / FINITE-APERTURE EXPERIMENT`

**为什么重要：**

- 直接把 limited-size receiving aperture 纳入问题；
- 实验生成 quasi-ring Airy vortex beam；
- 报告 72-Gbit/s 16-QAM DMT transmission；
- 在 turbulence 下与 conventional OAM beam 和 Bessel beam 比较 received power / BER。

**Paper 1 需警惕：**

该光束包含 vortex/OAM 与具体通信协议，因此不能把其整体 BER 优势直接当作 Airy caustic 的纯机制收益。精读时应分离 radial phase shaping、finite-aperture power 与 OAM detection 的作用。

### B3. Nelson et al. 2013/2014

同 A3，同时作为 Airy turbulence failure-boundary 文献。

### Mechanism B 的 jitter 先验

**PHYSICS PRIOR：** caustic/self-bending 能让局部能量沿设计轨迹重构，但 residual tilt 会改变整个 caustic trajectory 相对 receiver 的位置。需要特别检查：

- nominal self-bending trajectory 是否本身要求 receiver offset；
- jitter 是把 trajectory 整体平移/转动，还是只轻微改变焦散形成位置；
- finite-aperture capture 是否比形状保持更脆弱；
- Airy array 的 turbulence path-diversity 能否转化为 mechanical-jitter tolerance。

---

## 4. Mechanism C — Optical Pin Beam：self-focusing / longitudinal concentration

### C1. Zhang et al., APL Photonics 2019

**题目：** *Robust propagation of pin-like optical beam through atmospheric turbulence*  
**DOI：** `10.1063/1.5095996`  
**状态：** `ANCHOR_TO_READ / HIGH PRIORITY`

**为什么重要：**

- 提出 optical pin beam (OPB)；
- 通过 directionally truncated Airy-like components 的叠加形成 autofocusing / shape-preserving propagation；
- 理论、室内及 outdoor atmospheric propagation 均有验证；
- 直接与 Gaussian intensity stability 比较；
- 其突出机制是 beam width 随传播形成 pin-like self-focusing，而不只是 conventional self-healing。

**Paper 1 价值：**

OPB 很适合作为 Paper 1 的代表机制，因为它有很强的 turbulence-only 主张，但其高强度/窄 focal region 对整体 pointing displacement 的容差并不显然。

### C2. Nardo et al., 2025 preprint

**题目：** *Performance and applications of optical pin beams in turbulent long-range free space optical communications*  
**arXiv：** `2504.01704`  
**状态：** `SCREENED / RECENT PERFORMANCE BACKGROUND`

**初筛信息：**

- 建立 OPB unified theoretical model；
- 多 realization turbulence simulation 和 link-budget analysis；
- 100 km air-to-air 场景中报告相对 Gaussian 的 link-budget / beam-wander improvement；
- 还强调 transmitter aperture diameter 与可达距离之间的资源关系。

因属于预印本，证据等级低于同行评审锚点；但其 aperture/resource discussion 对 Paper 1 很有价值。

### Mechanism C 的 jitter 先验

**PHYSICS PRIOR：** OPB 的 turbulence resilience 很大部分来自 propagation-direction engineering 与 self-focusing。如果最终形成的是较窄高强度核心，那么：

- turbulence-only 时可能保持较小 width / 高 intensity；
- independent tilt 可能直接把这个高强度核心移出 receiver；
- “beam wander 较小”与“对额外 independent jitter 不敏感”仍是两个不同命题。

因此 OPB 是 Paper 1 最值得检验的“抗湍流可能反而更怕机械抖动”的候选之一。

---

## 5. Mechanism D — Partial Coherence：incoherent averaging / speckle decorrelation

### D1. Borah & Voelz, Optics Express 2010

**题目：** *Spatially partially coherent beam parameter optimization for free space optical communications*  
**DOI：** `10.1364/OE.18.020746`  
**状态：** `ANCHOR_TO_READ / OPTIMIZATION BASELINE`

**为什么重要：**

- weak turbulence；
- 直接优化 spatial coherence length；
- 目标涉及 outage probability；
- 同时讨论 beamwidth、phase-front curvature、distance、wavelength。

**Paper 1 价值：**

说明 partial coherence 不是“天然抗湍流”的单一标签，而是存在 coherence-length / beamwidth trade-off。后续与 jitter 比较时必须允许正确的 coherence baseline，不能固定一个随意 coherence length。

### D2. Liu et al., Optics Letters 2014

**题目：** *Experimental study of turbulence-induced beam wander and deformation of a partially coherent beam*  
**DOI：** `10.1364/OL.39.003336`  
**状态：** `ANCHOR_TO_READ / EXPERIMENTAL MECHANISM`

**为什么重要：**

实验表明 Gaussian Schell-model beam 降低空间相干性后，其 turbulence-induced beam wander 与 deformation 下降。

**Paper 1 价值：**

这类机制与 Bessel/OPB 不同：它不是通过主瓣重建，而是通过降低 coherence 使 turbulence-induced fluctuations / wander 被平均化。

### D3. Drexler, Roggemann, Voelz, Optical Engineering 2011

**题目：** *Use of a partially coherent transmitter beam to improve the statistics of received power in a free-space optical communication system: Theory and experimental results*  
**DOI：** `10.1117/1.3533737`  
**状态：** `ANCHOR_TO_READ / RECEIVED-POWER EXPERIMENT`

**为什么重要：**

把 partially coherent transmitter 与 received-power dropouts 联系起来，并有理论与实验。

### Mechanism D 的 jitter 先验

**PHYSICS PRIOR：** partial coherence 的 turbulence benefit 常伴随更复杂的 long-term beam size / source-mode distribution。对 independent jitter 可能存在两种相反效应：

- 更宽、较平缓的 capture curve 可能降低 lateral-jitter sensitivity；
- 但平均接收功率、峰值和有效发射资源可能同时下降。

因此它是分析“抗湍流收益是否只是空间展宽换来的”最好的机制对照之一。

---

## 6. Mechanism E — Flat-top / flattened / super-Gaussian：reduced spreading 与 flat central capture

### E1. Alavinejad, Ghafary, Kashani, Optics and Lasers in Engineering 2008

**题目：** *Analysis of the propagation of flat-topped beam with various beam orders through turbulent atmosphere*  
**DOI：** `10.1016/j.optlaseng.2007.07.003`  
**状态：** `ANCHOR_TO_READ / TURBULENCE ORIGIN`

**初筛主张：**

- analytical average intensity；
- higher-order flat-topped beam 在其模型下 turbulence broadening 较小；
- 计算 beam width 和 Strehl ratio。

### E2. Baykal & Kamacıoğlu, Optics & Laser Technology 2013

**题目：** *Averaging of receiver aperture for flat-topped incidence*  
**DOI：** `10.1016/j.optlastec.2013.04.011`  
**状态：** `ANCHOR_TO_READ / FINITE-APERTURE`

**为什么重要：**

直接研究 flat-topped incidence 的 power scintillation 与 receiver aperture averaging，适合连接我们 finite-aperture 主指标。

### E3. Jiang et al., Optics Communications 2022

**题目：** *Average irradiance with boresight pointing errors for flat-topped beam under atmospheric turbulence*  
**DOI：** `10.1016/j.optcom.2022.128703`  
**状态：** `DIRECT_COMPETITOR / FULL PDF NOT YET AVAILABLE`

已经覆盖 turbulence + jitter/bias + flat-top average irradiance / received-power 类问题，因此 Paper 1 不能把“flat-top + turbulence + pointing”本身作为创新。

### E4. Jiang et al., Applied Optics 2026

**题目：** *Far-field approximate expressions for average irradiance and average BER in flat-topped beam-based optical wireless communication links under pointing error and gamma–gamma turbulence*  
**DOI：** `10.1364/AO.578489`  
**状态：** `DIRECT_COMPETITOR / RECENT`

进一步把 flat-top + pointing + turbulence 推进到 far-field BER approximate model。

### Mechanism E 的 jitter 先验

**PHYSICS PRIOR：** flat-top 是 Paper 1 中比较特殊的一类：其中央强度/捕获曲线天然可能对小位移较平缓，因此它可能同时具备一定 jitter tolerance。它更适合作为：

- Paper 1 中“抗湍流机制恰好与 jitter 需求方向一致”的正对照；
- Paper 2 可能设计种子的背景。

但必须排除：优势是否仅来自把同样总功率铺得更宽、牺牲 aligned received power 或使用更大发射资源。

---

## 7. Optional mechanism — modal / channel eigenstructure

### F1. Cox et al., IEEE JSTQE 2020/2021

**题目：** *Structured Light in Turbulence*  
**DOI：** `10.1109/JSTQE.2020.3023790`  
**状态：** `ANCHOR_TO_READ / REVIEW`

这是 structured light turbulence 的重要综述/实验总结，应作为 Paper 1 机制库的总体入口。

### F2. Klug, Peters, Forbes, Advanced Photonics 2023

**题目：** *Robust structured light in atmospheric turbulence*  
**DOI：** `10.1117/1.AP.5.1.016006`  
**状态：** `ANCHOR_TO_READ / MODERN MECHANISM`

其方向是从 channel 本身寻找 turbulence eigenmodes / robust structured light，而不是传统 Bessel/Airy 形状家族。

### F3. Peters, Cocotos, Forbes, Advances in Optics and Photonics 2025

**题目：** *Structured light in atmospheric turbulence—a guide to its digital implementation: tutorial*  
**DOI：** `10.1364/AOP.538883`  
**状态：** `REFERENCE / IMPLEMENTATION REVIEW`

可用于后续冻结 digital turbulence implementation 和 structured-light measurement conventions。

### 当前处理原则

这些工作很重要，但 Paper 1 当前主接收任务是 finite-aperture direct detection。若一个“robust structured mode”只有在 mode sorting / coherent modal detection / coding protocol 下才体现收益，就不应与直接探测家族放在同一排行榜。

---

## 8. Direct competitor — structured beam + turbulence + pointing 已经有人做过

### Liu, Zhang, Jiang, Qin, J. Phys.: Conf. Ser. 2022

**题目：** *Fade probability simulation analysis for aircraft platform wireless optical communication based on Hermite-Gaussian beam*  
**DOI：** `10.1088/1742-6596/2252/1/012043`  
**状态：** `DIRECT_COMPETITOR / ANCHOR_TO_READ`

**已经确认：**

- aircraft-platform motivation；
- Hermite–Gaussian vs Gaussian；
- single-layer phase screen + pointing error；
- finite receiver aperture / received-power fluctuation；
- fade probability；
- simulation uses 10–50 microrad pointing standard-deviation-like parameter；
- 作者结论为 pointing 增大后，pointing error 相比 turbulence 成为 fade 的主导因素。

**对项目的约束：**

Paper 1 不能声称“首次系统研究 structured beam 在 turbulence + platform pointing error 下的可靠性”。真正可能的新意仍需落在：

- 多种**抗湍流机制**的统一系统比较；
- distributed multi-screen turbulence；
- turbulence-induced beam wander 与 independent residual jitter 的显式分离；
- finite-aperture low-tail metrics；
- resource-matched Gaussian baseline；
- sensitivity map / failure boundary，而不是单一 HG 优势。

此外，该文把“aircraft pointing error generally several tens of microradian”建立在二手文献和 scenario assumption 上，并非 UAV/PAT post-loop 实测，因此其 10–50 microrad 仍不能直接冻结为本项目参数。

---

## 9. Round 1 后的代表机制优先级

当前建议下一轮精读优先级：

### 第一优先级

1. Eyyuboğlu et al. 2013 — Bessel，资源公平性；
2. Zhang et al. 2019 — OPB，强 turbulence-only 新机制；
3. Gu & Gbur 2010 — Airy array，path-diversity 机制；
4. Liu et al. 2014 + Borah & Voelz 2010 — partial coherence；
5. Alavinejad et al. 2008 — flat-top turbulence 原始主张；
6. Liu et al. 2022 HG direct competitor。

### 第二优先级

7. Yuan et al. 2017 — Bessel beam-wander experiment；
8. Zhu et al. 2021 — Airy finite-aperture communication experiment；
9. Baykal & Kamacıoğlu 2013 — flat-top aperture averaging；
10. Cox et al. 2020/2021 — structured-light turbulence review；
11. Klug et al. 2023 — channel-robust eigenmodes。

### Paper 2 背景，暂不抢占 Paper 1 精读顺序

- Badás 2024 Gaussian–LG jitter-only optimum；
- 2026 super-Gaussian variational optimum；
- flat-top joint optimization / design papers。

---

## 10. 当前机制—jitter sensitivity 工作假设

| 机制 | turbulence-only 主张 | 对 independent jitter 的先验 | Paper 1 重点验证 |
|---|---|---|---|
| Bessel/self-healing | peripheral angular spectrum 重建、可能减小 beam wander | self-healing 未必能 recenter 整体偏移；窄核心可能敏感 | turbulence benefit 在 jitter 下保持多少；resource normalization 后是否消失 |
| Airy/caustic | self-bending、自愈、path diversity | trajectory 整体偏移可能导致固定孔径失配 | path-diversity 是否同时改善 jitter，还是只抗 turbulence |
| OPB/self-focusing | 长距离 shape preservation / autofocusing | 窄高强度 pin 可能对 tilt 很敏感 | turbulence-only 强优势是否被 residual jitter 快速抵消 |
| partial coherence | incoherent averaging，降低 scintillation/wander | 更宽/平滑可能抗 jitter，但可能损失 aligned power | 是否只是 beam-spreading 资源交换 |
| flat-top | reduced spreading、flat central distribution | 可能天然有较平缓 capture curve | 是否成为兼顾 turbulence+jitter 的正对照；收益是否只是铺宽 |

该表只用于组织后续实验问题，不是已支持结论。

## 11. Round 1 决策

**CONTINUE。**

当前已经可以把 Paper 1 的机制空间从“模式动物园”压缩到五个主机制。下一步不需要继续大范围搜新 beam name，而应逐篇精读上述一级锚点，并开始建立统一的参数证据矩阵。

在精读达到足够覆盖前：

- 不冻结最终 3–5 个数值候选；
- 不开始正式 structured-beam code；
- 不把任何 jitter sensitivity 先验写成论文结论；
- 不进入 Paper 2 联合设计。
