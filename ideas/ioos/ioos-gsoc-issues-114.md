# #114

**Parent:** IOOS — Project Ideas
**Source:** https://github.com/ioos/gsoc/issues/114
**Scraped:** 2026-02-22T23:28:47.603371

---

## [GSoC Project Proposal]: Add sex structure to FIMS statistical-catch-at-age model

**Labels:** project idea, GSoC26

### Project Description

Right now, the statistical catch-at-age model in the Fisheries Integrated Modeling System (FIMS) has a single sex. Adding sex structure to allow for males, females, and hermaphrodites is high on the priority list. This will involve coding in both C++ and R, where the population dynamics are written in C++ and interacting with setting up the model and structuring the data are in R. Implementation of this code in the standard way has been done several times in other platforms but there is ample room for experimenting with sparsity and how to adjust configurations to increase model speed because we all know that fish have two sexes out in the oceans and the only reason that we simply the model to one sex is to reduce run time.

### Expected Outcomes

FIMS has yet to be implemented in many regions because there is a **HIGH** need for a sex-specific model so this feature will allow for the increase of its use across the USA. At the end of this project we would expect the following:
1. Add sex to the statistical catch-at-age model where data can be sex-specific or not and parameters can be estimated to be sex specific.
2. Report on the time cost of estimation when adding sex to the model when data on sex-specific processes do not exist.
3. (stretch) Investigate how to best combine data from males and females using functions/likelihoods when you want to collapse a 2-sex model into a single-sex model.

### Skills Required

C++, R

### Expected Project Size

350 hours

### Project Difficulty

Intermediate

### Mentor Name(s)

Kelli Johnson, Adrianne Wilson

### Mentor GitHub Handle(s)

@kellijohnson-NOAA, @awilnoaa

### Mentor Contact Email(s)

kelli.johnson@noaa.gov, adrianne.wilson@noaa.gov

### Contributor Evaluation/GSoC GitHub Issue Links

There are several existing [issues in the FIMS repository](https://github.com/NOAA-FIMS/FIMS/issues) that are labeled "good first issue" or "low-hanging fruit" that could be worked on.
- [Good First Issue](https://github.com/NOAA-FIMS/FIMS/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22)
- [Low-hanging 🍎](https://github.com/NOAA-FIMS/FIMS/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22attribute%3A%20low%20hanging%20%F0%9F%8D%8E%22)


### Additional Project Background/Links

Related to [#638](https://github.com/NOAA-FIMS/FIMS/issues/638)

### Previous Project Idea Link(s)

_No response_

