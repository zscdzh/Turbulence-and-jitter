# Nelson et al. 2014：Bessel / Airy quasi-nondiffracting turbulence failure boundary

## 文献身份

- W. Nelson, J. P. Palastro, C. C. Davis, P. Sprangle
- *Propagation of Bessel and Airy beams through atmospheric turbulence*
- Journal of the Optical Society of America A 31(3), 603–609 (2014)
- DOI: `10.1364/JOSAA.31.000603`
- arXiv: `1312.0620`
- 证据角色：**Paper 1 的 turbulence-only failure-boundary anchor**。

## 核心结论

作者通过数值传播研究 Bessel 与 Airy beam 在 atmospheric turbulence 中的 quasi-nondiffracting 性质。最重要的边界结论是：

> 当 atmospheric transverse coherence length / Fried parameter 接近发射场的初始横向 aperture 尺度时，Bessel / Airy 的 quasi-nondiffracting 特性会被 turbulence-induced transverse phase distortion 明显破坏。

文献对尺度的表述分别为：

- Bessel：`r0` 接近 initial aperture **diameter**；
- Airy：`r0` 接近 initial aperture **diagonal**。

这说明“self-healing / quasi-nondiffracting”不是无条件的 turbulence immunity，而存在清楚的 turbulence-strength-to-aperture boundary。

## Bessel 结果对 Paper 1 的意义

公开图注可确认该文对 hard-apertured Bessel 做了明确的有限孔径传播，例如 15-ring Bessel、23 cm aperture radius 的例子，并比较 vacuum / turbulence、on-axis intensity、RMS radius，以及向有限 circular aperture 输送的 power。

因此这篇提供的不是 jitter 结果，而是一个很重要的 turbulence-only null expectation：

> Bessel 的结构优势应当随 `D_T/r0` 增大而衰减，并可能在 `r0 ~ D_T` 附近进入机制失效区。

Paper 1 后续如果观察到 Bessel 在 joint turbulence+jitter 下退化，必须区分：

1. turbulence 已经先破坏了 quasi-nondiffracting / self-healing structure；
2. structure 仍在，但 independent common-mode jitter 把 useful region 移出 receiver。

两类 failure 不应混为“Bessel 不抗抖动”。

## 对无量纲坐标的影响

本项目已使用

\[
\tau=D_T/r_0
\]

作为 turbulence severity 的候选无量纲量。Nelson 2014 直接支持把 `D_T/r0` 作为解释 Bessel-like turbulence failure 的核心尺度之一。

注意：文献没有证明某一个普适精确阈值 `tau=1`；“r0 approaches aperture diameter”是 regime boundary，不应被过度解释成严格相变点。

## 与 Airy 的关系

该文同样显示 Airy 的 quasi-nondiffracting behavior 也会在 turbulence 足够强时被破坏。因此 Airy 在 Paper 1 讨论层不能被描述成“自愈后始终保持结构”。

但外部审查后 Paper 1 首轮数值 scope 已收窄为 coherent deterministic single-aperture fields，并不包含 Gu–Gbur multi-beam path-diversity Airy array。因此 Nelson 的 Airy 结果只作为机制边界背景，不要求增加 Airy 数值代表。

## 对合同的直接裁决

### ACCEPT

- self-healing / quasi-nondiffracting mechanism 存在 turbulence-strength / aperture-scale failure boundary；
- `D_T/r0` 是 Bessel turbulence-failure 解释的重要无量纲坐标；
- Paper 1 必须区分“turbulence 先破坏结构”与“结构仍在但 jitter 造成 receiver displacement”。

### DO NOT INHERIT

- 不把 `r0 = D_T` 写成精确 universal threshold；
- 不从该文继承 UAV scene parameters；
- 不把 turbulence-only failure 解释成 mechanical-jitter sensitivity；
- 不因此把 Airy 加回第一轮数值集合。

## 文献链状态

**CLOSED FOR CONTRACT v0.3。**

该链已经足以约束 Paper 1 的 Bessel turbulence-only failure interpretation，不再继续横向扩展相关 Bessel/Airy 文献，除非后续数值结果与该 boundary 明显矛盾。
