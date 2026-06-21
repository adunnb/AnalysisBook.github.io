---
layout: proof
title: "Convergence of Taylor Series"
chapter: "Sequences of Functions"
---

**Theorem:** Let $f : A \to \mathbb{R}$ be infinitely differentiable at $c \in A$, and for $x \in A$ let $P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(c)}{k!}(x-c)^k$ be the $n$-th order Taylor polynomial of $f$ centered at $c$, with [Lagrange remainder](../T/taylors-theorem) $R_n(x) = f(x) - P_n(x)$. Then the [Taylor series](../D/taylor-series) of $f$ at $c$ converges to $f(x)$ if and only if:

$$\lim_{n \to \infty} R_n(x) = 0$$

**Remark:** This theorem reduces the question of whether a Taylor series converges to $f$ to a question about the size of the remainder term, which can often be bounded directly using [Taylor's theorem](../T/taylors-theorem). It is exactly this criterion that fails for $f(x) = e^{-1/x^2}$ with $f(0) = 0$: the Maclaurin series converges everywhere to the zero function, but for $x \neq 0$ the remainder does not tend to $0$, so the series fails to converge to $f$.

**Proof:** By definition, $P_n(x)$ is the $n$-th [partial sum](../D/partial-sums) of the Taylor series of $f$ at $c$, so the Taylor series converges to $f(x)$ if and only if $P_n(x) \to f(x)$ as $n \to \infty$. Since:

$$f(x) - P_n(x) = R_n(x)$$

we have $P_n(x) \to f(x)$ if and only if $R_n(x) \to 0$.
