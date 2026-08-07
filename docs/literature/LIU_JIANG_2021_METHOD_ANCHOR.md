# Liu / Jiang 2021 方法学锚点

## 文献身份

- Xin Liu, Dagang Jiang, et al.
- *Single-Layer Phase Screen With Pointing Errors for Free Space Optical Communication*
- IEEE Access, 2021, 9:104070–104078
- DOI: `10.1109/ACCESS.2021.3099871`
- 证据定位：**共用方法定义与弱湍流 benchmark**。它服务于 Paper 1 的统一评价模型，也可作为 Paper 2 的传播前序；它不是 UAV 场景参数锚点，也不是正式 multi-screen turbulence model 锚点。

## 1. 对当前项目最重要的贡献

该文献把独立 pointing error 明确引入波动光学 phase-screen propagation，而不是只把 pointing loss 作为接收端统计乘子。它支持本项目采用

\[
U_0'(x,y)=U_0(x,y)\exp[i k(\theta_x x+\theta_y y)]
\]

作为 independent mechanical residual jitter 的主 wave-optics 表示。

`theta_x`、`theta_y` 应解释为发射光轴相对名义方向的单轴随机角误差，单位 rad。若采用二维零均值 Gaussian，则 `sigma_theta` 表示每一轴的角标准差，不是二维径向 RMS，也不是 variance。

接收面直接平移可以作为快速近似和交叉验证，但不能默认替代发射倾斜后的波动传播。

## 2. Gaussian jitter broadening benchmark

对于

\[
I(x,y)\propto\exp[-2(x^2+y^2)/W^2]
\]

定义的 Gaussian `1/e^2` intensity radius `W`，无湍流二维独立角抖动满足

\[
W_{\rm eff}^2=W^2+4L^2\sigma_\theta^2.
\]

因此该关系可作为 jitter implementation 的解析 sanity check。若未来参考尺度采用其他 radius / encircled-energy convention，必须先换算。

## 3. 有限孔径接收功率的文献支持

该文献不仅比较 point irradiance fluctuation，也计算有限接收孔径内的 received-power fluctuation PDF，支持本项目继续采用

\[
P_R=\iint_{A_R}|U_L|^2\,dA
\]

作为主观测，再从 realization-level `P_R` 构造 ECDF、低分位功率和 outage。

它已经研究 turbulence + pointing 下的 finite-aperture received power，因此 Paper 1 和 Paper 2 都不得宣称“首次考虑有限接收孔径功率”。

## 4. 单层相位屏的使用边界

该文献采用位于约 `0.36 L` 的 single-layer equivalent phase screen，目标是弱湍流条件下的统计复现。

项目裁决：

- 保留 single-screen `0.36 L` 作为 weak-turbulence benchmark / cross-check；
- 不采用它作为正式 production turbulence model；
- 正式模型继续评估 multi-phase-screen split-step，并需要独立文献冻结 spectrum、inner/outer scale、screen number/spacing、low-frequency compensation、beam-wander accuracy 和 grid/window convergence。

## 5. 不能继承为 UAV 场景参数的数字

文中 `lambda=850 nm`、`L=1 km`、Gaussian beam radius `W0=0.04 m`、`sigma_theta=5/10/15 microrad`、若干 `Cn2`、receiver aperture、grid 和 realization 数均按作者模型验证或仿真扫描参数记录。

特别禁止：

- 把 `5–15 microrad` 写成典型 UAV + PAT/FSM residual jitter；
- 把 `W0=0.04 m` 写成 40 mm transmitter clear aperture。

## 6. 三类横向运动继续独立记账

正式模型应分别保存：

1. `rho_bw`：在 `jitter = 0` 条件下由 turbulence realization 产生的接收面质心漂移；
2. `rho_j = L theta_j`：independent mechanical residual jitter 对应的几何位移尺度；
3. `rho_b`：static / slow boresight bias。

目的是防止 beam wander 与 independent pointing 被重复计算，并允许解释有限孔径功率损失来自哪一类扰动。

## 7. 对 Paper 1 的直接边界

该文献已经覆盖 Gaussian beam 下的 phase screen + independent pointing error、boresight bias、有限孔径 received-power fluctuation 和 BER。

因此 Paper 1 不能把“第一次把 turbulence 与 pointing 一起放进 wave-optics”作为创新。

Paper 1 仍然需要回答的是：

- 文献中不同**抗湍流机制**面对 independent mechanical jitter 时是否保持原有优势；
- self-healing、caustic、self-focusing、flat-top、partial-coherence 等不同机制的 jitter sensitivity 有何系统差异；
- turbulence-only 优势在加入 jitter 后何时压缩、反转或失效；
- 这些差异是否能由 finite-aperture capture、长期光斑、外围能量等少量描述量解释；
- 结果是否形成可迁移的 applicability / failure regimes。

Paper 1 不要求为每种 structured beam 求完整 joint optimum。

## 8. 对 Paper 2 的直接边界

该文献提供共用传播方法背景，但没有提出 turbulence–jitter co-robust structured-beam design。Paper 2 若启动，创新应来自 Paper 1 揭示的机制 trade-off 与新的低维联合设计原则，而不是“联合 turbulence 与 pointing”。

## 9. 尚未解决

- UAV/PAT residual jitter 的真实量级、PSD、相关时间与各向异性；
- multi-phase-screen 数值参数与低频准确性；
- Paper 1 最终代表机制集合；
- 统一 Gaussian baseline 与资源匹配协议；
- 文中约 `1.87 microrad` satellite-ground experimental value 的原始引用链仍未确认。
