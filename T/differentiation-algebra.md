---
layout: proof
title: "Algebra of Differentiation"
chapter: "Differentiation"
---

**Theorem:** Let $f, g : A \to \mathbb{R}$ be [differentiable](../D/derivative) at $c \in A$. Then:

(i) $(f + g)'(c) = f'(c) + g'(c)$

(ii) $(fg)'(c) = f'(c)g(c) + f(c)g'(c)$ (the **product rule**)

(iii) $(cf)'(c) = cf'(c)$ for any constant $c \in \mathbb{R}$

(iv) $\left(\dfrac{f}{g}\right)'(c) = \dfrac{f'(c)g(c) - f(c)g'(c)}{g(c)^2}$ (the **quotient rule**), provided $g(c) \neq 0$

**Proof of (i):** By the [definition of the derivative](../D/derivative) and the [algebraic limit theorem for functions](../T/function-algebra):

$$\lim_{x \to c} \frac{(f+g)(x) - (f+g)(c)}{x - c} = \lim_{x \to c} \frac{f(x) - f(c)}{x-c} + \lim_{x \to c} \frac{g(x) - g(c)}{x - c} = f'(c) + g'(c)$$

**Proof of (ii):** Write:

$$\frac{f(x)g(x) - f(c)g(c)}{x - c} = \frac{f(x)g(x) - f(x)g(c) + f(x)g(c) - f(c)g(c)}{x - c}$$

$$= f(x) \cdot \frac{g(x) - g(c)}{x - c} + g(c) \cdot \frac{f(x) - f(c)}{x - c}$$

Taking the limit as $x \to c$, and using the fact that $f$ is [continuous](../D/continuity) at $c$ by [differentiability implies continuity](../T/diff-implies-cont), so $f(x) \to f(c)$:

$$(fg)'(c) = f(c)g'(c) + g(c)f'(c)$$

**Proof of (iii):** This follows from (ii) by setting $g(x) = c$ for all $x$, giving $g'(c) = 0$.

**Proof of (iv):** It suffices to show $\left(\frac{1}{g}\right)'(c) = -\frac{g'(c)}{g(c)^2}$, since the result then follows from (ii). Since $g(c) \neq 0$ and $g$ is continuous at $c$, there exists a neighborhood of $c$ on which $g$ is nonzero. Then:

$$\lim_{x \to c} \frac{\frac{1}{g(x)} - \frac{1}{g(c)}}{x - c} = \lim_{x \to c} \frac{g(c) - g(x)}{g(x)g(c)(x-c)} = \frac{-g'(c)}{g(c)^2}$$