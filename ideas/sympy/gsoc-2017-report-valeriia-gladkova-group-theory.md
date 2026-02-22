# GSoC 2017 Valeriia Gladkova: Computational Group Theory

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/wiki/GSoC-2017-Report-Valeriia-Gladkova:-Group-Theory
**Scraped:** 2026-02-22T23:28:47.571440

---

This page summarises the work I've done during my 2017 GSoC project with links to PRs in approximately the order they were submitted. See my [blog](https://valglad.github.io) for weekly posts following my progress. The contents of this page are almost identical to [this post](https://valglad.github.io/2017/08/25/report/).

## About me

My name is Valeriia Gladkova ([valglad](https://github.com/valglad/) on github) and I am a third year (starting in October 2017) mathematics undergraduate at Oxford University, UK.

## Introduction

My project focused mainly on implementing group homomorphisms and this included implementation of rewriting systems for finitely presented groups and finite presentations of permutation groups. Additionally, I worked on finitely presented groups' `order()` method, improved simplification of subgroup presentations and implemented Sylow subgroups of permutation groups. See my [proposal](https://github.com/sympy/sympy/wiki/GSoC-2017-Application-Valeriia-Gladkova:-Group-Theory) for further information.

I'd say that I have done all that was planned plus some minor additional things here and there (discovering and fixing bugs, modifying existing functions and occasionally adding new ones beyond what was planned). However, there is certainly room for improvement, and I will mention where the work could continue as I go through the PRs.

## Pull Requests and Comments

1. [The `subgroup` method PR](https://github.com/sympy/sympy/pull/12658). Here I added `subgroup()` methods to the `PermutationGroup` and `FpGroup` classes. There were some discussions as I wondered if `FreeGroup` class could be implemented differently, but it was mostly straightforward. Perhaps, it would be useful to add a keyword argument or something like that to `FpGroup`'s `subgroup()` to allow the user to get hold of the injective homomorphism from the subgroup to the parent group.

2. [Improvements to simplifying subgroup presentations.](https://github.com/sympy/sympy/pull/12681) I didn't look at `_elimination_technique_2` because it is not used anywhere in the code at the moment but it could probably be improved as well, especially now
that some new `FreeGroupElement` methods are available: one of them is the general substitution of words that I implemented in this PR and, as I recall, I modified a few other `FreeGroupElement` methods there, as I discovered that some of them were buggy or not general enough. In a later PR (#9), I united the main elimination technique (which removes redundant generators) and the simplification of relators into one function `simplify_presentation` that can be applied to any group, not just as part of `reidemeister_presentation` (used for finding presentations of subgroups).

3. [The Smith Normal form PR.](https://github.com/sympy/sympy/pull/12705) This is the only time I did work somewhere other than the `combinatorics` module during the project. I implemented the Smith Normal form for principal ideal domains because it could be used to test if a group is infinite (not a definitive test, as if the test is negative, we can't conclude the group isn't infinite). It's a bit awkward to use at the moment because the user has to add manually a certain attribute to their matrix and it won't be resolved until some further work is done on matrices. I wrote a bit more about it in the [relevant post](https://valglad.github.io/2017/06/05/smith/).

4. [Changing the order method](https://github.com/sympy/sympy/pull/12761). The previous PR allowed returning `S.Infinity` as the order of the group in some cases where in the past the `order()` method wouldn't terminate. This PR extended it even further by calculating the order in stages. First, it attempts to find a finite index subgroup and, if it succeeds, it finds the presentation of this subgroup and applies `order()` to it. In some cases, other methods can determine that this subgroup is infinite in which case, of course, the whole group is infinite. If it's finite, then the order of the group is the index times the order of the subgroup. It is still possible that this never terminates if a finite index subgroup is not found, but it's an improvement. It can be faster than direct coset enumeration on the trivial subgroup (that was used before) but occasionally it seems too slow for even smallish groups. Usually, the slowest part is finding the subgroup's presentation but sometimes it's the search for this subgroup that takes up the time. I feel that more work should be done here to make it more efficient.

5. [The homomorphism PR.](https://github.com/sympy/sympy/pull/12827) This was a substantial PR: not only did it introduce two new classes (`GroupHomomorphism` and `FpSubgroup`), it also involved quite a lot of work in the `PermutationGroup` class in order to implement the method that expresses a given permutation in terms of the group's strong generators. At this stage only homomorphisms from `FpGroup` to `PermutationGroup` were fully implemented. The kernel computation can't handle infinite domains - maybe, this could be addressed in the future.

6. [The Rewriting System PR.](https://github.com/sympy/sympy/pull/12893) This was probably the hardest thing in the project and it probably took the longest to get merged after its review started (or at least it felt the longest). Even after it did, some problems kept coming up. It seems stable at the moment but it could certainly do with more work. One thing that comes to mind is the reduction method: it is possible to do it more efficiently with an automaton which is built and modified as more reduction rules are added to the system. Also, perhaps, the completion algorithm could be made more efficient in some way.

7. [Fixing a bug in `reidemester_presentation`.](https://github.com/sympy/sympy/pull/12973) Discovered by accident, there was a small bug in `reidemeister_presentation` that led to `order()` returning wrong answers in some specific cases.

8. [FpSubgroup's `__contains__` method.](https://github.com/sympy/sympy/pull/13028) After the homomorphism PR was merged, it was discovered that occasionally the tests involving kernels would time out. This was because FpSubgroup's `__contains__` method would go into an infinite loop on encountering elements of the conjugate form `a**-1*w*a`. It took some time to work out a way of dealing with it.

9. [Finite presentation of permutation groups.](https://github.com/sympy/sympy/pull/12986) This is something I keep working on. The general algorithm is implemented and merged, however, the efficiency could potentially be improved by using a different method based on the group's strong generating set. I have tried one implementation but it's not clear when exactly it is more efficient. Currently, I am trying to implement a different, hopefully more consistently efficient, algorithm.

**Update** (11/02/2018): [Here](https://github.com/sympy/sympy/pull/13698) is a merged pull request that introduces the function `strong_presentation(G)` and uses Sims Verify algorithm - this is more efficient for strong presentations than `presentation(G)`.

10. [Fixing a bug in `minimal_block`.](https://github.com/sympy/sympy/pull/13070) A small bug in `minimal_block` was discovered during the implementation of sylow subgroups.

11. [Adding the other homomorphism cases.](https://github.com/sympy/sympy/pull/13077) This PR enabled homomorphisms with `FpGroup` as codomain (became possible after merging the rewriting PR) and `PermutationGroup` as domain (provided the keyword argument `check` was set to `False`).

12. [Sylow subgroups PR.](https://github.com/sympy/sympy/pull/13104) This one also took a while. The main function is fairly long and it required implementation of two types of action homomorphisms and a method for finding all minimal block systems of a group. A later [related PR](https://github.com/sympy/sympy/pull/13150) made sure symmetric and alternating groups were treated separately as the generators of their Sylow subgroups can be written down in a systematic way.

13. [PermutationGroup methods for FpGroup.](https://github.com/sympy/sympy/pull/13119) This is something that gave me the idea for the project in the first place: many methods for permutation groups are already available while finitely presented groups have limited functionality. However, it's possible to use an isomorphism between a finite FpGroup and a relevant permutation group to perform computations in the latter and then go back to the former. This is precisely what this PR does for many permutation group methods.

14. [Storing coset tables in `_finite_index_subgroup`.](https://github.com/sympy/sympy/pull/13138) Until the presentation PR, it wasn't possible to get hold of an incomplete coset table for which coset enumeration returned with an error (for example if the maximum number of entries was exceeded). After it was merged, I made use of this new feature in the search for a finite index subgroup (used by `FpGroup`'s `order()` method). This somewhat decreased the required time as coset tables didn't have to be recomputed.

15. [Checking that a homomorphism from PermutationGroup is well defined.](https://github.com/sympy/sympy/pull/13151/) After the presentation PR was merged, it became possible to complete the homomorphism class by enabling the check for whether given generator images define a homomorphism when the domain is a permutation group.

16. [Sylow subgroups for Sym(n) and Alt(n).](https://github.com/sympy/sympy/pull/13150) A separate method for computing Sylow subgroups of alternating and symmetric groups, to be used as part of the main `sylow_subgroup` method. This hugely improves the performance in the case of alternating and symmetric groups.

### Additionally

A couple other PRs had to do with renaming attributes ([this one](https://github.com/sympy/sympy/pull/12732) and [this one](https://github.com/sympy/sympy/pull/12719)) or moving code around (for example, moving all of the coset table and coset enumeration functions to the file `coset_table.py` in [this PR](https://github.com/sympy/sympy/pull/12947)). These didn't include any actual work so I didn't include them in the main list.

## Conclusion

Hopefully, this report will be of use to whoever else might be interested in developing the group theory module. I plan to continue working on it myself for some time, though probably less productively as the new academic year starts soon.

Overall, this was a fun summer and I enjoyed working on this project. I'd like to thank Google for sponsoring it, SymPy for giving me the opportunity to participate and my mentor [Kalevi (jksuom)](https://github.com/jksuom) for giving me guidance and useful suggestions on my code and generally being very helpful. :)
