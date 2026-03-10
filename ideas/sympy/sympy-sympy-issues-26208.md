# issue 2

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/26208
**Scraped:** 2026-03-10T16:58:40.300152

---

## Asymptotic series expansions for Shi & Chi functions

**Labels:** series

Though the limits work for most general points, these limits can also work more simply through gruntz if we have asymptotic series expansions. Currently we have none 
```
>>> Shi(x).series(x, oo)
Traceback (most recent call last):
...................
sympy.core.function.PoleError:
Asymptotic expansion of Shi around [oo] is not implemented.
>>>
>>> Chi(x).series(x, oo)
Traceback (most recent call last):
.................
sympy.core.function.PoleError:
Asymptotic expansion of Chi around [oo] is not implemented.
```

