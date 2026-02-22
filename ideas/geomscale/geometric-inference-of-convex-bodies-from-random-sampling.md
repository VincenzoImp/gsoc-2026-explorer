# Geometric Inference of Convex Bodies from Random Sampling

**Parent:** GeomScale — Project Ideas
**Source:** https://github.com/GeomScale/gsoc26/wiki/Geometric-Inference-of-Convex-Bodies-from-Random-Sampling
**Scraped:** 2026-02-22T23:28:47.593089

---

### Overview 

We aim to develop methods for geometric inference of convex bodies from random samples, using (geometric) random-walk sampling routines. Given a convex body described as an H-polytope (or by a membership oracle), the goal is to design and implement estimators for geometric quantities such as anisotropy, effective dimension, boundary activity, and behavior under random linear projections to lower dimensions. These estimators will be integrated into adaptive sampling pipelines that automatically diagnose poor geometric conditioning and trigger preprocessing steps such as rounding. The focus is on scalable, statistically meaningful diagnostics suitable for moderate to high dimensions.


### Expected Outcomes
- Estimators for anisotropy and effective dimension from sampled covariance and directional statistics.  
- Algorithms to analyze how geometric properties change under random projections to various target dimensions.  
- Diagnostics for mixing and geometric conditioning of sampled convex bodies.  
- An adaptive sampling and inference workflow integrated into Volesti/GeomScale.  

### Datasets / Benchmark Polytopes
The project will use families of convex bodies with known geometry, including:
- Standard polytopes: hypercubes, simplices, cross-polytopes  
- Random H-polytopes with controlled anisotropy  
- Product bodies and highly elongated boxes  
- Random linear projections (to multiple target dimensions) of known high-dimensional polytopes  
- Feasible regions of linear and semidefinite optimization problems  

These datasets enable systematic validation of geometric inference under dimensionality reduction, but they will be useful for other purposes as well.

**Difficulty**: High

## Size 
Large (350 hours)  


## Skills 

* Required: C++
* Preferred: Experience with linear algebra, convex geometry and algorithms

 

## Mentors

- [Vissarion Fisikopoulos](https://vissarion.github.io/) <vissarion.fisikopoulos at gmail.com> is an expert in mathematical software, computational geometry, and optimization, and has previous GSOC mentoring experience with Boost C++ libraries (2016-2017) and the R-project (2017). 
- [Apostolos Chalkis](https://tolischal.github.io) <tolis.chal at gmail.com> is a Research Engineer at Quantagonia GmbH. He is an expert in statistical software, computational geometry, and optimization, and has previous GSoC student experience (2018 & 2019) and mentoring experience with GeomScale (from 2020 to 2023).
- [Elias Tsigaridas](https://www-polsys.lip6.fr/~elias) <elias.tsigaridas at inria.fr> is an expert in computational nonlinear algebra and geometry with experience in mathematical software. He has contributed to the implementation, in C and C++, of several solving algorithms for various open source computer algebra libraries and has previous GSOC mentoring experience with the R-project (2019) and Geomscale (2020).
