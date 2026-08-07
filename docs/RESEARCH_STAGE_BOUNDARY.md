# RESEARCH_STAGE_BOUNDARY

**决策日期：2026-08-07**  
**当前状态：External Review = REVISE；Stage A broad literature search closed；Scientific Contract v0.3 candidate under short review。**

## 1. Paper 1 正式范围

Paper 1 不再泛称“所有抗湍流光束”。正式 scope 为：

> **coherent、deterministic、single-aperture transmit fields 在 direct-detection finite-aperture UAV-FSO 链路中的跨机制 turbulence–jitter sensitivity / failure map。**

研究问题：

> 已有 turbulence-resistant deterministic transmit-field mechanisms 在加入 independent post-PAT residual pointing jitter 后，哪些 turbulence-only 优势保持、压缩、反转或失效；这些变化能否在 transparent resources 与 optimized-Gaussian baseline 下形成可解释的 applicability / failure map？

## 2. Paper 1 第一轮 core set

冻结为：

- Gaussian G0/G1；
- circular-truncated zeroth-order Bessel `J0`；
- continuum radial-phase OPB；
- nested multi-Gaussian flat-top。

不进入首轮数值集合：

- Airy path-diversity array：multi-beam architecture，discussion only；
- partial coherence：source ensemble / mature joint-optimization family，discussion only；
- vector / mode diversity：超出 single-aperture direct-detection scope。

## 3. Paper 1 不做什么

- 不发明新的 joint-robust beam；
- 不为每种 structured beam 做 high-dimensional joint optimization；
- 不把 turbulence + pointing 本身作为 novelty；
- 不把 scintillation / point peak 当主通信指标；
- 不建 full UAV dynamics / PAT controller / time-domain PSD model；
- 不因负结果增加新 beam family 救论文。

## 4. Paper 1 两层公平比较

### Level A — primary

same `lambda, L, D_T, D_R, P_T`；same circular apertures；same paired turbulence/jitter realizations；aperture 后 equal-power normalization；完整 resource ledger。

### Level B — secondary diagnostic

唯一采用 no-turbulence/no-jitter receiver-plane `r80_R`-matched one-scale retuning。

`H0` 继续报告，但不是 matching constraint。

## 5. Gaussian zero hypothesis

G1 允许预注册的 `w_G + quadratic focus` 二维搜索，以 `Q5%(H)` 为唯一主目标，并保证 optimization ensemble 与 final evaluation ensemble 分离。

这用于排除“structured field 只是赢了一个没调好的 Gaussian”。

## 6. Paper 2 边界

Paper 2 才是 turbulence–jitter co-robust beam design。

只有 Paper 1 找到稳定、可解释、且经过 G1 与 `r80` control 后仍存在的 mechanism trade-off，才允许启动 Paper 2。

flattened-/super-Gaussian、Gaussian–LG/annular-like 仅是可能的 Paper-2 seeds。

## 7. 当前文献状态

Stage A 无边界扩展结束。只补的三条链已经关闭：

- Nelson 2014：Bessel/Airy turbulence failure boundary；
- Jiang 2022/2026：flat-top joint-channel direct competitors；
- Lane 1992：subharmonic / low-frequency phase-screen method anchor。

以后只有结果冲突、审稿要求或明确模型 blocker 才补定向文献。

## 8. 当前代码 gate

**NO structured-beam code before v0.3 short review。**

通过后顺序：

1. Gaussian free-space；
2. finite-aperture displacement；
3. analytic jitter；
4. Gaussian multi-screen validation；
5. Bessel literature reproduction sanity；
6. Bessel / OPB / flat-top common comparison。

## 9. Paper 1 主输出

目标是：

- turbulence-only -> joint ranking change；
- mechanism-specific jitter sensitivity；
- failure / applicability boundary；
- finite-aperture ECDF / `Q5%`；
- optimized-Gaussian paired comparison；
- resource / receiver-scale interpretation。

允许最终结论是负结果：若所有 structured-field advantages 在 G1 + `r80` control 后消失，这本身是 Paper 1 的有效机制结论。

## 10. 永久禁止的路线偷换

禁止把 Paper 1 偷换成：

- flattened-Gaussian / Gaussian–LG joint optimization；
- “找一个最强新光束”；
- “所有 anti-turbulence beams 大全”；
- 用更多模式、偏振、AI 或控制器补救不显著的主结果。
