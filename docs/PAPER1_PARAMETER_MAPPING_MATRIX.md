# PAPER1_PARAMETER_MAPPING_MATRIX

**状态：Scientific Contract v0.3 candidate 对齐版。短审通过前不授权代码。**  
**日期：2026-08-07**

本表只回答：如何把文献代表场转换为同一物理资源与同一 receiver-scale diagnostic，而不把原论文的 wavelength/aperture/power 当成结构收益。

## 1. common physical layer

Primary scene：

| Quantity | Frozen v0.3 candidate |
|---|---|
| `lambda` | 1550 nm |
| `L` | 1000 m |
| `D_T` | 50 mm |
| `D_R` | 50 mm |
| `P_T` | normalized 1 after common aperture |
| Tx aperture | circular hard aperture |
| Rx aperture | circular finite aperture, direct detection |
| turbulence | constant-`Cn2` horizontal modified/von-Karman |
| `Cn2` primary | `3e-15, 1e-14, 3e-14 m^-2/3` |
| `L0` baseline | 10 m; sensitivity 5/20 m |
| `l0` baseline | 5 mm; sensitivity 3/10 mm |
| jitter coordinate | `j=L sigma_theta/w_ref` |
| `j` primary | `0,0.25,0.5,1.0,1.5` |

所有 coherent fields 在 common Tx aperture 后重新归一：

\[
\int_{r\le a_T}|U_0|^2dA=P_T.
\]

## 2. G0 Gaussian reference

\[
U_{G0}(r)=C_G\exp(-r^2/w_G^2)\Pi(r/a_T),
\]

冻结：

- `w_G=0.65 a_T`；
- `f_G=infinity`；
- `w_ref=r80_R(G0)`，由 validated free-space propagation 得到。

Gaussian analytic jitter benchmark 使用单独的 `1/e^2` intensity radius `W`，不得与 `r80` 混用。

## 3. G1 optimized Gaussian

\[
U_G(r)=C_G\exp(-r^2/w_G^2)
\exp[-ikr^2/(2f_G)]\Pi(r/a_T).
\]

搜索：

- `gamma_G=w_G/a_T = 0.35,0.45,0.55,0.65,0.75,0.85,0.95`；
- `u_f=L/f_G = 0,0.5,1,1.5,2`。

唯一 objective：`Q5%(H)`。

每个 `(tau,j,alpha_R)` point 独立选择 G1；`N_opt=256` 与 `N_eval=1024` 使用完全分离 ensembles；关键 boundary 如仍不确定才增加到 `N_confirm=4096`。

## 4. Bessel mapping

Literature prototype：Eyyuboğlu 2013 truncated Bessel。

Paper 1 main field：

\[
U_B(r)=C_BJ_0(\chi_Br/a_T)\Pi(r/a_T).
\]

- primary `chi_B=10`；
- literature-supported mapped range约 `O(5-20)`；
- Level B 只允许 `chi_B in [6,18]` 做 `r80_R` matching；
- 正式 common comparison 前做一次 square-window Eyyuboğlu reproduction sanity；
- Bessel-Gaussian only if truncation sensitivity materially changes conclusions。

## 5. OPB mapping

Correct continuum field：

\[
U_{OPB}(r)=C_{OPB}\exp(-r^2/w_A^2)
\exp[-i(4/3)k\sqrt{\beta}r^{3/2}]\Pi(r/a_T),
\]

with

\[
w_A=0.65a_T.
\]

Correct pin-width relation：

\[
\boxed{W(z)=1/(4k\beta z)}.
\]

定义：

\[
\omega_{OPB}=W(L)/a_T.
\]

- primary `omega_OPB=0.35`；
- `beta=1/(4kLa_T omega_OPB)`；
- Level B 只允许 `omega_OPB in [0.20,0.70]` 做 `r80_R` matching；
- 不实现 32-filament / etched-mask details。

## 6. flat-top mapping

Canonical nested multi-Gaussian：

\[
U_N(r)=C_N\left[\frac1N\sum_{n=1}^N(-1)^{n-1}\binom{N}{n}
\exp(-nr^2/w_F^2)\right]\Pi(r/a_T).
\]

- `N=1` nested Gaussian sanity；
- `N=4` primary moderate representative；
- `N=8` optional high-order stress；
- primary `w_F=0.65a_T`；
- Level B 固定 `N=4`，只允许 `w_F/a_T in [0.40,0.90]` 做 `r80_R` matching。

不得把 `N=4/8` 写成 Jiang 2022/2026 joint optima。

## 7. Level A resource ledger

所有 field 必须记录：

- `r50_T,r80_T,r95_T`；
- peripheral/halo fraction；
- source second moment；
- transverse-frequency/angular-spectrum descriptor；
- no-disturbance `H0`；
- receiver `r50_R,r80_R`；
- receiver second moment；
- literature-supported generation loss/efficiency。

Level A 不硬匹配这些量。

## 8. Level B matching rule

唯一 secondary diagnostic：

\[
r80_R(field)=r80_R(G0)\pm1\%.
\]

只允许一个 family-specific scale parameter。若预注册范围内无唯一稳定解，报告 `NO R80 MATCH`，不得扩大参数范围救结果。

`H0` 始终报告，但不是匹配条件。

## 9. out-of-scope mechanisms

- Airy path diversity：discussion/architecture only；
- partial coherence：discussion/mature joint-optimization control only；
- vector/mode diversity：out of current direct-detection single-aperture scope。

## 10. parameter provenance rule

所有数值必须标记为以下之一：

- `LITERATURE_MEASURED`；
- `LITERATURE_SIMULATION`；
- `LITERATURE_DERIVED_RANGE`；
- `PROJECT_REPRESENTATIVE_FREEZE`；
- `PROJECT_SENSITIVITY_RANGE`；
- `DERIVED_FROM_FROZEN_SCENE`。

当前 `chi_B=10`、`omega_OPB=0.35`、flat-top `N=4`、primary geometry 均属于 `PROJECT_REPRESENTATIVE_FREEZE`，不是文献证明的 optimum。
