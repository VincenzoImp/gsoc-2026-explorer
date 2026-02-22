# #111

**Parent:** IOOS — Project Ideas
**Source:** https://github.com/ioos/gsoc/issues/111
**Scraped:** 2026-02-22T23:28:47.602964

---

## [GSoC Project Proposal]: Improve FIMS uncertainty reporting

**Labels:** project idea, GSoC26

### Project Description

The Fisheries Integrated Modeling System (FIMS) is an R package that uses RCPP to allow C++ to work inside of R to run statistical models for assessing the status of marine populations that are fished. Currently, FIMS calculates estimation uncertainty for all derived quantities (values calculated from combinations of parameters) in the model. The uncertainty calculations are computationally expensive and models with a large number of derived quanities are running into memory limits.

The aim of this project is to devise an interface for the user to turn on/off uncertainty reporting for specific derived quantities. 

### Expected Outcomes

1. A new interface that allows users to better control derived quantity uncertainty reporting.
2. Tests implemented in R's testthat for checking interface code and google test for checking any new C++ functions.
3. Documentation, including updates to existing vignettes with examples for running the interface.

### Skills Required

C++, R, Rcpp

### Expected Project Size

175 hours

### Project Difficulty

Intermediate

### Mentor Name(s)

Andrea Havron, Matthew Supernaw, Nathan Vaughan, Kelli Johnson

### Mentor GitHub Handle(s)

@Andrea-Havron-NOAA, @msupernaw, @nathanvaughan-NOAA, @kellijohnson-NOAA

### Mentor Contact Email(s)

andrea.havron@noaa.gov, matthew.supernaw@noaa.gov, nathan.vaughan@noaa.gov, kelli.johnson@noaa.gov

### Contributor Evaluation/GSoC GitHub Issue Links

There are several existing [issues in the FIMS repository](https://github.com/NOAA-FIMS/FIMS/issues) that are labeled "good first issue" or "low-hanging fruit" that could be worked on.

[Good First Issue](https://github.com/NOAA-FIMS/FIMS/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22)
[Low-hanging ](https://github.com/NOAA-FIMS/FIMS/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22attribute%3A%20low%20hanging%20%F0%9F%8D%8E%22)🍎

### Additional Project Background/Links

This project addesses the issue: NOAA-FIMS/FIMS#1139

### Previous Project Idea Link(s)

_No response_

