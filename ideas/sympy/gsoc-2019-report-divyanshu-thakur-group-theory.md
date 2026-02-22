# GSoC 2019 Divyanshu Thakur: Computational Group Theory

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/wiki/GSoC-2019-Report-Divyanshu-Thakur:-Group-Theory
**Scraped:** 2026-02-22T23:28:47.571522

---

This page summarises the work that I have done during the GSoC period along with the links to PR's submitted in chronological order. See my [blog](http://divyanshu132.github.io) for weekly progress of the project.

## About Me

My name is [Divyanshu Thakur](https://github.com/divyanshu132) and I have completed my third year of Bachelor's in Computer Science from Indian Institute of Information Technology Manipur.

## Pull Requests

1. [Abelian Invariants](https://github.com/sympy/sympy/pull/16670): Implementation of Abelian Invariants algorithm for both Permutation and Finitely Presented groups.

2. [Composition Series](https://github.com/sympy/sympy/pull/16881): Computation of Composition Series for solvable groups.

3. [Polycyclic Groups](https://github.com/sympy/sympy/pull/16991): Providing SymPy with the capability to compute with polycyclic groups. Two classes namely ``PolycyclicGroup`` and base class ``Collector`` has been implemented. Polycyclic presentation has been also implemented, In addition few other methods to compute with polycyclic single generator were also implemented.

4. [Induced Pcgs and Exponent vector](https://github.com/sympy/sympy/pull/17317): Added capability to compute with polycyclic subgroups.

5. [Documenting Polycyclic Groups](https://github.com/sympy/sympy/pull/17399): Added documentation for polycylic groups. The sequence in which polycyclic presentation is computed is also explained in detail. Examples were provided for every functionality.

6. [Extended Polycyclic Group docstrings ](https://github.com/sympy/sympy/pull/17476): Other additional missing sections were introduced in the docstrings of ``pc_groups.py`` like ``Parameters``, ``Returns`` and ``See Also``.

## Future Work
A lot of things have been covered during the GSoC period, things that remain will be continued by me post GSoC and I hope this report will be useful for anyone wishes to contribute to the ``Group Theory`` module in future.
Following is a list that comprises of all the ideas which can extend my GSoC project.

 - Extending the functionalities of polycyclic groups, Implementing Canonical polycyclic sequence to check if two polycylic subgroups are equal.
 - Implementing Polycyclic orbit stabilizer.
 - Implementing Hall Subgroups.

Due to the extended work on polycyclic groups, few of the things proposed in my [proposal](https://github.com/sympy/sympy/wiki/GSoC-2019-Application-Divyanshu:-Group-Theory) were remain un-implemented. Here is a list for further reference.

 - Implementation of Quotient groups.
 - Automorphisms.

## Conclusion
This summer has been a great learning experience. I plan to actively contribute to SymPy, specifically to this project. I am grateful to my mentor, [Kalevi](https://github.com/jksuom) for reviewing my work, giving me valuable suggestions, and being readily available for discussions.
