# issue 3

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/7872
**Scraped:** 2026-03-10T16:58:40.300717

---

## Substitution in Order fails

**Labels:** series

`O(x**3).subs(x, exp(-x**2))` should be `O(exp(-3*x**2), (x, oo))`
but gives an error

Related to #7529 


