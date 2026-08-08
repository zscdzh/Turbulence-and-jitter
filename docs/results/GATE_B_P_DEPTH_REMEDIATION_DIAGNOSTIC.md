# Gate B P-Depth Remediation Diagnostic

**日期：2026-08-08**  
**状态：DIAGNOSTIC ONLY — NOT FORMAL QUALIFICATION**

本文件记录原 `P*=6` formal failure 后，为 Gate-B v0.2.1 remediation policy 所做的独立诊断。所有数值只用于修订 implementation contract，不替代 formal `N_ens=512, B_boot=2000` qualification。

本版根据外部审计补齐唯一 diagnostic runner，并修正此前与 formal runner 不完全同构的 bootstrap RNG 使用方式。

## 1. Reproducibility

唯一 runner：

- `scripts/run_gate_b_p_depth_diagnostic.py`

机器结果：

- `results/gate_b_p_depth_diagnostic/metadata.json`
- `results/gate_b_p_depth_diagnostic/diagnostic_summary.json`
- per-screen P=8/9/12 `D_phi(rho)` observables（由 runner 生成；不保存 raw phase screens）

固定 diagnostic-only seeds：

| P | screen seed | bootstrap seed |
|---:|---:|---:|
| 8 | 2026080821 | 2026080822 |
| 9 | 2026080823 | 2026080824 |
| 12 | 2026080825 | 2026080826 |

每个 P 使用 512 screens、1000 次 screen-ID bootstrap。

bootstrap 与 formal runner 保持同一唯一算法：对每个 P 先生成一套 `1000 x 512` screen-ID resample-count weights，随后 x/y/45° 三方向共用同一套 weights。此前 Markdown 中部分 P=12 UB 使用了方向分别推进 RNG 的临时诊断实现，已在本版纠正。

---

## 2. Deterministic extension

将原 ladder 扩展后：

| P | K median x/y | K median 45° | K max x/y | K max 45° | K slope x/y | K slope 45° |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 11.252% | 11.306% | 17.927% | 17.778% | 1.62446 | 1.62419 |
| 5 | 9.184% | 9.226% | 14.638% | 14.495% | 1.63341 | 1.63323 |
| 6 | 7.749% | 7.784% | 12.357% | 12.218% | 1.63936 | 1.63924 |
| 7 | 6.755% | 6.785% | 10.776% | 10.640% | 1.64336 | 1.64328 |
| 8 | 6.066% | 6.092% | 9.679% | 9.546% | 1.64608 | 1.64603 |
| 9 | 5.588% | 5.611% | 8.919% | 8.787% | 1.64795 | 1.64791 |
| 10 | 5.256% | 5.278% | 8.392% | 8.261% | 1.64922 | 1.64920 |
| 11 | 5.026% | 5.047% | 8.027% | 7.896% | 1.65010 | 1.65008 |
| 12 | 4.867% | 4.887% | 7.773% | 7.643% | 1.65072 | 1.65070 |

finite-scale pointwise maximum error 在 P>=4 后约保持：

- x/y ≈ 5.12%；
- 45° ≈ 4.95%。

因此 remediation 的主要决定因素是 pure-Kolmogorov low-frequency representation。

---

## 3. P=8 diagnostic

| direction | impl point | impl 95% UB | K amp point | K amp 95% UB | slope point | slope 95% CI |
|:---:|---:|---:|---:|---:|---:|---|
| x | 1.843% | 4.423% | 7.796% | 10.220% | 1.64056 | [1.62843, 1.65295] |
| y | 2.188% | 4.789% | 8.121% | 10.564% | 1.63787 | [1.62517, 1.64970] |
| 45° | 0.204% | 3.199% | 5.900% | 8.304% | 1.64692 | [1.63512, 1.65903] |

P=8 已满足 deterministic pointwise `<10%`，但 x/y diagnostic amplitude UB 仍在 formal 10% gate 附近/之外。因此“仅增加 pointwise <=10%”不足以构成稳健 remediation policy。

---

## 4. P=9 diagnostic

| direction | impl point | impl 95% UB | K amp point | K amp 95% UB | slope point | slope 95% CI |
|:---:|---:|---:|---:|---:|---:|---|
| x | 0.704% | 3.410% | 6.277% | 8.676% | 1.64696 | [1.63493, 1.65934] |
| y | 0.483% | 3.224% | 6.047% | 8.444% | 1.64683 | [1.63504, 1.65885] |
| 45° | 0.706% | 3.496% | 6.309% | 8.816% | 1.64705 | [1.63514, 1.65877] |

该单组 diagnostic 显示 P=9 在当前 512-screen sample 下具有合理余量，但它不证明 P=9 是一般意义上的 variance optimum，也不能作为直接写死 P=9 的依据。

---

## 5. P=12 diagnostic

| direction | impl point | impl 95% UB | K amp point | K amp 95% UB | slope point | slope 95% CI |
|:---:|---:|---:|---:|---:|---:|---|
| x | 0.638% | 3.478% | 4.260% | 6.801% | 1.65454 | [1.64221, 1.66575] |
| y | 2.271% | **5.317%** | 2.706% | 5.636% | 1.65766 | [1.64403, 1.67038] |
| 45° | 0.126% | 3.313% | 5.028% | 7.746% | 1.65093 | [1.63787, 1.66243] |

外部审计独立复跑指出此前文档中的 y implementation UB `~5.01%` 无法逐位追溯。使用本版唯一 diagnostic runner、formal-runner-identical shared bootstrap weights 后得到 `5.317%`，与外部独立复跑 `~5.32%` 一致。

这一结果只说明该 P=12 diagnostic sample 没有显示出比满足偏差预算的更浅深度更可靠的 finite-sample qualification；不能推导“P 越大，variance 必然单调增大”。

---

## 6. Interpretation

当前证据支持：

1. 原 P=6 failure 是 representation-margin failure，不是 generator normalization failure；
2. 增加 subharmonic depth 会降低当前 frozen interval 上的 deterministic low-frequency bias；
3. P=8 的 deterministic tail 虽已低于10%，但 single diagnostic sample 的 formal-style UB 仍缺乏余量；
4. P=12 的 single diagnostic sample 出现 y implementation UB >5%，因此没有证据要求为了更低 deterministic bias 无限制增加低频层；
5. 不同 P 使用不同 seeds，不能据此建立一般性的 variance-vs-P 单调关系；
6. 因而 v0.2.1 采用 **minimum-depth deterministic bias-headroom policy**：定义 median + pointwise bias budget，选择满足条件的最小 P。

未来正式 v0.2.1 rerun 必须使用新的 formal seed family，不得复用本文件任何 diagnostic seeds。
