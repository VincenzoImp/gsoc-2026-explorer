# #101

**Parent:** IOOS — Project Ideas
**Source:** https://github.com/ioos/gsoc/issues/101
**Scraped:** 2026-02-22T23:28:47.603297

---

## [GSoC Project Proposal]: Enhancing the noaa_coops Python package

**Labels:** project idea, GSoC26

### Project Description

The noaa_coops Python package provides a wrapper for the NOAA CO-OPS Tides & Currents data APIs. This project will upgrade the noaa_coops Python package to improve usability across CO-OPS’ products, ensuring a seamless user experience while adhering to API best practices.
Improvements will include simplifying access to data requests exceeding CO-OPS Data API data length limits, and introducing support for additional CO-OPS API endpoints, such as the derived product API.


### Expected Outcomes

1. Automated Data Iteration: Upgrade the method to accept date ranges exceeding NOAA’s API limits. The logic will automatically chunk the request into compliant time blocks and concatenate the results.

2. Throttling & Error Handling: Implement robust error handling between iterative calls to respect NOAA's throttling policies and prevent IP blocking during bulk retrieval.

3. Derived Product Support: Create new methods to interface with the Derived Product API (DPAPI). This will allow users to retrieve Inundation Statistics, Extreme Water Levels, and Sea Level Trends directly.

4. Metadata Refinement: Enhance retrieval and storage of metadata. For example, add support to store depth bins for historical currents and expanded station resource details.

5. Maintenance: Address existing bugs and feature requests listed in the repository's GitHub issues.

6. Presentation: Present the enhancements accomplished with the package to internal team members. 

### Skills Required

Intermediary Python 

### Expected Project Size

90 hours

### Project Difficulty

Intermediate

### Mentor Name(s)

Tigist Jima, Matthew Conlin, Gregory Clunies

### Mentor GitHub Handle(s)

@tjima, @conlin-matt, @GClunies

### Mentor Contact Email(s)

tigist.jima@noaa.gov, matthew.conlin@noaa.gov, greg.clunies@gmail.com

### Contributor Evaluation/GSoC GitHub Issue Links

_No response_

### Additional Project Background/Links

The current [noaa_coops](https://github.com/GClunies/noaa_coops) repo is here.

### Previous Project Idea Link(s)

_No response_

