---
layout: proof
title: "Abel's Theorem"
chapter: "Sequences of Functions"
---

**Theorem:** Let $f(x) = \sum_{n=0}^{\infty} c_n x^n$ be a [power series](../D/power-series) with [radius of convergence](../D/radius-convergence) $R = 1$. If the series converges at $x = 1$, i.e. $\sum_{n=0}^{\infty} c_n = S$, then:

$$\lim_{x \to 1^-} f(x) = S$$

**Remark:** Abel's theorem says that if a power series converges at an endpoint of its interval of convergence, then the function defined by the series is continuous from the appropriate side at that endpoint. This extends the [continuity of power series](../T/power-series-continuous) result to the boundary of the interval of convergence.

**Proof:** Without loss of generality assume $S = 0$ (replace $c_0$ by $c_0 - S$ if necessary). Let $s_n = c_0 + c_1 + \cdots + c_n$ be the partial sums, so $s_n \to 0$. For $x \in [0, 1)$, write using Abel summation:

$$f(x) = \sum_{n=0}^{\infty} c_n x^n = \sum_{n=0}^{\infty} (s_n - s_{n-1}) x^n$$

where $s_{-1} = 0$. Rearranging:

$$f(x) = (1-x)\sum_{n=0}^{\infty} s_n x^n$$

Let $\varepsilon > 0$. Since $s_n \to 0$, there exists $N$ such that $n > N \implies \lvert s_n \rvert < \varepsilon$. Split the sum:

$$f(x) = (1-x)\sum_{n=0}^{N} s_n x^n + (1-x)\sum_{n=N+1}^{\infty} s_n x^n$$

The first term tends to $0$ as $x \to 1^-$ since it is a polynomial times $(1-x)$. For the second term, since $\lvert s_n \rvert < \varepsilon$ for $n > N$ and $(1-x)\sum_{n=N+1}^{\infty} x^n \leq 1$:

$$\left\lvert (1-x)\sum_{n=N+1}^{\infty} s_n x^n \right\rvert \leq \varepsilon (1-x) \sum_{n=N+1}^{\infty} x^n \leq \varepsilon$$

Therefore $\lvert f(x) \rvert < 2\varepsilon$ for $x$ sufficiently close to $1$, giving $\lim_{x \to 1^-} f(x) = 0 = S$.