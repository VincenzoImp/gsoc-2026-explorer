# GeomScale — Project Ideas

**Source:** https://github.com/GeomScale/gsoc26/wiki/table-of-proposed-coding-projects
**Scraped:** 2026-02-22T23:28:47.592531

---

---
:warning:   **NOTE** 

This year contributors will have to choose between a ~90 hours small-sized project, ~175 hours medium-sized project or ~350 hours large project.
For more information please read the [official gsoc website](https://summerofcode.withgoogle.com/) as well as [GeomScale's introductory wiki for GSoC 2026](/ideas/geomscale/geomscale-gsoc26-wiki).

---

GeomScale hosts a few projects in different github repositories. The most mature one is [volesti](https://github.com/GeomScale/volesti) written in C++. Then there are two repositories that act as interfaces of volesti (i) [Rvolesti](https://github.com/GeomScale/Rvolesti) in *R* that also contains utilities for financial applications and (ii) and [dingo](https://github.com/GeomScale/dingo) written in *Python* (uses C++ functions of volesti via Cython) and contains utilities for biological applications. Finally, there is [PorQua](https://github.com/GeomScale/PorQua) a Python package for index replication in finance.

Proposed projects are related to those repositories. There are **two** types of coding projects: research and development (marked as *R&D* in the table below) and pure development (marked as *Dev* in the table below). *R&D* projects needs a deep understanding of the mathematical background in addition to the implementation details that are needed by the *Dev* projects. Typically the former is more demanding than the later but this also depends on the background of the contributor.   

---

Mentors, please edit this wiki page, and add your ideas to the table below.

Contributors, please look for a project that interests you in the table below. Before emailing project mentors, please do at least one project **test** and post a link to your solution on the proposal's wiki page.

 Proposal                        | Type                  | Languages | Size | Hours |
---------------------------------|--------------------------|-----------|------|------|
[Non-convex sampling in dingo](/ideas/geomscale/non-convex-sampling) | R&D | C++ /Python| Large | 350 | 
[Exclude Lpsolve from R and C++ interfaces of volesti](/ideas/geomscale/exclude-lpsolve) | Dev |  C++/R | Medium | 175 |  
[Counting linear extensions with volume computation and applications in AI](/ideas/geomscale/counting-linear-extensions-with-volume-computation-and-applications-in-ai) | R&D | C++ | Large | 350 |
[Expose sampling and volume on spectrahedra to R interface of volesti](/ideas/geomscale/spectrahedra-r-interface) | Dev | R/Rcpp | Medium | 175 |
[Expose autodiff to R interface of volesti](/ideas/geomscale/autodiff-r-interface) | Dev | R/Rcpp | Medium | 175 |
[Geometric Inference of Convex Bodies from Random Sampling](/ideas/geomscale/geometric-inference-of-convex-bodies-from-random-sampling) | R&D | C++/Python | Large | 350|
[Supporting Sparse Matrix Representation for H‐Polytopes in Rvolesti](/ideas/geomscale/supporting-sparse-matrix-representation-for-h-e2-80-90polytopes-in-rvolesti) | Dev | R/Rcpp | Small | 90 |
[Enhancing Rvolesti: Integration of Advanced Rounding Routines](/ideas/geomscale/enhancing-rvolesti-e2-80-93-integration-of-advanced-rounding-routines) | Dev | R/Rcpp | Small | 90 |
[Benchmark Polytope Import Suite for volesti](/ideas/geomscale/benchmark-polytope-import-suite-for-volesti) | Dev | C++ | Medium | 175 |

All contributor applications will be discussed by the **GeomScale** mentor community, and proposals will be ranked considering factors such as quality, contributor's ability to successfully finish the project, and impact for the **GeomScale** project.  A finite number of slots will be granted to **GeomScale** by Google, thus, only the best proposals will get chosen. This implies that it is possible that some ideas will not become GSoC projects even if they are supported by a good contributor application. 

Contributors, if you are interested in a coding project related to **GeomScale** that is not listed above, please
try to find mentors by posting a description of your project idea on the [gitter](https://gitter.im/GeomScale/community?utm_source=share-link&utm_medium=link&utm_campaign=share-link). If you find mentors, feel free to add your project idea to this wiki and write an application.  

## Information Candidates Should Supply  

The application process has several steps. Before contacting anybody verifies that you are eligible.
The next step is to contact the mentor of the project you are interested in. You have to convince them that you are the right person to get the job done. The next step is to work out more details and to
contact the mentors or the GeomScale org by providing the following information by email or by
[gitter](https://gitter.im/GeomScale/community?utm_source=share-link&utm_medium=link&utm_campaign=share-link).  

* Project:
  * Select a project in the list and provide your personal and detailed description. If you wish to work on another idea of your own, we are pretty open as long as this serves the goal of consolidating GeomScale as a whole.
  * Provide a proposal of a technical solution with your envisioned methodology. The more detailed the better.
  * Explain how the solution will be available to the user, in which form. Do not forget the documentation, unitary tests, and cross-platform aspects.
  * Provide a realistic schedule with objectives (one every two weeks for example) and deadlines. Focus on mid-term objectives as well as on the final evaluation.


* Personal data:
  * First name, last name, affiliation, and geographical location.
  * A brief list of the main studies and programming courses attended, with ranking.
  * List of the most important software projects contributed and success.
  * Which are your best skills in terms of programming and scientific computing?
  * In general what is your taste in terms of programming? language, methodology, teamwork, etc.
  * Is there anything that prevents you from working full time on the project during the program period?
  * How do you see your involvement after the program ends? Do you see yourself pushing the project further, or do you see yourself contributing to other GeomScale projects?
  * Are you more interested in the theory/scientific aspect of GeomScale, or do you feel more like a hacker?
