# Paper 1 外部审查决策问题清单

**用途：** 配合 `PAPER1_EXTERNAL_REVIEW_PACKAGE.md` 使用。  
**目标：** 将外部意见转化为可执行的 Stage A -> Stage B 决策，而不是泛泛讨论。

---

## A. 科学问题与论文边界

1. 当前 Paper 1 主问题是否足够独立：

   > 已有 turbulence-resistant beam mechanisms 在 independent residual pointing jitter 下的敏感性、优势压缩、排序反转和失效区。

   请判断：**成立 / 需要收窄 / 不足以成文**。

2. 当前 Paper 1 与 Paper 2 的边界是否清楚？是否还有任何表述会让第一篇被误读成 turbulence–jitter joint beam design？

3. 如果最终结果是“多数所谓抗湍流光束的优势在 realistic jitter + optimized Gaussian 下显著压缩”，该负结果本身是否具有足够论文价值？需要满足什么附加条件？

4. 最危险的 novelty overclaim 是什么？

---

## B. 文献覆盖与机制分类

5. 当前机制 taxonomy 是否合理：

   - Bessel-like angular-spectrum redundancy / self-healing；
   - Airy-enabled path diversity；
   - OPB / radial autofocusing / inward-energy redistribution；
   - flat-top / broad capture / reduced relative spreading；
   - partial coherence / statistical averaging 作为成熟 joint-optimized control。

6. 是否存在一个明显遗漏、且具有独立 anti-turbulence physics、必须加入 Paper 1 主集合的光束家族？

7. 当前建议的第一轮 common-evaluation set：

   > **Gaussian + Bessel + OPB + flat-top**

   请判断：**接受 / 修改 / 反对**，并给出替代集合。

8. Airy path-diversity array 是否应：

   - A. 进入主数值集合；
   - B. 只做独立架构对照；
   - C. 只保留在文献讨论；
   - D. 其他。

9. Partial coherence 是否应：

   - A. 进入主数值集合；
   - B. 只做 validation / positive control；
   - C. 只保留在文献讨论。

10. Jiang 2022/2026、Liu 2022 HG、Badás 2024/2026 等 direct competitors 是否已经足以约束 novelty？是否还应优先追一条特定引用链？

---

## C. 代表光束与参数映射

11. Bessel 第一代表采用 circular-truncated `J0` 是否合理？还是必须使用 Bessel-Gaussian 才具有更好的实验可实现性与文献连续性？

12. OPB 第一代表采用 continuum radial phase，而不实现真实 32-filament / etched-mask discretization，是否足以回答 Paper 1 的物理问题？

13. flat-top 第一轮只保留：

   - `N=1` nested Gaussian sanity；
   - 一个 moderate order；
   - 必要时一个 high-order stress case；

   是否足够？

14. 将各论文有量纲参数先转换为无量纲 mechanism parameter，再在 common `lambda / a_T / L` 下重建，是否是正确做法？是否存在必须保持的绝对尺度，不能做相似缩放？

---

## D. 公平比较协议

15. Level A 的 common-resource contract 是否合理：

   - same wavelength；
   - same Tx clear aperture；
   - same Rx aperture；
   - same post-aperture transmitted power；
   - paired same turbulence / jitter realizations；
   - transparent source / receiver spatial-scale and peripheral-energy ledger。

16. 除总功率和口径外，哪些 resource 必须硬匹配，哪些只需要报告？

17. Level B 仅开放一个尺度参数做 diagnostic retuning 是否合理？

18. `H0`-matched 与 receiver-scale-matched 两种诊断中，哪一种更适合 Paper 1？是否建议同时做，还是只选一个以避免复杂化？

19. Gaussian 获得 `w_G + quadratic phase/focus` 的小规模 optimized envelope，是否已经足够公平？Gaussian 还必须开放哪些自由度？

20. 是否存在一个更简单、审稿人更容易接受的 fairness protocol？

---

## E. UAV/PAT residual jitter 场景

21. 当前证据：

   - high-performance fixed-wing actual flight约 `8–10 μrad (1σ)`；
   - multirotor retro-FSO + compact fine tracking约 `27–42 μrad per axis` residual reference；
   - pre-fine-tracking multirotor AoA约 `1–3 mrad`。

   是否足以支持 Paper 1 用 dimensionless jitter 为主、physical μrad 只做场景映射？

22. 是否必须在开始 Stage B 前找到 one-way active-transmitter multirotor post-PAT residual 数据？还是当前 evidence chain 已足够用于机制研究？

23. 第一版采用 zero-mean isotropic Gaussian residual，并只增加少量 anisotropic sensitivity，是否合理？

24. Paper 1 如果不做 time-domain dynamics，是否可以暂不使用 residual PSD / correlation time，只保留为讨论和后续扩展？

---

## F. turbulence numerical contract

25. production multi-screen module 至少验证以下量是否足够：

   - beam-wander variance；
   - long-term beam radius；
   - selected scintillation quantity；
   - power conservation / finite-aperture integration；
   - screen-number / spacing convergence；
   - low-frequency treatment sensitivity。

26. 对近地近似恒定 `Cn²` 的主场景，先用 equal-spacing screens 再做 convergence，是否合理？

27. 是否必须在第一版引入高度依赖 `Cn²(z)`、nonuniform screen placement，还是可作为 stress / secondary case？

28. `L0 / l0` 是否必须在 Stage B 启动前冻结为现实物理值，还是可以先做 Kolmogorov-like baseline、随后加 von Kármán sensitivity？

29. 除 Chen 2020 / Chahine 2020 外，是否有一篇必须加入的 phase-screen / split-step 数值锚点，否则当前验证合同不完整？

---

## G. Stage B 启动判断

30. 请选择总决策：

   - **CONTINUE**：当前文献与路线已足以冻结 v0.3 合同并开始最小数值实现；
   - **REVISE**：方向可行，但进入代码前需关闭若干明确 blocker；
   - **STOP**：当前科学问题/创新空间不足，应停止或转向另一问题。

31. 如果是 REVISE，请给出进入代码前必须关闭的**最多五个 blocker**，按优先级排序。

32. 如果是 CONTINUE，请给出最小 Stage B 顺序；请避免提出与论文问题无关的大规模工程验证。

33. 如果是 STOP，请明确指出是：

   - novelty 已被覆盖；
   - representative mechanisms 不能公平比较；
   - UAV scene 不成立；
   - numerical evidence burden 过高；
   - 结果即使成立也难以成文；
   - 其他原因。

---

## H. 希望审查者最终给出的简短结论模板

请最终用以下格式总结：

- **Decision:** CONTINUE / REVISE / STOP
- **Paper 1 scientific question:**
- **Strongest part:**
- **Largest scientific risk:**
- **Mechanism set:**
- **Fairness protocol:**
- **Jitter evidence:**
- **Turbulence model requirement:**
- **Must-fix blockers before code:**
- **Minimum next step:**
- **Claims that must be prohibited:**
