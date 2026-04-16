---
layout: proof
title: "Integrability of Continuous Functions"
chapter: "Integration"
---

**Theorem:** If $f : [a, b] \to \mathbb{R}$ is [continuous](../D/continuity) on $[a, b]$, then $f$ is [Riemann integrable](../D/riemann-integral) on $[a, b]$.

**Proof:** Let $\varepsilon > 0$. Since $f$ is continuous on a closed bounded interval, by the [uniform continuity theorem](../T/uniform-continuity-theorem) it is [uniformly continuous](../D/uniform-continuity) on $[a, b]$. So there exists $\delta > 0$ such that:

$$\lvert x - y \rvert < \delta \implies \lvert f(x) - f(y) \rvert < \frac{\varepsilon}{b - a}$$

Choose a [partition](../D/partition) $P = \{x_0, x_1, \ldots, x_n\}$ with mesh $\lVert P \rVert < \delta$. On each subinterval $[x_{k-1}, x_k]$, since $f$ is continuous it attains its supremum $M_k$ and infimum $m_k$ at some points $u_k, v_k \in [x_{k-1}, x_k]$. Since $\lvert u_k - v_k \rvert \leq \lVert P \rVert < \delta$:

$$M_k - m_k = f(u_k) - f(v_k) = \lvert f(u_k) - f(v_k) \rvert < \frac{\varepsilon}{b-a}$$

Therefore:

$$U(f, P) - L(f, P) = \sum_{k=1}^{n} (M_k - m_k)(x_k - x_{k-1}) < \frac{\varepsilon}{b-a} \sum_{k=1}^{n} (x_k - x_{k-1}) = \frac{\varepsilon}{b-a} \cdot (b-a) = \varepsilon$$

By the [integrability criterion](../T/integrability-criterion), $f \in \mathcal{R}[a,b]$.