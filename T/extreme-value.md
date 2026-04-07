---
layout: proof
title: "Extreme Value Theorem"
chapter: "Limits and Continuity"
---

**Theorem:** If $f : [a, b] \to \mathbb{R}$ is [continuous](../D/continuity) on a closed bounded interval $[a, b]$, then $f$ attains both a maximum and a minimum value. That is, there exist $c, d \in [a, b]$ such that:

$$f(d) \leq f(x) \leq f(c) \quad \text{for all } x \in [a, b]$$

**Proof:** We show $f$ attains a maximum; the minimum follows analogously.

**Step 1: $f$ is bounded above.** Suppose not. Then for each $n \in \mathbb{N}$ there exists $x_n \in [a,b]$ with $f(x_n) > n$. Since $(x_n) \subseteq [a,b]$ is bounded, by the [Bolzano–Weierstrass theorem](../T/bolzano-weierstrass) there exists a convergent subsequence $x_{n_k} \to c \in [a,b]$. Since $f$ is continuous at $c$:

$$f(x_{n_k}) \to f(c)$$

But $f(x_{n_k}) > n_k \to \infty$, a contradiction. So $f$ is bounded above.

**Step 2: $f$ attains its supremum.** Let $M = \sup\{f(x) : x \in [a,b]\}$, which exists by the [completeness axiom](../T/completeness-axiom). For each $n \in \mathbb{N}$, there exists $x_n \in [a,b]$ with $f(x_n) > M - \frac{1}{n}$. By [Bolzano–Weierstrass](../T/bolzano-weierstrass), some subsequence $x_{n_k} \to c \in [a,b]$. By continuity:

$$f(c) = \lim_{k \to \infty} f(x_{n_k}) = M$$

So $f$ attains its maximum at $c$.