---
layout: proof
title: "Integral Inequality"
chapter: "Integration"
---

**Theorem:** Let $f, g \in \mathcal{R}[a,b]$.

(i) If $f(x) \geq 0$ for all $x \in [a,b]$, then $\displaystyle\int_a^b f \geq 0$.

(ii) If $f(x) \leq g(x)$ for all $x \in [a,b]$, then $\displaystyle\int_a^b f \leq \int_a^b g$.

(iii) $\lvert f \rvert \in \mathcal{R}[a,b]$ and $\displaystyle\left\lvert \int_a^b f \right\rvert \leq \int_a^b \lvert f \rvert$.

**Proof of (i):** If $f \geq 0$ then $m_k \geq 0$ for all subintervals, so $L(f, P) \geq 0$ for all partitions $P$. Therefore $\int_a^b f = L(f) \geq 0$.

**Proof of (ii):** Apply (i) to $g - f \geq 0$ and use [linearity](../T/integral-linearity):

$$0 \leq \int_a^b (g - f) = \int_a^b g - \int_a^b f$$

**Proof of (iii):** Since $-\lvert f(x) \rvert \leq f(x) \leq \lvert f(x) \rvert$, applying (ii) and [linearity](../T/integral-linearity):

$$-\int_a^b \lvert f \rvert \leq \int_a^b f \leq \int_a^b \lvert f \rvert$$

which gives $\left\lvert \int_a^b f \right\rvert \leq \int_a^b \lvert f \rvert$. The integrability of $\lvert f \rvert$ follows from the fact that $\bigl\lvert \lvert f(x) \rvert - \lvert f(y) \rvert \bigr\rvert \leq \lvert f(x) - f(y) \rvert$, so the oscillation of $\lvert f \rvert$ on any subinterval is bounded by that of $f$.