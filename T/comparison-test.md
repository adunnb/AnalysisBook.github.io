---
layout: proof
title: "Comparison Test"
chapter: "Sequences and Series"
---

**Theorem:** Let $(a_n)$ and $(b_n)$ be sequences with $0 \leq a_n \leq b_n$ for all $n \in \mathbb{N}$.

(i) If $\sum_{n=1}^{\infty} b_n$ converges, then $\sum_{n=1}^{\infty} a_n$ converges.

(ii) If $\sum_{n=1}^{\infty} a_n$ diverges, then $\sum_{n=1}^{\infty} b_n$ diverges.

**Proof of (i):** Let $s_n = \sum_{k=1}^{n} a_k$ and $t_n = \sum_{k=1}^{n} b_k$ be the partial sums. Since $a_n \geq 0$, $(s_n)$ is increasing. Since $a_n \leq b_n$:

$$s_n \leq t_n \leq \sum_{n=1}^{\infty} b_n$$

So $(s_n)$ is increasing and bounded above, and by the [monotone convergence theorem](../T/monotone-convergence) it converges. Therefore $\sum a_n$ converges.

**Proof of (ii):** This follows from (i) by contrapositive.