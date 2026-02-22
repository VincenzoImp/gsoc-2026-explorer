# #28347

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/28347
**Scraped:** 2026-02-22T23:28:47.573339

---

## Improvements to the discrete-time systems in physics.control

**Labels:** physics.control

With PRs #28318 and #28326, the `physics.control` module is now quite fully extended to work with discrete-time systems.

There are, however, still some things missing:
- [x] Implement the discrete-time version of `get_asymptotical_stability_conditions()`.
       There could be differet ways to implement this method.
       The one I'm more inclined to is explained [here](https://faculty.washington.edu/chx/teaching/me547/2_1_stability.pdf#:~:text=2.6%20Routh,plane%20Real).
      Since SymPy already has a good implementation of the continuous-time version, it could be worth reusing it for discrete-time as well.
- [ ] Implement the Z-transform (and its inverse). See the previous issue #12502 EDIT: I found this draft which could be really useful #24985
- [ ] Implement the DiscretePIDController.



