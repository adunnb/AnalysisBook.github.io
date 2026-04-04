---
layout: proof
title: "Density of the Rationals"
chapter: "Completeness and the Real Numbers"
---

**Theorem:** For every two real numbers $a, b \in \mathbb{R}$ with $a < b$, there exists a rational number $q \in \mathbb{Q}$ such that $a < q < b$.

**Remark:** This theorem says that between any two real numbers, no matter how close together, there is always a rational number. The rationals are therefore **dense** in $\mathbb{R}$.

**Proof:** Since $a < b$, we have $b - a > 0$. By the [Archimedean property](../T/archimedean), there exists $n \in \mathbb{N}$ such that:

$$\frac{1}{n} < b - a$$

which gives $na < nb$ and $n(b-a) > 1$. By the [Archimedean property](../T/archimedean) again, the set $\{m \in \mathbb{Z} : m > na\}$ is non-empty, so let $m$ be its smallest element. Then:

$$m - 1 \leq na < m$$

which gives $m \leq na + 1 < nb$, so:

$$a < \frac{m}{n} < b$$

Setting $q = \frac{m}{n} \in \mathbb{Q}$ completes the proof.