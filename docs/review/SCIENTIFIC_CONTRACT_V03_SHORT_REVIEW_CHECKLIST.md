# Scientific Contract v0.3.1 Candidate — Short Review Checklist

**用途：** 这是 code gate 前的最终短复核，不重新开启 Stage-A broad literature review。  
**待审合同：** `../SCIENTIFIC_CONTRACT_DRAFT.md`  
**上一轮决定：** `SCIENTIFIC_CONTRACT_V03_SHORT_REVIEW_DECISION.md`

请只检查以下四组问题。

## 1. OPB finite-aperture feasibility

检查合同中：

\[
W(L)=1/(4k\beta L),
\qquad
\rho_s=4\beta L^2,
\qquad
\omega=W(L)/a_T.
\]

以及：

- `A(r)=exp(-r^2/w_A^2)`, `w_A=0.65a_T`；
- aperture 后 `r95_T≈0.775a_T`；
- primary `omega_OPB=0.55`；
- `beta≈4.49e-9 m^-1`；
- `rho_s≈17.94 mm < r95_T≈19.37 mm`；
- Level-B `omega in [0.55,0.90]` 且继续要求 `rho_s<=r95_T`。

问题：这些关系在量纲、数值与 Zhang 2019 的 stationary-phase interpretation 上是否自洽？

输出：`PASS / REVISE`，只列真正阻塞实现的问题。

## 2. G1 lower-tail optimization

检查：

- 35 个候选全部共享同一组 256 common random realizations；
- Top-5 再共享额外 768 realizations；
- finalist 的最终 `N_opt=1024`；
- winner 只由完整 1024 optimization set 决定；
- `N_eval=1024` 与 optimization 完全 disjoint；
- near-boundary evaluation 扩展至 4096。

问题：这一 staged CRN design 是否足以避免 5% quantile winner 被小样本噪声支配，同时不过度增加计算？

## 3. exact turbulence spectrum / absolute references

检查 exact convention：

\[
\Phi_n(\kappa)=0.033C_n^2
\frac{\exp[-(\kappa/\kappa_m)^2]}
{(\kappa^2+\kappa_0^2)^{11/6}},
\]

\[
\kappa_0=2\pi/L_0,
\qquad
\kappa_m=5.92/l_0,
\]

\[
\Phi_\phi(\kappa)=2\pi k^2\Delta z\,\Phi_n(\kappa),
\]

以及合同中明确写出的 continuous Fourier convention 和 `D_phi` integral。

再检查：

- V6a independent beam-wander spectral quadrature；
- V7a weak-Kolmogorov Gaussian `W_LT` absolute reference；
- V10a fixed-window grid-resolution refinement；
- V10b fixed-`Delta x` physical-window enlargement；
- V11 maximum-tilt wrap-around / aliasing。

问题：这些定义是否已经足以防止 FFT normalization 错误或“自收敛到错误答案”？若仍缺一项，请只指出最小必须补的绝对 benchmark。

## 4. final code-gate decision

若 1–3 均无 blocker，请输出：

> **PASS — AUTHORIZE GAUSSIAN-ONLY IMPLEMENTATION**

该 PASS 只授权：

1. Gaussian free-space；
2. finite-aperture displacement；
3. analytic jitter；
4. Gaussian phase-screen / multi-screen validation V0–V12。

不授权 Bessel / OPB / flat-top production comparison。structured fields 只有 Gaussian chain 全部通过后才进入。

若仍有 blocker，请输出：

> **REVISE — KEEP CODE GATE CLOSED**

并限制为最多 1–3 个真正阻塞实现的问题。
