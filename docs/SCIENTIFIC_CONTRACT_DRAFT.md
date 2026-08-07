# SCIENTIFIC_CONTRACT_DRAFT

**状态：** Draft v0.2 — 路线纠正版，尚未完成文献驱动的参数冻结  
**日期：** 2026-08-07  
**当前适用对象：** Paper 1 的文献机制地图与后续统一评价。Paper 2 联合设计单独列出，不得混入当前执行任务。  
**阶段权威边界：** `docs/RESEARCH_STAGE_BOUNDARY.md`

## 1. Paper 1 科学问题

当前首先研究的不是“什么光束在 turbulence + jitter 下 joint optimum”，而是：

> 文献中已经提出的不同 turbulence-resistant beam mechanisms，在加入独立机械 residual pointing jitter 后，哪些原有抗湍流优势能够保持、哪些明显退化、哪些发生排序反转？这种差异能否形成可解释的 jitter-sensitivity map、applicability regime 或 failure boundary？

Paper 1 的核心对象是**已有抗湍流机制**，不是提前设计新的联合鲁棒光束。

不得把以下问题偷换成 Paper 1 主任务：

- 直接寻找 flattened-Gaussian 的 joint optimum order；
- 直接寻找 Gaussian–LG 的 joint optimum weight；
- 为所有 structured beams 做多参数联合优化；
- 把“联合 turbulence 与 pointing error”本身当作创新。

## 2. Paper 2 条件性科学问题

只有 Paper 1 形成稳定机制 trade-off 后，才允许研究：

> 能否依据 Paper 1 暴露出的抗湍流机制与 anti-jitter 需求之间的矛盾，构造一个少参数、可解释、资源透明的 turbulence–jitter co-robust beam？

Paper 2 才允许定义 joint objective、比较 turbulence-only / jitter-only / joint optimum，并优化少量结构参数。

flattened-/super-Gaussian、Gaussian–LG/annular-like 当前仅是可能的设计种子，不是已冻结候选。

## 3. Paper 1 / Stage A：文献机制契约

在数值模型开始前，必须先建立文献证据矩阵。

### 3.1 文献按机制组织

初始需要覆盖但尚未冻结的机制包括：

- self-healing / angular-spectrum redundancy；
- caustic / self-accelerating propagation；
- self-focusing / pin-like / longitudinal concentration；
- flat-top / flattened / super-Gaussian；
- partial coherence / statistical beam shaping；
- 必要时再加入提供独立机制且计算成本合理的 vector / mode-diversity 类。

### 3.2 每篇关键文献必须提取

- 文献身份与证据等级；
- 发射场数学定义；
- 关键光场参数及其物理含义；
- 作者声称的抗湍流机制；
- turbulence model、强度范围和适用边界；
- 是否包含 turbulence-induced beam wander；
- 是否包含 independent pointing jitter / boresight bias；
- 发射/接收口径、距离、波长；
- Gaussian baseline 的定义和优化权限；
- 总功率、外围能量、硬孔径、生成损耗等资源；
- 评价指标及其局限；
- 参数属于理论定义、实测值、引用值还是作者仿真假设；
- 对整体 lateral displacement 的潜在敏感性；
- 对 Paper 1 或 Paper 2 的证据角色。

### 3.3 文献充分条件

目标不是机械凑篇数。建议初筛约 30–40 篇，精读约 15–20 篇锚点，并在以下条件接近满足时认为可以进入 Stage B：

- 每个核心机制都有方法/定义锚点；
- 关键模型定义至少有独立来源交叉确认；
- UAV/PAT residual jitter 的定义和现实量级有系统或实验依据；
- multi-screen turbulence / low-frequency beam-wander 数值问题有专门方法依据；
- direct-competitor 检索不再出现会实质改写 Paper 1 科学问题的新工作；
- 新增文献不再显著改变机制分类、代表光束选择或创新边界。

## 4. Paper 1 / Stage B：统一评价对象

文献冻结后，只选择约 3–5 个机制真正不同的代表光束。最终名单由 Stage A 决定，当前不预注册具体模式动物园。

每个代表机制至少比较：

1. turbulence only；
2. jitter only；
3. turbulence + independent jitter。

第一层优先使用原文有依据的代表参数，用来回答：

> 原抗湍流设计加入 independent jitter 后还剩多少优势？

第二层仅在必要时允许有限、透明的尺度 retuning，以及与 optimized Gaussian 的共同任务对照，用来判断收益是结构机制还是单纯的 beam spreading / peripheral energy / aperture resource exchange。

Paper 1 不要求为每个 structured beam 寻找完整 joint optimum。

## 5. 共用传播模型

发射面复场记为

\[
U_0(x,y;\boldsymbol\alpha),
\]

其中 \(\boldsymbol\alpha\) 在 Paper 1 中首先表示**文献给出的代表场参数**；只有明确授权的有限 retuning 才作为优化变量。

多相位屏传播计划表示为

\[
U_{m+1}
=
\mathcal P_{\Delta z_m}
\left[
U_m\exp(i\phi_m)
\right].
\]

正式 turbulence model 尚未冻结，后续必须由专门文献确定：

- Kolmogorov / von Karman / modified von Karman spectrum；
- inner / outer scale；
- phase-screen number and spacing；
- subharmonic 或其他 low-frequency treatment；
- beam-wander accuracy；
- grid / window / propagation sampling requirements。

Liu/Jiang 2021 的 single-screen `0.36 L` 模型只保留为 weak-turbulence benchmark，不作为正式生产模型。

## 6. independent mechanical jitter

当前接受 independent mechanical residual jitter 优先通过 transmitter angular tilt 进入 wave optics：

\[
U_0'(x,y)
=
U_0(x,y)
\exp\left[ik(\theta_xx+\theta_yy)\right].
\]

若使用零均值各向同性 Gaussian jitter：

\[
\theta_x,\theta_y\sim\mathcal N(0,\sigma_\theta^2),
\]

其中 `sigma_theta` 明确定义为**单轴 angular standard deviation**，单位 rad。

接收面平移可用于快速近似或交叉验证，但不能默认替代完整倾斜传播。

真实 UAV/PAT 的 `sigma_theta`、PSD、相关时间与各向异性尚未冻结，必须由系统/实验文献建立证据链。

## 7. 三类横向运动

必须分别记录：

1. \(\boldsymbol\rho_{bw}\)：由 turbulence realization 产生的接收面 centroid wander；
2. \(L\boldsymbol\theta_j\)：independent mechanical residual jitter 对应的位移尺度；
3. \(\boldsymbol\rho_b\)：static / slow boresight bias。

不得把 phase-screen 已包含的 beam wander 再作为独立 pointing loss 重复叠加。

## 8. Gaussian jitter sanity check

对于

\[
I(x,y)\propto\exp[-2(x^2+y^2)/W^2]
\]

定义的 Gaussian `1/e^2` intensity radius `W`，无湍流二维独立角 jitter 应满足

\[
W_{\rm eff}^2=W^2+4L^2\sigma_\theta^2.
\]

该式只作为 jitter implementation 的解析 benchmark，不能在 beam-radius convention 不一致时直接使用。

## 9. finite-aperture received power

圆形接收孔径半径为 \(a_R\)。单次 realization 下：

\[
P_R
=
\iint_{x^2+y^2\le a_R^2}
|U_L(x,y)|^2\,dx\,dy.
\]

归一化接收功率：

\[
H=P_R/P_T.
\]

Paper 1 的主统计证据应来自：

- finite-aperture received-power samples；
- ECDF；
- 一个或多个低分位指标；
- 必要时给定明确门限的 outage。

point irradiance、peak intensity、scintillation、shape similarity、mode fidelity 只能作为机制诊断，不能单独证明通信优势。

## 10. Paper 1 的机制描述量

当前候选解释量包括但尚未冻结：

- capture function \(G(\Delta;\omega)\)；
- 中心附近位移敏感性或曲率；
- threshold coverage area；
- long-term beam scale；
- peripheral / halo power fraction；
- turbulence-induced centroid wander；
- 与发射/接收 aperture 有关的无量纲比例。

这些量的作用是解释“为什么某类抗湍流机制怕或不怕 independent jitter”，而不是增加 Paper 1 的优化自由度。

## 11. Gaussian baseline 与比较原则

Paper 1 至少需要两类 Gaussian 角色：

1. 原代表文献自身使用的 Gaussian comparison（用于复现和理解原抗湍流主张）；
2. 针对共同任务认真处理的 Gaussian baseline（用于判断 structured-beam 优势是否只是尺度或资源交换）。

不得只与固定教科书 Gaussian 比较。

同时必须公开：

- 总发射功率；
- 发射清孔径；
- 接收口径；
- 硬孔径截断；
- peripheral / halo energy；
- generation efficiency 或无用级次（若相关）；
- 无扰动接收功率和长期光斑尺度。

新光束不要求在所有归一化口径下普适获胜，但资源代价必须透明。

## 12. Paper 1 可检验假设

当前只保留机制层假设：

- H1：turbulence-only superiority 不足以预测 turbulence + independent-jitter reliability；
- H2：self-healing / angular-spectrum redundancy 不自动转化为整体 lateral-displacement tolerance；
- H3：窄核心、高中心梯度或强能量集中机制可能提高 jitter sensitivity；
- H4：flat capture / wider coverage 可能降低 jitter sensitivity，但必须区分结构效应与额外外围能量；
- H5：partial-coherence 或 scintillation reduction 不保证 finite-aperture low-tail power 更高；
- H6：不同机制在加入 jitter 后可能出现排序压缩、反转或明确失效区；
- H7：上述差异可能由少量 capture / scale / resource descriptors 解释。

当前不把“flattened-Gaussian 最优阶数”或“Gaussian–LG 内部权重”列为 Paper 1 假设，它们属于可能的 Paper 2 问题。

## 13. Paper 1 最低成文条件

Paper 1 不能退化为几种光束的排行榜。至少需要形成一项以上可复用机制结论，例如：

1. 一类或多类抗湍流机制在 independent jitter 下出现稳定的优势压缩、反转或失效边界；
2. 不同机制的 jitter sensitivity 能形成清楚的机制分类；
3. 若干结果能用少量无量纲或 capture descriptors 归纳；
4. 证明常见“抗湍流”指标不能直接预测 finite-aperture joint reliability；
5. 给出对 UAV-FSO beam selection 有明确意义的 applicability / failure map。

## 14. Paper 2 启动条件

只有 Paper 1 明确揭示设计 trade-off 后，才允许冻结 Paper 2 科学契约。

最低条件包括：

- trade-off 跨连续参数区域稳定存在；
- 不能被普通 Gaussian scale optimization 完全解释；
- 可以转化为少参数设计原则；
- 资源代价适合目标场景；
- 与现有 jitter-only / turbulence-only beam shaping 文献相比仍有明确创新空间。

Paper 2 的设计种子暂包括 flattened-/super-Gaussian、Gaussian–LG/annular-like 等，但不预先承诺使用任何一种。

## 15. 当前数值参数状态

当前**不冻结**以下此前 Draft 中出现过的候选数字：

- 1550 nm；
- 1 km 主场景、2–3 km 压力场景；
- 40–80 mm 发射口径；
- 任何固定接收口径；
- `D_T/r0 ≈ 4`；
- `j = 0, 0.1, 0.25, 0.5, 1, 2`；
- 300–500 或 2000+ realization。

这些值目前只能作为前序讨论中的候选，不得机械进入实现。物理场景、UAV/PAT residual jitter、turbulence strength、aperture、sample size 与统计置信要求必须由 Stage A 文献证据重新冻结。

## 16. 当前允许的下一步

当前只允许推进文献驱动的 Paper 1 Stage A：

- 关键文献识别；
- 逐篇参数和机制证据提取；
- direct-competitor 审计；
- mechanism map 与 literature evidence matrix；
- 文献充分后冻结 Paper 1 代表机制和评价协议。

在负责人再次批准前，不直接实现 structured-beam families，不启动正式 multi-screen Monte Carlo，不进行 Paper 2 joint optimization。
