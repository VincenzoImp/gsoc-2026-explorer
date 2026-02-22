# Jaya for Modern Hyperparameter Optimization

**Parent:** R project for statistical computing — Project Ideas
**Source:** https://github.com/rstats-gsoc/gsoc2026/wiki/Jaya-for-Modern-Hyperparameter-Optimization
**Scraped:** 2026-02-22T23:28:47.626419

---

## Background

The [Jaya](https://cran.r-project.org/package=Jaya) R package implements the Jaya optimization algorithm, a gradient-free, population-based method suitable for solving single-objective and multi-objective optimization problems. Jaya is known for its simplicity and parameter-free design, making it attractive for users who seek robust optimization without extensive manual tuning.

Recent developments [published in the article](https://doi.org/10.3390/a19020133) have extended Jaya to adaptive and multi-objective settings, strengthening its methodological foundation. However, a major opportunity now lies in expanding Jaya beyond traditional engineering optimization and positioning it as a modern hyperparameter optimization (HPO) engine within the R machine learning ecosystem.

Hyperparameter tuning is central to contemporary data science workflows. Popular R ecosystems such as `mlr3`, `tidymodels`, and `caret` rely heavily on search-based tuning strategies. While Bayesian optimization and grid/random search are widely used, there remains strong demand for scalable, flexible, and mixed-type optimizers that can handle continuous, integer, categorical, and conditional parameters seamlessly.

This GSoC project proposes to transform the [Jaya](https://cran.r-project.org/package=Jaya) package into a plug-and-play hyperparameter optimization framework for R, supporting modern ML workflows while retaining Jaya’s simplicity and robustness.



## Related Work

Hyperparameter optimization in R is commonly handled through:

* Grid and random search (`caret`, `tidymodels`)
* Bayesian optimization (`mlr3mbo`, `ParBayesianOptimization`)
* Evolutionary strategies (`GA`, `DEoptim`)
* Particle swarm optimization (`pso`)

Most existing optimizers either:

* Focus primarily on continuous parameters,
* Require extensive tuning of their own control parameters,
* Or provide limited support for mixed and hierarchical search spaces.

Jaya offers a compelling alternative due to its parameter-free philosophy and stable convergence behavior. However, the current version of the Jaya package is not yet fully integrated into the ML tuning ecosystem and lacks native support for:

* Mixed-integer and categorical hyperparameters,
* Conditional parameter spaces,
* ML-native tuning workflows,
* Restart strategies tailored for model tuning.

This project aims to bridge that gap and position Jaya as a first-class hyperparameter optimization engine in R.



## Details of the Coding Project

The following enhancements will be implemented in the [Jaya](https://cran.r-project.org/package=Jaya) package:

### 1. Mixed and Conditional Hyperparameter Support

* Implement a unified search space definition layer supporting:

  * Continuous parameters (e.g., learning rate, regularization)
  * Integer parameters (e.g., tree depth, number of estimators)
  * Categorical parameters (e.g., activation function, kernel type)
  * Conditional/hierarchical parameters (e.g., booster-specific settings)
* Develop a robust encoding–decoding mechanism to map internal continuous representations to structured hyperparameter configurations.
* Prevent duplicate evaluations via parameter hashing and tracking.



### 2. Jaya-Based Hyperparameter Tuning Engine

* Introduce a new high-level function, e.g., `jaya_tune()`, for hyperparameter optimization.
* Support:

  * Cross-validation and resampling strategies
  * Custom evaluation metrics
  * Early stopping integration
  * Logging of full tuning history
* Provide tidy outputs compatible with modern ML workflows.



### 3. Plug-and-Play Integration with R ML Ecosystem

#### mlr3 Integration

* Implement a `TunerJaya` class compatible with `mlr3tuning`.
* Ensure compatibility with `paradox` parameter spaces.
* Support single- and multi-metric optimization.

#### tidymodels Integration

* Provide a wrapper compatible with `tune` workflows.
* Return results in tidy format suitable for downstream analysis.

#### caret Integration

* Implement a minimal wrapper enabling Jaya-based search within `caret::train()` workflows.



### 4. Bayesian-Like Restart Strategies

To improve robustness in hyperparameter tuning:

* Implement stagnation detection mechanisms.
* Introduce archive-guided restarts (sampling near historically strong configurations).
* Add diversity-based restarts to avoid premature convergence.
* Provide configurable restart policies without compromising the parameter-free philosophy of Jaya.



### 5. Robust Unit Testing and Continuous Integration

* Expand unit testing using `testthat`.
* Add tests for:

  * Mixed-type parameter decoding
  * Conditional parameter logic
  * Restart triggers
  * Integration compatibility
* Monitor coverage using `covr`.
* Maintain CI workflows using GitHub Actions.



### 6. Documentation and Tutorials

* Develop detailed vignettes for:

  * mlr3 integration
  * tidymodels integration
  * Neural network tuning
* Provide reproducible examples and benchmarking comparisons.
* Document the hyperparameter tuning API using `roxygen2`.



## Expected Impact

This project will reposition Jaya as a modern hyperparameter optimization engine within the R ecosystem.

Key impacts include:

* Seamless integration with mainstream ML frameworks (`mlr3`, `tidymodels`, `caret`)
* Native support for mixed and hierarchical hyperparameter spaces
* Robust tuning performance without algorithm-specific parameter tuning
* Increased adoption in machine learning, data science, and applied research

By extending Jaya into the ML ecosystem, this project significantly broadens its practical relevance beyond classical engineering optimization.



## Mentors

**Evaluating Mentor:**
**Neeraj Dhanraj Bokde**, Lead Researcher at Technology Innovation Institute, Abu Dhabi, and creator of the Jaya package. Neeraj holds a Ph.D. in Data Science, with extensive experience in R package development, optimization algorithms, and GSoC mentorship.
[neerajdhanraj@gmail.com](mailto:neerajdhanraj@gmail.com)
[https://www.neerajbokde.in/](https://www.neerajbokde.in/)

**Varun Tiwari**, Senior Researcher at the DEWA R&D Center, Dubai. Varun has substantial experience in optimization, data-driven modeling, and algorithmic development.
[varun.etrx@gmail.com](mailto:varun.etrx@gmail.com)



## Tests for Students

Students should complete at least one test before contacting mentors:

* **Easy:** Use the current Jaya package to optimize a simple machine learning model hyperparameter (e.g., tune `max_depth` in a decision tree) and document results in RMarkdown.

* **Medium:** Design a mixed-type hyperparameter search space (continuous + integer + categorical) and propose an encoding–decoding strategy for Jaya, with justification.

* **Hard:** Implement a minimal prototype of a `jaya_tune()` function that:

  * Accepts a user-defined evaluation function,
  * Handles integer parameters correctly,
  * Includes basic unit tests,
  * Builds successfully via [win-builder](https://win-builder.r-project.org/) with no Error/Warning/Note.



## Test Solutions

Students should submit their test results below:

| Contributor Name | GitHub Profile | Test Results |
| ---------------- | -------------- | ------------ |
|     |                |              |
|                  |                |              |
|                  |                |              |
