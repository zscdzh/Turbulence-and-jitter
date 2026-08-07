# Moon et al. 2025：UAV 三维姿态抖动到 LOS pointing error 的几何模型锚点

## 1. 文献身份

- Hyung-Joo Moon, Chan-Byoung Chae, Kai-Kit Wong, Mohamed-Slim Alouini
- *A Generalized Pointing Error Model for FSO Links With Fixed-Wing UAVs for 6G: Analysis and Trajectory Optimization*
- IEEE Transactions on Wireless Communications 24(7), 5723–5737 (2025)
- DOI: `10.1109/TWC.2025.3549062`
- 证据角色：**UAV-specific pointing geometry / model anchor，不是 residual-jitter measured-value anchor。**

---

## 2. 该文解决的是 raw UAV attitude jitter -> LOS pointing 的映射

作者不把 UAV jitter 简化成一个预先给定的 receiver-plane 2D Gaussian displacement，而是显式定义 UAV body-frame 的三维角抖动：

\[
\mathbf x=[\alpha,\beta,\gamma]^T,
\]

其中：

- `alpha`：roll-angle jitter；
- `beta`：pitch-angle jitter；
- `gamma`：yaw-angle jitter。

在 small-angle approximation 下，三个姿态扰动通过 3D rotation matrix 作用于 UAV-to-ground-station pointing vector。作者由此推导 LOS pointing-error angle 的概率分布。

最重要的物理结论是：

> **相同 roll/pitch/yaw jitter covariance，并不会在所有 UAV position/posture 下映射成相同 LOS pointing distribution。**

pointing distribution 的参数依赖 UAV 相对于 ground station 的位置和姿态。

作者得到的 pointing-error angle 可表示为 Hoyt-type distribution；当各方向对 LOS 的投影接近对称时，才会退化/接近更常见的 symmetric Gaussian/Rayleigh-type reduced model。

---

## 3. 为什么这篇对本项目重要

它直接阻止三个常见混淆：

### 3.1 raw platform attitude jitter != residual LOS jitter

机体 roll/pitch/yaw 角抖动是 platform state；

本项目 `sigma_theta` 则计划表示：

> **PAT/FSM 闭环之后，发射光轴相对名义 LOS 的 residual angular error。**

二者不是同一个变量。

一个 mrad 量级的 raw attitude disturbance 可以经过 gimbal/FSM/PAT rejection 后变成 μrad 量级 residual LOS error，因此不得把 Moon 的姿态标准差直接放入本项目 wave-optics transmitter tilt。

### 3.2 raw attitude jitter 可能明显各向异性

roll、pitch、yaw 的 disturbance level 可以不同，且其 LOS projection 随 geometry 改变。因此若要从 flight-dynamics model 出发，简单 isotropic 2D Gaussian pointing 可能失真。

### 3.3 但 Paper 1 不需要完整 6-DoF flight model

本项目的研究对象不是 PAT controller / trajectory design，而是：

> 在 PAT 已经工作之后，独立 residual LOS jitter 如何改变 anti-turbulence beam mechanisms。

因此可以保留低维 reduced model：

\[
\theta_x,\theta_y\sim \mathcal N(0,\sigma_\theta^2)
\]

作为 baseline，只要明确：

- 它是 **post-PAT residual LOS model**；
- 不是 raw UAV roll/pitch/yaw model；
- 后续可增加 anisotropic `sigma_x != sigma_y` 作为 sensitivity check；
- 不声称该 reduced model能复现完整 UAV posture dynamics。

这保持了 Paper 1 的最小性，也与 Moon 2025 的几何警告兼容。

---

## 4. Moon 文中的 mrad 数字全部是 simulation assumptions

论文用于 trajectory optimization 的典型 jitter characteristics 包括：

- dominant roll: `[sigma_alpha, sigma_beta, sigma_gamma] = [1, 0.1, 0.1] mrad`；
- dominant pitch: `[0.1, 1, 0.1] mrad`；
- dominant yaw: `[0.1, 0.1, 1] mrad`；
- symmetric: `[0.583, 0.583, 0.583] mrad`。

在 conventional-model comparison 中又把所谓“actual UAV jitter”设置成：

\[
[0.1,1,0.1]\;\mathrm{mrad},
\]

并构造：

- 2-DoF equivalent `[0.711,0.711,0.1] mrad`；
- 1-DoF symmetric `[0.583,0.583,0.583] mrad`。

这里的 `actual` 是**仿真中的 ground-truth 3-DoF case**，不是实飞测量。

因此这些数值只能记录为：

> `simulation jitter characteristics / cannot inherit as post-PAT residual evidence`

尤其不能因为论文标题有 UAV/6G，就把 `0.1–1 mrad` 当成典型 airborne laser terminal residual pointing。

---

## 5. Table III 也只是 trajectory simulation scenario

论文 Table III/正文使用：

- altitude `H = 600 m`（另有 400 m sensitivity）；
- transmit power `10 mW`；
- optical aperture diameter `20 cm`；
- log-amplitude standard deviation / atmospheric-link parameters；
- visibility、flight time、speed/acceleration constraints 等。

这些用于其 fixed-wing trajectory/energy-efficiency simulation，不构成本项目近地 UAV-FSO 的可继承参数。

---

## 6. 对 jitter probability model 的项目裁决

Moon 2025 给出一个有价值的层级关系：

### Level A：完整 flight/geometry model

\[
\{\alpha,\beta,\gamma,\text{posture},\text{relative geometry}\}
\rightarrow
\theta_{LOS}.
\]

适合 trajectory/control/system research。

### Level B：本项目 reduced post-PAT model

\[
(\theta_x,\theta_y)
\sim
\mathcal N(\mathbf 0,\Sigma_{res}).
\]

适合 Paper 1 wave-optics mechanism study。

第一版可以采用：

\[
\Sigma_{res}=\sigma_\theta^2 I,
\]

并在少量 sensitivity case 中检查：

\[
\Sigma_{res}=\operatorname{diag}(\sigma_x^2,\sigma_y^2).
\]

不需要一开始引入 roll/pitch/yaw、trajectory、bank angle 和 full flight dynamics。

---

## 7. 与 turbulence-induced beam wander 的关系

Moon 2025 的 pointing model属于 platform/geometry-induced pointing loss；它不是 atmospheric wave-optics beam-wander simulation。

因此本项目仍需分别保存：

- `rho_bw`：phase screens 产生的 turbulence-induced centroid wander；
- `rho_j = L theta_j`：post-PAT independent mechanical residual；
- `rho_b`：slow/static bias。

Moon 2025 不提供把三者合并成一个 Gaussian pointing factor 的理由。

---

## 8. 当前裁决

**状态：READ / UAV POINTING-GEOMETRY MODEL ANCHOR。**

接受的项目结论：

1. raw 3D UAV attitude jitter 与 residual LOS jitter 必须严格区分；
2. raw UAV jitter 映射到 LOS 后可以具有 geometry-dependent anisotropy；
3. Paper 1 仍允许使用二维 Gaussian transmitter-angle residual model，但必须明确它是 post-PAT reduced model；
4. isotropic Gaussian 应作为 baseline，而不是宣称为所有 UAV flight state 的真实分布；
5. Moon 文中的 0.1–1 mrad 数值全部不得继承为本项目 residual `sigma_theta`。