# Liu / Jiang 2021 方法学锚点

## 文献身份

- Xin Liu, Dagang Jiang, et al.
- *Single-Layer Phase Screen With Pointing Errors for Free Space Optical Communication*
- IEEE Access, 2021, 9:104070–104078
- DOI: `10.1109/ACCESS.2021.3099871`
- 证据定位：**方法定义与弱湍流解析/数值 benchmark 文献**，不是 UAV 场景参数锚点，也不是正式 multi-screen turbulence model 锚点。

## 1. 对当前项目最重要的贡献

该文献把独立 pointing error 明确引入波动光学 phase-screen propagation，而不是只把 pointing loss 作为接收端统计乘子。其核心意义是支持本项目采用：

\[
U_0'(x,y)=U_0(x,y)\exp[i k(\theta_x x+\theta_y y)]
\]

作为独立机械 residual jitter 的主建模方式。

在当前项目中，`theta_x`、`theta_y` 应解释为**发射光轴相对名义方向的单轴随机角误差**，单位 rad。若采用二维零均值 Gaussian，则 `sigma_theta` 表示**每一轴的角标准差**，不是二维径向 RMS，也不是 variance。

接收面直接平移可以作为快速近似和交叉验证，但不能默认替代发射倾斜后的波动传播。

## 2. Gaussian jitter broadening benchmark

该文献数值拟合得到类似

\[
W_{\rm eff}^2=W^2+4L^2\sigma_\theta^2
\]

的 long-term beam broadening 关系。

对于 intensity 定义

\[
I(x,y)\propto\exp[-2(x^2+y^2)/W^2],
\]

单轴空间方差为 `W^2/4`；独立角抖动产生的位置误差方差为 `L^2 sigma_theta^2`。二者 Gaussian convolution 后自然得到

\[
\boxed{W_{\rm eff}^2=W^2+4L^2\sigma_\theta^2}.
\]

因此该系数不是应机械照搬的经验拟合，而可以作为本项目 Gaussian 无湍流 / 弱湍流 jitter 模块的**解析 sanity check**。

若定义

\[
j=\frac{L\sigma_\theta}{W},
\]

则

\[
\frac{W_{\rm eff}}{W}=\sqrt{1+4j^2}.
\]

注意：这里的 `W` 是上述 Gaussian intensity convention 下的 `1/e^2` intensity radius。若未来 `w_ref` 采用其他尺度，该无量纲式不能不经换算直接继承。

## 3. 有限孔径接收功率的文献支持

该文献不仅比较 point irradiance fluctuation，也计算有限接收孔径内的 received-power fluctuation PDF，说明 point irradiance statistics 与 finite-aperture received-power statistics 不能等同。

这支持当前项目继续采用

\[
P_R=\iint_{A_R}|U_L|^2\,dA
\]

作为主观测，再从 realization-level `P_R` 构造 ECDF、低分位功率和 outage。

该文献已经研究 finite-aperture received power，因此本项目的创新点不能表述为“首次考虑有限接收孔径”。本项目仍需证明的是：不同发射光场在 turbulence-only、jitter-only 与 joint 条件下的最优结构、排序与适用域如何变化。

## 4. 单层相位屏的使用边界

该文献采用位于约 `0.36 L` 的 single-layer equivalent phase screen，目标是弱湍流条件下的统计复现。作者自身将该方法限定在 weak fluctuation / `sigma_R^2 < 1` 的适用范围附近。

因此当前项目作如下裁决：

- **保留** single-screen `0.36 L` 模型作为 weak-turbulence benchmark / cross-check；
- **不采用**它作为正式 production turbulence model；
- 正式模型仍按 multi-phase-screen split-step 路线评估，并需要独立文献冻结 von Karman spectrum、inner/outer scale、screen spacing/number、subharmonic 与低频 beam-wander accuracy。

该文献没有充分证明其 phase-screen implementation 对低频 beam wander 的数值精度，因此不能据此冻结本项目的 beam-wander implementation。

## 5. 不能继承为 UAV 场景参数的数字

文中使用的典型仿真设置包括：

- `lambda = 850 nm`；
- `L = 1000 m`；
- Gaussian beam radius `W0 = 0.04 m`；
- `Cn2 = 5e-15, 1e-14, 2e-14 m^(-2/3)`；
- `sigma_R^2 = 0.2, 0.4, 0.8`；
- `sigma_theta = 5, 10, 15 microrad`；
- receiver aperture example `D = 0.08 m`；
- 512 x 512 phase-screen grid；
- 10000 realizations。

这些数字的主要角色是**作者的模型验证与仿真扫描设置**。当前均不得直接冻结为 UAV-FSO 主场景参数。

特别是 `5–15 microrad` 没有被该论文建立为“多旋翼 UAV + PAT/FSM 闭环后 residual LOS jitter”的实测范围，必须标记为：

> simulation parameter / cannot inherit as UAV residual-jitter evidence

另外，正文对 `W0 = 0.04 m` 的数学定义是 Gaussian beam radius，不能误写为“40 mm transmitter clear aperture”。

## 6. 三类横向运动的项目级改进

该文献把 turbulence 与 pointing error 同时随机化，但没有建立本项目要求的三类位移账本。因此我们的正式模型应比该文献更明确地分别保存：

1. `rho_bw`：在 `jitter = 0` 条件下由 turbulence realization 产生的接收面质心漂移；
2. `rho_j = L theta_j`：独立机械 residual jitter 对应的几何位移尺度；
3. `rho_b`：static / slow boresight bias。

这样做的目的是防止 beam wander 与 independent pointing 被重复计算，并允许解释有限孔径功率损失来自哪一类扰动。

## 7. 已覆盖内容与创新边界

该文献已经覆盖：

- phase screen + independent pointing error；
- Gaussian beam；
- zero-mean pointing jitter；
- non-zero boresight bias；
- anisotropic x/y pointing variance；
- long-term irradiance；
- point irradiance fluctuation PDF；
- finite-aperture received-power fluctuation PDF；
- BER。

因此本项目不得声称：

- 首次在 wave optics / phase-screen simulation 中联合 atmospheric turbulence 与 pointing error；
- 首次将 independent pointing error 引入 phase-screen propagation；
- 首次在 turbulence + pointing 条件下研究 finite-aperture received power。

该文献尚未回答本项目核心问题：

- 不同发射光场在 joint channel 中的比较；
- optimized Gaussian baseline；
- turbulence-only / jitter-only / joint optimum 的分离；
- 模式排序反转；
- realization-level low-tail finite-aperture power；
- continuous applicability region；
- paired common-randomness beam comparison；
- structured-beam resource accounting；
- medium/strong turbulence multi-screen propagation。

## 8. 当前可进入科学契约的结论

经本项目讨论，当前接受以下四条作为后续科学契约修订依据：

1. independent mechanical residual jitter 主链优先使用 transmitter angular tilt；`sigma_theta` 定义为 per-axis angular standard deviation；
2. `W_eff^2 = W^2 + 4 L^2 sigma_theta^2` 作为 Gaussian jitter broadening 的解析 benchmark，但必须保持 beam-radius convention 一致；
3. finite-aperture received power 继续作为主观测，point irradiance 只能作为辅助诊断；
4. single-layer `0.36 L` phase screen 只作为 weak-turbulence benchmark，正式模型继续评估 multi-screen split-step；文中的 `5–15 microrad` 不进入 UAV 场景参数。

## 9. 尚未解决

- UAV/PAT residual jitter 的真实量级、PSD、相关时间与各向异性：需要 UAV / airborne PAT 实测或系统文献；
- multi-phase-screen 数值参数与低频准确性：需要专门 phase-screen / wave-propagation 文献；
- `w_ref` 的最终定义：需结合 optimized Gaussian baseline 文献后冻结；
- 文中提及的约 `1.87 microrad` satellite-ground experimental value 的原始引用链存在疑点，当前不得作为已确认实测证据使用。
