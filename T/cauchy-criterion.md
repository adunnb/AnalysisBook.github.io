---
layout: proof
title: "Cauchy Criterion for Convergence"
chapter: "Sequences and Series"
---

**Theorem:** A sequence $(a_n)$ of real numbers converges if and only if it is a [Cauchy sequence](../D/cauchy-sequence).

**Proof:**

**($\Rightarrow$) Convergent implies Cauchy.** Suppose $a_n \to L$. Let $\varepsilon > 0$. There exists $N \in \mathbb{N}$ such that:

$$n > N \implies \lvert a_n - L \rvert < \frac{\varepsilon}{2}$$

For all $m, n > N$, the [triangle inequality](../D/absolute-value) gives:

$$\lvert a_m - a_n \rvert = \lvert a_m - L + L - a_n \rvert \leq \lvert a_m - L \rvert + \lvert a_n - L \rvert < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$

So $(a_n)$ is Cauchy.

**($\Leftarrow$) Cauchy implies convergent.** Suppose $(a_n)$ is Cauchy. We proceed in two steps.

**Step 1: $(a_n)$ is bounded.** Taking $\varepsilon = 1$, there exists $N$ such that $m, n > N \implies \lvert a_m - a_n \rvert < 1$. In particular $\lvert a_n - a_{N+1} \rvert < 1$ for all $n > N$, so:

$$\lvert a_n \rvert \leq \lvert a_{N+1} \rvert + 1 \quad \text{for all } n > N$$

Setting $M = \max(\lvert a_1 \rvert, \ldots, \lvert a_N \rvert, \lvert a_{N+1} \rvert + 1)$ gives $\lvert a_n \rvert \leq M$ for all $n$.

**Step 2: $(a_n)$ converges.** Since $(a_n)$ is bounded, by the [Bolzano–Weierstrass theorem](../T/bolzano-weierstrass) it has a convergent subsequence $(a_{n_k}) \to L$. We claim $a_n \to L$.

Let $\varepsilon > 0$. Since $(a_n)$ is Cauchy, there exists $N_1$ such that:

$$m, n > N_1 \implies \lvert a_m - a_n \rvert < \frac{\varepsilon}{2}$$

Since $a_{n_k} \to L$, there exists $K$ such that:

$$k > K \implies \lvert a_{n_k} - L \rvert < \frac{\varepsilon}{2}$$

Choose $k > K$ with $n_k > N_1$. Then for all $n > N_1$:

$$\lvert a_n - L \rvert \leq \lvert a_n - a_{n_k} \rvert + \lvert a_{n_k} - L \rvert < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$

Therefore $a_n \to L$.