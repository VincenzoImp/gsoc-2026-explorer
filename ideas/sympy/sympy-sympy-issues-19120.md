# issue 1

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/19120
**Scraped:** 2026-03-10T16:58:40.300566

---

## ConditionSet not iterable from Order.subs

**Labels:** series

```
from sympy import *
cos(x).series(n=8).subs(x,cos(x).series(n=8))
```

this return type error

![image](https://user-images.githubusercontent.com/30024051/79179887-2ab3a880-7df8-11ea-9430-1fb04b5d4f14.png)


but if we use sin

```
from sympy import *
sin(x).series(n=8).subs(x,sin(x).series(n=8)).expand()
```

![image](https://user-images.githubusercontent.com/30024051/79179860-166fab80-7df8-11ea-8287-08d55d646ff6.png)


