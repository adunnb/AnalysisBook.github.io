---
layout: proof
title: "Integrability Criterion"
chapter: "Integration"
---

**Theorem:** A bounded function $f : [a, b] \to \mathbb{R}$ is [Riemann integrable](../D/riemann-integral) if and only if for every $\varepsilon > 0$ there exists a [partition](../D/partition) $P$ of $[a, b]$ such that:

$$U(f, P) - L(f, P) < \varepsilon$$

**Remark:** This criterion is also called **Riemann's criterion**. It is the main tool for proving integrability — rather than computing upper and lower integrals directly, it suffices to find a single partition making the difference of upper and lower sums arbitrarily small.

**Proof:**

**($\Rightarrow$)** Suppose $f$ is Riemann integrable, so $U(f) = L(f)$. Let $\varepsilon > 0$. By the definitions of upper and lower integrals as infimum and supremum respectively, there exist partitions $P_1$ and $P_2$ such that:

$$U(f, P_1) < U(f) + \frac{\varepsilon}{2}, \qquad L(f, P_2) > L(f) - \frac{\varepsilon}{2}$$

Let $P = P_1 \cup P_2$ be the common refinement. Since refinements decrease upper sums and increase lower sums:

$$U(f, P) - L(f, P) \leq U(f, P_1) - L(f, P_2) < U(f) + \frac{\varepsilon}{2} - L(f) + \frac{\varepsilon}{2} = \varepsilon$$

**($\Leftarrow$)** Suppose for every $\varepsilon > 0$ there exists a partition $P$ with $U(f,P) - L(f,P) < \varepsilon$. Since $L(f) \leq U(f)$ always, it suffices to show $U(f) \leq L(f)$. For any such $P$:

$$0 \leq U(f) - L(f) \leq U(f, P) - L(f, P) < \varepsilon$$

Since $\varepsilon > 0$ was arbitrary, $U(f) = L(f)$, so $f$ is Riemann integrable.