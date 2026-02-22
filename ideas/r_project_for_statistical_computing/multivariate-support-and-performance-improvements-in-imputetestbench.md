# Multivariate Support and Performance Improvements in imputeTestbench

**Parent:** R project for statistical computing — Project Ideas
**Source:** https://github.com/rstats-gsoc/gsoc2026/wiki/Multivariate-Support-and-Performance-Improvements-in-imputeTestbench
**Scraped:** 2026-02-22T23:28:47.626358

---

## Background

Data cleaning remains one of the most critical and time-consuming steps in Data Science and Data Analytics. Over the years, numerous methods have been proposed for processes such as imputation, outlier detection, formatting, and visualization. However, evaluating these methods rigorously on large and complex datasets remains a challenge. Tools like the [cleanTS](https://cran.r-project.org/package=cleanTS) R package ([Publication](https://www.sciencedirect.com/science/article/pii/S0925231222006117)) have automated several time series cleaning steps and improved workflow efficiency.

One of the core dependencies of **cleanTS** is the [imputeTestbench](https://cran.r-project.org/package=imputeTestbench) package ([Publication](https://journal.r-project.org/archive/2018/RJ-2018-024/index.html)). This package automates the evaluation and comparison of various imputation methods for time series data.

Currently, **imputeTestbench** mainly supports univariate time series and moderate-sized datasets. Modern datasets, however, are often multivariate and larger in scale. Therefore, there is a need to extend the package to handle multivariate time series and improve computational performance, while maintaining stability and CRAN compliance.

This proposal focuses on a realistic and focused upgrade of **imputeTestbench**, emphasizing multivariate support and improved efficiency.

---

## Related work

The **imputeTestbench** package automates the benchmarking of time series imputation methods by generating missing patterns and evaluating multiple techniques simultaneously.

The proposed updates will extend the package to support multivariate datasets and structured missing patterns. This will improve compatibility with modern datasets and complementary tools such as **cleanTS**, enabling more practical and scalable time series cleaning workflows.

The focus of this project is not a complete redesign, but a structured enhancement of the existing benchmarking framework.

---

## Details of your coding project

The goal of this project is to extend **imputeTestbench** to support multivariate time series and improve computational performance in a stable and maintainable way.

Key tasks include:

1. **Multivariate extension**

   * Extend the package to accept multivariate time series (e.g., matrices or data frames).
   * Ensure consistent time alignment across variables.
   * Enable benchmarking of imputation methods across multiple series simultaneously.
   * Provide both per-variable and aggregated performance evaluation.
   * Maintain backward compatibility with univariate workflows.

2. **Structured missing data generation**

   * Add support for block missingness (e.g., simulated sensor outage periods).
   * Allow variable-specific missing patterns.
   * Enable controlled missing proportions across multiple variables.
   * Improve realism of missing data simulation while keeping implementation simple and stable.

3. **Performance improvements and multicore support**

   * Improve internal data handling for better efficiency.
   * Integrate optional multicore processing using `future` or `foreach`.
   * Allow users to enable or disable parallel benchmarking.
   * Ensure CRAN-safe parallelization practices.

4. **Code refinement and stability**

   * Refactor selected internal components to reduce redundant computation.
   * Improve memory handling for larger datasets.
   * Maintain clear and readable code structure.

5. **Testing and documentation**

   * Expand unit testing using `testthat`.
   * Add a vignette demonstrating multivariate benchmarking.
   * Provide clear examples for structured missing data simulation.
   * Ensure the package passes CRAN checks with no Errors, Warnings, or Notes.


---

## Expected impact

With these updates, **imputeTestbench** will become more suitable for modern multivariate time series datasets while remaining lightweight and stable.

The updated version will allow researchers and practitioners to:

* Benchmark imputation methods on multivariate datasets.
* Simulate realistic missing data patterns.
* Reduce benchmarking runtime using multicore systems.
* Generate reproducible evaluation workflows.

This enhancement will improve usability in domains such as environmental monitoring, finance, sensor analytics, healthcare data analysis, and energy systems.

---

## Mentors

- **Aditya Gupta** (Evaluating Mentor): Postdoc at the University of Agder, Norway. Has a Ph.D. in data-driven solutions for environmental issues, currently working on AI for Sustainable Aquaculture. [adityagupta2590@gmail.com](https://github.com/rstats-gsoc/gsoc2026/wiki/adityagupta2590@gmail.com)

- **Neeraj Dhanraj Bokde**: Lead Researcher at Technology Innovation Institute, Abu Dhabi, and former Assistant Professor at Aarhus University, Denmark. [neerajdhanraj@gmail.com](https://github.com/rstats-gsoc/gsoc2026/wiki/neerajdhanraj@gmail.com). Has a Ph.D. in Data Science and has contributed to multiple R packages on time series analysis.

---

## Tests

Students, please complete one or more of the following before contacting the mentors:

* **Easy:** Download the [imputeTestbench](https://cran.r-project.org/package=imputeTestbench) package and demonstrate it on a naturally occurring time series. Document your work using RMarkdown.

* **Medium:** Propose a structured missing data simulation design for multivariate time series and explain how you would integrate it into the current architecture.

* **Hard:** Implement a basic multivariate wrapper for benchmarking (supporting matrix input) and create a vignette. Ensure the package passes with no Error/Warning/Note using [https://win-builder.r-project.org/](https://win-builder.r-project.org/).

---

## Solutions of tests

Contributors, please post a link to your test results below:

| Contributor Name | GitHub Profile | Test Results |
| ---------------- | -------------- | ------------ |
