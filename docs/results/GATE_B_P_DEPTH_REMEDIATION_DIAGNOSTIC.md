# Gate B P-Depth Remediation Diagnostic

**日期：2026-08-08**  
**状态：DIAGNOSTIC ONLY — NOT FORMAL QUALIFICATION**

本文件记录 Gate-B P=6 formal failure 后，为选择 v0.2.1 remediation policy 所做的独立诊断。所有数值仅用于修订 implementation contract，不替代 formal `N_ens=512, B_boot=2000` qualification。

## 1. Deterministic extension

将原 ladder 从 P<=7 扩展到 P<=14，用完全相同的 `D_disc,P` 定义比较连续 Kolmogorov reference。

| P | K median x/y | K median 45° | K max x/y | K max 45° | K slope x/y | K slope 45° |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 11.252% | 11.306% | 17.927% | 17.778% | 1.62446 | 1.62419 |
| 5 | 9.184% | 9.226% | 14.638% | 14.495% | 1.63341 | 1.63323 |
| 6 | 7.749% | 7.784% | 12.357% | 12.218% | 1.63936 | 1.63924 |
| 7 | 6.755% | 6.785% | 10.776% | 10.640% | 1.64336 | 1.64328 |
| 8 | 6.066% | 6.092% | 9.679% | 9.546% | 1.64608 | 1.64603 |
| 9 | 5.588% | 5.611% | 8.919% | 8.787% | 1.64795 | 1.64791 |
| 10 | 5.256% | 5.278% | 8.392% | 8.261% | 1.64922 | 1.64920 |
| 11 | 5.026% | 5.047% | 8.027% | 7.896% | 1.65010 approx | 1.65008 approx |
| 12 | 4.867% | 4.887% | 7.773% | 7.643% | 1.6507 approx | 1.6507 approx |

finite-scale pointwise maximum error 在 P>=4 后约保持：

- x/y ≈ 5.123%；
- 45° ≈ 4.953%。

因此当前 remediation 的决定因素仍是 pure-Kolmogorov low-frequency representation。

## 2. P=8 diagnostic-only empirical check

Diagnostic screen seed：`2026080821`。  
Diagnostic bootstrap seed：`2026080822`。  
Screens：512。  
Bootstrap：1000，仅用于风险估计。

| direction | impl point | K amplitude point | slope | endpoint signed bias | impl diagnostic 95% UB | K amplitude diagnostic 95% UB |
|:---:|---:|---:|---:|---:|---:|---:|
| x | 1.843% | 7.796% | 1.64056 | -12.076% | 4.423% | 10.220% |
| y | 2.188% | 8.121% | 1.63787 | -12.993% | 4.554% | 10.342% |
| 45° | 0.204% | 5.900% | 1.64692 | -9.264% | 3.409% | 8.524% |

结论：P=8 deterministic pointwise error 已低于 10%，但在一组独立 512-screen diagnostic 中 x/y amplitude upper bound 仍处于 formal 10% gate 边缘之外。因此仅增加 `max deterministic error <=10%` 不足以形成稳健 remediation policy。

## 3. P=9 diagnostic-only empirical check

Diagnostic screen seed：`2026080823`。  
Diagnostic bootstrap seed：`2026080824`。  
Screens：512。  
Bootstrap：1000，仅用于风险估计。

| direction | impl point | K amplitude point | slope | endpoint signed bias | impl diagnostic 95% UB | K amplitude diagnostic 95% UB |
|:---:|---:|---:|---:|---:|---:|---:|
| x | 0.704% | 6.277% | 1.64696 | -9.552% | 3.410% | 8.676% |
| y | 0.483% | 6.047% | 1.64683 | -9.374% | 3.162% | 8.484% |
| 45° | 0.706% | 6.309% | 1.64705 | -9.418% | 3.631% | 8.927% |

所有 diagnostic slope intervals 均位于 `5/3 ± 0.10` 内。

P=9 在该独立 sample 中同时表现出较低 representation bias 与合理的 finite-ensemble variance，但该结果不能作为预先指定 P=9 的理由。

## 4. P=12 diagnostic-only empirical check

Diagnostic screen seed：`2026080825`。  
Diagnostic bootstrap seed：`2026080826`。  
Screens：512。  
Bootstrap：1000，仅用于风险估计。

| direction | impl point | K amplitude point | slope | endpoint signed bias | impl diagnostic 95% UB | K amplitude diagnostic 95% UB |
|:---:|---:|---:|---:|---:|---:|---:|
| x | 0.638% | 4.260% | 1.65454 | -6.464% | 3.478% | 6.801% |
| y | 2.271% | 2.706% | 1.65766 | -4.632% | 5.010% | 5.404% |
| 45° | 0.126% | 5.028% | 1.65093 | -7.740% | 3.127% | 7.363% |

P=12 deterministic bias 更低，但 y-direction implementation-recovery diagnostic 95% UB 已约 5.01%，说明更深超低频层会提高 realization variance；固定 512-screen formal sample 下不能简单采用“越深越好”的 selection rule。

## 5. Diagnostic interpretation

这些结果共同支持：

1. P=6 failure 是 representation-margin failure，不是 generator normalization failure；
2. low-frequency depth 增加降低 deterministic bias；
3. 但很深的 subharmonics 会增加 finite-ensemble sampling variance；
4. selection policy 应同时考虑 systematic representation bias 与 formal 512-screen uncertainty margin；
5. 当前最值得外审的是 `docs/review/GATE_B_V021_REMEDIATION_PROPOSAL.md` 中提出的 median-headroom + pointwise-tail guard，而不是直接指定任一 P。

所有 diagnostic seed family 与原 formal P=6 seeds 不同；未来若 v0.2.1 获批准，正式 rerun 必须再次使用全新的 formal seeds，不得复用本文件的 diagnostic seeds。
