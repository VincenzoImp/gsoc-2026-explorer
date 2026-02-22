# #110

**Parent:** IOOS — Project Ideas
**Source:** https://github.com/ioos/gsoc/issues/110
**Scraped:** 2026-02-22T23:28:47.602886

---

## [GSoC Project Proposal]: Echoshader: a package for interactive visualisation and dashboarding of ocean sonar data

**Labels:** project idea, GSoC26

### Project Description

Ocean sonar systems, such as echosounders, [are a core tool for observing marine life](https://storymaps.arcgis.com/stories/e245977def474bdba60952f30576908f), providing unprecedented spatial, temporal, and vertical resolution of animal distributions and behaviour. These systems are now widely deployed on ships, autonomous vehicles, and moorings, generating large and complex multivariate datasets that require advanced processing before they can be scientifically interpreted.

This project builds on [Echopype](https://echopype.readthedocs.io/en/latest/), which standardises and processes sonar data from a wide range of platforms. The goal of this GSoC project is to further develop [Echoshader](https://echoshader.readthedocs.io/en/latest/), an open-source companion visualisation tool written in Python, originally developed by a GSoC’22 contributor to facilitate ocean sonar data visualisation; it already provides building blocks such as echogram plots, ship-track maps, and 3D curtain views.

We aim to further develop the Echoshader package by extending the current functionalities, and demonstrate its capabilities on multiple types of datasets (from ships, moorings, and autonomous vehicles) through robust cloud deployment. In doing so, we aim to integrate recent developments from [engine_echo_data_viz](https://github.com/uw-echospace/engine_echo_data_viz) into echoshader.

### Expected Outcomes

**Software architecture enhancement**: 
- An updated codebase compatible with the latest dependency versions.
- A unified widget system that can be used both in notebooks and in a web-based dashboard interface.
- A modular, robust, and maintainable echoshader architecture aligned with ongoing developments in Echopype.

**New functionalities**:
- Incorporate new features prototyped in Jupyter notebooks into Echoshader, including interactive annotation modification and 3D echogram visualization.
- Prototype and implement new features in Echoshader to support visualization of mooring data.

**Demonstration and deployment**:
- Demonstrations of Echoshader functionalities on several real-world datasets spanning different platforms.
- A deployable application to enable straightforward installation and cloud or local deployment for the acoustics and broader ocean sciences community.


### Skills Required

A keen interest in environmental data, including oceanographic, acoustic, and geospatial data; Fluency in Python programming ; Experience or strong interest in working with large, multi-dimensional datasets and knowledge of xarray, dask, HoloViz, Plotly

### Expected Project Size

175 hours

### Project Difficulty

Intermediate

### Mentor Name(s)

Lloyd Izard, Wu-Jung Lee, Valentina Staneva

### Mentor GitHub Handle(s)

@LOCEANlloydizard, @leewujung, @valentina-s

### Mentor Contact Email(s)

lloyd.izard@gmail.com, leewj@uw.edu, vms16@uw.edu

### Contributor Evaluation/GSoC GitHub Issue Links

https://github.com/OSOceanAcoustics/echoshader/issues/218

### Additional Project Background/Links

- Lee, W.J., Staneva, V., Setiawan, L. D., Mayorga, E., Tuguinay, C., Butala, S., Lucca, B., & Lei, D. (2024). Echostack: A flexible and scalable open-source software suite for echosounder data processing. Proceedings of the 23rd Python in Science Conference (SciPy 2024).

- Lee, W.J., Setiawan, L., Tuguinay, C., Mayorga, E. and Staneva, V., 2024. Interoperable and scalable echosounder data processing with Echopype. ICES Journal of Marine Science, 81(10), pp.1941-1951.

- https://github.com/OSOceanAcoustics/echopype
- https://github.com/OSOceanAcoustics/echopype-examples
- https://github.com/OSOceanAcoustics/echoshader
- https://github.com/uw-echospace/engine_echo_data_viz

### Previous Project Idea Link(s)

https://github.com/ioos/gsoc/issues/35

