---
layout: proof
title: "Convergence of Subsequences"
chapter: "Sequences and Series"
---

**Theorem:** If $(a_n)$ converges to $L$, then every [subsequence](../D/subsequence) $(a_{n_k})$ also converges to $L$.

**Proof:** Suppose $a_n \to L$ and let $(a_{n_k})$ be a subsequence. Let $\varepsilon > 0$. By the [definition of convergence](../D/convergence-sequence), there exists $N \in \mathbb{N}$ such that:

$$n > N \implies \lvert a_n - L \rvert < \varepsilon$$

Since $(n_k)$ is strictly increasing, $n_k \geq k$ for all $k$. Therefore for all $k > N$:

$$n_k \geq k > N \implies \lvert a_{n_k} - L \rvert < \varepsilon$$

So $a_{n_k} \to L$.

**Corollary:** If $(a_n)$ has two subsequences converging to different limits, then $(a_n)$ diverges. This is the standard method for proving divergence by the [divergence criterion](../T/divergence-criterion).