# #112

**Parent:** IOOS — Project Ideas
**Source:** https://github.com/ioos/gsoc/issues/112
**Scraped:** 2026-02-22T23:28:47.602710

---

## [GSoC Project Proposal]: Scalable OCSMesh: Parallelization and Spatial Partitioning

**Labels:** project idea, GSoC26

### Project Description

OCSMesh [V.2.0+](https://github.com/noaa-ocs-modeling/OCSMesh/tree/refactor/internal) is a Python package designed for generating unstructured meshes tailored to ocean modeling. A parallel version of OCSMesh [size function](https://github.com/noaa-ocs-modeling/OCSMesh/tree/refactor/internal/ocsmesh/hfun) was developed in GSoC 2025. This project expands on last years’ success to make OCSMesh a truly HPC-native tool capable of handling global-scale domains. There are multiple problems that can be addressed as a part of this year’s GSoC. The parallelization of size functions in GSoC 2025 needs to be expanded to ensure all mesh size functions and refinement algorithms are fully parallelized. Furthermore for OCSMesh to be relevant on HPC platforms the parallelization must be refactored such that it utilizes distributed architectures, using MPI (i.e. mpi4py). Lastly, the current parallelization logic relies on distinct input files, which creates significant bottlenecks when processing massive, single-source datasets or complex overlapping DEMs. This may be addressed by designing and implementing a spatial partitioning strategy to subdivide the domain prior to the mesh gen process, allowing distinct geographic regions to be processed independently regardless of the input file structure. This approach effectively decouples parallel performance from the input DEM data extent, enabling the efficient creation of high-resolution large domain meshes on supercomputing clusters.

### Expected Outcomes

* Fully implementation of parallel processing for all size function generation and mesh refinement steps
* A fully functional implementation of mpi4py-based parallelization.
* Development of a robust spatial partitioning engine capable of “windowing” massive datasets into manageable chunks for parallel processing.
* Address current memory bottlenecks and the reliance on pre-tiled inputs.
* Evaluate the scalability of the approach and identify optimal number (and size) of partitions (or windows).


### Skills Required

Python, Parallel Computing (multiprocessing and mpi4py), Unit Testing, Geospatial Technologies (GIS and geospatial python libraries)

### Expected Project Size

350 hours

### Project Difficulty

Expert

### Mentor Name(s)

Felicio Cassalho, Soroosh Mani

### Mentor GitHub Handle(s)

@felicio93, @SorooshMani-NOAA

### Mentor Contact Email(s)

felicio.cassalho@noaa.gov, soroosh.mani@noaa.gov

### Contributor Evaluation/GSoC GitHub Issue Links

_No response_

### Additional Project Background/Links

_No response_

### Previous Project Idea Link(s)

_No response_

