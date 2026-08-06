# SCIENTIFIC_CONTRACT_DRAFT

状态：Draft v0.1  
日期：2026-08-06

## 1. 科学问题

本项目研究近地面 UAV-FSO 链路中，大气湍流与独立机械残余抖动对发射光场联合最优结构的影响。

核心问题：

> 在有限发射口径、有限接收口径和固定链路几何下，独立 residual pointing jitter 是否改变 turbulence-resistant beams 的性能排序、最优参数和适用域？

需要区分三个最优问题：

- turbulence-only optimum；
- jitter-only optimum；
- joint turbulence–jitter optimum。

若三者没有可观察差异，或者联合最优始终等价于普通 Gaussian 束宽优化，则第二阶段新光场路线应停止。

## 2. 研究对象与边界

### 2.1 包含

- 1550 nm 标量或两正交偏振分量的波动光学传播；
- 圆形有限发射与接收孔径；
- 自由空间角谱法或 Fresnel split-step；
- von Kármán / modified von Kármán 多相位屏；
- turbulence-induced beam wander；
- 独立二维机械角抖动；
- 后续可选静态 boresight bias；
- 大面积直接探测下的有限孔径接收功率。

### 2.2 暂不包含

- 完整飞行动力学和 PAT 控制器；
- AO 瞬时补偿；
- 单模光纤耦合；
- 模式分解接收机；
- 复杂调制编码；
- 高维逆设计和神经网络。

## 3. 统一传播模型

发射面复场记为

\[
U_0(x,y;\boldsymbol\alpha),
\]

其中 \(\boldsymbol\alpha\) 是光场参数。

第 \(m\) 段传播为

\[
U_{m+1}
=
\mathcal P_{\Delta z_m}
\left[
U_m\exp(i\phi_m)
\right],
\]

其中：

- \(\mathcal P_{\Delta z_m}\)：自由空间传播算子；
- \(\phi_m(x,y)\)：第 \(m\) 个湍流相位屏；
- 相位屏应包含足够低频信息以产生 beam wander。

独立机械角抖动优先通过发射面倾斜加入：

\[
U_0'(x,y)
=
U_0(x,y)
\exp\left[ik(\theta_xx+\theta_yy)\right],
\]

\[
\theta_x,\theta_y
\sim
\mathcal N(0,\sigma_\theta^2).
\]

接收面平移可作为快速近似和交叉验证，但不能默认替代完整倾斜传播。

## 4. 三类位移

必须分别记录：

1. \(\boldsymbol\rho_{bw}\)：由湍流相位屏传播产生的质心漂移；
2. \(L\boldsymbol\theta_j\)：平台、云台和 PAT/FSM 闭环后的机械残余位移；
3. \(\boldsymbol\rho_b\)：慢 boresight bias。

不得把 phase-screen 已包含的 beam wander 再作为独立 pointing loss 重复叠加。

## 5. 有限孔径接收功率

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

主统计量：

- \(Q_{5\%}(H)\)：5% 分位功率；
- \(P_{out}=\Pr(H<H_{th})\)：中断概率；
- 完整 ECDF。

辅助量：

- 平均接收功率；
- aperture-averaged scintillation；
- 接收面质心；
- 长期光斑尺度；
- halo power fraction。

## 6. 捕获函数框架

对湍流 realization \(\omega\)，定义有限孔径捕获函数：

\[
G(\boldsymbol\Delta;\omega)
=
\int A_R(\mathbf r)
I(\mathbf r-\boldsymbol\Delta;\omega)
\,d^2\mathbf r.
\]

机械抖动等价于用其位移概率分布随机采样 \(G\)。

优先研究两个统一描述量。

### 6.1 小抖动曲率

\[
\kappa(\omega)
=
-\frac12\operatorname{tr}
\left[\nabla^2G(\mathbf0;\omega)\right].
\]

\(\kappa\) 越小，中心附近越平坦，小抖动二阶损失越低。

### 6.2 阈值覆盖面积

\[
\mathcal A(H_{th};\omega)
=
\operatorname{area}
\{\boldsymbol\Delta:G(\boldsymbol\Delta;\omega)\ge H_{th}\}.
\]

它描述较大偏移下仍能维持通信门限的位移区域。

需要检验这些量能否解释不同光场的低尾性能和排名反转。

## 7. 无量纲坐标

第一阶段优先使用：

\[
\tau=D_T/r_0,
\qquad
j=L\sigma_\theta/w_{ref},
\qquad
\alpha=D_R/(2w_{ref}),
\qquad
N_F=D_TD_R/(\lambda L).
\]

其中 \(w_{ref}\) 必须在每组结果中明确定义，可以是参考 Gaussian 的无湍流接收面尺度或统一包围能量尺度。

## 8. 初始光场家族

### 8.1 Gaussian 基线

每个信道参数点允许单独优化束腰和必要的二次相位。禁止使用固定教科书参数作为唯一基线。

### 8.2 Flattened-Gaussian

初始家族：

\[
U_N(r,0)=C_N
\exp(-r^2/w_0^2)
\sum_{m=0}^{N}
\frac{(r^2/w_0^2)^m}{m!}
\exp\left(-i\frac{kr^2}{2f}\right)
\Pi(r/a_T).
\]

初始阶数：\(N=0,1,2,4,8\)。\(N=0\) 为 Gaussian 嵌套基线。

### 8.3 正交偏振 Gaussian–LG 双模

\[
\mathbf E_0
=
\sqrt\eta E_G\hat{\mathbf x}
+
\sqrt{1-\eta}E_{LG_{0,1}}\hat{\mathbf y}.
\]

偏振不敏感探测时：

\[
I=\eta|E_G|^2+(1-\eta)|E_{LG}|^2.
\]

初始变量：

- \(\eta\)：Gaussian 功率比例；
- \(s=w_{LG}/w_G\)：相对束宽；
- 可选公共二次相位。

需要同时检查：

- 接收功率相关系数；
- 功率—位移平台；
- 最优权重是否位于内部区域；
- 收益是否只能由更宽长期光斑解释。

### 8.4 Bessel–Gaussian 或 OPB 对照

用途不是寻找第一候选，而是检验：

- 自愈是否转化为整体偏移容差；
- 窄主瓣和外围储能对有限孔径低尾功率的真实作用。

## 9. 比较原则

不存在唯一的“公平归一化”。本项目采用资源账本与互补比较口径。

### 9.1 硬件资源口径

报告并尽量固定：

- 总发射功率；
- 实际发射清孔径；
- 接收口径；
- 波长和距离；
- 光场生成效率和无用级次；
- 硬孔径截断。

### 9.2 结构机制口径

可进一步匹配：

- 无湍流接收面包围能量尺度；
- 无扰动有限孔径功率；
- 长期光斑尺度。

该口径用于判断收益来自更宽覆盖还是独立结构机制。

候选不要求在所有口径下都获胜，但结论必须清楚说明：

- 使用了什么额外资源；
- 换来了什么收益；
- 哪部分收益在匹配尺度后保留。

## 10. 最小可检验假设

- H1：turbulence-only 排名在加入独立 jitter 后会发生反转或压缩；
- H2：flattened-Gaussian 的最优阶数随湍流和抖动强度系统变化；
- H3：Gaussian–LG 双模在部分联合区域存在非端点最优权重；
- H4：Bessel/OPB 的自愈或 beam-wander 优势不自动转化为机械抖动优势；
- H5：复杂光场在强湍流或大接收孔径区域可能退化为优化 Gaussian；
- H6：捕获函数曲率、阈值覆盖面积、长期尺度和模态相关性能够压缩主要性能差异。

## 11. 第一阶段最低成文条件

至少满足一项：

1. 稳定、连续的模式排序反转；
2. 可用少数无量纲参数表达的适用域；
3. 捕获函数描述量与低尾功率之间形成可复用关系；
4. 明确证明若干常见“抗湍流”机制在独立 jitter 下系统失效；
5. 得到复杂光场退化为 Gaussian 的清晰边界。

仅有少量参数点的光束排行榜不足以成文。

## 12. 第二阶段启动条件

仅当出现以下证据时启动：

- flattened-Gaussian 最优阶数稳定为 \(N>0\)，或 Gaussian–LG 最优权重稳定处于内部；
- 收益跨连续参数区域存在；
- 收益可被结构机制解释；
- 与优化 Gaussian 相比，效果量具有论文意义；
- 资源代价仍适合目标应用场景。

## 13. 停止条件

- 联合最优在绝大多数区域回到 Gaussian；
- 所有收益可完全由普通束宽/发散角解释；
- 结果对随机种子、网格或少数参数点高度不稳定；
- 只有闪烁指数下降，而低尾有限孔径功率不改善；
- 模式排序没有稳定规律，也不能形成明确失效边界；
- 为保住方向必须不断增加模式、偏振、相干性或机器学习自由度。

## 14. 初始数值范围

第一轮只用于模型验证和粗筛，不作为最终论文参数：

- 波长：1550 nm；
- 距离：1 km 主场景，2–3 km 压力场景；
- 发射口径：40–80 mm 中选择一档主基准；
- 接收口径：至少两档；
- 湍流：从无湍流到 \(D_T/r_0\approx4\)；
- 归一化 jitter：\(j=0,0.1,0.25,0.5,1,2\)；
- 粗筛样本：每点 300–500；
- 关键点复核：2000 以上；
- 所有候选使用共同相位屏和共同 jitter realization。

物理参数最终应根据数值窗口、Fresnel 数和目标 UAV 场景重新冻结，不能机械照搬调研报告中的初始数字。
