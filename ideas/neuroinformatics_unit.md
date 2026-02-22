# Neuroinformatics Unit — Project Ideas

**Source:** https://neuroinformatics.dev/get-involved/gsoc/2026
**Scraped:** 2026-02-22T23:28:47.579184

---

# Google Summer of Code 2026[#](https://neuroinformatics.dev#google-summer-of-code-2026)

## GSoC NIU Projects 2026[#](https://neuroinformatics.dev#gsoc-niu-projects-2026)

NIU is offering a variety of projects for GSoC 2026, organized under different software tools. Click on a project below learn more about the scope and requirements for each one.

A project can be one of three sizes: small (90 h), medium (175 h) or large (350 h). The standard coding period is 12 weeks for medium and large projects, and 8 weeks for small projects.

However, GSoC contributors can request in their proposal up to a 22-week coding period, if they know they may have other commitments or certain weeks when they will not be able to work full time on their GSoC project. During the project preparation period (called “community bonding period”), both the GSoC contributor and the mentors will agree on a schedule and sign off on it.
For more details please see our [main GSoC page](/ideas/neuroinformatics-unit/index). Please also see our [application guidelines](https://neuroinformatics.dev/guidelines.html) and our [policy on the use of AI](https://neuroinformatics.dev/ai_policy.html).

Our GSoC ideas are based within specific, larger open source packages we develop. Some of these have specific project ideas associated with them.
Others do not yet have specific project ideas, but all on this list welcome ideas developed by GSoC participants. Please reach out to us via our [GSoc Zulip channel](https://neuroinformatics.zulipchat.com/#narrow/channel/487898-Google-Summer-of-Code) to discuss.

Other projects

The list below are just project “ideas”, we are very keen to hear about other potential projects from applicants. In 2026 we are particularly interested in:

Making our software more maintainable and reducing technical debt.

Making our tools more accessible to scientists. We are keen to help practicing scientists make their first contributions to open source.


If you have any ideas within these themes, please reach out via our [GSoc Zulip channel](https://neuroinformatics.zulipchat.com/#narrow/channel/487898-Google-Summer-of-Code).

## BrainGlobe[#](https://neuroinformatics.dev#brainglobe)

[BrainGlobe](https://brainglobe.info/) is a community-driven suite of open-source Python tools. The BrainGlobe tools are widely used to process, analyse and visualise images of brains (and other related data) in neuroscientific research.

Our working language is English, but our mentors for these projects also speak Italian, French, and German.

Three BrainGlobe repositories ([morphapi](https://github.com/brainglobe/morphapi), [brainrender](https://github.com/brainglobe/brainrender), [brainreg](https://github.com/brainglobe/brainreg)) are in pure maintenance mode, and therefore excluded from any GSoC project proposals. All other BrainGlobe repositories welcome alternative project ideas!

##
Refactor `brainglobe-heatmap`

to use atlas annotations rather than mesh slices for visualisation

`brainglobe-heatmap`

is BrainGlobe’s tool to generate heatmap plots of atlases in 2 and 3D. It relies heavily on BrainGlobe’s meshes, which can cause small imprecisions in visualising data. In 2D it also can fail to slice the meshes along a plane correctly. This could be improved by moving the heatmap functions to relies on the atlas annotations instead of the meshes. There are a number of additional refactoring improvements that could be done to `brainglobe-heatmap`

.

**Deliverables**

Refactor 2D plotting functionality to use atlas annotations instead of meshes

Tests for new functionality

Ensure any refactored functionality has docstrings

A blog on the

[BrainGlobe website](https://brainglobe.info/blog/)about the work done(Stretch goal) - further improvements to

`brainglobe-heatmaps`


**Duration**
Small (~90 hours)

**Difficulty**

This project is well suited for an intermediate contributor to open source.

**Required skills**

Fluency with Python

**Nice-to-haves**

Experience with

[pytest](https://docs.pytest.org/en/stable/).Experience with visualisation libraries, in particular

[matplotlib](https://matplotlib.org/)and/or[vedo](https://vedo.embl.es/)Experience with neuroanatomy


**Potential mentors**

**Further reading**
`brainglobe-heatmap`

issue [#103](https://github.com/brainglobe/brainglobe-heatmap/issues/103) nicely demonstrates the problem and a potential solution approach.

##
Improving the user experience in `brainrender-napari`


`brainrender-napari`

allows BrainGlobe users to download and visualise a variety of neuroanatomical atlases through a graphical user interface. As BrainGlobe supports more and more atlases, we’d like to make it more convenient for users to find the atlas they are interested in, and visualise it in more custom ways.

**Deliverables**

Add sorting functionality to

`brainrender-napari`

tablesAllow users to filter atlas tables by species

Add functionality to visualise the atlas annotation with preset colours

Any added functionality will require extensive tests and documentation

A blog on the

[BrainGlobe website](https://brainglobe.info/blog/)about the work done(Stretch) add functionality to allow users to set the colours of meshes


**Duration**
Large (~350 hours)

**Difficulty**

This project is well suited for an intermediate contributor to open source.

**Required skills**

Fluency with Python

**Nice-to-haves**

Experience with

[pytest](https://docs.pytest.org/en/stable/).Experience with graphical user face libraries, in particular

[napari](https://napari.org/stable/)and/or[Qt](https://www.qt.io/)

**Potential mentors**

**Further reading**

Further details can be found in

`brainrender-napari`

issues[#22](https://github.com/brainglobe/brainrender-napari/issues/22),[#46](https://github.com/brainglobe/brainrender-napari/issues/46),[#154](https://github.com/brainglobe/brainrender-napari/issues/154), and[#218](https://github.com/brainglobe/brainrender-napari/issues/218)Initial familiarisation with

`brainrender-napari`

’s current features may happen by working through the[atlas downloading tutorial](https://brainglobe.info/tutorials/manage-atlases-in-GUI.html)and the[atlas visualisation tutorial](https://brainglobe.info/tutorials/visualise-atlas-napari.html)

##
Expand `cellfinder`

to accept different types of input data (several or single channels, 2.5 dimensions)

BrainGlobe’s `cellfinder`

tool allows researchers to detect fluorescent cells in whole-brain microscopy images. It requires whole-brain images of both a signal and a background channels as input, which not many researchers have. We’d like to expand the types of inputs `cellfinder`

support to include brain slices (essentially 2D data) and single channel inputs (no background channel).

**Deliverables**

Add functionality supporting 2.5-dimensional data

Add functionality to support single-channel data

Any added functionality will require extensive tests and documentation

A blog on the

[BrainGlobe website](https://brainglobe.info/blog/)about the work done

**Duration**
Large (~350 hours)

**Difficulty**

This project is well suited for an intermediate contributor to open source.

**Required skills**

Fluency with Python and [NumPy](https://numpy.org/)

**Nice-to-haves**

Experience with

[pytest](https://docs.pytest.org/en/stable/).Experience working with image data

Experience working with large data, e.g. using

and/or`pytorch`

`dask`


**Potential mentors**

**Further reading**

Further details can be found in

`cellfinder`

issues[#298](https://github.com/brainglobe/cellfinder/issues/298)and[#352](https://github.com/brainglobe/cellfinder/issues/352)The current

`cellfinder`

functionality can be explored by working through the[3D cell detection tutorial](https://brainglobe.info/tutorials/cellfinder-detection.html)

## Movement[#](https://neuroinformatics.dev#movement)

Markerless pose estimation tools based on deep learning, such as [DeepLabCut](https://www.mackenziemathislab.org/deeplabcut) and [SLEAP](https://sleap.ai/), have revolutionised the study of animal behaviour. However, there is currently no user-friendly, general-purpose approach for processing and analysing the trajectories generated by these popular tools. To fill this gap, we’re developing [ movement](https://movement.neuroinformatics.dev/latest/), an open-source Python package that provides a unified data analysis interface across pose estimation frameworks.

Our working language is English, but our mentors for these projects also speak Spanish and Mandarin.

## Adding I/O support for formats used in human motion tracking

The `movement`

package currently supports a variety of pose estimation formats commonly used in animal behaviour research. With this project, we would like to expand our support to file formats more commonly used in human pose estimation, such as:

**Deliverables**

Functionality to load at least 3 popular file formats for human motion tracking, such as MMPose output files, COCO keypoint data, motion capture formats or motionBIDS.

Tests to cover any added functionality.

Documentation for the new functionality.

Example use-cases in the

`movement`

[gallery](https://movement.neuroinformatics.dev/latest/examples/index.html).

**Duration**

Large (~350 hours)

**Difficulty**

This project is well suited for an intermediate contributor to open source.

**Required skills**

Fluency with Python, [NumPy](https://numpy.org/) and/or [pandas](https://pandas.pydata.org/docs/index.html).

**Nice-to-haves**

Familiarity with pose estimation frameworks and their usual workflow.

Familiarity with any of the human pose estimation formats mentioned above.


**Potential mentors**

**Further reading**

## Adding I/O support for popular animal tracking software

The `movement`

package currently supports a variety of pose estimation formats commonly used in animal behaviour research. With this project, we would like to expand our support to other file formats used in the field, such as:

point trackers, such as

[cotracker3](https://github.com/facebookresearch/co-tracker)[Bonsai’s](https://bonsai-rx.org/docs/index.html)centroid tracker[TRex’s](https://trex.run/docs/)pose and bounding box outputs

**Deliverables**

Functionality to load 2-3 of the file formats mentioned above.

Tests to cover any added functionality.

Documentation for the new functionality.

Example use-cases in the

`movement`

[gallery](https://movement.neuroinformatics.dev/latest/examples/index.html).

**Duration**

Large (~350 hours)

**Difficulty**

This project is well suited for an intermediate contributor to open source.

**Required skills**

Fluency with Python, [NumPy](https://numpy.org/) and/or [pandas](https://pandas.pydata.org/docs/index.html).

**Nice-to-haves**

Familiarity with pose estimation frameworks and their usual workflow.

Familiarity with any of the software packages mentioned above.


**Potential mentors**

**Further reading**

Further details are available in the following `movement`

issues: [#348](https://github.com/neuroinformatics-unit/movement/issues/348), [#599](https://github.com/neuroinformatics-unit/movement/issues/599)

## Adding support for tracked segmentation masks

`movement`

has initially focused on pose estimation data, but the [long term goal](https://movement.neuroinformatics.dev/latest/community/mission-scope.html) of the package is to support all animal tracking data formats that are relevant to animal behaviour research. With tools like [SAM](https://github.com/facebookresearch/sam2) or [OCTRON](https://octron-tracking.github.io/OCTRON-docs/) that track segmentation masks in videos, adding support for such data would be a valuable extension of `movement`

’s input capabilities. In this project, we would like to explore how segmentation‑based tracking data can be integrated into the `movement`

framework and design a user-friendly workflow for doing so.

**Deliverables**

Support for at least one of the file formats output by a popular segmentation and tracking software package.

Tests to cover any added functionality.

Documentation for the new functionality.

Example use-cases in the

`movement`

[gallery](https://movement.neuroinformatics.dev/latest/examples/index.html).

**Duration**

Large (~350 hours)

**Difficulty**

This project is well suited for an intermediate contributor to open source.

**Required skills**

Fluency with Python, [NumPy](https://numpy.org/) and/or [pandas](https://pandas.pydata.org/docs/index.html).

**Nice-to-haves**

Familiarity with segmentation models (such as

[SAM2](https://github.com/facebookresearch/sam2),[SAM3](https://github.com/facebookresearch/sam3)or[Ultralytics Instance segmentation with YOLO](https://docs.ultralytics.com/tasks/segment/)) and their usual workflow.Familiarity with software packages for instance segmentation applied to biology or animal behaviour research, such as

[OCTRON](https://octron-tracking.github.io/OCTRON-docs/)or[convpaint](https://guiwitz.github.io/napari-convpaint/book/Landing.html)

**Potential mentors**

**Further reading**

Further details are available in the following

`movement`

issue:[#301](https://github.com/neuroinformatics-unit/movement/issues/301)

## Adding a module for trajectory complexity metrics

Quantitative characterisation of the trajectories of moving animals is an important component of many behavioural and ecological studies, and also falls within scope for `movement`

. We would like to enable our users to perform statistical characterisation of trajectories through a variety of well-defined metrics such as straightness index, tortuosity, and sinuosity. Functions for computing these metrics could be implemented in a standalone module under [ movement.kinematics](https://github.com/neuroinformatics-unit/movement/tree/main/movement/kinematics).

**Deliverables**

Functions for computing at least 3 metrics of trajectory complexity

Tests to cover any added functionality.

Documentation for the new functionality.

Example use-cases in the

`movement`

[gallery](https://movement.neuroinformatics.dev/latest/examples/index.html).

**Duration**

Medium (~175 hours)

**Difficulty**

This project is well suited for an intermediate contributor to open source, with a background in research.

**Required skills**

**Nice-to-haves**

Research experience in a relevant field: e.g. ethology, neuroscience, behavioural ecology, conservation.


**Potential mentors**

**Further reading**

The

and its associated`trajr`

R package[paper](https://onlinelibrary.wiley.com/doi/full/10.1111/eth.12739)

## Adding a module for metrics of collective behaviour

Understanding how individuals coordinate their movements within a group is a central question in behavioural ecology, ethology, and neuroscience. Since `movement`

already supports multi-individual tracking data, it is well positioned to enable users to quantify collective behaviour through established metrics such as group polarisation (alignment of heading directions), and nearest-neighbour distances. We would like to implement functions for computing collective behaviour metrics in a dedicated module.

**Deliverables**

A detailed GitHub issue describing suitable metrics to add.

Functions for computing at least 2 metrics of collective behaviour

Tests to cover any added functionality.

Documentation for the new functionality.

Example use-cases in the

`movement`

[gallery](https://movement.neuroinformatics.dev/latest/examples/index.html).

**Duration**

Medium (~175 hours)

**Difficulty**

This project is well suited for an intermediate contributor to open source, with a background in research.

**Required skills**

**Nice-to-haves**

Research experience in a relevant field: e.g. ethology, neuroscience, behavioural ecology, conservation.


**Potential mentors**

**Further reading**

The

and its associated`swaRm`

R package[paper](https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.14460)An

[example script](https://github.com/neuroinformatics-unit/zebras-stitching/blob/main/notebooks/03_notebook_compute_behaviour_metrics.py)for computing behaviour metrics for a herd of zebras. See also the corresponding[preprint](https://arxiv.org/abs/2505.16882).

## Ethology[#](https://neuroinformatics.dev#ethology)

The main goal of [ ethology](https://github.com/neuroinformatics-unit/ethology) is to facilitate the application of a wide range of computer vision tasks to animal behaviour research, by providing a unified data analysis interface across these tasks.

Our working language is English, but our mentors for these projects also speak Spanish.

##
Expanding annotations support in `ethology`


`ethology`

is a package in early development, whose goal is to make it very easy to mix and match computer vision tools to analyse animal behaviour data. Currently, `ethology`

supports loading and curating bounding box annotation datasets.We would like to expand the set of supported annotation types to include mask annotations, and add a UI interface for defining different annotation types in `napari`

.

**Deliverables**

Support for mask annotation datasets in

`ethology`

(following the current bounding box annotations dataset).Support for defining bounding box annotations in

`napari`

: drawing, exporting to file (e.g. JSON COCO format and as`ethology`

dataset netCDF) and loading from file.Support for defining mask annotations in

`napari`

: drawing, exporting to file (e.g. JSON COCO format and as`ethology`

dataset netCDF) and loading from file.Example use-cases in the

`ethology`

[gallery](https://ethology.neuroinformatics.dev/latest/examples/index.html).(Optional) Support for defining keypoint annotations in

`napari`


**Duration**

Large (~350 hours)

**Difficulty**

This project is well suited for an intermediate contributor to open source.

**Required skills**

Fluency with Python, experience working with multi-dimensional arrays libraries such as [xarray](https://docs.xarray.dev/en/stable/index.html), and experience with [pytest](https://docs.pytest.org/en/stable/).

**Nice-to-haves**

Experience with [napari](https://napari.org/stable/) plugins.

**Potential mentors**

**Further reading**

, to get familiar with the structure of the annotations dataset.`ethology`

examples

## Team[#](https://neuroinformatics.dev#team)

The NIU GSoC team for 2026 is composed of the following members. To read more about the different roles involved in GSoC, see [GSoC Participant Roles](https://google.github.io/gsocguides/mentor/#participant-roles).

Our working languages are Python and English ;) - but we also speak other languages! We listed any additional languages spoken by the mentors in the projects list.
