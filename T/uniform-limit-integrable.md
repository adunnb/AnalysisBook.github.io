---
layout: proof
title: "Integrability of Uniform Limits"
chapter: "Sequences of Functions"
---

**Theorem:** Let $(f_n)$ be a sequence of [Riemann integrable](../D/riemann-integral) functions on $[a, b]$. If $f_n \to f$ [uniformly](../D/uniform-convergence) on $[a, b]$, then $f \in \mathcal{R}[a,b]$ and:

$$\int_a^b f = \lim_{n \to \infty} \int_a^b f_n$$

**Remark:** This theorem says that uniform convergence allows us to interchange the limit and the integral. This interchange fails in general for pointwise convergence.

**Proof:** Let $\varepsilon > 0$. Since $f_n \to f$ uniformly, there exists $N$ such that for all $x \in [a,b]$:

$$n > N \implies \lvert f_n(x) - f(x) \rvert < \frac{\varepsilon}{2(b-a)}$$

**Integrability of $f$:** For $n > N$, on any subinterval the oscillation of $f$ satisfies:

$$\sup f - \inf f \leq \sup f_n - \inf f_n + \frac{\varepsilon}{b-a}$$

Since $f_n \in \mathcal{R}[a,b]$, by the [integrability criterion](../T/integrability-criterion) there exists a partition $P$ with $U(f_n, P) - L(f_n, P) < \frac{\varepsilon}{2}$. Then:

$$U(f, P) - L(f, P) \leq U(f_n, P) - L(f_n, P) + \frac{\varepsilon}{b-a}(b-a) < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$

So $f \in \mathcal{R}[a,b]$.

**Value of the integral:** For $n > N$, by the [integral inequality](../T/integral-inequality):

$$\left\lvert \int_a^b f_n - \int_a^b f \right\rvert = \left\lvert \int_a^b (f_n - f) \right\rvert \leq \int_a^b \lvert f_n - f \rvert < \frac{\varepsilon}{2(b-a)} \cdot (b-a) = \frac{\varepsilon}{2} < \varepsilon$$

Therefore $\displaystyle\int_a^b f_n \to \int_a^b f$.