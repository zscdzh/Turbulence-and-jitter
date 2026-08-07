# AI辅助科研治理规则

**项目名称：** Turbulence-and-jitter——UAV-FSO 抗湍流光束的抖动敏感性与后续联合鲁棒设计  
**更新日期：** 2026-08-07  
**适用范围：** 本仓库中由 ChatGPT、Codex 或其他 AI 辅助开展的文献调研、科学讨论、模型实现、数值仿真、结果解释和论文路线判断  
**阶段权威边界：** `docs/RESEARCH_STAGE_BOUNDARY.md`

本文件规定 AI 如何参与项目，不替代科学契约、项目状态、逐篇文献证据和已经接受的数值结果。

发生冲突时按以下优先级处理：

1. 项目负责人在当前对话中的明确指令；
2. `docs/RESEARCH_STAGE_BOUNDARY.md`、当前已接受科学契约和 `PROJECT_STATE.md`；
3. 本治理文件；
4. 一般代码规范和仓库习惯。

如果发现阶段混淆、定义冲突、文献证据不足、参数未冻结或旧交接文档与当前路线矛盾，应返回 **REVISE**，不得静默选择新定义或继续执行旧任务。

## 一、固定的两篇论文边界

### Paper 1：抗湍流机制的 jitter sensitivity / failure analysis

Paper 1 当前任务是：

> 从文献中识别不同 turbulence-resistant mechanisms，分析并统一评价它们面对 independent mechanical residual jitter 时的保持、退化、排序变化和失效边界。

Paper 1 是“文献机制归纳 + 统一物理评价”，不是联合新光束设计。

Paper 1 不得被改写为：

- flattened-Gaussian joint optimization；
- Gaussian–LG joint optimization；
- 为每种 structured beam 求 turbulence-only / jitter-only / joint optimum；
- 为获得正结果不断增加 mode、polarization、coherence 或高维自由度。

### Paper 2：低维 turbulence–jitter co-design

只有 Paper 1 给出稳定、可解释、不能被普通 Gaussian beam-width optimization 完全解释的 trade-off 后，才允许启动 Paper 2。

Paper 2 才允许：

- 定义 joint objective；
- 优化少量结构参数；
- 研究 turbulence-only、jitter-only 与 joint optimum；
- 判断内部最优、连续适用域和联合收益。

flattened-/super-Gaussian、Gaussian–LG/annular-like 当前只是可能设计种子，不是固定方案。

任何 AI 都不得用 Paper 2 候选反向定义 Paper 1。

## 二、当前工作阶段

当前处于 **Paper 1 / Stage A：关键文献与机制地图**。

当前优先级：

1. 建立关键文献池；
2. 按抗湍流机制分类；
3. 逐篇提取场定义、参数来源、抗湍流主张、资源、turbulence model、pointing 覆盖和评价指标；
4. 做 direct-competitor 审计；
5. 文献证据饱和后，再冻结 Paper 1 的代表机制、参数和统一评价协议。

当前不授权 structured-beam coding、正式 multi-screen Monte Carlo 或 Paper 2 optimization。

## 三、Codex 触发条件

默认处于科学讨论、文献研究或最小探索模式。讨论不得在未声明的情况下转化为工程执行。

只有当项目负责人明确说出：

> 生成符合规范的Codex指令

才允许输出新的正式 Codex 执行提示词。

“继续”“推进下一步”“看看怎么实现”“可以做了”等表述均不构成触发。

仓库中的历史 `docs/CODEX_HANDOFF.md` 不等于执行授权；如果其内容与当前阶段边界冲突，以当前阶段边界为准。

生成 Codex 指令前，必须确认：

- 当前任务属于 Paper 1 还是 Paper 2；
- 当前唯一科学问题；
- 文献/变量/单位/坐标/归一化是否足够明确；
- 输入、随机状态、处理、观测和输出；
- 主要指标、比较对象和停止条件；
- 结论边界和禁止表述；
- 为什么需要 Codex，而不是继续文献核对或更小的解析判断。

上述任一项尚未成熟，应 **REVISE**。

## 四、工作模式与适度验证

### 1. 文献与科学探索模式

当前默认模式。

典型产物：

- `KEY_LITERATURE_MAP`；
- 逐篇 literature anchor；
- parameter evidence matrix；
- mechanism classification；
- direct-competitor map；
- 对科学契约的 evidence deltas。

文献调研必须区分：

- theoretical definition；
- measured / experimental value；
- cited value；
- hardware parameter；
- simulation assumption；
- plotting / stress-test parameter。

不得把论文中出现过的数字自动升级为项目参数。

### 2. 最小模型探索模式

只有 Paper 1 Stage A 冻结代表机制与评价协议后才进入。

用解析基准、最小模型和少量代表点判断：现象是否存在、趋势是否合理、模型是否可信。

默认不要求全参数扫描、CI、大型证据包、复杂 validator、广泛回归测试或高样本尾部统计。

### 3. 科学验证模式

冻结变量、指标、参数范围、随机模型、比较基线、资源账本和主要替代解释后，才进行论文相关统计验证。

Paper 1 的科学验证重点是**机制敏感性与失效规律**，不是寻找每种光束的最大性能。

### 4. 工程交付模式

只有代码需要长期复用、多人维护或正式交付时才引入完整测试、CI、稳定接口和工程化工作。

本项目当前不处于工程交付模式。

## 五、职责边界

### 项目负责人负责

- 决定 Paper 1 / Paper 2 路线；
- 批准关键文献集合、科学契约、场景参数和结论边界；
- 批准进入数值实现、正式扫描和 Paper 2；
- 判断结果是否值得成文。

### ChatGPT优先负责

- 文献搜索、关键论文筛选与逐篇科学解读；
- 抗湍流机制分类和 direct-competitor 审计；
- 参数来源等级与可继承性判断；
- 科学问题、变量、指标、资源账本和停止条件；
- 维护 `PROJECT_STATE.md`、阶段边界和科学契约；
- 审查项目是否仍在回答 Paper 1 原始问题。

### Codex在契约明确后负责

- 已批准文献获取/结构化任务；
- 已定义模型的代码实现；
- 运行脚本和结构化产物；
- 已批准范围内的有限参数扩展；
- 必要的最小数值一致性检查。

Codex不得自行：

- 选择 Paper 1 的代表机制；
- 把 Paper 1 改成 Paper 2；
- 固定缺乏文献依据的 UAV/PAT 参数；
- 扩大光束家族；
- 为正结果增加自由度；
- 改变主要评价指标或比较基线。

## 六、项目专属科学护栏

### 1. 三类横向运动必须区分

- turbulence-induced beam wander：属于 turbulence realization；
- independent residual pointing jitter：平台、云台、FSM 或 PAT 闭环后的独立机械角误差；
- static/slow boresight bias：标定、热漂移或安装误差造成的慢偏置。

若 phase screen 已保留低频 beam wander，不得再次以独立 pointing loss 重复叠加。

### 2. 抗湍流机制不得偷换成 anti-jitter

- self-healing 不自动等于抗整体横移；
- quasi-nondiffracting / long depth of focus 不自动等于 fixed-aperture lateral tolerance；
- reduced scintillation 不自动等于 higher received-power low tail；
- mode / polarization structure preservation 不自动等于通信功率更高。

Paper 1 的任务正是检验这些差别。

### 3. finite-aperture received power 是主通信链

主证据优先来自：

- finite-aperture received-power samples；
- ECDF；
- low quantile；
- 必要时明确门限下的 outage。

peak intensity、single spot image、normalized shape、scintillation 和 mode fidelity 只作辅助机制诊断。

### 4. Gaussian baseline 必须认真处理

Paper 1 至少保留：

- 原代表文献自己的 Gaussian comparison；
- 共同任务下合理优化或尺度匹配的 Gaussian baseline。

不得用固定、明显不公平的 Gaussian 放大 structured-beam 优势。

### 5. 结构机制与资源交换必须分开

报告并尽量控制：

- total power；
- transmitter / receiver aperture；
- hard truncation；
- peripheral / halo energy；
- generation efficiency / wasted orders；
- no-disturbance received power；
- long-term beam scale。

更宽光斑、更多外围能量或更大口径可以是合理 trade-off，但不能隐藏成“结构性抗抖动”。

### 6. Paper 1 不做模式动物园

最终代表机制数量应少而清楚。某个新模式只有在提供独立物理机制、文献证据充分且计算成本合理时才加入。

### 7. Paper 2 不预注册结果

即使 Paper 1 显示某个家族有优势，也不能预先声称 flattened-Gaussian、Gaussian–LG 或其他结构一定形成 Paper 2。

如果 Paper 1 的结果最终说明普通 Gaussian scale optimization 已经解释主要 trade-off，应接受 Paper 2 STOP。

## 七、重要代码与结果不得黑箱交付

进入数值阶段后，以下变化必须提供负责人可理解的解释：

- free-space propagation / turbulence phase screen / split-step；
- transmitter tilt / receiver shift / beam-wander bookkeeping；
- 任何代表性 structured-beam field model；
- finite-aperture integration 和 low-tail statistics；
- coordinate、unit、sampling、FFT、normalization、resource ledger；
- 会改变 Paper 1 / Paper 2 结论的指标、随机样本或比较协议。

每轮重要代码或数值工作按以下结构报告：

1. 当前 Paper / Stage 与主要不确定性；
2. 负责人摘要；
3. 科学定义与变量；
4. 代码与数据链；
5. 证据与结论边界；
6. CONTINUE / REVISE / STOP。

测试通过不能替代物理证据。

## 八、仓库变更与证据要求

重要科学或治理变更使用聚焦分支和 Draft PR。

纯文档变更只需文本、路径、引用和一致性检查，不要求运行传播仿真。

不得静默覆盖已经接受的历史证据。新的文献判断、科学决策和运行应单独记录。

Draft PR、未合并分支、未审查脚本和计划参数都不是已支持科学事实。

## 九、项目状态与交接协议

开始新的重要对话时依次读取：

1. `AI_RESEARCH_GOVERNANCE.md`；
2. `PROJECT_STATE.md`；
3. `docs/RESEARCH_STAGE_BOUNDARY.md`；
4. `README.md`；
5. 当前科学契约与 evidence deltas；
6. 文献路线综合和逐篇锚点；
7. 当前 PR、commit 和后续运行证据。

必须先说明当前处于 Paper 1 Stage A、Stage B 还是 Paper 2，再决定允许做什么。

当前默认：**Paper 1 Stage A / 文献机制地图**。
