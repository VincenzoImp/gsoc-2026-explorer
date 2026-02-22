# Benchmark Polytope Import Suite for volesti

**Parent:** GeomScale — Project Ideas
**Source:** https://github.com/GeomScale/gsoc26/wiki/Benchmark-Polytope-Import-Suite-for-volesti
**Scraped:** 2026-02-22T23:28:47.593292

---

## Description
volesti offers advanced algorithms for sampling and volume computation of convex polytopes, but using real-world benchmark datasets requires manual preprocessing. Standard instances like Netlib linear programming test problems and metabolic-network flux polytopes are not directly available in volesti's inequality formats.  

This project builds a compact import layer to convert these datasets into volesti-ready H-polytopes with validation, metadata, and examples.

## Objectives
1. Standard LP benchmarks → volesti H-polytopes: Convert Netlib LP test problems into explicit linear inequalities (matrix \(A\), vector \(b\), bounds) that volesti can load directly.  
   
2. Metabolic flux polytopes → volesti H-polytopes  
   - Create reproducible export path from Dingo metabolic-network models to volesti inequality format.  
   - Document "model → polytope → sampling" workflow for reproducible experiments.

3. Validation, tests, benchmark  
   - Add sanity checks (dimensions, constraint counts, structural validation).  
   - Curate small benchmark collection (Netlib + metabolic examples) with regeneration scripts.  
   - Include end-to-end tests verifying converters produce valid volesti input.

4. Documentation  
   - Write tutorials for conversion workflows and minimal sampling/volume pipelines.

## Expected Outcomes
- Converters for LP benchmarks and metabolic polytopes to volesti H-polytopes.  
- Benchmark examples with reproducible conversion recipes.  
- Documentation lowering barrier to volesti benchmarking.

**Difficulty**: Medium  
**Size**: Medium (175 hours)

## Skills Required
- C++  
- Linear programing, linear algebra

## Mentors

- [Vissarion Fisikopoulos](https://vissarion.github.io/) <vissarion.fisikopoulos at gmail.com> is an expert in mathematical software, computational geometry, and optimization, and has previous GSOC mentoring experience with Boost C++ libraries (2016-2017) and the R-project (2017). 
- [Elias Tsigaridas](https://www-polsys.lip6.fr/~elias) <elias.tsigaridas at inria.fr> is an expert in computational nonlinear algebra and geometry with experience in mathematical software. He has contributed to the implementation, in C and C++, of several solving algorithms for various open source computer algebra libraries and has previous GSOC mentoring experience with the R-project (2019) and Geomscale (2020).
