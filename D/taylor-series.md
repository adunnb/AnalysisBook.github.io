---
layout: definition
title: "Taylor Series"
chapter: "Sequences of Functions"
---

**Definition:** Let $f : A \to \mathbb{R}$ be infinitely differentiable at $c \in A$. The **Taylor series** of $f$ centered at $c$ is the [power series](../D/power-series):

$$\sum_{n=0}^{\infty} \frac{f^{(n)}(c)}{n!}(x-c)^n = f(c) + f'(c)(x-c) + \frac{f''(c)}{2!}(x-c)^2 + \cdots$$

When $c = 0$, this is called the **Maclaurin series** of $f$:

$$\sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n$$

**Remark:** The Taylor series of $f$ at $c$ is the unique [power series](../D/power-series) centered at $c$ whose coefficients are determined by the derivatives of $f$ at $c$. However, a function can have a Taylor series that converges everywhere but does not converge to $f$ -- the classic example is $f(x) = e^{-1/x^2}$ with $f(0) = 0$, whose Maclaurin series is identically zero.