# current situation

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/wiki/UD-series-situation
**Scraped:** 2026-02-22T23:28:47.572998

---

# UD - Function expansions and series - current situation and applications

<p>&nbsp;</p>

**Note:** these are just the ideas of one person. It may not necessarily
  coincide with the ideas of others in the community.

**Note:** For GSoC, it doesn't have to be this way. On the contrary, we
  welcome the participants to describe their own ideas.

<p>&nbsp;</p>

# Usage and applications

## Series
- In some cases it is easier to work with series, while processing with original function is difficult or impossible symbolically.
- One can use formal power series to prove several relations familiar from analysis in a purely algebraic setting.
- Some ODE can be solved by consideration of the desired result as formal series. Some recurrence formula for series coefficients can be obtained.
- limits

## Asymptotic expansion

- Asymptotic expansions through series is used for approximation of functions. In some cases it is easier to work with truncated series, while processing with original function is difficult or impossible.
- Some ODE, Integral equations can be solved by consideration of the desired result as asymptotic expansions.

## Generating function

- Find a closed formula for a sequence given in a recurrence relation.
- Find recurrence relations for sequences — the form of a generating function may suggest a recurrence formula.
- Define function through sequence.
- Discrete representation of function.

## Common tasks
- Calculate items of sequences by recurrent formula

# Current situation


## The series exist in SymPy now.

A lot of work was done about it over the past years (without any of GCoS
project, so directly).

In this approach the series are treated (represented) as the ordinary
SymPy expressions, that is as `Add` object of terms and O(x).
It is bases on differentiation of expression (Taylor series definition),
and closely related with limits (Gruntz algorithms).

### Advantages:

- A *large* volume of tests was accumulated now. You can see them, e.g.
in the [test_nseries.py](https://github.com/sympy/sympy/blob/master/sympy/series/tests/test_nseries.py) file [4].

- A large volume of complex cases was accumulated or discussed: how to
deal with complex series (logs, x/sin(x), cases with point other then
zero, how it is related with complex limits, and singularities problems.

- As series are represented as ordinary SymPy expression, then we can
use them in further manipulation straightway and freely. E.g. we can
just right to aplly the multiplication or differentiation operations to
the result without additional efforts (only care with Order object).

- And university: we don't care about the kinds and about the types of
series.

They can be Taylor or Power (exponention generating function or ordinary
generating function), Laurent  (with negative powers) or not,
Generalised (with rational or complex powers, or with common
coefficient or with powers log(x) ). See [5] for details.

This is advantage (university) but at the same time it is and
disadvantage too, because it hard to understand what kind of series is
resulted and apply one algorithm or another.

### Disadvantages:

- As internal representation is the ordinary SymPy expression there is
no internal structure. So it is hard or ineffectively to parse this
expression and use it for the internal series calculation, operate only
with coefficients, determine kind of series.
- impossibility to operate with the infinity series.
- We meet the problems of mixing of topics: series (without Order term),
series expansions (with Order term), and formal series (it is differ
from ordinary expression mathematically)
- Minor: Grunz use series  for limits calculation, and series algorithm
use limits to calculate terms.


## 3. polys/ring_series

This is Mario Pernici  [current implementation of power series, wich is in SymPy](https://github.com/sympy/sympy/blob/master/sympy/polys/ring_series.py) with the help of poly rings.

### Advantages:

- See advantages below (of Lpoly2)



## 3. The Lpoly2 Distributed polynomials in series.

It is the work of Mario Pernici which is upon review process now.
See [pull request 609](https://github.com/sympy/sympy/pull/609) for details [3].

This approach is based on the internal representation of series as the
polynomials, that is it has the structure.

More over, it is based on multivariate polynomials!! (not only with x,
but with x, y, z...).

We can convert it to the ordinary expression with the help of `truncate`
method.

### Advantages:

- has a structure, that is implementation is operated with the
coefficients internally and don't parse expression every time. So it is
faster.
- Has specified algorithms, So it is meaningfully faster.
- Order term is separated. So, formally we can don't care about this
term, if we are inside the frame of structure. It arises just for the
final result representation.
- multivariate polynomials. We can expand series in a few variable.
- Typed fields (rings) of coefficient are implemented (QQ, RR), on which
coefficient can belong to.
- A large volume of tests was accumulated too.

### Disadvantages:

- It can be extended, of course, but as it is based on polynomials, so
it is a question how to deal with generalised series like: `1 + x*log(x) + x**2*log(x)**2 + ...`

Mario Pernici can add if it is omitted something.


## 3. Series-prototype:

See [2] for details.
Internal structure is based upon of sequences (for one variable).

And there is the difference of algorithms for series calculation.
We construct the symbolic expression which consist of series objects
(and internally use sequences expressions) , so we do not calculate every
time the coefficients while work with expression of series - only when
we want to see coefficient, and use calculations with only the terms
which are needed.

Of courses for multivariate another structure must be used instead of
sequences, but the main approach still remains (expression of series,
use only terms which are needed only)

### Advantages:

- has a structure (as Lpoly2 approach too)
- sequences are things in itself, it can be uses independently in SymPy,
there is why I separated it.
- sequences can be classified, so the algorithms for some primitive
sequences can be specified and simplify the calculations.
- separated types of series (don't mix Formal Taylor series and Formal
Power series).


### Disadvantages:

- not multivariate yet (but it can be extended)
- there is no accumulated enough volume of cases and tests, so it is
possible that the unknown limitations are. It is main disadvantages
which I care about now.

But I must notice that this approach intersected with Lpoly2 in some
place: if we use finite sequence then it is similar like the ordinary
polynomial.


## There are some more references

Which are mentioned in "Series expansions" section of GCoS Ideas [1].
Which can be used for the road-map construction. In particular:

- "Formal Power Series" by Dominik Gruntz and Wolfram Koepf
- "A New Algorithm Computing for Asymptotic Series" by Dominik Gruntz
- "Computing limits of Sequences" by Manuel Kauers
- "Symbolic Asymptotics: Functions of Two Variables, Implicit Functions"
by Bruno Savly and John Shackell
- "Symbolic Asymptotics: Multiseries of Inverse Functions" by Bruno
Savly and John Shackell


## Conclusion

a) I think we can combine all those approaches. But taking into account
the next:

b) That we must to design the road-map in more details.
The main (far away) target directions which I see (except combining of
the above) are:

- Use various kinds of series (Formal Power series). They have different
properties and algorithms, it is the reason why.
- Separate series expansion concept (with Order term) from series itself
(infinite).
- Combine them with generating functions concept.
- A lot of other topics which must be formulated.


## About series which is work in SymPy now.

[relevant issues](http://code.google.com/p/sympy/issues/list?q=label:Series)

- According to its docstring, ``f(x).series(x, x0, n)`` is supposed to return the (n-1)th order generalized Taylor expansion of \(f(x)\) for \(x \rightarrow x_0\).
Actually, it works only for \(x_0 = 0\) and when f doesn't have a generalized Taylor expansion, it returns some arbitrarily chosen asymptotic expansion of \(f(x)\).

- But the present method "series" which returns various kinds of series is convenient and used for the task of limits processing: limits use necessary amount of first terms of series whatever it be.
The work with processing of many various cases of series and limits was executed recently, also many tests have been collected and passed for series and limits.

- Class *Function* , *exp* *sin* and others contain method **taylor_term**.

- general algorithm for series() and nseries() consist in that the operations with asymptotic expansion  used through recursion:  F.e: ((sin(x))^1000 ).series() = \( (1 + \frac{x^3}{6} + O(x^4))^1000 = \cdots \).

- There is an object **Sum** defined in sympy, which represent unevaluated summation \( \sum_{k=a}^b a(n) \).

- sympy/solvers/recurr.py contains some methods for solving recurrences, main function on this module is **rsolve()**.

- The implementation of some series methods for solving IDEs is processing now in Saptarshi's branch (https://github.com/saptman/sympy/tree/dev_ide
).


## problems and remarks which we encounter

- Problems with big O representation and behaviour at non zero point or oo.
- representation of Derivative of function at some (no zero) point ([issue 1620](http://code.google.com/p/sympy/issues/detail?id=1620 "issue 1620")).
- representation of composition of functions while differentiation ([issue 1660](http://code.google.com/p/sympy/issues/detail?id=1660 "issue 1660")).
- Not effective algorithm in some cases: now is used that: (cos(x)*(sin(x)).series() = sin(x).series() * cos(x).series(), lseries.next() calculate the nseries(n)  every time  (f.e. fifth next() calculate nseries(5) and after this yield fifth term)
- How to deal with `acosh`, `acoth` - branches ([issue 564](http://code.google.com/p/sympy/issues/detail?id=564 "issue 564"))
- Singularities ([issue 2200](http://code.google.com/p/sympy/issues/detail?id=2200 "issue 2200"))



# Open questions and future topics
- what is exp(1/x).series(x, oo) - classical Laurent or power series at point oo?
- multivariable extension.
- complex numbers, non commutative formal variables.
- split-complex numbers, may be sometimes more convinient to expand in this plane e.g. hyperbolic inverse functions.
- convergence
- singularity and branches


# Links


[1] https://github.com/sympy/sympy/wiki/GSoC-2012-Ideas

[2]
https://github.com/sympy/sympy/wiki/UD-Sequences-and-formal-power-series-prototype

[3] https://github.com/sympy/sympy/pull/609
- [rmpoly](http://code.google.com/p/rmpoly/wiki/Tutorial) - nice Python project, by Mario Pernici. Handling polynomials and series.


[4]
https://github.com/sympy/sympy/blob/master/sympy/series/tests/test_nseries.py

[5] https://github.com/sympy/sympy/wiki/UD-series-definitions

[6] https://github.com/sympy/sympy/wiki/UD-series-situation



# Part-2
At this page we will be concentrated to the end-user's aims of series usage in sympy:

[Sequences-prototype](https://github.com/sympy/sympy/wiki/UD-Sequences-and-formal-power-series-prototype)
