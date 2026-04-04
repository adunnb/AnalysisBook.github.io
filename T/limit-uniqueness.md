---
layout: proof
title: "Uniqueness of Limits"
chapter: "Sequences and Series"
---

**Theorem:** If a sequence $(a_n)$ converges, its limit is unique. That is, if $a_n \to L$ and $a_n \to M$, then $L = M$.

**Proof:** Suppose $a_n \to L$ and $a_n \to M$. Let $\varepsilon > 0$. By the [definition of convergence](../D/convergence-sequence), there exist $N_1, N_2 \in \mathbb{N}$ such that:

$$n > N_1 \implies \lvert a_n - L \rvert < \frac{\varepsilon}{2}$$

$$n > N_2 \implies \lvert a_n - M \rvert < \frac{\varepsilon}{2}$$

Let $N = \max(N_1, N_2)$. For all $n > N$, the [triangle inequality](../D/absolute-value) gives:

$$\lvert L - M \rvert = \lvert L - a_n + a_n - M \rvert \leq \lvert L - a_n \rvert + \lvert a_n - M \rvert < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$

Since $\varepsilon > 0$ was arbitrary and $\lvert L - M \rvert < \varepsilon$ for all $\varepsilon > 0$, we conclude $L = M$.