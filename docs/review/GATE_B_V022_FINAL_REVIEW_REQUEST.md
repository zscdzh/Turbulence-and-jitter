# Gate B v0.2.2 Final Review Request

**日期：2026-08-08**  
**请求裁决：确认 fresh 1024-screen formal result 是否足以关闭 Gate B V4–V5**  
**当前内部裁决：PASS — GATE B V4–V5 QUALIFIED**  
**V6：尚未授权**

## 1. Review scope

本轮只请求确认 v0.2.2 fresh formal result 是否按照已授权 contract 完整 PASS。不要重开 Scientific Contract、PSD normalization、FFT/Hermitian 或 low-frequency representation，除非新结果本身显示明确矛盾。

## 2. Governance history

- v0.2 / P=6 formal FAIL：deterministic low-frequency margin 不足；
- v0.2.1 remediation：minimum-depth deterministic bias-headroom policy，fresh run 自动选 `P*=9`；
- v0.2.1 fresh 512-screen formal FAIL：Kolmogorov x empirical recovery/amplitude；
- post-failure 1024 continuation：仅 diagnostic；
- 外审支持 Option A，并要求：补齐 diagnostic reproducibility + 冻结一次性止损规则；
- v0.2.2 已冻结唯一 fresh 1024 seed family；若失败则禁止换 seed / 继续到 2048。

## 3. Fresh v0.2.2 result

Formal settings：`N_ens=1024`, `B_boot=2000`，其它 deterministic policy 与 formal thresholds 不变。

V4：PSD median error `0.2494%`，slope difference `0.002656`，PASS。

Deterministic ladder：自动选择 `P*=9`。

Finite-scale formal V5：x/y/45° 全部 PASS。

Kolmogorov formal V5：

| direction | impl 95% UB | amplitude 95% UB | slope 95% CI | result |
|---|---:|---:|---|:---:|
| x | 3.098% | 6.298% | [1.64303, 1.66016] | PASS |
| y | 2.370% | 7.732% | [1.63782, 1.65446] | PASS |
| 45° | 2.550% | 6.882% | [1.64026, 1.65741] | PASS |

Formal limits remain implementation UB ≤5%, amplitude UB ≤10%, slope CI fully inside `5/3 ± 0.10`.

## 4. Execution interruption disclosure

一次初始执行调用在 finite 第384张时因工具单次命令时限被外部强制终止，当时没有形成完整 ensemble 或 formal statistic。随后使用**完全相同、事前已提交的 seed family**从 screen 1 重启完整 run。未改变 seed、threshold、P-selection 或 ensemble size。

请审查该纯执行环境中断是否影响 one-shot governance interpretation。项目判断：不影响，因为没有观察到可用于选 seed/改规则的 formal result，且重启严格复用了同一 preregistered sequence。

## 5. Evidence

- `docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V022.md`
- `docs/review/GATE_B_V022_ENSEMBLE_REMEDIATION_DECISION.md`
- `scripts/run_gate_b_formal_v022.py`
- `docs/results/GATE_B_V4_V5_FORMAL_V022_RESULTS.md`
- `results/gate_b_v5_formal_v022/bootstrap_summary.json`
- `results/gate_b_v5_formal_v022/metadata.json`
- `results/gate_b_v5_formal_v022/deterministic_selection_summary.json`

Historical failed runs and diagnostic evidence remain preserved.

## 6. Requested decision

Recommended decision if the execution-interruption disclosure is accepted:

> **PASS — GATE B V4–V5 QUALIFIED; AUTHORIZE PREPARATION OF V6 IMPLEMENTATION CONTRACT**

This should not automatically authorize production propagation or structured fields. V6 should still begin from a separately frozen propagation-level implementation contract.
