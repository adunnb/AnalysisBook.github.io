---
layout: proof
title: "Bolzano–Weierstrass Theorem"
chapter: "Sequences and Series"
---

**Theorem:** Every bounded sequence has a convergent subsequence.

**Proof:** Let $(a_n)$ be a bounded sequence. We construct a monotone subsequence, which by the [monotone convergence theorem](../T/monotone-convergence) must converge.

Call an index $n \in \mathbb{N}$ a **peak** if $a_n \geq a_m$ for all $m > n$, i.e. $a_n$ is greater than or equal to all subsequent terms.

**Case 1: There are infinitely many peaks.** Let $n_1 < n_2 < n_3 < \cdots$ be the peak indices in order. Then by definition of a peak:

$$a_{n_1} \geq a_{n_2} \geq a_{n_3} \geq \cdots$$

So $(a_{n_k})$ is a decreasing [subsequence](../D/subsequence). Since $(a_n)$ is bounded, so is $(a_{n_k})$, and by the [monotone convergence theorem](../T/monotone-convergence) it converges.

**Case 2: There are finitely many peaks.** Let $N$ be the index of the last peak. Starting from $n_1 = N + 1$, since $n_1$ is not a peak there exists $n_2 > n_1$ with $a_{n_2} \geq a_{n_1}$. Since $n_2$ is not a peak there exists $n_3 > n_2$ with $a_{n_3} \geq a_{n_2}$, and so on. This produces an increasing subsequence:

$$a_{n_1} \leq a_{n_2} \leq a_{n_3} \leq \cdots$$

Since $(a_n)$ is bounded, so is $(a_{n_k})$, and by the [monotone convergence theorem](../T/monotone-convergence) it converges.

In both cases we have found a convergent subsequence of $(a_n)$.