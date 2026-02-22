# issue 1

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/26207
**Scraped:** 2026-02-22T23:28:47.571779

---

## Asymptotic series expansion for Cosine Integral function

**Labels:** series

I was just testing out the asymptotic series & limits at infinity for some error functions and I found this 
```
>>> Si(x).series(x, oo)
pi/2 - (-6/x**3 + 1/x + O(x**(-7), (x, oo)))*sin(x)/x - (24/x**4 - 2/x**2 + 1 + O(x**(-7), (x, oo)))*cos(x)/x
>>>
>>> Si(x).series(x, -oo)
-24*cos(x)/x**5 + 6*sin(x)/x**4 + 2*cos(x)/x**3 - sin(x)/x**2 - cos(x)/x - pi/2 + O(x**(-6), (x, -oo))
>>>
>>> Ci(x).series(x, oo)
-(-6/x**3 + 1/x + O(x**(-7), (x, oo)))*cos(x)/x + (24/x**4 - 2/x**2 + 1 + O(x**(-7), (x, oo)))*sin(x)/x
>>>
>>> Ci(x).series(x, -oo)
Traceback (most recent call last):
  File "C:\Users\91989\sympy\sympy\sympy\core\expr.py", line 2994, in series
    s = self.subs(x, cdir/x).series(x, n=n, dir='+', cdir=1)
  File "C:\Users\91989\sympy\sympy\sympy\core\expr.py", line 3015, in series
    rv = self.subs(x, xpos).series(xpos, x0, n, dir, logx=logx, cdir=cdir)
  File "C:\Users\91989\sympy\sympy\sympy\core\expr.py", line 3023, in series
    s1 = self._eval_nseries(x, n=n, logx=logx, cdir=cdir)
  File "C:\Users\91989\sympy\sympy\sympy\functions\special\error_functions.py", line 1800, in _eval_nseries
    return super()._eval_nseries(x, n, logx)
  File "C:\Users\91989\sympy\sympy\sympy\core\function.py", line 690, in _eval_nseries
    return self._eval_aseries(n, args0, x, logx)
  File "C:\Users\91989\sympy\sympy\sympy\functions\special\error_functions.py", line 2082, in _eval_aseries
    return super(Ci, self)._eval_aseries(n, args0, x, logx)
  File "C:\Users\91989\sympy\sympy\sympy\core\function.py", line 653, in _eval_aseries
    raise PoleError(filldedent('''
sympy.core.function.PoleError:
Asymptotic expansion of Ci around [-oo] is not implemented.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\91989\sympy\sympy\sympy\core\expr.py", line 2999, in series
    s = self.subs(x, cdir*x).aseries(x, n=n)
  File "C:\Users\91989\sympy\sympy\sympy\core\expr.py", line 3198, in aseries
    return self.subs(x, xpos).aseries(xpos, n, bound, hir).subs(xpos, x)
  File "C:\Users\91989\sympy\sympy\sympy\core\expr.py", line 3216, in aseries
    s = self.subs(x, exp(x)).aseries(x, n, bound, hir).subs(x, log(x))
  File "C:\Users\91989\sympy\sympy\sympy\core\expr.py", line 3238, in aseries
    s = func.series(k, 0, n)
  File "C:\Users\91989\sympy\sympy\sympy\core\expr.py", line 3023, in series
    s1 = self._eval_nseries(x, n=n, logx=logx, cdir=cdir)
  File "C:\Users\91989\sympy\sympy\sympy\functions\special\error_functions.py", line 1800, in _eval_nseries
    return super()._eval_nseries(x, n, logx)
  File "C:\Users\91989\sympy\sympy\sympy\core\function.py", line 690, in _eval_nseries
    return self._eval_aseries(n, args0, x, logx)
  File "C:\Users\91989\sympy\sympy\sympy\functions\special\error_functions.py", line 2082, in _eval_aseries
    return super(Ci, self)._eval_aseries(n, args0, x, logx)
  File "C:\Users\91989\sympy\sympy\sympy\core\function.py", line 653, in _eval_aseries
    raise PoleError(filldedent('''
sympy.core.function.PoleError:
Asymptotic expansion of Ci around [-oo] is not implemented.
```

