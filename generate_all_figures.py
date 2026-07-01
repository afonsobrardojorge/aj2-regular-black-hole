# -*- coding: utf-8 -*-
from __future__ import annotations
from pathlib import Path
import sys, csv
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
from aj2_utils import MU_CRIT, horizon_roots_mu

OUT = ROOT / "tables" / "horizons.csv"
OUT.parent.mkdir(exist_ok=True)
with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["mu", "x_inner", "x_outer"])
    for mu in np.linspace(MU_CRIT, 30, 120):
        roots = horizon_roots_mu(mu)
        if len(roots) >= 2:
            w.writerow([mu, roots[0], roots[-1]])
print(OUT)
