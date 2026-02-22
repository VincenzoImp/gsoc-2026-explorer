# GSoC 2015 Project: Amit Kumar

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/wiki/GSoC-2015-Application-AMiT-Kumar--Solvers-:-Extending-Solveset
**Scraped:** 2026-02-22T23:28:47.570707

---

# About Me

## Basic Information
**Name**: AMiT Kumar

**Email**: dtu.amit@gmail.com

**University**: [Delhi Technological University, India](http://dce.edu)

**Github/IRC**: [aktech](https://github.com/aktech)

**Website/Blog**: [iamit.in](http://iamit.in/) | [blog.iamit.in](http://iamit.in/blog)

**Timezone** :  IST (UTC +5:30)

## Personal Background
I am a 3rd year undergraduate pursuing Bachelor of Technology in **Mathematics and Computing** Engineering at Delhi Technological University, India. I have been consistently exposed to the field of Mathematics since my high school, and have taken courses in Higher Mathematics including Abstract Algebra, Linear Algebra, Real Analysis, Discrete Mathematics, Advanced Engineering Mathematics - I,II & III as well as in Computer Science including Data Structures and Algorithm Design & Analysis in my Graduation. 

## Programming Details
I work on Ubuntu 14.04 LTS machine with Sublime text 3 as my primary text editor because of it's user-friendliness and quick learning curve. I am very much familiar with version control system and been using Git(command line) and Github for quite some time now. I have been programming for over 3 years now, I started with C/C++ and then learnt some Object Oriented Concepts and tried Java and Python. I switched to **Python** over an year ago due to the fact that there is little difference between Pseudo Code and Python code, which makes life of a Programmer much easier.

Favorite Features of Python: Extended unpacking (Python 3) & Zipping/unzipping of iterables. 
In SymPy my Favorite feature is the Solvers & Integral Modules, since it implements the things which are often pretty tough doing Manually, that's the prime reason I am extremely Interested in the Solvers Module. 

I also own a copy of Mathematica 10 & Maple 18, which will help me in comparing the results obtained through my implementations in SymPy to ensure correctness.

# Contributions to SymPy
I started playing with SymPy for my coursework in mid November 2014 & made my first contribution in December 2014, Since then I have been consistently contributing and learning from the great community. I have made 19 Pull Requests out of which 17 were merged. Following is the list of all the Merged and unmerged Contributions in chronological order.

* **(Merged)** [PR #8647](https://github.com/sympy/sympy/pull/8647) : `Fix sign Error in Unrad Function in Solvers` `unrad` is used to simplify radicals, it had a minor sign error, for some type of Equations like: `(root(x + 1, 5) - root(x, 3))` which returned wrong answer. It was quite easy to fix. Fix Issue #8622.

* **(Merged)** [PR #8684](https://github.com/sympy/sympy/pull/8684) : Solve return solution for Equation where denominator becomes 0 in cases where equal terms cancel out on both sides of equation, For Equations like: `x + 1/x == 1/x` or `x**2 - 1/(x**2 - 4) == 4 - 1/(x**2 - 4)`: Earlier it returned `+/- 2` as the solution, which is wrong as it makes the denominator `Zero` Fixed that by unevaluating the expression, while processing the Equation. 
Fix Issue #8666

* **(Merged)** [PR #8700](https://github.com/sympy/sympy/pull/8700) : Function to Rewrite `gamma` as `Factorial`, Rewrite of this kind is very useful in case of combinatorial simplification. Earlier we could only rewrite factorial in terms of `gamma`, but with the help of this PR, we can do vice-versa also. 
Fix #8621

* **(Merged)** [PR #8706](https://github.com/sympy/sympy/pull/8706) : Add is_real functionality for factorial, Fix issue #8658

* **(Closed)** [PR #8719](https://github.com/sympy/sympy/pull/8719) : closed for the need of better patch, later this was Fixed in #8519

* **(Merged)** [PR #8723](https://github.com/sympy/sympy/pull/8723) : Improve real assumption helper for factorial function, there was some logical error in the earlier implementation, since earlier factorial(x) was not known to be real when x is a noninteger. 
Fix #8722

* **(Merged)** [PR #8741](https://github.com/sympy/sympy/pull/8741) : Add Support for negative numbers in `round` function, as round function didn't expected negative arguments: `round` function was behaving unexpectedly for negative values (as reported in mailing list), sometimes it returned right answer and sometimes wrong. Fixed that by creating different case for negatives. 
Fix Issue #8720   

* **(Merged)** [PR #8750](https://github.com/sympy/sympy/pull/8750) : Add is_composite for factorial function, Earlier If n is a nonnegative integer, `factorial(n+3).is_composite` returns None, but that was wrong since composite asumption helper was not implemented for Factorial. 
Fix 8724

* **(Merged)** [PR #8765](https://github.com/sympy/sympy/pull/8765) : Rewrite Factorial as Product, `>>> factorial(k).rewrite(Product)`
Fix Issue #8757

* **(Merged)** [PR #8784](https://github.com/sympy/sympy/pull/8784) : Fix solve(x < oo) & Handle infinity for converting a relational to Sets,  
There is some discussion needed to handle some cases, i.e. disallow oo as solution (i.e. we search for solutions over real/complex domains, not in extended reals) as pointed by Sergey.
Fix Issue #8783 , #8777, #8613, #8252.

* **(Merged)** [PR #8835](https://github.com/sympy/sympy/pull/8835) : Add Interval convenience Methods, such as 
`Interval.Ropen(0, 1)` : [0, 1) `Interval.Lopen(0, 1)` : (0, 1] `Interval.open(0, 1)` : (0, 1) : This was suggested by Chris.

* **(Merged)** [PR #8846](https://github.com/sympy/sympy/pull/8846) : Fix floor(x -/+ S.Half).is_even for negative even x & Fix is_positive for gamma. Closes #8524 

* **(Merged)** [PR #8874](https://github.com/sympy/sympy/pull/8874) : Add Sphinx docs for `solveset` Closes #8725  

* **(Merged)** [PR #9013](https://github.com/sympy/sympy/pull/9013): Remove C from sympy.solvers for non-cylic imports, This was in continuation of Joachim's effort to remove C.

* **(Merged)** [PR #9008](https://github.com/sympy/sympy/pull/9008): Extend Catalan number to negative numbers

* **(Merged)** [PR #8976](https://github.com/sympy/sympy/pull/8976): Fix `solve_univariate_inequality` to handle infinity : This was an improvement for my previous attempt at improving handling of infinity for inequalities, which was the culprit for wrong results in `as_set` as well.

* **(Merged)** [PR #9148](https://github.com/sympy/sympy/pull/9148): `ln(n) should be nonnegative for a positive integer n` , Fixes #9116

### Bugs/issues reported:
* [Issue #8783](https://github.com/sympy/sympy/issues/8783) : `solve(x < oo)` and `solve(x > -oo)` returns `False`,
**Caught and Fixed**.
* [Issue #8777](https://github.com/sympy/sympy/issues/8777) : `And(x > 2,x < oo).as_set()` returns `EmptySet()` ,
**Caught and Fixed**.
* [Issue #8716](https://github.com/sympy/sympy/issues/8716) : `solve(x, sqrt(x**2))` returns None.
* [Issue #8715](https://github.com/sympy/sympy/issues/8715) : `solve(x + 1/x > -2 + 1/x)` inequality returns solution  making denominator `0`.
* [Issue #8853](https://github.com/sympy/sympy/issues/8853) : floor(x - S.Half).is_even returns True for negative even 'x'
* [Issue #8666](https://github.com/sympy/sympy/issues/8666) : `solve(Eq(x**2 - 1/(x**2 - 4), 4 - 1/(x**2 - 4)))` returns a set of solution for Equation making denominator `0`. **Caught and Fixed**.

# The Project

## Brief Overview

*SymPy already has a pretty powerful solve function. But it has a lot of major issues.*

Last year, Harsh Gupta, did a Google Summer of Code project to improve Solvers. Instead of making changes in the current `solve` function a new submodule named `solveset` was written. The goal of writing solveset was to eventually replace solve, by the time `solveset` fixes all the mess around `solve`. Harsh rewrote the univariate solver, and built the basic Set infrastructure to support the solutions returned for solveset.
I, on my part have to extend the solveset module to support solving System of Equations, Transcendental Equations and Multivariate equations. The solveset is still in the sandbox, I need to make it fully functional, since, solvers are central to any Computer Algebra System.

# The Plan

The Current solve needs to be broken into various sub-modules (sub-hints, described below), to make the code more robust, modular, and approachable for developers, moving in lines of the new API, as developed in `solveset`. Currently the new API is implemented for univarate Equations (single equation, single variable) only, we need to incorporate it for linear systems, multivariate equations & transcendental by rewriting the solvers for these in the new `solveset`.


### Basic Idea 

Solving Equations in a Computer Algebra System is quite a General thing, there are always some problem sets which needs to be addressed, So it is very important to build a robust framework which is not effected by some changes in `foo` algorithm for solving a `bar` class of equations. An Important Idea in this regard is the Framework of **Rewriting** and **Decomposition** [ [13] ](https://groups.google.com/forum/#!msg/sympy/42GdMJ9ssyM/swC6bHVunP8J) , accompanied with the **Hint System**. The Framework of Rewriting and Decomposition will help to make an equation solvable by performing some transformation on the Equation(s), for example:

* If we have an Equation given as:

![Equation](https://github.com/aktech/sandbox/blob/master/fx.png?raw=true)

* We have to solve for f(x) = 0, then f(x) can be **Decomposed** as:

![fgx](https://github.com/aktech/sandbox/blob/master/fgx.png?raw=true)

* where `g(x)` is:

![gx](https://github.com/aktech/sandbox/blob/master/gx.png?raw=true)

* `g(x)` replaced by a dummy variabe `t` : 

![ft](https://github.com/aktech/sandbox/blob/master/ft.png?raw=true)

* solving `f(t)` as a polynomial (quadratic here) and finding it's roots

![ftfactor](https://github.com/aktech/sandbox/blob/master/ftfactor.png?raw=true)

* Now `f(x)` has been broken into two simple functions, i.e. `f(x)` has been **Rewritten** as product of two simple equations:

![fxfactor](https://github.com/aktech/sandbox/blob/master/fxfactor.png?raw=true)

* Written as product of two functions `h(x)` and `g(x)`:

![fhk](https://github.com/aktech/sandbox/blob/master/fhk.png?raw=true)

* Solving for the two simple functions, separately:

![hk](https://github.com/aktech/sandbox/blob/master/hk.png?raw=true)

* We get the solution as:

![solx](https://github.com/aktech/sandbox/blob/master/solx.png?raw=true)

The Methods used for solving various classes of Equations, can be encapsulated inside a **Hint System** , the idea of hint system is similar to the one used in `ODE` Module, the goal is to enhance convenience to add new solvers without disturbing others, for example the hints used above would use `LambertW` and `Polynomial(quadratic)` methods of hint system.

**Example**
```python
primaryhint = [
    "univariate",
    "multivariate",
    "single_eq",
    "multiple_eq"
    ]


subhints = [
    'solve_linear_system'
    'linear_trig',
    'polynomial',
    'transcendental',
    'piecewise',
    'relational'
    'solve_lambertw'
    'miscellaneous'
    'and a few more'
    ]
```
* The Framework of Rewriting and decomposition described above would help to convert the equation into classifiable form, for example the `f(x)` described above, when converted to `h(x)*k(x)` will then be analyzed with respect to `h(x)` and `g(x)` to find out the hints used to solve the comparatively simpler equations, this process would be repeated until the given equation is trivially solved.

--------------------------

##### 1. Complex Sets:

  - In `solveset` we have two functions `solveset_real` and `solveset_complex` for finding the solution in Real and Complex domains respectively, but we don't have Complex Sets to represent regions in Complex domain.

Currently, it returns only real solution, for equations like these.
```
In []: z = symbols('z', real=False)

In []: solveset(Abs(z) > 1)
Out[]: (-oo, oo)
```


  - We need to implement Complex Sets, Since as of know we don't have a function to compute the domain of a function, this is indeed would be a very useful feature, and not having a Complex Set Infrastructure is a blocking issue in this regard. We need to answer Questions like domain of `1/x` which should be ℂ - {0}.

  - With the Introduction of `solveset` an important problem of representing infinite solution has been solved to some          extent, but still there are some issues with ImageSet Union, due to which a lot of simpler results are not displayed        properly. This needs to be figured out to get better ImageSet Union.
```
In [18]: solveset(sin(3*x))
Out[18]: 
                                        ⎧        2⋅π        ⎫   ⎧        2⋅π  
{2⋅n⋅π | n ∊ ℤ} ∪ {2⋅n⋅π + π | n ∊ ℤ} ∪ ⎨2⋅n⋅π - ─── | n ∊ ℤ⎬ ∪ ⎨2⋅n⋅π + ─── |
                                        ⎩         3         ⎭   ⎩         3   

      ⎫   ⎧        π        ⎫   ⎧        π        ⎫
 n ∊ ℤ⎬ ∪ ⎨2⋅n⋅π - ─ | n ∊ ℤ⎬ ∪ ⎨2⋅n⋅π + ─ | n ∊ ℤ⎬
      ⎭   ⎩        3        ⎭   ⎩        3        ⎭
```
##### 2. Linear System of Equation:
  - Solving system of linear equations is an important feature of `solvers` in a CAS, these arise quite frequently in "real life", problems and can be incredibly complex sometimes. Most of the CAS have a convenient single function to solve linear systems for example `LinearSolve` in Mathematica, `linsolve` in Matlab and Maxima.

  - As of now Solving Linear System is a big mess in the current solve(), we have lots of function for handling this system, here is a list of ways we can solve linear systems in SymPy:

    * `solve(equations, unknowns)`
	* `solve_linear_system(aug_matrix)`
	* `solve_linear_system_LU(aug_matrix, unknowns)`
	* `solve_poly_system(equations, unknowns)`
	* `solve_linear(single_equation)`
	* `polys.solvers.solve_lin_sys(equations, ring)`
    * `minsolve_linear_system(system, symbols)`

  - and these are some helper functions (which should have been encapsulated):
    * `det_minor`
    * `det_quick`
    * `inv_quick`
    * `det_perm`

  - Secondly we have some inconsistency in the behaviour of  `solve_linear_system` and `solve_poly_system` :

``` 
    In []: M = Matrix([[1,2,0], [3,-4,1]])
    In []: solve_linear_system(M, x, y)
    Out[]: {x: 1/5, y: -1/10}

    In []: solve_linear_system(M, [x, y])
    Out[]: []

    In [32]: f = [x + 2*y, 3*x - 4*y - 1]

    In []: solve_poly_system(f, x, y)
    Out[]: [(1/5, -1/10)]

    In []: solve_poly_system(f, [x, y])
    Out[]: [(1/5, -1/10)]
```
  - `solve_linear_system()` fails when the variables are given inside an iterable, Whereas `solve_poly_system()` has a consistent output, it handles different input formats.
  - Currently Most of these functions are used sparsely inside SymPy's code base, given the frequency with which linear
systems are employed in mathematics, this inconsistency is unacceptable.

* **Proposed Solution:**
  - We need to implement a General Linear System Solver in the `solveset` 
     - Which should be able to recognize and pre-process all natural forms of linear systems.
     - It should be in public API as well, like say `linsolve()` (not just only accessible through `solveset`), since It always a good idea to directly use that specfic function, when we are already aware that we are dealing with linear systems.
     - There should be a convenience of Input in the form of either a Matrix or a List of Equations. (A convenience method to convert List of Equations into Matrix would be implemented.)
     - All the inconsistency inside the code base using linear system solver should be removed in favour of General Linear Solver
     - After all these, Most of the above functions should be deprecated in favour of the General Linear System Solver.


##### 3. Transcendental Equations
  - A Major class of Transcendental Equations can be solved by the LambertW Function, currently only the principal branch of     LambertW is implemented in old `solve`, which is one of the reasons for loss of Solutions. `solveset` doesn't support this as of yet.

  - This paper: [by Robert M. Corless, Gaston H. Gonnet, D. E. G. Hare, and David J. Jerey](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.33.2556&rep=rep1&type=pdf) 
    collects most of the facts about the LambertW function. I plan to implement the LambertW solver using this as reference.

  - Below are my notes on Brief Overview of the LambertW Function:
     * The LambertW Function is defined to be the multivalued inverse of the function:
        ![](https://github.com/aktech/sandbox/blob/master/fxlw.gif?raw=true)
     
     * That is:

        ![](https://github.com/aktech/sandbox/blob/master/finv.gif?raw=true)

        ![](https://github.com/aktech/sandbox/blob/master/xlw.gif?raw=true)

     * Writing the above in more General Form:
     
        ![](https://github.com/aktech/sandbox/blob/master/lamsomething.gif?raw=true)
     
     * Denoting `LambertW(x)` with `W(x)` Replacing x -> `W(z)`, we get:
     
        ![](https://github.com/aktech/sandbox/blob/master/zw.gif?raw=true)
        
    * Which can be simplified to get this general result:
    
       ![](https://github.com/aktech/sandbox/blob/master/lwsome.gif?raw=true)
       
       The above results are very useful in solving equations.
       
    * Real branches of LambertW function:
      - If x is real then for `-1/e <= x < 0` there are two possible values of W(x) (or `LambertW(x)`):
      We denote the branch satisfying: `-1 <= W(x)` by W<sub>0</sub>(x) known as **Principal branch**
      - & the branch satisfying `W(x) <= -1` by W<sub>-1</sub>(x)  (**See Graph**)
        
        ![](https://github.com/aktech/sandbox/blob/master/Diagram_of_the_real_branches_of_the_Lambert_W_function.png?raw=true)
    * **Summary**

      In General the solution of the Equation `x*exp(x) = a` is `W(a)` or `LambertW(a)` , a variety of equations can be solved in terms of the same transcendental function.
      Below are some examples:

      * **Problem|Solution**

      ![](https://github.com/aktech/sandbox/blob/master/lw1.gif?raw=true)
      
      ![](https://github.com/aktech/sandbox/blob/master/lw2.gif?raw=true)
      
      ![](https://github.com/aktech/sandbox/blob/master/lw3.gif?raw=true)
      
      

##### 4. Multivariate Equation solving:

* As of now solveset doesn't support solving equations for more than one variable, the support for Multivariate Equations and Multivariate System of Equations needs to be added

* We need to be very specific about the problem set we are 
going to tackle for 'Multivariate Functions' in the solveset.
Here are the cases where we encounter Multivariate Functions:

 - System of Multivariate Equations
 - Multivariate Single Equation with Point solution.
 - Multivariate Single Equation with non-point solution.
 - Multivariate inequalities (requires CAD), will be addressed in the API with `NotImplementedError`. 

* For solving multivariate equations, the order of variables should be given as input, so that we don't need to return dict of (variable and value) and, we can have a consistent Set output.


##### 5. Implementing new Algorithms
   (In `sympy.calculus`)

  * Singularities
    - Singularities module would be useful in general, so as to prevent getting wrong results, caused due to incorrect simplification of expression, as we saw in this issue: https://github.com/sympy/sympy/issues/8715 , Example: `x + 1/x > -2 + 1/x`  this inequality is written as expr = expr. lhs - expr.rhs , which cancels 1/x and gives wrong result, by including singular point in the solution.

  * General Methods in Differential Calculus
    - Some General convenience methods will be implemented, to check if a function is monotonic, increasing or decreasing.


##### Few other TODO`s:

* We should be able to have support for solving for non-Symbols entities as well, like functions.

* We also need to extend the set - boolean (relational) conversion methods to handle multivariate variables.

* Inequality solver in solveset currently uses inequalities.py (which is dependent on solvers.py) (some discussion here: https://groups.google.com/forum/#!topic/sympy/Yp5NqrXmp2U). It should rather use solveset. 

* All internal solve() calls needs to be replaced with `solveset()` , this is very important for bringing out the solveset from sandbox to eventually replace solve().   (we need to consider the output API (return type) also while replacing).


# Execution

The Project has been divided on the basis of Merge-able portions as mentioned in the following sections:  

#### I. Build Complex Set Infrastructure:

**Complex Set Infrastructure**
 
* There are two ways to represent Complex Interval, namely Rectangular Form & Polar Form:
   - `Z = {z ∈ ℂ | z = r*exp(iθ), r ∈ [r], θ ∈ [θ]}` 
   - `Z = {z ∈ ℂ | z = x + I*y, x ∈ [Re(z)], y ∈ [Im(z)]}`


This is how Complex Interval/Complex Sets/Complex Plane would look like.

* In Rectangular Form (Cartesian Form)
(Second arg contains product of Iota & Interval)
Args are Interval of `x` and `y` respectively for `x + I*y`

```
In []: unit_square = ComplexInterval(Interval(-0.5, 0.5), I*Interval(-0.5, 0.5))

In []: 0.25*I in unit_square
Out[]: True 

In []: a = 2 + 3*I

In []: a in unit_square
Out[]: False
```

* In Polar Form (Args are Range of r and theta respectively)

```
In[]: unit_disk = ComplexInterval(Interval(0,1), Interval(0, 2*S.pi))

In []: 0.5*I in unit_disk
Out[]: True

In []: a = 1 + 2*I

In []: a in unit_circle
Out[]: False
```

* Sets to Boolean & Boolean to set Transformations for multivariate sets and Boolean.

```
In []: (x**2 + y**2 < 1).as_set(r, theta)
Out[]: {(r⋅cos(θ), r⋅sin(θ)) | r, θ ∊ [0, 1] × [0, 2⋅π]}

In []: Interval(0, 1)*Interval(0, 3).as_relational(x, y)
Out[]: x ≥ 0 ∧ y ≥ 0 ∧ x ≤ 1 ∧ y ≤ 3
```

#### II. Solving Linear Systems: 

* `linsolve` : General Linear system solver.
* Return type is the FiniteSet of ordered tuple.
* An ordered tuple of variables to be solved for would be in the input API as well.
* Solution will be returned in the same order.

(For Linear Systems, we can have a general linear solver) 
```python
In [0] linsolve([x + y == 1, x - y == 0], (x,y))
Out[1] {(1/2, 1/2)}   # FinteSet of ordered tuple.

In []: linsolve([3*x + 2*y - z - 1, 2*x - 2*y + 4*z == -2, -x + (1/2)*y - z], (x, y, z)) 
Out[]: {(1, -2, -2)}

# Input can be Matrix as well

In []: M = Matrix([[1,2,0],[3,-4,1]])

In []: linsolve(M, (x, y))
Out[]: {(1/5, -1/10)}

In[]: M = Matrix([[-3, 2, -6, 6], [5, 7, -5, 6], [1, 4, -2, 8]])

In []: linsolve(M, (x, y, z))
Out[]: {(-2, 3, 1)}
```

* Method to convert system of Equations to Matrix Form:
(Convenience Method)

```python
In []: A, b = eq_to_matrix([3*x + 2*y - z ==  1, 2*x - 2*y + 4*z == -2, -x + (1/2)*y - z == 0], [x, y, z])

In []: A
Out[4]: 
Matrix([
[3, 2, -1],
[2, -2, 4],
[-1, 1/2, -1]])

In []: b
Out[8]: 
Matrix([
[1],
[-2],
[0]])

```

#### III. Solving Transcendental Equations
(Equations solvable by LambertW function)


```python
In []: solveset(x + log(x))
Out[]: {LambertW(1)}

In []: solveset(x + exp(x**2), x)
Out[]: {I*sqrt(LambertW(-2)/2)}

In []: solveset(2**x - 5*x, x)
Out[]:-LambertW(-ln(2)/5)/ln(2))
```

To solve equations involving exponents, the trick is to get the variables all on the right side, and then manipulate the right side until the equation pattern matches to `a = b*exp(b)`, & then apply LambertW on both sides.

* An Illustration of solving the Equation `x + exp(x**2) = 0` by hand so that it can be used in Heuristics:

```python
x + exp(x**2) = 0
1 = -x*exp(-x**2)

# Squaring both sides
1 = (x**2)*(exp(-2*x**2))

# Multiply by -2 on both sides
-2 = (-2*x**2)*(exp(-2*x**2))

# Taking LambertW on both sides:
LambertW(-2) = LambertW((-2*x**2)*(exp(-2*x**2)))

# Using the result LambertW of ('something' times exponential of 'something') is 'something' (See Result above in LambertW notes): 
LambertW(-2) = -2*x**2

x = I*sqrt(LambertW(-2)/2)  # Answer!
```


#### IV. Basic Structure for Hint System

The structure of the Hint System will be borrowing some ideas from SymPy’s ODE module. **`solveset`** will try to Rewrite as well as Decompose an Equation to a classifiable form so as to pattern match an equation to identify which type of Equation it belongs to and call various solver routines for solving the Equation. A variation from the `ODE` module is that it may require numerous hints to solve an Equation, following is a pseudo-code representation of the rough structure:.


```python
def solveset(f):

preprocess_function(f)  # Pre-processing of Equation takes place here.

hint = classify_solver()
# Required solver will be called based on the hints returned by classify_solve()
# The hints can be linear, poly, linear_trig, transcendental, etc 

solve_<hint>(f)

# This process is repeated until the equation is trivially solved
```

```python
def preprocess_function(f)
# Pre - processing the Equation, which involves routines for 
# Rewriting the Equation in a form which makes it easier to solve, and
# Decomposition of function to simpler functions, as mentioned in 
# the example above in the 'Basic Idea'
```

```python
def classify_solve(f):

# Matching the given function with various solvers.
# This will return the type of hint used to solve the equation.
```

```
def linsolve(f):

# Routine to solve linear system of Equations
```

```
def solve_transc(f):

# Routine to solve transcendental Equations
```

```
def solve_poly(f):

# Routine to solve polynomial Equations

:

:

and so on..
```
This structure will provide a convenient and user friendly way for adding new solvers and hence making it more robust and modular.


#### V. Multivariate Equation solving:

* For solving multivariate equations, the order of variables should be given as input, so that we don't need to return dict of variable and value.
* We can return consistent Set output using `ProductSet`.
* Here also the order of variables entered in the input will decide the order of variable set in the `ProductSet`.
* If the Equation has more variables than equation, then the variable to be solved for will be returned in terms of other dependent symbols in the Equation.  

1). Multivariate functions with non point solution:
```python
In [0] solveset((x - 1)*(y - 2), (x, y))
Out[1] {{1} x (-oo, oo), (-oo, oo) x {2}}  # set of ProductSets.
```

2). Multivariate functions with point solutions:

```python
In []: solveset(x**2 + y**2, (x, y))
Out[]: {(1/2, 1/2)}  # FinteSet set of ordered tuple.
```

3) System of Multivariate Equations.

```python
In []: solve([x**2 + 2*y - 9, 2*x - y - 1 ], (x, y))
Out[]: {(-2 + sqrt(15), -5 + 2*sqrt(15)), (-sqrt(15) - 2, -2*sqrt(15) - 5)}   # FinteSet set of ordered tuple.

In []: solveset([1/x + y - 1, 2*y + x -3], (x, y)])
Out[]: {(-1, 2), (2, 1/2)}
```

#### VI. Implementing new Algorithms

In `sympy.calculus`

##### 1. Singularities

> In general, a singularity is a point at which an equation, surface, etc., blows up or becomes degenerate. Singularities are often also called singular points.

As of now the singularities submodule in sympy.calculus.singularities supports only rational functions. I would extend this for more general usage, though we can't have a General Singularity finder, as for that we would need a perfect solver & that is an Ideal situation. This function is implemented in popular Computer Algebra Systems as `singular()` in Maple and `Singularity()` in Mathematica as well.

`Singularities` function is heavily dependent on the `solve`.

The User API is given below:

Arguments:
* Function
* Variable
* Range (optional)

```
In []: singularities(1/(x - 1), x)
Out[]: {1}

In []: singularities(ln(x)/(x**2 - 1), x)
Out[]: {-1, 0, 1}

In []: singularities(tan(x), x, Interval(0, 2*S.pi))
Out[]: {π/2, 3π/2}

In []: singularities((x - 1)/sin(x - 2))
Out[]: {2}
```

##### 2. General Methods in Differential Calculus

Calculus techniques can be applied to a wide variety of problems in real life. Quite Often, we construct a function
as a mathematical model of some problem and then analyze the function and its derivatives to gain information about the original problem.
To know about the nature of function in an Interval, it's quite important to know it's monotonicity, and having methods like is_increasing(), is_decreasing(), is_monotonic(), etc can be pretty useful.

* `is_monotonic()`

**A monotonic function is a function which is either entirely nonincreasing or nondecreasing.** <br />
Note: Domain should be specified in all these methods in the API.

```python
In [1]: (log(x)).is_monotonic(Interval(0, oo))
Out[1]: True

In []: fn = ((x - 1)**2)

In []: fn.is_monotonic(Interval(-oo, oo))
Out[]: False
```

* `is_increasing() `


**A function `f(x)` increases on an interval I if `f(b) >= f(a)` for all `b > a`, where `a, b` in I.**
```python
In [1]: (sin(x)).is_increasing(Interval(0, S.pi/2))
Out[1]: True

In [1]: (sin(x)).is_increasing(Interval(S.pi/2, S.pi))
Out[1]: False
```


* `is_strictly_increasing()`

**If `f(b) > f(a)` for all `b > a`, the function is said to be strictly increasing.**

```python
In [1]: (x**3).is_strictly_increasing(Interval(0, oo))
Out[1]: True

In [1]: (S(2))is_strictly_increasing(Interval(0, oo))
Out[1]: False
```

* `is_decreasing()`

**A function `f(x)` decreases on an interval I if `f(b) <= f(a)` for all `b > a`, where `a, b` in I.**

```python
In [1]: (cos(x)).is_decreasing(Interval(0, S.pi))
Out[1]: True

In [1]: cos(x).is_decreasing(Interval(S.pi, 2*S.pi))
Out[1]: False
```

* `is_strictly_decreasing()`

**If `f(b) < f(a)` for all `b > a`, the function is said to be strictly decreasing.**

```python
In [1]: (Abs(x)).is_strictly_decreasing(Interval(-10, 0))
Out[1]: True

In [1]: (Abs(x)).is_strictly_decreasing(Interval(0, 5)
Out[1]: False
```

-----------------

## Timeline
I will have my exams till 3rd week of May, thereafter I will start right away. As far as Community bonding is concerned, I already have been working with SymPy for around 4 months now, So I am quite familiar with the Development Workflow. My college will restarts on the second week of August, So I will have no problem in contributing full time during this period.

#### Community Bonding Period & Week 1
* Create Complex Set (Plane) Class.
* Add Methods for Intersection and Union
* Sets to Boolean & Boolean to set Transformations for multivariate sets.
* Submit the first PR.

#### Week 2
* Start working on creating a General Linear System solver in `solveset`.
* Submit a PR. 

#### Week 3 & 4
* Implement Transcendental Equations solver using LambertW function.
* Submit a PR.

#### Week 5 & 6
Work on 
* Creating the Basic structure for Rewriting and Decomposition Framework, as mentioned above in the Basic Idea.
* Create solver classification function and helper functions. <br />
(Note: The Linear system solver and LambertW Solver are more concrete problems, that's the reason they would be implemented before this, as suggested by @hargup)

#### Week 7 & 8
Start working on
* Multivariate Equation solver in `solveset`
  * Single Multivariate Equation
  * System of Multivariate Equation
  * Submit a PR.

#### Week 9
Since `solveset` is still in sandbox mode, to finally help it end up as a default solver in the sympy.solvers, we need to replace all `solve` internal calls with `solveset`. There over 400 `solve` calls currently, thanks to Harsh for finding [this](https://gist.github.com/hargup/9468786).
* Relevant Issue: [#8711](https://github.com/sympy/sympy/issues/8711)
* Submit a PR.

#### Week 10 & 11
* Creating a Singularity Finder.
* Submit a PR.

#### Week 12
* Work on Creating General Differential Calculus Methods
  * `is_monotonic()`
  * `is_increasing ()` 
  * `is_strictly_increasing() `
  * `is_decreasing ()`
  * `is_strictly_decreasing() `


#### Week 13
* Buffer Period.
* Fix Bugs.
* Report Issue for further work on solvers.


#### Any Plans/Commitment (During GSoC)
* I have no major commitments for this summer and I am positive that I will be able to contribute for about 40-50 hours a week for the project. This project at will form the core of all my working and learning throughout the Summer.
* I will be maintaining a Blog(weekly) at [blog.iamit.in](http://www.iamit.in/blog), to keep track of my progress & also to get feedback from the community.

#### Future Plans (After GSoC)
* Sympy is pretty close to my Interests as well as my Academics, I am looking forward for a long term association with Sympy Community.
* I plan to actively maintain my code and do Bug-fixing/Reviewing in SymPy even after my GSoC time period is over.

# References
* [1] Mailing List Discussion: [https://groups.google.com/forum/#!topic/sympy/_PbRL7QNbqk](https://groups.google.com/forum/#!topic/sympy/_PbRL7QNbqk)
* [2] Harsh Gupta's [GSoC Application](https://github.com/sympy/sympy/wiki/GSoC-2014-Application-Harsh-Gupta%3A-Solvers)
* [3] [Issue #7482](https://github.com/sympy/sympy/issues/7482) : Implement sets to Boolean and Boolean to set transformations for multidimensional/multivariate sets and Boolean
* [4] [Issue #6659](https://github.com/sympy/sympy/issues/6659) : solve() is a giant mess
* [5] [On the Lambert W Function](http://www.apmaths.uwo.ca/~djeffrey/Offprints/W-adv-cm.pdf)
* [6] [Lambert's W Function in Maple](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.33.2556&rep=rep1&type=pdf)
* [7] [Using the Lambert W Function, a.k.a. ProductLog](http://2000clicks.com/mathhelp/BasicSimplifyingLambertWFunction.aspx)
* [8] [General Linear Solve](https://github.com/sympy/sympy/pull/2580)
* [9] [Convert from a system of linear equations to a matrix](https://groups.google.com/forum/#!topic/sympy/Wqs1OhTBexg/discussion)
* [10] [MathWorks: Convert set of linear equations to matrix form](http://in.mathworks.com/help/symbolic/equationstomatrix.html)
* [11] [find singularities for any expression @smichr](https://github.com/sympy/sympy/pull/2925)
* [12] [Complex Interval Arithmetic with some Applications](http://interval.louisiana.edu/Moores_early_papers/Boche_complex.pdf)
* [13] [Complex interval arithmetic using polar form](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.101.9298&rep=rep1&type=pdf)
* [14] [Implementation of Equation Solvers](https://groups.google.com/forum/#!msg/sympy/42GdMJ9ssyM/swC6bHVunP8J)
* [15] [Solution of Linear Systems](http://www.mathcs.emory.edu/~haber/math315/chap3.pdf)
* [16] [LambertW Simplifications](https://github.com/sympy/sympy/issues/5080)
