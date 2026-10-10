---
layout: proof
title: "Summation Formulas"
chapter: "The Natural Numbers"
link_terms: ["sum of the first n natural numbers", "sum of squares"]
---

**Theorem:** For every $n \in \mathbb{N}$:

$$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$$

$$1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}$$

**Remark:** The first formula can also be seen by pairing terms. For example, $1 + 2 + \cdots + 10 = 55$: pairing the first and last terms, the second and next-to-last, and so on gives five pairs, each with sum $11$.

**Proof:** Both formulas are proved by [mathematical induction](../T/induction).

*First formula.* For $n = 1$, both sides equal $1$. If the formula holds for $n = k$, then:

$$1 + 2 + \cdots + k + (k+1) = \frac{k(k+1)}{2} + (k+1) = \frac{(k+1)(k+2)}{2}$$

which is the formula for $n = k + 1$.

*Second formula.* For $n = 1$, both sides equal $1$. If the formula holds for $n = k$, then:

$$\sum_{j=1}^{k+1} j^2 = \frac{k(k+1)(2k+1)}{6} + (k+1)^2 = \frac{(k+1)(2k^2 + 7k + 6)}{6} = \frac{(k+1)(k+2)(2k+3)}{6}$$

which is the formula for $n = k + 1$.
