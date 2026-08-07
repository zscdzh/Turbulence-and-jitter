# PAPER1_PARAMETER_MAPPING_MATRIX

**状态：与 Scientific Contract v0.3.1 candidate 对齐。**  
**用途：** 把 literature parameters 转换为 common physical resources；不把不同论文的有量纲数字直接拼接。

## 1. common physical resources

首轮全部 coherent deterministic fields 共享：

- `lambda=1550 nm`；
- `L=1 km`；
- circular `D_T=50 mm`；
- circular `D_R=50 mm`；
- post-aperture `P_T=1`；
- paired turbulence/jitter realizations；
- common nominal receiver axis。

所有场在 Tx hard aperture 后重新归一到相同 `P_T`。

必须报告：`r50_T/r80_T/r95_T`、peripheral fraction、source second moment、transverse-frequency descriptor、`H0`、receiver `r50_R/r80_R`、receiver second moment，以及有文献依据时的 generation loss。

## 2. Level A / Level B

### Level A — primary

固定共同物理资源，各 structured family 使用一个文献支持的 representative 参数，不做 joint optimization。

### Level B — only secondary diagnostic

唯一 secondary control：no-turbulence/no-jitter receiver `r80_R`-matched one-scale retuning。

\[
|r_{80,R}^{field}/r_{80,R}^{G0}-1|\le1\%.
\]

若预注册范围内无唯一稳定解，记录 `NO R80 MATCH`，不扩大范围。

`H0` 只报告，不用于 matching。

## 3. Gaussian

\[
U_G(r)=C_Ge^{-r^2/w_G^2}e^{-ikr^2/(2f_G)}\Pi(r/a_T).
\]

G0：`w_G=0.65a_T`, `f_G=infinity`。

G1 候选：

- `w_G/a_T = 0.35,0.45,...,0.95`；
- `u_f=L/f_G = 0,0.5,1.0,1.5,2.0`；
- objective only `Q5%(H)`。

G1 optimization：

1. 全 35 个候选共享 256 common random realizations；
2. Top-5 再共享 768 realizations，最终 `N_opt=1024`；
3. winner 由 1024-sample optimization set 决定；
4. `N_eval=1024` 完全独立；必要时边界点扩展至 4096。

## 4. Bessel

文献原型：Eyyuboğlu 2013 truncated Bessel。

common representative：

\[
U_B(r)=C_BJ_0(\chi_Br/a_T)\Pi(r/a_T).
\]

- Level-A `chi_B=10`；
- Level-B `chi_B in [6,18]`；
- 正式 comparison 前做一次原文 square-window reproduction；
- Bessel-Gaussian 仅在 hard-truncation sensitivity 必要时加入。

## 5. OPB

Zhang 2019 continuum radial phase：

\[
U_{OPB}(r)=C_{OPB}A(r)
\exp[-i(4/3)k\sqrt{\beta}r^{3/2}]\Pi(r/a_T),
\]

\[
A(r)=e^{-r^2/w_A^2},\qquad w_A=0.65a_T.
\]

正确渐近关系：

\[
W(L)=\frac{1}{4k\beta L},
\qquad
\rho_s=4\beta L^2.
\]

定义：

\[
\omega_{OPB}=W(L)/a_T,
\qquad
\rho_s=\frac{L}{ka_T\omega_{OPB}}.
\]

对于 aperture-truncated `w_A=0.65a_T` Gaussian illumination：

\[
r_{95,T}\approx0.775a_T.
\]

因此 primary scene 下：

- hard-aperture constraint：`omega>=0.395`；
- `rho_s<=r95_T`：`omega>=0.509`。

冻结：

- Level-A `omega_OPB=0.55`；
- `beta≈4.49e-9 m^-1`；
- `rho_s≈17.94 mm < r95_T≈19.37 mm`；
- Level-B `omega_OPB in [0.55,0.90]`，且每个候选必须继续满足 `rho_s<=r95_T`。

不实现真实 etched-mask discretization。

## 6. flat-top

\[
U_N(r)=C_N\left[\frac1N\sum_{n=1}^N(-1)^{n-1}\binom Nn
\exp(-nr^2/w_F^2)\right]\Pi(r/a_T).
\]

- `N=1`：Gaussian sanity；
- Level-A `N=4`, `w_F=0.65a_T`；
- `N=8`：optional stress；
- Level-B 固定 `N=4`，只调 `w_F/a_T in [0.40,0.90]`。

不同 `N` 均在 aperture 后 equal-power normalization；不得沿用 fixed-amplitude order-dependent source power。

## 7. discussion-only mechanisms

不进入首轮 common numerical set：

- Airy path diversity；
- partial coherence；
- vector / mode diversity。

它们保留为 literature / architecture context，不再用于扩张首轮代码。

## 8. current gate

本矩阵只定义 field / resource mapping。代码仍由 `docs/SCIENTIFIC_CONTRACT_DRAFT.md` 的 v0.3.1 gate 控制：短审通过前不授权 Gaussian 或 structured-beam implementation。
