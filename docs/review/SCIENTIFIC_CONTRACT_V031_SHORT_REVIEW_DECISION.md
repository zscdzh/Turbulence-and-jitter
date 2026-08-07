# Scientific Contract v0.3.1 短复核结论

**日期：2026-08-07**  
**Decision：REVISE — KEEP CODE GATE CLOSED**

本轮为 v0.3.1 的只读短复核。没有要求重开 Stage-A 文献调研，也没有改变 Paper 1 科学路线、core field set、primary physical scene、OPB 参数或 G1 优化策略。

## 1. 已通过项

### OPB finite-aperture feasibility — PASS

已核对：

- `beta = 4.4853e-9 m^-1`；
- `rho_s = 17.941 mm`；
- `r95_T = 19.368 mm = 0.7747 a_T`；
- hard-aperture lower bound `omega_OPB >= 0.3947`；
- `rho_s <= r95_T` lower bound `omega_OPB >= 0.5095`；
- primary `omega_OPB = 0.55` 满足 `rho_s < r95_T < a_T`；
- Level-B `omega_OPB in [0.55,0.90]` 整段满足 finite-aperture feasibility。

### G1 lower-tail optimization — PASS

已接受：

- 35 candidates share 256 common random realizations；
- Top-5 再补 768，finalist `N_opt=1024`；
- winner 仅由完整 1024 optimization set 决定；
- evaluation ensemble 与 optimization ensemble 完全独立；
- near-boundary confirmation 可扩至 4096。

当前不要求把全部 35 candidates 默认扩至 4096。

## 2. 唯一 remaining blocker：phase-spectrum `2pi` normalization

v0.3.1 同时采用了：

1. atmospheric-optics 常见的 refractive-index spectrum coefficient `0.033 Cn2` 与

   `Phi_phi^(atm) = 2 pi k^2 Delta-z Phi_n^(atm)`；

2. mathematical Fourier convention

   `phi(r) = integral d^2kappa/(2pi)^2 phi_tilde(kappa) exp(i kappa.r)`。

若直接把同一个 `Phi_phi` 同时放入第二套 convention，则 phase structure-function amplitude 会被错误缩小 `(2pi)^2`。

Kolmogorov limit 必须满足：

\[
D_\phi(\rho)
=2.91 k^2 C_n^2\Delta z\,\rho^{5/3}
=6.88\left(\frac{\rho}{r_{0,\mathrm{screen}}}\right)^{5/3},
\]

其中

\[
r_{0,\mathrm{screen}}
=[0.423 k^2 C_n^2\Delta z]^{-3/5}.
\]

## 3. 接受的最小修订方向

项目采用以下唯一 convention，避免继续混用：

- 保留 mathematical Fourier measure `d^2kappa/(2pi)^2`；
- 将 atmospheric spectrum 与 mathematical PSD 显式分名；
- 定义

\[
\Phi_{\phi}^{(\mathrm{atm})}(\kappa)
=2\pi k^2\Delta z\,\Phi_n^{(\mathrm{atm})}(\kappa),
\]

但进入 mathematical Fourier covariance 的 PSD 必须为

\[
\boxed{
\Phi_{\phi}^{(\mathrm{math})}(\kappa)
=(2\pi)^2\Phi_{\phi}^{(\mathrm{atm})}(\kappa)
=(2\pi)^3k^2\Delta z\,\Phi_n^{(\mathrm{atm})}(\kappa)
}.
\]

V5 同时增加 Kolmogorov-limit absolute-amplitude gate，不只检查 `5/3` slope。

## 4. code gate

当前仍为：

> **REVISE — KEEP CODE GATE CLOSED**

完成上述单一 normalization blocker 后，只需进行一次极短复核；若通过，预计可授权 Gaussian-only implementation。

structured-field production comparison 仍需等待 Gaussian numerical chain 通过全部 validation gates。