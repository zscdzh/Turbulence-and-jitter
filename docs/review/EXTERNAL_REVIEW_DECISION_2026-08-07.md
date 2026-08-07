# 外部审查正式结论（2026-08-07）

**Decision: REVISE**

含义：课题继续；停止无边界扩展 Stage A 文献；在下列科学 blocker 关闭前，不授权 structured-beam 代码或正式 Monte Carlo。

## 一、范围与核心集合

Paper 1 建议正式收窄为：

> coherent、deterministic、single-aperture transmit fields 在 direct-detection finite-aperture UAV-FSO 链路中的跨机制 turbulence–jitter sensitivity / failure map。

第一轮核心集合：

- optimized/common-resource Gaussian；
- zeroth-order Bessel；
- OPB；
- flat-top。

Airy path diversity 只保留为文献/架构讨论；partial coherence 作为成熟 joint-optimization 对照保留在讨论层，首轮不增加 source ensemble。

## 二、代表场裁决

- Bessel：circular-truncated `J0` 为主代表；进入正式比较前先做一次 Eyyuboğlu 2013 square-window 文献复现。只有结论依赖硬截断时，才增加 Bessel–Gaussian sensitivity check。
- OPB：continuum radial phase 足够，不实现 32-filament / etched-mask discretization。
- flat-top：`N=1` nested-Gaussian sanity + 一个 moderate order；一个 high-order 仅作为可选 stress point。

## 三、必须修正的 OPB 公式

原论文 Eq. (5) 的 pin-width 关系为：

\[
W(z)=\frac{1}{4k\beta z}.
\]

不得写成 `1/(4 k beta^2 z)`。错误版本量纲不成立，会污染 `beta` 与 target pin width 的映射。

## 四、公平比较裁决

### Level A：接受

统一：

- `lambda, L, D_T, D_R, P_T`；
- aperture 后总功率归一化；
- paired turbulence/jitter realizations；
- 完整 source/receiver resource ledger。

### Level B：修改

唯一 secondary diagnostic 改为：

> receiver-plane、无扰动 `r80_R`-matched one-scale retuning。

`H0` 继续报告，但不作为匹配约束。

每个 structured family 只能开放一个预注册尺度变量；不得同时改变 family order 和 radial scale 形成隐性多自由度优化。

### Gaussian G1

必须预注册：

- `w_G, f_G` 搜索边界；
- 唯一主优化指标；
- 是否逐 `(tau,j,alpha_R)` 点优化；
- optimization ensemble 与 final evaluation ensemble 完全分离。

当前推荐主指标为 `Q5%(H)`，完整 ECDF 为核心展示，outage 为辅助。

## 五、jitter 场景裁决

现有证据足以启动 dimensionless mechanism study：

- fixed-wing 约 `8–10 urad (1sigma)`：高性能真实飞行闭环锚点；
- Trinh 2021 约 `27–42 urad/axis`：multirotor double-pass compact-tracker stress anchor；不得升级为通用 one-way transmitter residual。

主坐标继续采用：

\[
j=\frac{L\sigma_\theta}{w_{ref}}.
\]

第一版可采用 zero-mean isotropic Gaussian residual，并补：

- 一个 anisotropic covariance case；
- 一个 nonzero boresight-bias case。

若 Paper 1 明确为 ensemble/static reliability study，可暂不模拟 PSD、correlation time 与闭环控制动态。

## 六、只关闭三条定向文献链

不再广撒网，只完成：

1. Nelson 等 Bessel/Airy turbulence failure boundary；
2. Jiang 2022/2026 flat-top direct-competitor audit；
3. Lane–Glindemann–Dainty 1992 subharmonic / low-frequency phase-screen anchor。

## 七、turbulence numerical contract 补充要求

在 beam-wander、long-term radius、scintillation、screen-number convergence 基础上，增加：

- phase-screen PSD / structure-function validation；
- grid/window convergence；
- propagation sampling convergence；
- 最大 tilt 下的 wrap-around / aliasing 检查；
- production 前冻结 von Kármán `L0/l0` baseline 与 sensitivity range。

constant-`Cn2` 水平链路可先用 equal-spacing screens；高度依赖 `Cn2(z)` 只作为 secondary case。

## 八、进入代码前必须关闭的五个 blocker

1. 修正 OPB `beta` 公式，并冻结 OPB `A(r)`、phase strength / pin-scale；冻结 Bessel truncation 与 flat-top canonical expression/order。
2. 正式冻结 Paper 1 scope 与四场核心集合。
3. 冻结 Level A、`r80_R`-matched Level B，以及 G1 的目标、范围和独立评价规则。
4. 只完成 Nelson、Jiang 2022/2026、Lane 1992 三条定向文献链。
5. 冻结一个 primary physical scene 与完整 Gaussian numerical-validation table，包括 `L0/l0`、grid/window、tilt sampling 与 observable-level tolerance。

## 九、允许的最小下一步

仅修改科学合同，形成 Scientific Contract v0.3 candidate。通过短审后，再依次执行：

1. Gaussian free-space；
2. finite-aperture displacement；
3. analytic jitter benchmark；
4. Gaussian multi-screen validation；
5. 最后加入 Bessel / OPB / flat-top。

## 十、禁止表述

- “首次联合 turbulence 与 pointing”；
- “首次 structured beam + joint channel”；
- “self-healing 等于自动回正”；
- “27–42 urad 是典型 UAV 发射端残差”；
- “flat-top 或 OPB 已被证明 joint-optimal”；
- “multi-screen 本身是创新”；
- “低 scintillation 等于高低分位接收功率”。
