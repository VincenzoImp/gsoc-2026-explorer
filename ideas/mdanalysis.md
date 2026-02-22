# MDAnalysis — Project Ideas

**Source:** https://github.com/MDAnalysis/mdanalysis/wiki/GSoC-2026-Project-Ideas
**Scraped:** 2026-02-22T23:28:47.550050

---

<img src="https://developers.google.com/open-source/gsoc/resources/downloads/GSoC-Vertical.png" title="Google Summer of Code 2026" alt="Google Summer of Code 2026" align="right" width="33%" />

<!--

----

**IMPORTANT:** THIS PAGE IS ONLY A DRAFT. Given that there is an application process for organizations — such as MDAnalysis — to participate in the [GSoC](https://summerofcode.withgoogle.com/) program, there is no guarantee that MDAnalysis will be selected by Google as a participating GSoC organization. Once we know more, we will share updates on our [public communication channels](https://www.mdanalysis.org/pages/community/), in particular in the [Announcement](/ideas/mdanalysis/mdanalysis-mdanalysis-discussions-categories-announcements) discussion.

----

-->

Hello, and welcome to MDAnalysis! 

Please **read [our blog post](https://www.mdanalysis.org/2026/02/19/gsoc2026)** for important official information.

Please see [[our Google Summer of Code wiki page|Google Summer of Code]] for general information, including advice on application writing, and [[our GSoC FAQ|GSoC-FAQ]] for commonly asked questions.

If you just found out about the MDAnalysis Python package from the GSoC website, you can watch the [MDAnalysis 2021 Trailer](https://www.youtube.com/watch?v=uMAfvwFkD3o) to get an overview of the scope of the MDAnalysis package.

### Prerequisites

MDAnalysis is a Python library for the analysis of computer simulations of many-body systems at the molecular scale, spanning use cases from interactions of drugs with proteins to novel materials. For Google Summer of Code, [we are also collaborating](#collaborations) with other organizations and software projects that use MDAnalysis. Our GSoC projects generally require a basic knowledge and hands-on experience in specific areas, so *for our suggested projects, please check carefully the project descriptions to see the associated desirable skills*. Broadly speaking, we found that applicants with experience in molecular dynamics (MD) simulations and the associated analyses — or equivalent experience in simulations and modeling of molecular systems (physics, biophysics, chemistry, or materials) — are very successful.

### To Prospective Applicants
If you are interested in taking part, please get in touch on the [GSoC with MDAnalysis Discussion Forum](/ideas/mdanalysis/mdanalysis-mdanalysis-discussions-categories-gsoc-discussions). Given the GSoC program structure (small, medium, and large projects), letting us know of your intentions to apply and getting acquainted with the project early will be very helpful.

### To Prospective Mentors
MDAnalysis welcomes new mentors; please get in touch on the [developer forum](/ideas/mdanalysis/mdanalysis-mdanalysis-discussions-categories-development) if you are interested in taking part. We typically expect mentors to be familiar with our development process, as evidenced by contributions to the code base and interactions on the developer forum.

# Overview

See below for a list of projects ideas for [[Google Summer of Code 2026|Google-Summer-Of-Code]].

The currently proposed projects are:

1. Dashboard for tracking MD simulation progress with the new streaming interface
2. Better interfacing of Blender and MDAnalysis
3. Benchmarking and performance optimization
4. Lazy trajectory loading and indexing
5. Dashboard for tracking WESTPA simulation progress
6. Interface for post-simulation analysis ("crawling") of WESTPA simulations

**Or work on your own idea!** Get in contact with us to propose an idea and we will work with you to flesh it out into a full project. Contact us via the [GSoC with MDAnalysis Discussion Forum](/ideas/mdanalysis/mdanalysis-mdanalysis-discussions-categories-gsoc-discussions) (or if your project is a specific feature you'd want to add, raise an issue in the [Issue Tracker](/ideas/mdanalysis/mdanalysis-mdanalysis-issues)).

Look at the [list of all available mentors for MDAnalysis](/ideas/mdanalysis/google-summer-of-code) for potential mentors for your project. Please send all communications to the [discussion forum](/ideas/mdanalysis/mdanalysis-mdanalysis-discussions-categories-gsoc-discussions) (and don't contact mentors privately). You can certainly ask for the opinion of a specific mentor if you know that their expertise is particularly suitable for your project.

## Collaborations

For GSOC, MDAnalysis collaborates with other projects that have direct links with MDAnalysis and where it is especially useful to draw on the combined mentoring expertise.

### Molecular Nodes

Built as an add-on for the popular and industry-leading 3D software [Blender](https://www.blender.org/), [Molecular Nodes](https://bradyajohnston.github.io/MolecularNodes/) (MN) enables import and visualization of complex molecular datasets inside of Blender. Many formats are supported such as static structures, electron density maps, EM (electromagnetic) tomography data and importantly, molecular dynamics simulation trajectories, powered by MDAnalysis. Blender is primarily intended for use via a GUI by artists, but scripting via the python API is also possible, with many potential avenues for automated animation and rendering.

A great overview of the project is the talk given at the [Blender Conference in 2022](https://www.youtube.com/watch?v=adhTmwYwOiA). The [MN documentation](https://bradyajohnston.github.io/MolecularNodes/) includes a lot of information about how to get started, including written and video tutorials, with one [specific to MD trajectory import](https://bradyajohnston.github.io/MolecularNodes/tutorials/03_molecular_dynamics.html). Workshop materials are also publicly available for an online [Introduction to MDAnalysis and Molecular Nodes workshop](https://github.com/MDAnalysis/MDAnalysisWorkshop-Intro0.5Day/tree/feb24-ws) held in February 2024, which includes an interactive tutorial for visualizing imported MDAnalysis data in Molecular Nodes.

It's important to first familiarize yourself with using Blender and Molecular Nodes via a GUI and some of the quirks that go along with it, before trying to write code for it.

### WESTPA

[WESTPA](http://westpa.github.io/westpa) (The Weighted Ensemble Simulation Toolkit with Parallelization and Analysis) is a high-performance Python framework for applying the weighted ensemble (WE) path sampling strategy, which enables simulations of processes that are orders of magnitude longer than the simulations themselves. A WE simulation involves an iterative process: many MD simulations are executed in parallel and periodically evaluated to be replicated or terminated based on a set WE resampling criteria. To rigorously apply WE resampling, the MD simulations are analyzed during run time with tools such as MDAnalysis to determine the state of the simulated system.

Read the [WE Overview](https://westpa.github.io/westpa/overview.html); [install the WESTPA package](https://github.com/westpa/westpa/wiki/Installing-WESTPA); and work through tutorials 7.1 and 7.5 of our [tutorials suite](https://github.com/westpa/tutorials) to start learning more about WESTPA.

------

# Project summary

The table summarizes the project ideas; long descriptions come after the table (or click on the links under each project name). The difficulty is a somewhat subjective ranking, where *easy* means that we know pretty much what needs to be done, *medium* requires some additional research into best solutions as part of the project, and *hard* is high risk/high reward where we think a solution exists but we will have to work with the student to find it and implement it. The project size is either 90 h (small), 175 h (medium) or 350 h (large) projects.

Each project has one *primary mentor* assigned and potentially multiple additional mentors.
Each primary mentor will only *mentor a single GSoC project*, even if listed as a potential mentor for multiple projects in the table. Mentor availability will be taken into account during the project selection process.

| project | name                                                                                                                                                      | difficulty | project size | description                                                                                    | skills                      | mentors                                |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------|------------|------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------|
| 1       | [Dashboard for tracking MD simulation progress with the new streaming interface](#project-1-dashboard-for-tracking-md-simulation-progress-with-the-new-streaming-interface)                                         | easy/medium     | 175/350 hours   | Create a web-based dashboard for real-time monitoring and analysis of MD simulations                                                                   | Python (frontend UI, multiprocessing), Networking (TCP/IP)                  | [@HeydenLab](https://github.com/HeydenLab) [@amrutesht](https://github.com/amrutesht) [@orbeckst](https://github.com/orbeckst) |
| 2       | [Better interfacing of Blender and MDAnalysis](#project-2-better-interfacing-of-blender-and-mdanalysis)                                         | medium     | 350 hours   | Improve how Blender and Molecular Nodes interface with MDAnalysis to import and animate MD trajectories                                                                   | Python, MDAnalysis, Blender (and programming via its Python API)                  |  [@bradyajohnston](https://github.com/bradyajohnston) [@nilay-v3rma](https://github.com/nilay-v3rma) |
| 3       | [Benchmarking and performance optimization](#project-3-benchmarking-and-performance-optimization)                                         | easy/medium     | 90/175/350 hours   | Write benchmarks for automated performance analysis and address performance bottlenecks                                                                   | Python/ASV, Cython                  | [@orbeckst](https://github.com/orbeckst) [@yuxuanzhuang](https://github.com/yuxuanzhuang) [@talagayev](https://github.com/talagayev) |
| 4       | [Lazy trajectory loading and indexing](#project-4-lazy-trajectory-loading-and-indexing)                                         | medium     | 175/350 hours   | Improve performance of trajectory reading by implementing lazy indexing                                                                   | Python, trajectory I/O, performance optimization                  | [@yuxuanzhuang](https://github.com/yuxuanzhuang) [@orbeckst](https://github.com/orbeckst) [@talagayev](https://github.com/talagayev) |
| 5       | [Dashboard for tracking WESTPA simulation progress](#project-5-dashboard-for-tracking-westpa-simulation-progress)                                         | easy     | 90 hours   | Create a graphical user interface to report MD trajectory progress                                                                   | Python (frontend UI, multiprocessing), Networking (TCP/IP)                  | [@jeremyleung521](https://github.com/jeremyleung521) [@ltchong](https://github.com/ltchong) [@nilay-v3rma](https://github.com/nilay-v3rma) |
| 6       | [Interface for post-simulation analysis ("crawling") of WESTPA simulations](#project-6-interface-for-post-simulation-analysis-crawling-of-westpa-simulations)                                         | easy     | 90 hours   | Create an interface for reading, analyzing, and writing post-simulation data from WESTPA HDF5 Framework             | Python (frontend UI, multiprocessing), HDF5 Format (h5py, hdf5)         | [@jeremyleung521](https://github.com/jeremyleung521) [@ltchong](https://github.com/ltchong) |


## Project 1: Dashboard for tracking MD simulation progress with the new streaming interface

### Summary

This project will develop a browser-based, real-time dashboard for molecular dynamics simulations using the new IMDv3 streaming protocol, enabling live monitoring, analysis, and visualization of running simulations. The dashboard will leverage [imdclient](https://imdclient.readthedocs.io) and MDAnalysis to receive a data stream from a running simulation.

### Detailed Description

Modern molecular dynamics (MD) simulations can run for days or weeks, yet most analysis workflows remain strictly post-hoc, requiring trajectory files to be written to disk and analyzed only after completion. Recently, we introduced IMDv3, a TCP/IP-based streaming protocol implemented in major MD engines such as LAMMPS, NAMD3, and GROMACS, together with a Python package, [imdclient](https://github.com/Becksteinlab/imdclient), that simplifies consuming these live data streams. In parallel, the MDAnalysis project now includes a reader ([IMDReader](https://docs.mdanalysis.org/stable/documentation_pages/coordinates/IMD.html))that can access IMDv3 streams as if they were conventional trajectory files.

The goal of this Google Summer of Code project is to build a browser-based dashboard that connects to a running MD simulation via imdclient/MDAnalysis and provides real-time feedback to users. At its most basic level, the dashboard will display simulation progress (e.g., current timestep or frame number) and connection status. Beyond this, the project will focus on interactive, live analysis: users should be able to select atoms or groups using familiar MDAnalysis selection syntax and compute properties on the fly as new frames arrive.

The project will explore both simple, frame-local analyses (such as distances, angles, or radius of gyration) and more advanced, time-dependent analyses that require buffering and processing historical data (e.g., autocorrelations or lag-time dependent observables). Results will be visualized live in the browser using plots and indicators. As an advanced extension, the project may integrate real-time 3D visualization via Blender and [Molecular Nodes](#molecular-nodes), enabling users to view the evolving molecular structure while analyses run in parallel.

Finally, the dashboard may include basic event detection and warning mechanisms, such as flagging unusual structural changes or simulation instabilities. The end result will be a flexible foundation for interactive, remote, and collaborative monitoring of MD simulations, tightly integrated with the Python MDAnalysis ecosystem.

### Expected Outcomes

1. A web-based dashboard that can connect to running MD simulations via IMDv3 and imdclient
2. Live display of simulation status and progress information
3. An interactive GUI for defining and running real-time analyses using MDAnalysis
4. Support for simple per-frame observables and buffered, time-dependent analyses
5. Live visualization of analysis results (plots, indicators, status messages)
6. (Optional/advanced) Live 3D molecular visualization using Blender and Molecular Nodes
7. (Optional) Basic event detection and warning system for problematic simulation behavior
8. Well-documented, open-source code suitable for long-term integration into the MDAnalysis ecosystem

### Relevant Skills

- Python (frontend UI, multiprocessing)
- Networking (TCP/IP)
- Web development (for browser-based dashboard)

### Related issues/PRs/etc.:

- https://imdclient.readthedocs.io
- https://www.mdanalysis.org/2024/11/03/ASU_streaming_workshop/

### Possible Mentors

- [@HeydenLab](https://github.com/HeydenLab)
- [@amrutesht](https://github.com/amrutesht)
- [@orbeckst](https://github.com/orbeckst)


### Expected Size of Project

Medium/Large (175/350 hours, depending on targeted features)

### Difficulty Rating

Easy/Medium

## Project 2: Better interfacing of Blender and MDAnalysis

### Summary

Improvements to how Blender and [Molecular Nodes](#molecular-nodes) interface with MDAnalysis which powers the import and animation of MD trajectories inside of Blender. Simple import is currently available when using the GUI in Blender, but there is still a lot of potential for improvements in scriptability, automated rendering, and using Blender as an analysis tool for MD trajectories.

### Detailed Description

[Blender](https://www.blender.org/) is industry-leading 3D modeling and animation software. Through the add-on [Molecular Nodes](https://bradyajohnston.github.io/MolecularNodes/), MDAnalysis universes are able to be imported into the 3D scene, enabling advanced rendering of molecular dynamics trajectories that is not possible inside of any other molecule viewer. The ability to script and automate this rendering is possible but limited with lots of room for improvement for visualizing many common MD datasets. Blender also provides a great platform for implementing a potential GUI, to enable interactive analysis of MD trajectories with stunning visuals, all powered by MDAnalysis under the hood.

This project focuses on:
- Better improving the Molecular Nodes ↔ MDAnalysis integration
- Improvements on Molecular Nodes notebook rendering API
- Visualizing particular analysis results inside of Blender / using Molecular Nodes rather than just structural information

### Expected Outcomes

1. Prototype improved API for scripting and working with Molecular Nodes from [Jupyter](https://jupyter.org/) Notebooks or other similar environments
2. Prototyping common analysis and visualization tasks that could be performed from within Blender via the GUI

### Relevant Skills

- Proficiency with Python
- Working knowledge of MDAnalysis
- Familiarity with Blender and programming via its Python API

### Related issues/PRs/etc.:

- https://github.com/BradyAJohnston/MolecularNodes/pull/719

### Possible Mentors

- [@bradyajohnston](https://github.com/bradyajohnston)
- [@nilay-v3rma](https://github.com/nilay-v3rma)

### Expected Size of Project

Large (350 hours)

### Difficulty Rating

Medium

## Project 3: Benchmarking and performance optimization

### Summary

The goal of this project is to increase the performance assessment coverage (using the existing ASV framework), identify code that should be improved, and optimize code.

### Detailed Description

The [MDAnalysis Roadmap](https://www.mdanalysis.org/2023/10/25/towards_3.0/) emphasizes performance improvement. The performance of the MDAnalysis library is assessed by automated nightly benchmarks with [ASV](https://asv.readthedocs.io/en/latest/) (see https://github.com/MDAnalysis/benchmarks/wiki) but coverage of the code base is low. The goal of this project is to substantially increase the performance assessment coverage, identify code that should be improved, and possibly implement performance optimizations. 

### Expected Outcomes

1. Write ASV benchmark cases for all major functionality in the core library
2. Write ASV benchmark cases for often-used analysis tools
3. Analyze performance history and generate a priority list of code that should be improved
4. Document writing benchmarks with a short tutorial
5. *Optional*: Optimize performance for at least one discovered performance bottleneck

### Relevant Skills

- Python/ASV
- Cython

### Related issues/PRs/etc.:

- https://github.com/MDAnalysis/mdanalysis/issues/1023
- https://github.com/MDAnalysis/mdanalysis/issues/1721
- https://github.com/MDAnalysis/mdanalysis/issues/4577

### Possible Mentors

- [@orbeckst](https://github.com/orbeckst)
- [@yuxuanzhuang](https://github.com/yuxuanzhuang)
- [@talagayev](https://github.com/talagayev)

### Expected Size of Project

Small/Medium/Large (90/175/350 hours)

(This project can be tailored in scope to the desired length. Discuss the length and scope with us while you are writing your application.)

### Difficulty Rating

Easy/Medium

## Project 4: Lazy trajectory loading and indexing

### Summary

This project aims to improve MDAnalysis's trajectory reading performance by implementing lazy indexing for trajectory formats that currently build a complete frame index on first file open, which can take hours for large files.

### Detailed Description

A general assumption in MDAnalysis has been for a long time that a trajectory reader can access arbitrary frames in a trajectory file, corresponding to the usage in MDAnalysis of `ts = u.trajectory[frame]`. However, many trajectory formats do not support random access natively. To get around this problem, some MDAnalysis trajectory readers (in particular the ones for XTC and TRR formats) *always* build a hidden frame index on first opening the file by rapidly scanning the whole file. (MDAnalysis calls this frame index *offsets*.) For large files, this "rapid scan" can still take hours during which the user has no idea what's happening.

This project proposes implementing "lazy trajectory loading" whereby we eschew index building if we are only iterating forward and instead resort to frame-by-frame loading (or possibly use the header-seeking trick from the index building for larger step sizes). In a way, this treats these files more like *streams* than random-access trajectories.

While reading we could then start building the index and possibly improve it iteratively while additional frames are being read. The index would be built right away if fancy indexing is used.

The behavior could potentially be made user-configurable at the Universe level with a kwarg like `index_trajectory="always" | "never" | "lazy"`.

### Expected Outcomes

1. Implementation of lazy indexing mode for XTC/TRR readers
2. Progressive index building during forward iteration
3. User-configurable indexing behavior via Universe kwarg
4. Performance benchmarks comparing lazy vs eager indexing
5. Documentation for users and developers

### Relevant Skills

- Python
- Understanding of trajectory I/O and file formats
- Performance optimization

### Related issues/PRs/etc.:

- https://github.com/MDAnalysis/mdanalysis/issues/3793
- [Notes on offsets for the XDRBaseReader](https://docs.mdanalysis.org/stable/documentation_pages/coordinates/XDR.html#MDAnalysis.coordinates.XDR.XDRBaseReader)

### Possible Mentors

- [@yuxuanzhuang](https://github.com/yuxuanzhuang)
- [@orbeckst](https://github.com/orbeckst)
- [@talagayev](https://github.com/talagayev)

### Expected Size of Project

Medium/Large (175/350 hours)

### Difficulty Rating

Medium

## Project 5: Dashboard for tracking WESTPA simulation progress

### Summary

[WESTPA](#westpa) simulations involve running multiple MD trajectories in parallel, which makes it hard to track progress. This project aims to create a graphical user interface that exploits MDAnalysis’s streaming ability and WESTPA’s work managers to monitor the progress of a WESTPA simulation.

### Detailed Description

While [WESTPA](https://westpa.github.io/westpa) simulations [report status](https://github.com/westpa/westpa/blob/32bf2ca0d710f55c38e60d7f35b63d653ab01c92/src/westpa/core/sim_manager.py#L179) at regular intervals, these iterations could last minutes to hours, leaving users unsure of the intermediate progress or time estimate. The task here will involve creating a graphical user interface reporting trajectory progress and completion time estimates through MDAnalysis’s streaming abilities and extracting relevant information from WESTPA’s [work managers](https://github.com/westpa/westpa/wiki/Work-Managers-and-Running-with-MPI) ([ZMQ](https://github.com/westpa/westpa/blob/westpa2/src/westpa/work_managers/zeromq/core.py), python [multiprocessing](https://github.com/westpa/westpa/tree/westpa2/src/westpa/work_managers)) and [data managers](https://github.com/westpa/westpa/blob/westpa2/src/westpa/core/data_manager.py).

### Expected Outcomes

1. New CLI tool for WESTPA tracking simulation progress
2. MDAnalysis module for aggregating/tracking multiple simulations

### Relevant Skills

- Python (frontend UI, multiprocessing)
- Networking (TCP/IP)

### Related issues/PRs/etc.:

Not applicable

### Possible Mentors

- [@jeremyleung521](https://github.com/jeremyleung521)
- [@ltchong](https://github.com/ltchong)
- [@nilay-v3rma](https://github.com/nilay-v3rma)

### Expected Size of Project

Small (90 hours)

### Difficulty Rating

Easy

## Project 6: Interface for post-simulation analysis ("crawling") of WESTPA simulations

### Summary

[WESTPA](#westpa) simulations involve running multiple MD trajectories in parallel. This makes post-simulation extraction of features and observables (that were not saved during the simulation) somewhat cumbersome. This project aims to create a simpler method for analyzing and extracting data from WESTPA simulation saved using the HDF5 Trajectory Storage Framework.

### Detailed Description

While users who wish to extract more data from their trajectories/WE Simulation can use [`w_crawl`](https://github.com/westpa/westpa/wiki/man:w_crawl), it requires writing and testing custom Python code to get it right. The task here is to simplify the process for users who have already saved their trajectory data with WESTPA's HDF5 Trajectory Storage Framework ("HDF5 Framework"), just by loading their [`west.h5` file](https://github.com/westpa/westpa/wiki/HDF5-File-Organization-of-Simulation-Data#user-content-Overall_structure_of_westh5). The resulting code for this project would read in the "west.h5" as a MDAnalysis universe object, allowing users to run analysis promptly and save it back into the west.h5 file as auxiliary data. Code that translates the topology in the HDF5 Framework to that of MDAnalysis has already been written and included in the source code of v2022.13.


### Expected Outcomes

1. New CLI/Python tool for analyzing trajectory data saved with WESTPA HDF5 Trajectory Storage Framework
2. New MDAnalysis/MDAKit parser for WESTPA west.h5 files (turns west.h5 + related iteration files into a MDAnalysis Universe object)

### Relevant Skills

- Python (frontend UI, multiprocessing)
- HDF5 (h5py, hdf5)

### Related issues/PRs/etc.:

- [WESTPA 2.0 Paper](https://pubs.acs.org/doi/full/10.1021/acs.jctc.1c01154)
- Tutorial 7.5 from [WESTPA 2.0 Tutorials](https://livecomsjournal.org/index.php/livecoms/article/view/v5i1e1655)
- HDF5 Framework update https://github.com/westpa/westpa/pull/484

### Possible Mentors

- [@jeremyleung521](https://github.com/jeremyleung521)
- [@ltchong](https://github.com/ltchong)

### Expected Size of Project

Small (90 hours)

### Difficulty Rating

Easy
