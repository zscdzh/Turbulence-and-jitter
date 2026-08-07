# PAPER1_COMMON_RESOURCE_GATE_DRAFT

**状态：与 Scientific Contract v0.3.1 candidate 对齐；不是代码授权。**

外部短审最新决定：**REVISE — KEEP CODE GATE CLOSED**。本文件只保留 common-resource / fairness / field-feasibility gate；权威数值以 `../SCIENTIFIC_CONTRACT_DRAFT.md` 为准。

## Gate A — common physical resources

第一版统一：

1. single circular Tx hard aperture；
2. equal post-aperture transmitted power `P_T`；
3. single circular finite Rx aperture，direct detection；
4. common `lambda, L, D_T, D_R`；
5. paired turbulence/jitter realizations；
6. common nominal receiver axis。

Level A 是正式主比较。

## Gate B — report resource ledger, do not over-match

所有场报告：

- `r50_T, r80_T, r95_T`；
- peripheral / halo fraction；
- source second moment；
- transverse-frequency descriptor；
- `H0`；
- receiver `r50_R, r80_R`；
- receiver second moment；
- generation efficiency / conversion loss if literature-supported。

这些量用于解释收益来源，不在 Level A 中全部配平。

## Gate C — only secondary control: `r80_R` matching

no-turbulence/no-jitter receiver `r80_R`-matched one-scale retuning：

\[
|r_{80,R}^{field}/r_{80,R}^{G0}-1|\le1\%.
\]

若预注册范围无唯一稳定解，记录 `NO R80 MATCH`，不得扩大范围救结果。

- Bessel：只调 `chi_B in [6,18]`；
- OPB：只调 `omega_OPB in [0.55,0.90]`；
- flat-top：固定 `N=4`，只调 `w_F/a_T in [0.40,0.90]`。

`H0` 只报告，不作为 matching constraint。

## Gate D — Gaussian G0/G1

G0：`w_G=0.65a_T`, `f_G=infinity`。

G1 search：

- `w_G/a_T = 0.35:0.10:0.95`；
- `u_f=L/f_G = 0,0.5,1.0,1.5,2.0`；
- 唯一 objective：`Q5%(H)`。

G1 final parameter selection 采用 CRN staged design：

1. 全 35 候选共享 256 realizations；
2. Top-5 补同一套 additional CRN 到总计 `N_opt=1024`；
3. winner 只由 1024 optimization set 决定；
4. `N_eval=1024` 与 optimization 完全 disjoint；
5. near-boundary evaluation 可扩至 4096。

## Gate E — frozen first-round field scope

只包括：

- Gaussian；
- circular-truncated `J0`；
- continuum OPB；
- nested multi-Gaussian flat-top。

不进入首轮数值：Airy path diversity、partial coherence、vector/mode diversity。

## Gate F — field feasibility

### Bessel

\[
U_B=C_BJ_0(\chi_Br/a_T)\Pi(r/a_T).
\]

Level-A `chi_B=10`。正式 comparison 前做 Eyyuboğlu square-window reproduction。

### OPB

\[
U_{OPB}=C_{OPB}e^{-r^2/(0.65a_T)^2}
\exp[-i(4/3)k\sqrt\beta r^{3/2}]\Pi(r/a_T).
\]

必须同时满足：

\[
W(L)=1/(4k\beta L),
\qquad
\rho_s=4\beta L^2,
\qquad
\rho_s\le r_{95,T}.
\]

primary scene 下冻结：

- `omega_OPB=W(L)/a_T=0.55`；
- `beta≈4.49e-9 m^-1`；
- `rho_s≈17.94 mm`；
- `r95_T≈19.37 mm`。

Level-B OPB 所有候选都必须重新检查 `rho_s<=r95_T`。

### flat-top

- `N=1` sanity；
- `N=4` primary；
- `N=8` optional stress；
- aperture 后 equal-power normalization。

## Gate G — turbulence numerical prerequisites

在任何 structured-field multi-screen run 前，Gaussian chain 必须通过：

- exact modified-von-Karman PSD / Fourier normalization；
- PSD / structure function；
- independent beam-wander absolute reference；
- weak-turbulence long-term-radius absolute reference；
- low-frequency refinement；
- screen-number convergence；
- **fixed-window grid-resolution** convergence；
- **fixed-Delta-x physical-window** convergence；
- maximum-tilt wrap-around / aliasing；
- split-step sampling convergence。

具体 V0–V12 acceptance 见科学合同。

## Current decision

> **KEEP CODE GATE CLOSED until v0.3.1 short re-review PASS.**

即使 PASS，也只授权 Gaussian-only implementation；Bessel/OPB/flat-top 等待 Gaussian V0–V12 全部通过。
