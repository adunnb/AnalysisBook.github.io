---
layout: proof
title: "Cauchy Criterion for Series"
chapter: "Sequences and Series"
---

**Theorem:** A series $\sum_{n=1}^{\infty} a_n$ converges if and only if for every $\varepsilon > 0$ there exists $N \in \mathbb{N}$ such that:

$$m > n > N \implies \lvert a_{n+1} + a_{n+2} + \cdots + a_m \rvert < \varepsilon$$

**Remark:** This is simply the [Cauchy criterion for convergence](../T/cauchy-criterion) applied to the sequence of [partial sums](../D/partial-sums). It is useful because it gives a convergence condition that makes no reference to the sum $S$.

**Corollary:** If $\sum_{n=1}^{\infty} a_n$ converges, then $a_n \to 0$. The converse is false — the harmonic series $\sum \frac{1}{n}$ diverges despite $\frac{1}{n} \to 0$.

**Proof:** The series $\sum a_n$ converges if and only if its sequence of partial sums $(s_n)$ converges. By the [Cauchy criterion for convergence](../T/cauchy-criterion), $(s_n)$ converges if and only if it is a [Cauchy sequence](../D/cauchy-sequence), i.e. for every $\varepsilon > 0$ there exists $N$ such that:

$$m > n > N \implies \lvert s_m - s_n \rvert < \varepsilon$$

Since $s_m - s_n = a_{n+1} + a_{n+2} + \cdots + a_m$, this is exactly the stated condition.