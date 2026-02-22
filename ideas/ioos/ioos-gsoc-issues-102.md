# #102

**Parent:** IOOS — Project Ideas
**Source:** https://github.com/ioos/gsoc/issues/102
**Scraped:** 2026-02-22T23:28:47.602477

---

## [GSoC Project Proposal]: Implement QARTOD Glider QA/QC recommendations in ioos-qc

**Labels:** project idea, GSoC26

### Project Description

Check what tests are in the QARTOD glider manual, but not implement yet. Note that some of the test are similar and may just need a new `kw` rather than a fresh implementation. Ideally we should avoid code repetition. Here is a list based on the latest version of the [QARTOD manual](https://cdn.ioos.noaa.gov/media/2017/12/Manual-for-QC-of-Glider-Data_05_09_16.pdf):

Test 1) Timing/Gap Test (Required)
Test 2) Syntax Test (Required)
Test 3) Location Test (Required)
Test 4) Gross Range Test (Required)
Test 5) Pressure Test (Required)
Test 6) Climatology Test (Strongly Recommended)
Test 7) Spike Test (Strongly Recommended)
Test 8) Rate of Change Test (Strongly Recommended)
Test 9) Flat Line Test (Strongly Recommended)
Test 10) Multi-Variate Test (Suggested)
Test 11) Attenuated Signal Test (Suggested)
Test 12) Previous Profile Test (Suggested)
Test 13) TS Curve/Space Test (Suggested)
Test 14) Density Inversion Test (Suggested)

Those that are already implemented in some way or another may need either a new  keyword option for glider, or improved documentation with sane default values for gliders. A good proposal would also include notebook examples with real glider data. Here are some data and a notebook for inspiration:

Possible data files for testing:
  - from https://github.com/ioos/ioos_qc/issues/58 we have https://github.com/ocefpaf/gdm/tree/main/tests/datasets/ru16-20110810T1330

Notebook example for glider QA/QC:
   - https://github.com/ioos/ioos_qc/pull/94

Bonus points would go for proposals that expand on QARTOD by contacting the glider community and augment ioos-qc with extra QA/QC rules, like the ones from the OG community and the IOOS own glider-dac:


  - https://github.com/OceanGlidersCommunity/glider-tools-list
  - https://github.com/ioos/glider-dac/issues/478

### Expected Outcomes

Improved docs, new glider QA/QC functions and some examples on how to use the library with real glider data.

### Skills Required

Intermedia Python

### Expected Project Size

350 hours

### Project Difficulty

Intermediate

### Mentor Name(s)

Filipe Fernandes, Callum Rollo

### Mentor GitHub Handle(s)

@ocefpaf, @callumrollo

### Mentor Contact Email(s)

ocefpaf@gmail.com

### Contributor Evaluation/GSoC GitHub Issue Links

_No response_

### Additional Project Background/Links

https://github.com/ioos/ioos_qc/

### Previous Project Idea Link(s)

_No response_

