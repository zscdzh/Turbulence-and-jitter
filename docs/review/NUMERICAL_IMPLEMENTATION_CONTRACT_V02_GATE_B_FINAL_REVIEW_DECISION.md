# Numerical Implementation Contract v0.2 — Gate-B 最终审查裁决

**日期：2026-08-08**  
**Decision：PASS — AUTHORIZE GATE B V4–V5 CORE IMPLEMENTATION**  
**Scientific Contract：v0.3.2 remains frozen**  
**对应实现合同：`docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V02.md`**

本文件记录 Gate B 的最终短审裁决。无需重新进行物理方向或 phase-screen 文献审查。

## 已确认通过

- V4 验证 base FFT spectral normalization，V5 验证 base FFT + low-frequency augmentation 的完整 spatial statistics；
- cycles/m 到 mathematical PSD 的映射不再额外乘除 `(2pi)^2`；
- `E|a|^2=S_phi df^2` 与 NumPy `norm="backward"` 下 `F=N^2 a` 一致；
- FFT independent half-plane、四个 self-conjugate bins 与 subharmonic 四个 independent cells 的 Hermitian ownership 唯一且无重复；
- `D_disc` 使用完整正负频率集合，外部 structure-function 系数 2 正确；
- deterministic low-frequency-depth selection 与 empirical confirmation 已完全分离；
- 当前规则下外审独立重算显示 Kolmogorov deterministic median error 从 P=4 的约 11.4% 降至 P=7 的约 6.9%，8% implementation guard 合理，但实际 `P_*` 必须由代码的 deterministic calculation 决定；
- 128/256 只作为 convergence diagnostics，512 是唯一 formal empirical PASS ensemble；
- formal bootstrap 以 screen ID 为 resampling unit，2000 次 bootstrap，单侧 upper bound 取 95th percentile，slope interval 取 2.5th–97.5th percentile。

## Authorization

现在允许实现：

1. base-FFT phase-screen coefficient generator；
2. Hermitian filling；
3. V4 PSD qualification；
4. recursive subharmonics；
5. deterministic `D_disc,P`；
6. deterministic `P_*` selection；
7. minimal empirical structure-function sanity run；
8. 后续按合同执行 formal 512-screen V5 empirical confirmation。

## Still not authorized

- propagation-level beam wander / scintillation claims；
- production multi-screen Monte Carlo；
- production grid / screen-number freeze；
- G1 optimization；
- Bessel / OPB / flat-top；
- structured-field comparison。

## Final decision

> **PASS — AUTHORIZE GATE B V4–V5 CORE IMPLEMENTATION**
>
> **SCIENTIFIC CONTRACT v0.3.2 REMAINS FROZEN**
>
> **V6–V12 PROPAGATION-LEVEL IMPLEMENTATION REMAINS NOT YET AUTHORIZED**
>
> **STRUCTURED-FIELD IMPLEMENTATION REMAINS NOT AUTHORIZED**
