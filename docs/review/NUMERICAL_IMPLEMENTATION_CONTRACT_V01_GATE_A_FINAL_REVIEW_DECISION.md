# Numerical Implementation Contract v0.1 — Gate-A 最终审查裁决

**日期：2026-08-07**  
**Decision：PASS — AUTHORIZE V0–V3 IMPLEMENTATION**  
**上位科学合同：Scientific Contract v0.3.2**  
**对应实现合同：`docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V01.md`**

本文件记录 Gaussian numerical qualification 的 Gate-A implementation review 最终裁决。它不修改 Scientific Contract v0.3.2，也不授权 Gate B / V4–V5。

---

## 1. 审查范围

本轮只审查：

- centered spatial grid；
- FFT frequency grid；
- centered FFT wrapper 与 NumPy normalization；
- paraxial Fresnel transfer-function convention；
- tilt sign；
- Gaussian power / centroid / second-moment radius estimator；
- V0/V1 qualification grid 与 analytic references；
- V1 phase-curvature estimator；
- V2 displaced-Gaussian finite-aperture reference 与 qualification points；
- V3 Gaussian-jitter deterministic quadrature、grid 与 analytic broadening reference。

不重新审查：

- Paper-1 scope；
- primary physical scene；
- fairness contract；
- structured-field definitions；
- turbulence PSD continuous normalization；
- V4–V12 的完整实现合同。

---

## 2. 已确认通过的定义

以下实现定义已确认无物理矛盾并足够唯一化：

### centered grid / FFT

\[
x_m=(m-N/2)\Delta x,
\qquad
f_p=\frac{p-N/2}{N\Delta x},
\]

以及唯一 centered wrapper：

\[
\mathcal F_c[U]
=
\operatorname{fftshift}
\{\operatorname{fft2}[\operatorname{ifftshift}(U)]\},
\]

\[
\mathcal F_c^{-1}[F]
=
\operatorname{fftshift}
\{\operatorname{ifft2}[\operatorname{ifftshift}(F)]\}.
\]

NumPy FFT 显式使用 `norm="backward"`；二维 inverse FFT 因而包含 `1/N^2`。

### Fresnel / tilt sign

Gate A 使用 paraxial Fresnel transfer function：

\[
H_F
=
\exp[-i\pi\lambda\Delta z(f_x^2+f_y^2)],
\]

并统一移除 global carrier phase。

transmitter tilt：

\[
U'(x,y)
=
U(x,y)\exp[i k_0(\theta_xx+\theta_yy)]
\]

与 vacuum 中正倾角产生正向 centroid displacement 一致。

### Gaussian radius

\[
W_{\rm num}
=
\sqrt{
2\frac{\sum[(x-x_c)^2+(y-y_c)^2]I}{\sum I}
}
\]

正确恢复 ideal circular Gaussian 的 `1/e^2` intensity radius。

`W` 与 Paper-1 的 `w_ref=r80_R_G0` 保持明确分离。

---

## 3. V0 / V1 qualification parameters — PASS

冻结：

\[
\lambda=1550\,\mathrm{nm},
\qquad
W_0=16.25\,\mathrm{mm},
\]

\[
z_R=535.210845\,\mathrm{m}.
\]

qualification grid：

\[
N=512,
\qquad
\Delta x=W_0/16=1.015625\,\mathrm{mm},
\]

\[
L_{\rm win}=0.520\,\mathrm{m}.
\]

固定传播点：

\[
z/z_R=\{0.5,1,2\}.
\]

V0 acceptance 保持 Scientific Contract 的：

\[
\max_z\frac{|P(z)-P(0)|}{P(0)}\le10^{-4}.
\]

V1 radius acceptance：

\[
\frac{|W_{\rm num}-W_{\rm ref}|}{W_{\rm ref}}\le1\%.
\]

---

## 4. V1 phase-curvature estimator — FINAL PASS

前一版 review 发现相邻 phase gradient 的拟合位置应位于 half-pixel，而不是左端 sample coordinate。最终合同已修复。

定义：

\[
g_x
=
\frac{\arg(U_{m+1,n}U^*_{m,n})}{\Delta x},
\qquad
x_{m+1/2}=x_m+\frac{\Delta x}{2},
\]

\[
g_y
=
\frac{\arg(U_{m,n+1}U^*_{m,n})}{\Delta x},
\qquad
y_{n+1/2}=y_n+\frac{\Delta x}{2}.
\]

拟合：

\[
g_x=2c_{\rm num}x_{m+1/2},
\qquad
g_y=2c_{\rm num}y_{n+1/2}.
\]

同时冻结：

- gradient pair 两端均满足 `I/Imax >= 1e-3`；
- intensity weight 为相邻两点强度的几何平均；
- `x/y` samples 联合做 zero-intercept weighted least-squares fit；
- 所有进入拟合的相邻 phase difference 满足

\[
|\Delta\phi_{\rm adjacent}|<\pi/2.
\]

解析 reference：

\[
c_{\rm ref}=\frac{k_0}{2R(z)}>0.
\]

acceptance：

\[
\frac{|c_{\rm num}-c_{\rm ref}|}{|c_{\rm ref}|}\le1\%.
\]

该定义消除了 global phase、piston 和二维 phase unwrap 的实现歧义。

---

## 5. V2 displaced Gaussian capture — PASS

独立 analytic reference 冻结为：

\[
H_{\rm ref}
=
1-Q_1\left(\frac{2d}{W},\frac{2a_R}{W}\right).
\]

允许使用数学等价的 noncentral-chi-square CDF 作为计算方式。

qualification grid：

\[
W_{\rm test}=10\,\mathrm{mm},
\qquad
N=512,
\]

\[
\Delta x=W_{\rm test}/64=0.15625\,\mathrm{mm},
\qquad
L_{\rm win}=80\,\mathrm{mm}.
\]

固定测试点：

\[
(a_R/W,d/W)
=
(2,0),\,(1,0.25),\,(1,1),\,(1,1.5).
\]

独立审查核算的 pixel-center relative errors 约为：

\[
0.0002\%,\quad0.0427\%,\quad0.1480\%,\quad0.2980\%,
\]

均低于冻结 acceptance：

\[
\frac{|H_{\rm num}-H_{\rm ref}|}{H_{\rm ref}}\le0.5\%.
\]

---

## 6. V3 Gaussian jitter broadening — FINAL PASS

冻结 primary validation propagation distance：

\[
L=1000\,\mathrm{m},
\]

以及

\[
W_{\rm vac}(L)=34.436977\,\mathrm{mm}.
\]

V3 明确沿用 V0/V1 spatial grid：

\[
N_{V3}=512,
\qquad
\Delta x_{V3}=W_0/16,
\qquad
L_{\rm win,V3}=0.520\,\mathrm{m}.
\]

V3 不施加 Tx aperture 或 Rx aperture。

validation-only jitter coordinate：

\[
s_J=\frac{L\sigma_\theta}{W_{\rm vac}(L)},
\]

且明确

\[
s_J\ne j,
\qquad
j=\frac{L\sigma_\theta}{w_{\rm ref}}.
\]

固定：

\[
s_J=\{0,0.25,0.50,0.75\}.
\]

V3 principal gate 使用 `9 x 9` product Gauss–Hermite deterministic quadrature：

\[
\theta_i=\sqrt2\sigma_\theta x_i,
\qquad
W_{ij}=\frac{w_iw_j}{\pi}.
\]

全部 81 个节点从 `z=0` 同一 unclipped Gaussian source 直接传播到 `L=1000 m`，中间不经过 screen、aperture 或其他 optical operation。

analytic benchmark：

\[
W_{\rm eff}^2
=
W_{\rm vac}^2+4L^2\sigma_\theta^2.
\]

acceptance：

\[
\frac{|W_{\rm num,LE}-W_{\rm eff}|}{W_{\rm eff}}\le1\%
\]

对全部四个 `s_J` 点成立。

外审对该冻结 grid 的独立检查显示，最强 `s_J=0.75` 时外侧 10% guard region 的功率约为

\[
5.4\times10^{-12},
\]

窗口足够，不构成 V3 finite-window blocker。

---

## 7. Gate-A code authorization

从本 decision 起，正式授权且仅授权以下最小实现：

1. centered spatial/frequency grid constructor；
2. centered FFT wrappers；
3. unclipped Gaussian validation source；
4. paraxial Fresnel propagator；
5. power / centroid / second-moment radius estimators；
6. V1 phase-curvature estimator；
7. circular receiver aperture；
8. displaced-Gaussian analytic reference；
9. deterministic tilt；
10. Gauss–Hermite jitter quadrature；
11. V0–V3 qualification runner；
12. 最小结果表与必要诊断图。

当前不要求 CI、大规模 regression suite、production architecture、batch Monte Carlo framework、structured-field abstraction 或 phase-screen module。

---

## 8. 结论边界

Gate A PASS 只支持：

> vacuum Gaussian propagation、finite-aperture capture 与 independent Gaussian pointing-jitter numerical kernel 已具备预注册实现合同，可进入 V0–V3 numerical qualification。

它不支持：

- turbulence propagation 已验证；
- phase screens 已验证；
- beam wander / scintillation 已验证；
- production grid 已收敛；
- structured-field implementation 已授权；
- Bessel / OPB / flat-top comparison 已授权；
- Gaussian 在正式 turbulence–jitter scene 下已有性能结论。

---

## 9. Gate B 状态

V4–V5 仍为：

> **NOT YET AUTHORIZED — IMPLEMENTATION CONTRACT PENDING**

V4 开始前仍需关闭：

- continuous PSD → discrete random Fourier coefficient 的唯一 normalization；
- Hermitian symmetry / DC / self-conjugate-bin treatment；
- V4 PSD estimator；
- V4 resolved spectral band；
- V5 resolved separation interval；
- V4 radial-annulus estimator、target slope 与 slope tolerance。

这些问题不再阻塞 V0–V3。

---

## 10. Final decision

> **PASS — AUTHORIZE V0–V3 IMPLEMENTATION**
>
> **SCIENTIFIC CONTRACT v0.3.2 REMAINS FROZEN**
>
> **V4–V5 IMPLEMENTATION REMAINS NOT AUTHORIZED**
>
> **STRUCTURED-FIELD IMPLEMENTATION REMAINS NOT AUTHORIZED**
