# Paper 1 外部审查材料包：抗湍流光束的抖动敏感性研究

**日期：** 2026-08-07  
**状态：** 外部审查用工作材料；不代表科学契约已经冻结。  
**当前阶段：** Paper 1 / Stage A 文献与机制地图已达到第一轮阶段性饱和，准备在进入 Stage B 数值实现前接受外部审查。  
**权威路线边界：** `docs/RESEARCH_STAGE_BOUNDARY.md`

---

## 1. 本次外部审查要解决什么

本项目当前不是请求审查具体代码或仿真结果，因为正式科学代码链尚未建立。当前需要审查的是：

1. Paper 1 的科学问题是否足够清楚、独立且具有论文价值；
2. 现有文献调研是否已经覆盖主要 turbulence-resistant beam mechanisms，是否存在明显遗漏会改写研究问题；
3. 当前机制分类与代表光束选择是否合理；
4. 资源公平性与 Gaussian baseline 的设计是否足够严格但不过度复杂；
5. UAV/PAT residual-jitter 与 turbulence 参数的证据链是否足以开始 Stage B；
6. 下一步应继续补文献、冻结合同并做最小实现，还是需要改变机制集合或研究问题。

请外部审查者不要把 Paper 1 与 Paper 2 混为一体。

---

## 2. 两篇论文的明确边界

### Paper 1：当前任务

核心问题：

> 文献中已经提出的不同 turbulence-resistant beam mechanisms，在加入独立机械 residual pointing jitter 后，哪些原有抗湍流优势能够保持、哪些明显退化、哪些发生排序反转？这种差异能否形成可解释的 jitter-sensitivity map、applicability regime 或 failure boundary？

Paper 1 的目标是：

- 机制文献归纳；
- 统一有限孔径物理评价；
- turbulence-only / jitter-only / joint 三类条件对照；
- 分析既有抗湍流机制遇到 independent jitter 后的保持、压缩、反转与失效；
- 给出资源透明的机制解释和适用域。

Paper 1 **不负责**：

- 发明新的 turbulence–jitter 联合鲁棒光束；
- 为每一种 structured beam 做高维 joint optimization；
- 把“第一次同时考虑 turbulence 与 pointing error”作为创新。

### Paper 2：条件性后续

只有 Paper 1 得到稳定的机制 trade-off 后，才研究：

> 能否据此构造少参数、可解释、资源透明的 turbulence–jitter co-robust beam？

flattened-/super-Gaussian、Gaussian–LG/annular-like 等目前只属于 Paper 2 的潜在设计种子。

---

## 3. 第一轮文献调研已经得到什么

当前已经从“按 beam 名字找论文”收敛为“按物理机制组织”。

### 3.1 Bessel-like angular-spectrum redundancy / self-healing

主要锚点：

- Eyyuboğlu, Voelz, Xiao, Applied Optics 2013, DOI `10.1364/AO.52.008032`。

已确认：

- truncated Bessel 在 turbulence-only 条件下可表现出较低 scintillation；
- equal source power 下优势较明显，但加入 received-power criterion 后优势区域大幅缩小；
- source aperture、外围能量和 receiver aperture 会显著改变所谓“抗湍流优势”；
- 原论文不能证明 self-healing 是低 scintillation 的唯一原因；
- independent mechanical jitter 未被研究。

对 Paper 1 的意义：

> Bessel 是检验“turbulence robustness 是否真正转化为 fixed-aperture pointing robustness”的高价值代表，同时天然暴露资源公平性问题。

当前 readiness：**较高**。数学定义、原始参数、资源陷阱均已提取；最终是 circular-truncated J0 还是 Bessel-Gaussian 尚待裁决。

详见：`docs/literature/EYYUBOGLU_2013_BESSEL_RESOURCE_ANCHOR.md`。

### 3.2 Airy / caustic / path diversity

主要锚点：

- Gu & Gbur, Optics Letters 2010, DOI `10.1364/OL.35.003456`；
- Zhu et al., Optics Express 2021, DOI `10.1364/OE.435863`。

文献阅读后发现，“Airy”不是单一机制：

1. Gu & Gbur 2010 的四 Airy beamlets 本质是 **self-bending enabled path diversity**：分离路径经历弱相关 turbulence，再在设计距离重新汇合；
2. Zhu 2021 quasi-ring Airy 更接近 **radial-phase autofocusing / inward-energy redistribution**，与 OPB 机制开始重叠。

因此当前不建议为了 beam-name 完整性强行设置一个统一“AIRY representative”。

当前角色：

- path-diversity Airy array：重要机制背景，但可能不进入单光束公平排行榜；
- radial Airy：与 OPB 竞争一个 autofocusing mechanism representative 名额。

详见：`docs/literature/GU_GBUR_2010_AIRY_PATH_DIVERSITY_ANCHOR.md` 与 `docs/literature/ZHU_2021_QR_AIRY_FINITE_APERTURE_ANCHOR.md`。

### 3.3 Optical pin beam / radial autofocusing / inward energy redistribution

主要锚点：

- Zhang et al., APL Photonics 2019, DOI `10.1063/1.5095996`。

已确认：

- OPB 使用径向 Airy-like phase、opposite transverse-wavevector pairing 和 inward energy flow 形成 autofocusing pin；
- 有 532 nm、约 2 W、约 5 cm phase mask、约 90% modulation efficiency 和 >1 km real-atmosphere demonstration；
- 原文 Gaussian 对照未针对相同 receiver objective 充分优化；
- 原文没有严格的 Kolmogorov distributed-turbulence quantitative contract；
- 原文没有 independent mechanical jitter。

项目提出的待证伪机制假设：

> common-mode mechanical tilt 不会被 OPB 内部 ± transverse-wavevector cancellation 自动消掉。OPB 可能仍围绕倾斜后的新轴形成 pin，但固定 receiver aperture 仍发生整体失配。

这使 OPB 成为 Paper 1 非常有价值的“turbulence robustness ≠ pointing robustness”候选。

当前 readiness：**中等偏高**。机制和连续场公式明确，但实现前还需冻结 source amplitude envelope 与代表 phase-strength / pin-scale。

详见：`docs/literature/ZHANG_2019_OPB_MECHANISM_ANCHOR.md`。

### 3.4 Flat-top / flattened / broad-capture

主要锚点：

- Eyyuboğlu et al., Optics Express 2006, DOI `10.1364/OE.14.004196`；
- Alavinejad et al., Optics and Lasers in Engineering 2008, DOI `10.1016/j.optlaseng.2007.07.003`；
- Jiang et al., Optics Communications 2022, DOI `10.1016/j.optcom.2022.128703`；
- Jiang et al., Applied Optics 2026, DOI `10.1364/AO.578489`。

已确认：

- higher flatness order 在部分 turbulence-only 指标下表现为较小 relative spreading；
- 但 source size、source power、M² 等资源也随 order 改变；
- 按自身 source power 归一以后，固定接收孔径的 PIB 未必随 order 改善；
- Jiang 2022/2026 已经直接研究 flat-top + turbulence + pointing，因此不能声称该交叉本身是空白。

对 Paper 1 的角色：

> 一个可能同时在 turbulence spreading 与 lateral displacement tolerance 上具有同向优势的成熟正对照，但必须严格排除“只是把功率铺宽 / 增加外围资源”的解释。

当前 readiness：**较高**。family 与资源问题明确，主要缺 equal-resource order/scale freeze。

详见：`docs/literature/FLAT_TOP_2006_2008_RESOURCE_AND_TURBULENCE_ANCHOR.md`。

### 3.5 Partial coherence / Gaussian Schell-model

主要链条：

- Borah & Voelz 2010；
- Lee et al. 2013；
- Liu et al. 2014；
- Lee et al. 2016。

已确认：

- coherence-length turbulence optimization 已成熟；
- 2013 年已经做到 turbulence + pointing + aperture 下 beam width / coherence joint optimization；
- 2014 有 turbulence-induced beam-wander/deformation 实验；
- 2016 继续扩展到 aperture、pointing、capacity、beam-width optimization。

因此该家族并不适合包装成 Paper 1 的主要“此前只研究 turbulence、现在第一次加入 jitter”的创新代表。

当前角色：

> **mature joint-optimized positive control / discussion reference**，而不是主 novelty mechanism。

详见：`docs/literature/PARTIAL_COHERENCE_2010_2016_MECHANISM_CHAIN.md`。

---

## 4. 当前机制分类与建议的最小 common-evaluation set

文献调研后，初始“五种 beam name”已收敛为更少的 physics taxonomy：

1. **angular-spectrum redundancy / self-healing** —— Bessel-like；
2. **path diversity** —— Airy array 作为机制锚点，但可能不进入同一排行榜；
3. **radial-phase autofocusing / inward energy redistribution** —— OPB / radial Airy 中选一代表；
4. **flat-top / broad capture / reduced relative spreading**；
5. **partial coherence** —— mature joint-optimized control。

当前建议第一轮真正准备代码的最小集合：

> **Gaussian + Bessel + OPB + flat-top**。

理由：

- 机制互相区分较明显；
- 仍属于同一有限 Tx/Rx aperture + direct-detection task；
- 计算复杂度可控；
- Airy path diversity 属多 beam architecture，硬件资源不同；
- partial coherence 已有成熟 turbulence–pointing optimization，更适合控制与讨论。

此建议**尚未冻结**，正是本次外部审查要重点判断的内容之一。

---

## 5. UAV/PAT residual jitter 的现实证据链

### 5.1 固定翼高性能实飞锚点

Lei, Li, Zhang 2019：两架 Y-12 固定翼真实飞行，约 300 km/h，10–144 km acquisition/tracking：

- coarse tracking error约 8.68 μrad (1σ)；
- fine tracking error约 8.19 μrad (1σ)。

证据角色：

> real-flight high-performance airborne closed-loop order-of-magnitude anchor。

不能直接等同于低 SWaP 多旋翼 per-axis residual。

### 5.2 多旋翼实际悬停锚点

Trinh et al., IEEE Access 2021, DOI `10.1109/ACCESS.2021.3117266`：

- DJI Matrice 600 Pro 六旋翼 + Ronin MX gimbal + CCR；
- one-way LoS约 101–102 m，roundtrip约 202–204 m；
- ground FSM + QD + PID fine-tracking；
- tracking 前 telescope-entrance AoA standard deviation约 1.17–2.67 mrad；
- tracking 后 PM-plane residual AoA Gaussian-fit standard deviation约 27–42 μrad per axis；
- hovering-related AoA frequency content mostly <50 Hz，少量延伸到约 200 Hz；
- beam-centroid displacement coherence time约 700 ms。

该实验是 retro-reflected double-pass，不可直接继承为本项目 one-way transmitter-side `sigma_theta`；但它是当前高价值的 multirotor actual-flight engineering-range anchor。

详见：`docs/literature/TRINH_2021_MULTIROTOR_RETRO_FINE_TRACKING_ANCHOR.md`。

### 5.3 当前场景判断

目前可以支持：

> realistic post-tracking airborne residual 可以跨越数 μrad 到数十 μrad，强烈依赖 platform / SWaP / tracking architecture。

当前不支持：

> “典型多旋翼 UAV 的 per-axis post-PAT residual 必然等于某个单一 μrad 数值”。

因此建议 Paper 1 仍以 dimensionless jitter 为主科学坐标：

\[
j=\frac{L\sigma_\theta}{w_{ref}},
\]

再用 8–10 μrad fixed-wing anchor 与 30–40 μrad multirotor engineering anchor 做物理映射。

---

## 6. turbulence + pointing 共用方法与数值模型证据

### 6.1 independent mechanical jitter 表示

Liu/Jiang IEEE Access 2021 支持将 independent pointing 作为发射角倾斜进入 wave optics：

\[
U_0'(x,y)=U_0(x,y)\exp[ik(\theta_xx+\theta_yy)].
\]

若采用零均值各向同性 Gaussian reduced model，则 `sigma_theta` 明确定义为**单轴 angular standard deviation**。

Gaussian jitter implementation 可用：

\[
W_{eff}^2=W^2+4L^2\sigma_\theta^2
\]

作为 radius convention 一致时的 sanity check。

### 6.2 finite-aperture received power

通信主观测保持：

\[
P_R=\iint_{A_R}|U_L|^2dA,
\qquad H=P_R/P_T.
\]

主统计来自 realization-level finite-aperture received power：ECDF、低分位、必要时 outage。

point intensity、peak、scintillation 只作机制解释，不能单独证明通信优势。

### 6.3 phase-screen low-frequency 要求

Chen et al., Applied Optics 2020 显示低空间频率欠采样会系统性低估：

- beam-wander variance；
- long-term beam radius；
- 部分 scintillation quantities。

因此 production turbulence module 必须对账 beam-wander variance 和 long-term radius，不能只看 phase RMS 或 spot image。

### 6.4 longitudinal screen placement

Chahine et al. 2020 支持：

> screen number / spacing 不应作为经验固定常数；应根据连续理论与目标 observable 收敛决定。

对近地近似恒定 `Cn²` 的水平链路可以先从等距 multi-screen 开始，但屏数必须由 beam wander / long-term radius / scintillation / received-power convergence 验证。

---

## 7. 已知 direct competitors 与创新边界

当前已经明确不能使用以下表述：

- “首次同时研究 turbulence 与 pointing error”；
- “首次在 phase-screen wave optics 中加入 pointing error”；
- “首次研究 structured beam + turbulence + pointing”；
- “首次研究 flat-top + turbulence + pointing”；
- “首次做 Gaussian–LG 的 jitter optimization”。

关键 direct competitors：

- Liu/Jiang 2021：single-layer phase screen + pointing error；
- Jiang 2022/2026：flat-top + turbulence + pointing / BER；
- Liu et al. 2022：aircraft-platform HG + turbulence + pointing + fade probability；
- Badás 2024/2026：jitter-only Gaussian–LG / annular / super-Gaussian optimization，主要约束 Paper 2。

因此 Paper 1 真正可能的贡献必须落在：

> **跨机制、统一资源、distributed turbulence、independent residual jitter、finite-aperture low-tail reliability，以及 mechanism sensitivity / failure map。**

这一创新边界尚需外部审查确认是否足够强。

---

## 8. 当前参数来源 readiness

完整盘点见 `docs/literature/PAPER1_PARAMETER_SOURCE_STATUS.md` 与 `docs/PAPER1_PARAMETER_MAPPING_MATRIX.md`。

### Bessel

- canonical field 与原文参数充分；
- 无量纲结构参数可用 `chi_B=k_r a_T`；
- Eyyuboğlu 2013 参数大致映射到 `chi_B ~ O(5–20)`；
- blocker：circular-truncated J0 vs Bessel-Gaussian。

### OPB

- continuum phase 可写为：

\[
U_{OPB}(r)=C A(r)\exp\left[-i\frac43k\sqrt\beta r^{3/2}\right]\Pi(r/a_T);
\]

- 可用 aperture-edge phase strength 或 target pin-scale ratio 做相似缩放；
- blocker：`A(r)`、代表 `beta` / target pin scale、是否需要真实 mask discretization。

### flat-top

- nested flat-top / multi-Gaussian family 与资源关系明确；
- blocker：canonical expression 对账、moderate order + high-order stress point、equal-power / common-aperture rescaling。

### Airy

- source-ready，但 mechanism taxonomy 已分裂；
- blocker 是“是否应进入共同评价”，不是缺公式。

### partial coherence

- source-ready，甚至 joint optimization 文献过于充分；
- blocker 是角色选择，而不是参数来源。

---

## 9. 当前提出的 common-resource comparison 方案

### Level A：common-resource / literature-mechanism comparison

所有 coherent source fields 统一：

- wavelength `lambda`；
- propagation distance `L`；
- circular Tx aperture `a_T`；
- circular Rx aperture `a_R`；
- post-aperture transmitted power `P_T`；
- same turbulence realizations；
- same jitter realizations。

并对每种场报告：

- source `r50/r80/r95`；
- peripheral energy；
- transverse spatial-frequency / angular-spectrum scale；
- no-disturbance receiver `r50/r80`；
- nominal capture `H0`；
- 必要的 generation efficiency / loss。

这些资源先报告，不强行全部匹配。

### Level B：one-scale diagnostic retuning

如果 Level A 出现明显结构差异，每个 structured family 最多开放**一个尺度自由度**，用于排除“只是宽一点 / 聚焦一点”的解释。

当前候选诊断方式：

- 匹配无扰动 `H0`；或
- 匹配无扰动 receiver-plane characteristic scale。

最终只选一种。

### Gaussian baseline

Gaussian 至少包含：

1. G0 common-resource Gaussian；
2. G1 optimized-Gaussian envelope，对少量 `w_G, f_G` 做低维搜索。

理由：必须排除 structured beam 只是击败一个未调优 Gaussian 的可能。

---

## 10. 下一步盘点：进入 Stage B 前还剩什么

当前不建议继续无限搜索新的 beam names。进入 Stage B 前主要只剩四个 blocker group。

### Blocker A：代表机制集合

需要外部审查确认：

- 第一轮是否应采用 `Gaussian + Bessel + OPB + flat-top`；
- Airy path diversity 是否只保留为机制讨论；
- partial coherence 是否只作为 mature positive control；
- 是否存在一个被遗漏且必须进入主集合的独立 anti-turbulence mechanism。

### Blocker B：field-specific representative freeze

- Bessel：circular-truncated J0 vs Bessel-Gaussian；
- OPB：`A(r)`、代表 phase strength / pin scale；
- flat-top：canonical field、moderate order、high-order stress point；
- Gaussian：G0/G1 的 `w_G,f_G` 合理搜索范围。

这些应由文献参数与统一资源映射决定，不允许为得到好结果而调参。

### Blocker C：common physical scene

需要冻结第一版主场景的：

- `lambda`；
- `L`；
- `D_T`；
- `D_R`；
- turbulence strength range；
- `L0/l0`；
- dimensionless jitter range 与少量 physical anchors。

其中 `sigma_theta` 不建议冻结成单一“典型 UAV”值。

### Blocker D：最小 numerical validation contract

在 structured fields 进入 turbulence 前，Gaussian turbulence module 至少应验证：

- free-space propagation；
- power conservation / aperture integration；
- jitter analytic sanity；
- beam-wander variance；
- long-term beam radius；
- selected scintillation quantity；
- phase-screen number / spacing convergence；
- low-frequency treatment sensitivity。

不需要工程级 CI 或大规模审计。

---

## 11. 当前建议的 Stage B 启动顺序

如果外部审查认为当前路线基本成立，建议按以下最小顺序推进：

1. 冻结 `Paper 1 v0.3 scientific contract`；
2. 冻结 first common scene 与 Gaussian radius convention；
3. 只实现 Gaussian free-space + finite aperture + jitter sanity；
4. 加入 production multi-screen turbulence，并完成 Gaussian beam-wander / long-term-radius validation；
5. 实现 Bessel、OPB、flat-top 三个代表场；
6. 先做极少量 turbulence-only / jitter-only / joint smoke points；
7. 只有出现机制差异后才展开 coarse sensitivity map；
8. 不在第一轮为 structured fields 做完整 joint optimization；
9. 若 structured fields 全部在 optimized Gaussian 下失去有意义差异，应允许 Paper 1 结论转向“现有 anti-turbulence mechanisms 在 realistic jitter 下普遍压缩/退化”，而不是强行救结果；
10. Paper 2 仍保持 conditional，不提前启动。

---

## 12. 当前负责人判断（供审查者挑战，而非结论）

### 当前倾向 GO

- Paper 1 的问题已经从“比较新光束”收敛为“跨机制 sensitivity / failure analysis”；
- 文献已经基本覆盖 Bessel、Airy、OPB、flat-top、partial coherence 五类最初候选；
- field definitions 与参数来源已足以进入统一映射准备；
- UAV/PAT residual-jitter 已有 fixed-wing 与 multirotor 实验数量级锚点；
- turbulence numerical method 已有 low-frequency / screen-placement 护栏；
- direct competitors 已证明“joint turbulence + pointing”本身不是创新，但尚未发现明显覆盖当前跨机制 failure-map 问题的工作。

### 当前最大风险

1. 最终所谓机制差异可能被 optimized Gaussian + scale/resource matching 大幅压缩；
2. OPB / Bessel / flat-top 的 literature advantage 中可能有相当部分来自不同 focusing / aperture / peripheral-energy resources；
3. Paper 1 若只得到“大家都怕 jitter”而没有明确 mechanism-dependent boundary，论文力度可能不足；
4. UAV 实际 residual 与研究模型之间仍需透明地用 dimensionless map 连接，不能把某篇实验数值直接冒充通用场景；
5. 现有 direct-competitor 检索虽然已较深入，但仍需外部审查者判断是否遗漏关键 structured-beam + turbulence + pointing 系列。

---

## 13. 建议外部审查者的阅读顺序

如果只进行一次高层审查，建议按以下顺序：

1. `docs/RESEARCH_STAGE_BOUNDARY.md`；
2. 本文件；
3. `docs/KEY_LITERATURE_MAP.md`；
4. `docs/PAPER1_PARAMETER_MAPPING_MATRIX.md`；
5. `docs/SCIENTIFIC_CONTRACT_EVIDENCE_DELTAS.md`；
6. `docs/literature/PAPER1_PARAMETER_SOURCE_STATUS.md`；
7. 根据争议点选择具体逐篇锚点阅读。

若只审查 4 篇代表性锚点，建议：

- `EYYUBOGLU_2013_BESSEL_RESOURCE_ANCHOR.md`；
- `ZHANG_2019_OPB_MECHANISM_ANCHOR.md`；
- `FLAT_TOP_2006_2008_RESOURCE_AND_TURBULENCE_ANCHOR.md`；
- `TRINH_2021_MULTIROTOR_RETRO_FINE_TRACKING_ANCHOR.md`。

---

## 14. 请求的外部审查输出

请不要只给泛泛的“方向可行/不可行”。希望审查输出至少包含：

1. **总决策：CONTINUE / REVISE / STOP**；
2. Paper 1 科学问题是否足以成为独立论文；
3. 机制分类和 proposed core set 是否合理；
4. 必须补充或删除的关键文献/机制；
5. common-resource / optimized-Gaussian fairness contract 是否充分；
6. UAV/PAT jitter evidence 是否足以开始 Stage B；
7. turbulence numerical validation contract 是否存在明显缺口；
8. 最危险的过度宣称是什么；
9. 进入代码前必须关闭的最少 3–5 个 blocker；
10. 建议的最小下一步，避免不必要的大规模验证。

配套问题清单见：`docs/review/PAPER1_EXTERNAL_REVIEW_QUESTIONS.md`。
