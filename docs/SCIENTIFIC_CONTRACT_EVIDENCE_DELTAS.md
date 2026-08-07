# SCIENTIFIC_CONTRACT_EVIDENCE_DELTAS

状态：滚动证据账本。这里记录已经经过逐篇文献审查并由项目负责人接受、但尚未统一并入正式科学契约的文献证据增量。

原则：

- 只记录有明确文献来源且已经讨论接受的定义或边界；
- 仿真展示参数不自动升级为项目场景参数；
- 每条增量保留来源文献与证据角色；
- 第一篇与第二篇的证据角色必须分开记录；
- 等关键文献链达到足够覆盖后，再集中冻结科学契约，避免逐篇阅读导致主合同频繁震荡。

## Delta 001 — independent mechanical residual jitter 的主表示

**状态：ACCEPTED**  
**来源：** Liu, Jiang et al., IEEE Access 2021, DOI `10.1109/ACCESS.2021.3099871`  
**证据角色：** 共用方法定义 / weak-turbulence benchmark

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

该方向有既有 turbulence + pointing 文献依据，因此不得宣称“首次考虑有限接收孔径功率”。第一篇的论文价值应落在不同**抗湍流机制**面对 independent jitter 时的敏感性、失效方式、排序变化和适用域；第二篇才讨论联合设计。

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

## Delta 007 — Badás 2024 的证据角色限定

**状态：ACCEPTED AS PAPER-2 BACKGROUND, NOT PAPER-1 TASK DEFINITION**  
**来源：** Badás et al., Optics Express 2024, DOI `10.1364/OE.533250`

该文献已经较完整地处理了 jitter-only 条件下 Gaussian 与 Gaussian–LG/annular-like irradiance shaping 的优化，并证明优化目标改变时最优 beam width / mode weight 也会改变。

对本项目的直接影响是：

- 第二篇若采用 Gaussian–LG，不得重复“jitter-only 权重和束宽优化”作为主要创新；
- Gaussian 基线必须针对同一目标认真优化；
- 正交偏振首先是避免相干干涉的实现方式，不能未经验证宣称带来独立 turbulence diversity；
- 该文献服务于第二篇联合设计的前序边界，不应反过来把第一篇改写成 Gaussian–LG joint optimization。

## Delta 008 — production turbulence model 必须验证低频 beam-wander 精度

**状态：ACCEPTED**  
**来源：** Chen et al., Applied Optics 2020, DOI `10.1364/AO.389121`  
**证据角色：** numerical-validation anchor

正式 multi-phase-screen implementation 不得只验证 phase RMS、screen appearance、short-term radius 或单一 scintillation。低空间频率欠采样会系统性低估 beam-wander variance 与 long-term beam radius，而这两项直接影响本项目对 turbulence-induced wander 与 mechanical jitter 相对重要性的判断。

因此 production turbulence module 至少需要：

- 明确 low-frequency treatment；
- 验证 turbulence-induced beam-wander variance；
- 验证 long-term beam radius；
- 再辅以 short-term radius / scintillation 等诊断。

具体使用 DFT-SH、sparse spectrum、randomized spectral sampling 或其他生成算法尚未冻结。

## Delta 009 — UAV raw attitude jitter 与 post-PAT residual LOS jitter 分层

**状态：ACCEPTED**  
**来源：** Moon et al., IEEE TWC 2025, DOI `10.1109/TWC.2025.3549062`  
**证据角色：** UAV pointing-geometry model anchor

raw roll/pitch/yaw jitter 经过 UAV position/posture geometry 后形成 LOS pointing error，可能具有明显各向异性。Moon 文中的 `0.1–1 mrad` 级 roll/pitch/yaw standard deviations 是 trajectory-simulation assumptions，不是实测 post-PAT residual。

Paper 1 仍允许采用二维 Gaussian transmitter-angle reduced model，但必须把它解释为 **PAT/FSM 闭环之后的 residual LOS angular error**，而不是 raw UAV attitude jitter。第一版可用 isotropic baseline，并保留少量 anisotropic sensitivity case。

## Delta 010 — `O(10 microrad)` airborne closed-loop residual 获得实飞数量级锚点，但单一 `sigma_theta` 仍不冻结

**状态：ACCEPTED AS RANGE EVIDENCE / NOT DIRECT PARAMETER INHERITANCE**  
**来源：** Lei, Li, Zhang, Photonic Sensors 2019, DOI `10.1007/s13320-018-0522-9`

两架 fixed-wing Y12 的真实飞行 laser-communication PAT 实验报告：

- aircraft speed约 `300 km/h`；
- acquisition/tracking range `10–144 km`；
- coarse tracking error约 `8.68 microrad (1sigma)`；
- fine tracking error约 `8.19 microrad (1sigma)`；
- 144 km 稳定通信；
- 2.5 Gbit/s，BER约 `1e-7`。

这足以支持：真实 airborne closed-loop optical tracking residual 达到 `O(10 microrad)` 是有同行评审实飞证据的。

但该值来自大型 fixed-wing Y12 composite PAT，不等价于小型 rotary-wing low-SWaP terminal 的 per-axis Gaussian `sigma_theta`。因此当前继续：

- 用 dimensionless jitter 作为 Paper 1 主扫描变量；
- 把 `~8–10 microrad` 作为真实 fixed-wing airborne order-of-magnitude anchor；
- `sigma_theta` 的唯一物理 baseline 仍保持 **UNFROZEN**；
- 不把 Ke 2021 的 `2.42 microrad (3sigma)` 室内 realignment 或 Moon 2025 的 mrad 级 raw attitude values 与该实飞 residual混用。