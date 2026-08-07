# Jiang 2022 / 2026：flat-top + turbulence + pointing direct-competitor audit

## 1. 文献身份

### Jiang et al. 2022

Dagang Jiang, Xin Liu, Zhimeng Hu, Bin Zhu, Qinyong Zeng, Kaiyu Qin, *Average irradiance with boresight pointing errors for flat-topped beam under atmospheric turbulence*, Optics Communications 522, 128703 (2022), DOI `10.1016/j.optcom.2022.128703`。

### Jiang et al. 2026

Dagang Jiang, Yuhang Yang, Bei Tang, Shuhang Yuan, Yuanze Ma, *Far-field approximate expressions for average irradiance and average BER in flat-topped beam-based optical wireless communication links under pointing error and gamma-gamma turbulence*, Applied Optics 65(2), 646–654 (2026), DOI `10.1364/AO.578489`。

证据角色：**Paper 1 flat-top direct-competitor boundary**。

## 2. 2022 已经覆盖到什么程度

公开正文/索引内容足以确认：

1. 使用 flat-topped multi-Gaussian family，order `N` 进入平均辐照度表达式；
2. atmospheric turbulence 与 boresight pointing errors 同时进入模型；
3. pointing errors 明确包含 jitter 与 bias；
4. 允许 x/y 方差不等与 nonzero mean；
5. 推导 average irradiance；
6. 推导 average received power；
7. 用 thin random phase screen 验证理论结果；
8. single equivalent phase screen 采用约 `0.36 L` 的经典 weak-turbulence equivalence；
9. average received power 使用近似 square-area integration，而不是本项目计划的 realization-level circular finite-aperture power distribution。

因此以下 novelty claim 已被直接排除：

- “首次 flat-top + turbulence + pointing”；
- “首次在 flat-top 中同时考虑 jitter 与 bias”；
- “首次讨论 unequal pointing variances / nonzero boresight”；
- “首次推导 flat-top joint-channel average received power”。

## 3. 2026 又覆盖到什么程度

2026 Applied Optics 进一步给出：

- flat-topped beam far-field approximate average irradiance；
- pointing error + gamma–gamma turbulence；
- average BER approximate expression；
- far-field approximation validity/application range。

其目标是快速 analytical link design，而不是 distributed wave-optics realization study。

因此不能把“加入 BER”作为本项目创新；但该工作仍未覆盖本项目计划的跨机制 failure map。

## 4. 它们没有覆盖的本项目主链

当前可确认的差异包括：

1. **distributed wave optics**：本项目要求 low-frequency-validated multi-screen，而 2022 以 single thin phase-screen verification 为主，2026 采用 gamma–gamma / far-field analytical approach；
2. **realization-level finite-aperture low tail**：本项目以每次 realization 的 circular-aperture `P_R` 构造 ECDF、`Q5%` 与 outage，不以 average irradiance / average power 为唯一结论；
3. **optimized Gaussian zero hypothesis**：本项目要求 G1 `w_G/f_G` 预注册优化；
4. **cross-mechanism comparison**：本项目同时比较 Bessel / OPB / flat-top；
5. **resource ledger**：本项目显式记录 source aperture occupation、halo/peripheral energy、receiver `r80` 与 generation cost；
6. **mechanical-jitter failure attribution**：本项目分账 turbulence-induced beam wander、independent residual jitter 与 boresight bias；
7. **failure/applicability map**：目标不是单一 flat-top closed form，而是判断 turbulence-only robustness 在 independent jitter 后何时保持、压缩或反转。

因此 Jiang 2022/2026 构成**强 direct competitor / novelty constraint，但不是 STOP 依据**。

## 5. flat-top canonical field for Paper 1

为与这条 multi-Gaussian 文献线保持连续，同时保证 `N=1` 明确嵌套 Gaussian，Paper 1 冻结以下实现 family：

\[
U_N(r)=C_N\left[\frac{1}{N}\sum_{n=1}^{N}(-1)^{n-1}\binom{N}{n}
\exp\left(-n\frac{r^2}{w_F^2}\right)\right]\Pi(r/a_T).
\]

说明：

- `C_N` 在 common circular aperture 后重新归一到同一 `P_T`；
- `w_F` 是本项目明确规定的 common radial scale parameter，不能把不同论文中的 `w0/alpha_s` 数字未经换算直接搬入；
- `N=1` 自动退化为 Gaussian amplitude；
- `N` 改变时必须重新报告 `r50_T/r80_T/r95_T`、peripheral fraction、receiver `r80_R` 与 `H0`。

## 6. order freeze

Paper 1 不是 flat-top order optimization。为避免大范围模式扫描，项目冻结：

- `N=1`：nested Gaussian sanity；
- `N=4`：第一轮 moderate flat-top representative；
- `N=8`：仅在需要验证 order sensitivity 时作为 optional high-order stress point。

`N=4` / `N=8` 是**项目代表性采样决策，不声称是 Jiang 2022/2026 的 joint optimum**。

Level B `r80_R` matching 时固定 `N`，只能调整 `w_F`；不得同时调 `N` 与 `w_F`。

## 7. 对 Paper 1 的正确 flat-top 角色

flat-top 不再承担“尚未有人把 pointing 加进 anti-turbulence beam”的 novelty 角色。

其正确角色是：

> 一个已有明确 turbulence + pointing 前序、并且理论上可能具有 broad-capture / reduced-relative-spreading 特征的成熟 positive-control mechanism，用来检验统一 distributed-wave-optics + resource-matched + low-tail framework 是否得到与既有平均量分析一致或不同的机制边界。

## 8. 禁止表述

- flat-top 过去只研究 turbulence、没有研究 pointing；
- Jiang 2022 没有 receiver-power 分析；
- 我们首次研究 flat-top joint channel；
- `N=4` 已被文献证明 joint-optimal；
- 2022 thin-screen / 2026 gamma–gamma 结果可以直接当 distributed-wave-optics low-tail 结论。

## 9. 文献链状态

**CLOSED FOR CONTRACT v0.3。**

后续不再横向扩展 flat-top 文献，除非正式结果与 Jiang 2022/2026 的平均量趋势产生无法解释的冲突。
