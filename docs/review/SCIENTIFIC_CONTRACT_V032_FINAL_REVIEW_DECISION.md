# Scientific Contract v0.3.2 最终归一化复核结论

**日期：2026-08-07**  
**Decision：PASS — AUTHORIZE GAUSSIAN-ONLY IMPLEMENTATION**

本文件记录 Scientific Contract v0.3.2 的最终极短复核。它不覆盖或改写此前的 v0.3 / v0.3.1 审查记录。

## 1. 已确认通过的归一化链

v0.3.2 显式区分 atmospheric PSD 与 mathematical Fourier PSD：

\[
\Phi_\phi^{(\mathrm{math})}
=(2\pi)^2\Phi_\phi^{(\mathrm{atm})}.
\]

在 mathematical Fourier convention

\[
\phi(\mathbf r)=\int\frac{d^2\kappa}{(2\pi)^2}
\tilde\phi(\boldsymbol\kappa)e^{i\boldsymbol\kappa\cdot\mathbf r}
\]

下，该 `(2pi)^2` conversion 与 integration measure 严格抵消，因此 mathematical 与 atmospheric 两种 phase-structure-function integral 完全等价。

## 2. Kolmogorov absolute amplitude — PASS

合同冻结：

\[
D_\phi(\rho)
=2.91k^2C_n^2\Delta z\,\rho^{5/3}
=6.88\left(\frac{\rho}{r_{0,\mathrm{screen}}}\right)^{5/3},
\]

\[
r_{0,\mathrm{screen}}
=[0.423k^2C_n^2\Delta z]^{-3/5}.
\]

由于 `6.88 × 0.423 = 2.91024`，两种写法与合同自身 Fried-parameter convention 一致。

## 3. V4 / V5 / propagation-level validation chain — PASS

- V4 检查 phase-screen PSD level 与 slope；
- V5 同时检查 finite-scale continuous integral、Kolmogorov absolute amplitude `6.88(rho/r0_screen)^(5/3)` 与 `5/3` slope；
- V6 / V7 继续用独立 beam-wander / long-term-radius references 检查传播后统计；
- 因此 generator 与 reference 不再可能仅依靠共享同一个错误 `(2pi)` normalization 而“自洽假通过”。

## 4. 前序 blocker 状态

以下在上一轮已 PASS，本轮不重新打开：

- OPB finite-aperture feasibility；
- G1 lower-tail staged CRN optimization；
- primary physical scene；
- mechanism set / novelty route；
- Level A / Level B fairness contract。

没有发现需要重新开启 Stage-A broad literature review 或修改 Paper-1 / Paper-2 路线的新问题。

## 5. Code authorization

从本 decision 起，授权范围仅为 **Gaussian-only implementation**：

1. Gaussian free-space propagation；
2. finite-aperture displacement / capture；
3. analytic jitter benchmark；
4. Gaussian phase-screen / multi-screen numerical validation V0–V12。

明确仍不授权：

- Bessel production comparison；
- OPB production comparison；
- flat-top production comparison；
- structured-field Monte Carlo；
- Paper-2 joint beam optimization。

只有 Gaussian numerical chain 完成并通过全部 V0–V12 后，才允许重新打开 structured-field implementation gate。

## 6. 当前项目状态

> **Scientific Contract v0.3.2: PASS FOR GAUSSIAN-ONLY IMPLEMENTATION**
>
> **Gaussian numerical qualification: AUTHORIZED**
>
> **Structured-field implementation: NOT AUTHORIZED**
>
> **Formal structured-beam numerical results: NONE**
