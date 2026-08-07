# Modified von Kármán PSD convention anchor

**用途：** 为 Scientific Contract v0.3.1 冻结 phase-screen spectrum 与 Fourier normalization，避免不同文献/代码库在 `cycles/m`、`rad/m`、`2pi` 与 `r0` normalization 上混用。

## 1. refractive-index spectrum

本项目采用 angular spatial frequency `kappa [rad/m]`：

\[
\boxed{
\Phi_n(\kappa)=0.033 C_n^2
\frac{\exp[-(\kappa/\kappa_m)^2]}
{(\kappa^2+\kappa_0^2)^{11/6}}
}
\]

其中：

\[
\kappa_0=2\pi/L_0,
\qquad
\kappa_m=5.92/l_0.
\]

这是常用 modified von-Kármán refractive-index PSD form；`L0` 为 outer scale，`l0` 为 inner scale。

## 2. thin-screen phase PSD

对厚度 `Delta z` 的均匀 turbulence slab，采用：

\[
\boxed{
\Phi_\phi(\boldsymbol\kappa)
=2\pi k^2\Delta z\,\Phi_n(|\boldsymbol\kappa|)
}
\]

其中 optical wavenumber：

\[
k=2\pi/\lambda.
\]

该形式与 OSA Continuum 2020 等 spectral-inversion phase-screen derivations 一致。

## 3. continuous Fourier convention

冻结：

\[
\phi(\mathbf r)=
\int\frac{d^2\kappa}{(2\pi)^2}
\tilde\phi(\boldsymbol\kappa)
\exp(i\boldsymbol\kappa\cdot\mathbf r),
\]

以及：

\[
\langle\tilde\phi(\boldsymbol\kappa)
\tilde\phi^*(\boldsymbol\kappa')\rangle
=(2\pi)^2\delta^{(2)}(\boldsymbol\kappa-\boldsymbol\kappa')
\Phi_\phi(\boldsymbol\kappa).
\]

由此：

\[
D_\phi(\rho)=
2\int\frac{d^2\kappa}{(2\pi)^2}
\Phi_\phi(\kappa)
[1-\cos(\boldsymbol\kappa\cdot\boldsymbol\rho)].
\]

离散 FFT 实现可以使用 `cycles/m` 或其他 normalization，但必须显式转换并通过 PSD / structure-function tests 回到账面 convention。

## 4. 与 AOtools 常见形式的关系

AOtools 等实现常用 spatial frequency `f [cycles/m]`，写作：

\[
PSD_\phi(f)\propto0.023r_0^{-5/3}
\frac{\exp[-(f/f_m)^2]}
{(f^2+f_0^2)^{11/6}},
\]

其中 `f0=1/L0`, `fm=5.92/(2pi l0)`。

这与本项目 `kappa=2pi f` 的 angular-frequency convention 等价，但**系数不能在不转换 measure / Fourier normalization 的情况下直接复制**。

因此 production implementation 不允许“库函数能跑”替代 normalization audit。

## 5. validation consequence

至少要求：

- screen PSD level + slope；
- phase structure function vs continuous integral；
- Kolmogorov-limit `5/3` slope sanity；
- low-frequency beam-wander consequence；
- finite `L0/l0` sensitivity。

## 6. 来源

- modified von-Kármán spectrum form：多篇 atmospheric-optics 文献采用 `0.033 Cn2`, `kappa0=2pi/L0`, `kappam=5.92/l0`；
- thin-screen phase spectrum `Phi_phi=2pi k^2 Delta-z Phi_n`：OSA Continuum 2020 spectral-inversion formulation；
- AOtools implementation用于说明 `cycles/m` convention 与 `0.023 r0^(-5/3)` 常见代码形式，不作为项目 normalization 的唯一权威。

本文件只冻结 spectrum convention，不宣称 phase-screen generation algorithm 本身具有创新性。
