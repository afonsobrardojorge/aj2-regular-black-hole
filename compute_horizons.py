# Development checklist for AJ-2 / AJ-3 v0.3.3

This checklist is the evaluation standard for future versions.

## A. AJ-2 effective model

| Item | Status |
|---|---|
| Mass profile \(m(r)=M(r/(r+a))^3\) | done |
| Core condition \(a^3=2M\ell^2\) | imposed by geometric consistency |
| Density and pressures | done |
| WEC/DEC/SEC analysis | done |
| Curvature invariants | done |
| Horizons and critical mass | done |
| Fixed-\(\ell\) thermodynamics | done |
| Photon sphere, ISCO, shadow | done |
| Magnetic NED reconstruction | done |
| AJ-NED obstruction theorem | done |
| Scalar perturbation potential | done |
| First-pass scalar WKB QNMs | preliminary only |

## B. Missing for a stronger effective-model paper

| Item | Status |
|---|---|
| Higher-order WKB / shooting / time-domain scalar QNMs | missing |
| Numerical comparison with Schwarzschild, Hayward, Bardeen | incomplete |
| Observational bounds on \(\alpha=a/M\) | missing |
| Complete reproducible notebooks | missing |
| External expert review | missing |

## C. Missing for a physical theory

| Item | Status |
|---|---|
| AJ-3 field equations from a concrete action | not done |
| Dynamical derivation of \(a^3=C M\ell^2\) | not done |
| Full axial perturbations | not done |
| Full polar perturbations | not done |
| Gravitational QNMs | not done |
| Slow-rotation sector | not done |
| Kerr-like extension | not done |
| Dynamical collapse | not done |
| Semiclassical evaporation evolution | not done |
| Hyperbolicity of the AJ-3 candidate | not done |

## D. Claims allowed

- AJ-2 is an effective regular black-hole model.
- AJ-2 has a finite de Sitter-like core.
- AJ-2 satisfies WEC and DEC for its effective source.
- AJ-2 violates SEC in the core.
- AJ-2 admits an extremal cold-remnant branch.
- AJ-2 has first-pass scalar-QNM WKB diagnostics.
- AJ-2 has an effective magnetic NED lift that is obstructed as a global microscopic completion.
- AJ-3 defines the missing dynamical-origin problem.

## E. Claims not allowed

- AJ is a final theory of black holes.
- AJ solves the singularity problem in nature.
- AJ-2 is fully stable.
- AJ-2 QNMs are completely calculated.
- AJ-2 predicts real astrophysical remnants.
- The NED reconstruction is the microscopic origin.
- Observations confirm the model.

## F. Next priorities

1. Compute robust scalar QNMs beyond first-order WKB.
2. Derive AJ-3 field equations in full.
3. Test whether AJ-3 generates the saturating density without inserting \(a\).
4. Derive the axial and polar perturbation system.
5. Construct a slow-rotation sector.
6. Build observational constraints on \(\alpha=a/M\) and \(\ell/M\).


## v0.3.3 cleanup status

- License metadata aligned with CC BY 4.0.
- Empty DOI removed from citation metadata.
- `__pycache__` removed from release package.
- Reproducibility guide added.
- Main paper now references the accompanying first-pass WKB table explicitly.
