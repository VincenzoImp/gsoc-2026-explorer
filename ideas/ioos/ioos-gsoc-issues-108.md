# #108

**Parent:** IOOS — Project Ideas
**Source:** https://github.com/ioos/gsoc/issues/108
**Scraped:** 2026-03-10T16:58:40.284719

---

## [GSoC Project Proposal]: Flesh out erddapy xarray plugin and xarray-subset-grid with  CIs, tests and documentation

**Labels:** project idea, GSoC26

### Project Description

## `erdappy`
The `erddapy` xarray plugin (https://github.com/ioos/erddapy) is a thin wrapper to erddapy's `to.xarray()` that provides a new engine to xarray. With this plugin xarray can load any ERDDAP netcdf-like URL instead of just OPeNDAP ones. It creates some consistency for users coming from ERDDAP by removing the requisite of knowing if the ERDDAP URL is a valid OPeNDAP one or not.

## `xarray_subset_grid`

The` xarray_subset_grid` package is an xarray extension that provides the ability to generate subsets of large oceanographic model results. Many oceanographic (and meteorologic) models are run on massive grids, with millions of nodes – end users often need only a small subset of the entire model domain (for instance one Bay or Estuary), and having to download and work with huge datasets is untenable. The package is designed to work with rectangular, curvilinear, and unstructured grid systems.

Both of these packages are currently functional, but need improvements to the documentation, test and Continuous Integration (CI) infrastructure, as well as attention to additional issues and bug reports that have been identified.

Detailed info can be found at:

[ioos/erddapy#434](https://github.com/ioos/erddapy/pull/434) [This is a merged PR – doesn’t seem to be the right one? Maybe just point to: https://github.com/ioos/erddapy/issues]

and 

https://github.com/ioos/xarray-subset-grid/issues 

(GSoC 2026 labels pending)


### Expected Outcomes

Test suites with >=90% of coverage running on Continuous Integration.
 
Major functionality documented.

Major bugs / issues addressed.


### Skills Required

Basic Python xarray, pytest
GitHub Actions
Sphinx documentation System 
 
### Expected Project Size

350 hours
 
### Project Difficulty

Novice / Intermediate
 
### Mentor Name(s)

Filipe Fernandes, Micah Wengren, Chris Barker
 
### Mentor GitHub Handle(s)

[@ocefpaf](https://github.com/ocefpaf), [@mwengren](https://github.com/mwengren), [@ChrisBarker-NOAA](https://github.com/ChrisBarker-NOAA)

 
### Mentor Contact Email(s)
[ocefpaf@gmail.com](mailto:ocefpaf@gmail.com)

(should we add Micah and Chris ?) 
 
### Contributor Evaluation/GSoC GitHub Issue Links

_No response_
 
### Additional Project Background/Links

https://github.com/ioos/erddapy
https://github.com/ioos/xarray-subset-grid/


