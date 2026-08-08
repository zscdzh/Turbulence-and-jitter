#!/usr/bin/env python3
"""Run the frozen Gate-A Gaussian qualification V0-V3."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from turbulence_jitter.gate_a import (  # noqa: E402
    apply_tilt,
    centroid_and_radius,
    circular_capture,
    displaced_gaussian_capture_reference,
    displaced_gaussian_intensity,
    fresnel_propagate,
    gauss_hermite_long_exposure,
    gaussian_field,
    gaussian_references,
    grid_power,
    make_centered_grid,
    normalize_grid_power,
    phase_curvature_coefficient,
)

WAVELENGTH = 1550e-9
W0 = 16.25e-3
N = 512
DX = W0 / 16.0
V1_RATIOS = (0.5, 1.0, 2.0)

V2_W = 10e-3
V2_N = 512
V2_DX = V2_W / 64.0
V2_CASES = ((2.0, 0.0), (1.0, 0.25), (1.0, 1.0), (1.0, 1.5))

V3_DISTANCE = 1000.0
V3_SJ = (0.0, 0.25, 0.50, 0.75)
V3_N_GH = 9


def relerr(value: float, reference: float) -> float:
    return abs(value - reference) / abs(reference)


def run() -> dict:
    grid = make_centered_grid(N, DX)
    u0 = normalize_grid_power(gaussian_field(grid, W0), DX)
    p0 = grid_power(u0, DX)
    z_r, _, _ = gaussian_references(WAVELENGTH, W0, 1.0)

    v0 = []
    v1 = []
    for ratio in V1_RATIOS:
        z = ratio * z_r
        uz = fresnel_propagate(u0, grid, WAVELENGTH, z)
        pz = grid_power(uz, DX)
        _, _, w_num = centroid_and_radius(np.abs(uz) ** 2, grid)
        _, w_ref, c_ref = gaussian_references(WAVELENGTH, W0, z)
        c_num, max_dphi = phase_curvature_coefficient(uz, grid)

        v0.append(
            {
                "z_over_zR": ratio,
                "power_relative_drift": abs(pz - p0) / p0,
            }
        )
        v1.append(
            {
                "z_over_zR": ratio,
                "W_ref_m": w_ref,
                "W_num_m": w_num,
                "W_relative_error": relerr(w_num, w_ref),
                "c_ref_rad_per_m2": c_ref,
                "c_num_rad_per_m2": c_num,
                "c_relative_error": relerr(c_num, c_ref),
                "max_adjacent_phase_rad": max_dphi,
            }
        )

    # Non-gate sign sanity: +10 urad should become +10 mm after 1 km.
    theta_test = 10e-6
    tilted = apply_tilt(u0, grid, WAVELENGTH, theta_test, 0.0)
    tilted_L = fresnel_propagate(tilted, grid, WAVELENGTH, 1000.0)
    x_c, y_c, _ = centroid_and_radius(np.abs(tilted_L) ** 2, grid)

    grid_v2 = make_centered_grid(V2_N, V2_DX)
    v2 = []
    for a_over_w, d_over_w in V2_CASES:
        a_r = a_over_w * V2_W
        d = d_over_w * V2_W
        intensity = displaced_gaussian_intensity(grid_v2, V2_W, d)
        h_num = circular_capture(intensity, grid_v2, a_r)
        h_ref = displaced_gaussian_capture_reference(V2_W, a_r, d)
        v2.append(
            {
                "aR_over_W": a_over_w,
                "d_over_W": d_over_w,
                "H_ref": h_ref,
                "H_num": h_num,
                "relative_error": relerr(h_num, h_ref),
            }
        )

    _, w_vac, _ = gaussian_references(WAVELENGTH, W0, V3_DISTANCE)
    v3 = []
    for s_j in V3_SJ:
        sigma_theta = s_j * w_vac / V3_DISTANCE
        intensity_le = gauss_hermite_long_exposure(
            u0,
            grid,
            WAVELENGTH,
            V3_DISTANCE,
            sigma_theta,
            n_gh=V3_N_GH,
        )
        _, _, w_num = centroid_and_radius(intensity_le, grid)
        w_ref = np.sqrt(w_vac**2 + 4.0 * (V3_DISTANCE * sigma_theta) ** 2)

        outer_guard = (
            (np.abs(grid.X) > 0.4 * grid.window)
            | (np.abs(grid.Y) > 0.4 * grid.window)
        )
        guard_fraction = (
            grid.dx**2 * np.sum(intensity_le[outer_guard])
            / (grid.dx**2 * np.sum(intensity_le))
        )

        v3.append(
            {
                "s_J": s_j,
                "sigma_theta_rad": sigma_theta,
                "W_eff_ref_m": float(w_ref),
                "W_eff_num_m": w_num,
                "relative_error": relerr(w_num, float(w_ref)),
                "outer_10pct_guard_power_fraction": float(guard_fraction),
            }
        )

    results = {
        "contract": "Numerical Implementation Contract v0.1 / Gate A",
        "constants": {
            "wavelength_m": WAVELENGTH,
            "W0_m": W0,
            "z_R_m": z_r,
            "N_v01_v3": N,
            "dx_v01_v3_m": DX,
            "window_v01_v3_m": grid.window,
            "V3_distance_m": V3_DISTANCE,
            "W_vac_1km_m": w_vac,
        },
        "V0": v0,
        "V1": v1,
        "tilt_sign_sanity": {
            "theta_x_rad": theta_test,
            "expected_x_centroid_m": 1000.0 * theta_test,
            "numerical_x_centroid_m": x_c,
            "numerical_y_centroid_m": y_c,
        },
        "V2": v2,
        "V3": v3,
    }

    # Frozen acceptance thresholds.
    assert max(row["power_relative_drift"] for row in v0) <= 1e-4
    assert max(row["W_relative_error"] for row in v1) <= 0.01
    assert max(row["c_relative_error"] for row in v1) <= 0.01
    assert max(row["max_adjacent_phase_rad"] for row in v1) < np.pi / 2.0
    assert max(row["relative_error"] for row in v2) <= 0.005
    assert max(row["relative_error"] for row in v3) <= 0.01

    return results


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
