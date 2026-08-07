# PAPER1_PARAMETER_SOURCE_STATUS

**状态：Stage A 参数来源审计；不是最终科学参数冻结。**

本文件回答：前序五类 turbulence-resistant beam 是否已经有足够明确的文献公式与参数来源，可以进入 Paper 1 的统一参数化准备？

结论：**五类均已获得初步文献覆盖和可追溯参数来源，但“文献参数可复现”不等于“Paper 1 统一比较参数已经冻结”。**

## 1. Bessel / Bessel-like angular-spectrum redundancy

状态：**SOURCE-READY / REPRESENTATIVE FORM NOT YET FROZEN**。

锚点：Eyyuboğlu, Voelz, Xiao, Applied Optics 2013, DOI `10.1364/AO.52.008032`。

已提取：

- source field `J_n(a_B r) exp(i n phi)`；
- square hard truncation；
- `S=10 cm, 40 cm`；
- `n=0...5`；
- `a_B=1...5 cm^-1` for `S=10 cm`；
- `a_B=0.2...1 cm^-1` for `S=40 cm`；
- multi-screen numerical settings、receiver aperture、source-power matching logic。

未冻结：最终用 square-truncated、circular-truncated 还是 Bessel-Gaussian；最终 common-aperture scale mapping。

## 2. Airy / caustic / path-diversity family

状态：**SOURCE-READY / TAXONOMY SPLIT**。

Gu & Gbur 2010：

- finite-energy Airy field；
- `x0=y0=0.012 m`；
- truncation `a=0.1`；
- `lambda=1.55 um`；
- `Cn2=1e-14 m^-2/3`；
- `L=3 km`；
- 4-beamlet array；
- spacing/design displacement `d=0.066 m`。

Zhu et al. 2021 quasi-ring Airy：

- radial phase `Phi=l phi + a k r^(3/2)`；
- `lambda=1550 nm`；
- theoretical input diameter `6.4 cm`、example `a=8e-4`；
- experimental beam diameter约 `6.4 mm`、`a=0.026`；
- `D/r0=1,4`；
- receiver apertures `10,4,3,2 mm`。

未冻结：Airy 是否进入 final common-evaluation set。path-diversity Airy array 是多 beam architecture；quasi-ring Airy 与 OPB 的 radial-autofocusing mechanism 重叠。

## 3. Optical pin beam / radial autofocusing

状态：**MECHANISM SOURCE-READY / FINAL DESIGN PARAMETER EXTRACTION STILL NEEDED**。

锚点：Zhang et al., APL Photonics 2019, DOI `10.1063/1.5095996`。

已提取：

- radial Airy-type phase form；
- `lambda=532 nm`；
- source power约 `2 W`；
- phase-mask diameter约 `5 cm`；
- measured modulation efficiency约 `90%`；
- real-atmosphere kilometer-scale propagation；
- inward energy-flow / opposite transverse-wavevector mechanism。

在正式实现前仍需再做一次“可复现参数抽取”：把原论文中的 exact radial phase / beta / aperture normalization 转写成代码参数，并决定如何在统一 wavelength / Tx aperture 下做物理相似缩放。

## 4. Partial coherence / Gaussian Schell-model

状态：**SOURCE-READY / MATURE JOINT-OPTIMIZATION CONTROL**。

2010–2016 文献链已经给出：

- GSM mutual coherence function；
- source width / coherence length definitions；
- turbulence-only coherence optimization；
- turbulence + pointing + aperture 下 beam-width / coherence joint optimization；
- experimental turbulence-induced beam-wander evidence。

典型公开参数包括：

- `lambda=1550 nm`；
- `L=7.5 km`；
- receiver diameter `40 mm`；
- nominal `w0=0.05 m`；
- pointing displacement sigma `30 cm`；
- 2016 work 还扫描 receiver diameter `40,80,200,400 mm`。

该家族参数来源充分，但因为 joint turbulence-pointing optimization 已成熟，当前倾向作为 control / discussion，而不是 Paper 1 主 novelty representative。

## 5. Flat-top / flattened / multi-Gaussian family

状态：**SOURCE-READY / RESOURCE NORMALIZATION NOT YET FROZEN**。

Eyyuboğlu et al. 2006 + Alavinejad et al. 2008 已提供：

- multi-Gaussian / flat-topped nested family；
- `N=1` 对应 Gaussian，`N>1` flatness 增强；
- source size、source power、M2、receiver beam size、PIB 随 order 的变化；
- 典型基础 source-size parameter `alpha_sx=alpha_sy=3 cm`；
- illustrative `lambda=1.55 um`、`Cn2=1e-15 m^-2/3` 等。

Jiang 2022/2026 又提供 turbulence + pointing direct-competitor boundary。

未冻结：最终 order subset、equal-power rescaling、actual Tx clear aperture matching 与 receiver-plane scale matching。

## 6. 当前总体判断

当前已经完成：

- 五类初始 beam family 均有文献锚点；
- canonical field / mechanism 基本可追溯；
- 大部分原论文示例参数已经可提取；
- 资源陷阱和 direct-competitor 边界已经识别。

当前尚未完成：

- 把各论文原始参数机械拼成一个统一 comparison table；
- 选择最终 3–5 个 representative mechanisms；
- 统一 wavelength / Tx aperture / total power / receiver aperture；
- 定义 field-specific scale conversion；
- 冻结 optimized Gaussian baseline；
- 冻结 turbulence / jitter physical scene ranges。

因此下一步不是继续无限扩充 beam names，而是建立 **literature parameter -> common physical resource -> Paper 1 simulation parameter** 的转换表。

当前推荐 physics taxonomy：

1. Bessel-like angular-spectrum redundancy / self-healing；
2. path diversity（Airy array 作为机制锚点，可不进入同表排行榜）；
3. radial-phase autofocusing / inward energy redistribution（OPB / quasi-ring Airy 中选一个代表）；
4. flat-top / broad-capture / reduced-relative-spreading；
5. partial coherence 作为 mature joint-optimized control。
