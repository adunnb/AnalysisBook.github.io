---
layout: proof
title: "Linearity of the Integral"
chapter: "Integration"
---

**Theorem:** Let $f, g \in \mathcal{R}[a,b]$ and $c \in \mathbb{R}$. Then:

(i) $f + g \in \mathcal{R}[a,b]$ and $\displaystyle\int_a^b (f + g) = \int_a^b f + \int_a^b g$

(ii) $cf \in \mathcal{R}[a,b]$ and $\displaystyle\int_a^b cf = c\int_a^b f$

**Proof of (i):** Let $\varepsilon > 0$. Since $f, g \in \mathcal{R}[a,b]$, by the [integrability criterion](../T/integrability-criterion) there exist partitions $P_1, P_2$ such that:

$$U(f, P_1) - L(f, P_1) < \frac{\varepsilon}{2}, \qquad U(g, P_2) - L(g, P_2) < \frac{\varepsilon}{2}$$

Let $P = P_1 \cup P_2$. Since for any partition $P$:

$$U(f+g, P) \leq U(f, P) + U(g, P), \qquad L(f+g, P) \geq L(f, P) + L(g, P)$$

we get:

$$U(f+g, P) - L(f+g, P) \leq (U(f,P) - L(f,P)) + (U(g,P) - L(g,P)) < \varepsilon$$

So $f + g \in \mathcal{R}[a,b]$. The value of the integral follows from:

$$L(f, P) + L(g, P) \leq \int_a^b f + \int_a^b g \leq U(f, P) + U(g, P)$$

and similarly for $f + g$, so both are squeezed to the same value.

**Proof of (ii):** For $c \geq 0$, $U(cf, P) = cU(f,P)$ and $L(cf, P) = cL(f,P)$, so integrability and the value follow directly. For $c < 0$ the supremum and infimum swap, giving $U(cf, P) = cL(f,P)$ and $L(cf, P) = cU(f,P)$, and the result follows similarly.