# SCIENTIFIC_CONTRACT_EVIDENCE_DELTAS

状态：滚动证据账本。这里记录已经经过逐篇文献审查并由项目负责人接受、但尚未统一并入 `docs/SCIENTIFIC_CONTRACT_DRAFT.md` 的契约增量。

原则：

- 只记录有明确文献来源且已经讨论接受的定义或边界；
- 仿真展示参数不自动升级为项目场景参数；
- 每条增量保留来源文献与证据角色；
- 等关键文献链达到足够覆盖后，再集中发布科学契约 v0.2，避免逐篇阅读导致主合同频繁震荡。

## Delta 001 — independent mechanical residual jitter 的主表示

**状态：ACCEPTED**  
**来源：** Liu, Jiang et al., IEEE Access 2021, DOI `10.1109/ACCESS.2021.3099871`  
**证据角色：** 方法定义 / weak-turbulence benchmark

项目采用发射面二维角倾斜作为 independent mechanical residual jitter 的主 wave-optics 表示：

\[
U_0'(x,y)=U_0(x,y)\exp[i k(\theta_xx+\theta_yy)].
\]

若采用零均值各向同性 Gaussian jitter：

\[
\theta_x,\theta_y\sim\mathcal N(0,\sigma_\theta^2),
\]

则 `sigma_theta` 明确定义为**单轴角标准差**，单位 rad。二维径向 RMS、variance、platform attitude RMS 与 LOS residual jitter 必须另行换算，不得混用。

接收面强度平移仅作为快速近似或交叉验证，不作为默认主链。

## Delta 002 — Gaussian jitter broadening 解析 benchmark

**状态：ACCEPTED WITH CONVENTION GUARD**

对于

\[
I(x,y)\propto\exp[-2(x^2+y^2)/W^2]
\]

定义的 Gaussian `1/e^2` intensity radius `W`，无湍流二维独立角抖动应满足

\[
W_{\rm eff}^2=W^2+4L^2\sigma_\theta^2.
\]

该式作为 jitter implementation 的解析 sanity check。未来若 `w_ref` 使用不同 radius / encircled-energy convention，必须先完成尺度换算。

## Delta 003 — finite-aperture received power 为主观测

**状态：ACCEPTED**

保持

\[
P_R=\iint_{A_R}|U_L|^2\,dA
\]

为通信主观测。point irradiance、peak intensity、scintillation index、beam shape similarity 等只作为辅助诊断。

后续主要统计量继续从 realization-level `P_R` 构造 ECDF、低分位功率与 outage。

该方向有既有 turbulence + pointing 文献依据，因此不得宣称“首次考虑有限接收孔径功率”。项目创新仍应落在不同发射结构的 joint optimum、排序变化、适用域与机制解释。

## Delta 004 — single-layer phase screen 的角色

**状态：ACCEPTED**

位于约 `0.36 L` 的 single-layer equivalent phase screen 仅保留为 weak-fluctuation benchmark / cross-check，不作为正式 production turbulence model。

正式模型继续评估 multi-phase-screen split-step，并需通过后续文献冻结：

- von Karman / modified von Karman spectrum；
- inner / outer scale；
- phase-screen number and spacing；
- subharmonic / low-frequency compensation；
- beam-wander accuracy；
- grid/window convergence 与适用范围。

## Delta 005 — Liu/Jiang 2021 数值不得作为 UAV 场景参数继承

**状态：ACCEPTED**

该文献的 `lambda=850 nm`、`L=1 km`、`W0=0.04 m`、`sigma_theta=5/10/15 microrad`、若干 `Cn2` 与 receiver aperture 等均按**作者模型验证/仿真扫描参数**记录。

特别禁止：

- 把 `5–15 microrad` 写成典型 UAV + PAT/FSM residual jitter；
- 把 `W0=0.04 m` 写成 40 mm transmitter clear aperture。

UAV residual jitter 必须由 airborne/UAV/PAT 实测或系统级文献单独建立证据链。

## Delta 006 — 三类横向运动继续独立记账

**状态：ACCEPTED**

正式模型继续分别保存：

- `rho_bw`：turbulence realization 在 independent jitter = 0 时产生的 centroid wander；
- `rho_j = L theta_j`：independent mechanical residual jitter 对应的几何位移尺度；
- `rho_b`：static / slow boresight bias。

目的不是增加模型复杂度，而是防止 beam wander 与 pointing error 重复计数，并支持有限孔径功率损失的物理归因。
