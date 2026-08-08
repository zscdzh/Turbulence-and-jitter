# Gate B v0.2.2 Ensemble Remediation Decision

**日期：2026-08-08**  
**裁决：PASS — AUTHORIZE N_ens=1024 GATE-B v0.2.2 REMEDIATION**  
**Gate B qualification status：NOT YET QUALIFIED**  
**V6：CLOSED**

## 1. Review conclusion

外部审查实质支持 Option A：在 v0.2.1 deterministic low-frequency representation 已满足冻结 bias-headroom policy 的前提下，不修改 low-frequency generator，而将 formal empirical ensemble 从 512 提高到 1024。

审查要求在正式授权前关闭两个程序性条件：

1. 为 post-failure same-seed 1024 diagnostic 补齐唯一可复现 runner 与 source/environment/seed/bootstrap metadata；
2. 在 v0.2.2 中冻结一次性止损规则，禁止 fresh 1024 FAIL 后更换 seed 或继续扩大 ensemble。

两项均已完成。

---

## 2. Condition 1 — CLOSED

新增：

- `scripts/run_gate_b_postfailure_1024_diagnostic.py`
- `results/gate_b_v5_formal_v021/postfailure_1024_diagnostic/metadata.json`
- `results/gate_b_v5_formal_v021/postfailure_1024_diagnostic/summary.json`

runner 明确：

- 使用历史 v0.2.1 Kolmogorov screen seed `2026080832`；
- 保留失败的前 512 张并继续同一 RNG sequence 到 1024；
- bootstrap seed `2026080841`；
- `B_boot=2000`；
- bootstrap unit 为 screen ID；
- x/y/45° 共享同一套 resample-count weights；
- 输出 per-screen `D_phi(rho)` observables；
- 结果永久标记 diagnostic-only，不能作为 v0.2.2 formal PASS evidence。

已保存的 1024 per-screen observables 使用该 shared-weight bootstrap 重新计算时，逐项复现 committed `postfailure_1024_bootstrap2000.json` 到浮点精度。

因此该证据链缺口关闭。

---

## 3. Condition 2 — CLOSED

新 authoritative contract：

- `docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V022.md`

冻结：

- 唯一 formal ensemble `N_ens=1024`；
- 512 / 768 等 prefix 只能 diagnostic；
- deterministic P-selection 保持 v0.2.1：`P=0..12`, median <=6%, pointwise max <=10%, slope error <=0.08, 选择最小通过 P；
- `B_boot=2000` 与所有 formal thresholds 不变；
- 只允许一组全新、预先提交的 v0.2.2 formal seed family；
- 原 P=6 FAIL、v0.2.1 512 FAIL 和事后 1024 diagnostic 永久保留；
- 如果 fresh 1024 formal rerun 仍 FAIL，禁止换 seed、禁止继续到 2048、禁止再调整 deterministic threshold 追求 PASS；
- fresh 1024 FAIL 后必须转入 low-frequency representation / qualification-statistic review；
- V6 在 Gate B 正式 PASS 前继续关闭。

因此一次性止损治理条件关闭。

---

## 4. What remains unchanged

不重开或修改：

- Scientific Contract v0.3.2；
- phase PSD normalization；
- cycles/m ↔ rad/m mapping；
- FFT/IFFT normalization；
- Hermitian ownership；
- self-conjugate bins；
- random coefficient variance；
- recursive subharmonic coefficient formula；
- continuous finite-scale / analytic Kolmogorov references；
- V4 physics；
- formal 5% / 10% / slope thresholds。

---

## 5. Authorization

现在允许且仅允许：

> **一次 fresh, preregistered, N_ens=1024 Gate-B v0.2.2 formal V5 rerun。**

该授权不等于 Gate B PASS。

只有新的 fresh 1024 formal run 全部通过 `docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V022.md` 后，才可裁决：

> **PASS — GATE B V4–V5 QUALIFIED**

即使届时 PASS，也必须等待项目负责人明确授权才能进入 V6。

当前项目状态：

> **CONTINUE — v0.2.2 FORMAL RERUN AUTHORIZED; V6 REMAINS CLOSED.**
