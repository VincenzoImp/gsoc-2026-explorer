# tourr: new PP indices based on scagnostics

**Parent:** R project for statistical computing — Project Ideas
**Source:** https://github.com/rstats-gsoc/gsoc2026/wiki/tourr%3A-new-PP-indices-based-on-scagnostics
**Scraped:** 2026-03-10T16:58:40.306904

---

## Background

This project will enhance the [tourr](https://github.com/ggobi/tourr) package to equip it with new methods for projection pursuit (PP) indexes based on scagnostics functions.

## Related work

The [spinebil](https://github.com/uschiLaa/spinebil) package provides functionality to diagnose potential projection pursuit indexes. The package [ferrn](https://github.com/huizezhang-sherry/ferrn/) provides diagnostics for the projection pursuit guided tour, which is available in the [tourr](https://github.com/ggobi/tourr) package. The tourr package has some existing PP indexes, and the new functionality should follow this form. The [cassowaryr](https://numbats.github.io/cassowaryr/) package contains an implementation of scagnostics that is accessible and debuggable, and suitable for developing into PP indexes.

## Details of your coding project

The project involves

* adding functions that build on cassowaryr functionality to produce new PP indexes for the guided tour.
* document code, and possibly add a new data set
* provide examples of usage of the new functionality
* develop tests for the new functions
* prepare the package with the changes for CRAN
* write a vignette providing guidance on using the new functions
* compare results from these PP guided tours with results obtained by non-linear dimension reduction methods like tSNE and UMAP
* create new PP indexes that will take a categorical variable as input, and use the scagnostic function to find the largest difference between the two groups.
* extend the PP index functions to use a penalty term to better handle a large number of variables, like the current pda index

## Expected impact

The availability of this package will provide new projection pursuit guided tours. Projection pursuit is widely used to reduce the dimension of high-dimensional data sets, to capture structure and associations that cannot be seen from principal component analysis. It is a linear dimension reduction method, so it doesn't suffer from hallucinations occurring from non-linear dimension reduction methods like t-SNE and UMAP.

## Mentors

* EVALUATING MENTOR: Di Cook [dicook@monash.edu](mailto:dicook@monash.edu) is the author of numerous R packages, including tourr, nullabor, GGally, and has had extensive GSOC experience since 2012.
* Co-mentor: Jess Leung [jessica.leung@monash.edu](mailto:jessica.leung@monash.edu) is an expert in optimisation.


## Tests

Contributors, please do one or more of the following tests before contacting the mentors above.

* Easy: Fork the [tourr](https://github.com/ggobi/tourr) package and add a new PP index function based on the scagnostic skinny. 
* Medium: Write a short vignette for the tourr package illustrating the use of the index with jellyfish optimisation. Share this using a pull request to the original repo.
* Hard: Extract a selection of daily finance data (e.g. bitcoin prices) using the [yahoofinancer](https://yahoofinancer.rsquaredacademy.com) for 2025, and use your PP index to generate a guided tour of the products to find combinations that are behaving similarly over the year. Share the code or an animated gif of this.

## Solutions of tests

Contributors, please post a link to your test results here.
- EXAMPLE CONTRIBUTOR 1 NAME, LINK TO GITHUB PROFILE, LINK TO TEST
  RESULTS.
- Jaydeep Pokhariya, [Github](https://github.com/Jaydeep869), [PR For Easy and Medium Test](https://github.com/ggobi/tourr/pull/140), [Hard Test](https://github.com/Jaydeep869/tourr-hard-test)
- Vaibhav Manihar, [Github](https://github.com/vai-man), [PR for Easy and Medium Tests](https://github.com/ggobi/tourr/pull/141), [Hard Test Gist](https://gist.github.com/Vai-Man/1831cf8cf31b08a602cb48331b519cab)
