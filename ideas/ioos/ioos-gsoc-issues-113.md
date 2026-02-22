# #113

**Parent:** IOOS — Project Ideas
**Source:** https://github.com/ioos/gsoc/issues/113
**Scraped:** 2026-02-22T23:28:47.602791

---

## [GSoC Project Proposal]: Refactoring Hurricane Surrogate Model

**Labels:** project idea, GSoC26

### Project Description

The Storm Surge Modeling team at the Office of Coast Survey (OCS) has developed a Python package, [EnsemblePerturbation](https://github.com/noaa-ocs-modeling/EnsemblePerturbation), for an end to end probabilistic prediction of tropical cyclone (TC)-driven coastal flood analysis. This package handles: 

1. generating ensembles of perturbed hurricane tracks to be used as input to a hydrodynamic model, 
2. subsetting and adjusting the outputs of hydrodynamic models for post-processing, 
3. developing machine learning (ML) surrogate models for hydrodynamic model outputs, and 
4. conducting probabilistic predictions using the surrogate models. 

[EnsemblePerturbation](https://github.com/noaa-ocs-modeling/EnsemblePerturbation) has a large dependency tree which makes it difficult to be approved for use on NOAA’s operational system (Weather and Climate Operational Supercomputing System - WCOSS). The goal of this project is to reduce the external package dependency of EnsemblePerturbation to a minimum, especially as it pertains to steps 3 and 4 above. This would require skills such as familiarity with Python and object oriented programming, as well as a basic understanding of package development and machine learning. Example tasks could include:
- Refactoring or rewriting EnsemblePerturbation post processing modules to reduce package dependencies, specifically modules related to generating and using the surrogate model
  - Special emphasis on ensembleperturbation.uncertainty_quantification
  - Limit the external dependencies to Python built-in packages, numpy, scipy, sklearn, numpoly and chaospy as much as possible
  - Additional package that are acceptable include pandas, geopandas, pyproj, shapely, matplotlib, xarray, netCDF4
  - Modifying input arguments, return values, and within-package calculations such that external dependencies are reduced
- Write new tests for the refactored package
- Update downstream packages to support new updates (e.g. [StormWorkflow](https://github.com/noaa-ocs-modeling/ondemand-storm-workflow), and upcoming UPSurgeML - currently private)
- Repackaging the surrogate model into a new package (fully separated from EnsemblePerturbation)
 
This project provides a great opportunity to put your ML knowledge and coding skills into practice for developing an operational package for prediction of coastal flooding. 

Links to relevant packages and references:
- EnsemblePerturbation: https://github.com/noaa-ocs-modeling/EnsemblePerturbation
- StormEvents: https://github.com/oceanmodeling/StormEvents 
- StormWorkflow: https://github.com/noaa-ocs-modeling/ondemand-storm-workflow 
- NOAA Technical Report: https://repository.library.noaa.gov/view/noaa/66123
- Probabilistic ML model (KL-PC): https://journals.ametsoc.org/view/journals/aies/2/2/AIES-D-22-0040.1.xml

### Expected Outcomes

- **First:** Refactored EnsemblePerturbation package with updated tests and documentation
- **Second:** Draft of a new package derived from the [EnsemblePerturbation](https://github.com/noaa-ocs-modeling/EnsemblePerturbation) package with specific functionalities and limited dependencies.

### Skills Required

Technical skills: 
- Python (Libraries: SciPy, scikit-learn, Xarray)
- Familiarity with numerical modeling 
- Basic understanding of ML models
- Basic understanding of probability

Soft skills: 
- Curiosity (engage with the team, ask questions, don’t shy away)
- Responsive to communications

### Expected Project Size

175 hours

### Project Difficulty

Intermediate

### Mentor Name(s)

Fariborz Daneshvar, Soroosh Mani

### Mentor GitHub Handle(s)

@FariborzDaneshvar-NOAA , @SorooshMani-NOAA 

### Mentor Contact Email(s)

fariborz.daneshvar@noaa.gov , soroosh.mani@noaa.gov 

### Contributor Evaluation/GSoC GitHub Issue Links

_No response_

### Additional Project Background/Links

_No response_

### Previous Project Idea Link(s)

_No response_

