# #118

**Parent:** IOOS — Project Ideas
**Source:** https://github.com/ioos/gsoc/issues/118
**Scraped:** 2026-03-10T16:58:40.285556

---

## [GSoC Project Proposal]: Enhancing CrocoLakeTools with IOOS Data Sync from ERDDAP

**Labels:** project idea, GSoC26

### Project Description

CrocoLake is a dataset gathering several physical and biogeochemical ocean observations, with the goal of providing an efficient format and a unified interface for data assimilation and ocean modeling activities. [CrocoLakeTools](https://github.com/boom-lab/crocolaketools-public/tree/develop) contains the python modules to convert existing datasets to CrocoLake's structure (i.e. parquet format with common schema), and a unified interface to load them in the same dataframe.

This project consists in adding to CrocoLakeTools the ability to download and sync specific IOOS datasets from the ERDDAP data server. Together with the mentor, the contributor will identify the package to use between [erdappy](https://ioos.github.io/erddapy/) and [gliderpy](https://github.com/ioos/gliderpy), what IOOS datasets to sync, and implement a 'downloader' module in CrocoLakeTools that fetches the data and store them locally.

### Expected Outcomes

At the end of the project, it will be possible to effortlessly sync delayed-mode data from the IOOS DAC (with a focus on glider and/or animal telemetry data). This will make it easier for CrocoLake's maintainers to later convert the synced data into CrocoLake's format and serve them through CrocoLake.

### Skills Required

Python (pandas, xarray), git

### Expected Project Size

175 hours

### Project Difficulty

Novice

### Mentor Name(s)

Enrico Milanese, Mathew Biddle

### Mentor GitHub Handle(s)

@enrico-mi, @MathewBiddle

### Mentor Contact Email(s)

enrico.milanese@whoi.edu

### Contributor Evaluation/GSoC GitHub Issue Links

_No response_

### Additional Project Background/Links

_No response_

### Previous Project Idea Link(s)

_No response_

