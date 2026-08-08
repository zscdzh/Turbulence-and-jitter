# Numerical Implementation Contract v0.2.1 — Gate B Remediation

**日期：2026-08-08**  
**状态：AUTHORIZED FOR ONE FRESH FORMAL V5 RERUN**  
**上位科学合同：Scientific Contract v0.3.2（保持冻结）**  
**Gate A：V0–V3 PASS / unchanged**  
**V6–V12：NOT YET AUTHORIZED**  
**Structured-field implementation：NOT AUTHORIZED**

本文件是从本日期起 Gate B / V4–V5 的唯一 authoritative implementation contract。它取代 `docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V02.md` 作为 Gate-B 执行依据；v0.2 保留为历史记录，用于解释原 `P*=6` formal failure。Scientific Contract v0.3.2、PSD normalization、FFT convention、Hermitian ownership 与 phase-screen random-coefficient definition 均不修改。

## 1. Remediation origin

Gate-B v0.2 正式运行中，V4、finite-scale V5、Kolmogorov implementation recovery 与 slope 均 PASS；Kolmogorov amplitude 仅 x PASS，y/45° FAIL。失败属于 C 类：generator 能恢复 `D_disc,6`，但 `D_disc,6` 相对连续 Kolmogorov reference 在较大 separation 上存在系统性负偏差。原 `8% median` deterministic guard 不能排除 tail bias 已超过正式 10% amplitude budget。

因此 v0.2.1 只修订 **low-frequency representation qualification / P-selection policy**。PSD、FFT、Hermitian、random-coefficient normalization、subharmonic coefficient formula、continuous references、formal ensemble 和 formal acceptance thresholds 均不修改。

## 2. Validation slab and grid

`lambda=1550 nm`, `Cn2=1e-14 m^(-2/3)`, `Delta z=125 m`, finite-scale `L0=10 m`, `l0=5 mm`。

`N=512`, `dx=1.015625 mm`, `Lwin=0.520 m`, `df=1/Lwin`。该 grid 仅用于 screen-level qualification。

## 3. PSD / FFT / Hermitian — unchanged

内部频率为 cycles/m，`kappa=2*pi*f`，且

\[
S_\phi(f_x,f_y)=\Phi_\phi^{(math)}(2\pi f_x,2\pi f_y).
\]

ordinary cell：

\[
E|a_{uv}|^2=S_\phi\Delta f^2,
\qquad
a_{uv}=\Delta f\sqrt{S_\phi}\xi,
\qquad
F_{uv}=N^2a_{uv}.
\]

每个 conjugate pair 只抽样一次，partner 由 `a(-u,-v)=conj(a(u,v))` 填充。DC piston 为零。Kolmogorov qualification 继续使用独立解析 spectrum branch。

## 4. V4 — unchanged

V4 只验证 base FFT spectrum。resolved band `4/Lwin` 至 `0.20/dx`，12 个 `geomspace` annuli，每环至少20 pixels。128 independent screens。

formal criteria：PSD annular median level error `<=10%`；numerical vs exact modified-von-Karman target slope difference `<=0.10`。

v0.2.1 不修改 base FFT implementation，fresh rerun 只要求 V4 regression sanity。

## 5. Subharmonic representation — unchanged

第 p 层：

\[
\Delta f_p=\Delta f/3^p.
\]

完整 3x3 low-frequency set 去掉 central cell；只对 `(1,0),(0,1),(1,1),(1,-1)` 四个 independent cells 抽样，另四个由共轭生成。完整八点只计数一次。

## 6. Deterministic structure function — unchanged

\[
D_{disc,P}=D_{FFT}+D_{SH,P},
\]

其中所有正负频率已完整计入，不得再额外乘共轭倍数。

x/y shifts：`[4,5,7,9,11,14,18,23,30,39,50,64]`；45° shifts：`[3,4,5,6,8,10,13,16,21,28,35,45]`。三个方向分别报告；empirical estimator 禁止 periodic roll。

finite reference 继续使用 independent atmospheric-measure quadrature，relative convergence `<1e-4`。Kolmogorov reference：

\[
D_K(\rho)=6.88(\rho/r_{0,screen})^{5/3}.
\]

## 7. v0.2.1 deterministic selection — NEW AUTHORITATIVE RULE

P ladder：

\[
\boxed{P=0,1,\ldots,12}.
\]

实际 deterministic calculation 决定 P*，不得写死。

对 finite/Kolmogorov、x/y/45° 分别要求：

### A. median bias headroom

\[
\boxed{
\operatorname{median}_\rho
\left|\frac{D_{disc,P}-D_{ref}}{D_{ref}}\right|\le6\%
}.
\]

6% 是原 P=6 formal failure 后明确引入的 remediation threshold，不是事前阈值或普适物理常数；其用途是在 formal 10% amplitude UB budget 下为 512-screen finite-sample uncertainty 预留 headroom。

### B. pointwise tail guard

\[
\boxed{
\max_\rho
\left|\frac{D_{disc,P}-D_{ref}}{D_{ref}}\right|\le10\%
}.
\]

### C. Kolmogorov slope guard

\[
\boxed{|s_{disc}-5/3|\le0.08}.
\]

选择满足 A+B+C 的**最小** P。本 policy 称为 **minimum-depth deterministic bias-headroom policy**；它不优化或声称优化 stochastic variance。

若 `P<=12` 无任何值满足，则停止并裁决 `REVISE — LOW-FREQUENCY REPRESENTATION`。

## 8. Diagnostic evidence exclusion

remediation diagnostic seeds：P8 `(2026080821,2026080822)`；P9 `(2026080823,2026080824)`；P12 `(2026080825,2026080826)`，分别为 screen/bootstrap seed。这些 seeds 永久 diagnostic-only，不得用于 formal rerun。

诊断 runner：`scripts/run_gate_b_p_depth_diagnostic.py`；summary：`results/gate_b_p_depth_diagnostic/metadata.json`、`diagnostic_summary.json`。

原 P=6 formal failure 及其 seeds/results 永久保留，不覆盖。

## 9. Fresh formal rerun seeds

新 formal rerun 必须在生成任何 screen 前登记全新且不与原 formal / diagnostic / future production seed families 相交的：finite screen、Kolmogorov screen、finite bootstrap、Kolmogorov bootstrap seeds。不得看到结果后换 seed。

## 10. Formal empirical ensemble and bootstrap — unchanged

128/256 仅 nested diagnostics；唯一 formal ensemble：`N_ens=512`。不得 early PASS 或失败后擅自扩大 ensemble。

只保存 per-screen x/y/45° `D_phi(rho)` observables，不保存完整 512 张 phase arrays。

bootstrap：`B_boot=2000`，unit=screen ID。每个 case 先生成同一套 `2000 x 512` resample-count weights，x/y/45° 三方向共享。95% UB=95th percentile；slope CI=2.5th–97.5th percentile。

## 11. Formal V5 criteria — unchanged

- implementation recovery：x/y/45° 各自 95% UB `<=5%`；
- finite-scale amplitude：x/y/45° 各自 95% UB `<=10%`；
- Kolmogorov amplitude：x/y/45° 各自 95% UB `<=10%`；
- Kolmogorov slope：三方向 95% CI 完整位于 `5/3 ± 0.10`。

全部 PASS 才能裁决 `PASS — GATE B V4–V5 QUALIFIED`。任一 FAIL：`REVISE — GATE B NOT YET QUALIFIED`。不得通过改 seed、阈值、ensemble 或事后改 P 修复。

## 12. V6 boundary and piston hygiene

Gate B PASS 也不自动授权 V6–V12。若后续负责人授权传播层，在计算 `exp(i*phi)` 前可做：

\[
\phi\leftarrow\phi-\langle\phi\rangle,
\]

只移除 spatial piston，不移除 tilt，不改变 structure function 或 intensity physics。

## 13. Authorization

> **AUTHORIZED — ONE FRESH GATE-B v0.2.1 FORMAL V5 RERUN**

仍禁止 V6–V12、production multi-screen、G1 production optimization、Bessel/OPB/flat-top 和 structured-field comparison。
