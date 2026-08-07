# Lane–Glindemann–Dainty 1992：subharmonic / low-frequency phase-screen anchor

## 文献身份

- R. G. Lane, A. Glindemann, J. C. Dainty
- *Simulation of a Kolmogorov phase screen*
- Waves in Random Media 2(3), 209–224 (1992)
- DOI: `10.1088/0959-7174/2/3/003`
- 证据角色：**production turbulence module 的 classical low-frequency / subharmonic method anchor**。

## 1. 为什么普通 FFT phase screen 会缺关键物理

有限离散网格的 Fourier synthesis 对低于 fundamental grid frequency 的 Kolmogorov components 采样不足。对于本项目，这不是只影响“phase screen 看起来像不像”，而会直接影响：

- large-scale phase tilt；
- speckle / spot linear shift；
- beam wander；
- long-term centroid statistics。

Lane et al. 的第一种方法正是通过引入 **subharmonics** 补充低空间频率，从而更准确重建 Kolmogorov spectrum 的低频部分。

## 2. 文献提供的验证逻辑

该文不只提出 subharmonics，还用 phase structure function 检查生成结果是否逼近理想 Kolmogorov 统计。

公开全文索引可确认：

- 增加 subharmonic sets 后 simulated phase structure function 逐渐逼近 ideal curve；
- 文中展示了 1、3、5 组 subharmonics 的比较，5 组在其示例中已经非常接近理想 structure function；
- low-frequency spectral leakage / subharmonic treatment 使线性 speckle shift 能按 Kolmogorov spectrum 表示；
- inner / outer scale 可在模拟中单独设置。

这里的“5 sets”只能作为该论文示例，不是本项目必须固定的 universal number。

## 3. 与 Chen 2020 的互补关系

Lane 1992 回答：

> **如何补低频，以及 phase statistics 应如何验证。**

Chen et al. 2020 回答：

> **如果低频处理不准，beam-wander variance、long-term radius 等 propagation observables 会怎样被系统性低估。**

两篇共同形成 production turbulence gate：

\[
\text{screen-level PSD / }D_\phi(\rho)
\rightarrow
\text{propagation-level beam wander / long-term radius}.
\]

不能只通过其中一层。

## 4. v0.3 numerical validation requirement

任何正式 phase-screen generator 必须至少通过：

### A. screen statistics

- target PSD / generated PSD 对账；
- phase structure function `D_phi(rho)` 对账；
- low-frequency compensation on/off 的差异记录。

### B. propagation observables

对 Gaussian benchmark：

- beam-wander variance；
- long-term beam radius；
- scintillation / short-term radius 作为辅助。

### C. numerical convergence

- grid/window；
- propagation sampling；
- screen number；
- subharmonic depth / equivalent low-frequency treatment；
- 最大 transmitter tilt 下 wrap-around / aliasing。

## 5. 不冻结具体算法品牌

Lane 1992 支持 subharmonic method 的经典合理性，但 v0.3 不要求 production implementation 必须使用原始 Lane algorithm。

允许：

- DFT + subharmonics；
- randomized / sparse spectral alternatives；
- 其他能同时通过 screen-level 与 propagation-level validation 的方法。

科学契约冻结的是**低频物理必须正确**，不是冻结某个代码实现。

## 6. horizontal-link screen placement

本项目 primary scene 为近地 constant/approximately-constant `Cn2` horizontal link 时，可从 equal-spacing screens 开始。

screen number 不预先写成“10 张”或“20 张”；通过 observable convergence 决定。

高度依赖 `Cn2(z)` 的 non-uniform screen placement 保留为 secondary case，参考 Chahine et al. 2020。

## 7. 对合同的裁决

### ACCEPT

- Lane 1992 正式升级为低频/subharmonic classical anchor；
- PSD / structure-function validation 成为显式验收项；
- low-frequency treatment 必须最终通过 beam-wander / long-term-radius propagation observables；
- subharmonic sets 数量由收敛决定，不机械继承文献示例。

### PROHIBIT

- 普通 FFT screen 只要 phase RMS 对就认为 production-ready；
- 用“屏看起来合理”代替 structure function / PSD；
- 把 multi-screen 或 subharmonic 本身包装成论文创新；
- 未检查 maximum-tilt aliasing 就进入 joint structured-beam production run。

## 8. 文献链状态

**CLOSED FOR CONTRACT v0.3。**

Lane 1992 + Chen 2020 + Chahine 2020 已足以定义第一版 low-frequency / longitudinal segmentation validation philosophy，不再继续无边界扩展 phase-screen algorithm 文献。
