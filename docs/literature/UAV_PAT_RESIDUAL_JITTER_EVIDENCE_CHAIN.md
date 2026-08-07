# UAV / airborne PAT residual-jitter 证据链

## 1. 目的

本文件只回答一个场景参数问题：

> 本项目的 post-PAT independent residual LOS jitter 应如何建立现实证据范围？

它不把 platform attitude、实验室 alignment accuracy、ground-station target-tracking error、retro-reflected AoA residual、airborne fine-tracking residual 混为同一个 `sigma_theta`。

当前所有数字按证据类型分层。

---

## 2. Level 1A：真实多旋翼悬停 + compact fine tracking —— 当前最相关 UAV 工程锚点

### Trinh et al., IEEE Access 2021

*Experimental Channel Statistics of Drone-to-Ground Retro-Reflected FSO Links With Fine-Tracking Systems*  
DOI: `10.1109/ACCESS.2021.3117266`

证据类型：**actual multirotor hover / retro-reflected FSO / closed-loop ground fine tracking / per-axis residual and temporal statistics**。

平台与实验：

- DJI Matrice 600 Pro 六旋翼；
- DJI Ronin MX 三轴云台；
- 63.5 mm corner-cube retro-reflector；
- one-way LoS 约 `101–102 m`；
- roundtrip 约 `202–204 m`；
- hover altitude `15 m` 与 `20 m`；
- ground fine tracker：FSM + QD + PID；
- `4 kHz` sampling；每组 `12000` samples / `3 s`。

### pre-fine-tracking / telescope-entrance AoA

15 m hover：

- `sigma_X = 1.47 mrad`；
- `sigma_Y = 1.17 mrad`。

20 m hover：

- `sigma_X = 1.17 mrad`；
- `sigma_Y = 2.67 mrad`。

这些反映 UAV hovering-position change / gimbal vibration 等导致的 return-beam incoming-AoA disturbance，不能当作 post-PAT `sigma_theta`。

### closed-loop residual

作者在模拟 small detector / fiber-coupled receiver 的 PM plane 给出每轴 Gaussian-fit residual：

15 m：

- `sigma_theta,X ~ 39 urad`；
- `sigma_theta,Y ~ 27 urad`；
- beam-centroid standard deviation `5.91 um / 4.36 um`。

20 m：

- `sigma_theta,X ~ 42 urad`；
- `sigma_theta,Y ~ 40 urad`；
- beam-centroid standard deviation `8.83 um / 8.38 um`。

Gaussian fits 的 `R^2` 约为 `0.999`。

### temporal evidence

- hover / AoA fluctuations 的主要频谱能量在 `<50 Hz`；
- 少量成分延伸到约 `200 Hz`；
- beam-centroid displacement coherence time 约 `700 ms`；
- received-power 中 `100–500 Hz`、偶尔到 `~2 kHz` 的成分作者主要归因于更强 turbulence contribution。

### 为什么这篇特别重要

它给出当前文献链中非常稀缺的：

> **真实中小型多旋翼悬停 + 紧凑 fine tracker + 每轴 residual Gaussian-fit + PSD / coherence-time 数据。**

因此它可以作为 `O(30–40 urad)` multirotor engineering / stress anchor。

### 为什么仍不能直接冻结 transmitter-side `sigma_theta = 30–40 urad`

因为：

1. double-pass retro-reflection != one-way active transmitter；
2. forward / return misalignments 与 turbulence 存在相关性；
3. fine tracker 位于地面 OGS；
4. CCR + gimbal 改变 drone attitude-to-LOS mapping；
5. PM-plane residual AoA 不是无人机 transmitter angular-command residual；
6. 该实验距离仅约 100 m one-way，系统光学与目标 UAV-FSO terminal 不同。

证据角色：

> **multirotor actual-flight engineering range anchor / stress reference, not direct inheritance**。

详见 `TRINH_2021_MULTIROTOR_RETRO_FINE_TRACKING_ANCHOR.md`。

---

## 3. Level 1B：真实固定翼长距离闭环 residual tracking —— 高性能 airborne 锚点

### Lei, Li, Zhang, Photonic Sensors 2019

*Experimental Study on PAT System for Long-Distance Laser Communications Between Fixed-Wing Aircrafts*  
DOI: `10.1007/s13320-018-0522-9`

证据类型：**actual flight / airborne closed-loop PAT tracking error**。

系统：

- 两架 fixed-wing Y12 aircraft；
- coarse + fine composite PAT；
- aircraft speed约 `300 km/h`；
- acquisition/tracking tests `10–144 km`；
- stable communication at `144 km`；
- data rate `2.5 Gbit/s`；
- BER约 `1e-7`。

flight tracking results：

\[
\sigma_{coarse}\approx8.68\;\mu rad,
\]

\[
\sigma_{fine}\approx8.19\;\mu rad.
\]

结论中写为 coarse `<10 urad (1sigma)`、fine `<8 urad (1sigma)` during flights。

### 证据意义

真实 airborne laser communication 飞行闭环后，`O(10 urad)` residual tracking error 有同行评审实测依据。

### 为什么仍不能直接冻结 `sigma_theta = 8 urad`

- fixed-wing Y12 != small rotary-wing UAV；
- SWaP / aperture / servo architecture不同；
- fine tracking error `1sigma` 未充分证明与本项目每轴独立 Gaussian standard deviation 完全同定义；
- tracking error 中可能包含 sensor / atmospheric spot / control residual 等。

证据角色：

> **high-performance real-flight residual LOS order-of-magnitude anchor / informs range, not direct parameter inheritance**。

---

## 4. Level 2：室内模拟 airborne tracking capability

### Ke & Liang 2021

*Airborne Laser Communication System with Automated Tracking*  
DOI: `10.1155/2021/9920368`

证据类型：**indoor simulated airborne environment / repeated realignment accuracy**。

系统目标是 six-rotor UAV lightweight tracking architecture，但实验并未在飞行 UAV 上进行。

作者约 `4500` 次 spot-drift / realignment trials，并报告：

\[
\text{realignment accuracy}(3\sigma)=2.42\;\mu rad.
\]

结论写 tracking accuracy better than `2.5 urad`。

这说明几微弧度级 closed-loop alignment 在受控实验条件下可以达到，但不能写成 six-rotor actual-flight post-PAT residual。

---

## 5. Level 3：短距离 field alignment capability

### Ke et al., Photonics 2023

*Design and Implementation of a Non-Common-View Axis Alignment System for Airborne Laser Communication*  
DOI: `10.3390/photonics10091037`

证据类型：**10 m / 20 m field alignment experiment**。

报告：

\[
\text{tracking accuracy}=13.98\;\mu rad.
\]

不是长距离飞行平台 post-PAT residual time series。

---

## 6. Level 4：真实 UAV/aircraft motion 但没有可继承 residual-angle measurement

若论文只报告：

- hover/moving received-power fluctuation；
- BER / crosstalk；
- link establishment；
- long-range rotary-wing data link；

而没有给出 closed-loop LOS angular error RMS / PSD，则只能证明场景真实性，不能提供 `sigma_theta`。

---

## 7. Moon 2025：raw attitude jitter 不能与上述 residual values 混用

Moon et al. 2025 研究 fixed-wing 3D attitude jitter，roll/pitch/yaw standard deviations 使用 `0.1–1 mrad` 量级 simulation cases。

这些对应：

\[
\text{platform attitude jitter before/without explicit PAT residual reduction}
\]

而 Lei 2019 / Trinh 2021 提供的是闭环 optical tracking 后的 residual / receiver-plane statistics。

两者量级不同完全合理，不能视为文献冲突。

---

## 8. 当前可以形成的物理场景判断

### 已支持

1. 高性能 fixed-wing airborne PAT：`O(8–10 urad)` residual tracking precision 有真实飞行依据；
2. 中小型 multirotor retro-FSO + compact ground fine tracking：`O(27–42 urad)` per-axis residual AoA 有真实悬停实验依据；
3. multirotor pre-fine-tracking / hover-related incoming AoA 可达 `O(1 mrad)`；
4. closed-loop residual 可以近似 Gaussian，但 anisotropy 真实存在；
5. multirotor hover-related angular disturbance 主要位于几十 Hz 以下。

### 仍未支持

仍没有足够强证据证明：

> **one-way small multirotor active laser transmitter + low-SWaP onboard PAT/FSM 的典型 per-axis post-loop residual 必然等于某一个确定数值。**

因此 `sigma_theta` 仍保持单物理 baseline **UNFROZEN**。

---

## 9. 对 Paper 1 参数设计的当前建议

### 9.1 dimensionless jitter 继续作为主科学坐标

\[
j=\frac{L\sigma_\theta}{w_{ref}}.
\]

这样 Paper 1 的机制结论不依赖一个尚不存在的唯一“典型 UAV jitter”。

### 9.2 physical anchors 用多个 evidence labels，而不是单值

正式场景映射至少可以保留：

- **high-performance airborne anchor**：`~8–10 urad`；
- **multirotor compact-tracker engineering / stress anchor**：`~30–40 urad`；
- laboratory capability 只作为更低 residual 的技术背景，不与实际 flight anchors 等级相同。

### 9.3 anisotropy 作为 secondary sensitivity

第一版可用 isotropic Gaussian residual 建主图；后续至少做一组 `sigma_x != sigma_y` sensitivity。

### 9.4 PSD 暂不进入 Paper 1 第一版主模型

只要 Paper 1 研究 realization-level received-power statistics，而不模拟控制链时域动态，就没有必要把 `<50 Hz` hover PSD 强行塞入 wave-optics ensemble。

PSD 作为后续 dynamic extension / controller-coupled study 的证据储备。

---

## 10. 当前裁决

**状态：MULTIROTOR + FIXED-WING PHYSICAL RANGE PARTIALLY ANCHORED / SINGLE BASELINE STILL UNFROZEN。**

现在可以比此前更明确地说：

> 实际 airborne/UAV closed-loop optical residual 从高性能固定翼的约 `O(10 urad)` 到多旋翼紧凑 tracking architecture 的 `O(30–40 urad)` 均有同行评审实验依据。

但 Paper 1 仍应以 dimensionless jitter 为主，并把上述数值作为现实场景映射，而不是把某一个架构的 residual 直接当作 universal UAV parameter。
