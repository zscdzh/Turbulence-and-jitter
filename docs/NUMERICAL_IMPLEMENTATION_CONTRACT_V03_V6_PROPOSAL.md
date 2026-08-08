# Numerical Implementation Contract v0.3 — V6 Beam-Wander Proposal

**日期：2026-08-08**  
**状态：PROPOSED FOR EXTERNAL REVIEW — NOT AUTHORIZED FOR IMPLEMENTATION**  
**上位科学合同：Scientific Contract v0.3.2（保持冻结）**  
**Gate B：V4–V5 QUALIFIED**  
**V6 simulation：NOT AUTHORIZED**  
**V7–V12 / production propagation / structured fields：CLOSED**

本文件只把 Scientific Contract 已冻结的 V6a/V6b 转化为唯一、可执行的 propagation-level qualification proposal。它不修改 Gate-B phase-screen PSD、FFT/Hermitian、subharmonic coefficient formula，也不授权任何 V6 数值运行。

---

## 1. V6 要回答的唯一问题

V6 不是 production turbulence Monte Carlo，也不评价通信增益。它只验证：

1. **V6a absolute beam-wander reference**：已通过 Gate B 的 phase-screen generator 经过 split-step propagation 后，weakest-turbulence Gaussian 的 turbulence-only centroid wander variance 是否恢复独立 spectral reference；
2. **V6b low-frequency refinement**：在完全相同传播设置下，进一步增加一层 subharmonic 是否使 beam-wander variance 改变小于 5%。

Scientific Contract 的冻结门限：

\[
\boxed{\left|V_{\rm bw,num}/V_{\rm bw,ref}-1\right|\le10\%}
\]

和

\[
\boxed{\left|V_{P+1}/V_P-1\right|<5\%}.
\]

V6 PASS 也不自动授权 V7–V12 或 structured fields。

---

## 2. Validation scene — PROPOSED

采用 Scientific Contract primary geometry 与 weakest turbulence：

- `lambda = 1550 nm`；
- `L = 1000 m`；
- `D_T = 50 mm`, `a_T = 25 mm`；
- G0 `w_G = 0.65 a_T = 16.25 mm`, `f_G = infinity`；
- post-aperture transmitted power normalized to `P_T = 1`；
- `Cn2 = 3e-15 m^(-2/3)`；
- baseline finite scales `L0 = 10 m`, `l0 = 5 mm`；
- `j = 0`；
- boresight bias = 0；
- no anisotropic jitter；
- no receiver-aperture clipping in the V6 centroid observable。

G0 仍按 common circular Tx aperture 定义。该 aperture 对 underlying Gaussian 截去的无穷平面功率约 0.879%，因此 V6a spectral reference 仍使用同一 underlying Gaussian 的 analytic `W(z)`；这一点作为本 proposal 的明确外审检查项，不把它伪装成无假设的等价关系。

---

## 3. Validation grid — PROPOSED, NOT PRODUCTION

沿用已经通过 V0–V5 的 qualification grid：

\[
N=512,\qquad
\Delta x=1.015625\ {\rm mm},\qquad
L_{\rm win}=0.520\ {\rm m}.
\]

这只是 V6 validation grid。

它不冻结 production grid；V10a/V10b 仍负责后续 resolution/window convergence。

### boundary diagnostic

每个最终 receiver-plane realization 记录 outer-10%-window power fraction。若任何 realization 明显出现边缘污染，或 ensemble 最大值超过 `1e-4`，则：

> **REVISE — V6 VALIDATION GRID / WINDOW**

该项是数值有效性 guard，不是新的物理 acceptance claim。

---

## 4. Longitudinal propagation — PROPOSED

V6a/V6b 固定使用：

\[
\boxed{M_{\rm val}=32}
\]

个 equal-spacing screens，作为 **validation-only longitudinal ceiling**。

\[
\Delta z=L/M_{\rm val}=31.25\ {\rm m}.
\]

screen 位于每个 segment 的 midpoint：

\[
z_m=(m+1/2)\Delta z,\qquad m=0,\ldots,31.
\]

传播采用 symmetric split-step：

1. source plane → `Delta z/2` Fresnel propagation；
2. apply screen 0；
3. 相邻 screen 间传播 `Delta z`；
4. apply next screen；
5. final screen → receiver plane `Delta z/2`。

Fresnel kernel 与 Gate A 保持一致：

\[
H_F=\exp[-i\pi\lambda\Delta z(f_x^2+f_y^2)].
\]

`M_val=32` 的目的只是避免 V6 absolute-reference comparison 被粗 longitudinal discretization 主导。它**不是 production screen-number selection**；V9 仍按 `4 -> 8 -> 16 -> 32` 决定 production screen count。

---

## 5. Per-screen turbulence definition — INHERITED

每个 V6 screen 使用 Gate B 已通过的 finite-scale modified-von-Kármán generator：

- cycles/m ↔ rad/m mapping unchanged；
- PSD normalization unchanged；
- Hermitian ownership unchanged；
- recursive subharmonics unchanged；
- per-screen strength使用 `Cn2 = 3e-15` 与 `Delta z = 31.25 m`；
- base FFT + recursive subharmonics；
- baseline low-frequency depth：

\[
\boxed{P=9}.
\]

P=9 来自 Gate-B minimum-depth deterministic bias-headroom policy；V6 不重新优化 P。

### piston hygiene

在每张总相位屏进入传播因子前执行：

\[
\boxed{\phi_m\leftarrow\phi_m-\langle\phi_m\rangle_{x,y}}.
\]

只去掉 spatial piston；禁止移除 tilt 或任何低阶梯度。

然后使用：

\[
U\leftarrow U\exp(i\phi_m).
\]

---

## 6. Beam-wander observable — UNIQUE DEFINITION

V6 使用 full computational plane intensity：

\[
I(x,y)=|U_L(x,y)|^2.
\]

不施加 receiver aperture，因为 V6 spectral reference 是 beam centroid 的 full-plane quantity，而不是 finite-aperture communication observable。

每个 realization：

\[
x_c=\frac{\sum xI}{\sum I},\qquad
y_c=\frac{\sum yI}{\sum I}.
\]

定义 ensemble turbulence-only beam-wander variance：

\[
\boxed{
V_{\rm bw}
=\frac1N\sum_{n=1}^N
\left[(x_{c,n}-\bar x_c)^2+(y_{c,n}-\bar y_c)^2\right]
}.
\]

单位：`m^2`。

同时报告：

- `Var_x`；
- `Var_y`；
- `V_bw = Var_x + Var_y`；
- `sqrt(V_bw)` in mm；
- sample mean centroid `(xbar,ybar)`。

x/y anisotropy 仅作 diagnostic，不新增正式门限。

---

## 7. V6a independent spectral reference — FROZEN PHYSICS, PROPOSED NUMERICS

独立 reference 必须在单独 code path 中实现，禁止调用：

- phase-screen generator；
- FFT/IFFT；
- discrete subharmonic summation；
- empirical propagation results。

直接使用 Scientific Contract frozen atmospheric PSD 与 spectral quadrature：

\[
\boxed{
\langle r_c^2\rangle_{\rm ref}
=4\pi^2k^2W_R^2
\int_0^L dz\int_0^\infty d\kappa\,
\kappa\Phi_n^{(\rm atm)}(\kappa)
\exp[-\kappa^2W^2(z)]
\left[1-\exp\left(-\frac{\Lambda_RL\kappa^2(1-z/L)^2}{k}\right)\right]
}
\]

其中：

\[
W(z)=W_0\sqrt{1+(z/z_R)^2},\qquad
W_0=16.25\ {\rm mm},
\]

\[
z_R=\pi W_0^2/\lambda,\qquad
W_R=W(L),\qquad
\Lambda_R=\frac{2L}{kW_R^2}.
\]

`Phi_n^(atm)` 使用 V6 finite-scale `Cn2=3e-15`, `L0=10 m`, `l0=5 mm`。

### quadrature convergence

reference 至少使用两档独立 numerical tolerances / refinement，并要求：

\[
\boxed{
|V_{\rm ref}^{(fine)}/V_{\rm ref}^{(coarse)}-1|<10^{-4}
}.
\]

若 reference 本身不能达到该收敛，则不得执行 empirical V6a acceptance。

---

## 8. V6 ensemble and seeds — PROPOSED

使用一个 fresh V6 validation ensemble：

\[
\boxed{N_{\rm V6}=1024}.
\]

seed 必须在任何 V6 result 出现前提交到未来 runner/metadata，并与 Gate A/B formal、diagnostic、future production seeds 不相交。

同一组 1024 path realizations同时服务：

- V6a baseline `P=9`；
- V6b paired `P=10` refinement。

不得看到 V6a 结果后换 seed。

建议记录 2000 次 screen-ID bootstrap 作为不确定度 diagnostic，但 Scientific Contract 当前 V6a/V6b formal gate 仍按冻结的 point-estimate relative difference 判定；本 proposal 不擅自把 bootstrap UB 新增为科学门限。

---

## 9. V6a formal acceptance

使用 `P=9`, `M_val=32`, fresh `N_V6=1024` 得到：

\[
V_{\rm bw,9}.
\]

与独立 spectral reference：

\[
V_{\rm bw,ref}=\langle r_c^2\rangle_{\rm ref}
\]

比较。

正式 criterion：

\[
\boxed{
\left|\frac{V_{\rm bw,9}}{V_{\rm bw,ref}}-1\right|\le10\%
}.
\]

PASS 后只说明 weakest-turbulence Gaussian beam-wander absolute normalization 得到 propagation-level 支持。

---

## 10. V6b low-frequency refinement — PROPOSED UNIQUE TEST

V6b 只测试一次**下一层** refinement：

\[
\boxed{P=9\rightarrow P=10}.
\]

不能把该测试变成事后搜索 P 的 ladder。

### paired construction

对每个 path、每个 screen：

- base FFT coefficients相同；
- SH levels `p=1..9` coefficients相同；
- refined path 只额外加入同一预登记 RNG sequence 生成的 `p=10` coefficients；
- screen placement、propagation、source完全相同。

因此 P9/P10 是 common-random-number paired comparison。

得到：

\[
V_{\rm bw,9},\qquad V_{\rm bw,10}.
\]

正式 criterion：

\[
\boxed{
\left|\frac{V_{\rm bw,10}}{V_{\rm bw,9}}-1\right|<5\%
}.
\]

若 PASS，保留 Gate-B qualified depth `P=9` 作为后续 validation baseline。

若 FAIL：

> **REVISE — LOW-FREQUENCY REPRESENTATION REQUIRES PROPAGATION-LEVEL REVIEW**

禁止自动采用 P=10、禁止继续 P=11/12 追求通过；下一步必须单独审查新的 low-frequency refinement contract。

---

## 11. V6 PASS rule

只有同时满足：

1. spectral reference quadrature convergence `<1e-4`；
2. V6 validation grid boundary guard PASS；
3. V6a absolute beam-wander disagreement `<=10%`；
4. V6b P9→P10 refinement change `<5%`；

才允许：

> **PASS — V6 BEAM-WANDER QUALIFIED**

该 PASS 仍不授权：

- V7 long-term radius；
- V8 scintillation；
- V9 production screen-number selection；
- production turbulence Monte Carlo；
- G1 production optimization；
- Bessel / OPB / flat-top；
- structured-field comparison。

下一阶段必须另行授权。

---

## 12. Explicitly prohibited implementation shortcuts

V6 implementation 不得：

- 用 empirical phase screens反算 spectral reference；
- 用 receiver aperture centroid代替 full-plane centroid；
- 把 jitter/boresight 加入 `rho_bw`；
- 在 piston removal 时减去 tilt / best-fit plane；
- 因 V6a FAIL 调 seed；
- 因 V6b FAIL 自动增加 P；
- 把 validation `M_val=32` 宣称为 production screen count；
- 进入 V7/V8/V9；
- 开放 structured fields。

---

## 13. External-review questions

本 proposal 请求外审只裁决以下 implementation choices，不重开 Gate-B physics：

1. V6a 使用 weakest-turbulence finite-scale G0 (`Cn2=3e-15`, `L0=10 m`, `l0=5 mm`) 是否正确对应 Scientific Contract；
2. production G0 带 Tx aperture，而 independent spectral reference 使用 underlying analytic Gaussian `W(z)`；鉴于 aperture 只截去约 0.879% 无穷平面 Gaussian power，这一 reference pairing 是否可接受，还是 V6a 应改成 validation-only unclipped Gaussian；
3. `M_val=32` 作为 validation-only longitudinal ceiling、由 V9 另行选择 production 4/8/16/32，是否正确解除 V6/V9 的循环依赖；
4. V6b 固定只做 paired `P=9→10` next-refinement test，FAIL 即停止而不自动搜索更深 P，是否足够严格；
5. `N_V6=1024`、formal gate 使用 Scientific Contract point estimate，同时 bootstrap 只作 uncertainty diagnostic，是否合适。

建议外审裁决格式：

> **PASS — AUTHORIZE V6 CORE IMPLEMENTATION**

或

> **REVISE — V6 IMPLEMENTATION CONTRACT**

在 PASS 前不得编写或执行 V6 simulation code。
