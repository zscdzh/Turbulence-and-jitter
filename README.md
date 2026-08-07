# Turbulence-and-jitter

面向无人机自由空间光通信（UAV-FSO）的抗湍流光束抖动敏感性与后续湍流—抖动联合鲁棒设计研究。

## 研究动机

近地面无人机动中通链路同时受到两类核心扰动：

1. 大气湍流引起的波前畸变、闪烁、光束扩展、散斑和 turbulence-induced beam wander；
2. 无人机平台振动、云台误差及 PAT/FSM 闭环残差引起的独立机械 pointing jitter 和慢 boresight bias。

现有文献已经提出多类所谓“抗湍流”发射光场，包括 self-healing、caustic/self-accelerating、self-focusing/pin-like、flat-top、partially coherent/statistically shaped 等机制。这些方案大多围绕 atmospheric turbulence 本身设计和评价，并不等价于已经针对独立机械 jitter 优化。

因此，本项目首先问的不是“怎样直接设计一个 joint optimum beam”，而是：

> 现有不同抗湍流机制在加入 UAV/PAT residual jitter 后，哪些优势能够保持，哪些会明显退化或发生排序反转？这种差异能否形成可解释的 sensitivity map、applicability regime 或 failure boundary？

只有在这个问题得到稳定机制认识后，才进入第二篇论文的 turbulence–jitter co-robust beam design。

详细阶段边界见 `docs/RESEARCH_STAGE_BOUNDARY.md`。

## 当前研究结构

### Paper 1 / Stage A：关键文献与机制地图

**当前正在进行。**

目标不是马上实现候选光束，而是从关键文献中提取：

- 发射场定义与关键参数；
- 作者声称的抗湍流机制；
- turbulence model 与评价指标；
- 发射/接收口径和资源假设；
- 与 Gaussian 的比较方式；
- 是否包含 beam wander 或 independent pointing jitter；
- 对整体 lateral displacement 的潜在敏感性。

文献按机制组织，而不是按模式名称堆积。当前计划先初筛约 30–40 篇，精读约 15–20 篇关键锚点，达到证据饱和后再冻结 Paper 1 的代表机制集合。当前入口见 `docs/KEY_LITERATURE_MAP.md`。

### Paper 1 / Stage B：代表性抗湍流机制统一评价

从文献地图中选择少量、机制真正不同的代表光束，在共同的 turbulence–jitter–finite-aperture 框架下比较：

- turbulence only；
- jitter only；
- turbulence + independent jitter。

第一层优先保持文献原方案或明确有依据的代表参数，回答“原有抗湍流设计在加入 jitter 后还剩多少优势”。第二层仅在必要时做透明的尺度 retuning 与 optimized Gaussian 对照，用来区分结构机制和资源交换。

Paper 1 不以为每种 structured beam 寻找完整 joint optimum 为任务，也不允许为了让某一光束获胜而不断增加自由参数。

主输出应是：

- 抗湍流优势的保持、压缩、反转或失效；
- 不同机制对 independent jitter 的敏感性；
- finite-aperture received-power ECDF、低分位功率和必要的 outage；
- 资源匹配后仍保留的结构收益；
- 机制化适用域或失效边界。

### Paper 2：低维 turbulence–jitter 联合鲁棒光束设计

**状态：CONDITIONAL GO。**

只有 Paper 1 得到稳定、可解释且不能由普通 Gaussian beam-width optimization 完全解释的 trade-off 后才推进。

flattened-/super-Gaussian、Gaussian–LG/annular-like 目前只是可能的设计种子，不是已经冻结的候选。最终设计应由 Paper 1 的机制结果决定。

Paper 2 才允许定义 joint objective、优化少量结构参数，并研究 turbulence-only、jitter-only 与 joint optimum 的迁移与内部最优。

## 当前裁决

- Paper 1 文献机制地图：**GO / 当前任务**；
- Paper 1 统一评价：**GO，但等待文献集合与评价协议冻结**；
- Paper 2 联合新光场设计：**CONDITIONAL GO**；
- 当前代码执行：**尚未授权**；
- 高维像素级逆设计、神经网络、完整无人机动力学和复杂通信协议：当前 **NO-GO / 不在范围内**。

## 仓库原则

- 这是科研项目，不以 CI、工程化完备性或大规模软件审计作为验收目标；
- 每轮工作必须先说明科学问题、变量、测试内容、关键结果和结论边界；
- 不把“同时考虑 turbulence 与 pointing error”本身当作创新；
- 区分 turbulence-induced beam wander、independent mechanical jitter 和 boresight bias；
- 不以轴上峰值、单幅光斑或 scintillation 单指标证明通信优势；
- Gaussian 基线必须针对同一比较任务认真处理；
- 新方案不要求普适最优，但资源代价、适用场景和比较边界必须透明；
- Paper 1 优先研究已有抗湍流机制的 jitter sensitivity；Paper 2 才允许联合设计。

## 关键文档

- `PROJECT_STATE.md`：当前权威项目状态；
- `AI_RESEARCH_GOVERNANCE.md`：ChatGPT/Codex 协作与结果说明要求；
- `docs/RESEARCH_STAGE_BOUNDARY.md`：Paper 1 与 Paper 2 的权威边界；
- `docs/KEY_LITERATURE_MAP.md`：当前 Paper 1 Stage A 文献机制地图；
- `docs/SCIENTIFIC_CONTRACT_DRAFT.md`：当前 Draft 科学契约；
- `docs/SCIENTIFIC_CONTRACT_EVIDENCE_DELTAS.md`：逐篇文献接受后的证据增量；
- `docs/LITERATURE_AND_ROUTE_SYNTHESIS.md`：文献结构与路线综合；
- `docs/literature/`：逐篇关键文献锚点；
- `docs/CHATGPT_HANDOFF.md`：新 ChatGPT 对话交接；
- `docs/CODEX_HANDOFF.md`：当前 Codex 状态说明；旧实现任务已暂停。
