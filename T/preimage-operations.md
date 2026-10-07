---
layout: proof
title: "Preimages of Unions and Intersections"
chapter: "Sets and Functions"
link_terms: ["preimages of unions and intersections"]
---

**Theorem:** Let $f : X \to Y$ be a [function](../D/function) and $H, K \subseteq Y$. Then for [preimages](../D/preimage):

1. $f^{-1}(H \cup K) = f^{-1}(H) \cup f^{-1}(K)$
2. $f^{-1}(H \cap K) = f^{-1}(H) \cap f^{-1}(K)$
3. $f^{-1}(Y \setminus H) = X \setminus f^{-1}(H)$

More generally, for any [indexed family](../D/indexed-family) $\{H_\alpha\}$ of [subsets](../D/subset) of $Y$, $f^{-1}\left(\bigcup_\alpha H_\alpha\right) = \bigcup_\alpha f^{-1}(H_\alpha)$ and $f^{-1}\left(\bigcap_\alpha H_\alpha\right) = \bigcap_\alpha f^{-1}(H_\alpha)$.

**Remark:** No hypothesis such as injectivity is needed here, unlike for [images](../T/image-operations). This is why preimages, not [images](../D/image), appear in the [characterization of continuity via open sets](../T/open-sets-continuity).

**Proof:** Each identity follows by testing where $f(x)$ lies, using the definitions of [union and intersection](../D/union-intersection) and [set difference](../D/set-difference). For $x \in X$:

$$x \in f^{-1}(H \cup K) \iff f(x) \in H \text{ or } f(x) \in K \iff x \in f^{-1}(H) \cup f^{-1}(K)$$

$$x \in f^{-1}(H \cap K) \iff f(x) \in H \text{ and } f(x) \in K \iff x \in f^{-1}(H) \cap f^{-1}(K)$$

$$x \in f^{-1}(Y \setminus H) \iff f(x) \notin H \iff x \in X \setminus f^{-1}(H)$$

The indexed versions are identical, with "or" replaced by "for some $\alpha$" and "and" replaced by "for every $\alpha$."
