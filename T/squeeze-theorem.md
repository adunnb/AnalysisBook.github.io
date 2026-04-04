---
layout: proof
title: "Squeeze Theorem"
chapter: "Sequences and Series"
---

**Theorem:** Let $(a_n)$, $(b_n)$, and $(c_n)$ be sequences satisfying:

$$a_n \leq b_n \leq c_n \quad \text{for all } n \in \mathbb{N}$$

If $a_n \to L$ and $c_n \to L$, then $b_n \to L$.

**Proof:** Let $\varepsilon > 0$. Since $a_n \to L$ and $c_n \to L$, there exist $N_1, N_2 \in \mathbb{N}$ such that:

$$n > N_1 \implies \lvert a_n - L \rvert < \varepsilon$$

$$n > N_2 \implies \lvert c_n - L \rvert < \varepsilon$$

Let $N = \max(N_1, N_2)$. For all $n > N$:

$$L - \varepsilon < a_n \leq b_n \leq c_n < L + \varepsilon$$

Therefore $\lvert b_n - L \rvert < \varepsilon$, and since $\varepsilon > 0$ was arbitrary, $b_n \to L$.