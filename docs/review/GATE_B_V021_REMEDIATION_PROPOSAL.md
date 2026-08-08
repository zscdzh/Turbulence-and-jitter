# Gate B v0.2.1 Remediation Proposal — Review-Resolved Draft

**日期：2026-08-08**  
**状态：CONDITIONAL PASS CONDITIONS RESOLVED — READY TO FREEZE v0.2.1**  
**上位合同：Scientific Contract v0.3.2（保持冻结）**  
**当前正式结果：REVISE — GATE B NOT YET QUALIFIED**

本文件针对 `docs/results/GATE_B_V4_V5_FORMAL_RESULTS.md` 中确认的 C 类失败提出 Gate-B v0.2.1 remediation policy，并根据外部短审修正因果表述、补齐可复现 diagnostic runner 与机器结果。它不修改 Scientific Contract，不推翻 Gate A，不修改 PSD / FFT / Hermitian / random-coefficient normalization，也不授权 V6。

---

## 1. 已确认的原始失败

原 v0.2 / `P*=6` formal qualification 中：

- V4 PASS；
- finite-scale V5 PASS；
- Kolmogorov implementation recovery PASS；
- Kolmogorov slope PASS；
- Kolmogorov amplitude x PASS；
- Kolmogorov amplitude y / 45° FAIL。

失败属于 C 类：empirical generator 能恢复自身 `D_disc,6`，但 `D_disc,6` 相对连续 Kolmogorov reference 存在随 separation 增大的系统性负偏差。原 `8% median` deterministic guard 只约束中位误差，不能排除冻结 separation 区间尾部已存在超过正式 10% amplitude budget 的 deterministic bias。

因此 remediation 对象是 **low-frequency representation qualification / P-selection policy**，不是 phase-screen 核心公式。

---

## 2. Deterministic extension

使用完全相同的 `D_disc,P` 定义扩展低频深度：

| P | K median x/y | K median 45° | K max x/y | K max 45° |
|---:|---:|---:|---:|---:|
| 6 | 7.749% | 7.784% | 12.357% | 12.218% |
| 7 | 6.755% | 6.785% | 10.776% | 10.640% |
| 8 | 6.066% | 6.092% | 9.679% | 9.546% |
| 9 | 5.588% | 5.611% | 8.919% | 8.787% |
| 10 | 5.256% | 5.278% | 8.392% | 8.261% |
| 11 | 5.026% | 5.047% | 8.027% | 7.896% |
| 12 | 4.867% | 4.887% | 7.773% | 7.643% |

finite-scale pointwise maximum error 在这些深度下约为 5.1% 或更低，因此 remediation 的决定因素仍是 pure-Kolmogorov low-frequency representation。

仅增加 `max deterministic error <= 10%` 会选择 P=8，但独立 diagnostic 表明这一条件对正式 10% upper-bound criterion 留出的统计余量仍不足。

---

## 3. 修正后的诊断因果表述

本项目**不声称 P=9 是“bias–variance 最优”**，也不声称 subharmonic depth 增加会导致 variance 单调增加。

现有证据只支持：

1. P=6 的 deterministic representation margin 不足；
2. 增加 P 会降低当前冻结 separation interval 上的 deterministic low-frequency bias；
3. 单组 P=12 diagnostic 的 y-direction implementation uncertainty 处于 5% formal gate 附近/之外，因此没有证据证明比满足偏差预算的更浅深度更可靠；
4. 不同 P 使用不同 diagnostic seed families，不能用这些单组 realization 证明一般性的 variance-vs-P 单调规律；
5. 因而 remediation policy 应采用 **minimum-depth deterministic bias-headroom policy**：先定义足够的 deterministic bias margin，再选择满足要求的最小深度，避免无必要加入更低频层。

这是一项 qualification implementation policy，不是普适大气湍流结论。

---

## 4. Reproducible diagnostic evidence

诊断现已由唯一 runner 生成：

- `scripts/run_gate_b_p_depth_diagnostic.py`

机器结果目录：

- `results/gate_b_p_depth_diagnostic/metadata.json`
- `results/gate_b_p_depth_diagnostic/diagnostic_summary.json`
- `results/gate_b_p_depth_diagnostic/p8_screen_observables.npz`
- `results/gate_b_p_depth_diagnostic/p9_screen_observables.npz`
- `results/gate_b_p_depth_diagnostic/p12_screen_observables.npz`

固定 diagnostic-only seeds：

- P=8 screens `2026080821`，bootstrap `2026080822`；
- P=9 screens `2026080823`，bootstrap `2026080824`；
- P=12 screens `2026080825`，bootstrap `2026080826`。

每个 P：512 screens；1000 次 screen-ID bootstrap。diagnostic bootstrap 与 formal runner 使用同一算法：先按 bootstrap seed 生成一套 resample-count weight matrix，x/y/45° 三方向共用这套 screen-ID resamples。

不保存 raw phase screens，只保存 per-screen `D_phi(rho)` observables。

---

## 5. Corrected diagnostic results

### P=8

| direction | impl point | impl 95% UB | K amplitude point | K amplitude 95% UB | slope |
|:---:|---:|---:|---:|---:|---:|
| x | 1.843% | 4.423% | 7.796% | 10.220% | 1.64056 |
| y | 2.188% | 4.789% | 8.121% | 10.564% | 1.63787 |
| 45° | 0.204% | 3.199% | 5.900% | 8.304% | 1.64692 |

因此 pointwise deterministic `<10%` 单独作为 selection rule 仍不够稳。

### P=9

| direction | impl point | impl 95% UB | K amplitude point | K amplitude 95% UB | slope |
|:---:|---:|---:|---:|---:|---:|
| x | 0.704% | 3.410% | 6.277% | 8.676% | 1.64696 |
| y | 0.483% | 3.224% | 6.047% | 8.444% | 1.64683 |
| 45° | 0.706% | 3.496% | 6.309% | 8.816% | 1.64705 |

三方向 diagnostic slope 95% intervals 均处于 `5/3 ± 0.10` 内。该结果仅说明当前最小满足偏差预算的深度具有合理的有限样本余量，不构成“P=9 最优”的证据。

### P=12

| direction | impl point | impl 95% UB | K amplitude point | K amplitude 95% UB | slope |
|:---:|---:|---:|---:|---:|---:|
| x | 0.638% | 3.478% | 4.260% | 6.801% | 1.65454 |
| y | 2.271% | **5.317%** | 2.706% | 5.636% | 1.65766 |
| 45° | 0.126% | 3.313% | 5.028% | 7.746% | 1.65093 |

此前 Markdown 中 P=12 y implementation UB 约 5.01% 的数值来自与 formal runner 不完全同构的 diagnostic bootstrap RNG 使用方式。补齐唯一 runner 后，formal-runner-identical 算法得到 5.317%，与外部独立复跑约 5.32% 一致。该差异不改变 remediation policy，但必须保留在证据记录中。

---

## 6. v0.2.1 selection policy

建议将 deterministic ladder 扩展为：

\[
P=0,1,\ldots,12.
\]

选择同时满足以下条件的最小 P。

### A. deterministic median headroom

\[
\boxed{
\operatorname{median}_\rho
\left|\frac{D_{\rm disc,P}-D_{\rm ref}}{D_{\rm ref}}\right|
\le 6\%
}
\]

对 finite / Kolmogorov、x / y / 45° 分别满足。

6% 是在原 P=6 formal failure 后明确引入的 remediation threshold；它不是事前阈值，也不是普适物理常数。其用途是在 formal `10%` amplitude upper-bound budget 下，为 512-screen finite-sample uncertainty 留出约 4 percentage points 的 implementation headroom。

### B. pointwise tail guard

\[
\boxed{
\max_\rho
\left|\frac{D_{\rm disc,P}-D_{\rm ref}}{D_{\rm ref}}\right|
\le 10\%
}
\]

同样分别对 finite / Kolmogorov、x / y / 45° 满足，用于防止 median 掩盖长 separation 尾部 bias。

### C. slope guard

保持：

\[
\boxed{|s_{\rm disc}-5/3|\le0.08}.
\]

当前 deterministic 数据下，P=8 因 K median 约 6.07% 未满足 A；P=9 首次满足 A+B+C。因此当前算法输出 `P*=9`，但 P=9 不是写死参数。

---

## 7. 正式 rerun 边界

冻结 v0.2.1 后，formal rerun 必须：

1. 永久保留原 P=6 failure 结果；
2. 使用全新的 formal screen seeds 与 bootstrap seeds；
3. 不复用 P=8/9/12 diagnostic seeds；
4. deterministic ladder 实际运行 P=0..12 并自动选择 P*；
5. `N_ens=512`、`B_boot=2000` 与所有 Scientific Contract formal thresholds 不变；
6. V4 base-FFT implementation 未变时只做 regression sanity；
7. formal V5 PASS 前继续禁止 V6。

进入未来传播层前，可以对每张 total phase screen 移除 spatial mean piston：

\[
\phi\leftarrow\phi-\langle\phi\rangle.
\]

该操作不改变 structure function，也不移除 tilt；它是 V6 前的 numerical hygiene，不属于本轮 V5 remediation gate。

---

## 8. Review resolution

外部审计结论为：

> **CONDITIONAL PASS — 同意 Gate B v0.2.1 remediation policy。**

条件：

1. 修正“P=9 bias–variance 最优”的过度因果表述；
2. 提交可复现 diagnostic runner、metadata、per-screen observables 与 bootstrap summary。

本修订已按上述两点关闭。下一步可以将 v0.2.1 写入 authoritative implementation contract，并使用全新 formal seeds 进行一次正式 rerun。
