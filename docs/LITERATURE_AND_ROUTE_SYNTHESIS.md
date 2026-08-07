# LITERATURE_AND_ROUTE_SYNTHESIS

**更新日期：** 2026-08-07  
**状态：** 路线纠正版。本文用于组织当前文献调研，不替代逐篇文献锚点和最终科学契约。  
**阶段边界：** `docs/RESEARCH_STAGE_BOUNDARY.md`

## 1. 当前领域结构

当前文献至少包含四条相邻研究线：

1. turbulence + pointing error 的联合信道或 wave-optics 建模；
2. Gaussian beam width / divergence / aperture 等常规 pointing-robust optimization；
3. Bessel、Airy、pin-like、flat-top、partially coherent、statistical beam shaping 等 turbulence-resistant structured beams；
4. flat-top、super-Gaussian、Gaussian–LG、annular-like irradiance 等 jitter-oriented beam shaping。

前两条说明“联合 turbulence 与 pointing”本身不构成创新。第四条主要约束未来 Paper 2 的 jitter-only 零假设。

Paper 1 的真正入口在第三条：

> 多类 turbulence-resistant beams 的提出与评价主要围绕湍流机制，但这些机制并不天然等价于对 independent mechanical pointing jitter 鲁棒。

因此 Paper 1 首先研究“抗湍流机制遇到 jitter 后会怎样”，而不是直接研究 joint optimum beam。

## 2. Paper 1 的机制主线

当前文献调研应按机制建立地图，而不是先选某两个设计家族。

### 2.1 self-healing / angular-spectrum redundancy

代表：Bessel / Bessel–Gaussian 等。

需要核对：

- 作者所谓 self-healing 在 turbulence 下具体恢复什么；
- 是否评价 finite-aperture power 还是只看主瓣/结构相似度；
- peripheral energy 和 transmitter aperture 付出了什么代价；
- 对整体 lateral shift 是否仍然敏感。

关键假设：局部扰动后的结构恢复不自动等于固定接收孔径对整体偏移不敏感。

### 2.2 caustic / self-accelerating propagation

代表：Airy 或其他 caustic-like beams。

需要核对：

- 抗 turbulence 的机制是轨迹、焦散重建、主瓣保持还是 beam wander reduction；
- 其曲线传播或非对称结构怎样影响固定 circular aperture；
- 对 independent jitter 的横向容差是否真正优于 matched Gaussian。

### 2.3 self-focusing / pin-like / longitudinal energy concentration

代表：optical pin beam、self-focusing / abruptly autofocusing 类中的合适代表。

需要核对：

- 优势是否主要来自维持轴上能量或抑制 beam spreading；
- 更窄的局部热点是否反而提高 jitter sensitivity；
- 轴向鲁棒性与横向有限孔径鲁棒性是否被混用。

### 2.4 flat-top / flattened / super-Gaussian

这类结构同时出现在 turbulence-resistant 和 jitter-oriented 文献中，因此是连接 Paper 1 与 Paper 2 的重要桥梁。

Paper 1 关心的是：已有 flat-top/flattened turbulence claims 加入 independent jitter 后的保持或退化。

Paper 2 若最终采用该家族，才研究 joint design / optimum order / scale migration。

Jiang 2022/2026 等 joint pointing+turbulence 工作属于必须审计的直接竞争边界，不能再宣称“首次研究 flat-top 在 turbulence + pointing 下的性能”。

### 2.5 partial coherence / statistical beam shaping

需要核对：

- turbulence robustness 是否主要体现为 scintillation reduction；
- beam spreading、source complexity 与 finite-aperture power 是否被同时计入；
- 加入 independent jitter 后，较宽长期光斑带来的容差究竟是结构机制还是资源交换。

### 2.6 vector / mode-diversity 类

暂不默认纳入 Paper 1。

只有在文献证明其提供与上述机制不同、且能在当前计算复杂度下公平评价的物理机制时，才作为补充代表。不得为了扩大论文内容机械增加模式、偏振和高维自由度。

## 3. Paper 1 的文献选择原则

每个机制优先寻找：

1. 定义/奠基或明确阐释抗湍流机制的论文；
2. 性能较强、与 Gaussian 有清楚比较的论文；
3. 必要时一篇实验或外场论文。

总目标：初筛约 30–40 篇，逐篇精读约 15–20 篇锚点。

不是每篇都进入仿真。Paper 1 最终只选约 3–5 个机制真正不同、定义清楚、资源可比且计算上可实现的代表光束。

## 4. 每篇文献统一提取字段

### 4.1 文献与证据角色

- 题目、作者、年份、期刊/会议、DOI；
- 理论、数值、室内实验或外场；
- 模型来源、参数来源、机制锚点、直接竞争或 Paper 2 背景。

### 4.2 光场与资源

- 发射场公式；
- waist / scale / order / mode parameters；
- transmitter aperture 与硬截断；
- total power normalization；
- peripheral / halo energy；
- generation efficiency、无用级次或额外器件（若相关）。

### 4.3 turbulence

- spectrum / phase-screen / analytical model；
- `Cn2`、`r0`、Rytov 等强度定义；
- beam wander 是否包含；
- single-screen / multi-screen；
- low-frequency treatment；
- weak/strong turbulence 适用边界。

### 4.4 pointing / jitter

- angular or lateral displacement；
- per-axis std、radial RMS、bias；
- distribution / PSD / correlation time；
- platform attitude、PAT error 还是 post-loop residual；
- 是否独立于 turbulence；
- 是否可能重复计入 beam wander。

### 4.5 receiver and metric

- receiver aperture / detector type；
- mean irradiance / scintillation / beam wander / power / outage / BER / capacity；
- finite-aperture received power 是否真正计算；
- Gaussian baseline 是否优化；
- 结论依赖什么 normalization。

### 4.6 参数来源等级

每个重要数字标记为：

- theoretical definition；
- measured / experimental；
- cited external value；
- engineering hardware parameter；
- simulation assumption；
- plotting / stress-test parameter。

## 5. 已经确认的共用方法锚点

### Liu / Jiang 2021

作用：joint wave-optics 方法定义与 weak-turbulence benchmark。

已接受：

- independent jitter 主链优先用 transmitter angular tilt；
- `sigma_theta` 是 per-axis angular standard deviation；
- finite-aperture received power 为主观测；
- single-screen `0.36 L` 仅作 weak-turbulence benchmark；
- 文中 `5–15 microrad` 等数字不得继承为 UAV residual-jitter 实测参数。

详见 `docs/literature/LIU_JIANG_2021_METHOD_ANCHOR.md`。

## 6. Paper 2 的前序边界

### Badás 2024

作用：jitter-only beam-shaping 零假设。

已确认：

- Gaussian 本身也应认真优化 beam width；
- Gaussian + LG / annular-like irradiance 的 jitter-only 权重与尺度优化已经有较成熟前序；
- 不同通信目标对应不同最优 irradiance distribution；
- 正交偏振首先实现非相干强度叠加，不能未经验证宣称 atmospheric diversity。

因此这篇文献主要约束 Paper 2，而不应把 Paper 1 改造成 Gaussian–LG joint optimization。

详见 `docs/literature/BADAS_2024_JITTER_OPTIMIZATION_ANCHOR.md`。

## 7. 直接竞争工作的审计方向

必须系统搜索并记录：

- structured beam + turbulence + pointing error；
- flat-top / flattened beam + turbulence + jitter / boresight；
- Bessel / Airy / HG / other structured beam + pointing error；
- aircraft/UAV platform + structured beam + turbulence + pointing；
- finite-aperture low-tail/outage 与 structured beam 的已有工作。

这些工作用于划定 Paper 1 的创新边界。

Paper 1 不能声称：

- 首次联合 turbulence 与 pointing；
- 首次在 phase-screen 中加入 pointing error；
- 首次计算 turbulence + pointing 下 finite-aperture received power；
- 首次研究任意 structured beam 在 turbulence + pointing 下的性能。

Paper 1 更窄的潜在贡献是：

> 按抗湍流**机制**而非模式名称，对现有 turbulence-resistant beams 在 independent residual jitter 下的保持、退化和失效进行统一比较，并形成可解释的机制敏感性与适用域。

## 8. Paper 1 的统一评价原则

Paper 1 不是 joint design paper。

第一层：保留文献代表参数，复现/确认原 turbulence claim 后加入 independent jitter。

第二层：必要时做有限尺度 retuning 与 optimized Gaussian 对照。

禁止：

- 为每种 structured beam 做多参数 joint optimization；
- 先预注册 flattened-Gaussian/Gaussian–LG 再反过来组织 Paper 1；
- 为得到正结果不断增加模式、偏振、相干性和自由度。

主输出应是：

- turbulence advantage retention ratio / degradation；
- ranking compression or reversal；
- jitter sensitivity；
- finite-aperture low-tail reliability；
- resource-normalized mechanism effect；
- applicability / failure regime。

## 9. Paper 2 的逻辑入口

只有 Paper 1 形成稳定 trade-off，才把机制结论转化为设计原则，例如：

- central capture efficiency 与 lateral coverage 的矛盾；
- turbulence redistribution 与 peripheral energy reservoir 的矛盾；
- narrow-core turbulence robustness 与 jitter tolerance 的矛盾。

然后再寻找少参数 co-robust field。

flattened-/super-Gaussian、Gaussian–LG/annular-like 只是可能种子。最终是否采用它们由 Paper 1 决定。

## 10. 当前执行原则

当前首要任务正是**扩展并整理关键文献库**，此前“不要再扩展文献清单、先实现 Gaussian 和候选场”的旧执行原则已失效。

正确顺序：

1. 文献机制地图；
2. 逐篇证据与参数提取；
3. direct-competitor 审计；
4. 文献证据饱和；
5. 冻结 Paper 1 的代表机制与统一评价协议；
6. 再讨论最小数值实现；
7. Paper 1 结果出来后，才决定 Paper 2 是否启动以及采用什么设计家族。

当前不启动正式 structured-beam coding、大规模 multi-screen Monte Carlo 或 Paper 2 joint optimization。
