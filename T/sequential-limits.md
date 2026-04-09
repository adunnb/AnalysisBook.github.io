---
layout: proof
title: "Sequential Characterization of Functional Limits"
chapter: "Limits and Continuity"
---

**Theorem:** Let $f : A \to \mathbb{R}$ and let $c$ be a [limit point](../D/limit-point) of $A$. Then, for any sequence $(x_n) \subseteq A \text{ with } x_n \neq c \text{ and } x_n \to c$:

$$\lim_{x \to c} f(x) = L \iff f(x_n) \to L$$

**Remark:** This theorem is extremely useful in practice. It allows us to extend all the machinery of [sequence limits](../D/convergence-sequence) to study functional limits, and to prove that limits do not exist by finding two sequences approaching $c$ along which $f$ converges to different values.

**Proof:**

**($\Rightarrow$)** Suppose $\lim_{x \to c} f(x) = L$ and let $(x_n)$ be a sequence in $A$ with $x_n \neq c$ and $x_n \to c$. Let $\varepsilon > 0$. By the [definition of the functional limit](../D/limit-function), there exists $\delta > 0$ such that:

$$0 < \lvert x - c \rvert < \delta \implies \lvert f(x) - L \rvert < \varepsilon$$

Since $x_n \to c$, there exists $N \in \mathbb{N}$ such that $n > N \implies \lvert x_n - c \rvert < \delta$. Since $x_n \neq c$ we have $0 < \lvert x_n - c \rvert < \delta$, so $\lvert f(x_n) - L \rvert < \varepsilon$. Therefore $f(x_n) \to L$.

**($\Leftarrow$)** Suppose the sequential condition holds but $\lim_{x \to c} f(x) \neq L$. Then there exists $\varepsilon_0 > 0$ such that for every $\delta > 0$ there exists $x \in A$ with $0 < \lvert x - c \rvert < \delta$ but $\lvert f(x) - L \rvert \geq \varepsilon_0$.

Taking $\delta = \frac{1}{n}$ for each $n \in \mathbb{N}$, we obtain a sequence $(x_n)$ in $A$ with $x_n \neq c$, $\lvert x_n - c \rvert < \frac{1}{n}$, and $\lvert f(x_n) - L \rvert \geq \varepsilon_0$. Then $x_n \to c$ but $f(x_n) \not\to L$, contradicting the sequential condition.