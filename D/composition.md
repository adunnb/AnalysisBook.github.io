---
layout: definition
title: "Composition of Functions"
chapter: "Set Theory and Functions"
link_terms: ["composition", "identity function"]
---

**Definition:** For [functions](../D/function) $f : A \to B$ and $g : B \to C$, the **composition** $g \circ f : A \to C$ is defined by:

$$(g \circ f)(a) = g(f(a))$$

More generally, it is enough that the domain of $g$ contain the [image](../D/image) $f(A)$. The **identity function** on $A$ is $\mathrm{id}_A : A \to A$, $\mathrm{id}_A(a) = a$.

**Example:** Order matters. If $f(x) = x^2$ and $g(x) = x + 5$, then:

$$(f \circ g)(x) = (x + 5)^2, \qquad (g \circ f)(x) = x^2 + 5$$

**Remark:** Composition is associative, since $(h \circ g) \circ f$ and $h \circ (g \circ f)$ both send $a$ to $h(g(f(a)))$, so parentheses can be omitted. For any $f : A \to B$, we have $f \circ \mathrm{id}_A = f = \mathrm{id}_B \circ f$.
