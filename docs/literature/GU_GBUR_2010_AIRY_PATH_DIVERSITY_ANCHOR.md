# Gu & Gbur 2010：Airy array 的 path-diversity / self-bending 机制锚点

## 文献身份

- Yalong Gu, Greg Gbur
- *Scintillation of Airy beam arrays in atmospheric turbulence*
- Optics Letters 35(20), 3456–3458 (2010)
- DOI: `10.1364/OL.35.003456`
- 证据角色：**Paper 1 的 Airy/path-diversity 机制锚点**。它不是 finite-aperture communications 结果，也不是独立 mechanical jitter 论文。

## 1. 这篇论文真正研究的不是“单个 Airy 自愈”

论文的核心设计是一个由多个空间分离 Airy beamlets 组成的 beam array。作者利用 Airy beam 的 self-bending / transverse acceleration，使各 beamlet 在传播初期走过不同横向区域，从而经历较弱相关的 turbulence；同时又通过初始几何参数使它们在指定接收距离重新汇合到轴上 detector 附近。

作者自己的机制叙述可以概括为：

1. transmitter plane 上 beamlets 空间分离；
2. 由于 self-bending，beamlets 走不同平均路径；
3. 各 beamlet 的 turbulence-induced intensity fluctuation 近乎去相关；
4. 在设计接收距离，beamlets 又在 on-axis detector 处重叠；
5. 多个近独立强度涨落平均后，scintillation 接近 `1/N` 理论极限。

因此，这篇最适合归类为：

> **Airy-trajectory-enabled spatial/path diversity**

而不是简单归类成“self-healing beam”。

## 2. 单个有限能量 Airy beam 定义

作者使用二维有限能量 Airy 场：

\[
U(x,y,0)=
\operatorname{Ai}(x/x_0)\exp(a x/x_0)
\operatorname{Ai}(y/y_0)\exp(a y/y_0).
\]

其中：

- `x0 = y0 = 0.012 m`；
- exponential truncation parameter `a = 0.1`。

这些是该文的 simulation design values，不是 UAV 场景参数，也不是本项目最终 Airy 参数。

论文首先验证单 Airy 的平均 self-bending path 在 turbulence 中仍大体保持抛物轨迹：

- wavelength `lambda = 1.55 um`；
- constant `Cn2 = 1e-14 m^(-2/3)`；
- nominal propagation distance `L = 3 km`；
- free-space intensity-peak location 约 `(0.066, 0.066) m`；
- turbulence ensemble average peak 约 `(0.058, 0.062) m`；
- 作者认为其差异约等于 1–2 个数值像素，可由 FFT turbulence-spectrum 离散采样和有限 realization 数解释。

论文使用 multiple-phase-screen propagation，并引用 Martin & Flatté (Applied Optics 1988)。但正文没有给出足够信息冻结本项目的 phase-screen number、spacing、spectrum low-frequency treatment 或 convergence，因此不能作为 production turbulence numerical contract。

## 3. 四 beamlet Airy array

作者定义四个不同方位的 Airy beamlets，通过 transverse displacement parameter `d` 设置其起始位置与方向。

在主示例：

- `N = 4` beamlets；
- `L = 3 km`；
- `d = 0.066 m`；
- 其余 Airy 与 turbulence 参数同上。

四个 beamlets 在 transmitter plane 分离，而在 `L = 3 km` 的 receiver plane 其 intensity peaks 基本在轴上 detector 处重合。

这一结构有重要资源含义：`d` 不是无代价数学参数，而意味着 transmitter plane 上需要较大的横向 source footprint / 多 beamlet 空间占用。以后若把这类方案放进 Paper 1 公平评价，必须把实际 Tx clear aperture、beamlet spacing 和总功率一起记账。

## 4. 最关键证据：cross-scintillation 几乎为零

作者定义 self-scintillation 和 cross-scintillation：

\[
\sigma^2_m=\frac{\langle I_m^2\rangle}{\langle I_m\rangle^2}-1,
\]

\[
\sigma^2_{mn}
=
\frac{\langle I_m I_n\rangle}
{\langle I_m\rangle\langle I_n\rangle}-1.
\]

在 3 km 四 beamlet 主示例中，各 beamlet 的 on-axis self-scintillation 约为：

- 0.8052；
- 0.8030；
- 0.7716；
- 0.8274。

而 cross-scintillation 大致位于 `-0.0192` 到 `0.0372` 之间，接近零。

因此作者认为 beamlets 的 turbulence-induced intensity fluctuations 基本不相关。四 beamlet array 的 on-axis scintillation index 为 `0.2135`，约为单 beamlet 的四分之一，接近理想极限：

\[
\sigma^2_{\min}=\sigma^2_{\mathrm{ind}}/N.
\]

这是真正支持“path diversity / decorrelation”机制的证据。

注意：论文主体聚焦 on-axis point scintillation；它没有建立本项目需要的 finite-aperture received-power ECDF、low-tail power 或 outage，因此 `0.2135` 不能被直接翻译成通信可靠性收益。

## 5. 机制有明显的距离与几何调谐条件

作者固定 `x0,y0,a` 后改变传播距离，并为了让 beamlets 在 detector 处最大重叠而重新调整 `d`。

报告的 scintillation reduction：

- `L = 2.5 km`：约 72%；
- `L = 3.0 km`：主示例约接近 75%；
- `L = 3.5 km`：约 74%；
- `L = 1.5 km`：只有约 55%。

短距离性能下降被作者归因于 beamlets 初始分离不足，导致其穿过 turbulence 的路径仍然相关。

这说明该机制不是“不用调就全距离有效”：

- 需要足够大的初始分离来降低 cross-correlation；
- 又需要 self-bending 轨迹在指定接收距离重新重叠；
- `d` 与目标 `L` 存在明显 geometry tuning；
- practical Airy 的 finite-energy truncation 还限制可维持 self-acceleration 的距离。

因此，对移动 UAV / varying range 场景，不能把这篇的 Airy array 视为天然 distance-robust 方案。

## 6. 对 independent mechanical jitter 的 Paper-1 推论

以下不是 Gu & Gbur 已验证结果，而是本项目基于其机制提出的待检验假设。

对所有 beamlets 施加同一个发射端 mechanical angular tilt：

\[
U'_m(\mathbf r)=U_m(\mathbf r)
\exp[i k\boldsymbol\theta_j\cdot\mathbf r].
\]

该 common-mode tilt 并不会自动破坏 beamlets 之间原本用于 path diversity 的**相对**初始分离和相对 Airy 几何；因此它们可能仍然经历相对分离的 turbulence paths，并在一个整体偏转后的坐标系中保持某种汇合关系。

但对固定在名义轴线上的 receiver aperture / detector，整个 beamlet ensemble 的汇合区域预计会发生 common-mode lateral displacement，量级首先近似为：

\[
\Delta_j\sim L\theta_j.
\]

因此可能出现：

> **scintillation-diversity mechanism 仍然工作，但 fixed-aperture received power 因整体 pointing displacement 明显下降。**

这会直接体现 Paper 1 的核心命题：

\[
\text{turbulence robustness}
\neq
\text{mechanical pointing robustness}.
\]

需要用 wave-optics tilt propagation + finite-aperture power 才能验证；不能从原论文的 on-axis scintillation 直接推断。

## 7. 与 OPB 的机制区别

Airy array 与 Zhang 2019 OPB 虽然都使用 Airy-like / curved-energy-flow 思想，但 Paper 1 中应暂时视为两个不同机制：

### Airy array

核心是：

> `spatially separated paths -> weakly correlated turbulence fluctuations -> receiver-plane overlap -> diversity averaging`

关键资源是 multiple beamlets、source footprint、distance-dependent trajectory overlap。

### OPB

核心是：

> `distributed inward energy flow / transverse-wavevector pairing -> sustained central pin / autofocusing`

关键资源是 structured radial phase、外围能量 reservoir、longitudinal focusing interval。

因此一个主要解决“随机涨落去相关”，另一个主要解决“沿传播距离维持中心能量集中”。二者面对 independent jitter 的失效物理可能不同。

## 8. 但 Airy array 未必进入最终 common-evaluation beam set

这篇虽然是优秀机制锚点，但它使用的是 **multi-beamlet spatial-diversity architecture**，不完全等价于单一有限发射孔径内的一种 monolithic beam profile。

如果 Paper 1 最终目标是比较 3–5 个“单发射口径 structured-beam mechanisms”，直接把四 beamlet Airy array 与单 Gaussian / Bessel / OPB 排在同一表中，可能产生明显硬件资源不对称。

因此当前裁决：

- Gu & Gbur 2010：保留为 **READ / PATH-DIVERSITY MECHANISM ANCHOR**；
- Airy/path-diversity 机制继续保留；
- 最终共同评价的 Airy representative 暂不冻结；
- 优先继续读 Zhu et al. 2021 的 quasi-ring Airy finite-aperture communication work，再决定用 single/ring Airy 作为代表，还是把 Airy array 只作为机制背景。

## 9. 对 Paper 1 统一协议的新增护栏

该文支持加入以下检查：

1. 对任何“diversity”光场，不只报告单分量 scintillation，还应报告不同分量有限孔径功率的 correlation / covariance；
2. 若方案依赖 multiple beamlets / separated source regions，必须将 transmitter footprint、beamlet spacing 和总功率写入 resource ledger；
3. 若最佳性能依赖目标距离下的几何汇合，必须报告 range sensitivity，不能把单一设计距离结果外推成宽距离鲁棒性；
4. on-axis scintillation reduction 不自动意味着 finite-aperture low-tail received power 改善；
5. common-mode mechanical tilt 与 turbulence-path decorrelation 应作为两个独立物理问题处理。

## 10. 当前结论

**证据角色：READ / PATH-DIVERSITY MECHANISM ANCHOR。**

这篇使 Paper 1 的 Airy 机制从模糊的“self-healing / caustic beam”收敛成更具体的：

> **self-bending enabled path diversity with receiver-plane recombination.**

它与 OPB 的 inward-flow/autofocusing 机制应暂时分开；但 Airy array 本身是否适合进入最终 3–5 个 common-evaluation representatives，仍需由后续 finite-aperture Airy 通信文献决定。