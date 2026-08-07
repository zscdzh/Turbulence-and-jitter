# Zhang 2019 OPB：finite-aperture stationary-radius feasibility addendum

**用途：** 修正 v0.3 contract 中仅按 pin width 反推 `beta`、但没有检查有限 Tx aperture 是否覆盖 stationary contribution 的缺口。

## 1. 原论文渐近关系

Zhang et al. 2019 的 continuum stationary-phase result 同时包含：

\[
W(z)=\frac{1}{4k\beta z},
\]

以及 amplitude sampling at approximately

\[
A(4\beta z^2).
\]

因此目标距离 `z=L` 对应的发射面 stationary source radius 为：

\[
\boxed{\rho_s=4\beta L^2}.
\]

只检查 `W(L)` 而不检查 `rho_s` 会产生一个有限孔径问题：数学上反推出的 pin width 可能依赖 aperture 外根本不存在的 source contribution。

## 2. 与 project `omega_OPB` 的关系

定义：

\[
\omega_{OPB}=\frac{W(L)}{a_T}.
\]

由 `W(L)=1/(4k beta L)`：

\[
\beta=\frac{1}{4kLa_T\omega_{OPB}},
\]

所以：

\[
\boxed{\rho_s=\frac{L}{ka_T\omega_{OPB}}}.
\]

hard-aperture 最低要求：

\[
\rho_s\le a_T
\Rightarrow
\omega_{OPB}\ge \frac{L}{ka_T^2}.
\]

在 `lambda=1550 nm, L=1 km, a_T=25 mm` 下：

\[
\omega_{hard,min}\approx0.395.
\]

因此旧 `omega=0.35` 不可作为该 finite-aperture scene 下的渐近 OPB representative。

## 3. Gaussian illumination 下更严格的 project rule

项目采用：

\[
A(r)=\exp(-r^2/w_A^2),
\qquad w_A=0.65a_T,
\]

并在 `r<=a_T` 后重新归一。

其 aperture-normalized encircled energy 为：

\[
E(<r)=
\frac{1-e^{-2r^2/w_A^2}}
{1-e^{-2a_T^2/w_A^2}}.
\]

令 `E(<r95)=0.95`，得到：

\[
r_{95,T}\approx0.775a_T.
\]

项目采用 representative feasibility rule：

\[
\boxed{\rho_s\le r_{95,T}}.
\]

这不是 Zhang 2019 的 universal theorem，而是本项目为了确保 stationary contribution 位于主要 source-energy support 内而采用的 conservative resource rule。

对应：

\[
\omega_{OPB}\gtrsim0.509.
\]

因此 v0.3.1 冻结：

\[
\boxed{\omega_{OPB}=0.55}.
\]

数值为：

- `W(L)=13.75 mm`；
- `beta≈4.49e-9 m^-1`；
- `rho_s≈17.94 mm`；
- `r95_T≈19.37 mm`。

Level-B 只允许 `omega in [0.55,0.90]`，并对每个候选再次检查 `rho_s<=r95_T`。

## 4. 证据边界

接受：

- `rho_s=4 beta L^2` 来自 Zhang 2019 stationary-phase structure；
- finite aperture 必须覆盖相关 stationary source region，否则不能直接调用该渐近 pin-width interpretation。

项目自定义而非文献定理：

- 用 `r95_T` 而不仅是 hard `a_T` 作为代表性 feasibility threshold；
- `omega=0.55` 是 resource-consistent representative，不是 turbulence/jitter optimum。

## 5. 对 Paper 1 的影响

该修订只解决“field definition 是否可由冻结 aperture 实现”的 blocker，不预判 OPB 在 turbulence、jitter 或 joint channel 中的性能。

来源：Zhang et al., APL Photonics 4, 076103 (2019), DOI `10.1063/1.5095996`。
