# GSoC 2016 Project: Shekhar Rajak

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/wiki/GSoC-2016-Shekhar-Prasad-Rajak-Application:-Solvers:-Completing-Solveset
**Scraped:** 2026-02-22T23:28:47.570810

---

**[Note]** : [Updated docs](https://drive.google.com/file/d/0B_GhLAhyhSVdaFlobDVCajhMUU0/view?usp=sharing) 

# About Me

## Basic Information
**Name**: Shekhar Prasad Rajak

**Email**: shekharstudy@ymail.com, shekharrajak@live.com, rshekhar@student.nitw.ac.in

**University**: [National Institute of Technology, Waranagal](http://nitw.ac.in/)

**Github/IRC**: [Shekharrajak](https://github.com/shekharrajak)

**Website**: [http://s-hacker.info/](http://s-hacker.info/)

**Timezone** :  IST (UTC +5:30)

## Personal Background

I am a 3rd year undergraduate pursuing Bachelor of Technology in **Computer Science and Engineering** at National Institute of Technology, Warangal, India. I love Mathematics, I like the logic in it, and that if you understood what you were doing you never had to remember anything you could always work things out just using your brain.

## Programming Details

I work on **Kali GNU/Linux 2.0** Operating system with vim as my primary text editor, when I code and sublime text editor otherwise. I am very much familiar with git and github. I have good knowledge on Python, C++, C, Java and have good familiarity with web technologies. I am very much interested in programming and contributing to Open Source community.

--------------------------

# Contributions to SymPy

When I was getting difficulties in solving the equations using Python code,I came to know about `SymPy` through Amit's blog and joined `SymPy` gitter chat room in August 2015. I learnt most of the things in gitter chat room. Slowly I understood the `SymPy` modules and codes.

* **(Closed)** [PR #10215](https://github.com/sympy/sympy/pull/10215) : Added some Usage/examples for `srepr` and showed how `repr` different from `srepr` printing.

* **(Merged)** [PR #10311](https://github.com/sympy/sympy/pull/10311) : Added more projects using `Sympy` in docs.

* **(Unmerged)** [PR #10312](https://github.com/sympy/sympy/pull/10312) : [PR #10215](https://github.com/sympy/sympy/pull/10215) extended and added more usage/examples for `srepr`. 

* **(Unmerged)** [PR #10314](https://github.com/sympy/sympy/pull/10314) : Dot printing examples and usage.

* **(Unmerged)** [PR #10319](https://github.com/sympy/sympy/pull/10319) : Addition of namespaces,namespaces_default,translation for `scipy` in `lambdify.py`

* **(Unmerged)** [PR #10330](https://github.com/sympy/sympy/pull/10330) : removal of `guide.rst`

* **(Merged)** [PR #10333](https://github.com/sympy/sympy/pull/10333) : better comment at `sympy/interactive/tests/test_print_builtin_option()`

* **(Unmerged)** [PR #10370](https://github.com/sympy/sympy/pull/10370) : `math.fabs()` converts its argument to float if it can (if it can't, it throws an exception). It then takes the absolute value, and returns the result as a float.
Fixes [#9474](https://github.com/sympy/sympy/issues/9474)

* **(Unmerged)** [PR #10385](https://github.com/sympy/sympy/pull/10385) : `Sympy` treated symbols having `zero = True` assumption as non-negative & non-positive & real.But `Sympy` don't know; that is `0`.It was not defined anywhere in` Sympy`. Previously line `x = Symbol('x' ,zero=True) `, `x` was treated as symbol only, during execution and didn't took its value. tried to fix [#8167](https://github.com/sympy/sympy/issues/8167)

* **(Closed)** [PR #10407](https://github.com/sympy/sympy/pull/10407) : In `NumPy` `amin` is defined as 
`numpy.amin(a, axis=None, out=None, keepdims=False)`
So if we use `Min` and `Numpy` is installed in the system. Then
`SymPy` use `NumPy` for `lambdify` method.
So when we pass 
`l(1, 2, 3)`
Then it takes` a =1 ,axis=2,out=3`
where a is list of numbers for which we want minimum.
`Sympy` mapping with `NumPy` `amin` is not correct.

* **(Unmerged)** [PR #10444](https://github.com/sympy/sympy/pull/10444) : Integration of summation type expressions.
Fixes [#7827](https://github.com/sympy/sympy/issues/7827)

* **(Unmerged)** [PR #10460](https://github.com/sympy/sympy/pull/10460) : `solveset` is now able to solve XFAIL test_issue_failing_pow. `assert solveset(x**(S(3)/2) + 4, x, S.Reals) == S.EmptySet`

* **(Closed)** [PR #10482](https://github.com/sympy/sympy/pull/10482) : This is able to give solutions in reduced and known easy form in many cases. 
Fixes [#9824](https://github.com/sympy/sympy/issues/9824) [#10426](https://github.com/sympy/sympy/issues/10426)

* **(Unmerged)** [PR #10494](https://github.com/sympy/sympy/pull/10494): Few lines added in docs for `singleton`, `S`

* **(Unmerged)** [PR #10502](https://github.com/sympy/sympy/pull/10502): Needed a  [list](https://github.com/sympy/sympy/pull/10502/files#diff-e2a46e260ac6a40415353a416f21fd4fR1349) which stores about if particular `cond` solution is added or not.Otherwise it may not add result , like previously if `cond` solution is not added but still [if condition](https://github.com/sympy/sympy/pull/10502/files#diff-e2a46e260ac6a40415353a416f21fd4fR1368) true(for this particular issue's testcase) and then it will mark `matches_other_piece = True` so this solution couldn't be add into [result](https://github.com/sympy/sympy/pull/10502/files#diff-e2a46e260ac6a40415353a416f21fd4fR1377) 
 Fixes [#10122](https://github.com/sympy/sympy/issues/10122)

* **(Unmerged)** [PR #10542](https://github.com/sympy/sympy/pull/10542): Need to pass if integral have symbolic upper and lower bound.
Fixes : [#10434](https://github.com/sympy/sympy/issues/10434)

* **(Unmerged)** [PR #10547](https://github.com/sympy/sympy/pull/10547): Problem was `solveset` was assuming that condition symbol is same as symbol for which it is finding solution. so there was problem when condition doesn't contains the solution symbol.
Now is storing the symbols of condition and defining the interval accordingly for all the symbols.
Fixes : [#10534](https://github.com/sympy/sympy/issues/10534)

* **(Unmerged)** [PR #10550](https://github.com/sympy/sympy/pull/10550): solveset_real need to check symbol in piecewise-condition.Expression with multiple abs ,having Piecewise solution as 0.
Fixes :  [#10122](https://github.com/sympy/sympy/issues/10122) and [#10534](https://github.com/sympy/sympy/issues/10534)

* **(Closed)** [PR #10552](https://github.com/sympy/sympy/pull/10552): `solveset` hyperbolic Functions.
```
# complex solution
>>> solveset(sinh(x))
{n⋅ⅈ⋅π | n ∊ ℤ}
# Real solution
>>> solveset(sinh(x), x, S.Reals)
{0}

```
Fixes [#9531](https://github.com/sympy/sympy/issues/9531) , [#9824](https://github.com/sympy/sympy/issues/9824) , [#10426](https://github.com/sympy/sympy/issues/10426) [#7914](https://github.com/sympy/sympy/issues/7914) and [#9606](https://github.com/sympy/sympy/issues/9606)

* **(Unmerged)** [PR #10575](https://github.com/sympy/sympy/pull/10575): linsolve now able to solve unsimplified equations having const variable.
Fixes :  [#10568](https://github.com/sympy/sympy/issues/10568) One testcase 

* **(Unmerged)** [PR #10579](https://github.com/sympy/sympy/pull/10579): modified domain range if denominator is zero.
Fixes : Fixes [#8715](https://github.com/sympy/sympy/issues/8715)

* **(Merged)** [PR #10622](https://github.com/sympy/sympy/pull/10622): Decompogen checking whether function contains `symbol` or not.

* **(Unmerged)** [PR #10649](https://github.com/sympy/sympy/pull/10649): replacing solver in some module.

* **(Unmerged)** [PR #10689](https://github.com/sympy/sympy/pull/10689): Real solution for some `const**(symbol)` type equation.
Fixes Real solution for [#10688](https://github.com/sympy/sympy/issues/10688) 

* **(Unmerged)** [PR #10713](https://github.com/sympy/sympy/pull/10713): proposing a method to get general form for list of args.

* **(Unmerged)** [PR #10733](https://github.com/sympy/sympy/pull/10733): Rewriting #10552 and #10482 with extensions.
 Fixes [#10671](https://github.com/sympy/sympy/issues/10671) [#7914](https://github.com/sympy/sympy/issues/7914) [#9531](https://github.com/sympy/sympy/issues/9531) [#9606](https://github.com/sympy/sympy/issues/9606) [#9824](https://github.com/sympy/sympy/issues/9824) [#10426](https://github.com/sympy/sympy/issues/10426) [#10217](https://github.com/sympy/sympy/issues/10217) and most of the XFAIL present in test_solveset.

* **(Unmerged)** [PR #10764](https://github.com/sympy/sympy/pull/10764): TODO part of #10733
 Fixes XFAIL test-cases and [#7914](https://github.com/sympy/sympy/issues/7914) 

* **(Unmerged)** [PR #10898](https://github.com/sympy/sympy/pull/10898):  Implementing the logic of [PR #10713](https://github.com/sympy/sympy/pull/10713 in solve_trig method in solveset.
This PR is able to give simplified solution for trigonometric equation.
Example : 
```
>>> print solveset(cos(x) + cos(3*x) + cos(5*x),x,S.Reals)
ImageSet(Lambda(_n, _n*pi/6), Integers())
```

---------------------------
### Bugs/issues reported:

* [Issue #10033](https://github.com/sympy/sympy/issues/10033) : Wrong answer by Inequality solver.

* [Issue #10313](https://github.com/sympy/sympy/issues/10313) :Need good description about Dot printing.

* [Issue #10453](https://github.com/sympy/sympy/issues/10453) : Integrate return wrong answer (inverse trigonometric functions).

* [Issue #10568](https://github.com/sympy/sympy/issues/10568) : `linsolve` Returns `EmptySet()` if equation is not simplified.

* [Issue #10688](https://github.com/sympy/sympy/issues/10688) : Not able to solve some `const**(symbol)` type equation.

* [Issue #10864](https://github.com/sympy/sympy/issues/10864) : `solveset(x**(y*z) - x,x,S.Reals)` returns `ConditionSet` .

--------------------------

# The Project

## Brief Overview

Harsh Gupta (GSoC'14)[1] and Amit Kumar (GSoC'15)[2] have implemented most of the things in `Solveset`.I want to continue and make it fully functional. Basically I want to close [#10006](https://github.com/sympy/sympy/issues/10006) .

My main intention is to implement : 

1. Non-linear multivariate system.

2. Equations solvable by `LambertW` (Transcendental equation solver).

3. nested (trig) expression e.g. issue [#10217](https://github.com/sympy/sympy/issues/10217) .
(I tried this here : [#10764](https://github.com/sympy/sympy/pull/10764) )

4. Equation having Trigonometric Functions using Fu module.

5. Simplified general solution from `_invert` method for trigonometric expressions.

6. Integer solution from `solveset` using `diophantine.py`.

7. Fixing XFAIL test-cases, General solution from inverse trigonometric equation, improvement in inequality solver.

# The Plan

#### 1. Trigonometric Equation Solver : 

Right now `solveset` can't handle this : `solveset(sin(2*x) - cos(2*x) -1,x)`, I tried to solve some XFAIL test-cases in this [PR #10733](https://github.com/sympy/sympy/issues/10733)  so this returns : 

```
>>> solveset(sin(2*x) - cos(2*x) -1, x, S.Reals)
⎧      π        ⎫   ⎧      π        ⎫
⎨n⋅π - ─ | n ∊ ℤ⎬ ∪ ⎨n⋅π + ─ | n ∊ ℤ⎬
⎩      2        ⎭   ⎩      4        ⎭
```
But still it can't handle `solveset(sin(x)**3 + cos(3*x) ,x,S.Reals)`. To solve this problem I came across an idea (during discussion in [google group](https://groups.google.com/forum/#!topic/sympy/XhgBx2bVFaA) ) that we can solve the trigonometric equation g = 0 where g is a trigonometric polynomial. We can convert that into a polynomial system by expanding the sines and cosines in it, replacing `sin(x)` and `cos(x)` by two new variables `s` and `c`.
before that need to check arguments are same or not.It should not be like `sin(x)` and `cos(x**2)`.
So now we have two variables and 1 equation another equation we know is :`s2 + c2 − 1 = 0`.Means `sin(x)**2 + cos(x)**2 =1`.
For `tan`,`sec` ; `cot`,`cosec` we convert all the trigonometric functions into `sin` and `cos` ,and solve them for all cases.Then solve the system of equation will give solution for `s` and `c`. 
Now replacing `s -> sin` and `c-> cos` and then `Solveset` can easily solve Eq(sin(x),<constant>) types of equations.
For example if we have equations like : 
`sin(x)**3 + cos(3*x) = 0`
then by `expand(trig = true)` we can get :
`s**3 + 4*(c**3) - 3*c =0  #(cos(3*x) expand)`
Similar things can be applied for hyperbolic functions.Using `fu` module, `rewrite` and `trigsimp` we can simplify the equations.

Another case is when equation have nested Trigonometric functions. something like [#10217](https://github.com/sympy/sympy/issues/10217)
One example is `solveset(sin(3*x)-1,x, S.Reals)` from the master branch `NotImplementedError:`
I fix these types of issues here : [#10764](https://github.com/sympy/sympy/pull/10764)  and [#10733](https://github.com/sympy/sympy/pull/10733)

There are many more [trigonometric identities](https://en.wikipedia.org/wiki/List_of_trigonometric_identities)like

       >>> product(sin(k*pi/n), (k,1,n-1))
       n - 1           
       ┬──┬         
       │  │    ⎛ π⋅k ⎞
       │  │ sin⎜─── ⎟
       │  │    ⎝  n ⎠
       │  │         
       k = 1  
    
       # answer is n/(2**(n-1))
       >>> asin(x) + acos(x)
       acos(x) + asin(x)   # ans is pi/2

And other similar expressions, don't give correct answer.

Also need to improve `rewrite` and `trigsimp` (we must use fu module) , because in many cases it can’t return answer in desired form, for example :

```
>>> sec(x).rewrite(sin)
sec(x)

# expected :  1/sqrt(1-sin(x)**2)
```

#### 2. Simplified general form for trigonometric solution: 

Right now `SymPy` returns  unsimplified general form. If you try this 
`solveset(cos(x) + cos(3*x) + cos(5*x),x)`  then you will get 

`ImageSet(Lambda(_n, 2*_n*pi + pi/2), Integers()) U ImageSet(Lambda(_n, 2*_n*pi - pi/2), Integers()) U    ImageSet(Lambda(_n, 2*_n*pi - 2*pi/3), Integers()) U ImageSet(Lambda(_n, 2*_n*pi + 2*pi/3), Integers()) U    ImageSet(Lambda(_n, 2*_n*pi - pi/3), Integers()) U ImageSet(Lambda(_n, 2*_n*pi + pi/3), Integers()) U ImageSet(Lambda(_n, 2*_n*pi - 5*pi/6), Integers()) U ImageSet(Lambda(_n, 2*_n*pi + 5*pi/6), Integers()) U ImageSet(Lambda(_n, 2*_n*pi - pi/6), Integers()) U ImageSet(Lambda(_n, 2*_n*pi + pi/6), Integers())`

which can be simplified as `(2*n +1)*pi/6`, `(2*n -1)*pi/6` or just `(n*pi/6`. Similarly many other solutions can be simplified.
I found a solution for this after some discussion in Quora, thanks to active Mathematicians in Quora: 

If we have terms like  `pi/6`, `pi/2`, `5*pi/6`, `7*pi/6`, `3*pi/2`.

one way of approaching a sequence like this is :

* Take differences until the differences are all equal (Means difference between 2nd and 1st term, 3rd and 2nd term,  4th and 3rd term and so on). In this case, the first differences are all pi/3. This indicates that you can fit a linear function in  n. If it had been necessary to calculate the second differences then one would have had to fit a quadratic function in  n. (if need third time then general expression will be of 3rd order and so on).  Very often one can calculate all possible differences without reaching equal differences. Then it's necessary to try something else.

* Since a linear function will work fit  `a*n+b`, where  `a`  and  `b`  are arbitrary constants. To do this, set:`pi/6=a+b` (using the first term) and `pi/2=2*a+b`  (using the second term), then solve for  `a`  and  `b` . Now you have a function that should represent all of the terms.

So actually we need a method that can make general from from the given terms.
Some parts of above steps,I tried to implement here : [#10713](https://github.com/sympy/sympy/pull/10713). But this PR was not coded for trigonometric equation solver. I tried to implement this logic in `solve_trig` method in PR [#10898](https://github.com/sympy/sympy/pull/10898)


Right now from current master branch `SymPy` 

               >>> solveset(sin(x), x)
               {2⋅n⋅π | n ∊ ℤ} ∪ {2⋅n⋅π + π | n ∊ ℤ}


but this should be `imageset(Lambda(n, n*pi), S.Integers)`

I opened a PR [#10552](https://github.com/sympy/sympy/pull/10552)   which gives simplified answer for these simple equations.
It passes [testcase](https://github.com/sympy/sympy/pull/10552/files#diff-85baa04bbf4e1dfd9128782738e45424R736) .If we add above steps then it can returns simplified solution for all.
I have rewrite this PR in a better way here :  [PR #10733](https://github.com/sympy/sympy/pull/10733)
So both PR [#10733](https://github.com/sympy/sympy/pull/10733) and [#10898](https://github.com/sympy/sympy/pull/10898) may help for simplified solution.


#### 3. Non linear Multivariate System of Equations & Multivariate, Transcendental Equations:

##### I simple non linear system 

I found that one of the good way may be substitution method (for [simple cases](http://www.purplemath.com/modules/syseqgen5.htm) ) and Using the Quadratic Formula ( some [complicated cases](http://www.purplemath.com/modules/syseqgen6.htm) ). `solver` use these methods for most of the cases.

##### II Multivariate System of Equations

`solve_poly_system` method is used to solve multivariate system of equations, which is returning solution with accuracy. There is only one issue is opened right now  [#9673](https://github.com/sympy/sympy/issues/9673) . So to implement this in `solveset` we need a proper method that can handle multivariate system of equations using `polysys.py` where polynomial system of equations is handled in old `solver`.

I found another good way to solve these types of equations in this link (page 9 example 2.2)
http://people.math.gatech.edu/~aleykin3/math4803spr13/BOOK/chapter1.pdf
So here we need to construct a `Res(f1,f2 )` matrix. I hope this method will work for most of the equation which is similar to this.
If there is any problem in solving any polynomial multivariate equation system then this method may help.

##### III Transcendental Equation and Multivariate Equation

       >>> a =symbols('a')
       >>> solve(x**(2*a) + 2*(x**a) +1,x)
       ⎡a ____⎤
       ⎣╲╱ -1 ⎦
      >>> solveset(x**(2*a) + 2*(x**a) +1,x)
      ConditionSet(x, Eq(x**(2*a) + 2*x**a + 1, 0), Complexes((-oo, oo) x (-oo, oo), False))
      >>> solveset(log(x) + 2*x, x)
      {x | x ∊ ℂ ∧ 2⋅x + log(x) = 0}
      >>> solve(log(x) + 2*x, x)
      [LambertW(2)/2]


The first one can be solved by decomposition method  y = x**a. We can use decompogen method implemented last year [#9831](https://github.com/sympy/sympy/pull/9831) ; to solve these types of equations.
For the second one I think there is just a bunch of `lambertW` code in solve that needs to be translated toSolveset.

Some more examples are : 

       >>> print solveset(5**(x**2) - 5**(6-x),x, S.Reals)
       ConditionSet(x, Eq(5**(x**2) - 5**(-x + 6), 0), (-oo, oo)
       >>> solveset(x+log(x)-3,x)
       {x | x ∊ ℂ ∧ x + log(x) - 3 = 0}

`Solver` uses `_tsolve` and `bivariate.py`  to handle transcendental equation. 
`_tsolve` does a very good job in solving a large space of transcendental equations. After the discussion I found that the problem lies in the fact that it's very messy and not very extensible. It is difficult to add solving of more class of transcendental equations, so it's very
important to write a more modular and extensible transcendental equation
solver. `_tsolve` also uses `bivariate.py` for most of the processing, though
you can note that there aren't many direct calls to `solve` in the `bivariate.py`
except one or two, So it would be great if we could directly call `bivariate.py` methods for
writing transcendental equation solver in `solveset`.
If we fix above issues then we can solve equations like
 `(x+log(x))**2 - 5*(x+log(x)) + 6` using Factorization/Decomposition method.


#### 4.  Integer solution of a linear equation having two variables

From the master branch : 

      >>> print solveset(172*x + 20*y -1000,x, S.Integers)
      Intersection(Integers(), {-5*y/43 + 250/43})
      >>> print solve(172*x + 20*y -1000)
      [{x: -5*y/43 + 250/43}]

`solve` returns correct answer,as it is build for getting this answer. But if we want to get solution for `S.Integers` then need to go for `solveset`.
Integer solution is ` x = 8 + 22t` and `y = -1 - 5t`
`solveset` is defined to solve only for single variable, need extension here, so that we get solution for multiple variable like `solve`. one good example is [#1790](https://github.com/sympy/sympy/pull/1790)
    
            >>> solve(x**y - 1)
            [{x: 1}, {y: 0}]


and then implement  Diophantine equation algorithm to solve `ax + by = c`
for integer solution of `x` , `y`.
`Diophantine` is implemented in `diophantine.py` but not connected with solveset.
To connect them; `solveset` must be able to pass more than 1 variable for solution.  Other way is whenever there is `S.Integers` then call to `diophantine.py` methods according to the equation then return answer in `solveset` format using `FiniteSet` , `ConditionSet`, `ImageSet` etc  accordingly.

`x**n + y**n -z**n` this type of equation don’t have any Integer solution for any value of `n > 2`. If we try to get answer,  using `diophantine` you will get not implemented error.(According to Bachet, Fermat stated:
“It is impossible to separate a cube into two cubes, or a fourth power into two fourth powers, or in general, any power higher than the second into two like powers. I have discovered a truly marvellous proof of this, which this margin is too narrow to contain.”)
So need to check this pattern in `diophantine` and `diop_solve` method and return `EmptySet`or `None`.

#### 5. Inequalities & Equation solver having functions

     >>> solveset(x**4 - 7*(x**2) + 4*x + 20 >=0,x ,S.Reals)
     (-∞, ∞)           # ans is 2
     >>> solve(x**4 - 7*(x**2) + 4*x + 20 >=0,x)
     -∞ < x ∧ x < ∞   # ans is 2

I found this example here : http://www.cantab.net/users/henry.liu/inequalities.pdf
In this link almost all the examples can't be solved correctly using `SymPy` master branch.
Also some main feature that can be added is : `minimise`, `maximize` etc.
Already there is one issue opened [#4173](https://github.com/sympy/sympy/issues/4173)

Right now we can't solve system of inequalities using Solveset.
`solve` use `reduce_inequalities` method for this.

```
        x = Symbol('x')
        system = [Lt(x**2 - 2, 0), Gt(x**2 - 1, 0)]
        assert solve(system) == \
          And(Or(And(Lt(-sqrt(2), x), Lt(x, -1)),
               And(Lt(1, x), Lt(x, sqrt(2)))), Eq(0, 0))
```

Also like `solvers`, need to implement function solver in `solveset` : 

```
    f, g = map(Function, 'fg')
    fx, gx = f(x), g(x)
    assert solve([fx + y - 2, fx - gx - 5], fx, y, gx) == \
        {fx: gx + 5, y: -gx - 3}
    assert solve(fx + gx*x - 2, [fx, gx]) == {fx: 2, gx: 0}
    assert solve(fx + gx**2*x - y, [fx, gx]) == [{fx: y - gx**2*x}]
    assert solve([f(1) - 2, x + 2]) == [{x: -2, f(1): 2}]

```

These can be implemented with little effort. If we fix this then we can add these [test-case of `solvers`](https://github.com/sympy/sympy/blob/master/sympy/solvers/tests/test_solvers.py#L435) in solveset.

Another problem comes when we want general solution for trigonometric inequalities using 
`solveset`
In this examples SymPy returns the same answer for different intervals:

```
>>> solveset((2*cos(x)+1)/(2*cos(x)-1) <0,x,S.Reals)
(pi/3, 2*pi/3) \ ImageSet(Lambda(_n, 2*_n*pi - pi/3), Integers()) U ImageSet(Lambda(_n, 2*_n*pi + pi/3), Integers()) U (4*pi/3, 5*pi/3) \ ImageSet(Lambda(_n, 2*_n*pi - pi/3), Integers()) U ImageSet(Lambda(_n, 2*_n*pi + pi/3), Integers())

>>> solveset((2*cos(x)+1)/(2*cos(x)-1) <0,x,Interval(0,pi))
(pi/3, 2*pi/3) \ ImageSet(Lambda(_n, 2*_n*pi - pi/3), Integers()) U ImageSet(Lambda(_n, 2*_n*pi + pi/3), Integers()) U (4*pi/3, 5*pi/3) \ ImageSet(Lambda(_n, 2*_n*pi - pi/3), Integers()) U ImageSet(Lambda(_n, 2*_n*pi + pi/3), Integers())

``` 
Answer is : `(⅓)* (3*pi*n + pi) < x < (⅓)*(3*pi*n+2 pi),   n element in Z
`
Right now we have similar open issues; one of them is : [#10140](https://github.com/sympy/sympy/issues/10140)
Actually solveset uses the method `solve_univariate_inequality` defined in `inequalities.py`,  like old `solver`. And this method uses `solver` to get critical points of inequalities.
If we think more on this, then it seems there are many more cases, we may get wrong answer and we still don’t know.

-----------------

## Execution 

I am sure that during the execution I will get some more ideas/problems, issues, then we need to solve these issues and implement new ideas/methods accordingly.Actually each issue comes with many more issues and we should not ignore any of them. I am dividing my work into 3 phases and each phase is somewhat dependent with previous phase(Check timeline).

### Phase I

#### 1.1 Implement Non linear system of Equation solver : nlinsolve

Use `solve_poly_system` from `polysys.py` to solve non linear multivariate system of equations.

_Pseudo-code_ representation of the rough structure: 
 
```
def nlinsolve(equations, *symbols):
    from sympy.solvers.polysys import solve_poly_system
    
    if not equations:
        return []

    polys = []
    failed = []

    for equation in equations:
        f = sympify(equation)
        if isinstance(f, Equality):
            f = f.lhs - f.rhs
        ...
        ...
        poly = Poly(f)
        if poly is not None:
            polys.append(poly)
        else:
            failed.append(f)
    result = S.Empty()
    if not polys:
        solved_syms = []
    else:
            if len(symbols) > len(polys):
                # handle like solvers do
                # code here..
            ...
            ...
            else:
                try:
                    result = solve_poly_system(polys, *symbols)
                    solved_syms = symbols
                except NotImplementedError:
                    # condition Set return or not implemented error
    ...
    ...
    if result:
        # return solution in FiniteSet
    else:
        # if all the symbols value is not present in result
        # try the substitution method: maintain list of symbols to be solved and remain unsolved symbols
        solved_syms = # containing result.keys()
        unsolved_syms = # symbols not in result.keys()
        ...
        ...
        for eq in equations:
            # substitute all the result.keys() with it's value.
            for r in result:
                    # update eq with everything that is known so far
                    eq2 = eq.subs(r)
                    # if eq2 is True then add `r` into `final_res` 
                    newresult.append(r)
                    ...
                    ...

                    # if eq2 contains `unsolved_syms` calling them eq2_syms
                    for s in eq2_syms:
                        try:
                            soln = solveset_real(eq2, s)
                        except NotImplementedError:
                            continue
                    ...
                    ...
                    # append the soln into newresult.
                    # and continue
...
…

    return FiniteSet(tuple(newresult))

```
 
After this add test-cases from old `solver` and some special cases. Grobner basis is used inSymPy  ` solvers` to solve polynomial equations,which is working good but to solve equations like in this issue 
[#9673](https://github.com/sympy/sympy/issues/9673) we need to go for substitution method.

#### 1.2 Implement Transcendental Equation solver : tsolveset

Right now we have `tsolve` which works pretty good.

      >>> from sympy.solvers.solvers import _tsolve as tsolve
      >>> from sympy.abc import x
      >>> tsolve(3**(2*x + 5) - 4, x)
      [-5/2 + log(2)/log(3), (-5*log(3)/2 + log(2) + I*pi)/log(3)]
      >>> tsolve(log(x) + 2*x, x)
      [LambertW(2)/2]

So instead of this we need a more modular and extensible transcendental equation solver.
`solve(4**(2*(x**2) + 2*x) - 8, x)` uses `_tsolve` to get solution, but in `solveset` these types equations are usually taken care by `_invert` and last `else` statement of `_solveset`. But `_invert` is not able to return  `symbol` for which we are solving equation; in `lhs`.
So at the end it is returning `ConditionSet`.

One thing we can do is improve `_invert` method, where `is_Pow`  type equations are handled and at last check for `LambertW` pattern in the equation like `_tsolve` do, then after the proper simplification call `_solve_lambert`, which is defined in `bivariate.py` . So in this way we can get solution in `LambertW`.

To improve `_invert` method where `is_Pow` type equations are handled, we have to simplify equation after taking `log` both side then pass again into `_invert` method in a proper way. If there is `log` then need to simplify and get a pattern, if possible. I tried to add initial code for to handle `log` in this PR : [#10733](https://github.com/sympy/sympy/pull/10733/files#diff-eec0422923e8f100745c015cd8fdd6cfR194)

There can be mainly 3 types of equation pattern for `LambertW`
`x*exp(x) = y`, then solution for x is `LambertW(y)`
 `log(A+B*x) + C*x = log(D)` , then x = LambertW(C*D/B  * exp(A*C/B))/C  - A/B
` F(X, a..f) = a*log(b*X + c) + d*X + f = 0`, where X = g(x) and x = g**(-1)(X), then
            `x = g**(-1) (-c/b + (a/d)*W(d/(a*b)*exp(c*d/a/b)*exp(-f/a)))`

The last pattern is used in `_lambert` method in `bivariate.py` by `solvers`. I tried to explore how it is working, I found that it runs again and again same method to reach at that pattern.
If we analyse these 3 patterns in our algorithm  then it would take less time and we can fix other XFAIL test-cases present in `test_solvers.py` as well. 

Using these pattern we will be getting solutions in `LambertW` and other solutions we will get from `solveset` by improving the `_invert` method and comparing LHS and RHS free_symbols. 

Mainly we have equations like:

```
Problem  : x*b**(x) = y 
Solution : 
Re(x)>0 and b = 0 and y = 0
x = y and b = 1
x = 0 and b!=0 and y = 0
x = 0 and log(b)!=0 and b!=0 and y = 0
x = (LambertW(ylog(b)))/(log(b)) and log(b)!=0 and ylog(b)!=0 and b!=0 and n in Z

Problem : x**(x**a) = b for x
Solution: 
x = ((a log(b))/(LambertW(a log(b))))^(1/a)

Problem: a**x= x+b for x
Solution:
x = -b and a = 0 and Re(b)<0
x = 1-b and a = 1
x = 0 and a!=0 and b = 1
x = -(LambertW(-a^(-b) log(a))+b log(a))/(log(a)) and a^b !=0 and log(a)!=0 and a!=0 and n element in Z

```


### Phase 2
Trigonometric Functions

#### 2.1 Simplified General solution for Trigonometric Equations

First we extract the solutions without `imageset`( means solutions like old solve), then  
Two or more solution is passed into `genform` method ( or using the similar type of code/logic ) and get general function for them. First two itself will be able to generate other terms , if solution is not satisfying other equation then we can’t make genral form .Then change them into imageset will be desired solution.

_Pseudo-code:_ 

```
         a = Dummy('a', real=True)
         b = Dummy('b', real=True)
         n = Dummy('n', real =True)
         equations = []
         for i in xrange(0,len(args)):
             eq = a*(i+1) + b - args[i]
             equations.append(eq)
         a, b= list(linsolve(equations,(a,b)))[0]
         res = simplify(a*n + b) # this is our result
```

I have implemented a demo `genform` method in PR [#10713](https://github.com/sympy/sympy/pull/10713) and implemented this in solve_trig method in this  PR [#10898](https://github.com/sympy/sympy/pull/10898)

The above method may help somewhere ( if we modify these steps to get desired form), but after the discussion I found some issues. 

**Another idea is** : 

If we can get more simplified `poly_solution ` (means if solution for exp form of trig eq is  -I and I  => then we get two solutions `2n*pi + pi/2` and `2n*pi + 3*pi/2` . But it can be  `pi*(n+1)/2` )) ( here I am taking `3*pi/2` instead of `-pi/2`). The number of `exp`  terms is more =>  number of solution will be more (union). If somehow we make all the `exp` present  in the expression; into one `exp` args
(means `exp(I*x) +exp(-I*x)  = > exp(-I*x) * ( exp(2*I*x) +1)`  then` exp(-I*x) = 0` have no solution and solution of `exp(2*I*x) +1= 0 `will contribute for final solution which is `pi*(n+1)/2` ) so in this way we can get more simplified solution. 


#### 2.2 Trigonometric Equation and System of Equations solver

#### 2.2.1 Trigonometric Equation

In this case we need to improve `solve_trig` method to handle some complicated equations. I have tried some changes in [PR #10733](https://github.com/sympy/sympy/pull/10733/files#diff-eec0422923e8f100745c015cd8fdd6cfR390) . This change is giving simplified solution for all trigonometric functions and using this change I have fixed many other bugs. 

But still we need improvement in `solve_trig` method for 
`solveset(sin(x)**3 + cos(3*x) ,x,S.Reals)` types of equation.

It seems there are two ways : 

* System of Equation : Do `expand(Trig = true)` and `rewrite` the expression in `sin`, `cos`. Use another Trigonometric identities accordingly mostly 
`sin(x)**2 + cos(x)**2 -1 =0` will help. Now using two Dummy variable `s` and `c` solve the equation using `linsolve` or `nlinsolve` accordingly. Then replace the Dummy variable with `sin`, `cos` and solve using `_solve_trig` and union.

* Factorization : Do `expand(Trig = true)` and `rewrite` the expression in `sin`, `cos`, then use `factor` , `decompogen` methods.
Thereafter we may get `f1(x)*f2(x)*f3(x)..` now solve for `f1(x) =0`, `f2(x)=0`and so on. Union of all these solution will be final answer.
I know a good way of factorization for special cases using vedic mathematics, I used during school days : [LOPANASTHĀPANĀBHYĀM ](https://drive.google.com/file/d/0B_GhLAhyhSVdLU5XSEQ3Vm5RVTQ/view?usp=sharing) [more examples](http://mathlearners.com/vedic-mathematics/solving-equations/factorization/) .

#### 2.2.2 Trigonometric System of Equations

Accordingly pass system of Trigonometric equation in `trigsolve` method (say).
In this method  `expand(Trig = true)` and `rewrite` in `sin`, `cos`, each equation passed in the system and simplify. (Before this check that all have same arguments ,means in `sin(A) , cos(B) => A should be equal to B`)
Now replace `sin`, `cos` with Dummy variables and solve them using `linsolve` or `nlinsolve` . We can use methods like `diophantine` have `classify_diop` which returns the type of the equation. (ODE also have hint system)

#### 2.3 Trigonometric Inequality General Solution

We are not getting general solution for the Trigonometric inequalities , even for the simple equation like`cos(x) <0` .
The main problem is `solveset` follows `solvers` way to get solution. It is using `solve_univariate_inequalities` method which uses `solvers` to get critical point
( so the answer is not in general solution).

Because we use `imageset` in solveset so if we write the same method 
(`solve_univariate_inequalities` ) using `solveset`,   problem comes in further lines of code in that method.

There are good ways to handle trigonometric inequalities [20](http://www.mathematicsmagazine.com/corresp/NghiNguyen/SOLVING_TRIGONOMETRIC_INEQUALITIES.pdf) ,  [21](http://www.shelovesmath.com/trigonometry/solving-trig-equations/) 

Step 1. Find critical points using solveset.
Step 2. In each imageset lambda put n=0 and get answer within 2*pi  say Xi.
Step 3. Draw sign chart range 0 to 2*pi . (maintain map; key : interval , value : +ve or -ve)
Step 4. Divide this into critical points Xi.
Step 5. Pick the point inside each interval and `subs` in inequality if true add that interval to `soln_set`.
Step 6. Add 2*n*pi to each `soln_set` interval boundary . This is final solution.

There may be the case where we can combine two interval if there is difference of `pi`.
And then we just need to add `pi*n` instead of `2*n*pi`.
Like in this case `(2*cos(x)+1)/(2*cos(x)-1) <0` 
Here critical points are : `2*pi*n + pi/3 , 2*pi*n + 2*pi/3 , 2*pi*n + 4*pi/3 , 2*pi*n +5*pi/3` . If we observe carefully then we find that after`pi` it is repeating.( inside range `2*pi` )
( check last two critical points)
`( pi+ pi/3 ) => 4*pi/3 , (pi+2*pi/3) => 5*pi/3`. 
So general solution can be written as `pi*n + pi/3 `and `pi*n + 2*pi/3`.
Final ans is : `( pi *n+ pi/3  )< x <  ( pi* n + 2 pi/3),   n  element  in Z`


### Phase 3

#### 3.1 Solution in S.Interger from Solveset using diophantine.py

Whenever `domain = S.Integers` it should call methods present in `diophantine.py`. It seems mostly we should use `diop_solve` method to get solution in Integers. 
There are many types of equations are already implemented in `diophantine.py` .

Right now we can pass only one symbol in `solveset`, so to get integer solution first check domain is `S.Integers` or not and call `diop_solve` get the solution like old solvers format, change the format accordingly for `solveset` and return the solution for the `symbol`.


```
>>> diop_solve(18*x + 5*y-48)
(5⋅t₀ + 96, -18⋅t₀ - 336)

>>> solveset(18*x + 5*y-48, x, S.Integers)
ConditionSet(ImageSet(Lambda(n, 5*n + 96), S.Integers), Eq(y, ImageSet(Lambda(n, -18*n - 336), S.Integers)), True)

>>> solveset(18*x + 5*y-48, y, S.Integers)
ConditionSet(ImageSet(Lambda(n, -18*n - 336), S.Integers), Eq(x, ImageSet(Lambda(n, 5*n + 96), S.Integers)), True)

```

If solution returned is `(None, None)` by `diop_solve` then in solveset we convert this to `ConditionSet` .
Example : 

```
>>> diop_solve(6*x + 51*y-22)
(None, None)

>>> solveset(6*x + 51*y-22, x, S.Integers)
ConditionSet(x, Eq(x, -17*y/2 + 11/3 ), S.Integers)

```

**_Another way is_** : 

Just pass the domain = S.integers in solveset with equation and solveset will return the solution for all the free_symbols present in the equation, in FiniteSetjust like linsolve return .

```
>>> solveset(18*x + 5*y-48, domain = S.Integers)
{x = 5⋅t₀ + 96, y = -18⋅t₀ - 336}

```

**System of Linear diophantine equations** :

To solve linear diophantine system of equation , one of the good algorithm is Euclidean Algorithm mentioned in this link : [System of Diophantine equations](https://www.math.uwaterloo.ca/~wgilbert/Research/GilbertPathria.pdf) (example 2 ,5th page).
General algorithms for almost all types of diophantine equations and linear system is in this link : [ pdf 98 page](http://fs.gallup.unm.edu/SolvingDiophantineEquations.pdf)


#### 3.2 System of Inequalities

Old `solver` can solve System of inequalities using `reduce_inequalities` method defined in
 inequalities.py.
But we can pass only one equation in `solveset` we need a method `ineq_solve` (say).

Pseudo code : 

```

def ineq_solve( ineq, symbols):
	from sympy.solvers.inequalities import reduce_inequalities

	if not ineq:
        return [ ]
	...
	...
    for i, fi in enumerate(ineq):
    	if isinstance(fi, (bool, BooleanAtom)) or fi.is_Relational:
            soln = reduce_inequalities(ineq, symbols=symbols)

	...
	...

    if soln is None:
    	# print condition set
    else:
    	# use piecewise or imageset accordingly and return.

```


#### 3.3 General solution for inverse trigonometric functions

`_invert` method is able to return the inverse solution in general form. We can implment it using similar logic .
We can add test cases from this link http://mathsfirst.massey.ac.nz/Trig/example2.htm

From the master branch here is what we get right now : 

```
>>> acos(S(1)/2)
pi/3
>>> asin(-S(1)/2)
-pi/6
```

#### 3.4 Others 


*  If we don't want solution in `imageset` and want answer for particular value of `n` then we should have a helping method on which we pass value of `n` and then substitute value in lambda and return.(This may be helpful in replacement of internal `solver`)


------------------

## Timeline

This project may take more time (15+ week),  I am confident that I have the skills and experience to successfully complete the project. If something will have not done by GSoC time period then I'll try to complete them after the GSoC.  As far as Community bonding is concerned, I have been working with `SymPy` for around 6 months and active in SymPy gitter chat room since August 2015, So I am quite familiar with the Development Workflow and almost know all the methods in `Solveset` and `Solvers` module.
I will have my exams 5 may to 12 May, So in this period I can spend 2 hours only. Thereafter I will be able to spend my full time on this project till August( college will be restarted in August).

#### Community Bonding Period Week 1,2,3 (exams time) [ 22 April - 14 May]

*  Implement Non linear multivariate equation system using `solve_poly_system` in `polysys.py`.
*  Add a method that will handle the multivariate equation system.

#### Week 4,5 [ 15 May - 28 May]

*  Rewrite `_tsolve` for `solveset` to solve Transcendental equations using `bivariate.py`.
*  Write test-cases and fix other types of equations.
 
#### Week 6, 7 [ 29 May - 11 June]

*  Implement non linear equation system solver use substitution, quadratic formula methods and old solver methods.
*  Write test-case and fix other types of bugs.

#### Week 8,9 [ 12 June - 25 June]

*  Simplified general form solution for trigonometric equations.
*  General solution for hyperbolic Functions.
*  General solution for inverse trigonometric equation.
*  Add test-case.

#### Week 10 & 11 [ 26 June - 9 July]

*  Implement trigonometric equation solver.
*  Write test-case and Fix internal bugs.
*  Implement trigonometric equation system solver, add testcase.

#### Week 12, 13, 14 [ 10 July - 31 July]

*  Integer solution from `Solveset` using `diophantine.py` .
*  Make required changes and add methods to make solution in `Sympy` sets.
*  Add test-cases.

#### Week 15, 16, 17 [ 1 August - 23 August]

*  Finishing above works if it is remaining.
*  Improve inequality solver ,Implement function solver in solveset, work on ODE, to make it more simpler.
*  Replace all internal `solve()` calls with `solveset()`
*  Work on `imageset` to get answer for particular value of `n` in `solveset`.

----------------

How do I fit in?


I have good working experience with SymPyand I am familiar with senior developers. I'm well familiar with `solveset` code and aware of the challenges of this project. I have already discussed/implemented some of the ideas and have sent PRs to be sure.  I am confident that I have the skills and the experience to complete the project successfully

-------------------------

#### Any Plans/Commitment (During GSoC)

* I don't have any specific plan for this summer, so I can spend my full time on this project.
* I will write my blog, for this GSoC project weekly in my website , [My blog template](http://shekharrajak.github.io/MyBlog/index.html).
Right now it is just filled with random text. I created this blog just for the GSoC.
Otherwise I will make wiki page for weekly report inSymPy.
* College will be restarted in 1st week of August (or last week of july). In 1st month of the semester, we don’t have any exams so I can concentrate on the project during these days and also for this month I have put relatively less work, in the timeline.

------------------------

#### Future Plans (After GSoC)


* If I stuck somewhere in implementation, I will try to complete them after the GSoC period. 
I will continue my contribution and will be active in `SymPy` community also will help new contributors.
* If possible, I want to contribute to [symengine](https://github.com/symengine) .

--------------------

##  Previous discussions

All the above contents are from my these discussions :

* https://groups.google.com/forum/#!topic/sympy/XhgBx2bVFaA
* https://github.com/sympy/sympy/wiki/Solveset-and-Solver-Discussion

Thanks to everyone who participated in the discussion and SymPy gitter chat room.

--------------------
# References

* [1] Harsh Gupta's [GSoC Application](https://github.com/sympy/sympy/wiki/GSoC-2014-Application-Harsh-Gupta%3A-Solvers)
* [2] Amit Kumar's [[GSoC Application](https://github.com/sympy/sympy/wiki/GSoC-2015-Application-AMiT-Kumar--Solvers-:-Extending-Solveset)
* [3] [On the Lambert W Function](http://www.apmaths.uwo.ca/~djeffrey/Offprints/W-adv-cm.pdf)
* [4] [Lambert's W Function in Maple](http://citeseerx.ist.psu.edu/viewdoc/download?
* [5] [Using the Lambert W Function, a.k.a. ProductLog](http://2000clicks.com/mathhelp/BasicSimplifyingLambertWFunction.aspx)
* [6] [LambertW Simplifications](https://github.com/sympy/sympy/issues/5080), [2870](https://github.com/sympy/sympy/pull/2870),  [5080](https://github.com/sympy/sympy/issues/5080)
* [7] [Implementation of Equation Solvers](https://groups.google.com/forum/#!msg/sympy/42GdMJ9ssyM/swC6bHVunP8J)
* [8] [wiki/solvers](https://github.com/sympy/sympy/wiki/solvers)
* [9]  [Action Plan on solvers](https://github.com/sympy/sympy/pull/2948)
* [10] [Harsh's blog for GSoC](http://hargup.github.io/categories/sympy.html)
* [11] [solveset pull request](https://github.com/sympy/sympy/pull/7523)
* [12] [Amit's blog for GSoC](http://iamit.in/blog/)
* [13] [Solveset Documentation](https://github.com/sympy/sympy/blob/master/doc/src/modules/solvers/solveset.rst)
* [14] [issues/10006](https://github.com/sympy/sympy/issues/10006)
* [15] [MinimizationAndMaximization](https://reference.wolfram.com/language/tutorial/MinimizationAndMaximization.html)
* [16] [factorize-the-polynomial](http://math.stackexchange.com/questions/543991/factorize-the-polynomial-x3y3z3-3xyz/544042#544042)
* [17] [Diophantine_equation](https://en.wikipedia.org/wiki/Diophantine_equation) , [#9748](https://github.com/sympy/sympy/issues/9748) , [System of Diophantine equations1](https://www.math.uwaterloo.ca/~wgilbert/Research/GilbertPathria.pdf) ,[page 48](https://books.google.co.in/books?id=mmYECAAAQBAJ&pg=PA42&lpg=PA42&dq=solving+diophantine+equations+complex+complicated+questions&source=bl&ots=qKrKtcqomW&sig=SUbFepqmhstwX5wIG-VernkO8SU&hl=en&sa=X&ved=0ahUKEwjVuvnum7TLAhXYCY4KHafCAu8Q6AEIQDAH#v=onepage&q=solving%20diophantine%20equations%20complex%20complicated%20questions&f=false) 
* [18] [List_of_trigonometric_identities](https://en.wikipedia.org/wiki/List_of_trigonometric_identities)
* [19] [fateman/papers/solving.pdf](http://www.cs.berkeley.edu/~fateman/papers/solving.pdf)
* [20] [SOLVING_TRIGONOMETRIC_INEQUALITIES](http://www.mathematicsmagazine.com/corresp/NghiNguyen/SOLVING_TRIGONOMETRIC_INEQUALITIES.pdf)
* [21] [solving-trig-equations](http://www.shelovesmath.com/trigonometry/solving-trig-equations/)
* [22]  https://perso.univ-rennes1.fr/marie-francoise.roy/bpr-ed2-posted1.pdf
* [23] [SolvingDiophantineEquations.pdf - with algorithms](http://fs.gallup.unm.edu/SolvingDiophantineEquations.pdf)
