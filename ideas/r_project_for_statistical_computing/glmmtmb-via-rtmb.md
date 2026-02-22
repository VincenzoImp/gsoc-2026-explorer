# glmmTMB via RTMB

**Parent:** R project for statistical computing — Project Ideas
**Source:** https://github.com/rstats-gsoc/gsoc2026/wiki/glmmTMB-via-RTMB
**Scraped:** 2026-02-22T23:28:47.626233

---

## Background

The `glmmTMB` package fits generalized linear mixed models with extended features such as zero-inflation, flexible dispersion, and many additional correlation structures. It was developed with a user-interface based on `lme4` and using the `TMB` package for efficient and robust computations. The `TMB` package requires the user (in this case the `glmmTMB` developer / contributor) to code computations using a superset of `C++`. However, the C++-like `TMB` language is no longer needed for these complex calculations because a simpler, more R-like, language `RTMB` was introduced several years ago and has been gaining popularity. Most courses that were formerly taught in `TMB` have replaced it with `RTMB`. Thus, we anticipate that there will be more future `glmmTMB` developers / contributors available if the computations are written in `RTMB`.

The `glmmTMB` package is popular across many research fields, with 13,167 citations on Google Scholar for the R-suggested citation and an additional 870 for other formats of the citation. According to https://cranlogs.r-pkg.org, there are 32K downloads per month. According to https://www.datasciencemeta.com/rpackages, there have been 1,725,397 downloads in total. There were originally 10 developers (of which a handfull are still at least occasionally active) and it has aquired 13 official contributors. At least 2 PhD students have contributed to the package as part of their dissertation work.

## Related work

The `brms` package has most of the same functionality (and more), but it requires a Bayesian flavor which takes much more computation time. Other packages such as `lme4`, `mgcv`, and `sdmTMB` have some of the funtionality, but not everything. `sdmTMB` was forked from `glmmTMB` but it may lack some of the distribution families and random effect correlation structures as well as compatibility with some packages for model evaluation and presentation. `lme4` lacks zero-inflation and dispersion models. `mgcv` lacks some of the distribution families and random effect correlation structures.

## Details of your coding project

We expect the contributor to fork our package on GitHub and make the following changes as time allows:
- discuss parallelization options with `RTMB` developer (K Kristensen) to determine feasability
- determine if utils.cpp is still needed (16 lines)
- determine if init.h is still needed (27 lines)
- determine if Makevars is still needed (3 lines)
- convert glmmTMB.cpp from `C++` to `RTMB` code (1386 lines)
- convert contrib.h from `C++` to `RTMB` code (148 lines)
- convert distrib.h from `C++` to `RTMB` code (440 lines)
- rewrite Make file
- rewrite documentation of how users can add functionality `vignettes/hacking.rmd`

Tests of correctness will be performed using our built-in unit tests that will expect the forked version to give the same results as the current CRAN version.

Speed comparisons of the old and new version will be performed using large data sets that M Brooks has, including spatial and temporal correlation. 

If extra time remains, the contributor could make a new version of the [selfisher package](https://github.com/mebrooks/selfisher) which is specifically developed for fisheries gear selectivity models. It was created by forking `glmmTMB` in 2017 and rewriting the model formulas. Since forking, the two packages have diverged immensely. It would be ideal to set up the new `selfisher` fork in a way that facilitates `glmmTMB` developments to be easily ported over. Then it should be easier to get and maintian`selfisher` on CRAN.

## Expected impact

This will make it easier for members of the R community to contribute to `glmmTMB` in the future because the internal computations will be done in a language that is very similar to R. Based on community-initiated developments and discussions, we know that the community likes to add correlation structures, distribution families, and link functions.

## Mentors

Contributors, please contact mentors below after completing at least one
of the tests below.

- EVALUATING MENTOR: Mollie Brooks <molbr@aqua.dtu.dk> is the
  maintiner of R packages `glmmTMB` and `selfisher`. 
  She teaches a semester-long course on `RTMB` each spring.
- Ben Bolker <bbolker@gmail.com> is an expert in R programming,
  and has previous GSOC experience with `lme4` via the
  RStats community in 2025. Ben is the most active developer of `glmmTMB` and has taught `RTMB`.
- Kasper Kristensen <kaskr@dtu.dk> is the maintiner of R packages `TMB` and `RTMB`.


## Tests

Contributors, please do one or more of the following tests before
contacting the mentors above.

MENTORS: write several tests that potential contributors can do to
demonstrate their capabilities for this particular project.  Ask some
hard questions that will give you insight about how the contributors write
code to solve problems. You'll see that the harder the questions that
you ask, the easier it will be for you to choose between the contributors
that apply for your project!  Please modify the suggestions below to
make them specific for your project.

- Easy: something that any useR should be able to do, e.g. download
  some existing package listed in the Related Work, and run it on some
  example data.
- Medium: something a bit more complicated. You can encourage contributors
  to write a script or some functions that show their R coding
  abilities.
- Hard: Can the contributor write a package with Rd files, tests, and
  vignettes? If your package interfaces with non-R code, can the
  contributor write in that other language?

## Solutions of tests

Contributors, please post a link to your test results here.
- EXAMPLE CONTRIBUTOR 1 NAME, LINK TO GITHUB PROFILE, LINK TO TEST
  RESULTS.
1) Name: Siddhesh Akole , [GITHUB PROFILE: "Siddd-hrr"](https://github.com/Siddd-hrr)
-  [Easy-test](https://github.com/Siddd-hrr/rstats-gsoc2026-task--glmmTMB-via-RTMB-/blob/main/README.md), [Medium-test](https://github.com/Siddd-hrr/rstats-gsoc2026-task--glmmTMB-via-RTMB-/blob/main/README.md), [Hard-test](https://github.com/Siddd-hrr/rstats-gsoc2026-task--glmmTMB-via-RTMB-/blob/main/README.md)
