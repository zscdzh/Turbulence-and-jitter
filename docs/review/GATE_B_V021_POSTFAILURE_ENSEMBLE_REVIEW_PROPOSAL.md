# Gate B v0.2.1 Post-Failure Review Proposal

**日期：2026-08-08**  
**状态：PROPOSED FOR NARROW EXTERNAL REVIEW**  
**当前正式裁决：REVISE — GATE B NOT YET QUALIFIED**  
**V6：CLOSED**

本文件只审查 Gate-B v0.2.1 fresh formal rerun 暴露的新问题：在 deterministic low-frequency margin 已修复后，`N_ens=512` 是否仍足以稳定资格化 P=9 sparse subharmonic Kolmogorov screens。它不重开 Scientific Contract、PSD normalization、FFT、Hermitian 或 subharmonic coefficient formula。

## 1. 历史链

### v0.2 / P=6

原正式失败属于 C 类：generator recovery PASS，但 `D_disc,6` 对连续 Kolmogorov reference 的 deterministic negative bias 过大，y/45° amplitude UB 超过10%。

### v0.2.1 remediation

外部审计批准：

- P ladder 扩展至 0..12；
- deterministic median bias <=6%；
- pointwise max bias <=10%；
- K slope error <=0.08；
- 选择满足条件的最小 P；
- formal ensemble 仍保持512，bootstrap 2000。

fresh deterministic calculation 自动选择 `P*=9`：K median约5.59%，max约8.92%，slope约1.64795。

因此原 P=6 deterministic-margin blocker 已关闭。

## 2. v0.2.1 fresh formal result

全新预登记 seeds：

- V4 `2026080830`；
- finite screen/bootstrap `2026080831 / 2026080833`；
- K screen/bootstrap `2026080832 / 2026080834`。

V4 regression PASS：PSD median error 0.4763%，slope difference 0.000564。

finite-scale formal V5 三方向全部 PASS。

Kolmogorov formal 512-screen：

| direction | impl point | impl 95% UB | amplitude point | amplitude 95% UB | slope 95% CI | result |
|:---:|---:|---:|---:|---:|---|:---:|
| x | 3.537% | **5.778%** | 8.927% | **11.042%** | [1.62311,1.64475] | FAIL |
| y | 0.505% | 3.876% | 5.111% | 7.952% | [1.63634,1.66391] | PASS |
| 45° | 2.082% | 4.508% | 7.576% | 9.866% | [1.62831,1.65159] | PASS |

因此正式结果仍是：

> **REVISE — GATE B NOT YET QUALIFIED**

## 3. 新失败与原失败不同

P=9 deterministic expectation 已满足 v0.2.1 bias-headroom policy。

但本组 512-screen Kolmogorov realization 在 x 方向相对 `D_disc,9` 出现随 separation 增大的负波动：endpoint empirical-vs-deterministic 约 -6%，与 deterministic 对 continuous reference 的负 bias 叠加后，endpoint empirical-vs-continuous 约 -14%。

因此本轮同时触发：

- implementation-recovery UB >5%；
- continuous amplitude UB >10%。

当前没有证据显示 PSD / FFT / Hermitian / coefficient normalization 重新失效，因为 y/45° recovery 正常、V4 正常，且同一 generator 在更大 ensemble 下向 deterministic expectation 收敛。

## 4. Post-failure 1024-screen convergence diagnostic

正式 FAIL 后，保持：

- 相同 P=9；
- 相同 Kolmogorov screen seed `2026080832`；
- 不丢弃正式前512张；

仅继续同一 RNG sequence 到累计1024 screens。该结果明确标记 diagnostic only，不能 retroactively 作为 PASS。

x direction point estimates：

| cumulative N | impl error | K amplitude error |
|---:|---:|---:|
| 512 | 3.537% | 8.927% |
| 640 | 3.105% | 8.519% |
| 768 | 2.080% | 7.551% |
| 896 | 1.364% | 6.875% |
| 1024 | 1.084% | 6.611% |

1024-screen、2000-bootstrap post-failure diagnostic（bootstrap seed `2026080841`）：

| direction | impl 95% UB | amplitude 95% UB | slope 95% CI |
|:---:|---:|---:|---|
| x | 2.915% | 8.340% | [1.63441,1.65240] |
| y | 2.443% | 7.523% | [1.63839,1.65680] |
| 45° | 2.397% | 7.731% | [1.63697,1.65445] |

这只说明同一 P=9 generator / same-seed sequence 随 ensemble 增加明显向 `D_disc,9` 收敛；不改变512-screen正式 FAIL。

## 5. 当前判断

现有证据更支持：

> v0.2.1 已修复 deterministic low-frequency bias margin，但 512 screens 对 sparse ultra-low-frequency Kolmogorov representation 的 formal empirical recovery 可能没有足够稳定的统计余量。

仍不能排除另一种方案：修改 low-frequency representation 本身，使单屏统计更高效、方向有限样本波动更小。但当前没有 generator-normalization 失败证据，也没有必要立即重设计 phase-screen method。

## 6. 请求外审的唯一核心问题

请裁决下一步优先方案：

### Option A — formal ensemble 提高到1024

- finite / Kolmogorov 统一 `N_ens=1024`；
- formal bootstrap 仍为 screen-ID bootstrap；
- 其它 v0.2.1 deterministic policy、PSD、P-selection 与 formal thresholds 不变；
- 使用全新正式 seeds；
- 当前 post-failure 1024 continuation 只作为修改 ensemble-size 的诊断依据，不作为新 formal evidence。

优点：不改变 generator；直接针对已观察到的有限样本收敛问题；计算成本可接受。

风险：这是看到512失败后的资格规则修改，必须透明记录，不能把当前1024 diagnostic 当作事前通过证据。

### Option B — 保持512，修改 low-frequency representation

例如增加更密的 low-frequency cell sampling / alternative low-frequency augmentation，使有限样本 directional variance 更低，再重新 deterministic + empirical qualification。

优点：可能提高单屏 representation efficiency。

风险：重新引入 phase-screen method design，会扩大当前已基本关闭的 Gate-B scope；需要新的 normalization / representation qualification，并且当前证据尚未证明这种复杂化必要。

## 7. 当前推荐

在外审前的项目判断是：

> **优先 Option A：将 formal V5 ensemble 从512提高到1024，finite/Kolmogorov 统一；其余 v0.2.1 科学与实现定义保持不变。**

理由不是“1024 diagnostic 已经 PASS”，而是：

1. deterministic representation 已满足 headroom policy；
2. 512 failure 包含 empirical-vs-deterministic recovery failure；
3. 同一随机序列从512继续到1024时 recovery 与 amplitude 持续向 expectation 收敛；
4. 项目计算资源允许；
5. 相比重新设计 low-frequency generator，这是更窄、更容易审计的 remediation。

但该建议必须由外审裁决后才能修改 authoritative contract 或执行新的正式 qualification。

## 8. 外审裁决建议格式

> **PASS — AUTHORIZE N_ens=1024 GATE-B v0.2.2 REMEDIATION**

或

> **REVISE — REQUIRE LOW-FREQUENCY REPRESENTATION CHANGE BEFORE RERUN**

或

> **STOP — CURRENT GATE-B QUALIFICATION STRATEGY NOT ADEQUATE**

本轮继续禁止 V6。
