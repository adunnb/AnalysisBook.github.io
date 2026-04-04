---
layout: proof
title: "Algebra of Limits"
chapter: "Sequences and Series"
---

**Theorem:** Let $(a_n)$ and $(b_n)$ be sequences with $a_n \to L$ and $b_n \to M$. Then:

(i) $a_n + b_n \to L + M$

(ii) $a_n b_n \to LM$

(iii) $ca_n \to cL$ for any constant $c \in \mathbb{R}$

(iv) $\dfrac{a_n}{b_n} \to \dfrac{L}{M}$, provided $M \neq 0$ and $b_n \neq 0$ for all $n$

**Proof of (i):** Let $\varepsilon > 0$. Since $a_n \to L$ and $b_n \to M$, there exist $N_1, N_2 \in \mathbb{N}$ such that:

$$n > N_1 \implies \lvert a_n - L \rvert < \frac{\varepsilon}{2}, \qquad n > N_2 \implies \lvert b_n - M \rvert < \frac{\varepsilon}{2}$$

For all $n > N = \max(N_1, N_2)$, the [triangle inequality](../D/absolute-value) gives:

$$\lvert (a_n + b_n) - (L + M) \rvert \leq \lvert a_n - L \rvert + \lvert b_n - M \rvert < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$

**Proof of (ii):** Let $\varepsilon > 0$. Since $(a_n)$ is convergent it is [bounded](../T/convergent-bounded), so there exists $M_0 > 0$ with $\lvert a_n \rvert \leq M_0$ for all $n$. Choose $N_1, N_2 \in \mathbb{N}$ such that:

$$n > N_1 \implies \lvert a_n - L \rvert < \frac{\varepsilon}{2(|M|+1)}, \qquad n > N_2 \implies \lvert b_n - M \rvert < \frac{\varepsilon}{2M_0}$$

For all $n > N = \max(N_1, N_2)$:

$$\lvert a_n b_n - LM \rvert = \lvert a_n b_n - a_n M + a_n M - LM \rvert$$
$$\leq \lvert a_n \rvert \lvert b_n - M \rvert + \lvert M \rvert \lvert a_n - L \rvert < M_0 \cdot \frac{\varepsilon}{2M_0} + \lvert M \rvert \cdot \frac{\varepsilon}{2(\lvert M \rvert + 1)} < \varepsilon$$

**Proof of (iii):** This follows from (ii) by setting $b_n = c$ for all $n$.

**Proof of (iv):** It suffices to show $\frac{1}{b_n} \to \frac{1}{M}$, since the result then follows from (ii). Since $b_n \to M \neq 0$, there exists $N$ such that $n > N \implies \lvert b_n \rvert > \frac{\lvert M \rvert}{2}$. Then for $n > N$:

$$\left\lvert \frac{1}{b_n} - \frac{1}{M} \right\rvert = \frac{\lvert b_n - M \rvert}{\lvert b_n \rvert \lvert M \rvert} < \frac{2\lvert b_n - M \rvert}{\lvert M \rvert^2} \to 0$$