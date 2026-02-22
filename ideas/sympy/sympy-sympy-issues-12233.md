# #12233

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/12233
**Scraped:** 2026-02-22T23:28:47.571589

---

## Rubi integrator

**Labels:** GSoC, integrals.rubi

A great GSoC project would be to make more progress in implementing the Rubi integrator into SymPy.

http://www.apmaths.uwo.ca/~arich/

Our current status is: https://github.com/sympy/sympy/issues/7749, that PR implements the if/then/else decision tree. However, we should probably go back and:

1) Implement some of the Rubi 4.9 pattern matching rules in SymPy for some subset of integrals, say, trig functions (this involves improving our pattern matching probably)

After that, another project is:

2) Implement a compiler for these pattern matching rules -> if/then/else decision tree

I got a permission from Albert Rich to share his TODO list for Rubi. The above two projects 1) and 2) seem like a good thing to do, given the TODO list, but we can modify it of course.

NOTE: see below for more applications of a rule based system. This framework would be useful beyond just integration, though integration algorithms are the most developed, so we should start there.

---

Rubi website projects:
1.  Update the Rubi, Mathematica and Maple test results and statistics displayed on the Rubi website.
2.  Update the repository of pattern matching rules on the Rubi website.
3.  Extend the cascading menu system to more finely select rules based on an integrand's form.
4.  Produce a histogram of rule applications categorized by integrand type, derivation type, etc.
5.  Register an appropriate domain name for Rubi and link it to the UWO site.

Rubi 4 enhancement projects:
1.  Generate a comprehensive set of test suite problems for integrand types not sufficiently tested.
2.  Find and fix the deficiencies in Rubi that will inevitably turn up when the enlarged test suite is run.
3.  Define rules for integrating elliptic and pseudo-elliptic integrals.
4.  Define rules for integrating expressions of the form
              (g cos(e+f x))^p (a+b sin(e+f x))^m (c+d sin(e+f x))^n (A+B sin(e+f x)+C sin(e+f x)^2).

Rubi 5 development projects:
1.  A program that compiles Rubi 4.9's pattern matching rules into an if-then-else decision tree.
2.  A decision tree interpreter that allows Rubi 5 to single-step through an integration using information implicitly stored in the decision tree.
3.  A program that displays the branching structure of the Rubi 5 decision tree as a simple directed graph.
4.  A program that animates the resulting decision tree graph by zooming and panning, ala Google Maps.
5.  An animation showing the descent through the decision tree graph to select a rule (much like a pinball game).

Rubi 6 development projects:
1.  An integrator that derives integration rules on the fly rather than having them hard-coded.

Rule-based system development projects:
1.  A rule-based definite integrator.
2.  A rule-based equation and inequality solver.
3.  A rule-based mathematical expression simplifier.
4.  A rule-based symbolic limit finder.
5.  A rule-based differential (ordinary and/or partial) equation solver.
6.  A rule-based matrix algebra system.

Academic papers:
1.  The rule-based integration techniques Rubi uses to produce optimal antiderivatives, and when to apply them.
2.  Flushing out a decision tree leads to the discovery of new formulas, symmetries and simplifications.
3.  Rule-based decision trees are mathematical objects subject to theoretical study (e.g. completeness, consistency, symmetry, uniqueness, etc.).
4.  The applicability of the rule-based paradigm to other areas of mathematics and science.

[RUBI rules](https://raw.githubusercontent.com/Upabjojr/RUBI_integration_rules/master/RUBI_DownValues_FullForm.txt) in an easily parseable format (maybe using [this tool](https://gist.github.com/Upabjojr/bc07c49262944f9c1eb0)).

