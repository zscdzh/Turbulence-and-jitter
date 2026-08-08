# Numerical Implementation Contract v0.2.1 — Gate B Remediation

**日期：2026-08-08**  
**状态：AUTHORIZED FOR ONE FRESH FORMAL V5 RERUN**  
**上位科学合同：Scientific Contract v0.3.2（保持冻结）**  
**Gate A：V0–V3 PASS / unchanged**  
**V6–V12：NOT YET AUTHORIZED**  
**Structured-field implementation：NOT AUTHORIZED**

本文件是从本日期起 Gate B / V4–V5 的唯一 authoritative implementation contract。它取代 `docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V02.md` 作为 Gate-B 执行依据；v0.2 保留为历史记录，用于解释原 `P*=6` formal failure。Scientific Contract v0.3.2、PSD normalization、FFT convention、Hermitian ownership 与 phase-screen random-coefficient definition 均不修改。

---

## 1. Remediation origin

Gate-B v0.2 正式运行得到：

- Gate A V0–V3：PASS；
- V4：PASS；
- deterministic ladder：原规则选择 `P*=6`；
- finite-scale formal V5：PASS；
- Kolmogorov implementation recovery：PASS；
- Kolmogorov slope：PASS；
- Kolmogorov amplitude：x PASS，y/45° FAIL。

原失败属于 C 类：generator 能恢复 `D_disc,6`，但 `D_disc,6` 相对连续 Kolmogorov reference 在较大 separation 上存在系统性负偏差。原 `8% median` deterministic guard 不能排除尾部 deterministic bias 已超过正式 10% budget。

因此 v0.2.1 只修订 **low-frequency representation qualification / P-selection policy**。

不修改：

- modified-von-Kármán / Kolmogorov PSD；
- atmospheric ↔ mathematical Fourier normalization；
- cycles/m ↔ rad/m mapping；
- FFT/IFFT normalization；
- Hermitian coefficient ownership；
- self-conjugate-bin treatment；
- subharmonic coefficient formula；
- finite/Kolmogorov references；
- formal ensemble size；
- formal bootstrap；
- Scientific Contract 10% / slope thresholds。

---

## 2. Validation slab and grid — unchanged

\[
\lambda=1550\,\mathrm{nm},\qquad
C_n^2=10^{-14}\,\mathrm{m^{-2/3}},\qquad
\Delta z=125\,\mathrm m.
\]

finite-scale case：

\[
L_0=10\,\mathrm m,\qquad l_0=5\,\mathrm{mm}.
\]

qualification grid：

\[
N=512,
\qquad
\Delta x=1.015625\,\mathrm{mm},
\qquad
L_{\rm win}=0.520\,\mathrm m,
\qquad
\Delta f=1/L_{\rm win}.
\]

Kolmogorov screen Fried parameter：

\[
r_{0,\rm screen}=[0.423k_0^2C_n^2\Delta z]^{-3/5}.
\]

该 grid 仅用于 screen-level qualification，不是 production grid。

---

## 3. PSD convention — unchanged

内部 Fourier frequency 使用：

\[
f_x,f_y\quad[\mathrm{cycles/m}],
\]

并映射：

\[
\kappa_x=2\pi f_x,
\qquad
\kappa_y=2\pi f_y.
\]

cycles-grid mathematical PSD：

\[
\boxed{
S_\phi(f_x,f_y)
=
\Phi_\phi^{(\rm math)}(2\pi f_x,2\pi f_y)
}
\]

因为：

\[
\frac{d^2\kappa}{(2\pi)^2}=d^2f.
\]

不得额外乘除 `(2pi)^2`。

finite-scale spectrum 使用 Scientific Contract v0.3.2 的 modified-von-Kármán definition。Kolmogorov qualification 必须使用独立解析 branch：

\[
\Phi_n^{(K)}(\kappa)=0.033C_n^2\kappa^{-11/3},\qquad \kappa>0,
\]

DC 置零，不通过 `L0=inf` / `l0=0` 数值参数模拟。

---

## 4. Base-FFT coefficients and Hermitian ownership — unchanged

对 ordinary Fourier cell：

\[
E|a_{uv}|^2=S_\phi(f_u,f_v)\Delta f^2,
\]

\[
a_{uv}=\Delta f\sqrt{S_\phi}\,\xi,
\qquad
\xi=(X+iY)/\sqrt2,
\qquad X,Y\overset{\rm iid}{\sim}\mathcal N(0,1).
\]

NumPy `norm="backward"` 二维 inverse FFT 使用：

\[
F_{uv}=N^2a_{uv}.
\]

每个 conjugate pair 只抽样一次，另一半完全由：

\[
a_{-u,-v}=a_{uv}^*
\]

填充。

四个 self-conjugate bins：

\[
(0,0),\ (-N/2,0),\ (0,-N/2),\ (-N/2,-N/2).
\]

DC piston 为零，其余三个 Nyquist self-conjugate bins 使用保持相同 cell variance 的实 Gaussian。

---

## 5. V4 — unchanged

V4 只验证 base FFT spectrum，不使用 subharmonics。

resolved band：

\[
f_{\min}=4/L_{\rm win},
\qquad
f_{\max}=0.20/\Delta x.
\]

12 个 annuli：

\[
e_k=\operatorname{geomspace}(f_{\min},f_{\max},13),
\qquad
f_k=\sqrt{e_ke_{k+1}}.
\]

每个 annulus 至少 20 pixels。numerical 与 exact target 使用相同 annulus membership。

单-bin PSD estimator：

\[
\widehat S_\phi=
\frac{\langle|F^{(\rm rec)}|^2\rangle}{N^4\Delta f^2}.
\]

V4 使用 128 independent base-FFT screens。

formal criteria：

\[
\operatorname{median}_k\left|\widehat S_k/S_{k,\rm target}-1\right|\le10\%,
\]

\[
|s_{\rm num}-s_{\rm target}|\le0.10.
\]

v0.2.1 不修改 base FFT implementation，因此 fresh formal V5 rerun 只要求 V4 regression sanity；原 V4 PASS 仍保留。

---

## 6. Recursive subharmonics — unchanged formula

第 p 层：

\[
\Delta f_p=\Delta f/3^p.
\]

完整八点：

\[
(i,j)\in\{-1,0,1\}^2\setminus\{(0,0)\}.
\]

只对：

\[
\mathcal H_{\rm SH}=\{(1,0),(0,1),(1,1),(1,-1)\}
\]

四个 independent cells 抽样，其余四个由共轭生成。

\[
a_{ij}^{(p)}=
\Delta f_p\sqrt{S_\phi(i\Delta f_p,j\Delta f_p)}\,\xi_{ij}^{(p)}.
\]

完整 real-space layer 必须包含八个 frequency cells；填满八点后禁止再次使用额外 `2*Re(...)` 重复计数。

---

## 7. Deterministic structure function — unchanged definition

\[
D_{\rm FFT}(\boldsymbol\rho)=
2\sum_{q\in\rm FFT}S_q\Delta f^2
[1-\cos(2\pi q\cdot\boldsymbol\rho)],
\]

\[
D_{\rm SH,P}(\boldsymbol\rho)=
2\sum_{p=1}^{P}\sum_{q\in\rm SH_p}
S_q\Delta f_p^2
[1-\cos(2\pi q\cdot\boldsymbol\rho)],
\]

\[
\boxed{D_{\rm disc,P}=D_{\rm FFT}+D_{\rm SH,P}}.
\]

完整正负频率均已包含，不得再次补共轭倍数。

---

## 8. Frozen directions — unchanged

+x / +y axial pixel shifts：

`[4,5,7,9,11,14,18,23,30,39,50,64]`。

45° shifts：

`[3,4,5,6,8,10,13,16,21,28,35,45]`，实际 radial separation 为 `sqrt(2)*n*dx`。

三个方向必须分别报告和验收。empirical structure function 只使用 valid/non-wrapped pairs，禁止 periodic `roll`。

---

## 9. Continuous references — unchanged

finite-scale independent atmospheric-measure reference：

\[
D_{\phi,\rm finite}(\rho)=
4\pi\int_0^\infty
\kappa\Phi_\phi^{(\rm atm)}(\kappa)
[1-J_0(\kappa\rho)]d\kappa.
\]

对全部冻结 separation，quadrature relative convergence 必须 `<1e-4`。

Kolmogorov absolute reference：

\[
\boxed{
D_{\phi,K}(\rho)=6.88(\rho/r_{0,\rm screen})^{5/3}
}.
\]

---

## 10. v0.2.1 deterministic selection — NEW AUTHORITATIVE RULE

P ladder 扩展为：

\[
\boxed{P=0,1,\ldots,12}.
\]

实际计算决定 P*；不得预先写死任何深度。

对每个 P，finite-scale 与 Kolmogorov、x/y/45° 分别检查。

### A. median bias headroom

\[
\boxed{
\operatorname{median}_\rho
\left|\frac{D_{\rm disc,P}-D_{\rm ref}}{D_{\rm ref}}\right|
\le6\%
}
\]

该 6% 是原 P=6 formal failure 后明确引入的 remediation threshold，不是事前阈值或物理常数。其用途是在 Scientific Contract 的 formal 10% amplitude upper-bound budget 下，为 512-screen finite-sample uncertainty 预留 implementation headroom。

### B. pointwise tail guard

\[
\boxed{
\max_\rho
\left|\frac{D_{\rm disc,P}-D_{\rm ref}}{D_{\rm ref}}\right|
\le10\%
}
\]

用于防止 median criterion 掩盖长-separation tail bias。

### C. Kolmogorov slope guard

\[
\boxed{|s_{\rm disc}-5/3|\le0.08}.
\]

选择满足 A+B+C 的**最小** P。

本 policy 名称为：

> **minimum-depth deterministic bias-headroom policy**

它不优化或声称优化 stochastic variance。不同 P 的单组 diagnostic samples 不能建立 variance 随 P 单调变化的结论。

若 P<=12 无值满足，则：

> **REVISE — LOW-FREQUENCY REPRESENTATION**

并停止 formal empirical rerun。

---

## 11. Diagnostic evidence and seed exclusion

remediation diagnostic 使用：

- P=8 screens `2026080821`, bootstrap `2026080822`；
- P=9 screens `2026080823`, bootstrap `2026080824`；
- P=12 screens `2026080825`, bootstrap `2026080826`。

这些 seeds 永久标记为 diagnostic-only，不得用于 v0.2.1 formal rerun。

诊断 runner：

- `scripts/run_gate_b_p_depth_diagnostic.py`

机器 summary：

- `results/gate_b_p_depth_diagnostic/metadata.json`
- `results/gate_b_p_depth_diagnostic/diagnostic_summary.json`

原 P=6 formal failure 的所有 seeds / results 同样永久保留，不得覆盖。

---

## 12. Fresh formal rerun seeds

v0.2.1 formal rerun 必须在生成任何新 formal screen 前，把一组**全新且与以下全部 seed families 不相交**的整数 seeds 写入新的 metadata：

- 原 P=6 formal seeds；
- P=8/9/12 remediation diagnostic seeds；
- Gate A / V4 / core diagnostic seeds；
- future production seeds。

至少独立登记：

- finite formal screen seed；
- Kolmogorov formal screen seed；
- finite bootstrap seed；
- Kolmogorov bootstrap seed。

不得看到结果后更换 seed。

---

## 13. Formal empirical ensemble — unchanged

128 / 256 只可作为 nested convergence diagnostics。

唯一 formal ensemble：

\[
\boxed{N_{\rm ens}=512}.
\]

不得 early PASS，也不得 formal FAIL 后擅自扩大到 1024 / 2048。

不保存 512 张 raw phase screens；只保存 formal bootstrap 所需 per-screen x/y/45° `D_phi(rho)` observables。

---

## 14. Bootstrap — unchanged and unique

\[
\boxed{B_{\rm boot}=2000}.
\]

bootstrap unit 是 screen ID。

对每个 case 先按 bootstrap seed 生成一套 `2000 x 512` resample-count weights；同一 case 的 x/y/45° 方向共享这套 weights。

每个 resample：

1. 有放回抽取 512 screen IDs；
2. 重新计算 ensemble-mean `D(rho)`；
3. 计算跨 rho 的 median relative error；
4. Kolmogorov case 重新拟合 slope。

单侧 95% upper bound 为 2000 statistics 的 95th percentile；slope CI 为 2.5th–97.5th percentile。

---

## 15. Formal V5 criteria — unchanged

### implementation recovery

三方向分别：

\[
\boxed{
95\%\,UB\left[
\operatorname{median}_\rho
\left|\frac{D_{\rm emp}-D_{\rm disc,P_*}}{D_{\rm disc,P_*}}\right|
\right]\le5\%
}.
\]

### finite-scale amplitude

三方向分别：

\[
\boxed{
95\%\,UB\left[
\operatorname{median}_\rho
\left|\frac{D_{\rm emp}-D_{\rm finite,ref}}{D_{\rm finite,ref}}\right|
\right]\le10\%
}.
\]

### Kolmogorov amplitude

三方向分别：

\[
\boxed{
95\%\,UB\left[
\operatorname{median}_\rho
\left|\frac{D_{\rm emp}-D_K}{D_K}\right|
\right]\le10\%
}.
\]

### Kolmogorov slope

三方向 bootstrap 95% CI 必须完整位于：

\[
\boxed{5/3\pm0.10}.
\]

---

## 16. Gate-B v0.2.1 decision

只有：

- V4 regression sanity PASS；
- deterministic v0.2.1 policy 成功选择 P*；
- finite implementation recovery + amplitude 三方向 PASS；
- Kolmogorov implementation recovery + amplitude + slope 三方向 PASS；

才允许：

> **PASS — GATE B V4–V5 QUALIFIED**

并且只允许项目负责人进一步决定是否授权 V6。

任一 formal criterion FAIL：

> **REVISE — GATE B NOT YET QUALIFIED**

不得通过改 seed、扩大 ensemble、调整 threshold 或事后改 P 修复结果。

---

## 17. V6 boundary and piston hygiene

即使 v0.2.1 Gate B PASS，也不自动授权 V6–V12。

若后续项目负责人授权传播层，在计算：

\[
e^{i\phi(x,y)}
\]

前，可对每张 total phase screen 移除 spatial mean piston：

\[
\boxed{
\phi\leftarrow\phi-\langle\phi\rangle
}.
\]

该操作不改变 structure function，不移除 tilt，也不改变 intensity physics；它只是避免很深 Kolmogorov subharmonics 带来的无意义大常数相位进入传播计算。

---

## 18. Final authorization boundary

从本合同起：

> **AUTHORIZED — ONE FRESH GATE-B v0.2.1 FORMAL V5 RERUN**

仍明确禁止：

- V6 beam-wander qualification；
- V7 long-term-radius qualification；
- V8 scintillation qualification；
- V9–V12；
- production multi-screen propagation；
- Gaussian G1 production optimization；
- Bessel / OPB / flat-top implementation；
- structured-field comparison。
