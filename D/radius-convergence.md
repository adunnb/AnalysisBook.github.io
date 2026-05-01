---
layout: definition
title: "Radius of Convergence"
chapter: "Sequences of Functions"
---

**Definition:** Given a [power series](../D/power-series) $\sum_{n=0}^{\infty} c_n(x-a)^n$, the **radius of convergence** is the extended real number:

$$R = \frac{1}{\limsup_{n \to \infty} \lvert c_n \rvert^{1/n}}$$

with the conventions $\frac{1}{0} = \infty$ and $\frac{1}{\infty} = 0$.

The power series converges absolutely for all $x$ with $\lvert x - a \rvert < R$ and diverges for all $x$ with $\lvert x - a \rvert > R$. The set $(a - R, a + R)$ is called the **interval of convergence**.

**Remark:** The behavior of the power series at the endpoints $x = a \pm R$ must be checked separately for each series and is not determined by $R$ alone. When $R = \infty$ the series converges for all $x \in \mathbb{R}$.