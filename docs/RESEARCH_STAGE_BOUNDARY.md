# RESEARCH_STAGE_BOUNDARY

**决策日期：2026-08-07**  
**当前状态：Paper 1 / CONTRACT FREEZE GATE**  
**最新短审：REVISE — KEEP CODE GATE CLOSED**

本文件是 Paper 1 / Paper 2 路线边界。它约束文献、ChatGPT/Codex 任务、科学合同和论文表述。

## 1. Paper 1 与 Paper 2 不得混合

正确逻辑：

\[
\text{existing turbulence-resistant mechanisms}
\rightarrow
\text{jitter sensitivity / failure analysis}
\rightarrow
\text{mechanism trade-off}
\rightarrow
\text{Paper-2 co-robust design principle}.
\]

错误逻辑：

\[
\text{先选 flattened-Gaussian / Gaussian-LG}
\rightarrow
\text{joint optimization}
\rightarrow
\text{再解释成 Paper 1}.
\]

## 2. Paper 1 正式 scope

Paper 1 限定为：

> **coherent、deterministic、single-aperture scalar transmit fields 在 direct-detection finite-aperture UAV-FSO 链路中的跨机制 turbulence–jitter sensitivity / failure map。**

首轮 core fields：

- Gaussian G0 / G1；
- circular-truncated `J0` Bessel；
- continuum radial-phase OPB；
- nested multi-Gaussian flat-top。

不进入首轮 numerical set：

- Airy path diversity；
- partial coherence；
- vector / mode diversity。

这些机制可以保留在文献讨论，但不再用于扩张首轮代码。

## 3. Paper 1 要回答什么

至少比较：

1. turbulence only；
2. jitter only；
3. turbulence + independent post-PAT residual jitter。

主结果不是 beam-name leaderboard，而是：

- turbulence-only 优势加入 jitter 后的保持、压缩、反转与失效；
- finite-aperture `H=P_R/P_T` 的 ECDF / `Q5%` / paired differences；
- optimized Gaussian 后仍剩多少结构收益；
- receiver `r80` scale control 后差异是否仍存在；
- resource ledger 能否解释差异；
- applicability / failure map。

## 4. Paper 1 不做什么

不允许：

- 为每个 structured field 求 full joint optimum；
- 为得到积极结果增加高维自由度；
- full UAV 6-DOF / PAT/FSM time-domain simulation；
- jitter PSD/controller dynamics 作为首轮主模型；
- AO、SMF coupling、mode decomposition、coherent receiver；
- high-dimensional inverse design / neural network。

## 5. Paper 2 启动条件

Paper 2 只有在 Paper 1 发现：

- 稳定、跨连续区域的 mechanism trade-off；
- 不能被 optimized Gaussian 完全解释；
- 可转化为少参数设计原则；
- 资源代价适合目标 UAV-FSO 场景；

才允许启动 turbulence–jitter co-design。

flattened-/super-Gaussian、Gaussian–LG/annular-like 目前只属于可能的 Paper-2 design seeds。

## 6. 文献阶段状态

Stage-A broad literature search：**CLOSED**。

三条外审指定补链已关闭：

- Nelson 2014；
- Jiang 2022/2026；
- Lane 1992。

后续只在结果冲突或审稿需要时定向补文献，不因为新 beam name 重新广撒网。

## 7. 当前 contract gate

当前 authoritative candidate：`docs/SCIENTIFIC_CONTRACT_DRAFT.md` v0.3.1。

v0.3 短审暴露三项 blocker：

1. OPB finite-aperture stationary-radius feasibility；
2. G1 5% tail optimization sample stability；
3. turbulence exact PSD normalization + absolute Gaussian references + split grid/window convergence。

这些已在 v0.3.1 candidate 中修订，但仍等待最终短复核。

## 8. code authorization

当前：

> **NO SCIENTIFIC CODE AUTHORIZED YET.**

若 v0.3.1 短审 PASS，只授权 Gaussian-only implementation：

1. free-space；
2. finite-aperture displacement；
3. analytic jitter；
4. Gaussian phase-screen / multi-screen V0–V12 validation。

Bessel / OPB / flat-top 只有在 Gaussian chain 全部通过后才授权。

## 9. 禁止表述

禁止：

- “首次联合 turbulence 与 pointing”；
- “首次 structured beam + joint channel”；
- “self-healing 等于自动回正”；
- “27–42 urad 是典型 UAV one-way residual”；
- “flat-top / OPB 已证明 joint-optimal”；
- “multi-screen / subharmonic 本身是创新”；
- “低 scintillation 等于高 `Q5%`”；
- “representative field parameter 是文献证明 optimum”。
