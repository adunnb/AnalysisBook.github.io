---
layout: proof
title: "Fundamental Theorem of Calculus II"
chapter: "Integration"
---

**Theorem:** Let $f : [a,b] \to \mathbb{R}$ be [Riemann integrable](../D/riemann-integral). If $G : [a,b] \to \mathbb{R}$ is [differentiable](../D/derivative) on $[a,b]$ with $G' = f$, then:

$$\int_a^b f = G(b) - G(a)$$

**Remark:** This theorem provides the practical tool for evaluating integrals. While FTC I establishes the theoretical connection between differentiation and integration, FTC II gives the computational method: find an antiderivative and evaluate at the endpoints.

**Proof:** Let $\varepsilon > 0$. By the [integrability criterion](../T/integrability-criterion), there exists a partition $P = \{x_0, x_1, \ldots, x_n\}$ of $[a,b]$ such that $U(f,P) - L(f,P) < \varepsilon$.

By the [mean value theorem](../T/mean-value), on each subinterval $[x_{k-1}, x_k]$ there exists $t_k \in (x_{k-1}, x_k)$ such that:

$$G(x_k) - G(x_{k-1}) = G'(t_k)(x_k - x_{k-1}) = f(t_k)(x_k - x_{k-1})$$

Summing over all subintervals:

$$G(b) - G(a) = \sum_{k=1}^{n} f(t_k)(x_k - x_{k-1})$$

Since $m_k \leq f(t_k) \leq M_k$ for each $k$:

$$L(f, P) \leq G(b) - G(a) \leq U(f, P)$$

Since $f \in \mathcal{R}[a,b]$, we also have $L(f,P) \leq \int_a^b f \leq U(f,P)$. Therefore:

$$\left\lvert G(b) - G(a) - \int_a^b f \right\rvert \leq U(f,P) - L(f,P) < \varepsilon$$

Since $\varepsilon > 0$ was arbitrary, $\int_a^b f = G(b) - G(a)$.