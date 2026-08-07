# KEY_LITERATURE_MAP

**状态：Stage A broad search CLOSED；Scientific Contract v0.3 candidate literature map。**  
**日期：2026-08-07**

本文件不再作为“继续扩文献”的任务清单，而是记录已经足够支持 v0.3 的核心证据链和角色边界。

## 1. Paper 1 正式 scope

只研究：

> coherent deterministic single-aperture transmit fields + direct-detection finite-aperture receiver。

因此 Airy path-diversity、partial coherence、vector/mode diversity 即使重要，也不要求进入首轮 common numerical set。

## 2. core mechanism anchors

### Gaussian / turbulence + pointing baseline

- Liu / Jiang et al. 2021, IEEE Access, DOI `10.1109/ACCESS.2021.3099871`：wave-optics pointing tilt、single-screen weak-turbulence benchmark、finite-aperture received-power PDF。
- classic Gaussian turbulence+pointing literature：用于约束 optimized Gaussian zero hypothesis。

### Bessel / angular-spectrum redundancy

- Eyyuboğlu, Voelz, Xiao 2013, Applied Optics, DOI `10.1364/AO.52.008032`：resource-fairness anchor；低 scintillation 不自动转化为 received-power advantage。
- Nelson et al. 2014, JOSA A, DOI `10.1364/JOSAA.31.000603`：quasi-nondiffracting turbulence failure boundary；`r0` 接近 aperture scale 时机制明显退化。

Numerical role：**core representative**。

### OPB / radial autofocusing

- Zhang et al. 2019, APL Photonics, DOI `10.1063/1.5095996`：mechanism + kilometer-scale atmosphere experiment anchor。
- Correct pin-width relation：`W(z)=1/(4 k beta z)`。

Numerical role：**core representative**。

### flat-top / broad capture

- Eyyuboğlu et al. 2006, Optics Express, DOI `10.1364/OE.14.004196`：source-size/power/M2/resource chain。
- Alavinejad et al. 2008, Optics and Lasers in Engineering, DOI `10.1016/j.optlaseng.2007.07.003`：turbulence spreading / Strehl anchor。
- Jiang et al. 2022, Optics Communications, DOI `10.1016/j.optcom.2022.128703`：flat-top + turbulence + jitter/bias + average irradiance / average received power direct competitor。
- Jiang et al. 2026, Applied Optics, DOI `10.1364/AO.578489`：pointing + gamma–gamma + far-field average BER direct competitor。

Numerical role：**core mature positive-control representative**。

## 3. discussion-only mechanisms

### Airy path diversity

- Gu & Gbur 2010, Optics Letters, DOI `10.1364/OL.35.003456`：self-bending enabled multi-path decorrelation / recombination。
- Zhu et al. 2021, Optics Express, DOI `10.1364/OE.435863`：quasi-ring Airy finite-aperture communication，机制与 radial autofocusing/OPB 部分重叠。

Role：**discussion / architecture context only**。

### partial coherence

- Borah & Voelz 2010；Lee et al. 2013；Liu et al. 2014；Lee et al. 2016。

Role：已有成熟 turbulence+pointing joint optimization，**discussion / mature control only**。

## 4. direct competitor boundary

- Liu/Jiang 2022 HG aircraft-platform work：structured beam + turbulence + pointing 已存在；不能宣称 first joint structured-beam channel。
- Jiang 2022/2026：flat-top joint-channel 已有明确 analytical/performance chain。
- Badás 2024/2026：jitter-only Gaussian/LG/annular/super-Gaussian optimization，主要约束 Paper 2。

因此 Paper 1 novelty 必须落在：

- coherent deterministic cross-mechanism comparison；
- low-frequency-validated distributed wave optics；
- independent beam-wander / mechanical-jitter ledger；
- realization-level finite-aperture low tail；
- optimized Gaussian；
- resource + receiver-scale control；
- mechanism failure/applicability map。

## 5. UAV/PAT residual evidence

- Lei et al. 2019 fixed-wing actual flight：约 `8–10 urad (1sigma)` high-performance closed-loop anchor。
- Trinh et al. 2021 multirotor retro-FSO：约 `27–42 urad/axis` closed-loop ground-tracker residual，double-pass stress-reference；不得解释成 universal one-way transmitter residual。
- Moon et al. 2025：3D raw attitude / geometry model；不得与 post-PAT residual 混用。
- Ke 2021 / 2023：lab/field tracking capability references。

状态：**足以支持 dimensionless jitter study，不再阻塞代码前合同。**

## 6. turbulence numerical-method chain

- Lane, Glindemann, Dainty 1992, DOI `10.1088/0959-7174/2/3/003`：subharmonic / low-frequency + structure-function anchor。
- Chen et al. 2020, Applied Optics, DOI `10.1364/AO.389121`：low-frequency error 对 beam wander / long-term radius 的 propagation consequence。
- Chahine et al. 2020：non-uniform screen placement for altitude-dependent turbulence；secondary scene only。

状态：**足以冻结 v0.3 first numerical-validation philosophy。**

## 7. broad-search stop rule

Stage A 广撒网正式结束。

只有以下情况允许再补文献：

1. 数值结果与已知 literature anchor 明显冲突；
2. 审稿人/短审指出一个会改变 core set 或 novelty 的直接竞争工作；
3. 某个 production numerical parameter 无法由当前 evidence chain 合理冻结。

不得因为发现新的 beam name 就重新打开 Stage A。
