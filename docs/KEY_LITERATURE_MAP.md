# KEY_LITERATURE_MAP

**状态：Stage A 工作文档，持续更新**  
**日期：2026-08-07**

本文件用于 Paper 1 的关键文献与机制地图。目标不是完整综述，而是找到足以冻结 Paper 1 代表机制、统一模型和参数证据的锚点文献。

Round 1 机制筛选详见：`docs/literature/PAPER1_MECHANISM_SCREEN_ROUND1.md`。

## 1. 当前筛选原则

文献按科学角色而不是按模式名字堆积：

- 抗湍流机制锚点；
- turbulence + pointing 共用方法；
- UAV/PAT residual-jitter 场景证据；
- multi-screen / beam-wander 数值方法；
- direct competitors；
- Paper 2 jitter-only / design 前序。

每篇文献最终标记：`SCREENED`、`ANCHOR_TO_READ`、`READ`、`METHOD_ONLY`、`PAPER2_BACKGROUND`、`DIRECT_COMPETITOR` 或 `DROP`。

## 2. Paper 1 抗湍流机制——Round 1 骨架

当前不再按 beam name 无限扩张，优先保留五个主机制。

### A. self-healing / angular-spectrum redundancy

代表：Bessel / Bessel–Gaussian。

关键锚点：

- Eyyuboğlu, Voelz, Xiao, *Applied Optics* 2013, DOI `10.1364/AO.52.008032`：**READ / RESOURCE-FAIRNESS ANCHOR**。equal-source-power 下 Bessel 的 aperture-averaged scintillation 优势较广，但加入 received-power criterion 后优势大幅收缩；论文也没有证明 self-healing 是低 scintillation 的确定原因。详见 `docs/literature/EYYUBOGLU_2013_BESSEL_RESOURCE_ANCHOR.md`。
- Yuan et al., *Scientific Reports* 2017, *Beam wander relieved orbital angular momentum communication in turbulent atmosphere using Bessel beams*：**ANCHOR_TO_READ / EXPERIMENTAL PERFORMANCE**。重点提取 beam-wander 机制，不直接继承 OAM 接收任务。
- Nelson et al., *Propagation of Bessel and Airy beams through atmospheric turbulence*, arXiv:1312.0620：**ANCHOR_TO_READ / FAILURE-BOUNDARY**。重点是 turbulence 破坏 quasi-nondiffracting 性的尺度边界。

当前 jitter 工作假设：self-healing 不自动 recenter 整体 mechanical displacement；窄核心和外围能量必须与 finite-aperture capture / resource ledger 一起评价。

当前从 Eyyuboğlu 2013 接受的 Paper-1 评价护栏：

- 不用 scintillation 单指标宣称通信优势；
- equal transmitted power 是必要资源口径，但不足以单独保证公平；
- 还需报告 transmitter aperture、外围能量、receiver aperture、无扰动接收功率和 receiver-plane characteristic scale；
- Bessel turbulence-only claim 应优先以低阶、尤其 `n=0` 为代表，避免无必要地扩展高阶/OAM模式；
- 最终使用 square-truncated Bessel、circular-truncated Bessel 还是 Bessel-Gaussian 尚未冻结。

### B. caustic / self-accelerating / path diversity

代表：Airy / caustic beams。

关键锚点：

- Gu & Gbur, *Optics Letters* 2010, DOI `10.1364/OL.35.003456`：**READ / PATH-DIVERSITY MECHANISM ANCHOR**。四个空间分离 Airy beamlets 依靠 self-bending 走过弱相关 turbulence paths，再在指定接收距离重新汇合；其 cross-scintillation 接近零、array scintillation 接近独立分量的 `1/N` 极限。该工作更应归类为 Airy-trajectory-enabled spatial/path diversity，而非普通“self-healing”。它依赖 multi-beamlet source footprint 和 distance-specific recombination，因此未必进入最终 monolithic-beam common-evaluation set。详见 `docs/literature/GU_GBUR_2010_AIRY_PATH_DIVERSITY_ANCHOR.md`。
- Zhu et al., *Optics Express* 2021, DOI `10.1364/OE.435863`：**ANCHOR_TO_READ / FINITE-APERTURE EXPERIMENT**。包含 limited receiver aperture、turbulence、received power 和 BER；需分离 Airy radial shaping 与 OAM/协议因素。该文将决定最终是否选 single/ring Airy 作为共同评价代表。
- Nelson et al. 2013/2014：同时作为 Airy failure-boundary 文献。

当前 jitter 工作假设：common-mode mechanical tilt 可能在保留 path-decorrelation 机制的同时整体移动 beamlet recombination region；因此低 scintillation 不保证固定接收孔径功率仍高。该判断是待验证机制先验，不是 Gu & Gbur 已证明结果。

### C. self-focusing / pin-like / longitudinal concentration

代表：optical pin beam (OPB)。

关键锚点：

- Zhang et al., *APL Photonics* 2019, DOI `10.1063/1.5095996`：**READ / MECHANISM + EXPERIMENTAL ANCHOR**。OPB 通过 radially assembled Airy-like fragments、opposite transverse-wavevector pairing 和 inward energy flow 形成 autofocusing pin；论文给出 532 nm、约 2 W、约 5 cm phase mask、约 90% modulation efficiency，并展示 >1 km real-atmosphere propagation，但 Gaussian baseline 未针对相同 receiver objective 优化，且作者明确承认没有 rigorous Kolmogorov-turbulence modeling。详见 `docs/literature/ZHANG_2019_OPB_MECHANISM_ANCHOR.md`。
- Nardo et al., 2025, arXiv:2504.01704：**SCREENED / RECENT PERFORMANCE BACKGROUND**。100 km air-to-air simulation、link budget、beam wander 与 transmitter-aperture resource scaling；预印本，不能作为最高等级证据。

当前 Paper-1 机制假设：OPB 的内部 opposite-wavevector cancellation 可维持其相对结构，但一个施加给整个 source field 的 common-mode mechanical tilt 不会被 ±wavevector pairing 自动消除；OPB 可能仍围绕 tilted axis 形成 pin，却整体偏离固定 receiver。该判断是本项目根据原文机制提出的待证伪理论先验，不是 2019 论文已证明结论。

### D. partial coherence / incoherent averaging

代表：Gaussian Schell-model / partially coherent transmitter。

当前状态：**READ AS A MECHANISM CHAIN / MATURE JOINT-OPTIMIZATION CONTROL**。

关键链条：

- Borah & Voelz, *Optics Express* 2010, DOI `10.1364/OE.18.020746`：已建立 coherence-length optimization，并直接以 outage 处理 scintillation reduction 与 mean-signal reduction 的 trade-off；
- Lee et al., *Optics Letters* 2013, DOI `10.1364/OL.38.000350`：已在 turbulence + pointing + aperture averaging 条件下联合优化 beam width 与 spatial coherence length；weak turbulence optimum 偏低 coherence，very strong turbulence optimum 可向 coherent limit 回落；
- Liu et al., *Optics Letters* 2014, DOI `10.1364/OL.39.003336`：实验确认降低 spatial coherence 可减小 **turbulence-induced** beam wander 与 deformation；
- Lee et al., *Applied Optics* 2016, DOI `10.1364/AO.55.000001`：进一步研究 partially coherent Gaussian 在 turbulence、beam wander、pointing errors、receiver aperture averaging 下的 beam-width optimization 与 average capacity。

详见 `docs/literature/PARTIAL_COHERENCE_2010_2016_MECHANISM_CHAIN.md`。

当前裁决：partial coherence 是重要成熟对照，但不宜作为 Paper 1 的核心“过去只抗 turbulence、现在首次加 jitter”的代表，因为这一家族的 joint turbulence–pointing optimization 已经相当成熟。若最终需要 positive control / validation case，可以保留；否则优先留在文献和讨论层。

### E. flat-top / flattened / super-Gaussian

该类同时连接 Paper 1 与 Paper 2。

关键锚点：

- Alavinejad, Ghafary, Kashani, *Optics and Lasers in Engineering* 2008, DOI `10.1016/j.optlaseng.2007.07.003`：**ANCHOR_TO_READ / TURBULENCE ORIGIN**。higher flat-top order 在其 analytical model 下表现为较少 turbulence broadening。
- Baykal & Kamacıoğlu, *Optics & Laser Technology* 2013, DOI `10.1016/j.optlastec.2013.04.011`：**ANCHOR_TO_READ / FINITE-APERTURE**。直接研究 flat-top power scintillation 与 receiver aperture averaging。
- Jiang et al., *Optics Communications* 2022, DOI `10.1016/j.optcom.2022.128703`：**DIRECT_COMPETITOR**。已覆盖 flat-top + atmospheric turbulence + jitter/bias + average irradiance / received-power 类问题。
- Jiang et al., *Applied Optics* 2026, DOI `10.1364/AO.578489`：**DIRECT_COMPETITOR / RECENT**。进一步到 pointing error + gamma-gamma turbulence + BER。

当前 jitter 工作假设：flat-top 可能是少数 turbulence mechanism 与 jitter requirement 同方向的正对照，但必须排除“只是把功率铺宽”的尺度/资源交换。

### F. vector / modal / channel-eigenmode 路线

当前只作为 optional literature context，不默认进入 Paper 1 direct-detection mechanism set。

重要入口：

- Cox et al., *IEEE JSTQE* 2020/2021, DOI `10.1109/JSTQE.2020.3023790`：**ANCHOR_TO_READ / REVIEW**。
- Klug, Peters, Forbes, *Advanced Photonics* 2023, DOI `10.1117/1.AP.5.1.016006`：**ANCHOR_TO_READ / MODERN MECHANISM**，channel eigenmode / robust structured light。
- Peters, Cocotos, Forbes, *Advances in Optics and Photonics* 2025, DOI `10.1364/AOP.538883`：**REFERENCE / DIGITAL IMPLEMENTATION REVIEW**。

若其收益依赖 mode sorting、coherent receiver、高维 coding 等不同接收任务，不与当前 finite-aperture direct detection 家族直接排行。

## 3. structured beam + turbulence + pointing direct competitor

### Liu, Zhang, Jiang, Qin, J. Phys.: Conf. Ser. 2022

*Fade probability simulation analysis for aircraft platform wireless optical communication based on Hermite-Gaussian beam*  
DOI: `10.1088/1742-6596/2252/1/012043`

状态：**DIRECT_COMPETITOR / ANCHOR_TO_READ**

已确认其覆盖：

- aircraft-platform motivation；
- Hermite–Gaussian vs Gaussian；
- single-layer phase screen + pointing error；
- finite receiver aperture / received-power fluctuation；
- fade probability；
- 10–50 microrad 的 simulation pointing range。

它证明“structured beam + turbulence + pointing”本身不是空白，但仍未覆盖本项目计划中的机制统一比较、distributed multi-screen、beam-wander / independent jitter 显式分离、resource-matched optimized Gaussian 和 sensitivity/failure map。

其“aircraft pointing several tens of microradian”属于 scenario assumption / secondary-source statement，不视为 UAV/PAT post-loop 实测证据。

## 4. 共用 turbulence + pointing 方法

### Liu / Jiang et al., IEEE Access 2021

*Single-Layer Phase Screen With Pointing Errors for Free Space Optical Communication*  
DOI: `10.1109/ACCESS.2021.3099871`

角色：wave-optics pointing 方法定义、finite-aperture received-power 前序、weak-turbulence benchmark。

状态：**READ / METHOD_ONLY**  
详见 `docs/literature/LIU_JIANG_2021_METHOD_ANCHOR.md`。

## 5. UAV / PAT residual jitter 场景证据

当前已识别但尚未形成可冻结数值范围：

- UAV-specific 3D pointing-error geometry / attitude mapping 文献；
- 几微弧度量级的室内或模拟 airborne PAT tracking 实验；
- 十几微弧度量级的 airborne alignment / tracking 实验；
- 实际 rotary-wing UAV FSO 外场链路论文。

当前结论：

- `sigma_theta` 的定义已较清楚；
- 真实 UAV + PAT/FSM post-loop residual jitter 的代表 RMS、PSD、相关时间和各向异性仍未冻结；
- 室内 tracking accuracy 或论文人为扫描范围不得直接写成实飞 residual-jitter distribution。

状态：**HIGH PRIORITY / ANCHORS TO READ**

## 6. multi-screen / beam-wander 数值方法

当前已识别：

- Lane et al. 1992：Kolmogorov phase screen / subharmonic 基础；
- Applied Optics 2020：phase-screen precision 对 beam wander、long-term beam radius、scintillation 的影响；
- JOSA A 2020：不同 phase-screen generation techniques 比较；
- randomized spectral sampling / low-frequency 方法；
- non-uniform multi-screen placement / split-step 方法。

当前优先问题：

- low-frequency sampling 是否正确保留 beam wander；
- formal model 应使用何种 spectrum；
- screen number / spacing 怎样根据 propagation regime 确定；
- grid/window convergence 的最低要求。

状态：**HIGH PRIORITY / ANCHORS TO READ**

## 7. Paper 2 背景——不得反向定义 Paper 1

### Badás et al., Optics Express 2024

DOI: `10.1364/OE.533250`

角色：jitter-only optimized Gaussian / Gaussian–LG / annular-like irradiance 前序。

状态：**READ / PAPER2_BACKGROUND**  
详见 `docs/literature/BADAS_2024_JITTER_OPTIMIZATION_ANCHOR.md`。

### 2026 super-Gaussian / variational optimum work

角色：进一步约束 jitter-only theoretical optimum 与 Paper 2 创新边界。

状态：**ANCHOR_TO_READ / PAPER2_BACKGROUND**

## 8. 当前精读优先级

### 第一批：决定 Paper 1 机制结构

1. ~~Eyyuboğlu et al. 2013 — Bessel / resource fairness~~ **READ**；
2. ~~Zhang et al. 2019 — OPB / self-focusing~~ **READ**；
3. ~~Gu & Gbur 2010 — Airy array / path diversity~~ **READ**；
4. ~~Borah & Voelz 2010 + Lee 2013 + Liu 2014 + Lee 2016 — partial coherence chain~~ **READ / MATURE CONTROL**；
5. Alavinejad et al. 2008 — flat-top turbulence origin；
6. Liu et al. 2022 HG — direct competitor。

### 第二批：强化实验和边界

7. Yuan et al. 2017 — Bessel beam wander experiment；
8. Zhu et al. 2021 — Airy finite-aperture communication experiment；
9. Baykal & Kamacıoğlu 2013 — flat-top aperture averaging；
10. Cox et al. 2020/2021 — structured-light turbulence review；
11. Klug et al. 2023 — channel robust eigenmodes。

## 9. Stage A 完成标准

进入数值实现前应至少做到：

- 3–5 个机制代表集合可以解释为什么被选中；
- 每个代表场都有可复现数学定义和文献参数来源；
- Gaussian baseline 与资源比较规则可以冻结；
- UAV/PAT jitter 和 turbulence 参数有现实证据范围；
- direct competitors 不再实质改变 Paper 1 科学问题；
- multi-screen beam-wander implementation 有明确方法依据。

Round 1 当前结论：**CONTINUE 文献精读，不进入数值实现。**