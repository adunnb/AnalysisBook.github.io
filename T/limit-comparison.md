---
layout: proof
title: "Limit Comparison Test"
chapter: "Sequences and Series"
---

**Theorem:** Let $(a_n)$ and $(b_n)$ be sequences with $a_n, b_n > 0$ for all $n$. Suppose:

$$L = \lim_{n \to \infty} \frac{a_n}{b_n}$$

(i) If $0 < L < \infty$, then $\sum a_n$ and $\sum b_n$ either both converge or both diverge.

(ii) If $L = 0$ and $\sum b_n$ converges, then $\sum a_n$ converges.

(iii) If $L = \infty$ and $\sum b_n$ diverges, then $\sum a_n$ diverges.

**Proof of (i):** Since $\frac{a_n}{b_n} \to L$ with $0 < L < \infty$, there exists $N$ such that for all $n > N$:

$$\frac{L}{2} < \frac{a_n}{b_n} < \frac{3L}{2}$$

which gives $\frac{L}{2} b_n < a_n < \frac{3L}{2} b_n$. The result follows from the [comparison test](../T/comparison-test) applied to both inequalities.

**Proof of (ii):** Since $\frac{a_n}{b_n} \to 0$, there exists $N$ such that $\frac{a_n}{b_n} < 1$ for all $n > N$, so $a_n < b_n$. By the [comparison test](../T/comparison-test), $\sum a_n$ converges.

**Proof of (iii):** Since $\frac{a_n}{b_n} \to \infty$, there exists $N$ such that $\frac{a_n}{b_n} > 1$ for all $n > N$, so $a_n > b_n$. By the [comparison test](../T/comparison-test), $\sum a_n$ diverges.