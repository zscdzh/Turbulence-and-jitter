# Flat-top 2006–2008：较小相对扩展、源端资源增长与有限孔径功率的机制锚点

## 1. 文献身份与证据角色

本笔记联合读取两篇早期 flat-topped beam 文献：

1. H. T. Eyyuboğlu, Ç. Arpali, Y. Baykal, *Flat topped beams and their characteristics in turbulent media*, Optics Express 14, 4196–4207 (2006), DOI `10.1364/OE.14.004196`；
2. M. Alavinejad, B. Ghafary, F. D. Kashani, *Analysis of the propagation of flat-topped beam with various beam orders through turbulent atmosphere*, Optics and Lasers in Engineering 46, 1–5 (2008), DOI `10.1016/j.optlaseng.2007.07.003`。

综合证据角色：

> **flat-top turbulence-origin + resource-accounting anchor。**

2008 文献强调 higher-order flat-top 在其 average-intensity / beam-width / Strehl 指标下受 turbulence 影响较小；但 2006 文献已经证明 flatness order 增加会同时改变 source size、source power、M² 与 fixed-aperture power-in-bucket。因此“higher order 更抗湍流”不能脱离资源账本解释。

---

## 2. 光束家族与嵌套 Gaussian

这条文献线采用 multi-Gaussian / flat-topped family，以整数 `N` 控制 flatness order：

- `N = 1` 退化为 fundamental Gaussian；
- `N > 1` 时 source intensity 越来越平坦、边缘更陡；
- 论文中的基础 Gaussian source-size 参数保持不变时，**实际 flat-top source size 并不保持不变**。

因此 `N=1` 是天然的 nested Gaussian reference，但不同 `N` 不能因为使用同一个基础 `w0` / `alpha_s` 参数，就被误认为拥有相同物理发射尺度或相同总功率。

这正是本项目以后必须避免的 normalization mistake。

---

## 3. Eyyuboğlu et al. 2006：源端资源随 flatness order 明显变化

### 3.1 作者专门计算了 source resource

该文不仅计算 receiver-plane average intensity，还明确推导并绘制：

- source beam size；
- source beam power；
- source `M²` factor；
- receiver-plane beam size；
- fixed-area power in bucket (PIB)；
- kurtosis / shape evolution。

在固定 Gaussian source-size parameters（示例中 `alpha_sx = alpha_sy = 3 cm`）时，作者明确指出：

> 随 `N` 增大，source profile 更平坦，但实际 source size、source power 和 `M²` 都增加。

并且 source power 对 `N` 的增长速度比 source size 更快。

这意味着：

> **flatness order 本身携带额外源端功率/面积/beam-quality resource。**

任何 fixed-amplitude 或 fixed-basic-width 的 order comparison 都不能直接解释成结构性 turbulence advantage。

### 3.2 2006 示例参数不是本项目场景参数

receiver-plane illustration 中论文使用过：

- `lambda = 1.55 um`；
- `Cn² = 1e-15 m^(-2/3)`；
- 若干 0–5 km propagation examples。

这些仅是论文理论示例值，不冻结为 UAV-FSO 参数。

---

## 4. flat-top 的确表现为“较小相对 spreading”，但这不是完整通信结论

Eyyuboğlu 2006 与 Alavinejad 2008 都得到类似趋势：

> flatness order 增大时，某些定义下的 relative beam spreading 下降；higher-order flat-top 的 average intensity / beam width 对 turbulence 显得更稳定。

Alavinejad 2008 进一步用 average intensity、analytical beam width 和 Strehl ratio 强调 higher-order beam “less affected by turbulence”。

但 Eyyuboğlu 2006 给出了更重要的通信层补充：

> 对固定 receiver aperture，按每一个 `N` 自己的 source power 归一以后，captured power / PIB **反而随着 flatness order 增大而下降**。

作者还明确提醒：如果不按各自 source power 归一，而统一除以 `N=1` Gaussian 的 source power，那么 PIB 会随 `N` 增大而上升——但那实际上把 higher-order beam 自身增加的 transmitted power 也算进“收益”里了。

因此 flat-top 文献给 Paper 1 一个非常明确的护栏：

\[
\boxed{\text{less spreading} \not\Rightarrow \text{higher finite-aperture power at equal transmitted resource}}
\]

这与 Eyyuboğlu 2013 Bessel 文献中“低 scintillation 不等于通信优势”的警告高度一致。

---

## 5. far-field / turbulence 会逐渐抹平 flat-top 结构

2006 Eyyuboğlu 与 2006 Cai 的相关工作都指出：flat-topped beam 传播后会经历明显 shape evolution，并在长传播距离 / turbulence 作用下逐渐趋向 Gaussian-like profile。

Eyyuboğlu 2006 的 receiver-plane shape evolution表现为：

1. 初期中心出现 ring-like structure；
2. 传播继续后环形结构缩窄并出现中心峰；
3. 更远处逐渐向 pure Gaussian profile 收敛；
4. 不同 `N` 的 kurtosis 最终也趋向 `N=1` Gaussian case。

这为 Paper 1 提供一个值得检验的 failure mechanism：

> 即使 source flatness 很高，distributed turbulence + diffraction 也可能逐渐“Gaussianize”其统计 intensity，导致不同 order 的结构差异被压缩。

因此不能默认 transmitter-plane flatness 会完整保留到 receiver。

---

## 6. 与 independent mechanical jitter 的关系

以下是本项目机制推论，不是 2006/2008 文献已证明的结论。

flat-top 对机械 jitter 的潜在优势通常来自 receiver-plane capture function 更平坦、中央 intensity gradient 更小或能量覆盖更宽。但这与早期 turbulence 文献所谓“较少 broadening”不是同一个机制。

因此必须分开问：

1. **turbulence-only：** higher-order profile 是否在 equal resources 下仍保持有意义的 finite-aperture power advantage？
2. **jitter-only：** 更平的 receiver-plane capture region 是否真正提高 displacement tolerance？
3. **joint：** turbulence-induced shape evolution / Gaussianization 是否破坏这种平坦 capture advantage？

如果 flat-top 在 joint channel 下表现较好，必须进一步判断收益来自：

- 真正的 flatness / edge structure；
- 更大的 source footprint；
- 更多 peripheral power；
- 更宽 receiver-plane scale；
- 或以上资源交换的组合。

---

## 7. direct-competitor 边界已经很强

flat-top 不能被当作“过去从未考虑 pointing”的典型空白，因为：

- Jiang et al. 2022 已研究 flat-topped beam + atmospheric turbulence + jitter/bias + average irradiance / average received power；
- Jiang et al. 2026 又进一步研究 pointing error + gamma–gamma turbulence + average BER。

因此 flat-top 在 Paper 1 中更适合定位为：

> **一个可能同时有利于 turbulence spreading 与 lateral-displacement tolerance 的成熟正对照 / mechanism control。**

它对 Paper 1 的价值主要在跨机制统一比较，而不是单独宣称“首次研究 flat-top 的 turbulence + pointing”。

---

## 8. 对 Paper 1 统一评价协议的新增要求

从这条文献链接受以下原则：

1. **flatness order 变化时必须重新计算实际 Tx source size、total power 和 M² / angular-spectrum cost；** 不能只固定一个数学 `w0` 就宣称资源相同；
2. **总发射功率必须先统一。** 不得把 higher-order source 自带的额外 power 当成结构收益；
3. **同时报告 fixed-aperture received fraction / absolute normalized received power。** relative beam width 或 Strehl 只作机制诊断；
4. **至少增加一种 receiver-plane scale-matched 对照。** 用于区分“更宽覆盖”与真正 flat-top edge/shape mechanism；
5. **检查 propagated profile 是否已经 Gaussianize。** 若 receiver plane 的结构已接近 Gaussian，则 source order 本身可能已失去解释力；
6. **flat-top 作为 Paper 1 candidate 的贡献是机制对照，不是 novelty anchor。** direct competitor 已经存在。

---

## 9. 当前裁决

**状态：READ / RESOURCE + TURBULENCE MECHANISM ANCHOR。**

flat-top 仍值得保留在 Paper 1 的候选机制集合中，但角色已经发生收敛：

- 不是“higher order 已证明抗湍流，因此拿来和 Gaussian 比”；
- 而是一个特别适合研究 **turbulence spreading、source resource、finite-aperture capture 与 jitter tolerance 是否同向** 的正对照。

是否最终占据 3–5 个 common-evaluation representatives 的一个名额，应在进一步审查 Jiang 2022/2026 direct competitors 后决定。