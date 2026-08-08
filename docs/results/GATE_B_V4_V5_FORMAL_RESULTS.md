# Gate B V4–V5 Formal Empirical Qualification

**运行日期：** 2026-08-08
**权威合同：** `docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V02.md`
**最终裁决：** **REVISE — PHASE-SCREEN IMPLEMENTATION**

## 1. 负责人摘要

本轮用于回答冻结的单屏 phase-screen generator 是否在频谱归一化、低频补偿和空间结构函数三个层面通过 V4–V5 absolute qualification。实际测试包含 128-screen V4、完整 P=0–7 deterministic ladder、finite/Kolmogorov 各 512 个独立 screens、nested 128/256/512 点估计，以及按 screen ID 重采样的 2000 次 bootstrap。

最终结果：**REVISE — PHASE-SCREEN IMPLEMENTATION**。

Gate B 尚未合格，不允许进入 V6，必须先修订 phase-screen implementation。

## 2. 数学定义

- `S_phi(fx,fy)`：以 cycles/m 为频率坐标、与 `dfx dfy` 配套的二维相位 PSD，单位 `rad² m²`。
- `a_uv`：离散 Fourier cell 的复随机系数，满足 `E|a_uv|²=S_phi df²`，单位 rad。
- `D_disc,P(rho)`：base FFT 加 P 层 subharmonics 的精确离散期望结构函数，单位 `rad²`。
- `D_emp(rho)`：逐 screen 用 non-wrapped valid pairs 计算后再作 ensemble mean 的经验结构函数，单位 `rad²`。
- `D_finite,ref(rho)`：独立 atmospheric-measure 连续积分得到的 finite-scale reference，单位 `rad²`。
- `D_K(rho)=6.88(rho/r0_screen)^(5/3)`：解析 Kolmogorov absolute reference，单位 `rad²`。
- `P_*`：P=0–7 中同时通过三方向 8% amplitude guard 与 0.08 slope guard 的最小 subharmonic depth。
- bootstrap 95% UB：2000 个 screen-ID bootstrap statistics 的第 95 百分位；slope 95% CI 为第 2.5–97.5 百分位。

## 3. 关键代码链

`finite_phase_psd_cycles` / `kolmogorov_phase_psd_cycles` → `generate_base_fourier_coefficients` → `build_hermitian_layout` → `ifft2c` phase screen → `generate_subharmonic_phase` → `structure_function_valid_pairs` → per-screen `D_phi` observable → ensemble mean → `bootstrap_case` → frozen PASS/FAIL rules。

## 4. 实际结果

### V4

| metric | numerical | target / limit | result |
|---|---:|---:|:---:|
| median annular PSD level error | 0.353% | <=10% | PASS |
| log-log slope | -3.883437 | target -3.888093 | — |
| slope difference | 0.004655 | <=0.10 | PASS |

### Deterministic P ladder

| P | finite x | finite y | finite 45° | K x | K y | K 45° | K slope x | K slope y | K slope 45° | guard |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| 0 | 20.152% | 20.152% | 20.269% | 33.689% | 33.689% | 33.862% | 1.48470 | 1.48470 | 1.48279 | FAIL |
| 1 | 9.526% | 9.526% | 9.578% | 24.743% | 24.743% | 24.868% | 1.55212 | 1.55212 | 1.55106 | FAIL |
| 2 | 3.852% | 3.852% | 3.869% | 18.538% | 18.538% | 18.630% | 1.58881 | 1.58881 | 1.58817 | FAIL |
| 3 | 2.849% | 2.849% | 2.860% | 14.235% | 14.235% | 14.305% | 1.61069 | 1.61069 | 1.61028 | FAIL |
| 4 | 2.818% | 2.818% | 2.829% | 11.252% | 11.252% | 11.306% | 1.62446 | 1.62446 | 1.62419 | FAIL |
| 5 | 2.818% | 2.818% | 2.829% | 9.184% | 9.184% | 9.226% | 1.63341 | 1.63341 | 1.63323 | FAIL |
| 6 | 2.818% | 2.818% | 2.829% | 7.749% | 7.749% | 7.784% | 1.63936 | 1.63936 | 1.63924 | SELECTED |
| 7 | 2.818% | 2.818% | 2.829% | 6.755% | 6.755% | 6.785% | 1.64336 | 1.64336 | 1.64328 | PASS |

实际计算选择最小通过值 `P_*=6`；该值不是输入参数。

### Empirical convergence（128/256 仅 diagnostic）

| case | N | direction | implementation error | continuous-reference error | fitted slope |
|---|---:|:---:|---:|---:|---:|
| finite | 128 | x | 4.394% | 1.452% | 1.63424 |
| finite | 128 | y | 3.901% | 6.608% | 1.59956 |
| finite | 128 | 45 | 0.881% | 1.973% | 1.61832 |
| finite | 256 | x | 1.482% | 1.378% | 1.62346 |
| finite | 256 | y | 1.976% | 4.738% | 1.60751 |
| finite | 256 | 45 | 0.661% | 2.187% | 1.61792 |
| finite | 512 | x | 0.587% | 3.388% | 1.61557 |
| finite | 512 | y | 0.084% | 2.736% | 1.61836 |
| finite | 512 | 45 | 0.806% | 2.046% | 1.61902 |
| kolmogorov | 128 | x | 4.143% | 3.929% | 1.65596 |
| kolmogorov | 128 | y | 0.565% | 7.229% | 1.64402 |
| kolmogorov | 128 | 45 | 2.628% | 5.362% | 1.65103 |
| kolmogorov | 256 | x | 1.273% | 6.575% | 1.64522 |
| kolmogorov | 256 | y | 1.281% | 6.568% | 1.64450 |
| kolmogorov | 256 | 45 | 3.086% | 4.939% | 1.65120 |
| kolmogorov | 512 | x | 0.573% | 7.169% | 1.63968 |
| kolmogorov | 512 | y | 0.601% | 8.304% | 1.63632 |
| kolmogorov | 512 | 45 | 0.198% | 7.967% | 1.63778 |

### Formal 512-screen bootstrap

| case | direction | impl point | impl 95% UB | amplitude point | amplitude 95% UB | slope point | slope 95% CI | result |
|---|:---:|---:|---:|---:|---:|---:|---:|:---:|
| finite | x | 0.587% | 2.584% | 3.388% | 5.261% | 1.61557 | [1.60577, 1.62546] | PASS |
| finite | y | 0.084% | 2.306% | 2.736% | 4.446% | 1.61836 | [1.60915, 1.62821] | PASS |
| finite | 45 | 0.806% | 2.776% | 2.046% | 3.800% | 1.61902 | [1.60978, 1.62892] | PASS |
| kolmogorov | x | 0.573% | 3.605% | 7.169% | 9.790% | 1.63968 | [1.62632, 1.65222] | PASS |
| kolmogorov | y | 0.601% | 3.278% | 8.304% | 10.615% | 1.63632 | [1.62405, 1.64893] | FAIL |
| kolmogorov | 45 | 0.198% | 3.490% | 7.967% | 10.483% | 1.63778 | [1.62498, 1.65109] | FAIL |

finite slope 仅为 diagnostic；冻结的 formal slope criterion 只适用于 Kolmogorov case。

#### Formal failure classification and location

本次属于合同定义的 **C 类失败**：三方向 implementation-recovery 95% UB 均低于 5%，说明 random coefficient variance、Hermitian fill、subharmonic ownership、valid-pair estimator 与 bootstrap aggregation 能恢复 `D_disc,6`；但 discrete representation 相对 continuous Kolmogorov reference 的负偏差随 separation 增大，叠加 formal sampling uncertainty 后使 y/45° amplitude UB 超过 10%。

| direction | deterministic median bias magnitude | empirical median point | formal 95% UB | 主要偏差区域 | endpoint signed bias and 95% CI |
|:---:|---:|---:|---:|---|---|
| y | 7.749% | 8.304% | 10.615% | `rho >= 30.469 mm` 时点估计低估超过 10% | `rho=65.000 mm`: -13.511%, `[-17.951%, -8.550%]` |
| 45° | 7.784% | 7.967% | 10.483% | `rho >= 40.217 mm` 时点估计低估超过 10% | `rho=64.634 mm`: -12.678%, `[-17.367%, -7.410%]` |

x 方向 amplitude 95% UB 为 9.790%，仅窄幅通过。`P=7` 的 deterministic error 更低不是改用 `P=7` 的授权理由；冻结规则要求选择最小通过 guard 的 `P_*=6`，本轮不得在看见结果后改变 P。

## 5. 证据入口

- 权威合同：`docs/SCIENTIFIC_CONTRACT_DRAFT.md`、`docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V01.md`、`docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V02.md`。
- 代码：`src/turbulence_jitter/gate_b.py`、`scripts/run_gate_b_core.py`、`scripts/run_gate_b_formal.py`。
- seeds：`{"finite_bootstrap_seed": 2026080813, "finite_formal_screen_seed": 2026080811, "kolmogorov_bootstrap_seed": 2026080814, "kolmogorov_formal_screen_seed": 2026080812, "v4_screen_seed": 2026080801}`；均在 formal screens 生成前写入 `metadata.json`。
- 机器结果：`results/gate_b_v5_formal/metadata.json`、`deterministic_ladder.json`、`v4_summary.json`、两份 `*_screen_observables.npz`、`bootstrap_summary.json`。
- 运行起始 commit SHA：`650064f7e0390cb4028f8ab6c4387096c890f0c2`；Draft PR #5。

## 6. 结论边界

- 已支持：V4 base-FFT PSD absolute level/slope；deterministic low-frequency depth；V5 empirical implementation recovery；finite-scale amplitude；Kolmogorov slope。
- 部分支持：Kolmogorov amplitude 点估计接近 deterministic expectation，但 y/45° formal 95% UB 未通过 10% gate；不得升级为 V5 amplitude PASS。
- 仍开放：V6–V12 propagation-level beam wander、long-term radius、scintillation、screen-number、production grid 与 split-step validation。
- 禁止宣称：完整 turbulence simulation 已正确、production multi-screen 已收敛、structured fields 已实现或任何 beam family 已获得性能优势。

## 7. 项目决策

**REVISE — GATE B NOT YET QUALIFIED**
