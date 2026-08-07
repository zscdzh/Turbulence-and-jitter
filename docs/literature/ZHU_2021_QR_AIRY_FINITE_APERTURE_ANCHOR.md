# Zhu et al. 2021：quasi-ring Airy 的 finite-aperture communication 与机制归类审计

## 1. 文献身份

- Long Zhu, Andong Wang, Mingliang Deng, Bing Lu, Xiaojin Guo
- *Free-space optical communication with quasi-ring Airy vortex beam under limited-size receiving aperture and atmospheric turbulence*
- Optics Express 29(20), 32580–32590 (2021)
- DOI: `10.1364/OE.435863`
- 证据角色：**Airy / finite-aperture experimental communication anchor**。

该文与 Gu & Gbur 2010 的 Airy array 机制明显不同：它不是用多个空间分离 beamlets 做 path diversity，而是给单个 OAM Gaussian source 添加径向 `r^(3/2)` phase，使接收面能量向 inner ring 集中，并获得 autofocusing / reduced-spreading 行为。

---

## 2. 生成方式：本质是 radial-phase engineering

QRAVB phase profile：

\[
\Phi(r,\phi)=l\phi + a k r^{3/2},
\]

其中：

- `l`：OAM topological charge；
- `a`：radial-phase design parameter；
- `k`：wave number。

通过调整 `a`，作者直接控制传播过程中 beam divergence / receiver-plane inner-ring concentration。

理论示例：

- input Gaussian diameter `6.4 cm`；
- `lambda = 1550 nm`；
- simulated 200 m link；
- `a = 8e-4`，专门选取以在 `z = 120 m` 最大化 inner OAM ring 的 optical power。

因此该结构明显是 **target-distance tuned** 的，而不是一个不依赖 range 的通用 Airy profile。

---

## 3. 实验结构与资源

实验中：

- 72 Gbit/s 16-QAM DMT data signal；
- expanded Gaussian beam diameter约 `6.4 mm`；
- SLM1 生成 QRAVB；
- experiment QRAVB parameter `a = 0.026`；
- pseudo-random Kolmogorov phase mask 同时加载到 SLM1 以 emulated turbulence；
- mode-conversion loss 约 `1.4 dB`，作者称与 conventional OAM 和 Bessel generation loss 接近；
- physical free-space propagation `1.2 m`，通过 optical scaling / SLM arrangement 模拟约 `120 m` free-space behavior；
- receiver aperture diameter 通过透明 circular mask 调为 `10, 4, 3, 2 mm`。

这一篇真正测量了 limited-aperture received optical power，因此它比 Liu 2022 HG conference paper 在 receiver observable 上清楚得多。

---

## 4. turbulence 与统计证据

作者以

\[
D/r_0
\]

表征 turbulence strength，并实验测试 `D/r0 = 1` 与 `4`。

在 received-power fluctuation tests 中：

- transmitted power 固定 `0 dBm`；
- 每个 condition 生成 `50` independent random phase masks；
- 比较 conventional OAM、Bessel、QRAVB；
- receiver aperture 主要使用 10 mm 与 3 mm；
- 记录 received-power samples 及 cumulative probability。

50 realizations 只足以说明大尺度趋势，不足以支撑深尾 outage；但这是真实有限孔径功率而不是单点 irradiance。

---

## 5. 主要实验结果与正确解释

无 turbulence：

- `d = 10 mm` receiver 时三类 beam 几乎都能收全，received power 接近；
- receiver 缩小时，conventional OAM power 明显下降；
- `d = 3 mm` 时 QRAVB reported received power 约比 conventional OAM 高 10 dB、比 Bessel 高约 2 dB。

weak turbulence `D/r0 = 1`：

- Bessel 与 QRAVB power fluctuation 小于 conventional OAM；
- QRAVB average received power 约比 Bessel 高 2 dB；
- BER tests 同时显示 QRAVB / Bessel 比 conventional OAM 所需 transmitter power 更低；
- 3 mm aperture 时报告 QRAVB 相对 conventional OAM 约 10 dB required-transmitter-power relaxation，Bessel 约 8 dB。

stronger turbulence `D/r0 = 4`：

- higher OAM orders 显著恶化；
- received power 与 BER 均明显变差；
- 作者明确指出 high-order QRAVBs 对 strong turbulence 更敏感。

作者结论中甚至直接说：QRAVB anti-turbulence ability **similar to Bessel beam**；它相对于 Bessel 的主要额外优势来自更高 inner-ring received power under limited aperture。

因此不能把该文解释成“Airy 的 turbulence robustness 远高于 Bessel”。

---

## 6. 对 Paper 1 机制分类的关键影响

### 6.1 Gu & Gbur 2010 与 Zhu 2021 不是同一个 Airy mechanism

Gu & Gbur 2010：

> separated beamlets + self-bending trajectories + weakly correlated turbulence paths + receiver recombination

即 **path diversity**。

Zhu 2021：

> radial `r^(3/2)` phase + autofocusing / reduced divergence + inner-ring energy concentration

即 **radial-phase / autofocusing energy redistribution**。

后者与 OPB 的 inward-energy-flow / pin-like autofocusing 在物理上开始明显重叠。

### 6.2 “Airy”作为 beam name 不适合作为独立机制类别

目前更合理的分类不是：

- Bessel；
- Airy；
- OPB。

而是：

1. Bessel/self-healing/angular-spectrum redundancy；
2. path diversity（Gu–Gbur Airy array 作为锚点，但可能不进 common evaluation）；
3. radial-phase autofocusing / inward energy redistribution（OPB + ring/quasi-ring Airy 属于相邻机制）。

这样可以避免为了“每个名字一个 beam”而重复实现高度相似的 caustic/autofocusing结构。

---

## 7. 对 mechanical jitter 的推论

Zhu 2021 没有 independent mechanical pointing jitter。

对 QRAVB 的设计机制而言，一个 common transmitter angular tilt 预计会整体偏移其 autofocusing / inner-ring concentration region。即使 radial phase 仍能压低 diffraction spreading，固定 receiver aperture 仍可能因整体 LOS displacement 丢功率。

因此其 Paper-1 价值仍是：

> `reduced divergence / central energy concentration` 是否能转化成 `common-mode lateral displacement tolerance`？

但这一问题与 OPB 高度相近，所以没有必要在第一轮 common-evaluation set 同时保留多个 radial-autofocusing variants，除非后续分析证明它们的 capture-function 机制显著不同。

---

## 8. 公平比较仍有明显局限

论文比较的是 conventional OAM、Bessel 和 QRAVB，目标本身围绕 OAM link 与 limited receiver aperture。

它没有提供：

- optimized fundamental Gaussian direct-detection baseline；
- same-task Gaussian quadratic-phase/focusing optimization；
- transmitter clear-aperture / radial-energy full resource ledger；
- independent mechanical jitter；
- turbulence-only / jitter-only / joint three-way attribution；
- large-sample low-tail statistics。

而 QRAVB parameter `a` 本身就是针对 target receiver distance / inner-ring power 设置的设计自由度。

所以 reported 2–10 dB effects 不能继承成我们 Paper 1 的预期 effect size。

---

## 9. 当前 Airy 路线裁决

**Gu & Gbur 2010：READ / PATH-DIVERSITY MECHANISM ANCHOR。**  
**Zhu et al. 2021：READ / FINITE-APERTURE AUTOfocusing COMMUNICATION ANCHOR。**

当前不建议直接冻结一个名为“AIRY”的 Paper-1 representative。

原因：

- path-diversity Airy array 是 multi-beam architecture，资源和单-beam profiles 不同；
- quasi-ring Airy 的核心机制与 OPB / radial autofocusing 重叠；
- OAM receiver task 又引入额外 modal objective。

因此 Airy 更适合在 Paper 1 中承担：

> **机制谱系与对照文献**，而不是为了模式名称完整性强行占据一个 common-evaluation slot。

后续如果 final set 需要 caustic/autofocusing representative，优先从 OPB 与 radial Airy 中选一个数学定义最干净、资源最容易账本化的代表，而不是二者都跑。

---

## 10. 当前总体收敛

经过 Gu 2010 + Zhang 2019 + Zhu 2021，Paper 1 的机制分类进一步从 beam-name taxonomy 收敛为 physics taxonomy：

- **Bessel-like angular-spectrum redundancy / self-healing**；
- **multi-path / spatial diversity**；
- **radial-phase autofocusing / inward energy redistribution**；
- **flat-top / broad capture / reduced relative spreading**；
- **partial coherence** 作为成熟 joint-optimized control，而非主要 novelty mechanism。

这比直接实现 Bessel/Airy/OPB/flat-top/partial-coherence 五个“名字”更科学，也能显著降低后续数值工作量。