# KEY_LITERATURE_MAP

**状态：Stage A 工作文档，持续更新**  
**日期：2026-08-07**

本文件用于 Paper 1 的关键文献与机制地图。目标不是完整综述，而是找到足以冻结 Paper 1 代表机制、统一模型和参数证据的锚点文献。

## 1. 当前筛选原则

文献按科学角色而不是按模式名字堆积：

- 抗湍流机制锚点；
- turbulence + pointing 共用方法；
- UAV/PAT residual-jitter 场景证据；
- multi-screen / beam-wander 数值方法；
- direct competitors；
- Paper 2 jitter-only / design 前序。

每篇文献最终标记：`SCREENED`、`ANCHOR_TO_READ`、`READ`、`METHOD_ONLY`、`PAPER2_BACKGROUND`、`DIRECT_COMPETITOR` 或 `DROP`。

## 2. Paper 1 抗湍流机制文献——当前最缺

### A. self-healing / angular-spectrum redundancy

代表候选：Bessel / Bessel–Gaussian。

当前任务：

- 找机制奠基/解释文献；
- 找 turbulence robustness 强性能论文；
- 找至少一篇能公开资源代价或实验结果的工作；
- 核对是否已有 independent pointing-error 评价。

**状态：ANCHOR SET NOT FROZEN**

### B. caustic / self-accelerating

代表候选：Airy / caustic beams。

当前任务同上，重点区分 self-healing、beam-wander reduction、trajectory robustness 和 fixed-aperture power。

**状态：ANCHOR SET NOT FROZEN**

### C. self-focusing / pin-like / longitudinal concentration

代表候选：optical pin beam / self-focusing 类。

重点检查：纵向维持与横向 jitter tolerance 是否被混淆；窄热点是否增加 residual-jitter sensitivity。

**状态：ANCHOR SET NOT FROZEN**

### D. flat-top / flattened / super-Gaussian

该类同时连接 Paper 1 与 Paper 2。

已识别：

- 早期 flat-topped beam turbulence propagation / aperture-averaging 工作；
- Jiang et al. 2022：flat-topped beam + atmospheric turbulence + boresight pointing error；
- Jiang et al. 2026：flat-topped beam + pointing error + gamma-gamma turbulence + BER。

Paper 1：研究已有 flat-top turbulence claims 加入 independent jitter 后的机制表现。  
Paper 2：若机制结果支持，才讨论 joint order/scale design。

**状态：DIRECT-COMPETITOR CHAIN IDENTIFIED / REPRESENTATIVE ANCHOR TO READ**

### E. partial coherence / statistical beam shaping

重点核对：scintillation reduction 是否伴随 beam spreading；finite-aperture low-tail power 与 jitter tolerance 是否只是尺度交换。

**状态：ANCHOR SET NOT FROZEN**

### F. vector / mode-diversity

只有在提供独立机制且计算复杂度可控时才加入。

**状态：OPTIONAL / NOT DEFAULT PAPER-1 FAMILY**

## 3. 共用 turbulence + pointing 方法

### Liu / Jiang et al., IEEE Access 2021

*Single-Layer Phase Screen With Pointing Errors for Free Space Optical Communication*  
DOI: `10.1109/ACCESS.2021.3099871`

角色：wave-optics pointing 方法定义、finite-aperture received-power 前序、weak-turbulence benchmark。

状态：**READ / METHOD_ONLY**  
详见 `docs/literature/LIU_JIANG_2021_METHOD_ANCHOR.md`。

### 结构光 direct competitor

已识别 aircraft-platform + Hermite-Gaussian + turbulence + pointing / fade-probability 工作。

角色：证明“structured beam + turbulence + pointing”本身不是空白；需要精读确认模型、Gaussian baseline 和结论边界。

状态：**ANCHOR_TO_READ / DIRECT_COMPETITOR**

## 4. UAV / PAT residual jitter 场景证据

当前已识别但尚未形成可冻结数值范围：

- UAV-specific 3D pointing-error geometry / attitude mapping 文献；
- 几微弧度量级的室内或模拟 airborne PAT tracking 实验；
- 十几微弧度量级的 airborne alignment / tracking 实验；
- 实际 rotary-wing UAV FSO 外场链路论文。

当前结论：

- `sigma_theta` 的定义已较清楚；
- 真实 UAV + PAT/FSM post-loop residual jitter 的代表 RMS、PSD、相关时间和各向异性仍未冻结；
- 室内 tracking accuracy 不得直接写成实飞 residual-jitter distribution。

状态：**HIGH PRIORITY / ANCHORS TO READ**

## 5. multi-screen / beam-wander 数值方法

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

## 6. Paper 2 背景——不得反向定义 Paper 1

### Badás et al., Optics Express 2024

DOI: `10.1364/OE.533250`

角色：jitter-only optimized Gaussian / Gaussian–LG / annular-like irradiance 前序。

状态：**READ / PAPER2_BACKGROUND**  
详见 `docs/literature/BADAS_2024_JITTER_OPTIMIZATION_ANCHOR.md`。

### 2026 super-Gaussian / variational optimum work

角色：进一步约束 jitter-only theoretical optimum 与 Paper 2 创新边界。

状态：**ANCHOR_TO_READ / PAPER2_BACKGROUND**

## 7. 当前阅读优先级

优先级不再以 Paper 2 候选为中心。当前顺序建议：

1. 每类 Paper 1 抗湍流机制的代表锚点；
2. structured beam + turbulence + pointing 的 direct competitors；
3. UAV/PAT post-loop residual-jitter 真实证据；
4. multi-screen / low-frequency beam-wander 数值方法；
5. Paper 2 的 jitter-only optimum 文献仅用于保持创新边界更新。

## 8. Stage A 完成标准

进入数值实现前应至少做到：

- 3–5 个机制代表集合可以解释为什么被选中；
- 每个代表场都有可复现数学定义和文献参数来源；
- Gaussian baseline 与资源比较规则可以冻结；
- UAV/PAT jitter 和 turbulence 参数有现实证据范围；
- direct competitors 不再实质改变 Paper 1 科学问题；
- multi-screen beam-wander implementation 有明确方法依据。
