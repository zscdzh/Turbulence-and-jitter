# Trinh et al. 2021：多旋翼无人机实飞 retro-reflected FSO fine-tracking / AoA 抖动锚点

## 1. 文献身份

- Phuc V. Trinh, Alberto Carrasco-Casado, Takuya Okura, et al.
- *Experimental Channel Statistics of Drone-to-Ground Retro-Reflected FSO Links With Fine-Tracking Systems*
- IEEE Access 9, 137148–137164 (2021)
- DOI: `10.1109/ACCESS.2021.3117266`
- 实验平台：DJI Matrice 600 Pro 六旋翼 UAV + DJI Ronin MX 三轴云台 + 63.5 mm corner-cube retro-reflector (CCR)
- 证据角色：**small/mid-size multirotor actual-flight AoA / fine-tracking residual / temporal-spectrum engineering anchor**。

该文是 retro-reflected double-pass architecture，不是单程 UAV 发射终端，因此不能把其数值直接继承为本项目 transmitter-side `sigma_theta`。但它是当前证据链中非常有价值的“小型/中型多旋翼实际悬停 + 紧凑 fine-tracking”实测来源。

---

## 2. 实验场景

实验在 NICT Kashima Space Technology Center 开展：

- OGS 与无人机水平距离约 `100 m`；
- UAV 悬停高度：`15 m`、`20 m`；
- one-way LoS distance：约 `101 m`、`102 m`；
- roundtrip propagation distance：约 `202 m`、`204 m`；
- OGS telescope aperture：`5 cm`；
- wavelength：`976 nm`；
- transmitted beam full divergence：约 `0.04 rad`；
- transmitter maximum power：`9 W`；
- OGS optics / fine-tracking breadboard：约 `30 cm × 30 cm`。

Drone gimbal 使用 independent mode，使云台姿态尽量不随 drone orientation 直接变化。因此作者指出，retro-reflected beam 的变化主要来自：

- drone hovering-position change；
- gimbal vibration；

而不是把全部机体 roll/pitch/yaw 原样映射到 return beam。

这一点使其特别适合作为“低 SWaP 多旋翼 + 云台后剩余运动”的现实背景。

---

## 3. 地面 fine-tracking 系统

OGS fine-tracking 包括：

- FSM；
- quadrant detector (QD)；
- PID closed loop；
- power meter (PM) 放在 Lens 3 焦面附近，模拟小探测器或 fiber-coupled receiver。

数据采样：

- sampling rate：`4 kHz`；
- 每个 dataset：`12000` samples；
- observation interval：`3 s`。

作者定义的“tracking accuracy”是 QD / PM 平面 beam-centroid displacement 的标准差，而不是 transmitter angular command RMS。

---

## 4. open-loop / pre-fine-tracking AoA：多旋翼悬停扰动量级

### 15 m hovering altitude

OGS receiving-telescope entrance 的 AoA：

- mean `mu_X = 6.96 mrad`；
- mean `mu_Y = 1.32 mrad`；
- standard deviation `sigma_X = 1.47 mrad`；
- standard deviation `sigma_Y = 1.17 mrad`。

根据 AoA 与 LoS geometry 推得无人机 hovering-position standard deviations 约：

- `0.15 m`；
- `0.12 m`。

### 20 m hovering altitude

OGS receiving-telescope entrance 的 AoA：

- mean `mu_X = 4.19 mrad`；
- mean `mu_Y = 10.82 mrad`；
- standard deviation `sigma_X = 1.17 mrad`；
- standard deviation `sigma_Y = 2.67 mrad`。

推得 hovering-position standard deviations 约：

- `0.12 m`；
- `0.27 m`。

这些 `~1–3 mrad` 量级反映的是 retro-reflected link 在 fine-tracking correction 前由 UAV hovering / gimbal motion 等造成的 incoming AoA disturbance，**不是** post-PAT residual `sigma_theta`。

---

## 5. closed-loop residual：最值得本项目保留的数据

论文在 QD / PM 平面分别统计 closed-loop residual，并给出每轴 Gaussian fit。

### 15 m altitude

PM plane beam-centroid displacement standard deviation：

- `sigma_X = 5.91 um`；
- `sigma_Y = 4.36 um`。

Fig. 4(g,h) 给出的 PM-plane residual AoA Gaussian-fit standard deviations：

- `sigma_theta,X ≈ 0.039 mrad = 39 urad`；
- `sigma_theta,Y ≈ 0.027 mrad = 27 urad`。

### 20 m altitude

PM plane beam-centroid displacement standard deviation：

- `sigma_X = 8.83 um`；
- `sigma_Y = 8.38 um`。

Fig. 8(g,h) 给出的 PM-plane residual AoA Gaussian-fit standard deviations：

- `sigma_theta,X ≈ 0.042 mrad = 42 urad`；
- `sigma_theta,Y ≈ 0.040 mrad = 40 urad`。

这些 residual distributions 的 Gaussian fits `R^2` 约为 `0.999`，说明在该短时实验 / tracker architecture 中，以 per-axis Gaussian 描述 fine-tracking residual 有直接实验支持。

### 证据意义

这使本项目第一次拥有：

> **small/mid-size multirotor actual-flight + compact ground fine-tracker 下，几十微弧度 per-axis closed-loop residual 的实验量级锚点。**

但正确角色仍是：

> `engineering range anchor / stress-reference`，不是本项目 transmitter-side `sigma_theta` 的直接继承值。

---

## 6. temporal evidence：机械/悬停扰动主要在低频

作者对 AoA 与 received power 做 PSD / spectrogram 分析。

对 radial AoA（主要由 drone hovering 引起）：

- significant spectral magnitude mostly `< 50 Hz`；
- 一些较小成分可延伸到约 `200 Hz`。

beam-centroid displacement coherence time 约：

- `700 ms`（15 m 与 20 m 两组均报告）。

received-power spectrum 中：

- `<50 Hz` 仍有明显 hovering/misalignment 贡献；
- `100–500 Hz`、偶尔到约 `2 kHz` 的高频成分被作者主要解释为更强 atmospheric-turbulence contribution。

因此该论文支持：

> multirotor hovering / gimbal-related AoA motion 主要集中在低频，而更高频 received-power fluctuation 不应全部归因于 mechanical jitter。

若 Paper 1 只做 realization-level ensemble，而不做时域控制链，该 PSD 不必进入主模型；但它是后续动态扩展或 stress-spectrum 设计的重要现实锚点。

---

## 7. 为什么 retro-reflected architecture 仍然可用，但不能直接继承

### 可以用的部分

1. **多旋翼真实悬停运动量级**；
2. **云台 + ground FSM/QD/PID 后 closed-loop residual 的量级**；
3. **每轴 residual Gaussian-fit 证据**；
4. **x/y anisotropy**；
5. **AoA frequency content / coherence time**；
6. **open-loop mrad -> closed-loop tens-of-urad 的现实压缩量级**。

### 不能直接继承的部分

1. double-pass retro-reflection 与本项目 one-way transmitter-to-receiver geometry 不同；
2. forward / return misalignments 和 turbulence 在同一路径上相关；
3. fine tracker 位于 OGS 接收端，而不是 UAV 发射端；
4. CCR / gimbal 使 drone attitude-to-LOS mapping 与主动 laser transmitter 不同；
5. `976 nm`、`0.04 rad` divergence、`9 W` 等为该实验专用参数；
6. PM-plane residual AoA 不应未经系统 optical mapping 直接解释为 UAV transmitter angular command residual。

因此：

> 该文可以强力约束“现实 residual-jitter 范围”，但不能单独冻结本项目 `sigma_theta`。

---

## 8. 对当前 UAV/PAT evidence chain 的影响

加入本论文后，当前证据层次可改为：

### multirotor actual-flight engineering anchor

Trinh et al. 2021：

- raw / pre-fine-tracking return AoA standard deviation：约 `1.17–2.67 mrad`；
- compact fine-tracking 后 PM residual：约 `27–42 urad` per axis；
- dominant mechanical/hover AoA frequency content：mostly `<50 Hz`。

### high-performance fixed-wing actual-flight anchor

Lei et al. 2019：

- fine tracking error 约 `8 urad (1sigma)`；
- 大型 fixed-wing / long-range / high-performance PAT。

二者不应互相矛盾地解读，而应说明：

> post-loop residual 与 platform / architecture / SWaP / tracker performance 强相关，现实范围可以跨越数微弧度到几十微弧度。

这进一步支持 Paper 1 用 dimensionless jitter `j` 做主科学坐标，同时用多个 evidence-labelled physical points 映射现实场景，而不是冻结一个“典型 UAV jitter”。

---

## 9. 当前裁决

**状态：READ / HIGH-VALUE MULTIROTOR ACTUAL-FLIGHT JITTER ANCHOR。**

接受：

- `O(10–40 urad)` 级 post-fine-tracking residual 在实际小/中型多旋翼 retro-FSO 场景中有直接实验依据；
- `O(1 mrad)` 级 pre-fine-tracking hover-related AoA disturbance 同样有实测依据；
- residual 可表现为近 Gaussian、各向异性分布；
- hovering-related disturbance 主要集中在较低频段。

不接受：

- 直接把 `27–42 urad` 写成 one-way UAV transmitter `sigma_theta`；
- 直接把 double-pass retro-reflected misalignment model 用作本项目主信道；
- 用本论文的 976 nm / 0.04 rad divergence / 9 W 等实验配置冻结本项目链路参数。
