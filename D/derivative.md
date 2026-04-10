---
layout: definition
title: "The Derivative"
chapter: "Differentiation"
---

**Definition:** Let $f : A \to \mathbb{R}$ and let $c \in A$ be a [limit point](../D/limit-point) of $A$. The **derivative** of $f$ at $c$ is defined as:

$$f'(c) = \lim_{x \to c} \frac{f(x) - f(c)}{x - c}$$

provided this limit exists. Equivalently, using the substitution $h = x - c$:

$$f'(c) = \lim_{h \to 0} \frac{f(c + h) - f(c)}{h}$$

If $f'(c)$ exists, we say $f$ is **differentiable at $c$**. If $f$ is differentiable at every point of $A$, we say $f$ is **differentiable on $A$**.

**Remark:** The derivative measures the instantaneous rate of change of $f$ at $c$, and geometrically represents the slope of the tangent line to the graph of $f$ at the point $(c, f(c))$.