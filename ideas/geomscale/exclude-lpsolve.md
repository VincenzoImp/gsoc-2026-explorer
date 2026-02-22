# Exclude Lpsolve from R and C++ interfaces of volesti

**Parent:** GeomScale — Project Ideas
**Source:** https://github.com/GeomScale/gsoc26/wiki/Exclude-Lpsolve
**Scraped:** 2026-02-22T23:28:47.592807

---

## Overview 

Lpsolve is a C package (with R interface) to solve Linear Programs (LPs). GeomaScale's C++ library `volesti`
uses the C code of Lpsolve to solve LPs. These computations are useful to compute the maximum interior ball
of a convex polytope. However, for several high-dimensional polytopes, Lpsolve fails to compute the inner
ball correctly. This leads to an unexpected halt of `volesti`.
The project will exclude from the R, C++ interfaces of `volesti` the Lpsolve solver and replace it 
with other R and C++ software that can solve LPs.


## Related work

A few CRAN R packages that can solve LPs are: (i) [nloptr](https://CRAN.R-project.org/package=nloptr), (ii) [quadprog](https://CRAN.R-project.org/package=quadprog), (iii) [qpmadr](https://CRAN.R-project.org/package=qpmadr), (iv) [ipop](https://cran.r-project.org/web/packages/ROI.plugin.ipop/index.html).
However, the contributor will have to take into account other open-source R and C++ packages, with the support of the mentors.  
See also https://github.com/GeomScale/dingo/pull/104 


## Details of your coding project

The student will have (i) to make research to find the most CRAN optimization packages that can solve LPs, (ii) repeat step (i) for C++ and python software, and (iii) to perform
extended comparison experiments for the software in (i) and (ii), and (iii) implement the computation of the maximum inner ball of a polytope
in R and C++. Then, the contributor will have to integrate the new function to the python, R and C++ interface of `volesti`.  

**Difficulty**: Easy  

## Size
Medium (175 hours) 

## Skills 

* Required: C++, R, python
* Preferred: Experience with mathematical software is a plus 


## Expected impact

This is a very useful project for `volesti`, since it could be used for more complex inputs without failing to perform
the preprocess that is necessary for sampling and volume computation.

## Mentors

- [Apostolos Chalkis](https://tolischal.github.io) <tolis.chal at gmail.com> is a Research Engineer at Quantagonia GmbH. He is an expert in statistical software, computational geometry, and optimization, and has previous GSoC student experience (2018 & 2019) and mentoring experience with GeomScale (from 2020 to 2023).  

- [Manolis Christoforou](http://users.uoa.gr/~echristo/) <emchristoforou at gmail.com> is an expert in open-source development, machine learning, and optimization.  

- [Zafeirakis Zafeirakopoulos](http://zaf.zafeirakopoulos.info/index.html) <zafeirakopoulos at gmai.com> is an expert in implementing and benchmarking geometric and algebraic algorithms and has previous GSOC experience with the R-project (2018, 2019).  


Students, please contact the first and the third mentor after completing at least one of the tests below.

## Tests

Students, please do one or more of the following tests before contacting the mentors above.

- Easy: Built and run the R and C++ interfaces of `volesti`. Compute the maximum ball of a polytope using the existing functions.  
- Medium: Report one more CRAN package except for nloptr, quadprog, solveqp, and ipop that can compute the maximum ball of a polytope. Report also 2 open-source C++ packages that solve linear programs.  
- Hard: Implement the maximum ball computation with CRAN package `nloptr`.  


**For tips and references contact the Mentors!**

## Solutions of tests

Students, please post a link to your test results here.
- EXAMPLE STUDENT 1 NAME, LINK TO GITHUB PROFILE, LINK TO TEST RESULTS.
