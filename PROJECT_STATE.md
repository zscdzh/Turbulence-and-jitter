# 项目状态——无人机 FSO 抗湍流光束的抖动敏感性与后续联合设计

**更新日期：** 2026-08-07  
**已接受主分支基线：** `main@16c02105a066cb123035f209c8f103abe13df88f`  
**当前工作分支：** `docs/ai-governance-initialization`（Draft，尚未合并）  
**当前阶段：** Paper 1 / Stage A——关键文献与抗湍流机制地图；尚未建立正式科学代码链，尚未运行自由空间或湍流仿真。  
**当前路线裁决：** Paper 1 文献与机制研究 **GO**；Paper 1 后续统一评价 **GO 但等待文献冻结**；Paper 2 低维联合设计 **CONDITIONAL GO**。  
**权威阶段边界：** `docs/RESEARCH_STAGE_BOUNDARY.md`

本文件只记录当前仓库和负责人已确认决策能够支持的状态。Draft PR、计划参数、文献中的示例数字和未运行模型均不得写成已支持科学结果。

## 一、项目原始科学问题

### Paper 1：当前主问题

现有文献已经提出多类 turbulence-resistant beams，但它们大多围绕 atmospheric turbulence 的传播、闪烁、beam wander、模式保持、自愈或平均功率等指标设计和评价，并不等价于已经针对 UAV/PAT 独立机械 residual jitter 优化。

当前主问题是：

> 当 independent mechanical residual pointing jitter 被加入以后，不同抗湍流机制的原有优势哪些能够保持、哪些明显退化、哪些发生排序反转？这种差异能否用有限孔径捕获特性、长期光斑尺度、外围能量或其他少量结构描述量形成可解释的 sensitivity map、applicability regime 或 failure boundary？

Paper 1 不是“寻找 joint optimum beam”，也不是“第一次联合 turbulence 与 pointing error”。

### Paper 2：条件性后续问题

只有 Paper 1 得到稳定机制 trade-off 后，才研究：

> 能否依据 Paper 1 的失效机制与资源权衡，设计一个少参数、可解释、可实现的 turbulence–jitter co-robust beam，并在与 optimized Gaussian 的公平比较中得到稳定的联合收益？

Paper 2 才讨论 joint objective、joint optimum 和低维联合设计。

## 二、当前研究阶段

### Stage A：关键文献与机制地图

**状态：当前正在进行。**

当前首要工作不是写传播代码，而是建立足以冻结 Paper 1 科学契约的关键文献库。

文献按“抗湍流机制”组织，而不是按光束名字无边界扩张。当前需要覆盖但尚未冻结的机制包括：

- self-healing / angular-spectrum redundancy；
- caustic / self-accelerating propagation；
- self-focusing / pin-like / longitudinal concentration；
- flat-top / flattened / super-Gaussian；
- partial coherence / statistical beam shaping；
- 只有在提供独立机制且数值复杂度可控时，才考虑 vector / mode-diversity 类补充。

每类优先寻找机制锚点、强性能论文和必要的实验论文。

从每篇关键文献提取：

- 发射场数学定义与关键参数；
- 作者声称的抗湍流机制；
- turbulence model 与适用范围；
- 评价指标；
- 发射/接收口径；
- Gaussian 基线和比较规则；
- 总功率、外围能量、生成损耗等资源；
- 是否包含 turbulence-induced beam wander；
- 是否包含 independent pointing jitter；
- 参数属于实测、引用、理论定义还是仿真假设；
- 对整体 lateral displacement 的潜在敏感性。

目标规模：先初筛约 30–40 篇直接相关文献，再精读约 15–20 篇关键锚点；以“新增文献不再实质改变机制分类、模型边界或创新判断”为证据饱和标准，而不是机械凑篇数。

### Stage B：Paper 1 统一评价

**状态：路线 GO，但尚未授权正式实现。**

只有在 Stage A 完成后，才从文献中选择约 3–5 个机制真正不同的代表光束。

统一评价至少比较：

- turbulence only；
- jitter only；
- turbulence + independent jitter。

第一层优先保留原文有依据的代表参数，回答“原抗湍流设计加入 jitter 后还剩多少优势”。第二层只在必要时允许有限尺度 retuning 和 optimized Gaussian 对照，用于区分结构机制与单纯光斑变宽/资源增加。

Paper 1 不要求为每种 structured beam 求完整 joint optimum，不为了得到积极结果给每个模式增加多参数自由度。

### Paper 2：低维联合设计

**状态：CONDITIONAL GO，尚未授权。**

flattened-/super-Gaussian、Gaussian–LG/annular-like 等目前只保留为可能的设计种子。最终是否采用任何一种结构必须由 Paper 1 的机制结果决定。

Badás 2024 等 jitter-only 工作主要用于约束 Paper 2 的零假设和创新边界，不应反过来定义 Paper 1 的任务。

## 三、当前共用物理边界

以下是两篇论文可能共用、但仍需文献冻结的模型边界：

### 计划包含

- 近地 UAV-FSO 的波动光学传播；
- 圆形有限发射与接收孔径；
- 多相位屏 distributed turbulence；
- turbulence-induced beam wander；
- independent mechanical angular jitter；
- 后续可选 static/slow boresight bias；
- 大面积直接探测下的 finite-aperture received power。

### 当前不包含

- 完整无人机六自由度动力学；
- 详细 PAT/FSM 控制器与飞控闭环；
- AO 瞬时补偿；
- 单模光纤耦合；
- 模式分解或相干接收；
- 复杂编码与完整 receiver noise chain；
- 高维像素级逆设计或神经网络。

## 四、已接受的方法学定义

来自 Liu/Jiang 2021 的逐篇精读，当前已经接受但仍需进入最终科学契约的共用方法增量见 `docs/SCIENTIFIC_CONTRACT_EVIDENCE_DELTAS.md`。

当前包括：

1. independent mechanical residual jitter 主链优先用 transmitter angular tilt；
2. `sigma_theta` 表示单轴 angular standard deviation；
3. `W_eff^2 = W^2 + 4 L^2 sigma_theta^2` 可作为 Gaussian jitter broadening 的解析 sanity check，前提是 beam-radius convention 一致；
4. finite-aperture received power 是通信主观测，point irradiance 和 scintillation 只作辅助；
5. single-layer `0.36 L` phase screen 只作 weak-turbulence benchmark，不作为正式 distributed-turbulence model；
6. turbulence beam wander、independent jitter 和 boresight bias 必须独立记账。

## 五、当前关键变量

以下只列共用变量；Paper 2 的设计变量尚未进入当前主状态。

| 变量 | 含义 | 单位 | 当前状态 |
|---|---|---:|---|
| `lambda` / \(\lambda\) | 波长 | m | UAV 主场景值待文献冻结；1550 nm 仍只是强候选，不视为已冻结 |
| `transmitter_diameter` / \(D_T\) | 发射清孔径直径 | m | 待真实终端/代表文献冻结 |
| `receiver_diameter` / \(D_R\) | 接收孔径直径 | m | 待文献冻结 |
| `range` / \(L\) | 链路距离 | m | 待 UAV 场景文献冻结 |
| \(r_0\) | Fried coherence length | m | 定义与计算方法待 turbulence 文献冻结 |
| `jitter_sigma` / \(\sigma_\theta\) | 单轴独立机械 residual angle std | rad | 定义已接受，真实 UAV/PAT 数值待实测/系统文献 |
| \(\rho_{bw}\) | turbulence-induced receive-plane centroid wander | m | 必须来自 turbulence propagation |
| \(\rho_j=L\theta_j\) | independent mechanical jitter 位移尺度 | m | 共用诊断量 |
| \(\rho_b\) | static/slow boresight bias | m | 第一篇可先设 0，后续是否加入待定 |
| \(P_T\) | 总发射功率 | W 或归一化 1 | 归一化协议待机制比较规则冻结 |
| \(P_R\) | 单 realization finite-aperture received power | W 或归一化功率 | 主观测 |
| \(H=P_R/P_T\) | normalized received power | 无量纲 | 主统计输入 |
| `mechanism_class` | 抗湍流机制分类 | 类别 | Stage A 正在建立 |
| `literature_anchor` | 代表机制的原始/关键文献 | 引用 | Stage A 正在建立 |
| `resource_ledger` | 功率、口径、外围能量、生成损耗等 | 多单位 | Stage A/Stage B 必须记录 |

当前不把 flattened-Gaussian 阶数、Gaussian–LG 权重或 relative waist 视为 Paper 1 的关键变量；它们属于可能的 Paper 2 设计变量。

## 六、Paper 1 计划中的输入—处理—输出关系

Stage A 的当前数据链是：

\[
\{\text{关键文献}\}
\rightarrow
\{\text{机制、场定义、参数来源、资源、指标、pointing 覆盖}\}
\rightarrow
\{\text{机制证据矩阵}\}
\rightarrow
\{\text{Paper 1 代表机制与统一评价协议}\}.
\]

Stage B 冻结后，才建立数值链：

\[
\{\text{代表抗湍流光场}\}
\rightarrow
\{\text{turbulence / jitter / joint propagation}\}
\rightarrow
U_L(x,y)
\rightarrow
P_R
\rightarrow
\{\mathrm{ECDF},\text{low-tail metrics},\text{mechanism sensitivity / failure regime}\}.
\]

## 七、当前仓库代码与数据链

### 已存在

- 负责人层科学与治理文档；
- `docs/RESEARCH_STAGE_BOUNDARY.md`：本轮路线纠正；
- `docs/SCIENTIFIC_CONTRACT_EVIDENCE_DELTAS.md`：已接受文献证据增量；
- `docs/literature/`：逐篇文献锚点；
- Frozen Wave 独立支线储备文档。

### 核心科学代码

**未建立。**

当前没有已接受的 free-space propagation、multi-screen turbulence、representative structured fields、receiver integration 或 statistics 代码链。

### 正式运行与结果

**未建立。** `results/` 仍无已接受科学结果。

## 八、当前开放 PR 状态

- PR #1：治理与项目状态初始化分支，当前正在吸收路线纠正与文献证据，拟作为统一文档 PR；
- PR #2：Liu/Jiang 2021 文献证据分支，其有效内容已迁入 PR #1，后续应关闭为 superseded，避免两个 Draft PR 维持不同状态。

在 PR #1 合并前，`main@16c02105...` 仍是已接受主分支基线；本文件中的新路线纠正属于 Draft 待合并内容。

## 九、已支持的结论

当前支持的是路线与文献边界，不支持任何 structured-beam 数值性能结论：

1. “同时考虑 turbulence 与 pointing error”本身不是创新；
2. 现有多类 turbulence-resistant beams 大多不是为 independent mechanical jitter 设计；
3. Paper 1 应先系统研究这些抗湍流机制在 independent jitter 下的敏感性、失效和排序变化；
4. Paper 1 的核心价值应是机制规律和适用域，而不是模式排行榜或 joint design；
5. Paper 2 才允许根据 Paper 1 的 trade-off 做 low-dimensional turbulence–jitter co-design；
6. flattened-/super-Gaussian、Gaussian–LG 当前只属于 Paper 2 的可能设计种子；
7. finite-aperture received power 作为主链有文献依据，但不是本项目创新本身；
8. single-screen 0.36L 仅可作 weak-turbulence benchmark；
9. Liu/Jiang 2021 的 5–15 microrad 等仿真值不能作为 UAV residual-jitter 场景参数；
10. Frozen Wave 保持独立纵向包络支线，不并入当前 Paper 1/2 主线。

## 十、工作假设

以下仍是需要 Paper 1 验证的假设，不得写成已支持结果：

- self-healing 能恢复局部扰动结构，但不自动抵抗整体 lateral displacement；
- 窄核心/高梯度光斑可能对 jitter 更敏感；
- flat-top 类可能具有较低中心位移敏感性，但其优势可能来自更宽覆盖或额外外围能量；
- partial coherence 降低 scintillation 不必然提高 finite-aperture low-tail power；
- 不同抗湍流机制在加入 jitter 后可能出现排序压缩或反转；
- 这些差异可能被少量 capture/scale/resource descriptors 解释。

## 十一、禁止表述

当前禁止：

- “首次把 turbulence 与 pointing error 联合起来”；
- “已经提出/验证了 turbulence–jitter 联合鲁棒新光束”；
- “Paper 1 的目标是寻找 joint optimum structured beam”；
- “flattened-Gaussian 或 Gaussian–LG 已经是本项目固定候选”；
- “5–15 microrad 是典型 UAV/PAT residual jitter”；
- “single-layer phase screen 足以代表正式中强湍流模型”；
- “降低 scintillation 等价于提高通信可靠性”；
- “self-healing 天然等价于 anti-jitter”；
- “当前仓库已经有可复现数值结果”。

## 十二、当前唯一主要不确定性

当前唯一最重要的不确定性已经从“是否能设计出 joint optimum beam”改为：

> 文献中不同 turbulence-resistant mechanisms 面对 independent UAV/PAT residual jitter 时，哪些机制保持、退化或失效？我们能否找到足够有代表性的机制集合与可信参数/评价依据，使 Paper 1 成为机制论文而不是光束排行榜？

任何当前工作都应直接减少这一不确定性。

## 十三、允许的最小下一步

当前只允许推进 Paper 1 / Stage A 文献工作：

1. 建立 `KEY_LITERATURE_MAP`；
2. 按机制初筛约 30–40 篇直接相关论文；
3. 选出约 15–20 篇锚点逐篇精读；
4. 对每篇记录模型定义、参数来源、抗湍流主张、资源代价、pointing 覆盖和可继承性；
5. 完成 direct-competitor 检索；
6. 文献证据饱和后，再冻结 Paper 1 代表机制、场参数和统一评价协议；
7. 只有在负责人再次批准后，才讨论数值实现。

当前**不允许直接执行旧 `docs/CODEX_HANDOFF.md` 中的光场实现任务**，也不允许直接开始 flattened-Gaussian / Gaussian–LG 联合优化或大规模多相位屏 Monte Carlo。

## 十四、仓库读取顺序

新的重要对话应依次读取：

1. `AI_RESEARCH_GOVERNANCE.md`；
2. `PROJECT_STATE.md`；
3. `docs/RESEARCH_STAGE_BOUNDARY.md`；
4. `README.md`；
5. `docs/SCIENTIFIC_CONTRACT_DRAFT.md`；
6. `docs/SCIENTIFIC_CONTRACT_EVIDENCE_DELTAS.md`；
7. `docs/LITERATURE_AND_ROUTE_SYNTHESIS.md`；
8. `docs/literature/` 中相关逐篇锚点；
9. 当前开放/已合并 PR、最近 commit 和后续结果。

较早聊天总结和旧 Codex 交接不得覆盖已经确认的阶段边界。
