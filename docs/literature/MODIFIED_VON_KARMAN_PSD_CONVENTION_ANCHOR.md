# Modified von Kármán PSD convention anchor

**用途：** 为 Scientific Contract v0.3.2 冻结 phase-screen spectrum 与 Fourier normalization，避免不同文献/代码库在 `cycles/m`、`rad/m`、`2pi` 与 `r0` normalization 上混用。

## 1. 先区分 atmospheric PSD 与 mathematical Fourier PSD

本项目明确区分两套对象：

1. `Phi_n^(atm)` / `Phi_phi^(atm)`：大气光学文献常用的谱归一化，谱积分 measure 不额外带 `(2pi)^-d`；
2. `Phi_phi^(math)`：与本项目数学 Fourier convention `d^2kappa/(2pi)^2` 配套的二维 phase PSD。

两者不能共用同一个数值系数。

## 2. atmospheric refractive-index spectrum

采用 angular spatial frequency `kappa [rad/m]`：

\[
\boxed{
\Phi_n^{(\mathrm{atm})}(\kappa)=0.033 C_n^2
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

这是常用 modified von-Kármán refractive-index spectrum form。

## 3. atmospheric thin-screen phase spectrum

对厚度 `Delta z` 的均匀 turbulence slab，在 atmospheric convention 下：

\[
\boxed{
\Phi_\phi^{(\mathrm{atm})}(\boldsymbol\kappa)
=2\pi k^2\Delta z\,\Phi_n^{(\mathrm{atm})}(|\boldsymbol\kappa|)
}
\]

其中 optical wavenumber：

\[
k=2\pi/\lambda.
\]

该式本身不与 `(2pi)^-2` Fourier measure 混用。

## 4. 本项目冻结的 mathematical Fourier convention

冻结：

\[
\phi(\mathbf r)=
\int\frac{d^2\kappa}{(2\pi)^2}
\tilde\phi(\boldsymbol\kappa)
\exp(i\boldsymbol\kappa\cdot\mathbf r),
\]

\[
\langle\tilde\phi(\boldsymbol\kappa)
\tilde\phi^*(\boldsymbol\kappa')\rangle
=(2\pi)^2\delta^{(2)}(\boldsymbol\kappa-\boldsymbol\kappa')
\Phi_\phi^{(\mathrm{math})}(\boldsymbol\kappa).
\]

为与 atmospheric convention 描述同一个 physical covariance，必须满足：

\[
\boxed{
\Phi_\phi^{(\mathrm{math})}(\kappa)
=(2\pi)^2\Phi_\phi^{(\mathrm{atm})}(\kappa)
=(2\pi)^3 k^2\Delta z\,\Phi_n^{(\mathrm{atm})}(\kappa)
}.
\]

因此：

\[
D_\phi(\rho)=
2\int\frac{d^2\kappa}{(2\pi)^2}
\Phi_\phi^{(\mathrm{math})}(\kappa)
[1-\cos(\boldsymbol\kappa\cdot\boldsymbol\rho)].
\]

等价地，也可以写成 atmospheric measure：

\[
D_\phi(\rho)=
2\int d^2\kappa\,
\Phi_\phi^{(\mathrm{atm})}(\kappa)
[1-\cos(\boldsymbol\kappa\cdot\boldsymbol\rho)].
\]

两种写法必须给出相同数值。

## 5. Kolmogorov-limit absolute normalization

在 `L0 -> infinity`、`l0 -> 0` 的 screen-level validation limit 中，必须恢复：

\[
\boxed{
D_\phi(\rho)
=2.91k^2C_n^2\Delta z\,\rho^{5/3}
=6.88\left(\frac{\rho}{r_{0,\mathrm{screen}}}\right)^{5/3}
}
\]

其中：

\[
\boxed{
r_{0,\mathrm{screen}}
=[0.423k^2C_n^2\Delta z]^{-3/5}
}.
\]

这个绝对幅值关系是本项目排除 `2pi` normalization 自洽错误的首要 screen-level sanity check。

## 6. 与 AOtools / cycles-per-meter convention 的关系

AOtools 等实现常用 spatial frequency `f [cycles/m]`，并写成类似：

\[
PSD_\phi(f)\propto0.023r_0^{-5/3}
\frac{\exp[-(f/f_m)^2]}
{(f^2+f_0^2)^{11/6}},
\]

其中 `f0=1/L0`, `fm=5.92/(2pi l0)`。

这与 `kappa=2pi f` 的 angular-frequency representation 可以等价，但只有同时转换：

- frequency variable；
- spectral measure；
- PSD coefficient；
- FFT normalization；

才能保持 physical covariance 不变。

因此 production implementation 不允许“库函数能跑”替代 normalization audit。

## 7. 离散实现要求

离散 FFT / subharmonic generator 可以内部采用任何一致 convention，但必须在文档和测试中明确：

- 内部 frequency unit：`cycles/m` 或 `rad/m`；
- 对应 PSD 是 `atm` 还是 `math` convention；
- spectral-cell measure；
- inverse-FFT normalization；
- random complex coefficient variance。

最终至少必须同时通过：

1. V4 phase-screen PSD absolute level + slope；
2. V5 phase structure function absolute amplitude + slope；
3. Kolmogorov-limit `6.88(rho/r0_screen)^(5/3)`；
4. propagation-level beam-wander / long-term-radius absolute references。

## 8. 当前裁决

Scientific Contract v0.3.2 采用：

> **保留 mathematical Fourier convention `d^2kappa/(2pi)^2`，并显式使用 `Phi_phi^(math)=(2pi)^3 k^2 Delta-z Phi_n^(atm)`。**

不再把 `Phi_phi=2pi k^2 Delta-z Phi_n` 直接代入带 `(2pi)^-2` 的积分。

本文件只冻结 spectrum / Fourier normalization，不宣称 phase-screen generation algorithm 本身具有创新性。