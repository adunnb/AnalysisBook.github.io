---
layout: definition
title: "Inverse Function"
chapter: "Set Theory and Functions"
link_terms: ["inverse function"]
---

**Definition:** If $f : A \to B$ is a [bijection](../D/bijective), its **inverse function** $f^{-1} : B \to A$ sends each $b \in B$ to its unique [preimage](../D/preimage) under $f$. In terms of [composition](../D/composition) and identity functions, it satisfies:

$$f^{-1} \circ f = \mathrm{id}_A, \qquad f \circ f^{-1} = \mathrm{id}_B$$

**Example:** The inverse of $x \mapsto x^2$ on $[0, \infty)$ is $y \mapsto \sqrt{y}$. The inverse of $\log : (0, \infty) \to \mathbb{R}$ is $\exp : \mathbb{R} \to (0, \infty)$.

**Example:** Let $f : \mathbb{R} \setminus \{1\} \to \mathbb{R} \setminus \{2\}$, $f(x) = \frac{2x}{x - 1}$. Solving $y = \frac{2x}{x-1}$ for $x$ gives $(y - 2)x = y$, so $x = \frac{y}{y - 2}$. This value exists and differs from $1$ for every $y \neq 2$, and direct substitution verifies both identities above. Hence:

$$f^{-1}(y) = \frac{y}{y - 2}$$

**Remark:** The graph of $f^{-1}$ is the graph of $f$ with every [ordered pair](../D/cartesian-product) reversed, which in the plane is its reflection across the line $y = x$. Don't confuse the inverse function $f^{-1}$, which exists only for bijections, with the [preimage](../D/preimage) $f^{-1}(H)$, which exists for every function. A function has an inverse exactly when it is a bijection ([Characterization of bijections by inverses](../T/inverse-characterization)).
