# 新 ChatGPT 对话交接词

请把以下内容作为新对话的首条消息使用。

---

这是 `zscdzh/Turbulence-and-jitter` 科研项目的延续对话。

请先通过 GitHub 完整读取当前仓库，不要只依赖本提示词或聊天记忆。读取顺序为：

1. `AI_RESEARCH_GOVERNANCE.md`；
2. `PROJECT_STATE.md`；
3. `docs/RESEARCH_STAGE_BOUNDARY.md`；
4. `README.md`；
5. `docs/SCIENTIFIC_CONTRACT_DRAFT.md`；
6. `docs/SCIENTIFIC_CONTRACT_EVIDENCE_DELTAS.md`；
7. `docs/LITERATURE_AND_ROUTE_SYNTHESIS.md`；
8. `docs/literature/` 中的逐篇关键文献锚点；
9. 当前 main、开放/已合并 PR、最近提交和后续运行证据。

读取后先做负责人层状态核验，至少说明：

- 当前处于 Paper 1 Stage A、Stage B 还是 Paper 2；
- 当前真正的科学问题和唯一主要不确定性；
- 哪些是已接受文献/方法结论，哪些只是工作假设；
- 当前代码、配置和结果链是否建立；
- 当前允许的最小下一步；
- 哪些旧交接或计划已经失效。

必须严格保持以下两篇论文边界。

## Paper 1

Paper 1 研究：文献中已有的不同 turbulence-resistant mechanisms，在加入 independent mechanical residual pointing jitter 后，哪些优势保持、退化、反转或失效；并尝试形成 mechanism sensitivity map、applicability regime 或 failure boundary。

Paper 1 是“关键文献与机制归纳 + 后续统一物理评价”，不是联合新光束设计。

当前处于 **Paper 1 / Stage A：关键文献与机制地图**。优先任务是：

- 按 self-healing、caustic、self-focusing/pin-like、flat-top、partial coherence 等机制建立关键文献池；
- 初筛约 30–40 篇，精读约 15–20 篇锚点；
- 提取发射场定义、关键参数、抗湍流机制、turbulence model、资源、Gaussian baseline、pointing coverage 和参数证据等级；
- 做 structured beam + turbulence + pointing 的 direct-competitor 审计；
- 文献证据饱和后，再冻结 Paper 1 代表机制和统一评价协议。

当前不要直接实现 flattened-Gaussian / Gaussian–LG，也不要开始正式 multi-screen Monte Carlo。

## Paper 2

Paper 2 才研究 turbulence–jitter co-robust beam design。

只有 Paper 1 发现稳定、可解释且不能由 ordinary Gaussian beam-width optimization 完全解释的 trade-off 后，才允许启动 Paper 2。

flattened-/super-Gaussian、Gaussian–LG/annular-like 目前只是可能设计种子，最终是否采用由 Paper 1 结果决定。

Badás 2024 等 jitter-only 工作用于 Paper 2 的零假设和创新边界，不能反向把 Paper 1 改写为 Gaussian–LG joint optimization。

## 共用科学护栏

- 不把“同时考虑 turbulence 与 pointing error”本身当创新；
- 区分 turbulence-induced beam wander、independent residual jitter 和 boresight bias；
- 不用 peak intensity、single spot image 或 scintillation 单指标证明通信优势；
- finite-aperture received power 是主通信链；
- Gaussian baseline 必须针对同一比较任务认真处理；
- 结构机制与更宽光斑、外围能量、大口径等资源交换必须分开；
- 不把论文中的 simulation parameter 写成 UAV/PAT 实测值；
- 不把 Draft PR、计划参数或未运行模型写成已支持结论。

没有出现治理文件规定的固定触发词“生成符合规范的Codex指令”时，不生成 Codex 执行指令。历史 `docs/CODEX_HANDOFF.md` 不构成执行授权。

---
