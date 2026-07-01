---
title: "AJ-2 / Buinheira--Sal Jorge: an effective regular black-hole sector"
subtitle: "v0.3.4 clean-release technical draft"
author: "Afonso Brardo Buinheira Sal Jorge"
date: "2026-05-24"
geometry: margin=1in
fontsize: 11pt
---

> **Status.** This is a technical development draft. It is not peer reviewed. AJ-2 is presented as an effective regular black-hole model, not as a final microscopic theory of black holes.

# Abstract

In geometrized units \(G=c=1\), AJ-2 is an effective static and spherically symmetric regular black-hole model defined by

\[
m(r)=M\left(\frac{r}{r+a}\right)^3,\qquad a^3=2M\ell^2,
\]

and

\[
f(r)=1-\frac{2m(r)}{r}=1-\frac{2Mr^2}{(r+a)^3}.
\] The model replaces the Schwarzschild curvature divergence by a finite de Sitter-like core with curvature controlled by \(\ell\). Its effective source satisfies the weak and dominant energy conditions and violates the strong energy condition in the core. It admits an analytic critical mass, an extremal cold-remnant branch, geodesic diagnostics through the photon sphere, ISCO and shadow radius, an effective magnetic NED reconstruction, and an obstruction showing that a one-invariant magnetic NED with Maxwell weak-field limit and finite UV saturation cannot be a global non-degenerate microscopic completion.

This clean-release package consolidates the AJ-2 effective sector, mathematical appendices, a first-pass scalar-QNM WKB diagnostic and an AJ-3 development program. The core open problem remains dynamical: derive the saturating density profile and the scale relation \(a^3=2M\ell^2\) from an action without inserting \(a\) or \(M\) into the Lagrangian.

# 1. Scientific positioning

AJ-2 belongs to the regular-black-hole literature. It should not be described as the first regular black-hole model or as a final theory of quantum gravity. Its distinctive features are:

1. a rational mass profile;
2. the scale relation \(a^3=2M\ell^2\), chosen so that the central curvature is controlled by \(\ell\);
3. an effective source satisfying WEC and DEC;
4. an analytic extremal cold-remnant branch;
5. a first thermodynamic description at fixed \(\ell\);
6. a magnetic NED lift that is explicitly obstructed as a global microscopic completion;
7. a concrete AJ-3 program aimed at deriving the saturating core dynamically.

The scientifically defensible claim is:

> AJ-2 is a controlled effective regular-black-hole sector of a broader saturating-vacuum framework.

The claim that must not be made is:

> AJ-2 is a complete physical theory of black holes.

# 2. Geometry

The metric is

\[
ds^2=-f(r)dt^2+\frac{dr^2}{f(r)}+r^2d\Omega^2.
\]

The mass profile obeys

\[
m(r)\to M \quad (r\to\infty),
\qquad
m(r)\sim \frac{M}{a^3}r^3 \quad (r\to0).
\]

Thus the central density is finite. Near the origin,

\[
f(r)=1-\frac{2M}{a^3}r^2+O(r^3).
\]

Using \(a^3=2M\ell^2\),

\[
f(r)=1-\frac{r^2}{\ell^2}+O(r^3),
\]

so the core is locally de Sitter-like.

The exterior expansion is

\[
f(r)=1-\frac{2M}{r}+\frac{6Ma}{r^2}+O(r^{-3}).
\]

The \(O(r^{-2})\) term resembles a charge-like deformation with \(Q_{\rm eff}^2=6Ma\). It is not an electric charge; it is only an effective metric coefficient.

# 3. Regularity and effective source

The effective density and pressures are

\[
\rho(r)=\frac{3Ma}{4\pi(r+a)^4},
\]

\[
p_r(r)=-\rho(r),
\]

\[
p_t(r)=\rho(r)\frac{r-a}{r+a}.
\]

At \(r=0\),

\[
p_r(0)=p_t(0)=-\rho(0),
\]

so the core has the equation of state of a de Sitter-like vacuum.

The curvature invariants are finite:

\[
R(r)=\frac{24Ma^2}{(r+a)^5},
\]

\[
R_{\mu\nu}R^{\mu\nu}=
\frac{144M^2a^2(r^2+a^2)}{(r+a)^{10}},
\]

\[
K(r)=
\frac{16M^2(3r^4-6ar^3+21a^2r^2+6a^4)}{(r+a)^{10}}.
\]

At the origin,

\[
R(0)=\frac{12}{\ell^2},\qquad
R_{\mu\nu}R^{\mu\nu}(0)=\frac{36}{\ell^4},\qquad
K(0)=\frac{24}{\ell^4}.
\]

# 4. Energy conditions

The weak energy condition holds:

\[
\rho\ge0,\qquad
\rho+p_r=0,\qquad
\rho+p_t=\rho\frac{2r}{r+a}\ge0.
\]

The dominant energy condition holds:

\[
|p_r|=\rho,\qquad
\left|\frac{p_t}{\rho}\right|=\left|\frac{r-a}{r+a}\right|\le1.
\]

The strong energy condition fails in the core because

\[
\rho+p_r+2p_t=2p_t<0
\qquad (r<a).
\]

This is expected for a nonsingular core.

# 5. Horizons and extremal branch

With

\[
x=\frac{r}{a},\qquad \mu=\frac{r_s}{a}=\frac{2M}{a},
\]

the horizon equation is

\[
(x+1)^3=\mu x^2.
\]

The critical value is

\[
\mu_c=\frac{27}{4},
\]

with extremal horizon

\[
x_+=2.
\]

Thus the black-hole branch satisfies

\[
0<\alpha=\frac{a}{M}\le\frac{8}{27}.
\]

![AJ-2 dimensionless metric function.](../figures/f_profiles.png)

![AJ-2 inner and outer horizon branches.](../figures/horizons_vs_mu.png)

# 6. Thermodynamics at fixed \(\ell\)

At the horizon,

\[
T_H=\frac{1}{4\pi}\left|\frac{r_+-2a}{r_+(r_++a)}\right|
\]

in geometrized units. At the extremal point \(r_+=2a\), \(T_H=0\).

At fixed \(\ell\), parameterizing the branch by \(x=r_+/a\),

\[
M(x)=\frac{\ell}{2}\frac{(x+1)^{9/2}}{x^3},
\]

\[
T(x)=\frac{x-2}{4\pi\ell(x+1)^{5/2}},
\]

\[
C_\ell=2\pi\ell^2
\frac{(x-2)(x+1)^7}{x^4(4-x)}.
\]

The temperature has a maximum at \(x=4\), where \(C_\ell\) diverges and changes sign.

![Fixed-\(\ell\) Hawking temperature.](../figures/temperature_fixed_ell.png)

![Fixed-\(\ell\) heat capacity, wide view with the divergence at \(x=4\).](../figures/heat_capacity_fixed_ell.png)

![Fixed-\(\ell\) heat capacity, limited vertical range near the remnant branch and the sign change at \(x=4\).](../figures/heat_capacity_fixed_ell_limited.png)

![Fixed-\(\ell\) heat-capacity sign structure using a symmetric logarithmic scale.](../figures/heat_capacity_fixed_ell_symlog.png)

# 7. Geodesic observables

The photon sphere satisfies

\[
rf'(r)-2f(r)=0.
\]

In \(x,\mu\) variables,

\[
2(x_{\rm ph}+1)^4=3\mu x_{\rm ph}^3.
\]

The ISCO satisfies

\[
x^5+(8-3\mu)x^4+(10+3\mu)x^3-8x^2-19x-8=0.
\]

The geometric shadow radius is

\[
b_c=\frac{r_{\rm ph}}{\sqrt{f(r_{\rm ph})}}.
\]

For \(a/M\ll1\),

\[
r_{\rm ph}=3M-4a+O(a^2/M),
\]

\[
r_{\rm ISCO}=6M-9a+O(a^2/M),
\]

\[
b_c=3\sqrt3\,M\left[1-\frac{a}{M}+O(a^2/M^2)\right].
\]

![Photon sphere radius.](../figures/photon_sphere.png)

![ISCO radius.](../figures/isco.png)

![Geometric shadow radius.](../figures/shadow_radius.png)

# 8. Scalar perturbations and first-pass QNM diagnostic

For a massless scalar test field,

\[
\frac{d^2\Psi}{dr_*^2}+\left[\omega^2-V_s(r)\right]\Psi=0,
\qquad
\frac{dr_*}{dr}=\frac1{f(r)},
\]

with

\[
V_s(r)=f(r)
\left[
\frac{\ell_s(\ell_s+1)}{r^2}+\frac{f'(r)}{r}
\right].
\]

The supplied code computes a first-order WKB diagnostic at the maximum of \(V_s\). This is not a final QNM calculation. The next required step is to compute scalar QNMs using a robust method such as higher-order WKB, shooting, continued fractions or time-domain evolution.

A representative subset of the accompanying first-pass WKB table is:

Here \(\alpha=0.296\) denotes \(0.999\alpha_c\), close to but below the extremal endpoint \(\alpha_c=8/27\), not the exactly extremal value.

| $\alpha=a/M$ | $\ell_s$ | $n$ | $\mathrm{Re}(\omega M)$ | $-\mathrm{Im}(\omega M)$ |
|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 0.329437 | 0.096256 |
| 0 | 2 | 0 | 0.506321 | 0.096124 |
| 0.1 | 1 | 0 | 0.362363 | 0.099087 |
| 0.1 | 2 | 0 | 0.562520 | 0.099127 |
| 0.2 | 1 | 0 | 0.410574 | 0.100364 |
| 0.2 | 2 | 0 | 0.646615 | 0.100493 |
| 0.25 | 1 | 0 | 0.446492 | 0.098295 |
| 0.25 | 2 | 0 | 0.711004 | 0.098261 |
| 0.296 | 1 | 0 | 0.496528 | 0.087692 |
| 0.296 | 2 | 0 | 0.804549 | 0.086360 |


The full table is provided in `tables/scalar_qnm_first_order_wkb.csv`. These values should be treated as a reproducibility check and a trend diagnostic, not as final QNM predictions.

Rows with \(\ell_s=0\) or higher overtones are included for reproducibility only and should not be interpreted as precision QNM estimates in first-order WKB.


![Exterior scalar potential for \(\alpha=0.05\).](../figures/scalar_potential_alpha_0.05.png)

![Exterior scalar potential for \(\alpha=0.15\).](../figures/scalar_potential_alpha_0.15.png)

![Exterior scalar potential for \(\alpha=0.25\).](../figures/scalar_potential_alpha_0.25.png)

# 9. Magnetic NED reconstruction and obstruction

AJ-2 can be reconstructed as an effective magnetic NED with

\[
F=\frac{q^2}{2r^4}.
\]

The effective Lagrangian is

\[
\mathcal L(F)=
\frac{3}{2\ell^2}
\left[
1+\left(\frac{3}{2\ell^2F}\right)^{1/4}
\right]^{-4}.
\]

It has Maxwell behavior for \(F\to0\) and saturates for \(F\to\infty\). However, a one-invariant magnetic NED of this type cannot be a global microscopic completion.

Define

\[
\Psi=\mathcal L_F+2F\mathcal L_{FF},
\qquad
Y(F)=\sqrt F\,\mathcal L_F.
\]

Then

\[
Y'(F)=\frac{\Psi}{2\sqrt F}.
\]

If \(\Psi\ge0\) globally and \(\mathcal L_F>0\), then \(Y\) is nondecreasing. Maxwell behavior gives \(Y\to0\) as \(F\to0\), while \(\mathcal L_F>0\) implies \(Y>0\) for \(F>0\). Thus at large \(F\),

\[
\mathcal L_F\ge\frac{C}{\sqrt F}
\]

for some \(C>0\), so \(\int^\infty \mathcal L_F\,dF\) diverges. This contradicts finite UV saturation of \(\mathcal L\). Therefore \(\Psi\) must vanish or become negative at finite field strength.

For AJ-2,

\[
\Psi_{\rm AJ2}=\frac{2-3z}{2(1+z)^6},
\qquad
z=\left(\frac{F}{F_0}\right)^{1/4}=\frac{a}{r}.
\]

The degeneracy occurs at

\[
r_\Psi=\frac{3a}{2},
\]

which lies behind the outer horizon on the black-hole branch, since \(r_+\ge2a\). The NED lift is therefore an exterior/intermediate effective description, not a global microscopic theory.

# 10. Why AJ-3 is required

AJ-2 imposes the mass profile. A complete theory must derive it, or derive a controlled deformation of it, from an action. The decisive target is not to insert \(a\) by hand, but to generate the saturating density

\[
\rho(r)=\frac{3}{8\pi\ell^2}\left(\frac{a}{r+a}\right)^4.
\]

If such a density is obtained with \(\rho_0=3/(8\pi\ell^2)\), then the mass integral gives

\[
M=4\pi\int_0^\infty \rho(r)r^2dr=\frac{a^3}{2\ell^2},
\]

and hence

\[
a^3=2M\ell^2.
\]

Thus AJ-3 must explain the density profile dynamically. It must not contain \(M\) or \(a\) as parameters of the Lagrangian.

# 11. Development status and open problems

AJ-2 is a mathematically controlled effective regular-black-hole sector. It is not yet a complete physical theory. The following problems remain open:

1. derive the scale relation \(a^3=2M\ell^2\) from field equations;
2. construct an AJ-3 action that generates the saturating core;
3. derive complete axial and polar perturbation equations;
4. compute scalar and gravitational QNMs using robust numerical methods;
5. construct a slow-rotation sector and then a Kerr-like extension;
6. study dynamical formation and evaporation;
7. derive quantitative observational bounds on \(\alpha=a/M\) and \(\ell/M\);
8. compare in detail with Bardeen, Hayward, Dymnikova, Bronnikov/NED, gravastars, Planck stars and limiting-curvature models;
9. obtain external expert review.

# 12. Claims to keep and claims to avoid

Keep:

- AJ-2 is an effective regular black-hole model.
- AJ-2 removes the Schwarzschild curvature divergence within a static effective model.
- AJ-2 satisfies WEC and DEC for its effective source.
- AJ-2 admits an extremal cold-remnant branch.
- AJ-2 has a magnetic NED lift that is obstructed as a global microscopic completion.
- AJ-2 has first-pass scalar perturbative and QNM diagnostics.

Avoid:

- AJ solves black-hole singularities.
- AJ is quantum gravity.
- AJ-2 is fully stable.
- AJ-2 predicts real astrophysical remnants.
- The NED lift is fundamental.
- The model is observationally confirmed.

# 13. Conclusion

AJ-2 is no longer only an intuition: it is a developed effective model with derivations, figures, code and first perturbative diagnostics. The next scientific step is not further rhetorical refinement. It is calculation: AJ-3 field equations, robust QNMs, full perturbations, rotation, dynamics and observational bounds.

## Reproducibility and algebraic validation

The accompanying package includes scripts to regenerate the figures and the first-pass scalar WKB table. It also includes symbolic checks for the curvature invariants, the ISCO polynomial and the energy-condition algebra. These checks are not a substitute for external peer review, but they make the main analytic claims easier to inspect and reproduce.
