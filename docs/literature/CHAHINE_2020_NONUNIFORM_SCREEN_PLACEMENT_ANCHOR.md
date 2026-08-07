# Chahine et al. 2020：multi-screen path discretization / screen placement 锚点

## 1. 文献身份

- Yousef K. Chahine, Sarah A. Tedder, Brian E. Vyhnalek, Adam C. Wroblewski
- *Beam propagation through atmospheric turbulence using an altitude-dependent structure profile with non-uniformly distributed phase screens*
- Proc. SPIE Free-Space Laser Communications XXXII (2020)
- DOI: `10.1117/12.2543583`
- NASA NTRS: `20200001115`
- 证据角色：**screen-number / placement methodology anchor**。

---

## 2. 它解决的不是 phase-screen spectrum，而是 longitudinal discretization

Chen 2020 主要提醒 transverse low-frequency phase sampling 会影响 beam wander；Chahine 2020 则研究另一个独立问题：

> continuous `Cn²(z)` turbulence path 应该如何离散成有限个 thin phase screens？

其 model：

- split-step wave optics；
- modified von Karman refractive-index statistics；
- Hufnagel-Valley altitude-dependent `Cn²(z)`；
- space-to-ground slant path case study；
- 将 uniformly spaced screens 与多种 non-uniform discretization 比较，并和 continuous analytical irradiance/phase statistics 对账。

---

## 3. screen number 不是越多越“科学”

文献回顾指出，在足够细的 segmentation 下，增加 phase-screen number 会减少 thin-screen approximation error；早期研究甚至可使用上百张屏。

但对于 `N >= 2048` 这类实际二维 wave-optics grid，每增加一张 screen 都显著增加计算成本。

所以正确问题不是：

> “文献常用几张屏？”

而是：

> **在目标 observables 达到连续介质/高精度 reference 所需误差后，最少需要多少张屏，以及这些屏应放在哪里？**

这与本项目“不做无意义大规模审计”的原则兼容：screen count 应由科学误差要求确定，而不是追求越多越好。

---

## 4. 为什么 uniform spacing 对非均匀 atmosphere 可能不好

对 slant path / vertical path，`Cn²(z)` 随高度变化很大。等距分段意味着某些 phase screens 代表很强 turbulence volume，另一些代表很弱 volume。

而 thin-screen approximation 在单段 scattering 太强、随后仍有较长 propagation distance 时会变差，因为被 phase-perturbed wavefront 继续传播后发生 energy redistribution，无法被一个简单 thin phase kick 完整代表。

因此文献讨论多种 segmentation philosophy，例如：

- minimize phase variance contribution per segment；
- minimize segment distance；
- minimize scintillation contribution per segment；
- match continuous turbulence moments。

作者的 case study 发现：

> **让每张 screen 对 receiver-plane scintillation 的贡献更均衡/更小的 non-uniform placement，与 analytical continuous-profile theory 的 agreement 优于简单 uniform spacing。**

---

## 5. 不能直接把 NASA 的 non-uniform layout 搬到本项目

该论文主要是：

- space-to-ground；
- altitude-dependent Hufnagel-Valley profile。

而本项目 Paper 1 主场景更可能是：

- near-ground horizontal / low-altitude slant UAV link；
- `Cn²(z)` 可能更接近常数或缓慢变化，但还未冻结。

即使 `Cn²` 为常数，screen 在 longitudinal position 对 receiver statistics 的权重也不完全相同；但是否需要明显 non-uniform spacing必须通过本项目 propagation regime 自己对账。

因此当前不接受：

> “NASA 用 non-uniform screens，所以本项目必须使用同一个 non-uniform algorithm。”

---

## 6. 当前可以冻结的 screen-placement contract

### 6.1 不冻结一个经验 screen count

目前禁止把：

- `5 screens`；
- `10 screens`；
- `20 screens`；
- `128 screens`

中的任何一个写成 science contract 常数。

### 6.2 在 Gaussian benchmark 上选择最小充分 segmentation

后续 production model 应在代表性最弱/最强 turbulence 与 propagation geometry 上比较多个 screen counts / placements，并至少检查：

- beam-wander variance；
- long-term beam radius；
- relevant scintillation statistic；
- finite-aperture mean / distribution stability（若 analytical reference 可用则对账）。

当继续增加 screens 或改变 placement 不再实质改变这些目标 observables，才接受该 segmentation。

### 6.3 screen placement 必须与 `Cn²(z)` profile 一起定义

如果最终主场景采用 constant `Cn²` horizontal path，可以先用 simple/equal segmentation 作为 baseline，再做收敛检查；

如果采用明显 altitude-dependent profile，应考虑按 scintillation contribution / integrated turbulence 进行 non-uniform placement，而不是默认等距。

---

## 7. 与 Chen 2020 的组合后，turbulence-module 验收框架已经更完整

两个 numerical anchors 解决正交问题：

### transverse spectrum accuracy

Chen 2020：

> low-frequency phase sampling 必须足以恢复 beam wander / long-term radius。

### longitudinal path discretization

Chahine 2020：

> screen number / placement 必须足以代表 distributed turbulence，尤其是 nonuniform `Cn²(z)` path。

因此 production model 不能只做其中一个正确。

完整最低逻辑应是：

\[
\text{correct phase-screen statistics}
+
\text{correct low-frequency content}
+
\text{sufficient path segmentation}
\rightarrow
\text{validated distributed-turbulence propagation}.
\]

---

## 8. 当前未冻结

仍然需要后续文献/模型决定：

- main scenario 的 `Cn²(z)` profile；
- Kolmogorov vs modified von Karman；
- `L0` / `l0`；
- actual grid/window；
- horizontal UAV path 下最小 screen count；
- whether non-uniform placement materially improves our observables。

---

## 9. 当前裁决

**状态：READ / SCREEN-PLACEMENT METHODOLOGY ANCHOR。**

接受的核心原则：

> **phase-screen number and spacing are numerical representation choices to be selected by observable-level accuracy/convergence, not physical constants to copy from another paper.**

对于 altitude-dependent turbulence，优先考虑 contribution-balanced non-uniform segmentation；对于 near-horizontal constant/slowly-varying turbulence，先以 simple segmentation 为 baseline，再由 convergence 决定是否需要更复杂 placement。