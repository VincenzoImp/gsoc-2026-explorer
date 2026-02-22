# #107

**Parent:** IOOS — Project Ideas
**Source:** https://github.com/ioos/gsoc/issues/107
**Scraped:** 2026-02-22T23:28:47.602631

---

## [GSoC Project Proposal]: Add empirical dynamic model to FIMS

**Labels:** project idea, GSoC26

### Project Description

The Fisheries Integrated Modeling System (FIMS) is an R package that uses RCPP to allow C++ to work inside of R to assess the status of marine populations that are fished. Currently, we have an age-structured assessment model and we are in the process of adding a surplus production model. It would be amazing to include an empirical dynamic model in the suite of models, which we call model families. The bulk of the code needed can be found in C++ already [rEDM](https://github.com/SugiharaLab/rEDM) but a recent [R package available on GitHub](https://github.com/tanyalrogers/GPEDM) added the Gaussian Process to it. We need a combination of this C++ and R code in our FIMS package.

### Expected Outcomes

The final outcome will be the ability to project a time series forward using EDM within FIMS. Secondarily, there will need to be formal tests added to the package to ensure that the code is implemented appropriately. We use both google tests and testthat to implement tests. The final product will be documentation, including a vignette, on how to use the EDM model within FIMS.

### Skills Required

C++, R

### Expected Project Size

175 hours

### Project Difficulty

Intermediate

### Mentor Name(s)

Andrea Havron, Molly Stevens, Nathan Vaughan, Kelli Johnson

### Mentor GitHub Handle(s)

@andrea-havron-NOAA @mollystevens-noaa @nathanvaughan-NOAA @kellijohnson-NOAA

### Mentor Contact Email(s)

kelli.johnson@noaa.gov, andrea.havron@noaa.gov, nathan.vaughan@noaa.gov, molly.stevens@noaa.gov

### Contributor Evaluation/GSoC GitHub Issue Links

There are several existing [issues in the FIMS repository](https://github.com/NOAA-FIMS/FIMS/issues) that are labeled "good first issue" or "low-hanging fruit" that could be worked on.
- [Good First Issue](https://github.com/NOAA-FIMS/FIMS/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22)
- [Low-hanging 🍎](https://github.com/NOAA-FIMS/FIMS/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22attribute%3A%20low%20hanging%20%F0%9F%8D%8E%22)

### Additional Project Background/Links

Here is a [link to the original issue](https://github.com/NOAA-FIMS/FIMS/issues/1182) in our repository.

### Previous Project Idea Link(s)

_No response_

