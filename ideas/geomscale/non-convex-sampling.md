# Non-convex sampling in dingo

**Parent:** GeomScale — Project Ideas
**Source:** https://github.com/GeomScale/gsoc26/wiki/non-convex-sampling
**Scraped:** 2026-02-22T23:28:47.592744

---

## Problem

Flux sampling is challenging, and even when uniformity and strict statistical criteria are achieved [1], other factors can lead to biologically non-meaningful samples. For example, loopy flux distributions may continuously consume energy, resulting in thermodynamically infeasible solutions [2].

In this project the student has to exploit whether such aspects can be limited by integrating omics data in a metabolic model. 

If this is the case, then the student will develop further `dingo` approaches for leveraging sampling for biological inference. 
Otherwise, the student will work towards assessing  the scalability and integration potential of non-convex sampling approaches (e.g., [3]) within the `dingo` library. 

Sampling points in non-convex domains is a very challenging problem and we might need to introduce several ad hoc tools
to make it efficient.

## References  

[1] Chalkis, Fisikopoulos, Tsigaridas, Zafeiropoulos - [dingo: a Python package for metabolic flux sampling](https://doi.org/10.1093/bioadv/vbae037)

[2] De Martino - [Scales and multimodal flux distributions in stationary metabolic network models via thermodynamics](https://doi.org/10.1103/PhysRevE.95.062419)

[3] Saa, Zapararte, Drovandi, Nielsen - [LooplessFluxSampler: an efficient toolbox for sampling the loopless flux solution space of metabolic models](https://doi.org/10.1186/s12859-023-05616-2)




**Difficulty:** Hard

## Size 
Large (350 hours)  

## Skills 

* Required: Python, data integration, basics on microbial metabolism 
* Preferred: linear algebra, optimization theory


## Expected impact

This project aims to establish the `dingo` Python library as a robust tool for real-world flux sampling studies, offering users a practical guide to tackling fundamental biological challenges commonly encountered in such analyses.

It will also make clear whether non-convex sampling approaches are required in the case of metabolic models. If yes, novel sampling methods  will be introduced as part of the `dingo` library.


## Mentors

- [Haris Zafeiropoulos](https://hariszaf.github.io) <haris.zafr at gmail.com> is post-doctoral researcher at KU Leuven in the Lab of Microbial Systems Biology, focusing on microbial interactions through data integration and reverse ecology approaches. He has participated in GSoC as both a student and a mentor with the GeomScale group, contributing to the `dingo` library (2021–2025).

- [Vissarion Fisikopoulos](https://vissarion.github.io) <vissarion.fisikopoulos at gmail.com> is an international expert in mathematical software, computational geometry, and optimization, and has previous GSOC mentoring experience with Boost C++ libraries (2016-2020) and the R-project (2017-2019).

- [Apostolos Chalkis](https://tolischal.github.io) <tolis.chal at gmail.com> is a Research Engineer at Quantagonia GmbH. He is an expert in statistical software, computational geometry, and optimization, and has previous GSoC student experience (2018 & 2019) and mentoring experience with GeomScale (from 2020 to 2023).

## Tests

- Easy: Download, compile and run a flux sampling analysis on the core model of *E.coli* ([`e_coli_core`](https://github.com/GeomScale/dingo/tree/develop/ext_data)) requiring: i. for optimal biomass growth, ii. for at least half of the optimal, and iii. setting biomass free.
- Medium: Exploit `dingo`'s functionalities to come up with reaction clusters differentiating in each case.  
- Hard: Try to interpret your findings. Then, describe how you would set a pipeline to address the problem described above.
