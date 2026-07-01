# -*- coding: utf-8 -*-
from __future__ import annotations
from pathlib import Path
import sys, csv, numpy as np
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from aj2_utils import ALPHA_CRIT, photon_sphere_x, isco_x, shadow_b_over_m

OUT = ROOT / "tables" / "geodesic_observables.csv"
OUT.parent.mkdir(exist_ok=True)
with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["alpha=a/M", "r_ph/M", "r_ISCO/M", "b_shadow/M", "ell/M"])
    for alpha in np.linspace(0.005, ALPHA_CRIT*0.995, 300):
        mu = 2/alpha
        rph = alpha*photon_sphere_x(mu)
        risco = alpha*isco_x(mu)
        b = shadow_b_over_m(alpha)
        ell_over_M = (alpha**1.5)/np.sqrt(2)
        w.writerow([alpha, rph, risco, b, ell_over_M])
print(OUT)
