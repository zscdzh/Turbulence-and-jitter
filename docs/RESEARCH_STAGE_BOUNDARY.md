# RESEARCH_STAGE_BOUNDARY

**决策日期：** 2026-08-07  
**状态：** 项目负责人已确认的路线纠正；用于约束后续文献调研、科学契约、ChatGPT/Codex 任务和论文表述。

## 1. 为什么需要这份边界

前序文档把两个不同层级的问题部分混在了一起：

- 第一篇论文原本要回答的是：已有多种“抗湍流”新光束，它们的设计与验证大多围绕 atmospheric turbulence；当 UAV-FSO 中再加入独立机械 residual jitter 后，这些抗湍流机制是否仍然有效、哪些机制更敏感、哪些优势会消失或反转？
- 第二篇论文才是：在第一篇获得机制认识后，能否据此设计一个同时面向 turbulence 与 jitter 的低维联合鲁棒发射光场？

因此，第一篇不是“联合光束设计”，也不是“寻找 joint optimum”。第一篇首先是**机制文献归纳 + 统一物理评价**；第二篇才进入 co-design。

## 2. Paper 1：已有抗湍流机制遇到独立抖动后会怎样

### 2.1 核心科学问题

> 文献中声称具有 turbulence robustness 的不同发射光场，其抗湍流机制面对独立机械 residual pointing jitter 时，哪些保持有效、哪些明显退化、哪些发生排序反转？这种差异能否用少量可解释的结构量和有限孔径捕获特性总结成适用域或失效边界？

Paper 1 不要求发明新的联合鲁棒光束。

### 2.2 第一阶段 A：文献与机制地图

当前首要任务是建立关键文献库，而不是立即写传播代码。

按“抗湍流机制”组织文献，而不是按模式名称堆积。初始需要重点覆盖但尚未冻结的机制包括：

- self-healing / angular-spectrum redundancy，例如 Bessel / Bessel–Gaussian；
- caustic / self-accelerating propagation，例如 Airy 类；
- self-focusing / pin-like / longitudinal energy concentration 类；
- flat-top / flattened / super-Gaussian 类；
- partial coherence / statistical beam shaping；
- 只有在提供独立机制且数值成本合理时，才考虑 vector / mode-diversity 类作为补充。

每一类优先寻找：

1. 一篇定义或奠定机制的文献；
2. 一篇较强的 turbulence-performance 论文；
3. 必要时一篇实验或外场论文。

从文献中提取：发射场公式、关键参数、作者声称的抗湍流机制、湍流模型、评价指标、发射/接收口径、Gaussian 比较方式、额外资源、是否包含 beam wander、是否包含 independent pointing jitter，以及对整体 lateral displacement 的潜在敏感性。

在文献机制地图达到足够覆盖前，不冻结 Paper 1 的最终光束集合。

### 2.3 第一阶段 B：统一评价

从文献地图中选择少量、机制真正不同的代表光束进入共同评价。目标不是建立“模式动物园”。

每个代表机制至少比较：

- turbulence only；
- jitter only；
- turbulence + independent jitter。

第一层比较优先保留文献原方案或有明确文献依据的代表参数，用来回答“原有抗湍流设计在加入 jitter 后还剩多少优势”。

第二层如有必要，只允许有限、透明的尺度 retuning 或与 optimized Gaussian 的对照，用来区分：

- 真正的结构机制；
- 单纯把光斑调宽、增加外围能量或使用更大资源带来的收益。

Paper 1 **不以**为每种 structured beam 寻找完整 joint optimum 为任务，也不应为了让某一光束获胜而增加多个自由参数。

### 2.4 Paper 1 的主输出

主输出应是机制层规律，而不是单一排行榜：

- turbulence-only 优势加入 jitter 后的保持、压缩、反转或失效；
- 各机制对 independent lateral displacement 的敏感性；
- finite-aperture received-power ECDF、低分位功率和必要的 outage；
- 资源匹配后仍保留的结构收益；
- 可解释的 sensitivity map、applicability regime 或 failure boundary；
- 能否由 capture function、中心梯度/曲率、长期光斑尺度、外围能量比例等少量描述量解释。

Paper 1 的潜在论文主张不是“首次联合 turbulence 与 pointing error”，而是对**既有抗湍流机制在独立机械抖动下的系统性脆弱性、保持区与失效区**进行统一、机制化分析。

## 3. Paper 2：turbulence–jitter 低维联合鲁棒光束设计

### 3.1 启动条件

Paper 2 只有在 Paper 1 给出稳定、可解释的 trade-off 或失效机制后才启动。

需要至少满足：

- Paper 1 发现可重复的机制矛盾，而不是少数参数点偶然差异；
- 该矛盾不能被普通 Gaussian beam-width optimization 完全解释；
- 能提出清楚的设计原则，例如“中心捕获效率—横向覆盖—湍流重分配”之间的低维权衡；
- 有合理的资源和实现边界。

### 3.2 设计任务

Paper 2 才允许：

- 定义明确的 joint objective；
- 优化少量结构参数；
- 比较 turbulence-only、jitter-only 与 joint optimum；
- 寻找内部最优、连续适用域和可解释的联合收益。

flattened-/super-Gaussian、Gaussian–LG/annular-like 目前只是**可能的设计种子**，不是已经冻结的 Paper 2 候选，更不是 Paper 1 必须实现的对象。最终设计应由 Paper 1 的机制结果决定。

Badás 2024 等 jitter-only 优化工作主要约束 Paper 2 的零假设和创新边界：第二篇不能重复已有的 jitter-only beam shaping。

## 4. 两篇论文之间的关系

正确逻辑链是：

\[
\text{existing turbulence-resistant mechanisms}
\rightarrow
\text{jitter sensitivity / failure analysis}
\rightarrow
\text{mechanism trade-off}
\rightarrow
\text{co-robust design principle}
\rightarrow
\text{low-dimensional Paper-2 design}.
\]

错误逻辑链是：

\[
\text{先选 flattened-Gaussian / Gaussian-LG}
\rightarrow
\text{直接做 joint optimization}
\rightarrow
\text{再把结果解释成 Paper 1}.
\]

后者会把两篇论文混为一篇，并使第一篇失去原始科学问题。

## 5. 当前立即任务

当前处于 **Paper 1 / Stage A：文献与机制地图**。

允许的下一步：

1. 初筛约 30–40 篇直接相关文献；
2. 选出约 15–20 篇关键锚点进行逐篇精读；
3. 建立“机制—代表光束—原始抗湍流主张—参数—资源—pointing 覆盖—可继承性”证据矩阵；
4. 完成 direct-competitor 检索，确认 structured beam + turbulence + pointing 已有工作覆盖到哪里；
5. 文献证据趋于饱和后，再冻结 Paper 1 的 3–5 个代表机制和统一评价协议。

当前**不允许因为已有旧交接文档而直接开始** flattened-Gaussian / Gaussian–LG 实现、联合优化或大规模多相位屏 Monte Carlo。

## 6. 当前决策

- Paper 1 机制文献与统一评价：**GO**；
- Paper 2 联合鲁棒新光束：**CONDITIONAL GO**；
- 当前执行阶段：**文献驱动的 Paper 1 科学契约冻结前阶段**；
- 当前代码执行：**NOT AUTHORIZED / 尚未到实现阶段**。
