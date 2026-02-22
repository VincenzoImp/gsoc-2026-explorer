# #10006

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/10006
**Scraped:** 2026-02-22T23:28:47.571299

---

## Replacing solve() with solveset()

**Labels:** solvers, solvers.solve, solvers.solveset

This is a tracking issue for the progress forward for replacing `solve` with `solveset`. We need to figure out what this will look like in the long run, as well as what should be done before the 1.0 release. 

Some things:
- [ ] Replacing internal calls with solveset https://github.com/sympy/sympy/issues/8711
- [x] Add `solveset` (and what other functions?) to `__init__.py`
- [ ] Is the solveset API stable? Do any changes need to be made before 1.0?
- [ ] Figure out how to deprecate solve in favor of solveset. A suggestion was to make solve a higher-level wrapper to solveset. Deprecation may be needed regardless, however, because of API changes.
- [x] Document the deprecation (even if we don't end up doing a formal deprecation by 1.0, we should still document that the change is happening)
  A couple of things that needs to be done to make it, at par with solve:

implement the following
- [ ] Non-linear multivariate system
- [ ] Equations solvable by LambertW (Transcendental equation solver).
- [ ] nested (trig) expression e.g. issue #10217


