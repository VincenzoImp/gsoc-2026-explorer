# Expose autodiff to R interface of volesti

**Parent:** GeomScale — Project Ideas
**Source:** https://github.com/GeomScale/gsoc26/wiki/Autodiff-R-interface
**Scraped:** 2026-02-22T23:28:47.593026

---

## Overview 

Automatic differentiation (autodiff) is a general procedure that performs the following task:
Assume that the we have program that, for a given input, outputs the value
of a function at the input; autodiff constructs another program that outputs the values of the derivatives 
of the function on the input (https://en.wikipedia.org/wiki/Automatic_differentiation).
This extremely useful, because in many cases the function is very complicated or even unknown 
and the thus the explicit computation of the derivatives is out of the question. 
volesti C++ library supports automatic differentiation through [autodiff library](https://autodiff.github.io/).

## Details of your coding project

The contributor will modify the R function `sample_points` of `volesti` to support sampling with automatic differentation. 
In this way, the user will be able to pass only the definition of a function (from which they want to sample) without its derivatives. 

**Difficulty**: Medium

## Size 
Medium (175 hours)  


## Skills 

* Required: C++, R
* Preferred: Experience with applied mathematics and machine learning

 

## Mentors

- [Vissarion Fisikopoulos](https://vissarion.github.io/) <vissarion.fisikopoulos at gmail.com> is an expert in mathematical software, computational geometry, and optimization, and has previous GSOC mentoring experience with Boost C++ libraries (2016-2017) and the R-project (2017). 
- [Apostolos Chalkis](https://tolischal.github.io) <tolis.chal at gmail.com> is a Research Engineer at Quantagonia GmbH. He is an expert in statistical software, computational geometry, and optimization, and has previous GSoC student experience (2018 & 2019) and mentoring experience with GeomScale (from 2020 to 2023).


Students, please contact the mentors after completing at least one of the tests below.

## Tests

Students, please do one or more of the following tests before contacting the mentors above.

- Easy: Compile and run CRAN version of `volesti`. 
- Hard: Modify an existing Rcpp function in the R interface of `volesti` to provide a new option to the user. This could be something simple; not a major change is required. 

**For tips and references contact the Mentors!**
