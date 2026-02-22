# home page

**Parent:** preCICE — Project Ideas
**Source:** https://precice.org/index.html
**Scraped:** 2026-02-22T23:28:47.561106

---

# Welcome to

## The coupling library for partitioned multi-physics simulations.

preCICE is an **open-source coupling library and ecosystem** for general partitioned multi-physics and multi-scale simulations, including surface and volume coupling.

Partitioned means that **preCICE couples existing programs/solvers** capable of simulating a subpart of the complete physics involved in a simulation. This allows for the high flexibility that is needed to keep a decent time-to-solution for complex coupled problems.


The software offers convenient methods for transient equation coupling, communication, time interpolation, and data mapping.


## Prepared for the next generation of multi-physics simulations

**Minimally invasive integration**

- Elegant library approach
- High-level API in C++, C, Fortran, Python, Matlab

[Learn more](https://precice.org/couple-your-code-overview.html)

**Coupling of arbitrary many programs**

- Arbitrary combinations of strong and weak interactions
- Arbitrary many solvers

[Learn more](https://precice.org/configuration-coupling-multi.html)

**State-of-the-art numerical methods**

- Robust quasi-Newton acceleration
- Radial-basis function data mapping

[Learn more](https://precice.org/fundamentals-literature-guide.html)

**Scalability up to complete supercomputers**

- Pure peer-to-peer approach
- Support of heterogenous hardware (CPU/GPU)
- Efficient also on a laptop

[Learn more](https://precice.org/fundamentals-literature-guide.html#parallel-and-high-performance-computing)

## Ready-to-use with your favourite open-source solver

Several free and proprietary codes are currently coupled with preCICE. Pick one of our official adapters below or check out our [community projects](https://precice.org/community-projects.html).

## What our community is saying

**—Kyle Davis**

University of the Free State, Department of Cardiothoracic Surgery, South Africa

**—Derek Risseeuw**

Aerodynamics, Faculty of Aerospace Engineering, TU Delft, The Netherlands

**—Marta Camps Santasmasas**

Aerodynamics research group, MACE, The University of Manchester, UK

## Academic at heart, 100% free software

preCICE has been developed by three generations of doctoral candidates from the [Chair of Scientific Computing](https://www.cs.cit.tum.de/en/sccs/home/) at the **Technical University of Munich** and from the [Institute for Parallel and Distributed Systems](https://www.ipvs.uni-stuttgart.de/) at the **University of Stuttgart**. We develop everything openly on GitHub, the preCICE library is licensed under LGPLv3, and every other component is developed under compatible free software licenses. [More information.](https://precice.org/fundamentals-license.html)

You can **cite the preCICE library** using the following paper. Please also consider citing the adapters you use, as well as the [preCICE Distribution](https://precice.org/installation-distribution.html) for **reproducibility**. You can find the respective references in our [literature guide](https://precice.org/fundamentals-literature-guide.html).

**preCICE v2: A sustainable and user-friendly coupling library**

*Gerasimos Chourdakis, Kyle Davis, Benjamin Rodenberg, Miriam Schulte, Frédéric Simonis, Benjamin Uekermann et al.*, **2022**. In Open Research Europe, 2:51.

[Publisher's Site](https://doi.org/10.12688/openreseurope.14445.2)

[Download BibTeX](https://precice.org/assets/precice-v2.bib)

[Citations of preCICE v2 paper (187)](https://scholar.google.com/scholar?oi=bibs&hl=en&cites=17974677460269868025,12004404035922881061)

[preCICE v1 (432)](https://scholar.google.com/scholar?cites=5053469347483527186&as_sdt=2005&sciodt=0,5&hl=en)

[Literature guide](https://precice.org/fundamentals-literature-guide.html)

## Join the community!

We develop everything in the open, with continuous feedback by a vivid community. Be part of it:

**Ask for help and help others**in the[preCICE forum](https://precice.discourse.group/)and register to receive news.- Directly
**edit the documentation**. We review and help - nothing can go wrong. - Report issues on
[GitHub](https://github.com/precice/)and help us solve them for everyone. [Contribute](https://precice.org/community-contribute-to-precice.html)code and simulation examples - we help you with guidelines, tools, and reviews.**Meet the community**in one of the[preCICE workshops and conference sessions](https://precice.org/community.html).-
Subscribe to our
**quarterly newsletter**including:- New publications
- New features
- New adapters, bindings, tools, tutorials, and more
- Upcoming events and news from the community


**The quarterly preCICE newsletter**

## You support preCICE – preCICE supports you

As the developers of preCICE, we enjoy supporting our academic and industry users, but due to the growing demand, we are not able to service all support requests any more. We are introducing **preCICE support** as a way to contribute to sustainable open-source software development and to ensure preCICE is developed and maintained in the future. Supporting preCICE comes with several benefits:

**Increased success rate**for your research proposal (include preCICE as a partner, software provider, or sub-contractor)**Priority support**and direct access to the preCICE developers- Private, on-site support and bespoke training

We offer different levels of support for industry and academia.

## Frequently asked questions (FAQ)

**Can preCICE be used for volume coupling?**

Yes. In preCICE v3 there have been many changes and improvements regarding large meshes. The following has ...

[Learn more](https://precice.discourse.group/t/can-precice-be-used-for-volume-coupling/27/9)

**What are best practices to write a new adapter?**

There are [guidelines for adapters](https://precice.org/community-guidelines-adapters.html), as well as for [application cases](https://precice.org/community-guidelines-application-cases.html), as part of the ecosystem standardization ...

[Learn more](https://precice.discourse.group/t/what-are-best-practices-to-write-a-new-adapter/44/3)

**Can preCICE be used for one-way coupling?**

Yes! Several people are doing this already. Even though there may be other ways to do one-way coupling, it may ...

[Learn more](https://precice.discourse.group/t/can-precice-be-used-for-one-way-coupling/28/2)

## Tried and tested by a global community

Through the **community-driven development** approach, preCICE has become one of the leading coupling libraries for multi-physics simulations both in **academia and industry**. The wide variety of application fields ranges from aerodynamics to astronautics, automotive manufacturing, wind energy, biomechanics, biomimetics, marine engineering, nuclear fusion, reactor safety, geophysical systems, and many more.

## How does it look like?

In this tutorial, we couple the CFD code OpenFOAM with a C++ rigid body solver for fluid-structure interaction, using a serial-explicit coupling, as defined in the [preCICE configuration file](https://precice.org/configuration-overview.html).
OpenFOAM loads a ready-to-use [adapter](https://precice.org/adapter-openfoam-overview.html), while the C++ code uses the [preCICE API](https://precice.org/couple-your-code-api.html).
OpenFOAM starts and waits for the other code. After they both start,
they find each other perform a black-box coupled simulation.
