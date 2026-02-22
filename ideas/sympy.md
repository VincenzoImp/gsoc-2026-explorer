# SymPy — Project Ideas

**Source:** https://github.com/sympy/sympy/wiki/GSoC-Ideas
**Scraped:** 2026-02-22T23:28:47.570182

---

# Introduction

This is the list of ideas for students wishing to apply for Google Summer of
Code. For more information on how to apply, see the [GSoC Student
Instructions](/ideas/sympy/gsoc-student-instructions). This list is here for inspiration and to give students an idea
of what directions may be good for SymPy.

If you want to pursue an idea listed here, you should contact us on our
[mailing list](http://groups.google.com/group/sympy) and discuss it. **Be sure
to always ask about these ideas to get the latest information about what is
implemented and what exactly has to be done.**

The order of ideas in this list has no bearing to the chances of an idea to be
accepted. All of them are equally good and your chances depend on the quality
of your application. Also do not worry if there are no mentors assigned to a given idea. If the application is good, we will find a mentor. As already said, you can very well submit your own idea
not listed here.

## Project length

GSoC allows three different project lengths, 90 hours, 175,
hours and 350 hours. The ideas below specify which project length is the best fit.

In some cases, it may be possible to extend a smaller project into a larger one by extending the ideas of what can be done in the project.
Similarly, in some cases a larger project can be shortened by only implementing part of the full idea and leaving the rest for a
future project. In either case, if you want to do this, please discuss it with
us first.

# Submitting Your Own Idea

You can apply with something completely different if you like. The best project
for you is one you are interested in, and are knowledgeable about. That way,
you will be the most successful in your project and have the most fun doing it,
while we will be the most confident in your commitment and your ability to
complete it.

If you do want to suggest your own idea, please [discuss
it](http://groups.google.com/group/sympy) with us first, so we can determine if
it is already been implemented, if it is enough work to constitute a summer's
worth of coding, if it is not too much work, and if it is within the scope of
our project.

Please be aware that some ideas are specifically [out of scope for
SymPy](#non-ideas) and may be a better fit for other GSoC organizations. Also
be aware that ideas that propose completely new modules to SymPy are less
likely to be accepted, unless they have already been mentioned on this page or
somewhere in the SymPy issue tracker. This is because most of the things that
are in-scope for SymPy already have at least a partial implementation in a
submodule in SymPy. However, many of these things are not fleshed out very
well yet and doing so can often make a good project. If you are unsure, it
doesn't hurt to ask us.

# Potential Mentors

If you are willing to mentor, please add yourself here. Also please register at
https://summerofcode.withgoogle.com and add your email that you registered
with. Finally, list your name with any
projects below that you would be willing to mentor.

(Note from Aaron, the org admin: if your name is on this list, I'm assuming
you're willing to either mentor or at least help review applications. If you
aren't able to help this year, please remove your name from the list. If you
have any questions about mentoring feel free to email me.)

* Aaron Meurer - asmeurer@gmail.com
* Advait Pote - apote2050@gmail.com (for `sympy.physics.continuum_mechanics`)
* Akshansh Bhatt - qaz.akshansh@gmail.com (for `sympy.physics.control`)
* Amit Kumar - dtu.amit@gmail.com (for `sympy.solvers`)
* Anurag Bhat - anuragbhatgsoc23@gmail.com
* Anutosh Bhat - anutosh.bhat.21@gmail.com (for `sympy.series`, `sympy.concrete`)
* Faisal Riyaz - faisalriyaz011@gmail.com
* Francesco Bonazzi - franz.bonazzi@gmail.com
* Hwayeon Kang - hwayeonniii@gmail.com (for `sympy.physics.mechanics`)
* Ishan Joshi - ishanaj98@gmail.com
* Ishan Pandhare - ishan9096137017@gmail.com
* Jason Moore - moorepants@gmail.com (physics.vector/mechanics/biomechanics, parsing.autolev, utilities.autowrap/codegen/lambdify)
* Mohit Balwani - mohitbalwani.ict17@gmail.com (for `sympy.solvers.ode`)
* Mohit Gupta - mohitgupta6678@gmail.com
* Naman Gera - namangera15@gmail.com (for `sympy.physics`)
* Naveen Sai - naveensaisreenivas@gmail.com
* Nijso Beishuizen - nijso.beishuizen@gmail.com (for ode and pde solvers)
* Nikhil Maan - nikhilmaan22@gmail.com
* Oscar Benjamin - oscar.j.benjamin@gmail.com
* Peter Stahlecker - peter.stahlecker@gmail.com (for `sympy.physics.mechanics` (Kane's method)`)
* Prakhar Saxena - prakharrsaxena@gmail.com (for `sympy.physics.continuum_mechanics`)
* Sachin Agarwal - sachinagarwal0499@gmail.com (for `sympy.series`)
* Sidharth Mundhra - sidharthmundhra16@gmail.com (for 'sympy.series')
* Smit Lunagariya - smitplunagariya@gmail.com
* Sudeep Sidhu - sudeepmanilsidhu@gmail.com (physics.vector/mechanics)
* Tilo Reneau-Cardoso - tiloreneau@gmail.com (for `sympy.assumptions`)
* Timo Stienstra - timostienstra00@gmail.com (for `sympy.physics.mechanics`/`vector`/`biomechanics`)
* Tom van Woudenberg - tom.van.woudenberg@gmail.com (for `sympy.physics.continuum_mechanics`)
* Yathartha Joshi - yathartha32@gmail.com
* Rushabh Mehta - mehtarushabh2005@gmail.com (for `sympy.physics.mechanics` (Wrapping Geometries))
* Sai Udayagiri - saibabu.udayagiri@gmail.com (for `sympy.physics.continuum_mechanics`)
* Leonardo Mangani - leomangani4@gmail.com (for `sympy.physics.control`)

# Table of Contents

<!-- Generate the TOC below with (https://github.com/thlorenz/doctoc):

doctoc --title " " GSoC-Ideas.md

-->

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [High Priority](#high-priority)
  - [Polynomial GCD](#polynomial-gcd)
  - [Benchmarks and performance](#benchmarks-and-performance)
  - [Assumptions](#assumptions)
- [Mathematics Projects](#mathematics-projects)
  - [Solvers](#solvers)
  - [Optimize floating point expressions](#optimize-floating-point-expressions)
  - [Group theory](#group-theory)
  - [Risch algorithm for symbolic integration](#risch-algorithm-for-symbolic-integration)
  - [Rule-based symbolic integration](#rule-based-symbolic-integration)
  - [ODE ideas](#ode-ideas)
  - [Improving Series Expansions & Limit Computations](#improving-series-expansions--limit-computations)
  - [Cylindrical algebraic decomposition](#cylindrical-algebraic-decomposition)
  - [Efficient Groebner bases and their applications](#efficient-groebner-bases-and-their-applications)
  - [Multivariate polynomials and factorization](#multivariate-polynomials-and-factorization)
  - [Univariate polynomials over algebraic domains](#univariate-polynomials-over-algebraic-domains)
  - [Concrete module: Implement Karr algorithm, a decision procedure for symbolic summation](#concrete-module-implement-karr-algorithm-a-decision-procedure-for-symbolic-summation)
- [Physics Projects](#physics-projects)
  - [Symbolic Control Systems (`sympy.physics.control`)](#symbolic-control-systems-sympyphysicscontrol)
  - [Symbolic quantum mechanics (`sympy.physics.quantum`)](#symbolic-quantum-mechanics-sympyphysicsquantum)
  - [Continuum Mechanics: Create a Rich 2D Beam Solving System](#continuum-mechanics-create-a-rich-2d-beam-solving-system)
  - [Classical Mechanics](#classical-mechanics)
  - [Classical Mechanics: Generalize the Equations of Motion System Output](#classical-mechanics-generalize-the-equations-of-motion-system-output)
  - [Classical Mechanics: Implement and Benchmark Equations of Motion Methods](#classical-mechanics-implement-and-benchmark-equations-of-motion-methods)
  - [Classical Mechanics: Efficient Equations of Motion Generation](#classical-mechanics-efficient-equations-of-motion-generation)
  - [Classical Mechanics: Implement Wrapping Geometry and Pathways for Musculoskeletal Modeling](#classical-mechanics-implement-wrapping-geometry-and-pathways-for-musculoskeletal-modeling)
  - [Classical Mechanics: Implement Specific Forces and Torques](#classical-mechanics-implement-specific-forces-and-torques)
  - [Classical Mechanics: Constructing Systems From Bodies and Joints](#classical-mechanics-constructing-systems-from-bodies-and-joints)
  - [Classical Mechanics: Implement an O(N) Equations of Motion Method](#classical-mechanics-implement-an-on-equations-of-motion-method)
- [Computer Science, Graphics, and Infrastructure Projects](#computer-science-graphics-and-infrastructure-projects)
  - [Enhancing the flexibility of MatchPy](#enhancing-the-flexibility-of-matchpy)
  - [Code Generation](#code-generation)
  - [Code Generation: Efficient Jacobian and Hessian Evaluation for Optimization and ODE Integration](#code-generation-efficient-jacobian-and-hessian-evaluation-for-optimization-and-ode-integration)
  - [Improve the LaTeX Parser for SymPy](https://github.com/sympy/sympy/wiki/GSoC-Ideas#improve-the-lark-based-latex-parser)
  - [Parsing](#parsing)
  - [Improve the plotting module](#improve-the-plotting-module)
  - [Documentation tooling](#documentation-tooling)
  - [Hypothesis testing](#hypothesis-testing)
- [User Application Projects](#user-application-projects)
- [LFortran SymPy Project Ideas](#lfortran-sympy-project-ideas)
  - [SymPy -> Fortran Code Generation and JIT](#sympy---fortran-code-generation-and-jit)
  - [Parsing Fortran code to SymPy](#parsing-fortran-code-to-sympy)
- [Idea Prompts](#idea-prompts)
- [Other Related Projects](#other-related-projects)
- [Non-Ideas](#non-ideas)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


**Mentors, please use the following template to add ideas to this page:**

```
## Title

**Idea**

(Specify your idea with proper explanation)

**Status**

(What is the Status of this Idea in the Sympy Community currently, previous
work done and Issues)

**Involved Software**

(Any other Software Involved that would be required to implement your idea)

**Difficulty**

(Advanced, Intermediate, or Beginner and any specific comments on the
difficulty)

**Prerequisite Knowledge**

(Any prerequisite knowledge or approach needed)

**Project Length**

Whether this project is appropriate for a 90, 175, or 350 hours GSoC project.
The same idea can have different project length sub-ideas.

NOTE: This section is required by Google. Be sure to include it for
any idea!
```

# High Priority

## Polynomial GCD

**Idea**

Add new algorithms for computing the greatest common divisor (GCD) of polynomials in the sparse representation. This would improve the speed of many parts of sympy such as matrices, solvers, integration and so on.

The issues and potential solutions along with many references are discussed in this issue:
https://github.com/sympy/sympy/issues/23131

**Status**

There is plenty of work that can be done in this area so this is effectively an open-ended area for improvement in sympy.

**Involved Software**

**Difficulty**

Medium to high difficulty

**Prerequisite Knowledge**

Python, some understanding of abstract algebra and of algorithms.

**Project Length**

175 or 350 hours, depending on the scope of the project.

## Benchmarks and performance

**Idea**

Speed is important for SymPy. One issue is that it's difficult to tell what is
too slow, and, more importantly, if a given change makes things faster or
slower.

SymPy needs more benchmarks. It also needs an automated system to run them.
That way, when someone adds some code that slows things down in an unexpected
way, we will know about it.

There are already some benchmarks at
https://github.com/sympy/sympy_benchmarks, and some others in the main SymPy
repo. But not all benchmarks are in the sympy_benchmarks repo. Also, the repo
uses asv, but the results are run and hosted *ad hoc*, as we don't have a
dedicated machine to run the benchmarks.

This project should do the following:

- Move benchmarks from the sympy repo to the sympy_benchmarks repo.
- Add new benchmarks as needed.
- Work with the community to set up a dedicated machine that can constantly
  run asv to warn about benchmarks. It would also be nice if this could be set
  up to warn for performance regressions on PRs.
- Make improvements to SymPy to improve performance issues found
  throughout the project.
- Improve the usability of the current GitHub Actions bot that adds benchmarks outputs to pull requests.

Some prior art:

- ASV (what we are using now)
- PyPy benchmarks page
- See https://www.youtube.com/watch?v=d65dCD3VH9Q for some ideas/warnings
  about setting up benchmarking.
- See this issue for ways to run benchmarks on GitHub Actions https://github.com/sympy/sympy/issues/21374.

**Status**

We currently have a benchmarking suite and run the benchmarks on GitHub
Actions, but this is limited and is often buggy.

**Involved Software**

**Difficulty**

Medium to low difficulty

**Prerequisite Knowledge**

Python

**Project Length**

175 hours or 350 hours, depending on the scope of the project.

## Assumptions

**Idea**

The project is to completely remove our old assumptions system, replacing it
with the new one. The difference between the two systems is outlined in the
first two sections of [this blog
post](http://matthewrocklin.com/blog/work/2013/02/05/Assuming).

This project is challenging. It requires deep understanding of the core of
SymPy, basic logical inference, excellent code organization, and attention to
performance.  It is also very important and of high value to the SymPy
community.

Numerous related tasks are mentioned in the "Ideas" section.

**Status**

There has been a significant amount of merged and unmerged work on this topic. A
list of detailed issues can be found at [this
issue](/ideas/sympy/sympy-sympy-issues-6730). You should take
a look at the work started at https://github.com/sympy/sympy/pull/2508.

[This mailing list post](https://groups.google.com/d/msg/sympy/PHR136kdxc4/eW4pKFcWmzIJ) by Aaron Meurer outlines the status of the project and some ideas of what to do. It is from 2015 but most of what is written there is still true. The main thing that is new is that the new assumptions call the old assumptions (`ask(Q.real(Symbol('x', real=True)))`). See also the prior GSoC projects on assumptions, including [this one](/ideas/sympy/gsoc-2015-application-sudhanshu-mishra-assumptions), which was accepted, but there may be parts of it that were not completed, and https://github.com/sympy/sympy/wiki/GSoC-2013-Application-Tom-Bachmann:-Removing-the-old-assumptions-module, which was not accepted (the student chose to do another project), but contains some good ideas.

**Involved Software**

None

**Difficulty**

Advanced

**Prerequisite Knowledge**

Number theory, Boolean algebra, etc.

**Project Length**

350 hours

# Mathematics Projects

## Solvers

**Idea**

SymPy already has a pretty powerful `solve` function. But it has a lot of major
issues

1. It doesn't have a consistent output for various types of solutions
   It needs to return a lot of types of solutions consistently:
   * single solution : ` x == 1`
   * Multiple solutions: `x**2 == 1`
   * No Solution: `x**2 + 1 == 0; x is real`
   * Interval of solution: `floor(x) == 0`
   * Infinitely many solutions: `sin(x) == 0`
   * Multivariate functions with point solutions `x**2 + y**2 == 0`
   * Multivariate functions with non point solution `x**2 + y**2 == 1`
   * System of equations `x + y == 1` and `x - y == 0`
   * Relational `x > 0`
   * And the most important case "We don't Know"

2. The input API is also a mess, there are a lot of parameter. Many of them
   are not needed and they makes it hard for the user and the developers to
   work on solvers.

3. There are cases like finding the maxima and minima of function using
   critical points where it is important to know if it has returned all the
   solutions. `solve` does not guarantee this.

**Salient Features of `solveset`**

* `solveset` has a cleaner input and output interface: `solveset` returns a set
  object and a set object take care of all the types of the output. For cases
  where it doesn't "know" all the solutions a `NotImplementedError` is raised.
  For input only takes the equation and the variables for which the equations
  has to be solved.

* `solveset` can return infinitely many solutions. For example solving for
  `sin(x) = 0` returns {2⋅n⋅π | n ∊ ℤ} ∪ {2⋅n⋅π + π | n ∊ ℤ} Whereas `solve`
  only returns [0, π]

* There is a clear code level and interface level separation between solvers
  for equations in complex domain and equations in real domain. For example
  solving `exp(x) = 1` when x is complex returns the set of all solutions that
  is {2⋅n⋅ⅈ⋅π | n ∊ ℤ} . Whereas if x is a real symbol then only {0} is
  returned.

* `solveset` returns a solution only when it can guarantee that it is returning
  all the solutions.

**Status**

**[GSoC 2014 Project: Harsh Gupta](/ideas/sympy/gsoc-2014-application-harsh-gupta-solvers)**
During the summer of 2014 Harsh Gupta worked to improve solvers as part of his
GSoC project. Instead of making changes in the current `solve` function a new
submodule named `solveset` was written.

**[GSoC 2015 Project: Amit Kumar](/ideas/sympy/gsoc-2015-application-amit-kumar-solvers-extending-solveset)**
In the summer of 2015 Amit Kumar worked on this project to improve solveset, implement complex sets as a part of his GSoC project.

**[GSoC 2016 Project: Kshitij SaraogiKshitij Saraogi](https://docs.google.com/document/d/1GljN3hj_qDzMvTAUW2X7idcsoDPhJ0uAqmMrqykSGGg/edit?usp=sharing) | [GSoC 2016 Project: Shekhar Rajak](/ideas/sympy/gsoc-2016-shekhar-prasad-rajak-application-solvers-completing-solveset)**
In the summer of 2016, two projects were selected to participate in Google Summer of Code to work on the Solvers.
New solver helper functions such as `solve_decomposition` and `nonlinsolve` were implemented to facilitate the porting from `solve` to `solveset`. Also, the inequality solver `solve_univariate_inequality` was refactored and added to `solveset`. Several methods related to functional analysis, such as `periodicty`, `continuous_domain` and `function_range` were implemented.

**[GSoC 2018 Project: Yathartha Joshi](https://docs.google.com/document/d/1kcZCdQuY3XxgHPuSA8vvwc6O8AbVZ-nYskMuXIia9hA/edit#)**
In the summer of 2018, Yathartha worked on the project to implement transcendental equation solver for `solveset`. `transolve` alongwith its helper solvers was implemented as a result of it.

**TODOs**

* Extending `transolve`:
As part of the work done in the summer of 2018, `transolve` is fully designed and is now able to handle logarithmic and exponential equations for `solveset`. To make `solveset` fully fledged and replace `solve` completely we expect it to handle equations like:
     * Lambert type equations (PR [#14972](https://github.com/sympy/sympy/pull/14972))
     * Handling modular equations ([#13178](/ideas/sympy/sympy-sympy-issues-13178))
     * Solving transcendental equations in complex domain.

     There may be other types of equations that `transolve` can be made to handle. It's still under development!! Feel free to propose any of your ideas.

* Integrating helper solvers with `solveset`:
Currently, `solveset` only solves a single equation for a single variable. In the future, we expect it to be capable of solving a system of equations and for more than one variable.
`linsolve`: Solves a system of linear equations
`nonlinsolve`: Solves a system of non-linear equations
`solve_decomposition`: Solves a varied class of equations using the concept of Rewriting and Decomposition
These are the helper functions that have been implemented in `solveset` during the past few years. We would like to have all these solvers(including `transolve`) to be integrating in `solveset` so as to increase its power.

* Build the set infrastructure: This includes implementing functions to handle
  multidimensional ImageSet etc., This part must go hand in hand with the
  improvements in the solvers as set module can be a universe in itself. Also
  there can be fundamental limits on the things you can do.

* `nonlinsolve` is not able to handle system having trigonometric/transcendental equations correctly all the time. Improve solveset's trigonometric solver and handle trig system of equations separately in `nonlinsolve`.


**References**
There had been a lot of discussion during and before the project and you should
know why we did what we did. Here are some links:

* [Discussion on the mailing list](https://groups.google.com/forum/#!searchin/sympy/solvers/sympy/Oyz8SkR2fRk/RMpooqwu3oMJ)
* [Action Plan on solvers](https://github.com/sympy/sympy/pull/2948)
* [Harsh Gupta's proposal for GSoC 2014](/ideas/sympy/gsoc-2014-application-harsh-gupta-solvers)
* [Harsh's blog for GSoC](http://hargup.github.io/categories/sympy.html)
* [solveset pull request](https://github.com/sympy/sympy/pull/7523)
* [Amit's blog for GSoC](http://iamit.in/blog/)
* [Solveset Documentation](/ideas/sympy/sympy-sympy-blob-master-doc-src-modules-solvers-solveset)
* [GSoC 2016 Solvers Progress and blog links](/ideas/sympy/gsoc-2016-solvers-progress)
* [Yathartha's blog for GSoC](https://yathartha22.github.io)
* [transolve pull request](https://github.com/sympy/sympy/pull/14736)
* [GSoC 2018 Solvers Progress](/ideas/sympy/gsoc-2018-solvers-progress)

**Involved Software**

SymPy

**Difficulty**

This project is difficult because it requires a good deal of thought in the
application period. You should have a clear plan of most of what you plan to do
in your application: waiting until the Summer to do the designing will not
work.

[#10006](/ideas/sympy/sympy-sympy-issues-10006) and
[#8711](https://github.com/sympy/sympy/issues/8711) can be good entry points.

**Prerequisite Knowledge**

Algebraic and differential equations

Potential mentor - Co-mentor: Shekhar (@Shekharrajak)

**Project Length**

350 hours.

## Optimize floating point expressions

**Idea**

Optimize floating point expressions (à la https://herbie.uwplse.org/).
The user will supply a SymPy expression and an optional
range of "x" (and other variables) and the module would determine
which symbolic simplifications make sense to make things more
accurate and/or faster.

Part of this project would also be to provide faster implementations of special
functions, say if it is determined that "x" in sin(x) is in the range [0,
1e-3], then there are much faster polynomial approximations that give the same
accuracy (the same is possible for other finite ranges, e.g., [1.5, 1.7]).

One mode is to concentrate on accuracy (possibly with larger/slower
expression). Another mode is to concentrate on speed, and this mode can have a
user prescribed accuracy, say 1e-16 for machine precision, or 1e-3 for lower
accuracy. For lower accuracies one can replace functions like sin(x) with a
much faster polynomial approximation.

**Difficulty**

Intermediate, Advanced

**Project Length**

350 hours, although you may propose a 175 hour project with a more limited
scope.

## Group theory

**Idea**

Continue developing the group theory functionality of the combinatorics module. You should take a look at the GAP
library, as this is the canonical group theory computation system right now.

Algorithms to think about implementing:

- Computation of various subgroups of infinite finitely presented groups
- Computation of Galois groups for a given polynomial
- Finding kernels of homomorphisms with infinite domains
- Extend functionalities of polycyclic groups
- Quotient groups
- Automorphism groups

**Status**

Previous projects on the topic include:

- [GSoC 2012 Aleksandar Makelov: Computational Group Theory](/ideas/sympy/gsoc-2012-report-aleksandar-makelov-computational-group-theory)
- [GSoC 2016 Gaurav Dhingra: Computational Group Theory](https://gxyd.github.io/blogs/Gsoc2016-project/)
- [GSoC 2017 Valeriia Gladkova: Computational Group Theory](/ideas/sympy/gsoc-2017-report-valeriia-gladkova-group-theory)
- [GSoC 2018 Ravi Charan: Computational Group Theory](https://ravicharann.github.io/blog//final-report/)
- [GSoC 2019 Divyanshu Thakur: Computational Group Theory](/ideas/sympy/gsoc-2019-report-divyanshu-thakur-group-theory)

A good amount of work has been done on polycyclic groups, polycyclic presentation with the base class collector were introduced in 2019 GSoC project but still there are a lot of things to be added for e.g. polycyclic orbit stabilizer and canonical polycyclic sequence to check if two polycylic subgroups are equal or not could be implemented. In addition, few other algorithms like abelian invariants and composition series implemented in 2019 GSoC project can be extended for infinite groups.

Some major algorithms for finitely presented groups include coset enumeration (there's been work on modified Todd-Coxeter in the 2018 GSoC project: see [this PR](https://github.com/sympy/sympy/pull/14830)), low index subgroup search and Reidemeister-Schreier algorithm for subgroup presentation. Rewriting systems together with the Knuth-Bendix completion algorithm are available but could be made more efficient.

Additionally, the 2017 project implemented group homomorphisms and the 2018 project implemented the computation of the isomorphism between 2 groups, an automaton for word reduction and a few additional algorithms. Find the complete work done during 2018 in the project report in the link below.

See the [2016](https://gxyd.github.io/blogs/Gsoc2016-project/), [2017](/ideas/sympy/gsoc-2017-report-valeriia-gladkova-group-theory) and [2019](/ideas/sympy/gsoc-2019-report-divyanshu-thakur-group-theory) reports for suggestions on where the work could continue.

Quite a lot of work has been done on permutation groups, but still, some things remain (some of those mentioned in [GSoC 2012 Report by Aleksandar Makelov](https://github.com/sympy/sympy/wiki/GSoC-2012-Report-Aleksandar-Makelov:-Computational-Group-Theory#after-gsoc) are still relevant, e.g. subgroup intersection). Some work is already done on discrete groups. Nonetheless, there is still much that can be done both for discrete groups and for Lie groups.

**Difficulty**: Medium/Difficult

**Resources**: *Handbook of Computational Group Theory* by *Derek F. Holt*, *Bettina Eick* and *Eamonn A. O'Brien*

**Prerequisite Knowledge**: Basic knowledge of Abstract Algebra

Potential mentor - Co-mentor: Divyanshu Thakur (@divyanshu132)

**Project Length**

350 hours.

## Risch algorithm for symbolic integration

**Idea**

The Risch algorithm is a complete algorithm to integrate any elementary
function.  Given an elementary function, it will either produce an
antiderivative, or prove that none exists.  The algorithm described in
Bronstein's book deals with transcendental functions (functions that do not
have algebraic functions, so ``log(x)`` is transcendental, but ``sqrt(x)`` and
``sqrt(log(x))`` are not).

**Status**

The project is to continue where Aaron Meurer left off in his 2010 GSoC
project, implementing the algorithm from Manuel Bronstein's book, _Symbolic
Integration I:  Transcendental Functions_.  If you want to do this project, be
sure to ask on the mailing list or our IRC channel to get the status of the
current project.

The algorithm has already been partially implemented, but there is plenty of
work remaining to do.  Contact Aaron Meurer for more information. There was
also work done in 2013, which hasn't been completely merged yet. A good place
to start would be to look at finishing this work:
https://github.com/sympy/sympy/pulls/cheatiiit. See
https://groups.google.com/forum/#!msg/sympy/bYHtVOmKEFs/UZoyDX81eP4J for some
more details on this project (nothing has changed since that email thread).

**Involved Software**

**Difficulty**

**Prerequisite Knowledge**

You should have at least a semester's worth of knowledge in abstract algebra.
Knowing more, especially about differential algebra, will be beneficial, as you
will be starting from the middle of a project. Take a look at the first chapter
of Bronstein's book (you should be able to read it for free via Google Books)
and see how much of that you already know. If you are unsure, discuss this
with Aaron Meurer (asmeurer).

**Project Length**

350 hours.

## Rule-based symbolic integration

**Idea**

Symbolic integration can also be performed with a "rule-based" system, which
pattern matches the integrand against a set of known integrals uses them to
return a result. This is a different approach to the Risch algorithm discussed
in the previous approach, and is generally seen as complementary to it. For
instance, the Risch algorithm can handle very complex expressions but it can
only work with elementary integrals. Rule-based systems are limited to
expressions that can match the given set or rules, but it can work with a
large set of special functions.

**Status**

The main work here is a software called [RUBI](https://rulebasedintegration.org/), which is a rule-based
integration system written in Wolfram Language. Several previous GSoC projects
have worked on integrating RUBI in SymPy, but this work has not yet been
successfully completed.

See

- [[GSoC-2017-Report-Abdullah-Javed-Nesar:-Rule-based-Integrator]]
- [GSoC 2018 Rubi Final Report](https://github.com/ashishkg0022/Gsoc-proposal-Rubi/wiki/GSoC-2018-Rubi-Final-Report)
- [[Improving-Rule-Based-Integrator]]
- Tracking issue [#12233](/ideas/sympy/sympy-sympy-issues-12233)

The RUBI code that has been written is now at https://github.com/sympy/rubi.
The primary issue with it is that RUBI is very large and the Python
translation is too slow to be useful.

RUBI also involves using MatchPy (see [Enhancing the flexibility of
MatchPy](#enhancing-the-flexibility-of-matchpy)), which enables the sort of
Mathematica-style pattern matching needed for integration.

Because previous projects have failed to integrate the entirety of RUBI due to
its size, a project working on RUBI should focus on integrating parts of it at
a time.

SymPy also has a separate module called
[manualintegrate](https://github.com/sympy/sympy/blob/master/sympy/integrals/manualintegrate.py)
which implements a pattern-based integration system. It only has a limited of
patterns right now, but could be extended. A potential project could just be
to extend manualintegrate and not involve RUBI.

**Involved Software**

- MatchPy
- RUBI

**Difficulty**

Intermediate to difficult

**Prerequisite Knowledge**

If working on RUBI knowledge of Mathematica code will be useful, but not
required. Prior knowledge of special functions will be useful, but can also
quite easily be learned.

**Project Length**

For anything involving RUBI, this should be 350 hours.

Smaller 175 or even 90 hour projects to just improve manualintegrate are
possible. Discuss with us.

## ODE ideas

You also might want to look at [Manuel Bronstein's sumit](http://www-sop.inria.fr/cafe/Manuel.Bronstein/sumit/index.html).

  * "Solving Differential Equations in Terms of Bessel Functions" by Ruben Debeerst.
(basic idea is [already implemented](https://github.com/sympy/sympy/pull/16581).)
      * Webpage: http://rubendebeerst.de/master/
      * Master Thesis: http://rubendebeerst.de/master/master.pdf
      * Corresponding ISSAC 08 paper: http://rubendebeerst.de/master/paper_issac2008.pdf

  * Lie groups and symmetry related:

      * ["Integrating factors for second order ODEs" by E.S. Cheb-Terrab and A.D. Roche](https://drive.google.com/file/d/1-XktJVEzpRK9nOlaMjE7arEgMgGlV_sN/view?usp=sharing)
      * ["Abel ODEs: Equivalence and Integrable Classes" by E.S. Cheb-Terrab and A.D. Roche](https://drive.google.com/file/d/1XpGRJc6ZQ_ReTgRSBc3_tnToZ-hjCNgS/view?usp=sharing)
        Note: Original version (12 pages): July 1999. Revised version (31 pages): January 2000

**Status**

**Involved Software**

**Difficulty**

Medium

**Prerequisite Knowledge**

Differential equations

**Project Length**

175 hours or 350 hours, depending on the project details (discuss with us).

## Improving Series Expansions & Limit Computations

**Idea**

This includes numerous smaller subprojects and is more of a bug burn down project than implementing things from scratch. Hence we should aim at solving as many bugs and possible issues having the label series or limits on them. There are around **146** open issues with the series label & around **26** open issues with the limits label with some overlap and the proposal should have a comprehensive list of ideas to fix a significant portion of these issues.

  * improve series expansions
    * [relevant issues](/ideas/sympy/sympy-sympy-labels-series)
  * improve limit computations
    * [relevant issues](/ideas/sympy/sympy-sympy-labels-limits)
  * improve formal power series
  * asymptotic series (for instance aseries for gamma, bessel, error type functions)
    * [issue 1](/ideas/sympy/sympy-sympy-issues-26207), [issue 2](/ideas/sympy/sympy-sympy-issues-26208), [issue 3](/ideas/sympy/sympy-sympy-issues-26210), [issue 4](/ideas/sympy/sympy-sympy-issues-26096)
  * Better support for Order term arithmetic (for example, expression of the
    order term of the series around a point that is not 0, like O((x - a)**3)).
    * [issue 1](/ideas/sympy/sympy-sympy-issues-22836)
    * Read through [discussion](https://github.com/sympy/sympy/pull/22247#issuecomment-977811355) & comments for fixing [issue](/ideas/sympy/sympy-sympy-issues-21315)
    * Fix _eval_subs method to hanlde [issue 1](/ideas/sympy/sympy-sympy-issues-19120), [issue 2](/ideas/sympy/sympy-sympy-issues-10290), [issue 3](/ideas/sympy/sympy-sympy-issues-7872), [issue 4](/ideas/sympy/sympy-sympy-issues-15915)
  * Fix limit computations for piecewise functions
    * revamp work on [PR](https://github.com/sympy/sympy/pull/22339) and test properly, [relevant issue](/ideas/sympy/sympy-sympy-issues-24127)
  * All other problems, which are described in wiki page about [series](/ideas/sympy/ud-series) and
    [current situation](/ideas/sympy/ud-series-situation)


**Status**

There is already a fast implementation called `rs_series` in SymPy. This
project would extend it to work for all functions and then make it the default
series expansion in SymPy.

SymPy now has support for Formal Power Series (series.formal). The algorithm is more or less
complete. The module should be made faster. There are also a lot of XFAIL tests that can be made to pass.

A new algorithm for computing limits of sequences has also been added (series.limitseq). There are still XFAIL tests that can be made to pass.

**Some references**

1. "Formal Power Series" by Dominik Gruntz and Wolfram Koepf
2. "A New Algorithm Computing for Asymptotic Series" by Dominik Gruntz
3. "Computing limits of Sequences" by Manuel Kauers
4. "Symbolic Asymptotics: Functions of Two Variables, Implicit Functions"
    by Bruno Savly and John Shackell
5. "Symbolic Asymptotics: Multiseries of Inverse Functions" by Bruno Savly
    and John Shackell

**Involved Software**

SymPy

**Difficulty**

Medium

**Prerequisite Knowledge**

Calculus

**Project Length**

175 hours or 350 hours, depending on the project details (discuss with us).


## Cylindrical algebraic decomposition

**Idea**

* Implement the Cylindrical algebraic decomposition algorithm
* Use CAD to do quantifier elimination
* Provide an interface for solving systems of polynomial inequalities

* Some references:
  * Cylindrical Algebraic Decomposition
    [[http://mathworld.wolfram.com/CylindricalAlgebraicDecomposition.html]]
  * "Algorithms in Real Algebraic Geometry"
    [[http://perso.univ-rennes1.fr/marie-francoise.roy/bpr-ed2-posted1.html]]
    (useful background resource, but contains much more information)
  * "Cylindrical Algebraic Decomposition I: The Basic Algorithm" by Dennis
    S. Arnon, George E. Collins, Scot McCallum
  * "Computing Cylindrical Algebraic Decomposition via Triangular
    Decomposition" by Marc Moreno Maza, Changbo Chen, Bican Xia, Lu Yang
  * "Simple CAD Construction and its Applications" by Christopher W. Brown
  * "Improved Projection for Cylindrical Algebraic Decomposition" by Christopher W. Brown
  * "Symbolic Computation for Inequalities" by Manuel Kauers
    [[http://www.sfb013.uni-linz.ac.at/uploads/media/SymCompIneq.pdf]]
  * "How To Use Cylindrical Algebraic Decomposition" by Manuel Kauers

**Status**

**Involved Software**

**Difficulty**

**Prerequisite Knowledge**

**Project Length**

350 hours

## Efficient Groebner bases and their applications

**Idea**

Groebner bases computation is one of the most important tools in computer
algebra, which can be used for computing multivariate polynomial LCM and GCD,
solving systems of polynomial equations, symbolic integration, simplification
of rational expressions, etc. Currently there is an efficient version of
Buchberger algorithm implemented and of the F5B algorithm, along with naive
multivariate polynomial arithmetic in monomial form. There is also the FGLM
algorithm converting reduced Groebner bases of zero-dimensional ideals from one
ordering to another.

Improve efficiency of Groebner basis algorithm by using better selection
strategy (e.g. sugar method) and implement Faugere F4 algorithm and analyze
which approach is better in what contexts.  Implement the generic Groebner walk
converting between Groebner basis of finite-dimensional ideals; there are
efficient algorithms for it, by Tran (2000) and Fukuda et al. (2005).

Apply Groebner bases in integration of rational and transcendental functions
and simplification of rational expressions modulo a polynomial ideal (e.g.
trigonometric functions).

**Status**

There was a project last year relating to Groebner bases. Please take a look a
the source and discuss things with us to see what remains to be done.

Some Groebner bases algorithms, in particular F4, require strong linear
algebra.  Thus, if you want to do that, you may have to first improve our
matrices (see the ideas relating to this above).

**Involved Software**

**Difficulty**

**Prerequisite Knowledge**

**Project Length**

350 hours

## Multivariate polynomials and factorization

**Idea**

Factorization of multivariate polynomials is an important tool in algebra
systems, very useful by its own, also used in symbolic integration algorithms,
simplification of expressions, partial fractions, etc. Currently multivariate
factorization algorithm is based on Kronecker's method, which is impractical
for real life problems. Undergo there is implementation of Wang's algorithm,
the most widely used method for the task.

Start with implementing efficient multivariate polynomial arithmetic and GCD
algorithm. You do this by improving existing code, which is based on recursive
dense representation or implement new methods based on your research in the
field. There are many interesting methods, like Yan's geobuckets or heap based
algorithms (Monagan & Pearce). Having this, implement efficient GCD algorithm
over integers, which is not a heuristic, e.g. Zippel's SPMOD, Musser's EZ-GCD,
Wang's EEZ-GCD. Help with implementing Wang's EEZ factorization algorithm or
implement your favorite method, e.g. Gao's partial differential equations
approach. You can go further and extend all this to polynomials with
coefficients in algebraic domains or implement efficient multivariate
factorization over finite fields.

**Status**

Some work on this may already be done. Take a look at
`sympy/polys/factortools.py` in the SymPy source code.

**Involved Software**

**Difficulty**

Advanced

**Prerequisite Knowledge**

**Project Length**

350 hours

## Univariate polynomials over algebraic domains

**Idea**

Choose a univariate polynomial representation in which elements of algebraic
domains will be efficiently encoded. By algebraic domains we mean algebraic
numbers and algebraic function fields. Having a good representation, implement
efficient arithmetic and GCD algorithm. You should refer to work due to
Monagan, Pearce, van Hoeij et. al. Having this, implement your favorite
algorithm for factorization over discussed domains. This will require
algorithms for computing minimal polynomials (this can be done by using LLL or
Groebner bases). You can also go ahead and do all this in multivariate case.

**Status**

Currently SymPy features efficient univariate polynomial arithmetic, GCD and
factorization over modular rings and integers (rationals). This is, however,
insufficient in solving real life problems, and has limited use for symbolic
integration and simplification algorithms. For example, the support for finite
fields GF(p^n) is missing.

**Involved Software**

**Difficulty**

Advanced

**Prerequisite Knowledge**

**Project Length**

350 hours

## Concrete module: Implement Karr algorithm, a decision procedure for symbolic summation

**Idea**

Algorithm due to Karr is the most powerful tool in the field of symbolic
summation, which you will implement in SymPy. There are strong similarities
between this method and Risch algorithm for the integration problem. You will
start with implementing the indefinite case and later can extend it to support
definite summation (see work due to Schneider and Kauers). Possibly you will
also need to work on solving difference equations.

* Some references:
  * "A=B" by Marko Petkovsek, Herbert S. Wilf, Doron Zeilberger
  * "Symbolic Summation with Radical Expressions" by Manuel Kauers and Carsten
    Schneider
  * "An Implementation of Karr's Summation Algorithm in Mathematica" by
    Carsten Schneider
  * Manuel Kauers, webpage: [[http://www.risc.jku.at/home/mkauers]]
  * Carsten Schneider, webpage: [[http://www.risc.jku.at/people/cschneid]]
  * "Algorithmen für mehrfache Summen", by Torsten Sprenger

**Status**

SymPy currently features Gosper algorithm and some heuristics for computing
sums of expressions. Special preference is for summations of hypergeometric
type. It would be very convenient to support more classes of expressions, like
(generalized) harmonic numbers etc. There is already an complete algorithm
rational expression summation.

**Involved Software**

**Difficulty**

Advanced

**Prerequisite Knowledge**

**Project Length**

350 hours

# Physics Projects

## Symbolic Control Systems (`sympy.physics.control`)

**Idea**

A Control Systems subpackage
([`sympy.physics.control`](https://github.com/sympy/sympy/tree/master/sympy/physics/control))
was added to SymPy in the summer of 2020, by Naman Gera. This was built upon
further by Akshansh Bhatt in 2021 and Anurag Bhat in 2023. It would be great
to continue its development and make it more accessible to the public. Since
the users are mostly students and researchers in the field of Control theory, a
set of problems from a textbook can be solved in the documentation, as the
development proceeds.

https://www.cds.caltech.edu/~murray/amwiki/Second_Edition.html can be used as a reference.

**Status**

The functionalities of the project can be viewed here:

https://docs.sympy.org/latest/modules/physics/control/lti.html#module-sympy.physics.control.lti

Future Work (can be modified after discussion):

* Refactor and complete plots:
    1. The plots namely **Pole Zero**, **Step Response**, **Impulse Response**, **Ramp Response**, **Bode Magnitude** and **Bode Phase** plots need to be refactored since they use `numpy` and `matplotlib`. The numerical methods were used for speed but they sacrifice on precision. Sympy's symbolic methods are used in the first place for the precision they provide, hence these numerical methods should be replaced by algebraic methods. \
[Davide](https://github.com/Davide-sd), a fellow contributor has been revamping the plotting module. Check this [roadmap](/ideas/sympy/sympy-sympy-issues-19263), according to which `SymPy` will soon have its own `plot_list` function after which this refactoring could be done with ease.
    2. The plots namely **Root Locus**, **Nichols** and **Nyquist** plots are draft pull requests and need to be completed. They have clear ideas to follow and some comments which can be addressed once `SymPy` no longer depends upon `matplotlib` and `numpy`.

* Implementations for the `StateSpace` class:
    1. Solve examples mentioned in [#25502](/ideas/sympy/sympy-sympy-issues-25502) and add them to the `control_problems` file . The required functionality is already supported in the pull request.

* Make the classes more feature rich:
    1. Read about Laub's or Horner's method to evaluate system transfer function at complex frequency. This will be the equivalent of `eval_frequency` for Transfer Functions.
    2. Other features can be picked up on comparison with `MATLAB` and `python-control`.
    3. Implement the Z-Transform and its inverse. See [#28347](/ideas/sympy/sympy-sympy-issues-28347) for more information.
    4. Implement the DiscretePIDController.
    
* Refactoring:
    1. Simplify the code to improve clarity.
    2. Add type annotations.

**Involved Software**

Python, Git

**Difficulty**

Intermediate

**Prerequisite Knowledge**

Undergraduate level Control Systems knowledge will suffice. Otherwise, one _can_ complete the project if they self-learn required topics and then contribute voraciously.

**Project Length**

150 or 350 hours.

## Symbolic quantum mechanics (`sympy.physics.quantum`)

In the past, Brian Granger was the maintainer of the `sympy.physics.quantum`
subpackage. He has stepped down from this position. Until someone takes over
the maintenance of this subpackage, we will not be able to mentor any GSoC projects
in this area. If you have questions about this, please contact Ondřej Čertík.

## Continuum Mechanics: Create a Rich 2D Beam Solving System

**Idea**

Singularity functions are a popular tool for solving beam bending stress and
deflection problems in mechanical design. This is traditionally done by hand
calculations and can be very tedious and error prone. This process could be
improved greatly by a CAS implementation of the functions and some high level
abstractions for constructing beam loading profiles.

The deliverable would be a unit tested and documented sub-package for SymPy 2D
and 3D beams that can solve many beam problems, add in arbitrary cross
sections, plotting, be robust, and add any other relevant features.

**Status**

Sampad Saha implemented Singularity Functions in 2016. The 2017 and 2018 GSoC
projects created the functionality shown here:

https://docs.sympy.org/dev/modules/physics/continuum_mechanics/beam_problems.html

Some students at Delft Univeristy of Technology expanded both the theoretical
and coding capabilities (https://oit.tudelft.nl/Macaulays-method/overview.html).

The next steps involve making it easier to define complex cross sectional
geometry via the geometry package, developing the 3D Beam into a well tested
and robust class, and polishing to the plotting for 2D and 3D beams. Adding a
large set of example problems that exercise the functionally.

Other next steps focus on extending capabilities to frames.

**Involved Software**

Python, Git

**Difficulty**

Intermediate

**Prerequisite Knowledge**

No specific prerequisite knowledge is necessary but it would help if the
student had some knowledge of beam stress/strain analysis methods.

**Project Length**

350 hours.

## Classical Mechanics

The following project ideas are in approximate order of priority.

## Classical Mechanics: Generalize the Equations of Motion System Output

**Idea**

We would like an ecosystem in which you can define/create your mechanical
system in a general way using joints, bodies, forces, torques, etc., compute
the equations of motion based on different methods like `LagrangesMethod` and
`KanesMethod`, to be used in numerical purposes, like simulations and
optimizations.

The above is the general picture for which a lot of work has been done over the
years on the different parts. However, some parts are disjoint while other
parts are still missing or should almost be entirely replaced.

Note that defining/creating the mechanical system falls into two other projects,
namely:
- [Classical Mechanics: Constructing Systems From Bodies and Joints](#classical-mechanics-constructing-systems-from-bodies-and-joints)
- [Classical Mechanics: Implement Specific Forces and Torques](#classical-mechanics-implement-specific-forces-and-torques)
- [Classical Mechanics: Implement and Benchmark Equations of Motion Methods](#classical-mechanics-implement-and-benchmark-equations-of-motion-methods)

**Status**

Previous work covers quite a few different parts, which can be improved and
extended, but mostly require to be tied together more properly:
- An abstract base class as an interface to the different equations of motion
  generation methods has been introduced in
  [#21778](https://github.com/sympy/sympy/pull/21778).
- Refer to the project
  [Classical Mechanics: Constructing Systems From Bodies and Joints](#classical-mechanics-constructing-systems-from-bodies-and-joints)
  for the status of bodies and joints.
- Refer to the project
  [Classical Mechanics: Implement Specific Forces and Torques](#classical-mechanics-implement-specific-forces-and-torques)
  for the status of implementing specific loads.
- In [#25560](https://github.com/sympy/sympy/pull/25560) a `System` class was
  introduced as a general frontend to define a mechanical system and generate
  the equations of motion using either of the implemented methods, i.e.
  `LagrangesMethod` and `KanesMethod`.
- In [#11431](https://github.com/sympy/sympy/pull/11431) as `SymbolicSystem` was
  introduced as a data class to store all information about a system and its
  equations of motion in a general format.
- In [PyDy](https://github.com/pydy/pydy) there also exists a
  [`System` class](https://github.com/pydy/pydy/blob/master/pydy/system.py),
  which can be used to simulate a system that was solved using `KanesMethod`.

The goal of this project is to implement a class to function as a general
interface of a system from which the equations of motion can be used for
numerical purposes. This class would be an extension or replacement of
`sympy.physics.mechanics.system.SymbolicSystem`. Some of the features it should
offer are:
- A general representation of the equations of motion and the algebraic
  constraints.
- Methods to code generate the functions to be used in simulation purposes, like
  with `scipy.integrate.solve_ivp` and `scikits.odes.dae`.
- It should use `sympy.physics.mechanics.system.System` for the basic system
  information. It could possibly have multiple methods to be instantiated, like
  a normal `__init__` where all equations and things need to be provided as is
  currently the case with `SymbolicSystem`, and a classmethod `from_system`,
  where it extracts most information from the `System` instance.

**Involved Software**

Python, Git

**Difficulty**

Advanced

**Prerequisite Knowledge**

This project requires basic understanding of dynamical systems and at least
understanding of one method of generating the equations of motion for a
multi-body system.

**Project Length**

350 hours.

## Classical Mechanics: Implement and Benchmark Equations of Motion Methods

**Idea**

There are many methods to derive the equations of motion. Each method has its
advantageous and disadvantageous when modeling different systems. SymPy
currently contains only two methods: `KanesMethod` and `LagrangesMethod`. The
idea of this project is to develop more methods to form the equations of motion
and to benchmark them for different models to also give users more insight what
model they should use for their application.

**Status**

- An abstract base class as an interface to the different equations of motion
  generation methods has been introduced in
  [#21778](https://github.com/sympy/sympy/pull/21778).

This project could roughly entail the following steps:
- Improve the abstract base class, `sympy.physics.mechanics.method._Methods` of
  the equations of motion generation methods, e.g. `KanesMethod`.
- Improve the implementation of `KanesMethod` and `LagrangesMethod`.
- Implementing more methods to generate the equations of motion, like
  `NetwonEulersMethod` or `HamiltonsMethod`.
- Develop a benchmark suite deriving the equations of motion using the different
  methods and measure their performance. Examples could include a 5-DoF planar
  kinematic chain, a four-bar linkage, and the Carvallo-Whipple bicycle model.

**Involved Software**

Python, Git

**Difficulty**

Intermediate

**Prerequisite Knowledge**

This project requires basic understanding of dynamical systems and at least
understanding of one method of generating the equations of motion for a
multi-body system.

**Project Length**

175 or 350 hours.

## Classical Mechanics: Efficient Equations of Motion Generation

**Idea**

Currently we have basic equation of motion generation with automated Kane's and
Lagrange's methods. These methods work well but can take many minutes to
complete for hard problems. The algorithms that derive these equations of
motion can be improved in both speed of computation and the resulting
simplification of the equations of motion. This project would involve profiling
to find the slow functions and speeding up the slow parts. This may involve
digging into the SymPy codebase for trigonometric simplification and other
relevant function calls to speed up the EoM generation. These modification will
help speed up both the entire SymPy codebase and the Mechanics package.

**Status**

There is no previous work on this topic.

**Involved Software**

Python, Git

**Difficulty**

Beginner

**Prerequisite Knowledge**

There are no prequisites to this project.

**Project Length**

175 or 350 hours.

## Classical Mechanics: Implement Wrapping Geometry and Pathways for Musculoskeletal Modeling

**Idea**

SymPy Mechanics includes classes to manage how forces and torques act on
connected bodies when the path of action is a complex pathway that wraps over
geometric features. This is critical for accurate musculotendon force
generation. The [Biomechanical Model
Example](https://docs.sympy.org/dev/tutorials/physics/biomechanics/biomechanical-model-example.html)
shows a simple cylindrical wrapping of a muscle around the elbow. This idea
involves adding more wrapping surfaces and pathways that are useful for
musculoskeletal modeling.
The work can include implementing new wrapping geometry classes, such as an ellipsoid or torus. In addition, the APIs of wrapping geometry objects can be expanded to expose new useful convenience methods (for example, computing tangent or contact points). More end to end example models can also be added to the documentation.

**Status**

- [Cylindrical, sphereical and conical wrapping geometry
  exist](https://docs.sympy.org/dev/modules/physics/mechanics/api/wrapping_geometry.html)
- [Example models for cylindrical, spherical and conical geometries exist in the dev documentation](https://docs.sympy.org/dev/tutorials/physics/mechanics/atwoods_machine_example.html)
- [Linear and obstacle pathway
  exist](https://docs.sympy.org/dev/modules/physics/mechanics/api/pathway.html#sympy.physics.mechanics.pathway.WrappingPathway)

**Involved Software**

Python, Git

**Difficulty**

Beginner to intermediate

**Prerequisite Knowledge**

This project requires basic understanding geometry, forces, anatomy and basic familiarity with Kane's/Lagrange's method.

**Project Length**

90, 175, or 350 hours (depends on how many features you'd like to implement)

## Classical Mechanics: Implement Specific Forces and Torques

**Idea**

Many forces and torques still have to be manually created by the user. It would
be helpful if we had a set of typical and common forces and torques. Some
possible examples:

- Actuator forces and torques
- Aerodynamic forces
- Contact force models
- Friction force models
- Linear and nonlinear springs and dampers
- Musculotendon models, like the Hill type muscle model
- Controller forces (like PID or full state feedback)
- [Eardrum model](https://www.cfm.brown.edu/people/dobrush/am33/Mathematica/ch4/nspring.html)

Some kind of force and torque objects will likely be needed as well as symbolic
mathematical descriptions of the force and torque models. The forces and
torques should work with SymPy's code generation to generate efficient and
robust numerical codes. Here is a [soft introduction to forces and
torques](https://moorepants.github.io/learn-multibody-dynamics/loads.html).

**Status**

- Timo Stienstra introduced a `Force` and `Torque` class, refer to
  [#24258](/ideas/sympy/sympy-sympy-issues-24240) and
  [#24641](https://github.com/sympy/sympy/pull/24641).
- Sam Brockie implemented an abstract base class to define actuators and
  implemented several types of actuators, like a `LinearSpring` and
  `LinearDamper`, refer to [#25518](https://github.com/sympy/sympy/pull/25518).
- Sam Brockie implemented base classes for Musculotendon force generators,
  refer to the [musculotendon
  API](https://docs.sympy.org/dev/modules/physics/biomechanics/api/musculotendon.html)
- Hwayeon Kang implemented [CoulombKineticFriction](https://docs.sympy.org/dev/modules/physics/mechanics/api/actuator.html#sympy.physics.mechanics.actuator.CoulombKineticFriction) and
  [DuffingSpring](https://docs.sympy.org/dev/modules/physics/mechanics/api/actuator.html#sympy.physics.mechanics.actuator.DuffingSpring) classes, refer to [#26438](https://github.com/sympy/sympy/pull/26438) and [#26412](https://github.com/sympy/sympy/pull/26412).
- Initial idea for the Hill muscle model is introduced in [#26443](https://github.com/sympy/sympy/pull/26443) -- it will be helpful to refer to the `DeGroote2016` classes in `sympy.physics.biomechanics.activation` together.

Some load types that could be worked on are:
- Contact force models
- Aerodynamic forces
- Nonlinear springs and dampers
- Models involving biomechanics, refer to
  [#24240](/ideas/sympy/sympy-sympy-issues-24240) for ideas.

**Involved Software**

Python, Git

**Difficulty**

Beginner to intermediate

**Prerequisite Knowledge**

This project requires basic understanding of dynamics and numerical methods.

**Project Length**

90, 175, or 350 hours (depends on how many features you'd like to implement)

## Classical Mechanics: Constructing Systems From Bodies and Joints

**Idea**

We'd like to be able to construct multibody systems by specifying descriptions
of rigid bodies and the joints and constraints that connect them.

**Status**

- Sahil Shekewat worked on implementing a joint-based descriptor for systems:
  https://github.com/sympy/sympy/pulls/sahilshekhawat
- Sudeep Sidhu completed Sahil's work and merged a functioning joint-based
  system that can solve open-chain problems. See his report:
  https://github.com/sympy/sympy/wiki/GSoC-2021-Report-Sudeep-Sidhu-:-Implement-JointsMethod
- Timo Steinstra furthered the work by enhancing the joint definition, adding
  new joints, and developing examples of using the joints framework.

The next steps are, in order of priority:

- Fix any existing bugs with the joints.
- Add many different example problems to test the robustness of the
  implementation.
- Allow parsing constants as generalized coordinates to `Joint`, such as
  `pi / 2` to the `PinJoint`, as if it is just a fixed pin.
- Implement and test quaternion rotations.
- Implement a `Mobilizer` joint or `CustomJoint` for describing complex motions,
  refer to ([#23920 comment](https://github.com/sympy/sympy/pull/23920#issue-1337665929)).
- Implement an option to choose the generalized speeds efficiently, refer to
  [#24053 comment](https://github.com/sympy/sympy/pull/24053#issuecomment-1262468801).

**Involved Software**

Python, Git

**Difficulty**

Intermediate to Advanced

**Prerequisite Knowledge**

This project requires familiarity with multibody dynamics. At the least, one
should know how to form the equations of motion of complex systems with one
method.

**Project Length**

90, 175, or 350 hours

## Classical Mechanics: Implement an O(N) Equations of Motion Method

**Idea**

Roy Featherstone, Abhi Jain, and others developed recursive methods of forming
the right-hand side of the differential equations for complex multibody systems
that have an evaluation time of O(N) instead of O(N^3). This project would be
dedicated to implementing a symbolic O(N) method to complement the
`LagrangesMethod` and `KanesMethod` classes. This project would involve
implementing 6D vectors and spatial operators, as well as the recursive
methods. This would give a significant speed boost in numerical evaluation for
systems with bodies greater than 20 or so.

**Status**

Brandom Milam made significant headway in this project in 2016. See:

- https://github.com/sympy/sympy/wiki/GSoC-2016-Application-James-Brandon-Milam:-Base-Class-and-Increased-Efficiency-for-Equation-of-Motion-Generators
- https://github.com/sympy/sympy/pulls/jbm950

**Involved Software**

Python, Git

**Difficulty**

Extremely Advanced

**Prerequisite Knowledge**

This project requires proficiency with multibody dynamics. At the least, one
should know how to form the equations of motion of complex systems with one
method. The ideal candidate will have experience forming the equations of
motion with the aforementioned Featherstone or Jain methods.

**Project Length**

350 hours.

# Computer Science, Graphics, and Infrastructure Projects

## Enhancing the flexibility of MatchPy

**Idea**

MatchPy, a Python library, provides associative-commutative pattern matching and replacement rules for expression trees. This functionality enhances the usability of computer algebra systems, simplifying the formulation of transformation rules for mathematical formulas.

In essence, MatchPy expressions can be likened to "regular expressions with an awareness of commutative and associative properties”. MatchPy also supports the simultaneous execution of multiple matches, contributing to its exceptional efficiency.

However, the current requirement for expression trees and wildcards to be subclasses of MatchPy objects presents a significant inflexibility. This constraint forces SymPy to delve into metaclass intricacies to function, limiting the ability to work with expression trees whose node type lacks identification by an object.

This proposal seeks to enhance MatchPy by restructuring its node type identification, the iteration criteria and wildcard definitions. This involves replacing type checks with custom node identification and iteration rules, fostering greater flexibility in working with various expression tree structures.

Since MatchPy is currently under a separate project and has experienced a period of inactivity, forking MatchPy becomes necessary for the progress of this project.

Additionally, if time allows it, this project also envisions exploring the possibility of a Rust implementation of MatchPy, aiming to enhance its speed and efficiency.

**Status**

An experimental connector to MatchPy has been successfully implemented and can be found in sympy.utilities.matchpy_connector. For a comprehensive understanding of the algorithm that drives MatchPy, refer to the paper authored by its creators, available at https://arxiv.org/abs/1710.06915.
Furthermore, it's worth noting that MatchPyCpp, an integral submodule of SymEngine, features a translation of the main MatchPy algorithms into C++. However, its performance is presently constrained by the absence of support for coroutines.

**Involved software**

Python, MatchPy

**Difficulty**

Advanced.

This project very likely requires the MatchPy library to be forked.

This project necessitates proficiency in executing tree-visiting algorithms.

**Project Length**

350 hours.


## Code Generation

**Idea**

There are quite a few potential projects for codegen.

The code generation system in SymPy has been overhauled to use AST nodes
from ``sympy.codegen.ast``, there are however lot of more nodes that can be added
for e.g. Fortran in ``sympy.codegen.fnodes``. It could also be useful if the code
printers could output parallel code using OpenMP directives (e.g. parallel for loops
for C and Fortran, including use of reduction). Most printers do not yet support the
new AST nodes, it would be useful if those were extended so that they can express ASTs
created e.g. by functions in ``sympy.codegen.algorithms``.

Another idea for codegen is to add more support for directly working with matrices. For instance, matrix expressions (sympy.matrices.expressions objects) should print LAPACK calls.

**Status**

We have support for a number of backends and basic code gen classes in place.
There is work on updating the system ongoing. Please ask on the mailing list.

You can check out the work done by Ankit Pandey to extend codegen to support matrix operations at [Extending Codegen GSoC 2019](/ideas/sympy/gsoc-2019-report-ankit-pandey-extending-codegen)

**Involved Software**

Fortran, C, C++, Julia, Rust, Python, LLVM, Javascript, Octave, Matlab, etc.

**Difficulty**

Intermediate to Advanced

**Prerequisite Knowledge**

**Project Length**

175 hours or 350 hours, depending on the project details (discuss with us).

## Code Generation: Efficient Jacobian and Hessian Evaluation for Optimization and ODE Integration

**Idea**

When solving optimization problems with gradient based solutions, you typically
need to evaluate the function to optimize along with its Jacobian and/or
Hessian (or the Lagrangian of the Hessian). SciPy offers many optimization
routines, many which accept three functions for evaluating the function, the
Jacobian, and the Hessian. If you create a function in SymPy, then having the
ability to do something like:

```python
rosenbrock_expr = (a - x)**2 + b*(y - x**2)**2
eval_f, eval_j, eval_h = generate_minimize_derivative_funcs(expr, (x, y), extra_args=(a, b))
result = minimize(eval_f, x0, jac=eval_j, hess=eval_h)
```

would make it very easy to solve optimization problems from functions defined in
SymPy. If the expression is very large, the computational cost of evaluating
those three functions needs to be minimized. With careful use of lambdify,
autorwrap, and shared common sub expressions, SymPy can generate very efficient
versions of these functions.

Similarly, when numerically integrating ordinary differential equations, the
Jacobian of the integrand  (and its sparsity information) can be useful for the
integration algorithms.

```python
rhs = [
    v(t),
    (-sign(v(t))*B*v(t)**2 - k*x(t) - c*v(t) + A*sin(w*t))/m
]
eval_f, eval_j, sparsity = generate_ode_derivative_funcs(rhs, (x(t), v(t)), extra_args=(A, B, m, c, k))
result = solve_ivp(eval_f, (0.0, 1.0), y0, jac=eval_j, jac_sparsity=sparsity)
```

Once again, for very large expressions, generating computationally efficient
code becomes very important for fast integration performance.

**Status**

There are existing tools where these basic ideas have been implemented outside
of SymPy. For example:

- [pyodesys](https://github.com/bjodah/pyodesys): integrates ODEs defined with
  SymPy
- [symopt](https://github.com/spcornelius/symopt): optimizes functions defined
  with SymPy
- [opty](https://github.com/csu-hmc/opty): generates a numerical function and
  its sparse jacobian
- [simple stackoverflow
  question](https://stackoverflow.com/questions/34115233/python-optimization-using-sympy-lambdify-and-scipy)
- [optimization problem that doesn't quite connect sympy to
  scipy](https://gist.github.com/XavierMBP/5b783b4b03100483c107d7425070a15b)
- [symjit](https://github.com/siravan/symjit) has a simple API for generated
  numerical functions on-the-fly.

Riccardo added a new Jacobian function in 2024 that efficiently computes
Jacobians of very large expressions in
[#26773](https://github.com/sympy/sympy/pull/26773). We should be able to use
this, at least optionally, for computing derivatives.

See the SciPy documentation:

- [SciPy Optimization](https://docs.scipy.org/doc/scipy/tutorial/optimize.html)
- [solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)

**Involved Software**

None

**Difficulty**

Intermediate to Advanced

**Prerequisite Knowledge**

Knowledge of optimization and ODE integration and their associated numerical
methods.

**Project Length**

175 or 350

## Improve the Lark-based LaTeX parser

**Idea**

There are a lot of issues with the old ANTLR-based parser. Motivations for why we need a new LaTeX parser
can be found [here](https://wermos.github.io/blog/gsoc/sympy/gsoc-2-the-sympy-boogaloo/), where it is discussed
in great detail.

**Status**

There was some work done in 2023: [Rewrite the LaTeX parser (GSoC 2023)](https://summerofcode.withgoogle.com/archive/2023/projects/apj3AeJL),
wherein a new parser was designed and implemented from the ground up. It supports a lot of the features of the existing ANTLR-based parser,
but is not a full drop-in replacement yet.

But the Lark-based parser is not complete, as it is not a drop-in replacement for the ANTLR-based parser. The current state of the parser can
be found in [this blog post](https://wermos.github.io/blog/gsoc/sympy/gsoc-2-the-final-status-report/) that was written during the 2023 GSoC, and
SymPy Issue [#25365](/ideas/sympy/sympy-sympy-issues-25365).

**Involved Software**

Python, [Lark](https://lark-parser.readthedocs.io/en/latest/)

**Difficulty**

Intermediate

**Prerequisite Knowledge**

Some knowledge of LaTeX would be helpful

**Project Length**

175 hours or 350 hours, depending on the details (discuss with us).

## Parsing

**Idea**

SymPy has the ability to generate Python, C, and Fortran code from
SymPy expressions.

It would be very interesting to go the other way, to be able to parse Python,
C, and Fortran code and produce SymPy expressions. This would allow SymPy to
easily read in, alter, and write out computational code. This project would enable
many other projects in the future. Ideally, this project would create a general
framework for parsers and then use this system to implement parsers for a few
of the languages listed above. See the other parsing ideas on this page, as
well as [[Parsing]].

**Status**

SymPy currently has a parsing module that supports parsing LaTeX and
[autolev](GSoC-2018:-Autolev-Parser-(using-ANTLRv4):-Final-Report) using
ANTLR, C, and Fortran. The parsing module also supports a Python parser,
with special extensions to support things like implicit multiplication (`2a` -> `2*a`)
and implicit function application (`sin x` -> `sin(x)`), which uses the Python `tokenize` module.

You can check out the work done on the C and Fortran parsers at [Creating a C and Fortran Parser GSoC 2019](/ideas/sympy/gsoc-2019-report-nikhil-maan-creating-a-c-and-fortran-parser-for-sympy)

The existing parsers could be improved by adding support for more features of the programming languages, or new parsers could be added for other languages like Julia, Octave, MATLAB, etc.

**Involved Software**

Fortran, C, C++, Julia, Rust, Python, LLVM, Octave, Matlab, etc.

**Difficulty**

Intermediate to Advanced

**Prerequisite Knowledge**

**Project Length**

175 hours or 350 hours, depending on the project details (discuss with us).

## Improve the plotting module

**Idea**

A new plotting module
[sympy-plot-backends](https://github.com/Davide-sd/sympy-plot-backends) has
been written, which is planned to replace the existing `sympy.plot` module
(see https://github.com/sympy/sympy/issues/23036).

The idea is to merge this module into SymPy, also implementing substantial
improvements and possibly new functionalities.

A very approximate guesstimate is given.

  * medium/hard: Refactoring of *Series classes in order to reduce code repetition
    and allow the implementation of new features.
  * easy/medium: Improve numerical evaluation.
  * medium/hard: implement custom theming for interactive applications and fix a
    behaviour affecting the current interactive module.
  * easy/medium: Implement new functionalities:
      * 2D and 3D linear operators (the effect of a matrix on a plane/3D space)
      * Phase portrait for Ordinary Differential Equations.
      * Improve plot_parametric_region to better visualize complex maps.
      * Animations.
  * easy/medium: Packaging: while the main plotting functionalities work just with
    sympy, numpy and matplotlib, the full plotting module relies on several other
    packages. It has been observed that building a conda package with the full
    dependencies is difficult: most of the time the build succeed but the installation
    fails. Debug and fix it.
  * easy/medium: Implement a intelligent routine that automatically determines
    the regions of interest for plotting.
  * Fix related things/bugs in SymPy

More detailed information can be found on [this page](https://github.com/Davide-sd/sympy-plot-backends/wiki/Roadmap-to-version-2).

**Status**

Currently, the new plotting module lives on an external repository: [sympy-plot-backends](https://github.com/Davide-sd/sympy-plot-backends)

**Involved Software**

Python, HTML, Javascript, CSS

**Difficulty**

Intermediate to Advanced: working with several different packages can be overwhelming.

**Prerequisite Knowledge**

**Project Length**

350 hours.

## Documentation tooling

**Idea**

SymPy's documentation makes use of Sphinx and several Sphinx extensions. The
idea here is to improve the tooling around the docs by developing some Sphinx
extensions. Some ideas here

- Write a Sphinx extension that improves the way autodoc cross references work (see
  https://github.com/sympy/sympy/issues/23081)
- Add autosummary to our docs so that each function is on a separate page.
  This may require writing a Sphinx extension or some other tooling. See
  https://github.com/sympy/sympy/pull/22589 for why default autosummary does
  not work.
- Implement linters for various parts of markup so that people can avoid
  common mistakes. Mistakes include:
  - Using the wrong type of markup for math, code, and cross-references (see
    also https://github.com/sympy/sympy/issues/13519)
  - Common mistakes in LaTeX $math$ (see for instance https://github.com/sympy/sympy/issues/17803)
  - Various things outlined in the [documentation style
    guide](https://docs.sympy.org/dev/guides/contributing/docstring.html)
- Improved tooling to make sure every docstring is included in Sphinx and
  every docstring has a doctest (see the `bin/coverage_doctest` script in the
  SymPy repo, which needs improvement)
- Some way to make it so that headers in docstrings can be easily linked to
  and cross-referenced https://github.com/sympy/sympy/issues/17599
- Allow subheaders in docstrings https://github.com/sympy/sympy/issues/17618
- Several other small issues, mostly relating to the way autodoc generates
  documentation. See these issues for some additional ideas
  https://github.com/sympy/sympy/labels/GSoD.


**NOTE: Google requires that any GSoC project be primarily coding. This
project is *not* primarily about writing documentation, as such a project is
not allowed. It is instead about developing tooling to improve the SymPy
documentation system.**

**Status**

Some things are already implemented, for instance, we have an extension that
lets us use dollar signs for math in RST
https://github.com/sympy/sphinx-math-dollar. See the above issues for the
status of any specific item.

**Involved Software**

This would primarily involve working with Sphinx and building Sphinx
extensions or modifying existing ones. If relevant, we may prefer to upstream
changes to Sphinx itself (although the Sphinx developers will not be mentors
on this project, so we should not rely on this happening).

**Difficulty**

Intermediate to advanced (working with Sphinx can often be difficult)

**Prerequisite Knowledge**

Prior experience with RST and using autodoc is recommended.

**Project Length**

A project to implement all or the majority of the above ideas would require a
350 hours project, but a 175 hours or even 90 hours project can also be done that only
implements a subset of the above ideas.

## Hypothesis testing

**Idea**

[Hypothesis](https://hypothesis.readthedocs.io/en/latest/) is a Python library
for property-based testing. Hypothesis tests work by specifying properties
that a function should satisfy, and automatically generating inputs to test
it. There are more details of the idea of adding hypothesis to SymPy in [this
issue](/ideas/sympy/sympy-sympy-issues-20914).

The idea is to explore adding hypothesis testing to SymPy. We should start
small, ideally with a function that is already well tested and has relatively
easy to generate inputs. From there we can expand the testing.

Some work has begun on this but hypothesis is currently only used in a couple
of tests (search the sympy codebase for "hypothesis" to see where it is
currently used). However, we would like for much larger fractions of the tests
to use hypothesis.

Work on this project will involve adding tests to more functions, adding more
hypothesis strategies for different kinds of inputs, and reporting and
potentially fixing any SymPy bugs that you find along the way.

It's expected that throughout this process you will find many bugs in SymPy.
You may end up spending a lot of time in this project debugging failures,
fixing bugs, or working around bugs that are not so easily fixed.

**Status**

SymPy has some basic hypothesis tests, which demonstrate a proof-of-concept of using it. However, the usage could be expanded significantly, as only a handful of functions currently have hypothesis tests.

**Involved Software**

The hypothesis testing library.

**Difficulty**

Intermediate to Advanced.

Hypothesis testing is simple in principle, but using it in practice can be
difficult because it will uncover many bugs in SymPy. It will also not be
straightforward to use hypothesis to test symbolic expressions (there are some
ideas on how to do this outlined in the issue).

**Prerequisite Knowledge**

Prior experience with using hypothesis would be a huge plus, but it is not a
hard requirement. If you have not used hypothesis before it is recommended
that you play around with it and perhaps try adding some simple tests for
something (in SymPy or somewhere else) to get familiar with it.

**Project Length**

350 hours (175 hours is possible, but the longer is preferred since there will
be many things to do for this project).

# User Application Projects

# LFortran SymPy Project Ideas

[LFortran](https://gitlab.com/lfortran/lfortran) is a modern open-source (BSD licensed) interactive Fortran compiler
built on top of LLVM. It can execute user's code interactively to allow
exploratory work (much like Python, MATLAB or Julia) as well as compile to
binaries with the goal to run user's code on modern architectures such as
multi-core CPUs and GPUs.

The basic idea of LFortran is to provide the infrastructure that can be used as a foundation to do anything related to Fortran (tools that need any of: parsing, source code generation, code transformation, machine code generation, etc.)

LFortran is currently written in Python. Down the line it will get rewritten into C++ for speed and robustness, but even then it will have Python wrappers, so the Python API should not change much.

There are many potential projects regarding Fortran in general and . Please see the two ideas here first for background information:

https://github.com/sympy/sympy/wiki/GSoC-Ideas#code-generation
https://github.com/sympy/sympy/wiki/GSoC-Ideas#parsing

And then read through LFortran's documentation, mainly the [Developer Tutorial](https://docs.lfortran.org/developer_tutorial/) to understand LFortran's AST and ASR.

This page contains a few well developed ideas.

## SymPy -> Fortran Code Generation and JIT

**Idea**

Code generation from SymPy -> ASR, and then have two options: ASR -> AST -> source code, or ASR -> LLVM -> JIT and load it from Python to test it out.

Down the road the LLVM route might even be producing better (faster) code than using SymEngine->LLVM, because one can do optimizations on the ASR itself and before it is lowered to LLVM (as part of LFortran down the road), especially if one starts using do loops and arrays, because one knows more semantic information at the Fortran level than the LLVM level. And one can at least see the high level Fortran code (for debugging), as opposed to the relatively low level LLVM IR.

Currently SymPy represents Fortran code as a SymPy AST which is a combination of `sympy.codegen.ast` and `sympy.codegen.fnodes`. The `sympy.printing.fcode` module then has a visitor pattern that transforms this `ast`/`fnodes` AST into Fortran source code.

As a first step, one would change `fcode()` to transform this SymPy AST to LFortran's ASR. That will greatly simplify the printing, as LFortran will take care of transforming ASR -> AST (adding variable definitions mostly) and AST->source code. So SymPy code will get simplified. But also this will enable to then use LFortran to just in time compile this ASR and execute it from Python, thus allowing to interactively test the generated code.

One would port all the features from `fcode()` into LFortran, where it makes sense. SymPy should only do things which are SymPy specific.

After this is done, one can implement more features. For example it could be useful if the code
printers could output parallel code using OpenMP directives (e.g. parallel for loops
for C and Fortran, including use of reduction). Most printers do not yet support the
new AST nodes, it would be useful if those were extended so that they can express ASTs
created e.g. by functions in `sympy.codegen.algorithms`.

Another idea for codegen is to add more support for directly working with matrices. For instance, matrix expressions (`sympy.matrices.expressions` objects) should print LAPACK calls.

**Project Length**

350 hours.

## Parsing Fortran code to SymPy

**Idea**

LFortran can parse Fortran source code to AST and then convert AST to ASR.
This ASR will then get inspected and Fortran expressions identified and converted to SymPy expressions.
This would allow SymPy to easily read in, alter, and write out computational Fortran code. This project would enable
many other projects in the future.

This would be a general framework, some applications of this (some of which can
be part of this project):

* load the right hand side expressions and generate manufactured solution
* check that a special function (e.g., spherical harmonics) Fortran
  implementation has the right expressions in it

Part of this project can also be to implement a capability in LFortran
to track the values of variables ("x") that go into an expression when you
actually run the code on production data.

A separate project idea is to:

* optimize floating point expressions (à la https://herbie.uwplse.org/)
* Based on the range of "x" (and other variables), determine which
symbolic simplifications make sense to make things more accurate --- and to
provide faster implementations of special functions, say if it is determined
that "x" in sin(x) is in the range [0, 1e-3], then there are much faster
polynomial approximations that give the same accuracy (the same might be
possible if the range is say [1.5, 1.7], or any other finite range).

See https://github.com/sympy/sympy/wiki/GSoC-Ideas#optimize-floating-point-expressions for the expansion of this idea, as this capability is independent of
LFortran.

**Project Length**

350 hours.

# Idea Prompts

* Linear algebra
  * Improve the matrices module documentation
  * Refactor the ``MatrixBase`` class.
  * Add more special matrices to the matrix expressions module, and migrate some special matrices from the quantum physics
    module.
  * Add more matrix decomposition methods: Schur Decomposition, Polar Decomposition,
    Hermite Decomposition, ...
  * Make the matrices use the specialized data types (Modular Integers, Gaussian Rationals, Polynomial Ring, ...) from the
    ``polys`` module.

* improve the integration algorithm
  * integration of functions on domains of maximum extent, etc.
  * Interesting idea: "SYMBOLIC COMPUTATION OF INTEGRALS BY RECURRENCE" by
    MICHAEL P. BARNETT
  * A Simple Method for Computing Some Pseudo-Elliptic Integrals in Terms of Elementary Functions,
    https://arxiv.org/pdf/2004.04910.pdf

* definite integration & integration on complex plane using residues.  Note
  that we already have a strong algorithm that uses Meijer G-Functions
  implemented.  So we need to first determine if such an algorithm would be
  worthwhile, or if it would be better to extend the current algorithm.  Note
  that there are many integrals that are easy to compute using residues that
  cannot be computed by the current engine.  Other possibilities:  the ability
  to closed path integrals in the complex plane, which is not possible with
  the Meijer G algorithm.
  * https://www.researchgate.net/publication/312366307_Contour_Integration_or_what_is_still_missing_in_Mathematica_Part_1_Residues_and_Contour_Integration
  * https://www.researchgate.net/publication/312343785_Contour_Integration_or_what_is_still_missing_in_Mathematica_Part_2_Construction_of_sophisticated_Contour_Paths_Location_of_Poles_insideoutside_Closed_Contours_Special_Functions_Representations_by_Cont
  * https://www.researchgate.net/publication/319554309_Contour_Integration_or_what_is_still_missing_in_Mathematica_Part_3_Contour_Integrals_of_Functions_with_Branch_Cuts
  * http://www.cs.kent.edu/~pwang/Paul-phd-dissertation.pdf
  *

* Groebner bases and their applications in geometry, simplification and
  integration
  * improve Buchberger's algorithm and implement Faugere F4 (compare their
    speed) _Note: This has already been implemented by a previous GSoC
    student.  Please check with us to see the current state of Groebner bases
    in SymPy_
* improve polynomial algorithms (gcd, factorization) by allowing coefficients
  in algebraic extensions of the ground domain
* implement efficient multivariate polynomials (arithmetic, gcd,
  factorization)
  * Implement a sparse representation for polynomials (see the dummy files in
    sympy/polys/ starting with "sparse" in the SymPy source code for a start
    to this project).
  * Figure out which representations to use where (sparse vs. dense).
  * implement efficient arithmetic (e.g. using geobuckets (Yan) or heaps
    (Monagan & Pearce))
* improve SymPy's pattern matching abilities (efficiency and generality)
  * implement similarity measure between expression trees
  * expression complexity measures (e.g. Kolmogorov's complexity)
  * implement expressions signatures and heuristic equivalence testing
  * implement semantic matching (e.g. expression: cos(x), pattern: sin(a*x) +
    b)
    * e.g by using power series for this purpose (improve series speed)
  * Expand the capabilities of Wild() and match() to support regular
    expression-like quantifiers.
* improve simplification and term rewriting algorithms
  * add (improve) verbatim and semi-verbatim modes (more control on expression
    rewriting)
  * implement more expression rewrite functions (to an exact form that user
    specifies).  This may involve rewriting the rewrite framework to be more
    expressive.  For example, should cos(x).rewrite(sin) return sqrt(1 -
    sin(x)**2) or sin(pi/2 - x)?
  * maybe put transformation rules in an external database (e.g. prolog), what
    about speed?
  * improve context (e.g. input) depended simplification steps in different
    algorithms
      * e.g. the integrator needs different sets of rules to return "better"
        output for different input
      * but there are more: recurrences, summations, solvers, polynomials with
        arbitrary coefficients
  * what about information carried by expressions?
      * what is simpler: chebyshevt(1, x) or x ?
      * what is simpler: chebyshevt(1000, x) or (...) ?
  * improve trigonometric simplification. See for example the paper by fu et. al.
* implement symbolic (formal) logic and set theory
  * implement predicate (e.g. first-order), modal, temporal, description
    logic
  * implement multivalued logic; fuzzy and uncertain logic and variables
  * implement rewriting, minimization, normalization (e.g. Skolem) of
    expressions
  * implement set theory, cardinal numbers, relations etc.
  * This task is heavily tied to the assumptions system.
* implement symbolic global optimization (value, argument) with/without
  constraints, use assumptions
* continue work on objects with indices (tensors)
  * include the index simplification algorithms used in
    [xAct](http://www.xact.es/) and [cadabra](http://cadabra.phi-sci.com/).
* generalized functions - Dirac delta, P(1/x), etc... Convolution, Fourier
  and Laplace transforms
  * Fourier and Laplace transforms are implemented but we can not do many
    cases involving distributions _Is this enough alone for a project though? -Aaron_
* vector calculus, differential fields, maybe Lie algebras & groups
* parametric integrals asymptotic expansion (integral series)
* Integral equations.  See for example the work started at
  http://code.google.com/p/sympy/issues/detail?id=2344.  This could be part of
  a project on ODEs, for example.
* partial differential equations. Currently, SymPy can't solve any PDEs,
  though a few tools related to separation of variables are implemented. The
  PDE module should be structured similarly to the ODE module (see the source
  code of sympy/solvers/ode.py).
* improve SymPy's Common Subexpression Elimination (CSE) abilities.
  * Poly factorization http://cseweb.ucsd.edu/~kastner/papers/tcad06-poly_factorization_cse.pdf
* Singular analysis and test continuous.
  * find singularities of the function and classify them.
  * test the function whether it is continuous at some point or not. And in the interval.
    Note: Please discuss this idea with us if you are interested, as as it currently presented,
    it is somewhat vague.
* Control theory. systems for Maple and Mathematica might provide insight
  here. http://www.mcs.anl.gov/~wozniak/papers/wozniak_mmath.pdf might be useful.
* Diophantine Equations: SymPy does have substantial support for solving
  these, nevertheless there is more work possible to improve the solver.

# Other Related Projects

# Non-Ideas

Every year, people ask about implementing various things that we have already
decided do not belong in SymPy. Among these are:

- Out-of-scope ideas. SymPy is primarily a symbolic mathematics software.
  Ideas that are not related to **symbolic** mathematics are generally out of
  scope (with the exception of related topics like plotting or code
  generation, which are already mentioned here).
- Graph theory. The [NetworkX](http://networkx.github.com/) package already
  does a great job of graph theory in Python. If you are interested in working
  in graph theory, you should contact them.
- Numerical solvers. SymPy is a symbolic library, so the code should focus on
  solving things symbolically. There are already many libraries for solving
  problems numerically ([NumPy](http://www.numpy.org/),
  [SciPy](http://www.scipy.org/), ...).

<!--  LocalWords:  GSoC GUIs iOS Andriod sqrt sumit José Debeerst Cheb Terrab
 -->
<!--  LocalWords:  Duarte da Mota Kolokolnikov Onur Kiymaz Seref Karr Dominik
 -->
<!--  LocalWords:  Mirasyedioglu Gruntz Koepf Kauers Savly Shackell Arnon Xia
 -->
<!--  LocalWords:  McCallum Maza Changbo Bican GCD Buchberger FGLM Faugere et
 -->
<!--  LocalWords:  Fukuda al Yan's geobuckets Monagan Pearce Zippel's SPMOD
 -->
<!--  LocalWords:  Musser's EZ EEZ Gao's Hoeij LLL Gosper Marko Petkovsek für
 -->
<!--  LocalWords:  Wilf Doron Zeilberger Carsten Karr's Algorithmen mehrfache
 -->
<!--  LocalWords:  Summen Torsten Sprenger Granger Schroedinger Coulombic cse
 -->
<!--  LocalWords:  Solovay Kitaev Bosons Hartree Fock Bogoliubov KanesMethod
 -->
<!--  LocalWords:  LagrangesMethod pyglet PyOpenGL vtk mayavi mprint mlatex
 -->
<!--  LocalWords:  NDSovle InterpolatingFunction Mathics autowrap matplotlib
 -->
<!--  LocalWords:  asciart js openGL textplot Buchberger's gcd Yan prolog fu
 -->
<!--  LocalWords:  Kolmogorov's chebyshevt Skolem xAct cadabra asmeurer Vig
 -->
<!--  LocalWords:  Krastanov certik seanv wdjoyner Mateusz Paprocki mattpap
 -->
<!--  LocalWords:  Lukas hazelnusse moorepants Gede gilbertgede
 -->
