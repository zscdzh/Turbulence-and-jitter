# PAPER1_PARAMETER_MAPPING_MATRIX

**状态：Stage A -> Stage B 参数映射草案；不是数值参数冻结。**  
**日期：2026-08-07**

本文件回答一个具体问题：

> 已精读文献中的光束定义和参数，如何转换到同一个 Paper 1 物理资源与评价框架，而不把论文各自的波长、口径、功率、传播距离和数学归一化误当成结构性收益？

本文件的目标不是现在决定最终数值，而是把“文献原参数 -> 无量纲机制参数 -> 统一物理资源 -> Paper 1 可执行参数”的转换规则先写清楚。

---

## 1. 总体映射原则

### 1.1 不直接拼接不同论文的有量纲参数

例如：

- Eyyuboğlu 2013 的 `a_B = 1–5 cm^-1`；
- Zhang 2019 的 `lambda = 532 nm`、约 5 cm phase mask；
- Gu & Gbur 2010 的 `x0 = 12 mm`、`d = 66 mm`；
- flat-top 文献中的 `alpha_s = 3 cm`；

都只能先用于复现原文或构造无量纲结构参数，不能直接混成同一个 1550-nm UAV 场景。

### 1.2 common-evaluation 首先统一真正的物理资源

Paper 1 的共同资源层至少包括：

- wavelength `lambda`；
- propagation distance `L`；
- circular transmitter clear-aperture radius `a_T`；
- circular receiver-aperture radius `a_R`；
- post-aperture transmitted optical power `P_T`；
- turbulence realization；
- independent mechanical jitter realization；
- receiver coordinate / nominal optical axis。

所有 coherent source fields 在裁剪到相同 transmitter aperture 后重新归一化：

\[
\iint_{r\le a_T}|U_0|^2\,dA=P_T.
\]

因此数学场振幅常数不属于可比较收益。

### 1.3 “相同总功率 + 相同硬口径”仍然不够

不同 structured fields 可能通过以下资源获得表面优势：

- 更大的 source-plane occupation；
- 更多外围 / halo energy；
- 更大的 transverse spatial frequency / angular spectrum；
- 更强的 focusing phase；
- 多 beamlet source footprint；
- 更低的 generation efficiency。

因此每个代表场还必须报告 resource ledger：

- source encircled-energy radii `r50_T, r80_T, r95_T`；
- peripheral power fraction；
- transverse-wavevector / spatial-frequency scale；
- 无湍流 receiver-plane `r50_R, r80_R`；
- nominal finite-aperture capture `H0=P_R/P_T`；
- 如文献有依据，generation efficiency / mode-conversion loss。

这些量先**报告而不强行全部匹配**。否则会把真正结构机制也归一掉。

---

## 2. 两层共同比较合同

为了区分“系统绝对性能”与“形状机制本身”，Paper 1 建议保留两层比较，而不是为所有光束做复杂联合优化。

### Level A — common-resource / literature-mechanism comparison

固定：

- `lambda, L, a_T, a_R, P_T`；
- 同一 turbulence / jitter realizations；
- 每类 structured field 只采用一个或极少数文献支持的代表结构参数。

每个场只允许进行必要的**相似缩放**，使其落入统一 Tx aperture，而不针对 joint channel 搜索内部最优。

该层回答：

> 一个已有 anti-turbulence mechanism 放进相同 UAV-FSO 资源后，原有优势面对 independent jitter 是否保持？

### Level B — one-scale diagnostic retuning

仅在 Level A 出现明显差异时，对每个 structured family 最多开放**一个尺度自由度**，用于排除“只是宽一点 / 聚焦一点”的解释。

优先采用以下一种诊断匹配方式（最终只选一种）：

- 匹配无扰动 receiver-plane `H0`；或
- 匹配无扰动 receiver-plane `r50_R` / characteristic scale。

然后重新评价 turbulence-only / jitter-only / joint。

Paper 1 不允许在此阶段对 Bessel ring spacing、OPB phase strength、flat-top order 等做全维 joint optimization。

---

## 3. Gaussian baseline 的特殊角色

Gaussian 是 Paper 1 的零假设，不是普通候选之一。

### G0 — common-resource Gaussian

建议场：

\[
U_G(r)=C_G\exp(-r^2/w_G^2)
\exp\left[-i\frac{k r^2}{2f_G}\right]\Pi(r/a_T).
\]

其中：

- `w_G/a_T`：source occupation；
- `f_G`：允许合理 quadratic phase / focusing；
- 裁剪后重新归一到同一 `P_T`。

### G1 — optimized-Gaussian envelope

在正式 Paper 1 比较中，Gaussian 可以比 structured fields 多获得一个“baseline fairness privilege”：

> 对少量 `w_G, f_G` 做低维搜索，形成同一任务下的 Gaussian performance envelope。

原因是 Paper 1 必须排除“新光束只是比一个没有调好的 Gaussian 更宽/更聚焦”。

但该搜索不应演变为大规模优化；只需足以建立简单 Gaussian 能做到哪里。

### reference beam scale

当前建议将无扰动 G0 的 receiver-plane characteristic radius 作为共同归一化尺度：

\[
w_{ref}=W_{G0}(L)
\]

或等价的固定 encircled-energy radius。最终 radius convention 在实现前冻结。

随后：

\[
j=\frac{L\sigma_\theta}{w_{ref}},
\qquad
\alpha_R=\frac{a_R}{w_{ref}}.
\]

这样 jitter / receiver size 不依赖某个 structured field 自己的 spot size。

---

## 4. Bessel-like angular-spectrum redundancy / self-healing

### 4.1 文献原型

Eyyuboğlu et al. 2013：

\[
U_B(r,\phi)=J_n(a_B r)e^{in\phi},
\]

原文采用 square hard truncation。

Paper 1 direct-detection 第一代表优先 `n=0`，避免把 OAM/order 问题引入主线。

### 4.2 原文参数 -> 无量纲结构参数

对 common circular aperture，最自然的结构参数不是直接搬 `a_B [cm^-1]`，而是：

\[
\chi_B=k_r a_T,
\]

其中 `k_r` 对应文献中的 `a_B`。

Eyyuboğlu 2013 的两组原始扫描大致映射为：

- `S=10 cm`, `a_B=1–5 cm^-1`，若取等效半径 `a_T=S/2`，则 `chi_B≈5–25`；
- `S=40 cm`, `a_B=0.2–1 cm^-1`，则 `chi_B≈4–20`。

两组无量纲范围相互重叠，说明 `chi_B ~ O(5–20)` 可作为后续代表结构区间的**文献来源范围**，但当前不冻结具体值。

### 4.3 common-resource 重建

候选共同评价场：

\[
U_B(r)=C_B J_0\left(\chi_B\frac{r}{a_T}\right)\Pi(r/a_T).
\]

这保留了：

- radial angular-spectrum redundancy；
- finite-energy truncation；
- clear-aperture resource；

同时去掉高阶/OAM自由度。

### 4.4 当前 blocker

需要在开代码前做一个最小裁决：

- 采用上述 **circular-truncated J0** 作为 physics representative；还是
- 采用 Bessel-Gaussian 以更接近常见实验生成。

Eyyuboğlu 2013 的 turbulence claim 本身来自 square truncation，因此如果改用 circular/BG，必须先做一个文献复现 sanity case，确认没有把机制换掉。

**当前 readiness：YELLOW-GREEN。数学场可写，最终 truncation form 尚需一次小裁决。**

---

## 5. radial-phase autofocusing / inward-energy redistribution — OPB

### 5.1 文献原型

Zhang et al. 2019 的 continuum radial model：

\[
\psi_0(r)=A(r)
\exp\left[-i\frac{4}{3}k\sqrt{\beta}\,r^{3/2}\right],
\]

其中 `beta` 具有 `1/length` 量纲。

其 stationary-phase 结果给出 Bessel-like pin width 近似：

\[
W(z)\approx\frac{1}{4k\beta z}.
\]

### 5.2 最有用的相似缩放方式

OPB 不应直接搬 532-nm mask 的毫米/厘米参数到 1550 nm。

推荐用两种等价的无量纲表述之一：

#### aperture-edge phase strength

\[
\chi_{OPB}
=\frac{4}{3}k\sqrt{\beta}\,a_T^{3/2}.
\]

#### target pin-scale ratio

给定目标传播距离 `L`：

\[
\omega_{OPB}=\frac{W(L)}{a_T}
\]

并由

\[
\beta\approx\frac{1}{4kLW(L)}
\]

反求 `beta`。

后者更适合 Paper 1，因为它把 phase parameter 直接连接到“接收面会形成多窄的 pin”。

### 5.3 common-resource 重建

候选：

\[
U_{OPB}(r)=C_{OPB}A(r)
\exp\left[-i\frac{4}{3}k\sqrt{\beta}r^{3/2}\right]
\Pi(r/a_T).
\]

所有比较先固定 `a_T, P_T`。

必须记录：

- `A(r)` source amplitude envelope；
- `chi_OPB` 或 `W(L)/a_T`；
- receiver-plane pin width；
- peripheral-energy reservoir；
- transverse-wavevector scale。

### 5.4 当前 blocker

原论文正文给出了 continuum phase 形式和 `W(z)` 解析关系，但实际 photoetched mask / input amplitude 的完整参数主要在 supplementary material。

正式实现前仍需：

1. 冻结一个明确 `A(r)`；
2. 确认是否需要 faithful mask discretization，还是 continuum phase 足以代表机制；
3. 选择一个 literature-supported `chi_OPB` / target pin scale，而不是把目标调到最有利于我们结果。

当前倾向：**先用 continuum radial phase，不实现 32 个 phase filaments 和真实刻蚀台阶。** 真实 mask 只进入 generation-resource discussion。

**当前 readiness：YELLOW。机制公式已足够，但还差 amplitude / beta representative freeze。**

---

## 6. flat-top / broad-capture / reduced-relative-spreading

### 6.1 文献原型

Eyyuboğlu et al. 2006 / Alavinejad et al. 2008 使用 nested flat-topped family：

- `N=1` 为 Gaussian；
- `N>1` 增加 flatness；
- source size、source power 和 `M^2` 随 `N` 改变。

常见等价表达可通过 multi-Gaussian / flattened-Gaussian 形式实现，但 Paper 1 必须以原文定义完成一次一致性核验后才编码。

### 6.2 common-resource 参数

核心参数：

\[
N=\text{flatness order},
\qquad
\gamma_F=\frac{w_F}{a_T}
\]

或使用原文 `alpha_s/a_T` 的无量纲版本。

所有 `N` 必须在相同 circular aperture 后重新归一到同一 `P_T`，不能沿用原文 fixed-amplitude 导致的 order-dependent source power。

### 6.3 第一版不需要 order sweep 很大

Paper 1 的问题不是找最优 `N`。建议第一轮只保留：

- `N=1`：nested Gaussian sanity check；
- 一个 moderate flatness representative；
- 必要时一个 higher-order stress representative。

具体 `N` 值由 Jiang 2022/2026 + 2006/2008 文献参数对账后冻结。

### 6.4 必须增加的资源诊断

对每个 `N` 记录：

- actual `r50_T/r80_T/r95_T`；
- source second moment；
- peripheral fraction；
- no-turbulence `H0`；
- receiver-plane flatness / `r50_R`；
- 若可稳定计算，angular-spectrum second moment / `M^2` proxy。

这样才能判断 joint benefit 是 flat capture，还是 simply larger source / broader footprint。

**当前 readiness：YELLOW-GREEN。文献 family 很成熟；主要缺 equal-resource order / scale freeze。**

---

## 7. Airy path diversity

### 7.1 文献原型

Gu & Gbur 2010：finite-energy Airy beamlets，主例：

- `x0=y0=12 mm`；
- truncation `a=0.1`；
- four beamlets；
- source displacement `d=66 mm`；
- target recombination around `L=3 km`。

### 7.2 为什么不直接塞进同一排行榜

其 mechanism 是：

> separated source regions -> weakly correlated turbulence paths -> designed receiver recombination。

因此它使用了额外 source footprint / multi-beam architecture，并且强依赖 target range。

若与单一 Bessel / OPB / flat-top 直接排行，必须额外匹配：

- total aperture footprint；
- beamlet total power；
- beamlet separation；
- target-range tuning；
- number of independently sampled paths。

### 7.3 当前角色

保留为：

- mechanism anchor；
- optional architecture-level stress/control；
- 不默认进入第一轮 monolithic common-evaluation core set。

若以后纳入，优先无量纲化：

\[
\chi_A=x_0/a_T,
\qquad
\delta_A=d/a_T,
\]

并用自弯轨迹约束 target recombination distance。

**当前 readiness：YELLOW，但不是代码 blocker，因为当前倾向不进入 core set。**

---

## 8. partial coherence / GSM

### 8.1 文献原型

Gaussian Schell-model mutual coherence：

\[
\Gamma(\mathbf r_1,\mathbf r_2)
=\exp\left[-\frac{r_1^2+r_2^2}{w_0^2}
-\frac{|\mathbf r_1-\mathbf r_2|^2}{2\sigma_g^2}\right].
\]

核心无量纲参数：

\[
\gamma_C=w_0/a_T,
\qquad
c=\sigma_g/w_0.
\]

### 8.2 为什么暂不作为第一轮 core field

该家族已经有 mature turbulence + pointing joint optimization；而且数值上需要 coherent-mode decomposition / source ensemble 等额外统计层，会显著扩大计算成本。

因此当前角色：

- literature-positive control；
- optional validation case；
- 不默认占主 structured-field 名额。

如果以后实现，必须区分 source coherence realizations 与 atmospheric realizations，避免错误地把两种 ensemble 混为同一个随机变量。

**当前 readiness：GREEN as literature control / YELLOW as numerical implementation。**

---

## 9. 当前推荐的 provisional core set

在不冻结最终名单的前提下，当前文献证据最支持先准备以下最小代码对象：

1. **Gaussian G0/G1** — 必须；
2. **zeroth-order Bessel-like field** — angular-spectrum redundancy；
3. **OPB continuum radial phase** — autofocusing / inward-energy redistribution；
4. **flat-top representative** — broad-capture / reduced-relative-spreading。

并保留：

- Airy array：path-diversity mechanism / optional architecture control；
- partial coherence：mature joint-optimized literature control。

这个集合并不是“最终论文只有三种新光束”，而是当前最小集合已经覆盖三种彼此真正不同、且与 Paper 1 核心问题直接相关的 structured-field physics，同时避免为了名字完整而重复实现 Airy/OPB 相近的 radial-autofocusing family。

---

## 10. common resource ledger — 代码开始前必须统一输出

对每个 coherent field，至少输出以下无湍流源端/接收端量：

### Tx plane

- `P_T`；
- `a_T`；
- `r50_T, r80_T, r95_T`；
- peripheral-energy fraction；
- field-specific dimensionless structure parameter；
- transverse-spatial-frequency second moment（若数值稳定）。

### Rx plane, no turbulence / no jitter

- `H0=P_R/P_T`；
- `r50_R, r80_R`；
- centroid；
- peak intensity（diagnostic only）；
- capture curve `G(Delta)` 的少量 displacement samples。

### generation resource

若文献给出：

- generation efficiency；
- mode-conversion loss；
- extra rejected diffraction orders；

则单独报告，不默认先乘入 propagation result。Paper 1 可先给 ideal-field result，再给 realistic-efficiency sensitivity。

---

## 11. jitter physical anchors 如何映射到 dimensionless coordinate

当前 physical evidence 已有两类真实飞行锚点：

- high-performance fixed-wing PAT：约 `O(8–10 urad, 1sigma)`；
- multirotor retro-FSO compact fine tracking：约 `O(27–42 urad)` per-axis residual AoA，作为 architecture-mismatched engineering / stress anchor。

这些值不直接冻结 `sigma_theta`。

一旦 `L` 和 Gaussian reference scale `w_ref` 冻结，统一映射：

\[
j=\frac{L\sigma_\theta}{w_{ref}}.
\]

建议最终物理图上至少标注：

- fixed-wing real-flight anchor；
- multirotor compact-tracker engineering anchor；
- 若后续找到 one-way multirotor active-transmitter residual，则加入更直接的 scene point。

科学主图仍以 `j` 为横轴，避免过度声称存在唯一“典型 UAV sigma_theta”。

---

## 12. 下一步参数冻结所需的最小剩余工作

### 必做 A — 冻结统一 common resource convention

需要项目负责人确认：

1. common Tx aperture 是否统一为 circular hard aperture；
2. post-aperture `P_T` 是否作为第一版 equal-power 口径；
3. secondary one-scale diagnostic 选 `H0-matched` 还是 `r50_R-matched`；
4. `w_ref` 最终使用 Gaussian `1/e^2` radius 还是 encircled-energy radius。

### 必做 B — 只关闭三个 field-specific blocker

1. Bessel：circular-truncated J0 vs Bessel-Gaussian；
2. OPB：冻结 `A(r)` 与一个 literature-supported phase-strength / pin-scale representative；
3. flat-top：转录确认 canonical family expression，并冻结一个 moderate order + 可选 high-order stress point。

### 必做 C — scene parameter layer

继续文献驱动冻结：

- wavelength；
- main distance；
- Tx/Rx aperture；
- realistic `Cn2/r0/L0/l0` range；
- physical jitter anchor mapping。

完成 A+B+C 后，即可从 Stage A 转入 Stage B 的**最小代码实现**。无需等所有文献都穷尽。

---

## 13. 当前决策

**CONTINUE。**

现在的主要缺口已经不是“是否有五类新光束文献和参数”，而是：

> 如何把已知文献参数映射到同一资源坐标，并用最少自由度保留各自机制。

当前证据已经足以开始做这种参数映射；尚不足以直接启动正式 Monte Carlo structured-beam comparison。
