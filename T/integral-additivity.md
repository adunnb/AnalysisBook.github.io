---
layout: proof
title: "Additivity over Subintervals"
chapter: "Integration"
---

**Theorem:** Let $f : [a, b] \to \mathbb{R}$ be bounded and let $c \in (a, b)$. Then $f \in \mathcal{R}[a,b]$ if and only if $f \in \mathcal{R}[a,c]$ and $f \in \mathcal{R}[c,b]$, in which case:

$$\int_a^b f = \int_a^c f + \int_c^b f$$

**Proof:** Let $\varepsilon > 0$.

**($\Rightarrow$)** Suppose $f \in \mathcal{R}[a,b]$. By the [integrability criterion](../T/integrability-criterion), there exists a partition $P$ of $[a,b]$ with $U(f,P) - L(f,P) < \varepsilon$. Refining $P$ to include $c$ if necessary, write $P = P_1 \cup P_2$ where $P_1$ is a partition of $[a,c]$ and $P_2$ of $[c,b]$. Then:

$$U(f, P_1) - L(f, P_1) \leq U(f,P) - L(f,P) < \varepsilon$$

and similarly for $P_2$, so $f \in \mathcal{R}[a,c]$ and $f \in \mathcal{R}[c,b]$.

**($\Leftarrow$)** Suppose $f \in \mathcal{R}[a,c]$ and $f \in \mathcal{R}[c,b]$. Choose partitions $P_1$ of $[a,c]$ and $P_2$ of $[c,b]$ with:

$$U(f,P_1) - L(f,P_1) < \frac{\varepsilon}{2}, \qquad U(f,P_2) - L(f,P_2) < \frac{\varepsilon}{2}$$

Then $P = P_1 \cup P_2$ is a partition of $[a,b]$ with $U(f,P) - L(f,P) < \varepsilon$, so $f \in \mathcal{R}[a,b]$.

The integral identity follows from:

$$\int_a^b f = U(f) = U(f\vert_{[a,c]}) + U(f\vert_{[c,b]}) = \int_a^c f + \int_c^b f$$