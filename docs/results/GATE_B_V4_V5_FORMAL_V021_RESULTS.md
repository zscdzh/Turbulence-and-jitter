# Gate B v0.2.1 Formal V5 Rerun

**运行日期：2026-08-08**  
**权威合同：`docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V021.md`**  
**正式裁决：REVISE — GATE B NOT YET QUALIFIED**  
**V6：NOT AUTHORIZED**

## 1. 负责人摘要

本轮在外部审计批准 Gate-B v0.2.1 remediation policy 后，使用全新 seed family 正式重跑 V5。原 v0.2 / `P*=6` failure 永久保留，没有覆盖或复用 seeds。

v0.2.1 deterministic policy 实际选择最小通过深度：

\[
\boxed{P_*=9}.
\]

V4 regression、finite-scale formal V5、Kolmogorov y/45° implementation recovery、amplitude 与三方向 slope 均通过。

但是 Kolmogorov x direction：

- implementation-recovery point = **3.537%**；
- implementation-recovery 95% UB = **5.778% > 5%**；
- continuous amplitude point = **8.927%**；
- continuous amplitude 95% UB = **11.042% > 10%**。

因此正式裁决仍为：

> **REVISE — GATE B NOT YET QUALIFIED**

不得进入 V6。

---

## 2. Fresh seeds

这些 seeds 在任何新 formal screen 生成前已写入 `scripts/run_gate_b_formal_v021.py`：

- V4 regression screen seed：`2026080830`；
- finite formal screen seed：`2026080831`；
- Kolmogorov formal screen seed：`2026080832`；
- finite bootstrap seed：`2026080833`；
- Kolmogorov bootstrap seed：`2026080834`。

均不同于原 P=6 formal seeds 和 P=8/9/12 remediation diagnostic seeds。

---

## 3. V4 regression

128-screen fresh-seed regression：

- PSD median annular relative error = **0.4763%**；
- numerical slope = `-3.887529`；
- exact modified-von-Karman target slope = `-3.888093`；
- slope difference = **0.000564**。

结果：**PASS**。

---

## 4. Deterministic v0.2.1 selection

v0.2.1 使用：

- `P=0..12`；
- median bias `<=6%`；
- pointwise max bias `<=10%`；
- Kolmogorov slope error `<=0.08`；
- 选择满足全部条件的最小 P。

continuous finite-scale quadrature 最大相对变化约 `5.81e-14`。

实际计算：

- P=8：Kolmogorov median 约 `6.066% / 6.092%`，未通过6% headroom；
- P=9：Kolmogorov median约 `5.588% / 5.611%`，max约 `8.919% / 8.787%`，slope约 `1.64795 / 1.64791`，首次通过；
- 因此 `P*=9`。

P=9 仍是 deterministic policy 输出，不是写死参数。

---

## 5. Formal 512-screen bootstrap

### finite-scale

| direction | impl point | impl 95% UB | amplitude point | amplitude 95% UB | result |
|:---:|---:|---:|---:|---:|:---:|
| x | 1.149% | 2.974% | 3.934% | 5.693% | PASS |
| y | 1.174% | 3.076% | 1.677% | 3.456% | PASS |
| 45° | 0.016% | 2.020% | 2.830% | 4.347% | PASS |

finite slope 只作 diagnostic，不属于 formal slope gate。

### Kolmogorov

| direction | impl point | impl 95% UB | amplitude point | amplitude 95% UB | slope point | slope 95% CI | result |
|:---:|---:|---:|---:|---:|---:|---|:---:|
| x | 3.537% | **5.778%** | 8.927% | **11.042%** | 1.63414 | [1.62311, 1.64475] | **FAIL** |
| y | 0.505% | 3.876% | 5.111% | 7.952% | 1.65009 | [1.63634, 1.66391] | PASS |
| 45° | 2.082% | 4.508% | 7.576% | 9.866% | 1.63988 | [1.62831, 1.65159] | PASS |

三方向 slope CI 均位于 `5/3 ± 0.10` 内。

---

## 6. Failure structure

本次失败与原 v0.2 / P=6 的纯 C 类失败不同。

P=9 deterministic Kolmogorov bias 已满足 remediation policy：x/y median约 `5.588%`，max约 `8.919%`。

但本组 512-screen formal Kolmogorov sample 在 x 方向相对 deterministic expectation 出现随 separation 增大的负偏差：

- empirical-vs-`D_disc,9` 从小 separation 约 `-2.2%` 增至 endpoint 约 `-6.0%`；
- empirical-vs-continuous reference 从约 `-6.2%` 增至 endpoint 约 `-14.4%`；
- `rho >= 23.359 mm` 后 x direction point estimate 已低估 continuous reference 超过10%。

相同 realization set 的 y direction 基本贴近 `D_disc,9`，45° 介于两者之间。

因此 formal failure 包含：

1. **x implementation-recovery 95% UB >5%**；
2. deterministic negative bias 与该 finite-sample x-direction negative fluctuation 叠加，使 x amplitude UB >10%。

当前没有证据指向 PSD / FFT / Hermitian / coefficient normalization 重新出错；更符合 sparse ultra-low-frequency modes 在固定 512-screen ensemble 下产生较强 direction-dependent finite-sample fluctuation。

---

## 7. Post-failure convergence diagnostic — NOT FORMAL

为判断 512-screen sample size 与 representation 的责任边界，只在 formal FAIL 之后继续**同一个 Kolmogorov seed 的同一随机序列**到 1024 screens。该扩展不改变正式裁决，也不得 retroactively 用作 PASS。

x direction point estimates 随累计屏数：

| N | implementation error | K amplitude error |
|---:|---:|---:|
| 512 | 3.537% | 8.927% |
| 640 | 3.105% | 8.519% |
| 768 | 2.080% | 7.551% |
| 896 | 1.364% | 6.875% |
| 1024 | 1.084% | 6.611% |

1024-screen diagnostic 使用独立 post-failure bootstrap seed `2026080841`、2000 screen-ID resamples：

| direction | impl point | impl 95% UB | K amp point | K amp 95% UB | slope 95% CI |
|:---:|---:|---:|---:|---:|---|
| x | 1.084% | 2.915% | 6.611% | 8.340% | [1.63441, 1.65240] |
| y | 0.049% | 2.443% | 5.640% | 7.523% | [1.63839, 1.65680] |
| 45° | 0.371% | 2.397% | 5.961% | 7.731% | [1.63697, 1.65445] |

这些数字只支持诊断判断：同一 P=9 generator 与同一 seed sequence 随 N 增加明显向 deterministic expectation 收敛。它们不是 v0.2.1 formal PASS 证据。

---

## 8. 当前科学判断

当前证据更支持：

> v0.2.1 已修复原 P=6 deterministic margin 问题，但 `N_ens=512` 对 P=9 sparse ultra-low-frequency Kolmogorov representation 的 formal empirical recovery 未必具有足够稳定的统计余量。

这不是允许直接把 formal ensemble 改成1024的授权。由于 `N_ens=512` 是 v0.2.1 预注册规则，本轮必须保留 FAIL。

下一步只需要外审一个更窄的问题：

> 是否应把 Gate-B formal V5 ensemble 从512提高到1024（最好 finite / Kolmogorov 统一），还是应进一步修改 low-frequency representation 本身以降低 finite-ensemble directional variance？

在该问题裁决前，不重新设计 PSD/Hermitian，也不进入 V6。

---

## 9. Evidence boundary

已支持：

- V4 normalization；
- v0.2.1 deterministic P-selection；
- finite-scale formal V5；
- Kolmogorov slope；
- Kolmogorov y/45° formal amplitude/recovery；
- P=9 generator 随 ensemble 增大向 deterministic expectation 收敛的 post-failure diagnostic。

未支持：

- Gate B formal PASS；
- 512 screens 对该 low-frequency representation 已足够；
- V6 beam wander；
- production multi-screen；
- structured fields。

## 10. Project decision

> **REVISE — GATE B v0.2.1 NOT YET QUALIFIED**
>
> **V6 remains CLOSED.**
