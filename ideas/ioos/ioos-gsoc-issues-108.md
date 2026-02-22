# #108

**Parent:** IOOS — Project Ideas
**Source:** https://github.com/ioos/gsoc/issues/108
**Scraped:** 2026-02-22T23:28:47.602558

---

## [GSoC Project Proposal]: Flesh out erddapy xarray plugin and xarray-subset-grid with  CIs, tests and documentation

**Labels:** project idea, GSoC26

### Project Description

The plugin is a thin wrapper to erddapy's `to.xarray()` that provides a new engine to xarray. With this plugin xarray can load any ERDDAP netcdf-like URL instead of just OPeNDAP ones. It creates some consistency for users coming from ERDDAP by removing the requisite of knowing if the ERDDAP URL is a valid OPeNDAP one or not.

The same skills will be required for improving  xarray-subset-grid package CIs. This package aim is to create a convenient way for users to subset xarray datasets in space.

These packages continuous integration tests and deployment, and some documentation.

Detailed info can be found at https://github.com/ioos/erddapy/pull/434 and https://github.com/ioos/xarray-subset-grid/issues (GSoC 2026 labels pending)

### Expected Outcomes

A test suite with ~90% of coverage running on Continuous Integration.

### Skills Required

basic python and GitHub Actions

### Expected Project Size

350 hours

### Project Difficulty

Novice

### Mentor Name(s)

Filipe Fernandes, Micah Wengren, Chris Barker

### Mentor GitHub Handle(s)

@ocefpaf, @mwengren, `@ChrisBarker-NOAA`

### Mentor Contact Email(s)

ocefpaf@gmail.com

### Contributor Evaluation/GSoC GitHub Issue Links

_No response_

### Additional Project Background/Links

https://github.com/ioos/erddapy, https://github.com/ioos/xarray-subset-grid/

