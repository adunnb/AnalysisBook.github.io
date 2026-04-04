---
layout: proof
title: "Alternating Series Test"
chapter: "Sequences and Series"
---

**Theorem:** Suppose $(a_n)$ is a sequence satisfying:

1. $a_n \geq 0$ for all $n \in \mathbb{N}$
2. $(a_n)$ is decreasing: $a_{n+1} \leq a_n$ for all $n$
3. $a_n \to 0$

Then the alternating series $\sum_{n=1}^{\infty} (-1)^{n+1} a_n = a_1 - a_2 + a_3 - a_4 + \cdots$ converges.

**Proof:** Let $s_n$ denote the $n$-th partial sum. Consider the even partial sums:

$$s_{2n} = (a_1 - a_2) + (a_3 - a_4) + \cdots + (a_{2n-1} - a_{2n})$$

Since $(a_n)$ is decreasing, each parenthesized term is non-negative, so $(s_{2n})$ is increasing. Also:

$$s_{2n} = a_1 - (a_2 - a_3) - \cdots - (a_{2n-2} - a_{2n-1}) - a_{2n} \leq a_1$$

So $(s_{2n})$ is increasing and bounded above by $a_1$. By the [monotone convergence theorem](../T/monotone-convergence), $s_{2n} \to S$ for some $S \in \mathbb{R}$.

For the odd partial sums: $s_{2n+1} = s_{2n} + a_{2n+1}$. Since $a_{2n+1} \to 0$:

$$s_{2n+1} = s_{2n} + a_{2n+1} \to S + 0 = S$$

Since both the even and odd partial sums converge to $S$, we conclude $s_n \to S$.