# Numerical Implementation Contract v0.1

**日期：2026-08-07**  
**状态：Gate A PASS — AUTHORIZE V0–V3 IMPLEMENTATION**  
**上位合同：Scientific Contract v0.3.2**  
**Gate B：V4–V5 IMPLEMENTATION NOT YET AUTHORIZED**

本文件冻结 Gaussian numerical qualification 的 Gate-A 离散实现约定。它只解决连续物理模型落到离散数组、FFT、真空传播、有限孔径和 Gaussian jitter benchmark 时的实现歧义，不修改 Scientific Contract v0.3.2 的 scientific scope、primary scene、fairness contract、field definitions 或 V0–V12 acceptance thresholds。

Gate A 只包含：

- V0：free-space power conservation；
- V1：unclipped Gaussian analytic propagation；
- V2：displaced Gaussian finite-aperture capture；
- V3：Gaussian jitter broadening。

本文件不授权 phase-screen generation、turbulence、subharmonics、multi-screen propagation、G1 optimization、Bessel、OPB、flat-top 或 structured-field Monte Carlo。

---

## 1. 坐标与数组 convention — FROZEN

采用偶数网格：

\[
N\in2\mathbb Z,
\qquad N_x=N_y=N,
\qquad \Delta x=\Delta y.
\]

物理坐标：

\[
\boxed{
x_m=(m-N/2)\Delta x,
\qquad
y_n=(n-N/2)\Delta x
}
\]

其中

\[
m,n=0,\ldots,N-1.
\]

因此 array index `N/2` 对应物理原点，单轴物理窗口为

\[
L_{\rm win}=N\Delta x,
\]

坐标区间为

\[
[-L_{\rm win}/2,\,L_{\rm win}/2-\Delta x].
\]

不得另行引入 half-pixel-centered grid。

---

## 2. Spatial-frequency grid — FROZEN

离散 FFT 内部使用 spatial frequency

\[
f_x,f_y\quad[\mathrm{cycles/m}].
\]

冻结

\[
\boxed{
f_p=\frac{p-N/2}{N\Delta x}
}
\]

其中

\[
p=0,\ldots,N-1.
\]

频率间隔：

\[
\Delta f=\frac{1}{N\Delta x}=\frac{1}{L_{\rm win}}.
\]

Scientific Contract 中的 angular spatial frequency 由

\[
\kappa_x=2\pi f_x,
\qquad
\kappa_y=2\pi f_y
\]

映射得到。

变量命名必须显式区分：

- `fx, fy`：cycles/m；
- `kappa_x, kappa_y`：rad/m；
- `k0=2*pi/lambda`：optical wavenumber，rad/m。

禁止用同一个代码变量 `k` 同时表示 optical wavenumber 与 transverse spatial frequency。

---

## 3. Centered FFT wrapper — FROZEN

全项目只允许以下 centered FFT wrapper：

\[
\boxed{
\mathcal F_c[U]
=
\operatorname{fftshift}
\left\{
\operatorname{fft2}
[\operatorname{ifftshift}(U)]
\right\}
}
\]

以及

\[
\boxed{
\mathcal F_c^{-1}[F]
=
\operatorname{fftshift}
\left\{
\operatorname{ifft2}
[\operatorname{ifftshift}(F)]
\right\}
}
\]

NumPy 调用必须显式使用 `norm="backward"`。

因此：

- forward FFT 不含 `1/N^2`；
- inverse FFT 含 `1/N^2`。

不得依赖 NumPy 默认参数的隐式行为。

---

## 4. Free-space propagator — FROZEN

Gate A 使用 **paraxial Fresnel transfer-function propagator**，不称为 exact angular-spectrum propagator。

global carrier phase

\[
\exp(i k_0\Delta z)
\]

在整个实现中统一移除。

传播 transfer function 冻结为

\[
\boxed{
H_F(f_x,f_y;\Delta z)
=
\exp\left[
-i\pi\lambda\Delta z(f_x^2+f_y^2)
\right]
}
\]

并定义

\[
U(z+\Delta z)
=
\mathcal F_c^{-1}
\left[
\mathcal F_c[U(z)]H_F
\right].
\]

Gate A 不同时实现多个 production propagator。

---

## 5. Tilt convention — FROZEN

沿用 Scientific Contract v0.3.2：

\[
\boxed{
U'(x,y)
=
U(x,y)
\exp[i k_0(\theta_x x+\theta_y y)]
}
\]

其中

\[
k_0=\frac{2\pi}{\lambda}.
\]

正方向冻结为

\[
\theta_x>0\Rightarrow x_c(L)>0,
\qquad
\theta_y>0\Rightarrow y_c(L)>0.
\]

paraxial vacuum reference：

\[
x_c(L)=L\theta_x,
\qquad
y_c(L)=L\theta_y.
\]

所有 angular variables 使用 rad。

---

## 6. Power、centroid 与 Gaussian radius estimator — FROZEN

强度：

\[
I_{mn}=|U_{mn}|^2.
\]

full-grid power：

\[
\boxed{
P_{\rm grid}
=\Delta x^2\sum_{m,n}|U_{mn}|^2
}
\]

centroid：

\[
\boxed{
x_c=\frac{\sum x_m I_{mn}}{\sum I_{mn}},
\qquad
y_c=\frac{\sum y_n I_{mn}}{\sum I_{mn}}
}
\]

Gaussian numerical `1/e^2` intensity radius：

\[
\boxed{
W_{\rm num}
=
\sqrt{
2\frac{
\sum[(x_m-x_c)^2+(y_n-y_c)^2]I_{mn}
}{
\sum I_{mn}
}
}
}
\]

对于

\[
I(r)=I_0\exp(-2r^2/W^2),
\]

该 estimator 对应 `1/e^2` intensity radius `W`。

必须区分：

- `W`：Gaussian `1/e^2` intensity radius；
- `r80`：80% encircled-energy radius；
- `w_ref=r80_R_G0`：Paper-1 jitter normalization reference。

不得令 `W = w_ref`。

---

## 7. Gate-A qualification Gaussian — FROZEN

V0、V1、V3 使用专门的 unclipped Gaussian：

\[
U(r,0)=C\exp(-r^2/W_0^2).
\]

冻结：

\[
\lambda=1550\,\mathrm{nm},
\]

\[
\boxed{
W_0=0.65a_T=16.25\,\mathrm{mm}
}
\]

其中 primary scene 的

\[
a_T=25\,\mathrm{mm}.
\]

该 field 只是 analytic qualification field，不施加 Tx aperture，不属于正式 G0 comparison result。

Rayleigh range：

\[
\boxed{
z_R=\frac{\pi W_0^2}{\lambda}=535.210845\,\mathrm{m}
}
\]

---

## 8. V0/V1 qualification grid — FROZEN

冻结：

\[
\boxed{N=512}
\]

\[
\boxed{
\Delta x=\frac{W_0}{16}=1.015625\,\mathrm{mm}
}
\]

因此

\[
\boxed{
L_{\rm win}=N\Delta x=0.520\,\mathrm{m}
}
\]

该 grid 只用于 V0/V1 qualification，不是 turbulence production grid。

---

## 9. V0 — Free-space power conservation

固定传播距离：

\[
\boxed{
z/z_R=\{0.5,1,2\}
}
\]

定义

\[
\epsilon_P(z)
=
\frac{|P_{\rm grid}(z)-P_{\rm grid}(0)|}{P_{\rm grid}(0)}.
\]

验收：

\[
\boxed{
\max_z\epsilon_P(z)\le10^{-4}
}
\]

V0 不施加 Tx aperture、Rx aperture、jitter 或 turbulence。

---

## 10. V1 — Analytic Gaussian radius

解析 radius：

\[
\boxed{
W(z)=W_0\sqrt{1+(z/z_R)^2}
}
\]

固定验证点仍为

\[
z/z_R=\{0.5,1,2\}.
\]

定义

\[
\boxed{
\epsilon_W
=
\frac{|W_{\rm num}-W_{\rm ref}|}{W_{\rm ref}}
}
\]

验收：

\[
\boxed{
\epsilon_W\le1\%
}
\]

不得根据数值结果事后更换传播距离。

---

## 11. V1 — Phase-curvature estimator — FROZEN

Gate A 不验 absolute optical phase、global piston 或 Gouy phase 本身。验收变量为 quadratic phase coefficient

\[
\boxed{
c_{\rm ref}=\frac{k_0}{2R(z)}
}
\]

其中

\[
R(z)=z\left[1+(z_R/z)^2\right].
\]

按本合同的传播符号：

\[
\boxed{c_{\rm ref}>0}.
\]

不执行二维 global phase unwrap。

### 11.1 Wrapped local phase gradient

定义

\[
g_x(m,n)
=
\frac{
\arg[U(x_{m+1},y_n)U^*(x_m,y_n)]
}{\Delta x},
\]

\[
g_y(m,n)
=
\frac{
\arg[U(x_m,y_{n+1})U^*(x_m,y_n)]
}{\Delta x}.
\]

上述梯度对应半像素位置：

\[
\boxed{
x_{m+1/2}=x_m+\frac{\Delta x}{2},
\qquad
y_{n+1/2}=y_n+\frac{\Delta x}{2}
}
\]

因此拟合模型冻结为

\[
\boxed{
g_x=2c_{\rm num}x_{m+1/2},
\qquad
g_y=2c_{\rm num}y_{n+1/2}}
\]

而不得使用 `x_m` 或 `y_n` 作为 gradient sample position。

### 11.2 Fitting region

一个 gradient pair 只有在两个端点都满足

\[
\boxed{
I/I_{\max}\ge10^{-3}
}
\]

时才允许进入 fit。

权重冻结为相邻两点强度的几何平均：

\[
\boxed{
w_x(m,n)=\sqrt{I_{m+1,n}I_{m,n}}
}
\]

\[
\boxed{
w_y(m,n)=\sqrt{I_{m,n+1}I_{m,n}}
}
\]

`x` 与 `y` gradient samples 联合进行 zero-intercept weighted least-squares fit，得到唯一 `c_num`。

### 11.3 Wrapped-gradient guard

所有进入拟合的相邻 phase differences 必须满足

\[
\boxed{
|\Delta\phi_{\rm adjacent}|<\frac{\pi}{2}
}
\]

若该 guard 不满足，不允许通过 phase unwrap 或改变拟合方式补救，应判定 qualification grid 不适用于该 V1 phase test，并先修订 grid contract。

### 11.4 Acceptance

\[
\boxed{
\epsilon_c
=
\frac{|c_{\rm num}-c_{\rm ref}|}{|c_{\rm ref}|}
\le1\%
}
\]

并要求

\[
\boxed{c_{\rm num}>0}.
\]

V1 phase PASS 只验证 Gaussian quadratic phase curvature，不代表 arbitrary phase-field propagation 已全面验证。

---

## 12. V2 — Displaced Gaussian finite-aperture capture

V2 不依赖 V0/V1 propagated field，直接构造 receiver-plane analytic Gaussian intensity：

\[
\boxed{
I(x,y)
=
\frac{2}{\pi W^2}
\exp\left[
-\frac{2[(x-d)^2+y^2]}{W^2}
\right]
}
\]

receiver aperture：

\[
A_R(x,y)=
\begin{cases}
1,&x^2+y^2\le a_R^2,\\
0,&\mathrm{otherwise}.
\end{cases}
\]

numerical capture：

\[
\boxed{
H_{\rm num}=\Delta x^2\sum A_R I
}
\]

### 12.1 Independent analytic reference

冻结：

\[
\boxed{
H_{\rm ref}
=
1-Q_1\left(\frac{2d}{W},\frac{2a_R}{W}\right)
}
\]

其中 `Q1` 为 first-order Marcum-Q function。实现允许使用数学上等价的 noncentral-chi-square CDF 计算 reference。

不得使用同一 Cartesian pixel mask 作为 reference。

### 12.2 Qualification grid and points

validation-only：

\[
\boxed{W_{\rm test}=10\,\mathrm{mm}}
\]

\[
\boxed{N=512}
\]

\[
\boxed{
\Delta x=W_{\rm test}/64=0.15625\,\mathrm{mm}
}
\]

因此

\[
L_{\rm win}=80\,\mathrm{mm}.
\]

固定四组 dimensionless cases：

\[
\boxed{
(a_R/W,d/W)
=
(2,0),\,(1,0.25),\,(1,1),\,(1,1.5)
}
\]

对应 analytic capture approximately：

\[
H_{\rm ref}\approx0.9997,\,0.8309,\,0.3965,\,0.1133.
\]

不得根据 numerical outcome 更换测试点。

### 12.3 Acceptance

\[
\boxed{
\epsilon_{V2}
=
\frac{|H_{\rm num}-H_{\rm ref}|}{H_{\rm ref}}
}
\]

四点全部要求：

\[
\boxed{\epsilon_{V2}\le0.5\%}
\]

V2 只验证 aperture geometry、pixel-center integration、displacement 和 finite-aperture capture。

---

## 13. V3 — Gaussian jitter broadening

V3 使用与 V0/V1 相同的 unclipped Gaussian source，传播距离固定为

\[
\boxed{L=1000\,\mathrm{m}}.
\]

vacuum analytic radius：

\[
\boxed{
W_{\rm vac}(L)
=
W_0\sqrt{1+(L/z_R)^2}
=34.436977\,\mathrm{mm}
}
\]

### 13.1 V3 qualification grid — FROZEN

V3 明确沿用 V0/V1 spatial grid：

\[
\boxed{N_{V3}=512}
\]

\[
\boxed{
\Delta x_{V3}=W_0/16=1.015625\,\mathrm{mm}
}
\]

\[
\boxed{
L_{\rm win,V3}=0.520\,\mathrm{m}
}
\]

V3 不施加 Tx aperture，也不施加 Rx aperture。

### 13.2 Validation-only jitter coordinate

定义

\[
\boxed{
s_J=\frac{L\sigma_\theta}{W_{\rm vac}(L)}
}
\]

必须明确

\[
\boxed{s_J\ne j}.
\]

Paper-1 正式变量保持

\[
j=\frac{L\sigma_\theta}{w_{\rm ref}}.
\]

固定

\[
\boxed{
s_J=\{0,0.25,0.50,0.75\}
}
\]

不得根据结果更换 jitter points。

### 13.3 Deterministic Gauss–Hermite ensemble

V3 PASS/FAIL 不使用 Monte Carlo estimator。

采用 product Gauss–Hermite quadrature：

\[
\boxed{n_{\rm GH}=9\quad\text{per axis}}
\]

若一维 nodes/weights 对应

\[
\int_{-\infty}^{\infty}e^{-x^2}f(x)dx,
\]

则 angular nodes 冻结为

\[
\boxed{
\theta_i=\sqrt{2}\sigma_\theta x_i
}
\]

二维 normalized weight：

\[
\boxed{
W_{ij}=\frac{w_iw_j}{\pi}
}
\]

共 `9 x 9 = 81` 个 angular nodes。每个节点均：

1. 从同一个 `z=0` unclipped Gaussian source 出发；
2. 只施加对应 transmitter tilt phase；
3. 使用冻结的 paraxial Fresnel propagator；
4. 从 `z=0` 直接传播到 `L=1000 m`；
5. 不经过中间 screen、aperture 或其他 optical operation。

long-exposure intensity：

\[
I_{\rm LE}=\sum_{i,j}W_{ij}I_{ij}.
\]

### 13.4 Observable and acceptance

对 `I_LE` 使用与 V1 相同的二阶矩 radius estimator。

analytic benchmark：

\[
\boxed{
W_{\rm eff}^2
=
W_{\rm vac}^2+4L^2\sigma_\theta^2
}
\]

定义

\[
\boxed{
\epsilon_{V3}
=
\frac{|W_{\rm num,LE}-W_{\rm eff}|}{W_{\rm eff}}
}
\]

全部四个 `s_J` 点均要求

\[
\boxed{\epsilon_{V3}\le1\%}.
\]

未来 Monte Carlo jitter RNG 只做非 Gate 的低成本 sanity check：均值、两轴方差和轴间相关性。Monte Carlo noise 不参与 V3 principal PASS/FAIL。

---

## 14. Gate-A 最小代码范围

Gate-A PASS 后，只授权建立：

1. centered spatial/frequency grid constructor；
2. centered FFT wrappers；
3. Gaussian validation source；
4. paraxial Fresnel propagator；
5. power / centroid / second-moment radius estimators；
6. phase-curvature estimator；
7. receiver circular aperture；
8. displaced-Gaussian analytic reference；
9. deterministic tilt；
10. Gauss–Hermite jitter quadrature；
11. V0–V3 qualification runner；
12. 最小结果表。

当前不要求 CI、大规模 regression suite、production architecture、batch Monte Carlo framework、structured-field abstraction 或 phase-screen module。

---

## 15. Gate-A 最小输出

### V0

- propagation distance；
- input/output power；
- relative drift。

### V1

- `z/z_R`；
- analytic / numerical `W`；
- radius error；
- analytic / numerical `c`；
- curvature error；
- wrapped-gradient guard maximum。

### V2

- `a_R/W`；
- `d/W`；
- `H_ref`；
- `H_num`；
- relative error。

### V3

- `s_J`；
- `sigma_theta`；
- analytic / numerical `W_eff`；
- relative error。

少量诊断图可以生成，但图不作为唯一 PASS/FAIL 依据。

---

## 16. 结论边界

即使 V0–V3 全部 PASS，也只能表述：

> vacuum Gaussian propagation、finite-aperture capture 与 independent Gaussian pointing-jitter numerical kernel 已通过预注册 analytic qualification。

不得由此表述：

- turbulence propagation 已正确；
- phase screens 已正确；
- beam wander 已正确；
- scintillation 已正确；
- production grid 已收敛；
- structured fields 已获准正式比较；
- Gaussian 在 turbulence–jitter channel 中的性能已经得到结论。

---

## 17. Gate B 状态

V4–V5 implementation 仍未授权。进入 Gate B 前还必须冻结并复核：

- continuous PSD → discrete frequency-cell coefficient variance；
- Hermitian random coefficients、DC 与 self-conjugate bins；
- V4 PSD estimator；
- V4 resolved spectral band；
- V5 resolved separation interval；
- V4 radial-annulus estimator、target slope definition 与 slope tolerance。

当前只作为候选而非授权值保留：

\[
f\in\left[4/L_{\rm win},\,0.20/\Delta x\right],
\]

\[
\rho\in[4\Delta x,\,L_{\rm win}/8].
\]

因此：

> **V4–V5 IMPLEMENTATION REMAINS NOT AUTHORIZED.**
