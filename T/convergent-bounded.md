---
layout: proof
title: "Boundedness of Convergent Sequences"
chapter: "Sequences and Series"
---

**Theorem:** Every convergent sequence is bounded.

**Proof:** Let $(a_n)$ be a sequence with $a_n \to L$. Applying the [definition of convergence](../D/convergence-sequence) with $\varepsilon = 1$, there exists $N \in \mathbb{N}$ such that:

$$n > N \implies \lvert a_n - L \rvert < 1$$

By the [triangle inequality](../D/absolute-value), for all $n > N$:

$$\lvert a_n \rvert = \lvert a_n - L + L \rvert \leq \lvert a_n - L \rvert + \lvert L \rvert < 1 + \lvert L \rvert$$

The finitely many terms $a_1, a_2, \ldots, a_N$ are bounded by $\max(\lvert a_1 \rvert, \ldots, \lvert a_N \rvert)$. Therefore, setting:

$$M = \max(\lvert a_1 \rvert, \ldots, \lvert a_N \rvert, 1 + \lvert L \rvert)$$

we have $\lvert a_n \rvert \leq M$ for all $n \in \mathbb{N}$, so $(a_n)$ is [bounded](../D/bounded-sequence).