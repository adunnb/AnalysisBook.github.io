---
layout: proof
title: "Common Taylor Series"
chapter: "Sequences of Functions"
---

**Theorem:** The following Maclaurin series hold for all $x \in \mathbb{R}$ unless otherwise stated:

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

$$\sin x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$$

$$\cos x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$$

$$\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n = 1 + x + x^2 + \cdots \quad \text{for } \lvert x \rvert < 1$$

$$\ln(1+x) = \sum_{n=1}^{\infty} \frac{(-1)^{n+1} x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots \quad \text{for } \lvert x \rvert \leq 1,\ x \neq -1$$

**Proof for $e^x$:** Let $f(x) = e^x$. Then $f^{(n)}(x) = e^x$ for all $n$, so $f^{(n)}(0) = 1$. The Lagrange remainder is:

$$R_n(x) = \frac{e^\xi}{(n+1)!} x^{n+1}$$

for some $\xi$ between $0$ and $x$. For any fixed $x$, $e^\xi$ is bounded by $e^{\lvert x \rvert}$, and $\frac{\lvert x \rvert^{n+1}}{(n+1)!} \to 0$ since the exponential series converges. By [convergence of Taylor series](../T/taylor-series-convergence), $e^x = \sum \frac{x^n}{n!}$.

**Proof for $\sin x$:** Let $f(x) = \sin x$. The derivatives cycle: $\sin x, \cos x, -\sin x, -\cos x, \ldots$ with $f^{(2n)}(0) = 0$ and $f^{(2n+1)}(0) = (-1)^n$. The remainder satisfies $\lvert R_n(x) \rvert \leq \frac{\lvert x \rvert^{n+1}}{(n+1)!} \to 0$, so the series converges to $\sin x$.

**Proof for $\cos x$:** Analogous to $\sin x$ with $f^{(2n)}(0) = (-1)^n$ and $f^{(2n+1)}(0) = 0$.

**Proof for $\frac{1}{1-x}$:** This is the [geometric series](../T/geometric-series) with ratio $x$, which converges for $\lvert x \rvert < 1$.

**Proof for $\ln(1+x)$:** Integrate the geometric series $\frac{1}{1+x} = \sum_{n=0}^{\infty} (-x)^n$ term by term using [differentiability of power series](../T/power-series-differentiable) and [FTC II](../T/ftc-2). The convergence at $x = 1$ follows from [Abel's theorem](../T/abel-theorem).