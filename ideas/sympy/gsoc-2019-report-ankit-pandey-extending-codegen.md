# Extending Codegen GSoC 2019

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/wiki/GSoC-2019-Report-Ankit-Pandey:-Extending-Codegen
**Scraped:** 2026-02-22T23:28:47.573507

---

-
-
[Notifications](https://github.com/login?return_to=%2Fsympy%2Fsympy)You must be signed in to change notification settings -
[Fork 5.1k](https://github.com/login?return_to=%2Fsympy%2Fsympy)

# GSoC 2019 Report Ankit Pandey: Extending Codegen

[3 revisions](https://github.com/sympy/sympy/wiki/GSoC-2019-Report-Ankit-Pandey:-Extending-Codegen/_history)

My name is Ankit, and I’m an undergraduate student at Grinnell College in Grinnell, Iowa.

My project for this summer had two parts: extending SymPy’s support for the
generation of code related to matrix expressions, and enabling the generation of
Fortran code through the [LFortran](https://gitlab.com/lfortran/lfortran) compiler.

I think I realized many of the goals that I described in my proposal, though there were some major differences in the plan and actual implementation.

Here’s a selection of some of the pull requests within the SymPy project that I filed over the summer:

-
**(Open)**[#16931](https://github.com/sympy/sympy/pull/16931)*LFortran code printing*- A code generator that utilizes the LFortran interpreter

-
**(Merged)**[#17022](https://github.com/sympy/sympy/pull/17022)*NumPy print support for identity*- A minor extension to the NumPy printer

-
**(Merged)**[#17041](https://github.com/sympy/sympy/pull/17041)*Add optimization of numpy code involving matrix inverses*- Introduces a
`matrix_nodes`

module that allows the optional rewriting of select matrix multiplications to an equivalent matrix solving operation

- Introduces a
-
**(Merged)**[#17223](https://github.com/sympy/sympy/pull/17223)*Rewrite of non-commutative multiplication matching*- A complete rewrite of non-commutative matching in SymPy’s core

-
**(Open)**[#17299](https://github.com/sympy/sympy/pull/17299)*Convert matrix expressions to Indexed*- Adds functionality to convert a matrix expression to a contraction
represented by an
`Indexed`

object

- Adds functionality to convert a matrix expression to a contraction
represented by an
-
**(Open)**[#17365](https://github.com/sympy/sympy/pull/17365)*Add matrix wildcards*- A wildcard capable of matching any matrix sub-expression


Additionally, I made a number of (very minor) contributions to the LFortran
project on GitLab, in the form of issues [#118](https://gitlab.com/lfortran/lfortran/issues/118), [#117](https://gitlab.com/lfortran/lfortran/issues/117), [#116](https://gitlab.com/lfortran/lfortran/issues/116), and [#110](https://gitlab.com/lfortran/lfortran/issues/110), in addition
to request [#225](https://gitlab.com/lfortran/lfortran/merge_requests/225).

The next subsections describe in more detail what changes some of these pull requests introduce.

[#16931](https://github.com/sympy/sympy/pull/16931) allows code generation through the LFortran compiler. For supported
expressions, the output is essentially identical to code produced using the
traditional `fcode`

printer:

```
>>> from sympy.abc import x
>>> from sympy.codegen.lfort import sympy_to_lfortran
>>> from lfortran.asr.pprint import pprint_asr
>>> print(lfortran.ast_to_src(lfortran.asr_to_ast(sympy_to_lfortran(3.0 + x))))
x + 3.0_dp
```

This may not seem like much, but the SymPy expression was directly converted to an LFortran abstract syntax tree, and the output itself was produced by LFortran itself (though some excess newlines have been cleaned up because of an existing bug in LFortran). While both the LFortran back end and the SymPy converter itself are far from being completed, the existing infrastructure is already in place.

[#17223](https://github.com/sympy/sympy/pull/17223) is a complete rewrite of the matching code in the core for
non-commutative expressions. While my proposal mentioned extending SymPy’s
ability to match within expressions, I eventually opted to use the existing
functionality provided by the `Wild`

class. Unfortunately, the matching code
sometimes produced incorrect results for non-commutative expressions in addition
to being completely untested. This pull request makes the behavior of `match`

for non-commutative expressions more closely resemble what already exists for
commutative expressions:

```
>>> A, B, C, D = symbols('A:D', commutative=False)
>>> W = Wild('W', commutative=False)
>>> (A*B*D).match(W)
{W_: A*B*D}
>>> (A*B*C*D).match(W*D)
{W_: A*B*C}
>>> (A*B*C*D).match(A*W*D)
{W_: B*C}
>>> (A*(B**2)*C).match(A*B*W*C) (ref:pow)
{W_: B}
>>> print((A*B*C).match(A*B*W*C)) (ref:none)
None
```

Just like with commutative wildcards, the wildcard attempts to match the largest
subexpression, expanding all-subexpressions where appropriate, such as in the
case of [{ref:pow}](https://github.com/(pow)). Additionally, wildcards must match at least one
sub-expression, as demonstrated by the `None`

returned in [{ref:none}](https://github.com/(none)).

[#17365](https://github.com/sympy/sympy/pull/17365) introduces a wildcard capable of matching matrix expressions, which
directly continues the work of [#17223](https://github.com/sympy/sympy/pull/17223) by extending it to matrices. A matrix
wildcard behaves much in the same way as a regular wildcard, though it is also
able to match the dimensions of the target expression:

```
>>> from sympy import MatrixSymbol
>>> from sympy.matrices.expressions.matexpr import MatrixWild
>>> from sympy.core.symbol import Wild
>>> A, B = MatrixSymbol('A', 3, 3), MatrixSymbol('B', 3, 3)
>>> x = Wild('x')
>>> Y = MatrixWild('Y', x, 3)
>>> (A*B).match(Y)
{Y_: A*B, x_: 3}
```

The matcher first checks for a possible candidate using the new non-commutative
matching code, then checking to see if the dimensions of the target expression
matches that of the wildcard. In this case, the dimensions of `Y`

matched that
of the target expression, and since the dimension of `Y`

itself included
a wildcard, the result of this match was also included.

The greatest possibility of extension lies in the actual matrix optimizations themselves. This project introduces only one optimization in a very specific case where a matrix product involving an inverse may be rewritten as a solving operation. With the matrix matching code in place, it should be relatively easy to define newer optimizations. There are also possibilities in extending the LFortran printer. Since the infrastructure is already in place, this should be as simple as adding additional print methods to the printing module as the LFortran project develops.
