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

- Eyyuboğlu, Voelz, Xiao, *Applied Optics* 2013, DOI `10.1364/AO.52.008032`：**ANCHOR_TO_READ / HIGH PRIORITY**。重点是 equal-source-power 与 per-unit-received-power 两种评价下 Bessel 优势明显不同，是资源公平性一级锚点。
- Yuan et al., *Scientific Reports* 2017, *Beam wander relieved orbital angular momentum communication in turbulent atmosphere using Bessel beams*：**ANCHOR_TO_READ / EXPERIMENTAL PERFORMANCE**。重点提取 beam-wander 机制，不直接继承 OAM 接收任务。
- Nelson et al., *Propagation of Bessel and Airy beams through atmospheric turbulence*, arXiv:1312.0620：**ANCHOR_TO_READ / FAILURE-BOUNDARY**。重点是 turbulence 破坏 quasi-nondiffracting 性的尺度边界。

当前 jitter 工作假设：self-healing 不自动 recenter 整体 mechanical displacement；窄核心和外围能量必须与 finite-aperture capture / resource ledger 一起评价。

### B. caustic / self-accelerating / path diversity

代表：Airy / caustic beams。

关键锚点：

- Gu & Gbur, *Optics Letters* 2010, DOI `10.1364/OL.35.003456`：**ANCHOR_TO_READ / MECHANISM**。Airy array 的抗 scintillation 主张来自 self-bending 带来的 path diversity，不应简单归为 self-healing。
- Zhu et al., *Optics Express* 2021, DOI `10.1364/OE.435863`：**ANCHOR_TO_READ / FINITE-APERTURE EXPERIMENT**。包含 limited receiver aperture、turbulence、received power 和 BER；需分离 Airy radial shaping 与 OAM/协议因素。
- Nelson et al. 2013/2014：同时作为 Airy failure-boundary 文献。

当前 jitter 工作假设：independent tilt 可能整体移动/转动设计 caustic trajectory；需要检查 trajectory robustness 是否真的转化为固定孔径功率鲁棒性。

### C. self-focusing / pin-like / longitudinal concentration

代表：optical pin beam (OPB)。

关键锚点：

- Zhang et al., *APL Photonics* 2019, DOI `10.1063/1.5095996`：**ANCHOR_TO_READ / HIGH PRIORITY**。OPB 原始核心文献，理论 + 室内 + outdoor turbulence，直接与 Gaussian intensity stability 比较。
- Nardo et al., 2025, arXiv:2504.01704：**SCREENED / RECENT PERFORMANCE BACKGROUND**。100 km air-to-air simulation、link budget、beam wander 与 transmitter-aperture resource scaling；预印本，不能作为最高等级证据。

当前 jitter 工作假设：self-focusing / narrow high-intensity pin 在 turbulence-only 下可能很强，但可能对 independent tilt 很敏感，是 Paper 1 最值得证伪的机制之一。

### D. partial coherence / incoherent averaging

代表：Gaussian Schell-model / partially coherent transmitter。

关键锚点：

- Borah & Voelz, *Optics Express* 2010, DOI `10.1364/OE.18.020746`：**ANCHOR_TO_READ / OPTIMIZATION BASELINE**。优化 coherence length，并与 outage、beamwidth、curvature 等连接。
- Liu et al., *Optics Letters* 2014, DOI `10.1364/OL.39.003336`：**ANCHOR_TO_READ / EXPERIMENTAL MECHANISM**。实验显示降低 coherence 可减小 turbulence-induced beam wander 与 deformation。
- Drexler, Roggemann, Voelz, *Optical Engineering* 2011, DOI `10.1117/1.3533737`：**ANCHOR_TO_READ / RECEIVED-POWER EXPERIMENT**。直接连接 partially coherent transmitter 与 received-power dropout statistics。

当前 jitter 工作假设：partial coherence 的 robustness 可能伴随 beam spreading，因此对 jitter 的潜在改善必须与 aligned received power / long-term spot / transmitter resource 一起解释。

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

1. Eyyuboğlu et al. 2013 — Bessel / resource fairness；
2. Zhang et al. 2019 — OPB / self-focusing；
3. Gu & Gbur 2010 — Airy array / path diversity；
4. Borah & Voelz 2010 + Liu et al. 2014 — partial coherence；
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
