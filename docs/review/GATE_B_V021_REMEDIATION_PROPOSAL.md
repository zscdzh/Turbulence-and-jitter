# Gate B v0.2.1 Remediation Proposal — External Review Draft

**日期：2026-08-08**  
**状态：PROPOSED FOR EXTERNAL REVIEW — DO NOT AUTHORIZE FORMAL RERUN YET**  
**上位合同：Scientific Contract v0.3.2（保持冻结）**  
**当前正式结果：REVISE — GATE B NOT YET QUALIFIED**

本文件针对 `docs/results/GATE_B_V4_V5_FORMAL_RESULTS.md` 中已确认的 C 类失败提出修订方案。当前不修改 Scientific Contract，不推翻 Gate A，不修改 phase-screen PSD / FFT / Hermitian / subharmonic coefficient normalization，也不授权 V6。

---

## 1. 已定位的失败

正式 P=6 qualification 中：

- V4 PASS；
- finite-scale V5 PASS；
- Kolmogorov implementation recovery PASS；
- Kolmogorov slope PASS；
- Kolmogorov amplitude x PASS；
- Kolmogorov amplitude y / 45° FAIL。

失败原因不是 generator 无法恢复自身离散期望，而是 `D_disc,6` 相对连续 Kolmogorov reference 的负偏差随 separation 增大。现有 `8% median` deterministic guard 只约束中位误差，不能排除冻结 separation 区间尾部已存在 >10% 的 deterministic bias。

因此修订对象应是 **low-frequency representation qualification / P-selection policy**，而不是 phase-screen 核心公式。

---

## 2. 新增诊断：仅加 pointwise 10% guard 不够稳

将 deterministic ladder 扩展后：

| P | K median x/y | K median 45° | K max x/y | K max 45° |
|---:|---:|---:|---:|---:|
| 6 | 7.749% | 7.784% | 12.357% | 12.218% |
| 7 | 6.755% | 6.785% | 10.776% | 10.640% |
| 8 | 6.066% | 6.092% | 9.679% | 9.546% |
| 9 | 5.588% | 5.611% | 8.919% | 8.787% |
| 10 | 5.256% | 5.278% | 8.392% | 8.261% |
| 11 | 5.026% | 5.047% | 8.027% | 7.896% |
| 12 | 4.867% | 4.887% | 7.773% | 7.643% |

若只增加：

\[
\max_\rho |D_{\rm disc,P}/D_{\rm ref}-1|\le10\%,
\]

则会自动选择 P=8。

但独立 diagnostic-only 512-screen P=8 run（非正式 seeds，1000 bootstrap，仅用于修订诊断）得到：

- x amplitude point ≈ 7.80%，diagnostic 95% UB ≈ 10.22%；
- y amplitude point ≈ 8.12%，diagnostic 95% UB ≈ 10.34%；
- 45° amplitude point ≈ 5.90%，diagnostic 95% UB ≈ 8.52%。

因此“pointwise deterministic ≤10%”虽然修复了 P=6 的尾部漏洞，但对 formal 10% upper-bound criterion 仍缺乏稳定统计余量。

---

## 3. 不建议简单使用更深 P 的原因

低频深度增加会降低 deterministic bias，但也会增加超低频 realization-to-realization variance。在固定 `N_ens=512` 下，过深 representation 可能反过来提高 empirical implementation-recovery uncertainty。

独立 diagnostic-only P=12 run 得到：

- deterministic K median ≈ 4.87%；
- deterministic K max ≈ 7.77%；
- amplitude diagnostic 95% UB 约 5.4%–7.4%；
- 但 y direction implementation-recovery diagnostic 95% UB ≈ 5.01%，已经贴近冻结 5% gate。

因此不能采用“P 越深越好”的规则。

这表明当前问题是一个实际的 **representation bias — finite-ensemble variance tradeoff**。

---

## 4. P=9 的独立 diagnostic 结果

使用新的 diagnostic-only seed family，对 P=9 运行 512 screens + 1000 bootstrap（不作为正式 PASS 证据）：

### point estimates

- x: implementation ≈ 0.70%，continuous K amplitude ≈ 6.28%，slope ≈ 1.64696；
- y: implementation ≈ 0.48%，continuous K amplitude ≈ 6.05%，slope ≈ 1.64683；
- 45°: implementation ≈ 0.71%，continuous K amplitude ≈ 6.31%，slope ≈ 1.64705。

### diagnostic bootstrap

- implementation 95% UB: x ≈ 3.41%，y ≈ 3.16%，45° ≈ 3.63%；
- amplitude 95% UB: x ≈ 8.68%，y ≈ 8.48%，45° ≈ 8.93%；
- slope 95% intervals 均位于 `5/3 ± 0.10` 内。

该结果表明 P=9 在当前 grid / 512-screen sample size 下同时具有更好的 deterministic bias margin 和合理的 empirical variance。

**但 P=9 不能被直接写死。** 需要先冻结一个可解释、预注册的 selection rule，再由 deterministic calculation 自动选出 P。

---

## 5. 推荐外审的 R3 selection policy

建议把 P ladder 扩展为：

\[
P=0,1,\ldots,12.
\]

保留原有：

- three-direction finite-scale checks；
- three-direction Kolmogorov checks；
- Kolmogorov slope guard `|s-5/3| <= 0.08`。

将 amplitude representation guard 从单一 median rule 修订为两级 bias budget：

### A. deterministic median headroom

\[
\boxed{
\operatorname{median}_\rho
\left|\frac{D_{\rm disc,P}-D_{\rm ref}}{D_{\rm ref}}\right|
\le6\%
}
\]

对 finite / Kolmogorov、x / y / 45° 分别满足。

这里 6% 不修改 Scientific Contract 的 formal 10% criterion；它是 implementation-level representation headroom，为正式 95% upper-bound qualification 预留 4 percentage points 的 sampling margin。

### B. pointwise tail guard

\[
\boxed{
\max_\rho
\left|\frac{D_{\rm disc,P}-D_{\rm ref}}{D_{\rm ref}}\right|
\le10\%
}
\]

同样分别对 finite / Kolmogorov、x / y / 45° 满足。

### C. slope guard

保持：

\[
\boxed{|s_{\rm disc}-5/3|\le0.08}.
\]

选择满足 A+B+C 的最小 P。

在当前 deterministic 数据上：

- P=8 因 K median ≈ 6.07% 而未满足 6% headroom；
- P=9 首次同时满足 median、pointwise 与 slope guards；
- 因此当前规则会自动得到 `P_*=9`，但 9 仍是输出，不是写死参数。

---

## 6. 为什么不推荐“8% pointwise everywhere”

另一种看似更简单的方案是把原 8% guard 从 median 改为所有点均 ≤8%。该规则会自动选择约 P=12。

但 P=12 diagnostic 表明更深的超低频层会增加 512-screen finite-ensemble uncertainty，implementation-recovery y 已贴近 5% gate。因此“把所有 deterministic error 压得越低越好”并不是当前 formal qualification 的最优策略。

R3 应显式承认：

> representation bias 必须足够低，但不能无代价地追求极深 subharmonics；formal 512-screen qualification 同时受超低频 sampling variance 约束。

---

## 7. 若 R3 外审通过后的正式 rerun

只有外审通过并将 R3 写入 authoritative contract 后才允许正式重跑。

正式 rerun 要求：

1. 保留原 P=6 failure 结果，不覆盖；
2. 使用新的正式 screen seeds 与新的 bootstrap seeds；
3. deterministic ladder 从 P=0 跑到 12；
4. selection rule 自动决定 P_*；
5. 不复用 P=8/P=9/P=12 diagnostic seeds；
6. `N_ens=512`、`B_boot=2000`、formal thresholds 保持不变；
7. V4 若 base FFT implementation 未改，只需 regression sanity，不需要重开 V4 科学审查；
8. formal V5 PASS 前继续禁止 V6。

---

## 8. 外审请求

请重点裁决：

1. C 类失败是否应归因于 deterministic representation margin policy，而不是 generator normalization；
2. 是否同意同时约束 median bias 与 pointwise tail bias；
3. `median <= 6%` 作为 formal 10% upper-bound gate 的 implementation headroom 是否合理；
4. 是否同意 P ladder 扩展到 12；
5. 是否需要比当前 R3 更原则化的 bias/variance selection rule。

建议外审裁决：

> **PASS — AUTHORIZE GATE B v0.2.1 REMEDIATION**

或

> **REVISE — GATE B v0.2.1 SELECTION POLICY**

本 proposal 不修改 Scientific Contract，不授权 V6，也不将任何 diagnostic run 视为正式资格证据。
