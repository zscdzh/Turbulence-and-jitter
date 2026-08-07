# UAV / airborne PAT residual-jitter 证据链

## 1. 目的

本文件只回答一个场景参数问题：

> 本项目的 post-PAT independent residual LOS jitter 应如何建立现实证据范围？

它不把 platform attitude、实验室 alignment accuracy、ground-station target-tracking error、airborne fine-tracking residual 混为同一个 `sigma_theta`。

当前所有数字按证据类型分层。

---

## 2. Level 1：真实飞行闭环 residual tracking —— 当前最高价值锚点

### Lei, Li, Zhang, Photonic Sensors 2019

*Experimental Study on PAT System for Long-Distance Laser Communications Between Fixed-Wing Aircrafts*  
DOI: `10.1007/s13320-018-0522-9`

证据类型：**actual flight / airborne closed-loop PAT tracking error**。

系统：

- 两架 fixed-wing Y12 aircraft；
- coarse + fine composite PAT；
- coarse stage：gyro-stabilized turntable / passive+active suppression；
- fine stage：CCD spot detection + high-rate ROI + piezo-ceramic/electromagnetic galvanometer；
- fine-tracking error budget明确包含 residual platform vibration。

flight test：

- aircraft speed约 `300 km/h`；
- long-distance acquisition/tracking tests `10–144 km`；
- stable communication at `144 km`；
- reported data rate `2.5 Gbit/s`；
- BER约 `1e-7`。

flight tracking results：

\[
\sigma_{coarse}\approx8.68\;\mu rad,
\]

\[
\sigma_{fine}\approx8.19\;\mu rad.
\]

结论中写为：

- coarse tracking precision `<10 μrad (1σ)`；
- fine tracking precision `<8 μrad (1σ)` during flights。

### 为什么这篇重要

这是当前文献链中第一条可以明确说：

> **真实 airborne laser communication 飞行闭环后，约 `O(10 μrad)` 的 residual tracking error 是有同行评审实测依据的。**

### 为什么仍不能直接冻结 `sigma_theta = 8 μrad`

仍有四个边界：

1. fixed-wing Y12 != small rotary-wing UAV；
2. system SWaP / aperture / servo architecture 与目标低成本 UAV terminal 不同；
3. 论文的 “fine tracking error 1σ” 没有充分拆成与本项目 `theta_x, theta_y` 完全一致的 per-axis Gaussian standard deviation；
4. tracking error 中仍可能混有 sensor noise、atmospheric spot disturbance、controller residual 等，不是纯机械 vibration PSD。

所以正确证据角色是：

> **real-flight residual LOS order-of-magnitude anchor / informs range, not direct parameter inheritance**。

---

## 3. Level 2：室内模拟 airborne tracking capability

### Ke & Liang 2021

*Airborne Laser Communication System with Automated Tracking*  
DOI: `10.1155/2021/9920368`

证据类型：**indoor simulated airborne environment / repeated realignment accuracy**。

系统目标是 six-rotor UAV lightweight tracking architecture，但实验并未在飞行 UAV 上进行。

作者进行约 `4500` 次 spot-drift / realignment trials，并报告：

\[
\text{realignment accuracy}(3\sigma)=2.42\;\mu rad,
\]

结论表述为 tracking accuracy better than `2.5 μrad`。

这说明几 μrad 级 closed-loop alignment 在受控实验条件下可以达到，但不能写成：

> six-rotor UAV actual-flight post-PAT residual = 2.5 μrad。

尤其 `2.42 μrad` 是该文定义的 `3σ` radial realignment accuracy，与本项目 per-axis `1σ` 不可直接等值。

证据角色：

> **laboratory capability / lower-stress reference, not flight residual distribution**。

---

## 4. Level 3：短距离 field alignment capability

### Ke et al., Photonics 2023

*Design and Implementation of a Non-Common-View Axis Alignment System for Airborne Laser Communication*  
DOI: `10.3390/photonics10091037`

证据类型：**10 m / 20 m field alignment experiment**。

报告：

\[
\text{tracking accuracy}=13.98\;\mu rad.
\]

该实验验证 non-common-view axis-alignment concept；不是长距离飞行平台上的 post-PAT residual time series。

证据角色：

> **field alignment capability / method demonstration, not UAV flight residual distribution**。

---

## 5. Level 4：真实 UAV/aircraft motion 但不是 residual-angle measurement

若论文只报告：

- UAV hover/moving received-power fluctuation；
- BER / crosstalk；
- link establishment；
- 6.7 km rotary-wing data link；

而没有给出 closed-loop LOS angular error RMS / PSD，则它只能证明场景真实性，不能提供 `sigma_theta`。

例如：

- rotary-wing UAV 6.7 km / 1.25 Gbit/s field demonstrations：证明 small-UAV FSO scene 真实存在，但公开综述信息没有给出 residual angular distribution；
- Li et al. 2017 moving-UAV OAM experiment：hover/moving received-mode fluctuation可以证明 motion causes measurable optical impairment，但不能反演成唯一 `sigma_theta`。

---

## 6. Moon 2025：不能与上述 residual values 混用

Moon et al. 2025 研究 raw fixed-wing 3D attitude jitter：roll/pitch/yaw standard deviations 可到 `0.1–1 mrad` 的 simulation cases。

这些是：

\[
\text{platform attitude jitter before/without explicit PAT residual reduction}
\]

而 Lei 2019 的约 `8 μrad` 是：

\[
\text{closed-loop airborne fine tracking error after PAT action}.
\]

两者相差一到两个数量级完全合理，不能用“文献数值冲突”解释。

这正是本项目必须定义 `sigma_theta` 为 **post-PAT residual LOS angular error** 的原因。

---

## 7. 当前可以形成的物理场景判断

### 已支持

真实 airborne closed-loop laser-communication PAT 文献已经证明：

> **约 `10 μrad` 量级的 residual tracking precision 在大型 fixed-wing 实飞系统中是现实的。**

因此此前完全依赖 5/10/15 μrad simulation scan 的状态得到改善：`O(10 μrad)` 不再只是理论猜测。

### 仍未支持

目前尚未找到足够强的开放同行评审证据证明：

> **small rotary-wing UAV + low-SWaP PAT/FSM 的典型 per-axis post-loop residual 必然是某一个确定的 1σ 数值。**

因此 `sigma_theta` 仍应保持：

> **UNFROZEN as a single physical baseline value**。

---

## 8. 对 Paper 1 参数设计的当前建议

### 8.1 继续以 dimensionless jitter 为主科学扫描

Paper 1 的机制图仍应优先使用：

\[
j=\frac{L\sigma_\theta}{w_{ref}}
\]

或等价 displacement normalization，避免论文结论依赖一个尚未冻结的“典型 UAV μrad”。

### 8.2 物理单位只用于 scene anchors

后续可以设置三种 evidence-labelled physical points：

- **lab-capability point**：由 Ke 2021 一类几 μrad 级实验提供数量级背景，但不直接把 3σ 转成 per-axis 1σ；
- **real airborne fixed-wing anchor**：约 `8–10 μrad (1σ)` tracking-error 量级；
- **higher-residual stress case**：需要更多 actual airborne / low-SWaP literature 后再冻结，不从 Moon 的 0.1–1 mrad raw attitude直接继承。

### 8.3 anisotropy 作为 secondary sensitivity

第一版 Paper 1 可用 isotropic residual Gaussian；后续至少做一组 `sigma_x != sigma_y` sensitivity，以回应 Moon 2025 的 geometry/anisotropy evidence。

不需要加入完整 roll/pitch/yaw flight model。

---

## 9. 当前需要继续追的证据

优先继续寻找：

1. rotary-wing UAV actual-flight optical terminal closed-loop angular residual；
2. airborne PAT residual PSD / correlation time / frequency-band information；
3. low-SWaP gimbal + FSM terminal field data；
4. tracking-error definition是否为 per-axis / radial RMS / 1σ / 3σ；
5. atmospheric spot-motion contribution与 mechanical platform residual是否可以拆分。

若这些数据长期无法获得，Paper 1 不应因此停滞：使用 dimensionless jitter + fixed-wing real-flight anchor + transparent stress range依然可以形成可信机制研究。

---

## 10. 当前裁决

**状态：PARTIALLY ANCHORED / SINGLE BASELINE STILL UNFROZEN。**

当前最重要的新证据是 Lei et al. 2019：

> two-Y12 actual flight, 10–144 km, ~300 km/h, fine tracking error ~8.19 μrad (1σ), 2.5 Gbit/s / ~1e-7 BER。

它足以支持 `O(10 μrad)` 作为真实 airborne closed-loop residual 的数量级锚点，但还不足以把本项目多旋翼 UAV 的 `sigma_theta` 唯一冻结为 8 μrad。