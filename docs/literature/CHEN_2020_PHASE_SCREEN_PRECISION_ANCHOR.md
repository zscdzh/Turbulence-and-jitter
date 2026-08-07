# Chen et al. 2020：phase-screen 低频精度与 beam-wander 验收锚点

## 1. 文献身份

- Zhibin Chen, Dongxiao Zhang, Cheng Xiao, Mengze Qin
- *Precision analysis of turbulence phase screens and their influence on the simulation of Gaussian beam propagation in turbulent atmosphere*
- Applied Optics 59(12), 3726–3735 (2020)
- DOI: `10.1364/AO.389121`
- 证据角色：**multi-phase-screen numerical-validation anchor**。

该文不是某种 structured beam 的性能论文。它直接回答本项目后续 production turbulence model 的一个核心数值问题：

> phase-screen spectrum 的低空间频率是否被正确采样，会不会系统性改变 beam wander / long-term spot，从而把 turbulence 与 mechanical jitter 的相对重要性算错？

---

## 2. split-step / multi-screen 路线本身是成熟方法

作者将 turbulent wave propagation 表述为标准 split-step：

- free-space propagation；
- stochastic phase perturbation；
- 沿 propagation axis 离散成多个 step；
- turbulence 用一系列互不相关 phase screens 表示。

比较五类 phase-screen generation approaches：

- subharmonic-complemented DFT (`DFT-SH`)；
- sparse spectrum (`SS`)；
- sparse spectrum with uniform wave vectors (`SU`)；
- randomized DFT；
- optimization-based (`OB`) method。

因此本项目不需要把“采用 multi-phase-screen split-step”包装成方法创新；真正要做的是选择和验证一个对目标统计量足够准确的方法。

---

## 3. 最关键结论：低频欠采样不会平均地影响所有 observable

论文比较：

- beam-wander variance；
- long-term beam radius；
- short-term beam radius；
- on-axis scintillation index。

核心结果非常明确：

### 对 large-scale turbulence 敏感

如果 phase screen 的 low-frequency spectrum undersampled，会系统性低估：

- **beam-wander variance**；
- **long-term beam radius**；
- focused Gaussian beam 的 on-axis scintillation。

原因是这些量显著依赖 atmospheric large-scale inhomogeneities。

### 对 large-scale turbulence 相对不敏感

同样的 low-frequency undersampling 对：

- short-term beam radius；
- collimated Gaussian 的 on-axis scintillation

影响明显小得多。

因此不能用“某一个 scintillation / spot-size 指标与理论一致”就证明 phase-screen implementation 对本项目足够准确。

---

## 4. 这对 Paper 1 尤其关键

Paper 1 明确要区分：

\[
\rho_{bw}
\]

即 turbulence-induced centroid wander，与

\[
\rho_j=L\theta_j
\]

即 independent mechanical residual jitter。

如果 low-frequency turbulence 被欠采样：

\[
\operatorname{Var}(\rho_{bw})
\]

会被系统性低估，那么后续可能得到一个完全错误的机制图：

> 误以为 mechanical jitter 更早成为主导因素，或者误以为某种“抗 beam wander” structured beam 的作用很小。

所以 low-frequency accuracy 在本项目不是软件优化问题，而是**科学结论正确性的必要条件**。

---

## 5. 当前可以冻结的不是具体算法，而是最低验收协议

这篇文献不足以单独裁决本项目必须使用 DFT-SH、SU、SS、randomized DFT 或 OB 中哪一种。

当前可以先接受的 contract delta 是：

### production phase-screen generator 必须至少验证

1. phase structure function / spatial-spectrum statistics 与目标 turbulence spectrum 一致；
2. Gaussian benchmark 的 turbulence-induced **beam-wander variance** 与可靠理论/高精度 reference 一致；
3. long-term beam radius 与理论/reference 一致；
4. short-term radius 作为补充诊断；
5. focused / collimated case 不应只选对 low-frequency 不敏感的那一种作为唯一验证；
6. low-frequency compensation / sampling method 必须明确记录，不能使用默认 FFT grid 后不说明。

### 不接受的“假验证”

以下单独通过不能证明 turbulence module 足够：

- 一张 phase-screen 图看起来像 turbulence；
- phase RMS 对；
- 高空间频率 speckle 看起来合理；
- collimated beam scintillation 大致对；
- short-term spot radius 大致对。

这些量可能在低频错误时仍看起来正常。

---

## 6. 与 Liu/Jiang single-layer benchmark 的关系

Liu/Jiang 2021 的 single-layer `0.36L` model 已经被本项目限定为 weak-turbulence cross-check。

Chen 2020 进一步说明，正式 distributed turbulence implementation 还必须处理：

- low-frequency phase accuracy；
- beam wander；
- long-term beam statistics。

因此正确的 model hierarchy 应是：

1. free-space Gaussian analytic benchmark；
2. no-turbulence mechanical-tilt benchmark；
3. weak-turbulence single-layer cross-check；
4. **low-frequency-validated multi-screen split-step production model**。

而不是从 single-screen 直接扩大 turbulence strength 当作 production model。

---

## 7. 对 structured-beam mechanism comparison 的影响

本项目不同机制可能对 large-scale turbulence 的响应不同：

- Bessel / broad angular-spectrum beam；
- OPB / autofocusing beam；
- flat-top；
- Gaussian control。

若 phase screen 对 large-scale modes 的采样不准，各光场受到的 bias 未必相同，因此 ranking 甚至可能被 numerical spectrum choice 改写。

所以后续 Paper 1 在正式跑 structured fields 前，应先在 Gaussian 上冻结 turbulence implementation；不要边跑 structured-beam ranking 边修改 phase-screen generator。

---

## 8. 还没有冻结的事项

这篇论文没有单独解决：

- 本项目最终使用 Kolmogorov 还是 von Kármán / modified von Kármán；
- `L0` / `l0` 的物理取值；
- screen number；
- screen spacing；
- nonuniform `Cn²(z)`；
- grid/window criteria；
- UAV near-ground horizontal path 的实际 turbulence range。

这些还需 Lane 1992、JOSA A 2020、nonuniform multi-screen placement、scenario literature 等继续冻结。

---

## 9. 当前裁决

**状态：READ / NUMERICAL-VALIDATION ANCHOR。**

当前正式接受的核心原则是：

> **任何用于 Paper 1 的 production turbulence model，都必须显式证明 low-frequency phase content 足以恢复 turbulence-induced beam wander 和 long-term beam statistics。**

具体 phase-screen generation algorithm 暂不冻结。