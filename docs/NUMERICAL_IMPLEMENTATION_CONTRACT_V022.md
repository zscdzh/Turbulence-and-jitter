# Numerical Implementation Contract v0.2.2 — Gate B Ensemble Remediation

**日期：2026-08-08**  
**状态：PASS — AUTHORIZE ONE FRESH 1024-SCREEN FORMAL V5 RERUN**  
**上位科学合同：Scientific Contract v0.3.2（保持冻结）**  
**Gate A：V0–V3 PASS / unchanged**  
**V6–V12：NOT YET AUTHORIZED**  
**Structured-field implementation：NOT AUTHORIZED**

本文件自本日期起成为 Gate B / V4–V5 的唯一 authoritative implementation contract。它继承 v0.2.1 已通过外审的 physics / PSD / FFT / Hermitian / subharmonic / deterministic-selection 定义，只修改 **formal empirical ensemble size 与一次性止损治理规则**。

原 v0.2 / P*=6 formal failure、v0.2.1 / P*=9 512-screen formal failure，以及事后 1024-screen continuation diagnostic 必须永久保留，均不得覆盖或重解释为 PASS。

---

## 1. Remediation origin

v0.2.1 已修复原 P=6 deterministic low-frequency margin 问题，并按 frozen minimum-depth deterministic bias-headroom policy 自动选择：

\[
P_*=9.
\]

v0.2.1 fresh 512-screen formal rerun 中：

- V4 regression PASS；
- finite-scale V5 三方向 PASS；
- Kolmogorov y / 45° recovery、amplitude、slope PASS；
- Kolmogorov x implementation-recovery 95% UB = 5.778% > 5%；
- Kolmogorov x amplitude 95% UB = 11.042% > 10%。

P=9 deterministic expectation 已满足 v0.2.1 representation guards，因此该次失败不要求重开 PSD normalization、FFT convention、Hermitian ownership 或 subharmonic coefficient formula。

正式 FAIL 后，保持同一 P=9、同一 Kolmogorov screen seed、保留前512张并继续同一 RNG sequence 到累计1024张。该事后 diagnostic 显示 empirical statistics 随 ensemble 增大向 `D_disc,9` 收敛，但它只能支持一次新的 fresh 1024 rerun，不能 retroactively qualify v0.2.1。

---

## 2. Scientific and numerical definitions — unchanged

以下全部保持 v0.2.1：

- validation slab：`lambda=1550 nm`, `Cn2=1e-14 m^(-2/3)`, `Delta z=125 m`；
- finite-scale：`L0=10 m`, `l0=5 mm`；
- qualification grid：`N=512`, `dx=1.015625 mm`, `Lwin=0.520 m`；
- cycles/m ↔ rad/m mapping；
- atmospheric / mathematical PSD normalization；
- NumPy `norm="backward"` FFT/IFFT normalization；
- base-FFT Hermitian ownership 与 self-conjugate-bin handling；
- recursive 3x3 subharmonic coefficient formula；
- valid/non-wrapped structure-function estimator；
- x / y / 45° frozen direction sets；
- finite-scale independent continuous quadrature；
- analytic Kolmogorov reference；
- V4 annuli、V4 estimator 与 V4 thresholds。

任何实现与这些定义不一致时，应修实现，不得借 v0.2.2 修改 physics contract。

---

## 3. Deterministic P-selection — unchanged

P ladder：

\[
\boxed{P=0,1,\ldots,12}.
\]

对 finite-scale / Kolmogorov 与 x / y / 45° 分别检查。

### median bias headroom

\[
\boxed{
\operatorname{median}_\rho
\left|\frac{D_{\rm disc,P}-D_{\rm ref}}{D_{\rm ref}}\right|
\le6\%
}
\]

### pointwise tail guard

\[
\boxed{
\max_\rho
\left|\frac{D_{\rm disc,P}-D_{\rm ref}}{D_{\rm ref}}\right|
\le10\%
}
\]

### Kolmogorov slope guard

\[
\boxed{|s_{\rm disc}-5/3|\le0.08}.
\]

选择满足全部条件的**最小** P。

policy 名称保持：

> **minimum-depth deterministic bias-headroom policy**

该 policy 不直接计算或优化 stochastic variance，也不声称某个 P 是 bias–variance optimum。

若 P<=12 无值通过，则立即：

> **REVISE — LOW-FREQUENCY REPRESENTATION**

并禁止进行 empirical rerun。

---

## 4. Historical diagnostic evidence — not qualification

以下均永久标记 diagnostic-only：

- P=8 / 9 / 12 remediation diagnostics；
- v0.2.1 formal FAIL 后的 same-seed 512→1024 continuation；
- 其 bootstrap 与 prefix convergence results。

1024 continuation 的唯一可复现入口：

- `scripts/run_gate_b_postfailure_1024_diagnostic.py`

该 runner 必须记录：

- source commit / source blob SHAs；
- Python / NumPy / SciPy versions；
- screen seed；
- bootstrap seed；
- bootstrap count；
- bootstrap unit 与 shared-weight rule；
- per-screen structure-function observables 输出路径。

它不得使用 fresh v0.2.2 seeds，也不得作为 v0.2.2 formal PASS evidence。

---

## 5. v0.2.2 fresh formal seed rule — ONE ATTEMPT ONLY

v0.2.2 只授权**一个**全新的 formal seed family。

在生成任何 v0.2.2 formal screen 之前，必须先把固定整数 seeds 提交到 runner / metadata，至少包括：

- V4 regression screen seed；
- finite formal screen seed；
- Kolmogorov formal screen seed；
- finite bootstrap seed；
- Kolmogorov bootstrap seed。

这些 seeds 必须与以下全部不相交：

- 原 v0.2 / P=6 formal seeds；
- P=8/9/12 remediation diagnostic seeds；
- v0.2.1 / P=9 512-screen formal seeds；
- v0.2.1 post-failure 1024 diagnostic bootstrap seed；
- Gate A / core diagnostic seeds；
- future production seeds。

**一旦该 seed family 被提交，即冻结。**

禁止：

- 看见结果后换 seed；
- 用第二套 fresh 1024 seed family 重试；
- 挑选“更好看”的 seed family。

---

## 6. Formal empirical ensemble — NEW AUTHORITATIVE RULE

v0.2.2 唯一 formal ensemble：

\[
\boxed{N_{\rm ens}=1024}.
\]

允许保留 nested prefixes 作为 convergence diagnostics，例如：

\[
N=256,512,768,1024.
\]

但：

- 所有 `N<1024` 只能 diagnostic；
- 不得 early PASS；
- 不得因某个 prefix FAIL 提前改变 seed 或 representation；
- 正式裁决只使用完整 1024 screens。

finite-scale 与 Kolmogorov 均统一使用 1024 formal screens。

不保存完整 raw phase-screen archive；只保存按 screen ID 索引的 x / y / 45° `D_phi(rho)` observables 及必要 metadata。

---

## 7. Bootstrap — unchanged except ensemble size

\[
\boxed{B_{\rm boot}=2000}.
\]

bootstrap unit 仍为 screen ID。

对每个 case：

1. 用冻结 bootstrap seed 生成一套 `2000 x 1024` screen-ID resample-count weights；
2. 同一 case 的 x / y / 45° 共用完全相同的 weights；
3. 每个 resample 有放回抽取 1024 screen IDs；
4. 重算 ensemble-mean `D(rho)`；
5. 重算 median relative error；
6. Kolmogorov case 重算 log-log slope。

单侧 95% upper bound：2000 statistics 的 95th percentile。  
slope 95% CI：2.5th–97.5th percentile。  
percentile method：NumPy `linear`。

---

## 8. Formal V5 thresholds — unchanged

### implementation recovery

x / y / 45° 分别要求：

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

所有 formal criteria 必须同时 PASS。

---

## 9. v0.2.2 PASS rule

只有同时满足：

- V4 regression sanity PASS；
- deterministic P-selection PASS；
- finite x/y/45° implementation recovery PASS；
- finite x/y/45° amplitude PASS；
- Kolmogorov x/y/45° implementation recovery PASS；
- Kolmogorov x/y/45° amplitude PASS；
- Kolmogorov x/y/45° slope PASS；

才允许：

> **PASS — GATE B V4–V5 QUALIFIED**

随后仍必须等待项目负责人明确授权，才能进入 V6。

Gate-B PASS 本身不自动启动 V6。

---

## 10. ONE-SHOT STOP-LOSS RULE

如果这一组**唯一 fresh 1024-screen seed family**在任一 formal criterion 上 FAIL，则正式裁决必须是：

> **REVISE — GATE B NOT QUALIFIED AFTER v0.2.2 ENSEMBLE REMEDIATION**

并立即停止 ensemble-size escalation。

明确禁止：

- 更换 seed 再跑另一组 1024；
- 将同一序列继续到 1280 / 1536 / 2048 以争取 PASS；
- 把 1024 formal FAIL 后的更大-N continuation 用作 retroactive qualification；
- 再通过改变 deterministic headroom threshold 追求通过。

若 v0.2.2 fresh 1024 仍 FAIL，下一步必须进入独立审查，二选一或组合审查：

1. **low-frequency representation review**：是否需要更密 / 不同的低频随机场表示；
2. **qualification-statistic review**：当前方向分离的 median-error + bootstrap criterion 是否是合理且稳定的 screen-level qualification statistic。

在该审查完成前，不得继续扩大 ensemble，也不得进入 V6。

---

## 11. Historical evidence retention

必须永久保留并明确标记：

1. v0.2 / P=6 formal FAIL；
2. v0.2.1 remediation diagnostics；
3. v0.2.1 / P=9 512-screen formal FAIL；
4. post-failure same-seed 1024 continuation diagnostic；
5. v0.2.2 fresh 1024 formal result，无论 PASS 或 FAIL。

任何新结果不得覆盖上述目录或重写历史 decision。

---

## 12. Piston note for future V6 — NON-BLOCKING

较深 Kolmogorov subharmonics 可产生很大的无物理意义 piston。

未来若 Gate B PASS 并明确授权进入 propagation-level V6，在构造传播相位因子前应对每张总相位屏执行：

\[
\phi\leftarrow\phi-\langle\phi\rangle.
\]

这里只移除 spatial mean / piston，不移除 tilt，不改变 structure function 或强度物理量。

该条是 V6 numerical-hygiene note，不属于本次 Gate-B v0.2.2 formal rerun 的 acceptance condition。

---

## 13. Authorization boundary

本合同授权且仅授权：

> **一次 fresh, preregistered, 1024-screen Gate-B formal V5 rerun。**

仍不授权：

- V6 beam wander；
- V7 long-term radius；
- V8 scintillation；
- production multi-screen propagation；
- G1 production optimization；
- Bessel / OPB / flat-top implementation；
- structured-field Monte Carlo；
- Paper-2 joint optimization。

Scientific Contract v0.3.2 保持冻结。
