# issue 2

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/10290
**Scraped:** 2026-02-22T23:28:47.572562

---

## Computing series where the free variable is not just a symbol is broken

**Labels:** series

``` python
In [1]: sin(x).series(x)
Out[1]: x - x**3/6 + x**5/120 + O(x**6)

In [2]: sin(sin(x)).series(sin(x))
Out[2]: sin(x) - sin(x)**3/6 + sin(x)**5/120 + O(x**6) #Correct, but odd notation

In [3]: sin(exp(x)).series(exp(x))
Out[3]: exp(5*x)/120 - exp(3*x)/6 + exp(x) #Wrong, and also missing big O

In [4]: sin(cos(x)).series(cos(x))
TypeError: zip argument #2 must support iteration
```

Arguably series should just complain and quit if it's not given an symbol for the free variable.

This odd behaviour is related to what `Order` does under `subs`:

``` python
In [5]: Order(x).subs(x, exp(x))
Out[5]: 0

In [6]: Order(x).subs(x, cos(x))
TypeError: zip argument #2 must support iteration
```

The error is occurring because `solveset` cannot solve an equation Order gives it in `.eval_subs`, and there is no code handling no solution. 


