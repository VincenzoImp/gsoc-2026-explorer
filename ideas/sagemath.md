# SageMath — Project Ideas

**Source:** https://wiki.sagemath.org/GSoC/2026
**Scraped:** 2026-02-22T23:28:47.599784

---

## Introduction

Welcome to [SageMath](/ideas/sagemath/sagemath)'s Ideas Page for GSoC 2026! ([Last year 2025](/ideas/sagemath/2025))

The [Timeline](https://summerofcode.withgoogle.com/how-it-works/#timeline) for GSoC 2026.

Make sure you have gone through the ** information regarding application procedures, requirements and general advice**. The Application Template is also available on that wiki page. Also, please subscribe to the

[sage-gsoc](https://groups.google.com/forum/#!forum/sage-gsoc)mailing list and the Sage developer list. Archives of past GSoC project ideas can be found

[here](/ideas/sagemath/gsoc).

We also **require** you to show us that you are able to execute actual development by submitting a relevant Pull Request and/or reviewing a Pull Request of the project you are interested in applying to. The [developer guide](http://doc.sagemath.org/html/en/developer/index.html) is a great comprehensive resource that can guide you through your first steps in contributing to [SageMath](/ideas/sagemath/sagemath).

Apart from the project ideas listed below, there is also a wishlist for new features in our [open GitHub Issues](https://github.com/sagemath/sage/issues?q=sort%3Aupdated-desc+is%3Aopen). They might contain or inspire the perfect project idea for you that we didn't even think about! Note that projects can be one of three lengths:

- Short: 90 hours
- Medium: 175 hours
- Large: 350 hours

Contents

-
[Project Ideas](https://wiki.sagemath.org#Project_Ideas)-
[Coordinate the graded commutative algebra and exterior algebra implementations and Gröbner bases](https://wiki.sagemath.org#Coordinate_the_graded_commutative_algebra_and_exterior_algebra_implementations_and_Gr.2BAPY-bner_bases) -
[Add additional combinatorial (Hopf) algebras and additional bases](https://wiki.sagemath.org#Add_additional_combinatorial_.28Hopf.29_algebras_and_additional_bases) -
[Refactor the diagram algebras/monoids and add new ones](https://wiki.sagemath.org#Refactor_the_diagram_algebras.2Fmonoids_and_add_new_ones) -
[Improve (free) module implementations](https://wiki.sagemath.org#Improve_.28free.29_module_implementations) -
[Create an interface to the SmallGrp database](https://wiki.sagemath.org#Create_an_interface_to_the_SmallGrp_database) -
[Implement representations of Lie algebras and quantum groups](https://wiki.sagemath.org#Implement_representations_of_Lie_algebras_and_quantum_groups) -
[Implement KLR algebras and their representations](https://wiki.sagemath.org#Implement_KLR_algebras_and_their_representations) -
[Implement a solver for the Killing equations](https://wiki.sagemath.org#Implement_a_solver_for_the_Killing_equations) -
[Provide an implementation of q- and qt-characters](https://wiki.sagemath.org#Provide_an_implementation_of_q-_and_qt-characters) -
[Interface combinatorial species and Usain-Boltz](https://wiki.sagemath.org#Interface_combinatorial_species_and_Usain-Boltz) -
[Interface FriCAS guessing routines with the lazy power series ring](https://wiki.sagemath.org#Interface_FriCAS_guessing_routines_with_the_lazy_power_series_ring) -
[Provide a direct interface to FriCAS](https://wiki.sagemath.org#Provide_a_direct_interface_to_FriCAS)

-


# Project Ideas

Here is a list of project proposals with identified mentors. Other well-motivated proposals from prospective contributors involving [SageMath](/ideas/sagemath/sagemath) in a substantial way will be gladly considered, as well.


## Coordinate the graded commutative algebra and exterior algebra implementations and Gröbner bases

Mentor |
Travis Scrimshaw |
Area |
Algebra, Performance |
Skills |
Understanding of abstract algebra and Cython. Knowledge of Gröbner basis is strongly recommended. |
Length |
175 hour and 350 hour variants |
Difficulty |
Medium-hard |

A graded commutative algebra (GCA) is an algebra where the even generators commute and the odd generators skew-commute. The implementation currently relies on singular's library [plural](https://www.singular.uni-kl.de/Manual/4-0-2/sing_469.htm) as a quotient ring of a g-algebra. [SageMath](/ideas/sagemath/sagemath) has a native implementation of the exterior algebra, but it does not interface well with the GCA implementation. The primary goal of this project would be to improve the interaction between the two implementations; likely with a native implementation of GCAs. A second goal would be to improve the implementation of [SageMath](/ideas/sagemath/sagemath)'s implementation of Gröbner bases for the exterior algebra, which is currently quite slow (see, e.g., [#34437](https://github.com/sagemath/sage/issues/34437)). For the ambitious, these computations would be extracted to an independent C++ library for many common rings (implemented using other libraries).


## Add additional combinatorial (Hopf) algebras and additional bases

Mentor |
TBD |
Area |
Algebra, Combinatorics |
Skills |
Foundations in algebra and combinatorics, experience reading research papers recommended. |
Length |
175 hours and 350 hours variants |
Difficulty |
Medium |

There are a number of combinatorial Hopf algebras (CHAs) currently implemented in [SageMath](/ideas/sagemath/sagemath). However, there are a number of bases that are known and not yet implemented. For example, the double Schurs (as defined by Molev), and (weak) dual (canonical) Grothendiecks. There are also a number of related non-symmetric but still important polynomials that [SageMath](/ideas/sagemath/sagemath) would benefit from providing. The goal of this project is to implement more of these bases and combinatorial (Hopf) algebras.


## Refactor the diagram algebras/monoids and add new ones

Mentor |
TBD |
Area |
Algebra, Combinatorics |
Skills |
Foundations in algebra and combinatorics, experience reading research papers recommended. |
Length |
175 hours and 350 hours variants |
Difficulty |
Medium |

The diagram algebras (i.e., subalgebras of the partition algebra) are implemented using code that has a number of redundancies that makes it hard to extend for new subalgebras. The main goal of this project is to refactor the underlying implementation in order to make it easier to implement new diagram algebras such as the Motzkin algebra. Furthermore, we will want to refactor the code so that the underlying diagram multiplication can be manipulated as a monoid. As an optional part, this would provide the cellular bases of these algebras in certain cases.


## Improve (free) module implementations

Mentor |
TBD |
Area |
Linear Algebra, Performance, Refactoring |
Skills |
Understanding of linear algebra and object-oriented programming. Cython experience is highly recommended. |
Length |
175 hours |
Difficulty |
Medium-easy |

[SageMath](/ideas/sagemath/sagemath) has multiple implementations of free modules:

1. Finite dimensional coordinate representations in the "standard" basis using `FreeModule` that provides both a dense and sparse implementation. 2. Using `CombinatorialFreeModule` (CFM) as (possibly infinite dimensional) sparse vectors.

There are various benefits to each implementation. However, they are largely disjoint and would mutually benefit from having a common base classes. In particular, having a dense implementation for CFM elements for applications that require heavier use of (dense) linear algebra. The goal of this project is to refactor these classes to bring them closer together (although they will likely remain separate as they are likely not fully compatible implementations for the parents).


## Create an interface to the SmallGrp database

Mentor |
TBD |
Area |
Group Theory |
Skills |
Group Theory, GAP and Python experience |
Length |
350 hours |
Difficulty |
Medium-hard |

Create a convenient Pythonic interface to the small groups database that wraps the [SmallGrp](https://gap-packages.github.io/smallgrp/) GAP package. This will enable to create all small groups satisfying certain properties (e.g. abelian, solvable, non-nilpotent, given order) in an easy way, and to provide information about them. This project should also aim to improve the connection between the implementations of permutation, matrix and finitely presented groups in Sage`Math. This can also include programmable access to information about each group, like the subgroup lattice, as in `[GroupNames](http://groupnames.org).

As an example, the interface might be `SmallGroups(60, nilpotent=True, type="permutation")` for an iterator that return Sage's PermutationGroup objects of all nilpotent groups of order 60, say sorted by GAP ID. For the implementation, the SmallGroups class might inherit from [ConditionSet](https://doc.sagemath.org/html/en/reference/sets/sage/sets/condition_set.html#sage.sets.condition_set.ConditionSet), and add methods for the information the SmallGrp GAP package provides such as cardinality and short summary as in SmallGroupsInformation.


## Implement representations of Lie algebras and quantum groups

Mentor |
Travis Scrimshaw |
Area |
Algebra |
Skills |
Foundations in algebra and representation theory |
Length |
175 hours and 350 hours variants |
Difficulty |
Medium |

Lie algebras, their associated quantum groups, and their representations are an important object with deep applications to physics. For this project, we want to construct a general framework for the representations of these algebraic objects and implement some general methods for algorithmically building certain (irreducible) representations.


## Implement KLR algebras and their representations

Mentor |
Travis Scrimshaw |
Area |
Algebra |
Skills |
Foundations in algebra and representation theory |
Length |
175 hours and 350 hours variants |
Difficulty |
Medium-Hard |

KLR algebras, also known as quiver Hecke algebras, categorify representations of quantum groups through their representations. The goal of this project is to implement these algebras in different bases, the modules of the KLR algebras, and their corresponding crystal structure. For a shorter variant, one can only implement the modules.


## Implement a solver for the Killing equations

Mentor |
Travis Scrimshaw |
Area |
Analysis, PDEs |
Skills |
Understanding of PDEs is highly recommended |
Length |
350 hours |
Difficulty |
Hard |

The Killing equations are a system of PDEs that determines the Killing vector field on a pseudo-Riemannian manifold, a vector that preserves the metric and has many other important properties. The goal of this project is to implement a program to solve the system of equations on a given manifold in some form.


## Provide an implementation of q- and qt-characters

Mentor |
Travis Scrimshaw |
Area |
Algebra, Combinatorics |
Skills |
Foundations in algebra and combinatorics, experience reading research papers recommended. |
Length |
175 hours |
Difficulty |
Easy-Medium |

q-characters and qt-characters encode the essential information about finite dimensional affine Lie algebra representations. This project would provide an implementation of the FM algorithm and its t-deformed variation due to Nakajima, a method to compute the qt-characters of simple modules, and perform manipulations in this character ring.


## Interface combinatorial species and Usain-Boltz

Mentor |
Martin Rubey |
Area |
Combinatorics |
Skills |
excellent understanding of recursive definitions and python |
Length |
175 hours |
Difficulty |
Easy-Medium |

We want to be able to create large random structures of a family of combinatorial objects ("species") given by a recursive definition. Standard examples are various families of rooted trees. In this project you will achieve this by providing an interface to [Usain-Boltz](https://gitlab.com/ParComb/usain-boltz). The first and probably hardest step is to implement a method that computes a grammar for species. The interfacing to Usain-Boltz will then be comparatively easy.


## Interface FriCAS guessing routines with the lazy power series ring

Mentor |
Martin Rubey |
Area |
Combinatorics |
Skills |
familiarity with |
Length |
90 hours |
Difficulty |
Easy |

FriCAS provides some routines that guess a formula for a sequence given its first few values. While this is currently accessible via, for example, `fricas.guessPRec`, the result is not as easy to manipulate as it could be. To fix this, you will provide a method that transforms the result of such a routine into its [SageMath](/ideas/sagemath/sagemath) equivalent.


## Provide a direct interface to FriCAS

Mentor |
Martin Rubey |
Area |
external packages |
Skills |
familiarity with interfacing python and SBCL or ECL |
Length |
350 hours |
Difficulty |
Hard |

The current interface to FriCAS is based on pexpect, and therefore slow, especially when large lists should be transferred. The goal of this project is to provide an interface similar to what is done for Maxima. This is most likely a very hard project, and you will be mostly on your own. Some proof of concept hacks can be found at [https://groups.google.com/g/fricas-devel/c/qYzrY-92Q2A/m/P49CneVKAQAJ](https://groups.google.com/g/fricas-devel/c/qYzrY-92Q2A/m/P49CneVKAQAJ) and [https://groups.google.com/g/fricas-devel/c/ds7aqEd-lj4/m/IvUXk3ZCAgAJ](https://groups.google.com/g/fricas-devel/c/ds7aqEd-lj4/m/IvUXk3ZCAgAJ)
