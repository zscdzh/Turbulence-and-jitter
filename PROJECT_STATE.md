# 项目状态——UAV-FSO 抗湍流 deterministic transmit fields 的抖动敏感性

**更新日期：2026-08-07**  
**当前主分支：main**  
**当前阶段：Paper 1 / CONTRACT FREEZE GATE**  
**外部审查：REVISE**  
**Scientific Contract：v0.3 candidate，尚未通过短审**  
**正式科学代码：未建立**  
**正式数值结果：无**

## 1. 当前科学问题

Paper 1 已正式收窄为：

> coherent、deterministic、single-aperture transmit fields 在 direct-detection finite-aperture UAV-FSO 链路中的跨机制 turbulence–jitter sensitivity / failure map。

目标不是设计 joint-optimum beam，而是研究既有 turbulence-resistant mechanisms 在 independent post-PAT residual jitter 下的优势保持、压缩、排序反转与失效，并判断这些差异经过 optimized Gaussian 和 receiver-scale control 后是否仍具有结构意义。

Paper 2 才是条件性的 turbulence–jitter co-design。

## 2. 外部审查后的核心集合

第一轮数值集合冻结为：

1. Gaussian G0 / optimized G1；
2. circular-truncated zeroth-order Bessel `J0`；
3. continuum radial-phase OPB；
4. nested multi-Gaussian flat-top。

讨论层保留但不进入首轮数值：

- Airy path diversity；
- partial coherence；
- vector / mode diversity。

## 3. 已关闭的定向文献链

Stage A broad literature search 已结束，只补三条 external-review blocker：

- Nelson et al. 2014：Bessel / Airy quasi-nondiffracting turbulence failure boundary；
- Jiang et al. 2022 / 2026：flat-top + turbulence + pointing direct-competitor audit；
- Lane–Glindemann–Dainty 1992：subharmonic / low-frequency phase-screen anchor。

对应文件：

- `docs/literature/NELSON_2014_BESSEL_AIRY_FAILURE_BOUNDARY_ANCHOR.md`
- `docs/literature/JIANG_2022_2026_FLAT_TOP_DIRECT_COMPETITOR_AUDIT.md`
- `docs/literature/LANE_1992_SUBHARMONIC_LOW_FREQUENCY_ANCHOR.md`

以后不再无边界扩展 beam-name 文献。

## 4. 已修正的关键错误

Zhang 2019 OPB 锚点此前误写：

\[
W(z)\propto1/(4k\beta^2z).
\]

现已修正为原论文 Eq. (5)：

\[
W(z)=1/(4k\beta z).
\]

所有 OPB `beta` / pin-scale mapping 必须使用修正版本。

## 5. v0.3 已冻结的公平比较

### Level A — 主比较

统一：

- `lambda, L, D_T, D_R, P_T`；
- circular Tx / Rx apertures；
- aperture 后 equal-power normalization；
- paired turbulence / jitter realizations；
- transparent source / receiver resource ledger。

### Level B — 唯一 secondary diagnostic

receiver-plane no-turbulence/no-jitter：

\[
r_{80,R}\text{-matched one-scale retuning}.
\]

`H0` 报告但不用于 matching。

## 6. Gaussian zero hypothesis

G1 预注册搜索：

- `w_G/a_T in [0.35,0.95]`；
- `u_f=L/f_G in {0,0.5,1,1.5,2}`；
- 每个 `(tau,j,alpha_R)` point 独立选择；
- 唯一 objective：`Q5%(H)`；
- `N_opt=256` 与 `N_eval=1024` 使用完全分离 random ensembles；
- 只在关键 reversal/boundary uncertainty 未收敛时增加到 `N_confirm=4096`。

## 7. v0.3 primary physical scene

### geometry

- `lambda = 1550 nm`；
- `L = 1 km`；
- `D_T = 50 mm`；
- `D_R = 50 mm`；
- simulation `P_T=1` normalized。

### turbulence

constant-`Cn2` horizontal primary path：

- baseline `Cn2=1e-14 m^(-2/3)`；
- primary sweep `3e-15, 1e-14, 3e-14`；
- baseline `L0=10 m`, `l0=5 mm`；
- sensitivity `L0=5,20 m`, `l0=3,10 mm`。

对 50-mm Tx aperture，primary sweep 对应的 plane-wave diagnostic `D_T/r0` 约为 `0.31, 0.64, 1.23`。

### jitter

主坐标：

\[
j=L\sigma_\theta/w_{ref},
\]

primary sweep：`0, 0.25, 0.5, 1.0, 1.5`。

physical anchors：

- fixed-wing flight约 `8–10 urad (1sigma)`；
- Trinh multirotor retro-FSO约 `27–42 urad/axis`，仅 stress-reference。

另外仅做：

- 一个 `sigma_y/sigma_x=2` anisotropic case；
- 一个 `rho_b=0.5 w_ref` boresight-bias case。

不做 time-domain PSD/controller model。

## 8. core field parameters

### G0

- `w_G=0.65 a_T`；
- `f_G=infinity`。

### Bessel

\[
U_B=C_BJ_0(\chi_Br/a_T)\Pi(r/a_T),
\]

primary `chi_B=10`；Level B 允许 `[6,18]` 只用于 `r80_R` matching。

### OPB

- Gaussian amplitude `A(r)=exp(-r^2/w_A^2)`；
- `w_A=0.65a_T`；
- continuum `r^(3/2)` phase；
- primary `W(L)/a_T=0.35`；
- Level B 允许 `[0.20,0.70]` 只用于 `r80_R` matching。

### flat-top

nested multi-Gaussian family：

- `N=1` sanity；
- `N=4` primary moderate order；
- `N=8` optional stress；
- Level A `w_F=0.65a_T`；
- Level B 固定 `N=4`，只调 `w_F/a_T in [0.40,0.90]`。

## 9. numerical validation contract

structured-field production 之前必须先完成 Gaussian chain：

1. free-space power conservation；
2. Gaussian analytic propagation；
3. displaced finite-aperture capture；
4. analytic jitter broadening；
5. phase-screen PSD；
6. phase structure function；
7. low-frequency / subharmonic convergence；
8. beam-wander variance；
9. long-term radius；
10. scintillation auxiliary convergence；
11. screen-number convergence；
12. grid/window convergence；
13. propagation sampling；
14. maximum-tilt wrap-around / aliasing。

完整 tolerance table 见 `docs/SCIENTIFIC_CONTRACT_DRAFT.md` v0.3 candidate。

## 10. 当前证据边界

### 已支持

- turbulence + pointing 本身不是创新；
- Bessel / OPB / flat-top 具有不同 anti-turbulence physics，值得做跨机制 jitter sensitivity；
- flat-top joint-channel 已有 Jiang 2022/2026 强 direct competitors；
- Bessel/Airy quasi-nondiffracting property 有 Nelson-type turbulence failure boundary；
- low-frequency phase-screen accuracy 会影响 beam wander；Lane 1992 + Chen 2020 足以约束第一版 validation philosophy；
- UAV/PAT residual evidence 足以支持 dimensionless jitter + multiple physical anchors。

### 尚未支持

- 任何 structured field 在本项目 joint channel 中优于 G1；
- 任何 ranking reversal；
- OPB common-tilt failure hypothesis；
- flat-top joint advantage；
- Paper 2 co-design 必然值得启动。

## 11. 当前禁止表述

- “首次联合 turbulence 与 pointing”；
- “首次 structured beam + joint channel”；
- “self-healing 会自动回正”；
- “27–42 urad 是典型 UAV one-way transmitter residual”；
- “OPB / flat-top 已被证明 joint-optimal”；
- “multi-screen / subharmonic 是本项目创新”；
- “低 scintillation = 高 low-tail received power”；
- 把 project representative values 写成 literature-proven optima。

## 12. 当前允许的最小下一步

**当前不授权代码。**

下一步只做 Scientific Contract v0.3 candidate 的短审。若通过，才按以下顺序实施：

1. Gaussian free-space；
2. finite-aperture displacement；
3. analytic jitter；
4. Gaussian multi-screen validation；
5. Eyyuboğlu Bessel reproduction sanity；
6. Bessel / OPB / flat-top common comparison。

## 13. 当前决策

- Paper 1：**CONTINUE**；
- Stage A broad literature：**CLOSED**；
- Contract：**v0.3 CANDIDATE / NEED SHORT REVIEW**；
- Structured-beam code：**NOT AUTHORIZED**；
- Paper 2：**CONDITIONAL GO / NOT AUTHORIZED**。
