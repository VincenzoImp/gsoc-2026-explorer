# MLLAM — Project Ideas

**Source:** https://github.com/mllam/neural-lam/wiki/GSoC-ideas
**Scraped:** 2026-02-22T23:28:47.631647

---

# neural-lam

<img src="
https://raw.githubusercontent.com/joeloskarsson/neural-lam-dev/refs/heads/extra-figures/figures/overview.png" width="800">

## About neural-lam and the MLLAM community

MLLAM is a collaborative community dedicated to advancing machine learning applications in weather forecasting, specifically for Limited Area Modeling (LAM). The organization hosts several open-source key repositories, including neural-lam, which focuses on neural weather prediction using graph-based models. Members are from various research institutions and national weather services committed to improve weather forecasting at regional, high-resolution scale.

### Policy on the use of AI tooling
We generally allow the use of AI tools to write, edit and review source code, but each contributor is fully responsible for their code. This means that everyone must understand all the code they contribute, and be able to argue why the design choices made are suitable (no "vibe-coding").

# Getting started
If you plan to become a GSoC contributor, we encourage you to
* contact us early to show your interest in a project idea (join e.g. the `GSoC` slack channel at https://kutt.it/mllam)
* look through the current list of issues and identify one that you want to solve to get familiar with the project. You likely want to choose one that is marked as good-first-issue
* comment on the issue and request to be assigned to the issue so that we can make sure only one person is working on each issue. If we do not see any progress within 7 days (e.g. by opening a PR and actively engage in the conversation) we might re-assign the issue again.
* open a pull request and discuss your contributions with the maintainers


# Writing the Proposal
**Deadline to upload proposal at https://summerofcode.withgoogle.com/ is [March 31 18:00 UTC](https://developers.google.com/open-source/gsoc/timeline#march_31_-_1800_utc)!**

- Select a project idea (see below) and write a detailed proposal (in advance!). You can use [this template](https://github.com/python-gsoc/python-gsoc.github.io/blob/master/ApplicationTemplate.md) as inspiration, as well as the [GSoC guide](https://google.github.io/gsocguides/student/writing-a-proposal).
- Plan your prepwork for the community bonding period (eg. a Proof-Of-Concept)
- Define milestones for each evaluation phase (i.e. Prototype, Pilot / Final Demo)
- Plan you weekly work & deliverables (tasking out: high-level goals for each milestone)
- Describe the acceptance criteria ("Minimum Viable Product" of each phase)
- Share an early draft and discuss your approach in the group with mentors. We are here to help! Do not forget to submit your application to the [Google system](https://summerofcode.withgoogle.com/) when ready, some days before the deadline (the server can be overloaded at last minute).

# Project ideas

Here is a list of projects we think are interesting and can be managed within the time-frame of the Google Summer of Code:

## 1. Flexible graph construction

Neural-LAM supports already a variety of graphs like multi-scale and hierarchical graphs in rectangular and triangular arrangements. The training data might however be on a different grid, which can lead to non-optimal alignments of the neural network architectural grid and the data grid. The challenge is to explore and implement a methodology that can create well-balanced neural network grids based on different data structures, from irregularly structured atmospheric model output to sparse ship-observations.

- **Skills**: Shell, Python, familiarity with [PyTorch](https://pytorch.org/) is highly beneficial.
- **Difficulty**: Medium
- **Project length**: 350 hour
- **Potential mentors**: Hauke Schulz ([@observingClouds](https://github.com/observingClouds)), Leif Denby ([@leifdenby](https://github.com/leifdenby)), Joel Oskarson ([@joeloskarsson](https://github.com/joeloskarsson))

Related issues are: [#164](/ideas/mllam/mllam-neural-lam-issues-164), [weather-model-graphs](https://github.com/mllam/weather-model-graphs/issues)

## 2. Automatic generation of documentation from source code files

One of the challenges for users of the neural-lam codebase is that much of the documentation of different functions and constructs can only be found within the code. The project would strongly benefit from having a separate documentation system set up, where both much of the information currently in the readme could be found, but also a structured presentation of the API. Since much of the codebase contains well-written Python docstrings, it should be possible to use automatic tools to generate documentation pages from these. Such a documentation system should also be integrated in the CI/CD workflow, to be updated when new changes are merged.

- **Skills**: Shell, Python
- **Difficulty**: Medium
- **Project length**: 175 hour
- **Potential mentors**: Hauke Schulz ([@observingClouds](https://github.com/observingClouds)), Leif Denby ([@leifdenby](https://github.com/leifdenby)), Joel Oskarson ([@joeloskarsson](https://github.com/joeloskarsson))

Related issues are: https://github.com/mllam/neural-lam/issues/61 https://github.com/mllam/neural-lam/issues/69

## 3. Generalizing to probabilistic forecasting models

The scientific field of neural weather prediction is increasingly moving towards probabilistic model formulations. In these approaches, generative machine learning is used to produce ensemble forecasts representing different possible outcomes. Here the neural-lam codebase has earlier been leveraged in research projects to build such probabilistic models (see e.g. https://arxiv.org/abs/2406.04759 and https://arxiv.org/abs/2502.07532). However, these new ideas and models rarely find their way back to the main repository due to the big discrepancy with how the codebase is currently structured. To allow for such probabilistic models, parts of the neural-lam model code would need to be generalized for models that can sample different possible forecasts, rather than just giving a single prediction. This includes changing how forecasts are being produced, visualized and evaluated.

- **Skills**: Python, PyTorch
- **Difficulty**: Large
- **Project length**: 350 hour
- **Potential mentors**: Joel Oskarson ([@joeloskarsson](https://github.com/joeloskarsson)), Hauke Schulz ([@observingClouds](https://github.com/observingClouds)), Leif Denby ([@leifdenby](https://github.com/leifdenby))

Related issues are: https://github.com/mllam/neural-lam/issues/49 https://github.com/mllam/neural-lam/issues/62

## 4. Global weather forecasting

Neural-lam was mainly designed with regional, limited-area, forecasting in mind, integrating boundary conditions around the region. However, global weather forecasting is really just a special case of this, where the region is the whole earth and there are no boundary conditions. Still, some changes are needed in the codebase in order to make this work frictionless. The major challenge with enabling global forecasting is the need to construct a global graph for the Graph Neural Network models to work on. There are multiple options for this, including writing code for such graph-generation ourselves or building in a connection to suitable third-party libraries.

- **Skills**: Python, PyTorch, PyTorch Geometric and [xarray](/ideas/mllam/xarray-pydata-org) are highly beneficial
- **Difficulty**: Medium
- **Project length**: 175 hour
- **Potential mentors**: Joel Oskarson ([@joeloskarsson](https://github.com/joeloskarsson)), Hauke Schulz ([@observingClouds](https://github.com/observingClouds)), Leif Denby ([@leifdenby](https://github.com/leifdenby))

Related issues are: https://github.com/mllam/neural-lam/issues/63
