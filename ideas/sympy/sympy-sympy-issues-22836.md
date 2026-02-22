# issue 1

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/22836
**Scraped:** 2026-02-22T23:28:47.572141

---

## Series: Possible improvements for Order of expressions involving factorials

**Labels:** series

Being a contributor to the `series` module I have my fair share of idea of what sympy can achieve currently and what are it's limitations. Hence I make this issue  thinking what a user would expect out of the following expressions shown below 

Following basic pattern of growth of functions which is `const < log(x) < x**n < 2**x or exp(x) < factorial(x) < x**x` we have 
**On Master**

```
>>> O(2**x + factorial(x), (x, oo))
O(exp(x*log(2)) + factorial(x), (x, oo))

>>> O(2**x + factorial(x) + x**x, (x, oo))
O(exp(x*log(x)) + factorial(x), (x, oo))

>>> O(x + factorial(x), (x, oo))
O(x*(1 + factorial(x)/x), (x, oo))

```

**Expected Results:** I also ended up checking the results on other CAS and If i remember the results worked properly on `diofant` 
```
>>> O(2**x + factorial(x), (x, oo)) 
O(factorial(x), (x, oo))

>>> O(2**x + factorial(x) + x**x, (x, oo))
O((1/x)**(-x), (x, oo))

>>> O(x + factorial(x), (x, oo))
O( factorial(x) , (x, oo))

```



