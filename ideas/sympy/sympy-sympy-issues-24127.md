# relevant issue

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/24127
**Scraped:** 2026-02-22T23:28:47.572860

---

## Error on all limits with Piecewise

**Labels:** limits, functions.elementary.piecewise

```
# %% Init
from sympy import *
init_printing()
# %% Diff should be undefined in singularities
x = symbols('x', real=True)
f0 = tanh(x)
f1 = Piecewise((sin(x), x<0), (S(1)/2, True))
print(f1.diff())
print(f1.diff().subs(x,0))    # should return undefined
# %% No limits, even away from the discont.
x0 = 1              # Errors no matter the value of x0
f1.limit(x,x0)       # f0 works
# %%
import sys, sympy; print(sympy.__version__, sys.version)
```
Two issues:
1) Cell 2: While the two one-sided limits at $x=0$ exist, they do not agree as $1 \neq 0$, so $f_1'(x)$ should be left undefined at $x=0$. However, the output is:
`Piecewise((cos(x), x < 0), (0, True))` and `0`

2) Cell 3: Discontinuity is at $x=0$, but no limits can be computed:
	"name": "AttributeError",
	"message": "'ExprCondPair' object has no attribute '_eval_is_meromorphic'",
Even, the simple function `f1 = Piecewise((0, x<0), (1, True))` gives the same error. 

Version of SymPy:
Cell 4 outputs `1.11.1 3.10.6 (main, Aug 10 2022, 11:40:04) [GCC 11.3.0]`

