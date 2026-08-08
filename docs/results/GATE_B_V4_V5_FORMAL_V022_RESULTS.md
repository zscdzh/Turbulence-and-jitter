# Gate B v0.2.2 Formal 1024-Screen Result

**日期：2026-08-08**  
**权威合同：`docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V022.md`**  
**正式裁决：PASS — GATE B V4–V5 QUALIFIED**  
**V6：仍未自动授权，等待项目负责人明确授权**

## 1. 负责人摘要

按照 v0.2.2 一次性止损规则，使用事前提交的唯一 fresh seed family 执行正式 `N_ens=1024` V5 qualification。没有更换 seed、改变 P-selection、扩大 ensemble 或修改 formal threshold。

- V4 regression：PASS；
- deterministic policy：仍自动选择 `P*=9`；
- finite-scale V5：x/y/45° 全部 PASS；
- Kolmogorov implementation recovery：x/y/45° 全部 PASS；
- Kolmogorov amplitude：x/y/45° 全部 PASS；
- Kolmogorov slope：x/y/45° 全部 PASS。

因此：

> **PASS — GATE B V4–V5 QUALIFIED**

该结果只关闭 screen-level Gate B。V6 beam-wander qualification 仍需项目负责人显式授权。

## 2. Frozen formal settings

- `N_ens=1024`；
- `B_boot=2000`；
- screen-ID bootstrap，同 case 三方向共享 resample weights；
- P ladder `0..12`；median guard 6%，pointwise guard 10%，slope guard 0.08；
- formal thresholds：implementation UB ≤5%，amplitude UB ≤10%，Kolmogorov slope CI 完整落入 `5/3 ± 0.10`。

Fresh seeds：

- V4 `2026080860`；
- finite screen/bootstrap `2026080861 / 2026080863`；
- Kolmogorov screen/bootstrap `2026080862 / 2026080864`。

这些 seeds 已在任何 v0.2.2 formal result 出现前提交到 `scripts/run_gate_b_formal_v022.py`。

## 3. Execution note

执行环境的第一次命令调用在 finite 第384张时被工具单次命令时限强制终止；当时没有形成完整 formal ensemble 或 formal statistic。随后以**完全相同的已预登记 seed family**从 screen 1 重新执行完整 run。没有更换 seed、threshold、P-selection 或 ensemble size。

## 4. V4 and deterministic selection

- V4 PSD median error = **0.2494%**；
- V4 numerical slope = `-3.885437`；
- exact target slope = `-3.888093`；
- slope difference = **0.002656**；
- continuous finite-scale quadrature 最大相对收敛变化 = `5.813e-14`；
- deterministic policy 再次计算得到 **`P*=9`**。

P=8 的 Kolmogorov x median error 为约 `6.066%`，未通过6% guard；P=9 首次通过，因此 P=9 仍然是规则输出而不是写死参数。

## 5. Formal finite-scale V5

| direction | impl point | impl 95% UB | amplitude point | amplitude 95% UB | result |
|---|---:|---:|---:|---:|:---:|
| x | 0.721% | 1.940% | 3.519% | 4.703% | PASS |
| y | 0.289% | 1.648% | 3.098% | 4.317% | PASS |
| 45° | 1.072% | 2.156% | 3.871% | 4.924% | PASS |

## 6. Formal Kolmogorov V5

| direction | impl point | impl 95% UB | amplitude point | amplitude 95% UB | slope point | slope 95% CI | result |
|---|---:|---:|---:|---:|---:|---|:---:|
| x | 1.144% | 3.098% | 4.508% | 6.298% | 1.65169 | [1.64303, 1.66016] | PASS |
| y | 0.458% | 2.370% | 6.020% | 7.732% | 1.64613 | [1.63782, 1.65446] | PASS |
| 45° | 0.545% | 2.550% | 5.097% | 6.882% | 1.64878 | [1.64026, 1.65741] | PASS |

全部 implementation-recovery 95% UB 均明显低于 5%；全部 amplitude 95% UB 均低于 10%；三方向 slope CI 均完整位于 `[1.5667, 1.7667]`。

## 7. Prefix diagnostics

256/512/768 prefixes 只作 convergence diagnostic，不参与正式裁决。完整 1024 Kolmogorov point estimates：

- x：implementation `1.144%`，amplitude `4.508%`；
- y：implementation `0.458%`，amplitude `6.020%`；
- 45°：implementation `0.545%`，amplitude `5.097%`。

## 8. Evidence

- authoritative contract：`docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V022.md`；
- authorized runner：`scripts/run_gate_b_formal_v022.py`；
- runner blob SHA：`d1ff27c347e37a68a9ca0d9bb111433aa3136d65`；
- machine summary：`results/gate_b_v5_formal_v022/bootstrap_summary.json`；
- run metadata：`results/gate_b_v5_formal_v022/metadata.json`；
- deterministic selection summary：`results/gate_b_v5_formal_v022/deterministic_selection_summary.json`。

历史 v0.2/P=6 FAIL、v0.2.1/512 FAIL 和 post-failure 1024 diagnostic 均保留，不被本结果覆盖。

## 9. Evidence boundary

已支持：

- base-FFT PSD normalization；
- recursive subharmonic low-frequency representation 在冻结 screen-level qualification 上的 deterministic adequacy；
- finite-scale structure-function absolute qualification；
- Kolmogorov implementation recovery、absolute amplitude 与 slope qualification。

仍未支持：

- V6 beam wander；
- V7 long-term radius；
- V8 scintillation；
- production multi-screen placement / screen-number convergence；
- structured-field comparison。

## 10. Project decision

> **CONTINUE — GATE B V4–V5 QUALIFIED; WAIT FOR PROJECT-LEAD AUTHORIZATION BEFORE V6.**
