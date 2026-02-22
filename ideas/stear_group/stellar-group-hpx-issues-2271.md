# issue #2271 on HPX bug tracker

**Parent:** Ste||ar group — Project Ideas
**Source:** https://github.com/STEllAR-GROUP/hpx/issues/2271
**Scraped:** 2026-02-22T23:28:47.614512

---

## Add vectorization to the par_vec (aka par_unseq) implementations of the parallel algorithms

**Labels:** type: compatibility issue, category: algorithms, project: GSoC, tag: pinned

The `par_vec` (aka `par_unseq`) policy allows interleaving of element access functions, e.g. it is safe to the iterations of the algorithm.

Explicit engagement of compiler vectorizers through pragmas is probably the best way to ensure this occurs (e.g. `#pragma simd`, `#pragma omp simd`).

I will probably take a look into doing this myself while preparing my CppCon talk on parallel algorithms.


