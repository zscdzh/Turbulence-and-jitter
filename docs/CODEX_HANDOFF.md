# CODEX_HANDOFF

**状态：SUSPENDED / DO NOT EXECUTE AS AN IMPLEMENTATION TASK**  
**更新日期：2026-08-07**

本文件原先包含“先实现 Gaussian、flattened-Gaussian、Gaussian–LG，再进入 turbulence”的启动任务。该执行顺序已经被 2026-08-07 的路线纠正明确废止。

权威边界见：

- `PROJECT_STATE.md`
- `docs/RESEARCH_STAGE_BOUNDARY.md`
- `AI_RESEARCH_GOVERNANCE.md`
- `docs/SCIENTIFIC_CONTRACT_DRAFT.md`

## 一、当前阶段

当前处于：

> **Paper 1 / Stage A：关键文献与抗湍流机制地图**

Paper 1 的任务是研究已有 turbulence-resistant beams / mechanisms 面对 independent mechanical residual jitter 时的保持、退化、排序变化和失效边界。

Paper 1 不是联合新光束设计。

Paper 2 才允许在 Paper 1 机制 trade-off 明确后开展 low-dimensional turbulence–jitter co-design。

## 二、当前不授权的旧任务

当前不要执行：

- 建立正式 propagation / turbulence 代码框架；
- 实现 flattened-Gaussian 参数扫描；
- 实现 Gaussian–LG joint optimization；
- 预注册 Paper 2 设计候选；
- 正式 multi-phase-screen Monte Carlo；
- 为每种 structured beam 寻找 joint optimum；
- 大规模参数扫描、BER 链路或高维模式扩展。

旧版本中关于 `N=0,1,2,4,8`、`eta`、`waist_ratio`、候选 smoke 等任务均不再构成当前执行授权。

## 三、当前唯一允许的方向

当前首先需要由 ChatGPT / 项目负责人完成文献驱动的科学契约冻结：

1. 按抗湍流机制建立关键文献库；
2. 初筛约 30–40 篇直接相关文献；
3. 精读约 15–20 篇关键锚点；
4. 建立机制—场定义—参数来源—资源—turbulence model—pointing coverage 证据矩阵；
5. 完成 structured beam + turbulence + pointing 的 direct-competitor 审计；
6. 文献证据趋于饱和后，冻结 Paper 1 的 3–5 个代表机制和统一评价协议。

如果未来项目负责人明确要求 Codex 参与文献下载、结构化抽取或后续代码实现，必须重新生成一份与当时科学契约一致的新正式 Codex 指令。

## 四、Codex 触发规则仍有效

只有当项目负责人明确说出：

> 生成符合规范的Codex指令

才允许生成新的正式 Codex 执行提示词。

“继续”“推进下一步”“可以做了”等表述不构成触发。

因此，本文件当前只用于防止误执行旧任务，不是新的 Codex prompt。
