---
layout: proof
title: "Integrability of Monotone Functions"
chapter: "Integration"
---

**Theorem:** If $f : [a, b] \to \mathbb{R}$ is [monotone](../D/monotone-sequence) on $[a, b]$, then $f$ is [Riemann integrable](../D/riemann-integral) on $[a, b]$.

**Proof:** Without loss of generality suppose $f$ is increasing — the decreasing case is analogous. Then $f$ is bounded since $f(a) \leq f(x) \leq f(b)$ for all $x \in [a,b]$.

Let $\varepsilon > 0$. Choose $n \in \mathbb{N}$ large enough so that:

$$\frac{(f(b) - f(a))(b - a)}{n} < \varepsilon$$

which is possible by the [Archimedean property](../T/archimedean). Let $P = \{x_0, x_1, \ldots, x_n\}$ be the uniform partition with $x_k = a + \frac{k(b-a)}{n}$. Since $f$ is increasing, on each subinterval $[x_{k-1}, x_k]$:

$$M_k = f(x_k), \qquad m_k = f(x_{k-1})$$

Therefore:

$$U(f, P) - L(f, P) = \sum_{k=1}^{n} (f(x_k) - f(x_{k-1}))(x_k - x_{k-1})$$

$$= \frac{b-a}{n} \sum_{k=1}^{n} (f(x_k) - f(x_{k-1})) = \frac{(b-a)(f(b) - f(a))}{n} < \varepsilon$$

By the [integrability criterion](../T/integrability-criterion), $f \in \mathcal{R}[a,b]$.