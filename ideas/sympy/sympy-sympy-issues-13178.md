# #13178

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/13178
**Scraped:** 2026-02-22T23:28:47.570918

---

## Ability to solve modular equations with integer solutions

**Labels:** solvers.solveset

See for instance https://www.johndcook.com/blog/2017/08/22/predicting-a-lcg-output/. It would be cool if you could just write

```py
n = symbols('n', integer=True)
a = 742938285
z = 1898888478
m = 2**31 - 1
x = 20170816
solveset(x – Mod(a**n*z, m), n, S.Integers)
```

and it produced the answer {100}. 

