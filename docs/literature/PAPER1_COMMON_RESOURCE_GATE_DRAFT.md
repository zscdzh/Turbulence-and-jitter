# PAPER1_COMMON_RESOURCE_GATE_DRAFT

**状态：待项目负责人确认；不是已冻结科学契约。**

本文件把 `PAPER1_PARAMETER_MAPPING_MATRIX.md` 中仍需人工裁决的内容压缩成一个最小 Gate。只有以下问题回答后，才有理由开始 structured-beam 最小代码实现。

## Gate A — common physical resources

建议第一版统一：

1. transmitter：circular hard aperture；
2. equal post-aperture transmitted power `P_T`；
3. receiver：circular finite aperture；
4. all fields share exactly the same turbulence and jitter realizations；
5. source-plane field after aperture is numerically renormalized to equal `P_T`。

这五项的作用是把最明显的 power/aperture advantage 排除掉。

## Gate B — what is *reported*, not necessarily matched

所有场同时报告：

- `r50_T, r80_T, r95_T`；
- peripheral-energy fraction；
- transverse-frequency / angular-spectrum cost；
- no-disturbance `H0`；
- `r50_R, r80_R`；
- generation efficiency if literature-supported。

第一版不强行让上述所有量相同，因为那会把结构机制本身一并消掉。

## Gate C — secondary scale-control

为了判断“收益是不是只来自 spot 更宽/更窄”，只增加一个 secondary diagnostic comparison。

当前两个候选：

### C1. `H0`-matched

每个 structured family 允许调一个 scale，使 no-turbulence/no-jitter finite-aperture capture `H0` 接近 Gaussian。

优点：直接排除初始 throughput 差异。

缺点：可能对 ring/halo fields 存在多个解；也可能人为抹掉其本来就有的 focusing advantage。

### C2. `r50_R`-matched

每个 family 调一个 scale，使 receiver-plane no-disturbance `r50_R` 接近 Gaussian。

优点：更接近“同 spot scale 比 shape”。

缺点：对环形/多峰光场，`r50` 未必充分表示 capture geometry。

当前建议：**优先 C1 (`H0`-matched) 作为 secondary diagnostic；primary result 仍来自 common-resource Level A。**

## Gate D — reference scale

建议主无量纲 jitter 使用固定 Gaussian reference：

\[
j=L\sigma_\theta/w_{ref}.
\]

当前建议 `w_ref` 采用 common-resource Gaussian G0 在 no-turbulence/no-jitter receiver plane 的 `1/e^2` intensity radius，原因：

- 与现有 Gaussian jitter analytic benchmark直接兼容；
- 定义简单；
- 不随 structured family 改变。

如果 G0 在目标距离存在明显非-Gaussian clipping，改用 Gaussian `r50_R`。

## Gate E — provisional core fields

第一轮代码不建议同时实现全部五类文献名词。

建议：

- Gaussian G0/G1；
- Bessel-like `n=0`；
- OPB continuum radial phase；
- flat-top representative。

暂不主跑：

- Airy path-diversity array：multi-beam architecture，保留机制层；
- partial coherence：已有成熟 turbulence+pointing joint optimization，保留 positive-control / discussion。

## Gate F — field-specific blockers

### Bessel

在 circular-truncated `J0` 与 Bessel-Gaussian 中二选一。

当前建议：**先 circular-truncated J0**，因为它与统一 circular Tx aperture 兼容，且最少引入额外 apodization 参数；另做一个 Eyyuboğlu square-window reproduction sanity check 验证机制没有被换掉。

### OPB

当前建议：

- continuum radial phase；
- simple Gaussian or top-hat-like amplitude `A(r)` 必须有明确来源/说明；
- 不实现真实 photoetched mask steps；
- phase strength通过 literature-supported / physically interpretable `W(L)` 或 aperture-edge phase strength确定。

尚需补一个 exact amplitude/representative phase-strength 证据。

### flat-top

当前建议：

- 保留 nested Gaussian property `N=1 -> Gaussian`；
- 第一轮只选一个 moderate order；
- 一个 higher-order point仅作 stress，不进行大范围 order optimization；
- 每个 order都在 aperture 后重新 equal-power normalization。

具体 order 尚需从 2006/2008 + Jiang direct-competitor 参数中裁决。

## Gate G — scene layer

在 coding 开始前还需要冻结至少一个 primary scene：

- wavelength；
- `L`；
- `D_T`；
- `D_R`；
- turbulence strength range；
- `L0/l0` treatment；
- physical jitter anchors映射到 `j`。

当前 multirotor / fixed-wing residual evidence已经足够支持数量级映射，但还不足以单独确定唯一 `sigma_theta`。

## 当前建议

**现在不要开始正式 structured-beam Monte Carlo。**

可以开始的下一类工作是：

1. 关闭 OPB / Bessel / flat-top 三个 field-specific definition blockers；
2. 冻结一个 primary UAV-FSO scene；
3. 然后只实现无湍流 free-space + jitter sanity layer；
4. turbulence module 通过 low-frequency / beam-wander validation 后再合入 common comparison。
