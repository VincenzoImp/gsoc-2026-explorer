# issue 3

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/26210
**Scraped:** 2026-02-22T23:28:47.571963

---

## Asymptotic series expansions for modified bessel functions

**Labels:** series

The TODO from bessel.py says 
```
# TODO
# o Scorer functions G1 and G2
# o Asymptotic expansions
#   These are possible, e.g. for fixed order, but since the bessel type
#   functions are oscillatory they are not actually tractable at
#   infinity, so this is not particularly useful right now.
```

So most bessel type functions like Hankel, Kelvin or even Spherical Bessel functions would fall under this category but modified bessel functions don't.
**Besseli** grows exponentially whereas **Besselk** exponentially decays so we can have aseries implementations for these and also that would be in use for calculating limits through gruntz.

