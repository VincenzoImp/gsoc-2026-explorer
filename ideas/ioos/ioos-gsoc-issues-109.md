# #109

**Parent:** IOOS — Project Ideas
**Source:** https://github.com/ioos/gsoc/issues/109
**Scraped:** 2026-02-22T23:28:47.603037

---

## [GSoC Project Proposal]: Enhancing Daily Skill Assessment Workflows for NOAA’s Surge and Tide Operational Forecast System (STOFS)

**Labels:** project idea, GSoC26

### Project Description

This project focuses on enhancing the [AUTOVAL](https://github.com/noaa-ocs-modeling/autoval/tree/v3.0.0) package, which provides daily skill assessments and statistical summaries for different STOFS components. Currently, AUTOVAL generates static HTML reports evaluating model performance across different cycles and locations. The primary goal is to transform this existing Python-based evaluation logic into an interactive Chatbot interface. This interface will allow users to query general model performance and station-specific skill, and request on-demand plots or summary tables. By the end of the GSoC period, the applicant will have developed a functional, conversational bridge between AUTOVAL's data and the end-user.

### Expected Outcomes

**Integrated Chatbot Interface**: A functional chatbot (prototype React SPA and modular component) ready for deployment on the [nowCOAST](https://nowcoast.noaa.gov/) website, allowing users to interactively query STOFS data and produce on-demand skill assessments.
**Expanded Data Integration**: Integration of new observational data sources, broadening the package’s validation capabilities beyond current limitations.
**3D Variable Assessment _(Stretch Goal)_**: If time allows following the successful integration of the first two steps, the project will aim to extend the evaluation workflow from 2D variables to 3D oceanographic parameters, including temperature, salinity, and currents.

### Skills Required

Python; Chatbot & NLP Frameworks; Data Visualization; Scientific Data Handling (especially Xarray, Numpy, Pandas, NetCDF files). Preferred additional skills: Statistical Knowledge of skill assessment metrics; Version Control; Web Development. 

### Expected Project Size

350 hours

### Project Difficulty

Intermediate

### Mentor Name(s)

Jack Reeves Eyre, Atieh Alipour, Adam Gibbons, Gregory Seroka

### Mentor GitHub Handle(s)

@JackReevesEyre-NOAA,  @AtiehAlipour-NOAA, @agibbons-NOAA, @gseroka

### Mentor Contact Email(s)

jack.reeveseyre@noaa.gov, atieh.alipour@noaa.gov, adam.m.gibbons@noaa.gov, gregory.seroka@noaa.gov

### Contributor Evaluation/GSoC GitHub Issue Links

Applicants are expected to demonstrate their technical proficiency by completing the following two-step qualification task:

**Environment Setup & Validation**: Follow the instructions in the project’s [README.md](https://github.com/noaa-ocs-modeling/autoval/blob/v3.0.0/README.md) to install the AUTOVAL package and execute the STOFS-2D-Global test case. Applicants must successfully generate the validation output and share a link to their results (e.g., a Google Drive or Cloud Storage link) as proof of setup.

**Prototype Development (Mini-Chatbot)**: Develop a lightweight Python-based chatbot that interacts with STOFS-2D-Global data stored in the cloud. The prototype should demonstrate the ability to:
- Fetch data for a specific date from the provided S3 bucket.
- Process a user query for specific stations (e.g., "Show me the skill for Station X").
- Return a simple summary and visualization in response.

The STOFS-2D-Global data bucket can be accessed here: https://noaa-gestofs-pds.s3.amazonaws.com/index.html

Example STOFS-2D-Global data for 01/25/2026: https://noaa-gestofs-pds.s3.amazonaws.com/index.html#stofs_2d_glo.20260125/

### Additional Project Background/Links

_No response_

### Previous Project Idea Link(s)

_No response_

