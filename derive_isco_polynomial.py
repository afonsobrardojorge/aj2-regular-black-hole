# -*- coding: utf-8 -*-
"""AJ-2 dimensionless utilities.

Variables:
    M = 1 in most scripts.
    alpha = a/M.
    x = r/a.
    mu = r_s/a = 2M/a = 2/alpha.

Black-hole branch:
    0 < alpha <= 8/27
    mu >= 27/4
"""

from __future__ import annotations
import numpy as np
from scipy.optimize import brentq, minimize_scalar

MU_CRIT = 27.0 / 4.0
ALPHA_CRIT = 8.0 / 27.0

def f_r(r: float | np.ndarray, alpha: float) -> float | np.ndarray:
    """Metric function f(r) for M=1 and a=alpha."""
    a = alpha
    return 1.0 - 2.0 * r**2 / (r + a)**3

def fp_r(r: float | np.ndarray, alpha: float) -> float | np.ndarray:
    a = alpha
    return 2.0 * r * (r - 2.0*a) / (r + a)**4

def fpp_r(r: float | np.ndarray, alpha: float) -> float | np.ndarray:
    a = alpha
    return -4.0 * (r**2 - 4*a*r + a**2) / (r + a)**5

def f_x(x: float | np.ndarray, mu: float) -> float | np.ndarray:
    return 1.0 - mu * x**2 / (x + 1.0)**3

def positive_real_roots(coeffs, min_x=0.0):
    roots = np.roots(coeffs)
    vals = []
    for r in roots:
        if abs(r.imag) < 1e-8 and r.real > min_x:
            vals.append(float(r.real))
    return sorted(vals)

def horizon_roots_mu(mu: float):
    # (x+1)^3 - mu x^2 = x^3 + (3-mu)x^2 + 3x + 1.
    return positive_real_roots([1.0, 3.0-mu, 3.0, 1.0], min_x=0.0)

def outer_horizon_r(alpha: float) -> float:
    mu = 2.0/alpha
    roots = horizon_roots_mu(mu)
    if not roots:
        return np.nan
    return alpha*roots[-1]

def photon_sphere_x(mu: float) -> float:
    # 2(x+1)^4 - 3 mu x^3 = 0.
    coeffs = [2.0, 8.0-3.0*mu, 12.0, 8.0, 2.0]
    roots = positive_real_roots(coeffs, min_x=0.0)
    h = horizon_roots_mu(mu)
    outer = h[-1] if h else 0.0
    outside = [r for r in roots if r > outer + 1e-8]
    return outside[-1] if outside else np.nan

def isco_x(mu: float) -> float:
    # x^5 + (8-3mu)x^4 + (10+3mu)x^3 -8x^2 -19x -8 = 0.
    coeffs = [1.0, 8.0-3.0*mu, 10.0+3.0*mu, -8.0, -19.0, -8.0]
    roots = positive_real_roots(coeffs, min_x=0.0)
    h = horizon_roots_mu(mu)
    outer = h[-1] if h else 0.0
    outside = [r for r in roots if r > outer + 1e-8]
    return outside[-1] if outside else np.nan

def scalar_potential(r: float | np.ndarray, alpha: float, ell_s: int) -> float | np.ndarray:
    f = f_r(r, alpha)
    return f * (ell_s*(ell_s+1)/r**2 + fp_r(r, alpha)/r)

def shadow_b_over_m(alpha: float) -> float:
    mu = 2.0/alpha
    xph = photon_sphere_x(mu)
    rph = alpha*xph
    fph = f_r(rph, alpha)
    return rph / np.sqrt(fph)
