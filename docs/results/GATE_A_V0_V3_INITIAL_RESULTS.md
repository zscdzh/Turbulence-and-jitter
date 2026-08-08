# Gate A V0–V3 initial numerical qualification

**日期：2026-08-07**  
**实现合同：** `docs/NUMERICAL_IMPLEMENTATION_CONTRACT_V01.md`  
**范围：** Gaussian vacuum / finite-aperture capture / deterministic Gaussian-jitter benchmark only

## 负责人摘要

本轮只验证共同数值底座，不含 turbulence、phase screen 或 structured field。

初步结果：V0、V1、V2、V3 均 PASS。这些结果只说明 Gate-A kernel 与预注册解析关系一致，不授权 V4–V5 或 structured-field implementation。

## V0 — free-space power conservation

冻结点：`z/z_R = 0.5, 1, 2`。

最大 full-grid power relative drift：`0.000e+00`。

Acceptance：`<= 1e-4`。

**PASS**。

## V1 — Gaussian radius / phase curvature

参数：`lambda=1550 nm`，`W0=16.25 mm`，`z_R=535.210845218 m`。

三个冻结传播点的最大 radius relative error：`0.000e+00`。

最大 quadratic phase-curvature relative error：`1.501e-16`。

fitting region 内最大相邻 phase difference：`0.204687500 rad < pi/2`。

**PASS**。

### Tilt sign non-gate sanity

输入 `theta_x=+10 urad`，`L=1000 m`。

解析 centroid：`+10.000000 mm`；数值 centroid：`+10.000000000000 mm`。

说明 frozen Fresnel / tilt sign chain 一致。

## V2 — displaced Gaussian finite-aperture capture

| `a_R/W` | `d/W` | `H_ref` | `H_num` | relative error |
|---:|---:|---:|---:|---:|
| 2.00 | 0.00 | 0.999664537 | 0.999662491 | 0.0002% |
| 1.00 | 0.25 | 0.830859361 | 0.830504456 | 0.0427% |
| 1.00 | 1.00 | 0.396499039 | 0.395912116 | 0.1480% |
| 1.00 | 1.50 | 0.113279246 | 0.112941629 | 0.2980% |

最大 relative error：`0.2980%`。

Acceptance：`<= 0.5%`。

**PASS**。

## V3 — Gaussian jitter broadening

`L=1000 m`，vacuum Gaussian radius `W_vac=34.436977380 mm`。使用 `9 x 9` product Gauss–Hermite quadrature。

| `s_J` | `sigma_theta` [urad] | `W_eff,ref` [mm] | `W_eff,num` [mm] | relative error |
|---:|---:|---:|---:|---:|
| 0.00 | 0.000000000 | 34.436977380 | 34.436977380 | 2.015e-16 |
| 0.25 | 8.609244345 | 38.501711180 | 38.501711180 | 1.802e-16 |
| 0.50 | 17.218488690 | 48.701240458 | 48.701240458 | 0.000e+00 |
| 0.75 | 25.827733035 | 62.082143857 | 62.082143857 | 0.000e+00 |

最强 `s_J=0.75` 的 outer 10% guard power fraction：`5.351e-12`。

Acceptance：`<= 1%`。

**PASS**。

## 证据边界

已支持：vacuum Gaussian propagation、finite-aperture capture、deterministic tilt 与 independent isotropic Gaussian jitter broadening kernel 与冻结解析 benchmark 一致。

尚未支持：turbulence phase-screen normalization、beam wander、scintillation、multi-screen convergence、production grid、structured-field comparison，或 Gaussian 在正式 turbulence–jitter scene 下的性能优势。

## 决策

**CONTINUE — Gate A V0–V3 initial qualification PASS.**

下一步应先审查代码与上述结果，再决定是否进入 Gate B / V4–V5 implementation contract；不应直接启动 structured-field code。
