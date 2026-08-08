# Gate B V4–V5 Core — Initial Verification Results

**日期：2026-08-08**  
**状态：CORE IMPLEMENTATION CHECKED — FORMAL V5 NOT YET RUN**  
**合同：`docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V02.md`**

本记录对应 Gate-B 核心实现的提交前独立原型核算。原型使用与仓库 `gate_b.py` / `run_gate_b_core.py` 相同的冻结公式、Hermitian ownership、subharmonic representation、方向集合和 seeds 逻辑。当前运行环境不能直接联网 clone GitHub，因此本文件不把这些数值表述为“仓库分支 runner 已独立复跑”。正式 512-screen + bootstrap V5 尚未执行。

---

## 1. Qualification parameters

- `lambda = 1550 nm`
- `Cn2 = 1e-14 m^(-2/3)`
- `Delta z = 125 m`
- `L0 = 10 m`
- `l0 = 5 mm`
- `N = 512`
- `dx = 1.015625 mm`
- `Lwin = 0.520 m`
- `df = 1.923076923 cycles/m`
- `r0_screen = 0.273295177 m`

---

## 2. V4 base-FFT PSD

128 independent base-FFT screens，使用 frozen Hermitian ownership 与 `norm="backward"` IFFT。

12 annuli 的 pixel counts：

`[44, 56, 104, 188, 312, 540, 928, 1576, 2716, 4672, 8008, 13748]`

全部大于冻结 minimum 20 pixels。

结果：

- median annular PSD relative error = **0.2548%**；
- numerical log-log slope = **-3.88589**；
- exact modified-von-Kármán target slope = **-3.88809**；
- slope difference = **0.00221**；
- real-screen Hermitian sanity 的 imaginary residual 约为 `8e-16` 量级。

因此当前原型明显满足：

- PSD median level error `<=10%`；
- target-slope disagreement `<=0.10`。

> **Initial V4 result: PASS.**

该结果只验证 base FFT spectrum normalization，不验证 low-frequency completeness。

---

## 3. Independent finite-scale reference

finite-scale structure-function reference 使用 atmospheric-measure continuous quadrature：

\[
D_{\phi,\rm finite}(\rho)=
4\pi\int_0^\infty
\kappa\Phi_\phi^{(\rm atm)}(\kappa)
[1-J_0(\kappa\rho)]d\kappa.
\]

对冻结 x/y/45° separation points，以 `epsrel=1e-8` 与 `1e-10` 两次独立积分比较，最大相对变化约：

\[
5.8\times10^{-14},
\]

远小于合同要求的 `1e-4` reference convergence threshold。

---

## 4. Deterministic low-frequency-depth selection

下表是 algorithmic discrete expectation `D_disc,P` 与 continuous references 的比较。

| P | finite x/y median error | finite 45° | Kolmogorov x/y | Kolmogorov 45° | K slope x/y | K slope 45° |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 2.818% | 2.829% | 11.252% | 11.306% | 1.62446 | 1.62419 |
| 5 | 2.818% | 2.829% | 9.184% | 9.226% | 1.63341 | 1.63323 |
| 6 | 2.818% | 2.829% | 7.749% | 7.784% | 1.63936 | 1.63924 |
| 7 | 2.818% | 2.829% | 6.755% | 6.785% | 1.64336 | 1.64328 |

8% / 0.08 deterministic selection guard 下：

- `P=5` 因 Kolmogorov amplitude error > 8% 而失败；
- `P=6` 三方向 amplitude error < 8%；
- `P=6` 的 slope error 相对 `5/3` 约 0.0274，也小于 0.08。

因此当前冻结离散规则实际选择：

\[
\boxed{P_*=6}.
\]

这不是预先写死的参数，而是 deterministic calculation 的输出。

finite-scale error 在 `P≈2` 后已基本饱和于约 2.8%；继续增加 subharmonic depth 主要在修复 Kolmogorov low-frequency deficit。

---

## 5. 128-screen empirical diagnostic — finite-scale

注意：128 screens 只属于 convergence / implementation sanity diagnostic，不属于正式 V5 PASS ensemble。

在 `P_*=6` 下，empirical structure function 与 deterministic `D_disc,6` 的 median relative error：

- x：**0.99%**；
- y：**1.37%**；
- 45°：**1.44%**。

与 continuous finite-scale reference 的 median relative error：

- x：**3.78%**；
- y：**1.49%**；
- 45°：**1.43%**。

这支持当前 random coefficient、Hermitian filling、subharmonic ownership 和 valid-pair estimator 没有明显的 factor-of-two / factor-of-half 实现错误。

---

## 6. 128-screen empirical diagnostic — Kolmogorov

同样仅为 diagnostic。

empirical vs deterministic `D_disc,6` median relative error：

- x：**1.66%**；
- y：**0.21%**；
- 45°：**2.91%**。

empirical vs analytic Kolmogorov reference median relative error：

- x：**6.22%**；
- y：**7.56%**；
- 45°：**5.10%**。

empirical fitted slopes：

- x：**1.64905**；
- y：**1.64199**；
- 45°：**1.65554**。

这些结果与 deterministic expectation 一致，并显示 128-screen sample 已进入合理区间；但根据冻结合同，不能据此宣布 formal V5 PASS。

---

## 7. 当前支持的结论

支持：

> base-FFT PSD normalization、Hermitian ownership、recursive subharmonic representation 与 deterministic `D_disc,P` 的核心实现逻辑在初步数值核对中相互一致；当前规则确定性选择 `P_*=6`。

部分支持：

> 128-screen empirical diagnostic 能恢复自身 deterministic structure function 到数个百分点以内，并与 continuous references 保持合理一致。

仍未完成：

- formal `N_ens=512` empirical V5；
- screen-ID bootstrap `B=2000`；
- implementation-recovery 95% upper bound；
- finite/Kolmogorov amplitude 95% upper bound；
- Kolmogorov slope 95% interval。

因此当前状态不是完整 Gate-B PASS，而是：

> **V4 INITIAL PASS + V5 CORE IMPLEMENTATION SUPPORTED; FORMAL V5 EMPIRICAL CONFIRMATION PENDING.**

不支持任何 beam-wander、scintillation、production multi-screen 或 structured-field 结论。
