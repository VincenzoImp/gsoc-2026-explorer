# Expose sampling and volume on spectrahedra to R interface of volesti

**Parent:** GeomScale — Project Ideas
**Source:** https://github.com/GeomScale/gsoc26/wiki/Spectrahedra-R-interface
**Scraped:** 2026-02-22T23:28:47.592963

---

## Overview 

Sampling from [Spectrahedra](https://en.wikipedia.org/wiki/Spectrahedron) and computing their volume is a fundamental problem in applied mathematics. 
The aim of this project is to expose in the R interface of `volesti` the C++ functions that are used to sample and compute volumes of Spectrahedra.

### References

[1] Sampling the feasible sets of SDPs and volume approximation - Chalkis, Fisikopoulos, Repouskos, Tsigaridas, 2020 [pdf](https://web.archive.org/web/20210715200233id_/https://hal.inria.fr/hal-02572792/document) 

## Details of your coding project

The contributor will edit the R functions `volume` and `sample_points` of `volesti` to support Spectrahedra. An R class that represents Spectrahedra already exists. Rcpp methods should be used to call the C++ functions from the R interface and there are already many examples to follow.   

**Difficulty**: Medium

## Size 
Medium (175 hours)  


## Skills 

* Required: C++, R
* Preferred: Experience with linear algebra

 

## Mentors

- [Vissarion Fisikopoulos](https://vissarion.github.io/) <vissarion.fisikopoulos at gmail.com> is an international expert in mathematical software, computational geometry, and optimization, and has previous GSOC mentoring experience with Boost C++ libraries (2016-2017) and the R-project (2017). 
- [Apostolos Chalkis](https://tolischal.github.io) <tolis.chal at gmail.com> is a Research Engineer at Quantagonia GmbH. He is an expert in statistical software, computational geometry, and optimization, and has previous GSoC student experience (2018 & 2019) and mentoring experience with GeomScale (from 2020 to 2023).


Students, please contact the mentors after completing at least one of the tests below.

## Tests

Students, please do one or more of the following tests before contacting the mentors above.

- Easy: Compile and run CRAN version of `volesti`. 
- Hard: Modify an existing Rcpp function in the R interface of `volesti` to provide a new option to the user. This could be something simple; not a major change is required. 

**For tips and references contact the Mentors!**
