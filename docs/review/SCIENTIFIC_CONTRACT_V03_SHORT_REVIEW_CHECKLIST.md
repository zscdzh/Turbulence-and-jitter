# Scientific Contract v0.3.2 Candidate — Final Ultra-Short Review Checklist

**用途：** code gate 前的最终极短复核；不重新开启 Stage-A broad literature review，也不重新审查已 PASS 的 OPB、G1、scene 或 mechanism set。  
**待审合同：** `../SCIENTIFIC_CONTRACT_DRAFT.md`  
**上一轮决定：** `SCIENTIFIC_CONTRACT_V031_SHORT_REVIEW_DECISION.md`

本轮只检查一个问题：**phase-spectrum / Fourier `2pi` normalization 是否已经完全自洽。**

## 1. atmospheric spectrum

合同定义：

\[
\Phi_n^{(\mathrm{atm})}(\kappa)=0.033C_n^2
\frac{\exp[-(\kappa/\kappa_m)^2]}
{(\kappa^2+\kappa_0^2)^{11/6}},
\]

\[
\kappa_0=2\pi/L_0,
\qquad
\kappa_m=5.92/l_0,
\]

\[
\Phi_\phi^{(\mathrm{atm})}(\kappa)
=2\pi k^2\Delta z\,\Phi_n^{(\mathrm{atm})}(\kappa).
\]

这里 atmospheric spectrum integral 不额外使用 `(2pi)^-2` measure。

## 2. mathematical Fourier convention

合同保留：

\[
\phi(\mathbf r)=
\int\frac{d^2\kappa}{(2\pi)^2}
\tilde\phi(\boldsymbol\kappa)e^{i\boldsymbol\kappa\cdot\mathbf r},
\]

因此要求：

\[
\boxed{
\Phi_\phi^{(\mathrm{math})}(\kappa)
=(2\pi)^2\Phi_\phi^{(\mathrm{atm})}(\kappa)
=(2\pi)^3k^2\Delta z\,\Phi_n^{(\mathrm{atm})}(\kappa)
}.
\]

并使用：

\[
D_\phi(\rho)
=2\int\frac{d^2\kappa}{(2\pi)^2}
\Phi_\phi^{(\mathrm{math})}(\kappa)
[1-\cos(\boldsymbol\kappa\cdot\boldsymbol\rho)].
\]

请确认这与 atmospheric-measure 写法

\[
D_\phi(\rho)
=2\int d^2\kappa\,
\Phi_\phi^{(\mathrm{atm})}(\kappa)
[1-\cos(\boldsymbol\kappa\cdot\boldsymbol\rho)]
\]

严格等价。

## 3. absolute Kolmogorov gate

V5 现在要求在 screen-level Kolmogorov validation limit 中恢复：

\[
\boxed{
D_\phi(\rho)
=2.91k^2C_n^2\Delta z\,\rho^{5/3}
=6.88\left(\frac{\rho}{r_{0,\mathrm{screen}}}\right)^{5/3}
}
\]

\[
\boxed{
r_{0,\mathrm{screen}}
=[0.423k^2C_n^2\Delta z]^{-3/5}
}.
\]

V5 acceptance：

- finite-scale continuous integral median relative error `<=10%`；
- Kolmogorov-limit absolute amplitude median relative error `<=10%` over preregistered resolved inertial interval；
- log-slope `5/3 ±0.10`。

问题：上述定义是否已经消除 v0.3.1 中的 `(2pi)^2` variance error，并使 V4/V5 能发现 absolute normalization 错误？

## 4. final code-gate decision

若无 remaining normalization blocker，请输出：

> **PASS — AUTHORIZE GAUSSIAN-ONLY IMPLEMENTATION**

该 PASS 只授权：

1. Gaussian free-space；
2. finite-aperture displacement；
3. analytic jitter；
4. Gaussian phase-screen / multi-screen validation V0–V12。

仍不授权 Bessel / OPB / flat-top production comparison。

若仍有确定 blocker，请输出：

> **REVISE — KEEP CODE GATE CLOSED**

并只指出 normalization / absolute-reference 层的最小问题，不重开路线或文献调研。