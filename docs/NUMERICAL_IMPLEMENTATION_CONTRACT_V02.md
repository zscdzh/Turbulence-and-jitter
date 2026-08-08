# Numerical Implementation Contract v0.2 — Gate B

**日期：2026-08-08**  
**状态：PASS — AUTHORIZE GATE B V4–V5 CORE IMPLEMENTATION**  
**上位合同：Scientific Contract v0.3.2**  
**Gate A：V0–V3 remains authorized**  
**Propagation-level V6–V12：NOT YET AUTHORIZED**  
**Structured-field implementation：NOT AUTHORIZED**

本文件是 Gate B / V4–V5 的唯一 authoritative implementation contract。它合并此前 Gate-B R1/R2 proposal 的有效条款，并补入最终短审要求的 bootstrap/sequential rule。Scientific Contract v0.3.2 保持冻结。

---

## 1. Gate B 验证对象

### V4 — base-FFT spectral normalization

V4 只验证主 FFT phase-screen component：

\[
\phi_{\rm FFT}.
\]

验证对象包括：PSD absolute level、radial dependence / slope、FFT/PSD/frequency-cell normalization。V4 不使用 subharmonics。

### V5 — complete-screen spatial statistics

V5 验证：

\[
\phi_{\rm total}=\phi_{\rm FFT}+\phi_{\rm SH}.
\]

验证 finite-scale structure function、Kolmogorov absolute amplitude 与 5/3 slope。V5 必须包含 low-frequency augmentation。

---

## 2. Validation parameters

冻结 screen-level qualification slab：

\[
\lambda=1550\,\mathrm{nm},\qquad
C_n^2=10^{-14}\,\mathrm{m^{-2/3}},\qquad
\Delta z=125\,\mathrm m.
\]

finite-scale case：

\[
L_0=10\,\mathrm m,\qquad l_0=5\,\mathrm{mm}.
\]

qualification grid：

\[
N=512,
\qquad
\Delta x=1.015625\,\mathrm{mm},
\qquad
L_{\rm win}=N\Delta x=0.520\,\mathrm m.
\]

\[
\Delta f=1/L_{\rm win}.
\]

该 grid 只用于 screen-level qualification，不是 production grid。

Kolmogorov screen Fried parameter：

\[
r_{0,\rm screen}=[0.423k_0^2C_n^2\Delta z]^{-3/5}\approx273.3\,\mathrm{mm}.
\]

---

## 3. PSD convention — FROZEN

Scientific Contract 使用 angular spatial frequency：

\[
\kappa_x=2\pi f_x,\qquad \kappa_y=2\pi f_y.
\]

finite-scale atmospheric refractive-index spectrum：

\[
\Phi_n^{(\rm atm)}(\kappa)=0.033C_n^2
\frac{\exp[-(\kappa/\kappa_m)^2]}
{(\kappa^2+\kappa_0^2)^{11/6}},
\]

\[
\kappa_0=2\pi/L_0,\qquad \kappa_m=5.92/l_0.
\]

mathematical phase PSD：

\[
\Phi_\phi^{(\rm math)}(\kappa)=(2\pi)^3k_0^2\Delta z\,\Phi_n^{(\rm atm)}(\kappa).
\]

cycles-grid PSD 唯一定义：

\[
\boxed{S_\phi(f_x,f_y)=\Phi_\phi^{(\rm math)}(2\pi f_x,2\pi f_y)}.
\]

因为：

\[
\frac{d^2\kappa}{(2\pi)^2}=d^2f.
\]

不得额外乘除 \((2\pi)^2\)。

Kolmogorov qualification 必须直接使用解析 branch：

\[
\Phi_n^{(K)}(\kappa)=0.033C_n^2\kappa^{-11/3},\qquad \kappa>0,
\]

不得通过 `L0=np.inf` 或 `l0=0` 调用 finite-scale branch。DC 始终设为零。

---

## 4. Base-FFT coefficient normalization

对普通 Fourier cell：

\[
E|a_{uv}|^2=S_\phi(f_u,f_v)\Delta f^2.
\]

NumPy FFT/IFFT 显式使用：

`norm="backward"`。

因此交给 centered inverse FFT 的数组为：

\[
\boxed{F_{uv}=N^2a_{uv}}.
\]

最终：

\[
\phi_{\rm FFT}=\mathcal F_c^{-1}[F].
\]

---

## 5. Base-FFT Hermitian ownership — UNIQUE

centered integer Fourier indices：

\[
u,v\in\{-N/2,\ldots,N/2-1\}.
\]

independent set：

\[
\boxed{
\mathcal H_{\rm FFT}=
\{v=1,\ldots,N/2-1,\ \forall u\}
\cup\{v=0,\ u=1,\ldots,N/2-1\}
\cup\{v=-N/2,\ u=1,\ldots,N/2-1\}
}.
\]

其数量为：

\[
(N^2-4)/2.
\]

每个 independent bin 只抽样一次：

\[
\xi=(X+iY)/\sqrt2,\qquad X,Y\overset{\rm iid}{\sim}\mathcal N(0,1),
\]

\[
a_{uv}=\Delta f\sqrt{S_\phi(f_u,f_v)}\,\xi.
\]

partner 完全由：

\[
\boxed{a_{-u,-v}=a_{uv}^*}
\]

填充。禁止 partner 二次独立抽样。

四个 self-conjugate bins：

\[
(0,0),\ (-N/2,0),\ (0,-N/2),\ (-N/2,-N/2).
\]

其中 DC：

\[
a_{00}=0.
\]

另外三个使用实 Gaussian \(\eta\sim\mathcal N(0,1)\)，保持相同 cell variance。Nyquist self-conjugate bins 不进入 V4 resolved band。

---

## 6. V4 resolved band 与 annuli

\[
\boxed{f_{\min}=4/L_{\rm win}},\qquad
\boxed{f_{\max}=0.20/\Delta x}.
\]

数值约为：

\[
7.692\le f\le196.923\ \mathrm{cycles/m}.
\]

12 个 annuli 的 edges 一次性定义为：

\[
\boxed{e_k=\operatorname{geomspace}(f_{\min},f_{\max},13)}.
\]

第 \(k\) 环：\(e_k\le f<e_{k+1}\)，最后一环包含右端点。代表频率：

\[
\boxed{f_k=\sqrt{e_ke_{k+1}}}.
\]

每个 annulus 至少 20 个 Fourier pixels；否则该 qualification grid 不具备 V4 资格。numerical 与 target PSD 必须使用完全相同的 annulus pixel membership。

baseline \(l_0=5\) mm 对应：

\[
f_m=5.92/(2\pi l_0)\approx188.44\ \mathrm{cycles/m}.
\]

因此 V4 slope 不强制整个 band 服从固定 \(-11/3\)。

---

## 7. V4 estimator 与 acceptance

每张 screen 重建：

\[
F^{(\rm rec)}=\mathcal F_c[\phi_{\rm FFT}].
\]

单-bin estimator：

\[
\boxed{
\widehat S_\phi(f_u,f_v)=
\frac{\langle|F^{(\rm rec)}_{uv}|^2\rangle}
{N^4\Delta f^2}
}.
\]

V4 core qualification 使用 128 个 independent screens。

每个 annulus 的 target PSD 为同一 pixels 上 exact modified-von-Kármán PSD 的平均。annular relative level error：

\[
\epsilon_k=\left|\frac{\widehat S_k}{S_{k,\rm target}}-1\right|.
\]

要求：

\[
\boxed{\operatorname{median}_k\epsilon_k\le10\%}.
\]

numerical 与 target slope 均在相同 12 个 annular points 上对 \(\log S\) vs \(\log f_k\) 做 linear least-squares，要求：

\[
\boxed{|s_{\rm num}-s_{\rm target}|\le0.10}.
\]

---

## 8. Recursive subharmonics

第 \(p\) 层：

\[
\Delta f_p=\Delta f/3^p,\qquad p=1,2,\ldots,P.
\]

完整八点：

\[
(i,j)\in\{-1,0,1\}^2\setminus\{(0,0)\}.
\]

只对四个 independent cells 抽样：

\[
\boxed{\mathcal H_{\rm SH}=\{(1,0),(0,1),(1,1),(1,-1)\}}.
\]

\[
a_{ij}^{(p)}=\Delta f_p\sqrt{S_\phi(i\Delta f_p,j\Delta f_p)}\,\xi_{ij}^{(p)}.
\]

其余四点完全由：

\[
a_{-i,-j}^{(p)}=(a_{ij}^{(p)})^*
\]

填充。不同 level、screen、非共轭 cell 相互独立。

每层 field 必须按完整八点求和：

\[
\boxed{
\phi_{\rm SH}^{(p)}(x,y)=
\sum_{(i,j)\ne(0,0)}
a_{ij}^{(p)}e^{i2\pi(i\Delta f_px+j\Delta f_py)}
}.
\]

填满八点后禁止再次使用 `2*Re(...)`，否则重复计数。

完整 screen：

\[
\phi_{\rm total}=\phi_{\rm FFT}+\sum_{p=1}^{P}\phi_{\rm SH}^{(p)}.
\]

---

## 9. Deterministic discrete structure function

在任何 Monte Carlo screen 之前，先计算算法自身精确离散期望：

\[
D_{\rm FFT}(\boldsymbol\rho)=
2\sum_{q\in\rm FFT}S_q\Delta f^2
[1-\cos(2\pi q\cdot\boldsymbol\rho)],
\]

\[
D_{\rm SH,P}(\boldsymbol\rho)=
2\sum_{p=1}^{P}\sum_{q\in\rm SH_p}
S_q\Delta f_p^2
[1-\cos(2\pi q\cdot\boldsymbol\rho)],
\]

\[
\boxed{D_{\rm disc,P}=D_{\rm FFT}+D_{\rm SH,P}}.
\]

和式已包含完整正负频率集合，禁止外部再补共轭倍数。

---

## 10. V5 direction set

### +x

\[
n_\rho=[4,5,7,9,11,14,18,23,30,39,50,64],
\]

\[
\boldsymbol\rho_x=(n_\rho\Delta x,0).
\]

### +y

\[
\boldsymbol\rho_y=(0,n_\rho\Delta x).
\]

### 45°

\[
\boxed{n_{45}=[3,4,5,6,8,10,13,16,21,28,35,45]},
\]

\[
\boldsymbol\rho_{45}=(n_{45}\Delta x,n_{45}\Delta x),
\qquad
|\boldsymbol\rho_{45}|=\sqrt2n_{45}\Delta x.
\]

三个方向必须分别报告和验收，不允许先平均。

empirical estimator 只使用 valid/non-wrapped pairs；禁止 periodic `roll`。

---

## 11. Independent continuous references

finite-scale reference 使用 atmospheric measure：

\[
\boxed{
D_{\phi,\rm finite}(\rho)=
4\pi\int_0^\infty
\kappa\Phi_\phi^{(\rm atm)}(\kappa)
[1-J_0(\kappa\rho)]d\kappa
}.
\]

该 quadrature 必须与 generator 不共享 discrete-frequency code、FFT normalization 或 empirical generator，并对全部冻结 \(\rho\) 达到：

\[
\boxed{\text{relative quadrature convergence}<10^{-4}}.
\]

Kolmogorov reference 直接使用：

\[
\boxed{D_{\phi,K}(\rho)=6.88(\rho/r_{0,\rm screen})^{5/3}}.
\]

---

## 12. Deterministic P-selection

预注册：

\[
P=0,1,2,3,4,5,6,7.
\]

在生成任何 empirical screen 前，完成全部 deterministic comparison。

Scientific Contract 正式 V5 threshold 仍为 10%，但为避免在验收边界附近依赖 Monte Carlo fluctuation，P-selection 使用 implementation guard：

\[
\boxed{8\%}
\]

以及 Kolmogorov slope guard：

\[
\boxed{0.08}.
\]

选择满足以下条件的最小 \(P=P_*\)：

- finite-scale：x/y/45° 三方向各自 median relative error \(\le8\%\)；
- Kolmogorov amplitude：三方向各自 median relative error \(\le8\%\)；
- Kolmogorov slope：三方向各自 \(|s_{\rm disc}-5/3|\le0.08\)。

若 \(P\le7\) 无任何值满足，则停止：

> **REVISE — LOW-FREQUENCY REPRESENTATION**

不得用更多 Monte Carlo realizations 修复 deterministic bias。

实际 deterministic calculation 决定 \(P_*\)；不得预先写死 \(P_*=6\)。

---

## 13. Empirical confirmation 与 seeds

确定 \(P_*\) 后才允许生成 empirical screens。

deterministic selection 不使用 random seeds。empirical confirmation 使用完全独立、预注册、可重现的 seed family；不得复用 realization 来选择 \(P_*\)。

128 与 256 只作为 convergence diagnostics；

\[
\boxed{N_{\rm ens}=512}
\]

是唯一 formal PASS ensemble。

512 个 screens 内部可以保留 nested 128/256 diagnostic prefixes，但正式裁决只看全部 512。

---

## 14. Empirical implementation-recovery check

先比较 generator empirical statistics 与自身 deterministic expectation：

\[
E_{\rm impl}=\operatorname{median}_{\rho}
\left|\frac{D_{\rm emp}-D_{\rm disc,P_*}}{D_{\rm disc,P_*}}\right|.
\]

正式要求三方向各自满足：

\[
\boxed{\text{95\% bootstrap upper bound of }E_{\rm impl}\le5\%}.
\]

即使 empirical screen 偶然更接近 continuous reference，只要不能恢复自身 deterministic expectation，也不得 PASS。

---

## 15. Bootstrap — UNIQUE RULE

formal ensemble 固定为 512 screens。

bootstrap 单位是 **screen ID**，不是 spatial pixels。

冻结：

\[
\boxed{B_{\rm boot}=2000}.
\]

运行前记录 bootstrap seed。

每个 bootstrap resample：

1. 从 512 个 screen IDs 中有放回抽取 512 个；
2. 重新计算 ensemble-mean \(D(\rho)\)；
3. 再计算跨冻结 \(\rho\) 的 median relative error；
4. 对 Kolmogorov case 重新拟合 slope。

single-sided 95% upper bound 取 2000 个 bootstrap statistics 的 95th percentile。

slope 95% interval 取 2.5th–97.5th percentile。

128/256 diagnostic results 不参与 formal sequential hypothesis testing，因此不需要 Bonferroni 或 alpha-spending。

---

## 16. Empirical V5 formal PASS

对 x/y/45° 三方向分别要求：

### implementation recovery

\[
\boxed{\text{95\% upper bound}(E_{\rm impl})\le5\%}.
\]

### finite-scale amplitude

\[
\boxed{
\text{95\% upper bound of }
\operatorname{median}_{\rho}
\left|\frac{D_{\rm emp}-D_{\rm finite}}{D_{\rm finite}}\right|
\le10\%
}.
\]

### Kolmogorov amplitude

\[
\boxed{
\text{95\% upper bound of }
\operatorname{median}_{\rho}
\left|\frac{D_{\rm emp}-D_K}{D_K}\right|
\le10\%
}.
\]

### Kolmogorov slope

bootstrap 95% slope interval 必须完整落在：

\[
\boxed{5/3\pm0.10}
\]

之内。

---

## 17. Low-frequency diagnostic boundary

此前约 24.6% → 61.5% 的 missing-low-frequency estimate 是 pure-Kolmogorov、continuous circular cutoff \(f<1/L_{\rm win}\) 的诊断结果，只用于证明 base FFT 不能单独承担 V5。

它不是 finite-\(L_0\) exact error、square FFT grid 的逐点 bias，也不是特定 \(P\) 的误差预测。正式 deterministic error 必须由 \(D_{\rm disc,P}\) 与 continuous reference 决定。

---

## 18. Gate-B implementation authorization

从本合同起，授权且仅授权：

1. finite-scale / Kolmogorov PSD functions；
2. base-FFT Hermitian coefficient generator；
3. V4 PSD estimator / annular qualification；
4. recursive subharmonic generator；
5. deterministic \(D_{\rm disc,P}\)；
6. deterministic \(P_*\) selection；
7. valid-pair empirical structure-function estimator；
8. minimal empirical sanity run；
9. formal 512-screen empirical V5 confirmation 与 frozen bootstrap procedure。

不授权：

- beam-wander qualification；
- scintillation qualification；
- production multi-screen Monte Carlo；
- production grid / screen-number freeze；
- G1 optimization；
- Bessel / OPB / flat-top；
- structured-field comparison。

---

## 19. Gate-B conclusion boundary

Gate B PASS 只支持：

> phase-screen spectrum normalization 与 screen-level spatial statistics 已通过 absolute qualification，可进入 V6–V8 propagation-level implementation review。

它不支持 beam wander、long-term radius、scintillation、screen-number convergence、production-grid convergence 或 structured-field conclusions。
