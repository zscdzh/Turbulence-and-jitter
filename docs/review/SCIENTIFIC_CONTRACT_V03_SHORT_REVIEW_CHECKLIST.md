# Scientific Contract v0.3 Candidate — Short Review Checklist

**用途：** 这是 code gate 前的短审，不是重新进行 Stage-A broad literature review。

**待审合同：** `../SCIENTIFIC_CONTRACT_DRAFT.md`

请只回答以下五组问题。

## 1. scope / field formulas

- coherent deterministic single-aperture + direct-detection finite-aperture scope 是否足够清楚？
- Gaussian / circular `J0` / OPB / flat-top 四场是否属于机制足够不同、且同一 receiver task 下可比的最小集合？
- OPB corrected `W(z)=1/(4 k beta z)`、`A(r)=Gaussian`、`W(L)/a_T=0.35` 是否 dimensionally / physically self-consistent？
- flat-top canonical nested multi-Gaussian expression 是否自洽，`N=1` 是否正确退化到 Gaussian？

输出：`PASS / REVISE`，只列真正阻塞实现的问题。

## 2. primary physical scene

检查：

- `lambda=1550 nm`；
- `L=1 km`；
- `D_T=D_R=50 mm`；
- constant-`Cn2` primary horizontal path；
- `Cn2=3e-15,1e-14,3e-14 m^-2/3`；
- `L0=10 m`, `l0=5 mm` baseline，5/20 m 与 3/10 mm sensitivity。

问题：

- 是否足以作为“representative mechanism scene”，同时没有冒充 universal UAV terminal？
- 是否有一个数值明显不合理到会让第一轮结果失去物理意义？

不要因为存在其他可选 UAV 场景而要求重新做广泛场景调研。

## 3. fairness / optimized Gaussian

检查：

- Level A common resource；
- Level B no-disturbance `r80_R`-matched one-scale retuning；
- G1 `w_G/a_T in [0.35,0.95]`；
- `L/f_G in {0,0.5,1,1.5,2}`；
- G1 objective = `Q5%(H)`；
- per `(tau,j,alpha_R)` optimization；
- `N_opt=256`, `N_eval=1024`, disjoint ensembles；
- `N_confirm=4096` only near unresolved claimed boundaries。

请判断是否：

- 对 Gaussian 足够强；
- 对 structured fields 没有隐性多自由度；
- 不会明显产生 selection bias。

## 4. Gaussian numerical-validation table

检查 V0–V12：

- free-space power / Gaussian analytic propagation；
- finite-aperture displacement；
- analytic jitter；
- phase PSD / structure function；
- low-frequency beam wander；
- long-term radius / scintillation；
- screen number；
- grid/window；
- propagation sampling；
- maximum-tilt wrap-around / aliasing。

只指出：

- 缺失的必要 observable；
- 明显过松或不现实的 tolerance；
- 会导致假收敛的验收方式。

不要增加与 Paper 1 科学结论无关的工程 CI / exhaustive audit。

## 5. final code-gate decision

请给一个且仅一个：

- `PASS — AUTHORIZE GAUSSIAN-ONLY IMPLEMENTATION`；
- `REVISE — KEEP CODE GATE CLOSED`；
- `STOP — SCIENTIFIC CONTRACT FUNDAMENTALLY INVALID`。

如果是 `REVISE`，最多列 **3 个**必须修改的 blocker。

即使 PASS，也只授权按顺序：

1. Gaussian free-space；
2. finite-aperture displacement；
3. analytic jitter；
4. Gaussian multi-screen validation；
5. Bessel literature reproduction sanity；
6. 最后才 structured-field common comparison。

**PASS 不等于授权直接运行 structured-beam Monte Carlo。**
