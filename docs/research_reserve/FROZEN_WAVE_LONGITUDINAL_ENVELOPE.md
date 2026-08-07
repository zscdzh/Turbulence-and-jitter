# Frozen Wave 纵向包络设计：独立研究储备

**状态：** PARK / 独立支线储备  
**原记录日期：** 2026-08-06  
**路线校正：** 2026-08-07  
**与当前主线的关系：** 不属于 Paper 1 的“已有抗湍流机制在 independent jitter 下的统一评价”，也不属于 Paper 2 的默认联合设计候选。

## 一、为什么保留

Frozen Wave 的主要辨识度不是横向 anti-jitter，而是利用有限组等频 Bessel 分量合成预定纵向强度包络，使近轴能量在一段传播距离内维持、起伏受控或按目标函数重新分配。

这一机制更自然地对应：

- 移动 FSO 链路的传播距离持续变化；
- 发射端不具备实时变焦或发散角连续调节能力；
- 距离估计、控制延迟或轴向位置存在不确定性；
- 同一静态发射光场需要覆盖一段距离区间；
- 研究 turbulence 是否破坏预设 longitudinal envelope 及其 finite-aperture reliability。

它与当前两篇主线论文的区别是：

- Paper 1 研究既有 turbulence-resistant mechanisms 在 independent mechanical jitter 下的保持、退化和失效；
- Paper 2 只有 Paper 1 给出明确 trade-off 后，才研究 low-dimensional turbulence–jitter co-design；
- Frozen Wave 更自然地研究 longitudinal envelope、range variation 和静态光场替代部分 dynamic refocusing 的边界；
- longitudinal-envelope programmability 不自动意味着抗整体 lateral displacement。

因此不得为了扩充 Paper 1 的机制数量或 Paper 2 的设计候选而强行把 Frozen Wave 并入主线。

## 二、候选科学问题

若未来独立激活，可研究：

> 在有限发射口径、有限总功率和有限接收孔径下，有限能量 Frozen Wave 的纵向包络设计能否提高一段传播距离区间内的最小接收功率、低分位接收功率或链路可用率；这种收益需要付出多少峰值功率、外围能量、发射口径和光场生成复杂度？

这里不要求 Frozen Wave 在所有条件下普适优于 Gaussian。允许的结论类型包括：

- 单一名义距离峰值较低，但距离区间内最低接收功率更高；
- 以更大的外围能量或发射口径换取更低的 range-feedback / dynamic-refocus 要求；
- 在特定距离不确定范围内优于固定参数 Gaussian；
- 与逐距离动态优化 Gaussian 相比仍有差距，但系统复杂度更低。

## 三、最小数学结构

零阶有限能量 Frozen Wave 可用以下形式作为起点：

\[
E_{\mathrm{FW}}(r,0)
=
C_0\,
\Pi\!\left(\frac{2r}{D_T}\right)
\exp\!\left(-\frac{r^2}{w_a^2}\right)
\sum_{n=-N}^{N} A_n J_0(k_{\rho n}r),
\]

\[
k_{zn}=Q+\frac{2\pi n}{L_d},
\qquad
k_{\rho n}=\sqrt{k^2-k_{zn}^2},
\]

\[
A_n=
\frac{1}{L_d}
\int_0^{L_d}
F(z)
\exp\!\left(-i\frac{2\pi n}{L_d}z\right)\,dz.
\]

其中：

- \(F(z)\)：目标 longitudinal envelope；
- \(N\)：Bessel 分量阶数范围；
- \(Q\)：纵向载波参数；
- \([z_1,z_2]\)：目标能量维持区间；
- \(w_a\)：有限能量包络和截断尺度；
- \(D_T\)：实际发射清孔径。

不采用任意像素级优化作为首轮方案。

## 四、合理比较对象

若未来激活，至少比较：

1. 单一中心距离优化的固定 Gaussian；
2. 整个距离区间 minimax / low-tail 优化的固定 Gaussian；
3. 可选的两档或多档可切换 Gaussian；
4. Frozen Wave 固定发射方案；
5. 必要时 Bessel–Gaussian，用于分离普通 quasi-nondiffracting 结构与 longitudinal-envelope programmability。

资源账本至少包括：

- total transmitted power；
- transmitter / receiver aperture；
- main-region / peripheral-energy ratio；
- generation efficiency / wasted orders；
- peak power 与区间最低功率；
- 所需动态调节能力。

## 五、未来最小证伪顺序

### 第一步：无湍流、有限口径

- 复现目标 longitudinal envelope；
- 检查能量守恒、窗口截断和 FFT 回卷；
- 计算不同距离下 finite-aperture received power；
- 建立主区、外围和截断损失账本；
- 与固定 Gaussian 和区间优化 Gaussian 比较。

### 第二步：距离不确定统计

计算：

- \(\min_z P_R(z)\)；
- 距离分布下的低分位 received power；
- 给定门限下可用距离比例；
- longitudinal interval 与 peak/average power 的 Pareto relation。

### 第三步：只有前两步出现非平凡 trade-off 后才加 turbulence

- 检查预设 longitudinal envelope 是否仍有统计意义；
- 以 finite-aperture low-tail power 为主，不以轴上峰值或单幅场形作为结论；
- independent lateral jitter 仅作为 pressure test，不作为该支线的核心创新叙事。

## 六、继续与停止条件

### 可继续

至少出现一项：

- longitudinal-envelope length 与区间最低功率之间存在明确、非平凡且可解释的 trade-off；
- 固定 Frozen Wave 在合理 range-variation 区间内显著优于固定或区间优化 Gaussian；
- 可给出 aperture、主区尺度、longitudinal maintenance interval 与 finite-aperture efficiency 的标度关系或设计边界；
- static Frozen Wave 能以可接受资源代价替代部分 dynamic refocusing / multi-level divergence control。

### 应停止或仅保留负结果

- 优势只体现在 normalized on-axis peak 或 shape similarity；
- finite-aperture received power 始终被 optimized Gaussian 明显压制，且没有合理系统交换；
- 纵向鲁棒性完全来自不可接受的大发射口径或 peripheral energy；
- 为获得结果必须不断增加任意 Bessel 系数或高维优化自由度；
- 与已有 Frozen Wave turbulence / obstruction / communication 工作缺乏实质差异。

## 七、论文定位与激活条件

当前只视为：

- 低成本理论—数值小论文候选；
- 会议论文或短篇传播研究储备；
- 未来在共用 propagation / finite-aperture infrastructure 成熟后可能复用的独立问题。

不应预先表述为：

- Frozen Wave 已被证明优于 Gaussian；
- Frozen Wave 天然同时 anti-turbulence 和 anti-jitter；
- Frozen Wave 是 UAV-FSO 普适最优光束。

只有满足以下任一条件并由负责人明确批准时才转为 ACTIVE：

1. Paper 1 的共用 propagation / finite-aperture 基础已经成熟，可低成本复用；
2. 需要独立会议论文或短篇论文候选；
3. 新文献检查仍确认 longitudinal-envelope / range-uncertainty / finite-aperture reliability 未被充分覆盖。

在激活前，本文件只作为研究储备，不进入当前允许下一步，也不生成 Codex 执行指令。
