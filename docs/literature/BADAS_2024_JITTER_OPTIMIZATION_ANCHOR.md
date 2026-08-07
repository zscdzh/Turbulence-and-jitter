# Badás 2024 jitter-only 优化锚点

## 文献身份

- Badás et al.
- *On the optimum far-field irradiance distribution using Laguerre-Gaussian beams for intersatellite free-space optical communications*
- Optics Express, 2024
- DOI: `10.1364/OE.533250`
- 证据定位：**Paper 2 的 jitter-only 零假设与创新边界文献**，不是 Paper 1 的任务定义文献。

## 1. 已有工作覆盖到哪里

该文献在 pointing-jitter-only 的星间 FSO 场景中，对 Gaussian 与 Gaussian + 高阶 LG/annular-like irradiance shaping 做了较完整优化。

关键点：

- 不是拿固定 Gaussian 做陪跑；纯 Gaussian 的远场 beam width 也针对目标优化；
- Gaussian + LG 组合优化功率权重与远场尺度；
- 不同目标函数（如 ABEP 与 outage）对应的最优光斑尺度和模式权重并不相同；
- 文中采用正交偏振使不同空间模式的强度非相干相加，不能据此推断两分量经历独立 atmospheric turbulence；
- 论文场景接近 receiver aperture 相比远场 spot/jitter 很小的极限，与近地 UAV-FSO 的有限孔径比例未必相同。

## 2. 对 Paper 1 的意义

Paper 1 研究的是“已有抗湍流机制遇到 independent jitter 后会怎样”，不是重新解决 jitter-only beam shaping。

因此本篇文献对 Paper 1 只提供两项辅助约束：

1. Gaussian baseline 若用于 jitter 对照，必须允许合理 beam-width optimization；
2. “最优光束”依赖目标函数，不能把 ABEP、outage、低分位功率或平均功率混成同一个优化问题。

Paper 1 不需要为了追随本篇工作而提前实现 Gaussian–LG joint optimization。

## 3. 对 Paper 2 的意义

如果 Paper 2 最终采用 Gaussian–LG 或 annular-like 设计，则不能把以下内容作为主要创新：

- jitter-only 下调 mode weight；
- jitter-only 下调远场 beam width；
- 仅证明 annular irradiance 对 pointing error 有优势。

Paper 2 真正需要回答的是：

> Paper 1 揭示的 turbulence mechanism / jitter-sensitivity trade-off 能否导出新的低维联合设计原则；加入 distributed atmospheric turbulence 后，已有 jitter-only optimum 如何迁移、退化或被新的 joint optimum 取代？

## 4. 当前项目裁决

- Gaussian–LG 保留为 Paper 2 的**可能设计种子**，不冻结为必选路线；
- 其是否进入 Paper 2，应由 Paper 1 机制结果决定；
- 不应因为这篇文献的存在，把 Paper 1 改写成 turbulence-only / jitter-only / joint optimum 的多参数联合优化论文；
- 文中报告的具体星间链路收益、口径和 jitter 参数不得直接继承为 UAV-FSO 场景结论。
