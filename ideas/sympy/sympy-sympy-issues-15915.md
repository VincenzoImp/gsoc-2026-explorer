# issue 4

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/15915
**Scraped:** 2026-02-22T23:28:47.572743

---

## Error substituting a function into an Order

**Labels:** core

Order `O` doesn't like having a function substituted into it:
```julia
In [17]: expr = 1 + x + O(x**2)                                                                                                                

In [18]: expr                                                                                                                                  
Out[18]: 
         ⎛ 2⎞
1 + x + O⎝x ⎠

In [19]: expr.subs(x, y)                                                                                                                       
Out[19]: 
         ⎛ 2⎞
1 + y + O⎝y ⎠

In [20]: expr.subs(x, f(y))                                                                                                                    
---------------------------------------------------------------------------
TypeError 
~/current/sympy/sympy/sympy/series/order.py in _eval_subs(self, old, new)
    441                             e2 = sol.args[1]
    442                             sol = set(e1) - set(e2)
--> 443                         res = [dict(zip((d, ), sol))]
    444                         point = d.subs(res[0]).limit(old, self.point[i])
    445                     newvars[i] = var

TypeError: zip argument #2 must support iteration
```

I would have expected the result to be `1 + f(y) + O(f(x)**2)` but that also comes out strangely:
```julia
In [21]: 1 + f(y) + O(f(x)**2)                                                                                                                 
Out[21]: 
 ⎛ 2   ⎞
O⎝f (x)⎠
```

