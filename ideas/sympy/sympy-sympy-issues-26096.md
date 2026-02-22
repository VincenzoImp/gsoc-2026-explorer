# issue 4

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/26096
**Scraped:** 2026-02-22T23:28:47.572027

---

## Please implement asymptotic expansion of Gamma...

**Labels:** series

Hello, it would be great if sympy allowed for asymptotic expansion of some combinatorial quantities like binomial coefficients.... at least very approximate, like 2^(leadterm * (1 + o(1))), that would be sufficient for most applications.. (in my case designing algorithms in theoretical computer science)

Currently, I can get many different errors depending on how exactly I formulate the request, but there is no way to get an answer, it seems, although the computation is in fact pretty simple to do by hand (but I would like to estimate a bit more involved expressions, of course, on computer..)

Sorry, I don't know what is inside, but is it hard to just substitute Stirling's expansion whenever factorials or gamma have to be expanded at +inf?

```
>>> sympy.series(sympy.log(sympy.binomial(n, n / 3)), n, oo)
Traceback (most recent call last):
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/functions/elementary/exponential.py", line 989, in _eval_nseries
    a, b = z.leadterm(t, logx=logx, cdir=1)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3538, in leadterm
    l = self.as_leading_term(x, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/cache.py", line 72, in wrapper
    retval = cfunc(*args, **kwargs)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3501, in as_leading_term
    obj = self._eval_as_leading_term(x, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/functions/combinatorial/factorials.py", line 1102, in _eval_as_leading_term
    return self.rewrite(gamma)._eval_as_leading_term(x, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/mul.py", line 2035, in _eval_as_leading_term
    return self.func(*[t.as_leading_term(x, logx=logx, cdir=cdir) for t in self.args])
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/mul.py", line 2035, in <listcomp>
    return self.func(*[t.as_leading_term(x, logx=logx, cdir=cdir) for t in self.args])
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/cache.py", line 72, in wrapper
    retval = cfunc(*args, **kwargs)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3501, in as_leading_term
    obj = self._eval_as_leading_term(x, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/functions/special/gamma_functions.py", line 215, in _eval_as_leading_term
    raise PoleError()
sympy.core.function.PoleError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3005, in series
    s = self.subs(x, cdir/x).series(x, n=n, dir='+', cdir=1)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3026, in series
    rv = self.subs(x, xpos).series(xpos, x0, n, dir, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3034, in series
    s1 = self._eval_nseries(x, n=n, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/functions/elementary/exponential.py", line 991, in _eval_nseries
    s = z._eval_nseries(t, n=n, logx=logx, cdir=1)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/function.py", line 690, in _eval_nseries
    return self._eval_aseries(n, args0, x, logx)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/function.py", line 653, in _eval_aseries
    raise PoleError(filldedent('''
sympy.core.function.PoleError: 
Asymptotic expansion of binomial around [oo, oo] is not implemented.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/series/series.py", line 63, in series
    return expr.series(x, x0, n, dir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3010, in series
    s = self.subs(x, cdir*x).aseries(x, n=n)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3209, in aseries
    return self.subs(x, xpos).aseries(xpos, n, bound, hir).subs(xpos, x)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3215, in aseries
    om, exps = mrv(self, x)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/series/gruntz.py", line 285, in mrv
    s, expr = mrv(e.args[0], x)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/series/gruntz.py", line 311, in mrv
    raise NotImplementedError("MRV set computation for functions in"
NotImplementedError: MRV set computation for functions in several variables not implemented.
```

Or, another attempt, directly via gamma:
```
>>> sympy.series(sympy.log(sympy.gamma(n) / sympy.gamma(1/3 * n) / sympy.gamma(2/3 * n)), n, oo)
Traceback (most recent call last):
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/functions/elementary/exponential.py", line 989, in _eval_nseries
    a, b = z.leadterm(t, logx=logx, cdir=1)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3538, in leadterm
    l = self.as_leading_term(x, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/cache.py", line 72, in wrapper
    retval = cfunc(*args, **kwargs)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3501, in as_leading_term
    obj = self._eval_as_leading_term(x, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/mul.py", line 2035, in _eval_as_leading_term
    return self.func(*[t.as_leading_term(x, logx=logx, cdir=cdir) for t in self.args])
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/mul.py", line 2035, in <listcomp>
    return self.func(*[t.as_leading_term(x, logx=logx, cdir=cdir) for t in self.args])
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/cache.py", line 72, in wrapper
    retval = cfunc(*args, **kwargs)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3501, in as_leading_term
    obj = self._eval_as_leading_term(x, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/functions/special/gamma_functions.py", line 215, in _eval_as_leading_term
    raise PoleError()
sympy.core.function.PoleError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/mul.py", line 1964, in _eval_nseries
    coeff, exp = t.leadterm(x)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3544, in leadterm
    raise ValueError(filldedent("""
ValueError: 
cannot compute leadterm(1/gamma(0.333333333333333/_t), _t). The
coefficient should have been free of _t but got
1/gamma(0.333333333333333/_t)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/power.py", line 1678, in _eval_nseries
    _, m = b.leadterm(x)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3538, in leadterm
    l = self.as_leading_term(x, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/cache.py", line 72, in wrapper
    retval = cfunc(*args, **kwargs)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3501, in as_leading_term
    obj = self._eval_as_leading_term(x, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/functions/special/gamma_functions.py", line 215, in _eval_as_leading_term
    raise PoleError()
sympy.core.function.PoleError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3005, in series
    s = self.subs(x, cdir/x).series(x, n=n, dir='+', cdir=1)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3026, in series
    rv = self.subs(x, xpos).series(xpos, x0, n, dir, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3034, in series
    s1 = self._eval_nseries(x, n=n, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/functions/elementary/exponential.py", line 991, in _eval_nseries
    s = z._eval_nseries(t, n=n, logx=logx, cdir=1)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/mul.py", line 1985, in _eval_nseries
    facs = [t.nseries(x, n=ceiling(n-n0), logx=logx, cdir=cdir) for t in self.args]
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/mul.py", line 1985, in <listcomp>
    facs = [t.nseries(x, n=ceiling(n-n0), logx=logx, cdir=cdir) for t in self.args]
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3407, in nseries
    return self._eval_nseries(x, n=n, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/power.py", line 1680, in _eval_nseries
    b = b._eval_nseries(x, n=max(2, n), logx=logx, cdir=cdir).removeO()
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/functions/special/gamma_functions.py", line 201, in _eval_nseries
    return super()._eval_nseries(x, n, logx)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/function.py", line 690, in _eval_nseries
    return self._eval_aseries(n, args0, x, logx)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/function.py", line 653, in _eval_aseries
    raise PoleError(filldedent('''
sympy.core.function.PoleError: 
Asymptotic expansion of gamma around [oo] is not implemented.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/functions/elementary/exponential.py", line 989, in _eval_nseries
    a, b = z.leadterm(t, logx=logx, cdir=1)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3538, in leadterm
    l = self.as_leading_term(x, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/cache.py", line 72, in wrapper
    retval = cfunc(*args, **kwargs)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3501, in as_leading_term
    obj = self._eval_as_leading_term(x, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/mul.py", line 2035, in _eval_as_leading_term
    return self.func(*[t.as_leading_term(x, logx=logx, cdir=cdir) for t in self.args])
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/mul.py", line 2035, in <listcomp>
    return self.func(*[t.as_leading_term(x, logx=logx, cdir=cdir) for t in self.args])
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/cache.py", line 72, in wrapper
    retval = cfunc(*args, **kwargs)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3501, in as_leading_term
    obj = self._eval_as_leading_term(x, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/functions/special/gamma_functions.py", line 215, in _eval_as_leading_term
    raise PoleError()
sympy.core.function.PoleError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/mul.py", line 1964, in _eval_nseries
    coeff, exp = t.leadterm(x)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3544, in leadterm
    raise ValueError(filldedent("""
ValueError: 
cannot compute leadterm(1/gamma(0.333333333333333/_t), _t). The
coefficient should have been free of _t but got
1/gamma(0.333333333333333/_t)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/power.py", line 1678, in _eval_nseries
    _, m = b.leadterm(x)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3538, in leadterm
    l = self.as_leading_term(x, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/cache.py", line 72, in wrapper
    retval = cfunc(*args, **kwargs)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3501, in as_leading_term
    obj = self._eval_as_leading_term(x, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/functions/special/gamma_functions.py", line 215, in _eval_as_leading_term
    raise PoleError()
sympy.core.function.PoleError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/series/series.py", line 63, in series
    return expr.series(x, x0, n, dir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3010, in series
    s = self.subs(x, cdir*x).aseries(x, n=n)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3209, in aseries
    return self.subs(x, xpos).aseries(xpos, n, bound, hir).subs(xpos, x)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3227, in aseries
    s = self.subs(x, exp(x)).aseries(x, n, bound, hir).subs(x, log(x))
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3249, in aseries
    s = func.series(k, 0, n)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3034, in series
    s1 = self._eval_nseries(x, n=n, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/functions/elementary/exponential.py", line 991, in _eval_nseries
    s = z._eval_nseries(t, n=n, logx=logx, cdir=1)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/mul.py", line 1985, in _eval_nseries
    facs = [t.nseries(x, n=ceiling(n-n0), logx=logx, cdir=cdir) for t in self.args]
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/mul.py", line 1985, in <listcomp>
    facs = [t.nseries(x, n=ceiling(n-n0), logx=logx, cdir=cdir) for t in self.args]
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/expr.py", line 3407, in nseries
    return self._eval_nseries(x, n=n, logx=logx, cdir=cdir)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/power.py", line 1680, in _eval_nseries
    b = b._eval_nseries(x, n=max(2, n), logx=logx, cdir=cdir).removeO()
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/functions/special/gamma_functions.py", line 201, in _eval_nseries
    return super()._eval_nseries(x, n, logx)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/function.py", line 690, in _eval_nseries
    return self._eval_aseries(n, args0, x, logx)
  File "/home/elexunix/.local/lib/python3.10/site-packages/sympy/core/function.py", line 653, in _eval_aseries
    raise PoleError(filldedent('''
sympy.core.function.PoleError: 
Asymptotic expansion of gamma around [oo] is not implemented.
```

