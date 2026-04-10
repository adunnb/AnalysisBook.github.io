---
layout: proof
title: "Differentiability Implies Continuity"
chapter: "Differentiation"
---

**Theorem:** If $f : A \to \mathbb{R}$ is [differentiable](../D/derivative) at $c \in A$, then $f$ is [continuous](../D/continuity) at $c$.

**Remark:** The converse is false. The function $f(x) = \lvert x \rvert$ is continuous at $0$ but not differentiable there, since:

$$\lim_{h \to 0^+} \frac{\lvert h \rvert}{h} = 1 \neq -1 = \lim_{h \to 0^-} \frac{\lvert h \rvert}{h}$$

**Proof:** Since $f$ is differentiable at $c$, $f'(c)$ exists. We write:

$$f(x) - f(c) = \frac{f(x) - f(c)}{x - c} \cdot (x - c)$$

for $x \neq c$. Taking the limit as $x \to c$ and using the [algebraic limit theorem for functions](../T/function-algebra):

$$\lim_{x \to c} (f(x) - f(c)) = \lim_{x \to c} \frac{f(x) - f(c)}{x - c} \cdot \lim_{x \to c} (x - c) = f'(c) \cdot 0 = 0$$

Therefore $\lim_{x \to c} f(x) = f(c)$, so $f$ is continuous at $c$.