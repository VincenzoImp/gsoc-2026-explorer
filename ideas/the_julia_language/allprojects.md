# single page with all our projects together

**Parent:** The Julia Language — Project Ideas
**Source:** https://julialang.org/jsoc/allprojects/
**Scraped:** 2026-03-10T16:58:40.261502

---

This page is designed to improve discoverability of projects. You can search this page (Ctrl+F / Cmd+F) for specific keywords to find all relevant projects across all domains.

Climate models are complex codes that simulate Earth's climate system (atmosphere, ocean, land, ice). These models demand immense computing power and present significant software engineering challenges, including managing massive datasets, ensuring numerical stability, optimizing performance, and coupling diverse components. The complexity and legacy nature of existing models hinder their ability to fully utilize modern computing infrastructure (GPUs, machine learning, etc.). The Climate Modeling Alliance is developing CliMA, a new climate model built in Julia and designed from the outset to leverage GPU acceleration and modern software engineering practices to overcome the limitations of traditional climate models.

`ClimaExplorer`

: An Interactive Visualizer of Climate Model OutputsVisualizing simulation output is crucial for both scientific understanding and outreach. This project involves developing `ClimaExplorer`

, an interactive visualizer for the output of the CliMA Earth system model. `ClimaExplorer`

will leverage the [Makie](https://github.com/MakieOrg/Makie.jl) ecosystem and web technologies, providing a user-friendly interface for exploring complex climate data. This will enable researchers to more easily analyze and interpret simulation results, accelerating scientific discovery. Furthermore, the web-based component will facilitate broader dissemination of results to a wider audience.

**Desired Skills:** Familiarity with front-end web development (HTML, JavaScript, and CSS), Julia, and [Makie](https://github.com/MakieOrg/Makie.jl).

**Difficulty:** Medium

**Duration** 175 hours

**Expected Results:** `ClimaExplorer`

, a new module for interactive visualization of simulation output (with tests and documentation).

**Mentor:** [Gabriele Bozzola](https://github.com/sbozzolo)

**Contact:** Feel free to ask questions via [email](https://julialang.org/clima-software@caltech.edu) or [Julia Slack](https://join.slack.com/t/julialang/shared_invite/zt-2a5wdtotu-H52pQQTMDOa4NwsTSgQ_lQ) (DM to Gabriele Bozzola).

*Interested in other aspects of climate modeling in Julia but not this particular project? Get in touch—we have many more projects!*

The Julia manual and the documentation for a large chunk of the ecosystem is generated using [Documenter.jl](https://github.com/JuliaDocs/Documenter.jl) – essentially a static site generator that integrates with Julia and its docsystem. There are tons of opportunities for improvements for anyone interested in working on the interface of Julia, documentation and various front-end technologies (web, LaTeX).

Here are some features or areas that are looking for contributions:

User-contributed notes and examples to documentation (e.g. backed by GitHub Discussions).

One-page-per-function documentation listings (prototype for main Julia manual). See

[JuliaDocs/Documenter.jl#2133](https://github.com/JuliaDocs/Documenter.jl/issues/2133).JuliaSyntax-based code highlighter for Julia code that can be re-used for both the HTML and LaTeX/PDF output.

Rework Documenter's page layout and navigation. See

[JuliaDocs/Documenter.jl#2177](https://github.com/JuliaDocs/Documenter.jl/issues/2177).Improve or rework Documenter's search index.

Work on any of the ideas that have been

[marked as plugins](https://github.com/JuliaDocs/Documenter.jl/labels/Type%3A%20Plugin), as they offer self-contained features to work on.

If any of these sound interesting, please reach out to the mentors to ask for more details and to narrow down the project for a proposal. The possible projects vary in difficulty and size, depending on the project and the ultimate scope.

**Recommended skills**: Depends on the project, but the work would generally involved both Julia programming, but also basic web development (HTML, CSS, JS).

**Mentors:** [Morten Piibeleht](https://github.com/mortenpi), [Fredrik Ekre](https://github.com/fredrikekre)

Best way to reach out is to message in the `#documentation`

channel on the [JuliaLang Slack](https://julialang.org/slack/)!

[Ferrite.jl](https://github.com/ferrite-fem/Ferrite.jl) is a Julia package providing the basic building blocks to develop finite element simulations of partial differential equations. The package provides extensive examples to start from and is designed as a compromise between simplicity and generality, trying to map finite element concepts 1:1 with the code in a low-level . Ferrite is actively used in teaching finite element to students at several universities across different countries (e.g. Ruhr-University Bochum and Chalmers University of Technology). Further infrastructure is provided in the form of different mesh parsers and a Julia based visualizer called [FerriteViz.jl](https://github.com/Ferrite-FEM/FerriteViz.jl).

Below we provide a two of potential project ideas in [Ferrite.jl](https://github.com/ferrite-fem/Ferrite.jl). However, interested students should feel free to explore ideas they are interested in. Please contact any of the mentors listed below, or join the `#ferrite-fem`

channel on the Julia slack to discuss. Projects in finite element visualization are also possible with for example [FerriteViz.jl](https://github.com/Ferrite-FEM/FerriteViz.jl). As a starting point, or to gather inspiration for a potential project, please check out issues marked with [Good First Issue](https://github.com/Ferrite-FEM/Ferrite.jl/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).

**Difficulty**: Medium

**Project size**: 300-350 hours

**Problem**: [Ferrite.jl](https://github.com/ferrite-fem/Ferrite.jl) supports arbitrary order interpolations in 1D and 2D. However, for 3D problems the order for the interpolations is right now limited to interpolations with at most a single dof per face. The difficulty here is of geometric nature. Faces in typical finite element meshes typically have a non-trivial relative orientation, and therefore the facet dofs of the neighboring elements do not match spatially.

**Minimum goal**: A minimal goal would be to add the necessary infrastructure to support the adjustment of the dof location for high order Lagrange polynomial interpolation on all 3D elements interpolations during the dof assignment phase.

**Extended goal**: With this minimally functional example it is possible to extend the project into different directions, e.g. high-order H(div) and H(curl) elements or optimizing the CellCache for these higher order elements by exploiting the tensor-product structure.

**Recommended skills**:

Basic knowledge about the finite element method

Good geometric thinking

The ability (or eagerness to learn) to write fast code


**Mentors**: [Dennis Ogiermann](https://github.com/termi-official) and [Fredrik Ekre](https://github.com/fekre)

**Difficulty**: Hard

**Project size**: 350 hours

**Problem**: Adaptive mesh refinement is an attractive technique to speed up simulations with localized features, like for example steep traveling wave-fronts. Over the last years multiple prototypes have been developed and adopted for a specific use-case. Our generic implementation utilizes ideas from the [p4est](https://p4est.github.io/papers/BursteddeWilcoxGhattas11.pdf) research paper and lives in a separate branch for quite a bit of time now (see [here](https://github.com/Ferrite-FEM/Ferrite.jl/pull/780)). We need more hands to finish the last steps.

**Minimum goal**: As the PR is almost done, the bare minimum would be to push the PR over the finish line. This includes more adding more extensive tests, help with missing documentation, more debug coverage to track down failures and completing a nice user-interface. THe user interface is partially done and needs to cover the marking, error estimation, refinement, coarsening and efficient transfer operations between two nested grids.

**Extended goal**: We see are essentially four ways to can explore as an extended goal. The first one would be to expend the approach as described in the subsequent work by the group (t8code) to allow more element types that just line/quad/hex. The second possible extension would be to parallelize the algorithms and making them GPU ready, so we do not need a roundtrip for the grid through the main memory. The third option would be to allow MPI parallelization and (SFC-based) load balancing. The fourth one is to extend the data structures to 4D hypercubes to allow space-time adaptive simulations.

**Recommended skills**:

Basic knowledge about either the finite element method and/or tree-based data structures

Good geometric thinking

The ability (or eagerness to learn) to write fast code


**Mentors**: [Dennis Ogiermann](https://github.com/termi-official) and [Maximilian Köhler](https://github.com/koehlerson)

**Difficulty**: Hard

**Project size**: 350 hours

**Problem**: [FerriteDistributed.jl](https://github.com/ferrite-fem/FerriteDistributed.jl) is the MPI variant of Ferrite allowing scalable distributed assembly. However, it has been initially developed during the Ferrite v1.0 release window, right before proper subdomain has been added to Ferrite. Therefore, right now the upgrade to Ferrite v1 is primarily blocked by adding proper support for subdomains through the newly introduced SubDofHandler.

**Minimum goal**: At the very least a DistributedSubDofHandler must be added. Therefore the internal communication infrastructure must be upgraded to properly subdomains instead of the full domain.

**Extended goal**: Probably the most useful extended goal right now is to refactor the internal communication infrastructure to better integrate with MPI.jl, as we do not use the full potential of MPI.jl yet. Alternatively, we would like to also allow users to use other distributed memory backends to be used, as for example Reactant.jl.

**Recommended skills**:

Basic knowledge about the finite element method

Basic knowledge about benchmarking

The ability (or eagerness to learn) to write fast code


**Mentors**: [Dennis Ogiermann](https://github.com/termi-official) and [Maximilian Köhler](https://github.com/koehlerson)

[FreeBird.jl](https://github.com/wexlergroup/FreeBird.jl) is a Julia package of enhanced sampling methods, such as nested sampling, Wang-Landau sampling, Metropolis Monte Carlo, for accelerating materials discovery through statistical mechanics. It is designed to be an extensible platform for computationally studying phase equilibria across a diverse range of atomistic and molecular systems, with easy extension to other phenomena.

**Difficulty**: Easy to medium

**Project size**: 175 hours

**Problem**: Nested sampling (NS) for materials is a novel computational algorithm that efficiently explores the phase space (position and momentum) and configuration space of an atomistic system, estimates partition function and detects phase transitions. The nested sampling algorithm requires continuous generation of new atomistic configurations under a monotonously decreasing energy limit. Currently in FreeBird.jl, it is done via a chian of Monte Carlo (MC) random walks. Molecular dynamics (MD) is a proven alternative to MC for a potentially better performance, especially when running on GPUs. In this project, we will integrate the Julia MD package, [Molly.jl](https://github.com/JuliaMolSim/Molly.jl), as the MD backend of NS in FreeBird.jl.

**Expected outcome**:

To implement an easy conversion between FreeBird.jl's walker system and Molly's atoms objects.

To implement a dispatch of the NS function using Molly.jl's MD as a configuration generator.

To enable MD-NS energy evaluations using classical and machine learning interatomic potentials, as well as force fields.

To improve FreeBird.jl's test suits and documentations related to this project.


**Recommended skills**:

Prior exposure or strong interest in computational chemistry and/or materials science

Prior Julia coding experience


**Mentors**: [Ray Yang](https://github.com/yangmr04) (primary), [Joe Greener](https://github.com/jgreener64), [Robert Wexler](https://github.com/rwexler)

**Contact**: Feel free to reach out to Ray Yang via [email](mailto:my@ainest.ee), #juliamolsim on the Julia Slack, or at the JuliaMolSim [Zulip(https://juliamolsim.zulipchat.com)].

Quantum harmonic oscillators are important modalities for quantum computation and quantum networking. A class of them, known as Gaussian bosonic systems, are efficient to simulate on a classical computer. Although such systems do not provide quantum computational advantage, they are present in most protocols and algorithms in continuous variable quantum information. [Gabs.jl](https://github.com/apkille/Gabs.jl) is a Julia library designed to enable fast simulations of Gaussian bosonic circuits and serve as a sandbox for quantum hardware and protocol design.

Non-Gaussian quantum states cannot be simulated via their first- and second-order statistical moments in the phase space representation like Gaussian states. However, there exist fast classical algorithms for simulating superpositions of Gaussian states, which are non-Gaussian in nature. This project involves implementing such algorithmic support for analyzing certain classes of non-Gaussian states.

**Recommended skills:** In-depth understanding of the quantum phase space formalism. [This paper](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.110.042402) and [also this paper](https://arxiv.org/abs/2404.07115) are useful references.

**Mentors:** [Andrew Kille](https://github.com/apkille) and [Stefan Krastanov](https://github.com/Krastanov).

**Expected duration:** 175 hours (but applicants can scope it as longer if they plan more extensive work)

**Difficulty:** Medium

A matrix product state (MPS) is a valuable tensor network method for simulating quantum many-body systems. In particular, large continuous variable quantum systems that contain low entanglement can be simulated extremely fast with the MPS method. This project involves implementing support for MPS representations of Gaussian and non-Gaussian systems.

**Recommended skills:** In-depth understanding of the quantum phase space formalism. In addition, familiarity with tensor network methods and software such as [ITensors.jl](https://github.com/ITensor/ITensors.jl). For this project, [this paper](https://opg.optica.org/optica/fulltext.cfm?uri=optica-8-10-1306&id=460148) and [also this paper](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.104.012415) are useful references.

**Mentors:** [Andrew Kille](https://github.com/apkille) and [Stefan Krastanov](https://github.com/Krastanov).

**Expected duration:** 175 hours (but applicants can scope it as longer if they plan more extensive work)

**Difficulty:** Hard

Due to the technological maturity of quantum measurement schemes for photons, one-way quantum computation is an attractive approach for photonic quantum processing. In the continuous variable formalism, Gaussian cluster states serve as an important piece of the measurement-based quantum computation model. This project involves the creation of conversion tools between phase space representations of Gaussian bosonic systems and Gaussian cluster states in the graph formalism.

**Recommended skills:** Understanding of the quantum phase space formalism and the measurement-based quantum computation model. [This review article](https://journals.aps.org/rmp/pdf/10.1103/RevModPhys.84.621) and [recent paper](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.2.030343) is a useful reference.

**Mentors:** [Andrew Kille](https://github.com/apkille) and [Stefan Krastanov](https://github.com/Krastanov).

**Expected duration:** 175 hours (but applicants can scope it as longer if they plan more extensive work)

**Difficulty:** Easy

Graph Neural Networks (GNN) are deep learning models that are well adapted to data in the form of graphs with feature vectors associated with nodes and edges. GNNs are a growing area of research and find many applications in complex network analysis, relational reasoning, combinatorial optimization, molecule generation, and many other fields.

[GraphNeuralNetworks.jl](https://github.com/CarloLucibello/GraphNeuralNetworks.jl) is a pure Julia package for GNNs equipped with many features. It implements common graph convolutional layers, with CUDA support and graph batching for fast parallel operations. There are several ways by which the package could be improved.

As part of the documentation and for bootstrapping new projects, we want to add fully worked-out examples and applications of graph neural networks. We can start with entry-level tutorials and progressively introduce the reader to more advanced features.

**Duration**: 175h.

**Expected difficulty**: easy.

**Expected outcome**: A few pedagogical and more advanced examples of graph neural network applications.

Provide Julia-friendly wrappers for common graph datasets in [ MLDatasets.jl](https://github.com/JuliaML/MLDatasets.jl). Create convenient interfaces for the Julia ML and data ecosystem.

**Duration**: 175h.

**Expected difficulty**: easy.

**Expected outcome**: A large collection of graph datasets easily available to the Julia ecosystem.

Many graph convolutional layers can be expressed as non-materializing algebraic operations involving the adjacency matrix instead of the slower and more memory-consuming gather/scatter mechanism. We aim at extending as far as possible and in a gpu-friendly way these *fused* implementation. The project will involve fixing some outstanding issues in CUDA.jl that are blocking sparse adjacency matrix support on GPU.

**Duration**: 350h.

**Expected difficulty**: hard.

**Expected outcome**: A noticeable performance increase for many graph convolutional operations.

We currently support scatter/gather operation only on CPU and CUDA hardware. We aim to extend this to AMDGPU and Apple Silicon leveraging KernelAbstractions.jl, AMDGPU.jl, and Metal.jl.

**Duration**: 175h.

**Expected difficulty**: medium.

**Expected outcome**: Graph convolution speedup for AMD GPU and Apple hardware, performance roughly on par with CUDA.

[Carlo Lucibello](https://github.com/CarloLucibello) (author of [GraphNeuralNetworks.jl](https://github.com/JuliaGraphs/GraphNeuralNetworks.jl)). Feel free to contact me on the [Julia Slack Workspace](https://Julialang.slack.com/) or by opening an issue in the GitHub repo.

[JuliaGPU](https://github.com/JuliaGPU) provides a suite of packages for programming GPUs in Julia. We have support for AMD, NVIDIA and Intel GPUs through various backends, unified by high-level array abstractions and a common programming model based on kernel programming.

**Difficulty:** Medium

**Duration:** 175 or 350 hours (the scope of functionality to port can be adjusted accordingly)

**Description:** The Julia GPU stack consists of several layers, from low-level vendor-specific packages like CUDA.jl to high-level abstractions like GPUArrays.jl. While the high-level packages aim to be vendor-agnostic, many optimized operations are still implemented in vendor-specific ways. This project aims to improve portability by moving these implementations to GPUArrays.jl using KernelAbstractions.jl.

The project will involve:

Identifying vendor-specific kernel implementations in packages like CUDA.jl

Porting these kernels to KernelAbstractions.jl in GPUArrays.jl

Improving KernelAbstractions.jl where needed to support these kernels

Ensuring performance remains competitive with vendor-specific implementations

Adding tests to verify correctness across different GPU backends


**Required Skills:**

Experience with Julia programming

Familiarity with GPU programming concepts

Experience with GPU programming in Julia is a plus

Understanding of performance optimization


**Expected Results:** A set of optimized GPU kernels in GPUArrays.jl that are vendor-agnostic and performant across different GPU backends. This will improve the portability of the Julia GPU stack and make it easier to support new GPU architectures.

**Mentors:** [Tim Besard](https://github.com/maleadt), [Valentin Churavy](https://github.com/vchuravy)

Wouldn’t it be great if Julia would program itself? Tell it what you want, Julia magic happens, and you get your program directly. We introduce Herb.jl, a library written in Julia that gets us a step closer to our big goal. [Herb.jl](https://herb-ai.github.io/) is a library for program synthesis: The task of automatically generating programs from a given specification. Here, “a program” could be anything, from an actual Python program over moves in chess to the synthesis of biochemical molecules. There are numerous works on program synthesis, all speaking a different language in code and terminology. We want to make developing, comparing, and applying ideas in program synthesis easier.

Herb’s main goal is, therefore, two-fold. First, we aim to provide a toolbox for 1. developing new program synthesizers or 2. easily re-implementing existing ones. Second, we aim to unify many different flavors of program synthesis under a joint framework, making program synthesizers easy to use on new problems.

If you have any questions or ideas, please [contact Tilman](mailto:t.r.hinnerichs@tudelft.nl).

**Difficulty:** Medium

**Estimated Duration:** 350 hours

**Project Overview:** `Herb.jl`

has an outstanding performance in enumerating programs. Every generated program also needs to be evaluated, making evaluation the main bottleneck in finding a suitable program. We want to improve this aspect by leveraging various well-engineered projects from the Julia community.

First, we have so far lessened the burden of evaluation by developing custom interpreters. This is time-consuming and error-prone, so we would like to avoid it. The core challenge here is that the explore programs don't have a fixed structure and are constructed during synthesis; therefore, they cannot be compiled ahead of time. The Julia package `DynamicExpressions.jl`

is developed to overcome this exact problem, allowing for "ridiculously fast symbolic expressions". We would like to integrate `DynamicExpressions.jl`

into our ecosystem and get a faster evaluation of Julia programs *for free*.

Second, Herb is limited to Julia so far. Our goal is, however, to make Herb a *language agnostic* program synthesis library. We would like to extend Herb with connections to other interpreters for common languages like Python, Java, Prolog, et cetera. This would make it possible for Herb users to use any programming language that fits their needs.

Third, another crucial aspect of every program synthesis engine is the construction of candidate programs. State-of-the-art program synthesis tools, like CVC5, have invested significant time into optimizing the program construction step, resulting in significantly improved performance. We want to map these ideas into Herb.

**Minimum goal:** Connect `DynamicExpressions.jl`

to `Herb.jl`

. This involves implementing the expression interface from `DynamicExpressions.jl`

for `Herb.jl`

’s expression tree formulation.

**Extended goal:** Add support for at least one non-Julia program interpreter or add tricks from CVC5 to Herb.

**Recommended skills:**

basic knowledge of data structures

interest in program optimization

the eagerness to learn to write and optimize code


**Mentors:** Reuben Gardos-Reid, Tilman Hinnerichs and Sebastijan Dumancic

**Some literature:**

The Program Synthesis book (by Gulwani et al.,

[link](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/10/program_synthesis_now.pdf)CVC4SY paper:

[link](https://link.springer.com/chapter/10.1007/978-3-030-25543-5_5)`DynamicExpression.jl`

:[link](https://ai.damtp.cam.ac.uk/dynamicexpressions/dev/)Our website:

[link](https://herb-ai.github.io/)

**Difficulty:** Medium

**Estimated Duration:** 350h

**Problem description:** Neurally-guided program synthesizers form a popular class of synthesizers, which learn a heuristic to guide program generation. Following Herb's paradigm to unify the field, we want to reach the same goal for this sub-field. Specifically, learning guiding policies comprise the same building blocks of 1. program sampling, 2. program-data-encoding, 3. policy learning with respect to a loss function, and 4. deploying that strategy.

In this project, we want to implement these building blocks to allow researchers to reuse the modules directly. To guide this project, we implemented a template structure to follow and extend.

**Minimum goal:** Implement a naive but modular strategy for all four steps. To allow for easy integration of with existing models, we aim to implement the machine learning part using Flux.jl.

**Extended goal:** The extended goal is to deepen one or more of these modules that fit the student's interests. The literature provides numerous ideas on how to make all four steps smarter individually. Concretely, this could include

smarter program-sampling,

different program encoding strategies from the literature,

implementing and applying different loss functions, and

incorporating this with different search procedures.


**Recommended skills:**

Basic knowledge of machine learning principles (neural networks, model training, ...)

Preferably prior experiences with Flux.jl


**Mentors:** Tilman Hinnerichs, Reuben Gardos-Reid and Sebastijan Dumancic

**Some literature:**

The Program Synthesis book (by Gulwani et al.,

[link](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/10/program_synthesis_now.pdf)Our website:

[https://herb-ai.github.io/](https://herb-ai.github.io/)BUSTLE: Bottom-up Program Synthesis through learning-guided exploration:

[link](https://arxiv.org/pdf/2007.14381)DeepCoder

[link](https://arxiv.org/pdf/1611.01989)DreamCoder

[link](https://dl.acm.org/doi/pdf/10.1145/3453483.3454080)

Julia is emerging as a serious tool for technical computing and is ideally suited for the ever-growing needs of big data analytics. This set of proposed projects addresses specific areas for improvement in analytics algorithms and distributed data management.

**Difficulty:** Medium (175h)

Sometimes a problem fits in GPU memory - great! Sometimes the problem only fits in CPU memory, but you want to use the GPU - hmm, complicated but doable. What if the problem doesn’t fit in any kind of memory? This is the problem that “out-of-core” computing seeks to solve - how to fit a large dataset into small memory and run important computations on it. In this project, you’ll dive deep into how Dagger.jl handles data management on the CPU and GPU, and implement logic in Dagger’s scheduler to allow it to pace computations to ensure they don’t exceed GPU memory, keeping datasets resident on the CPU when not in use. Going further, you’ll extend this approach to allow loading datasets from disk (files) or the network (S3, etc.) and operating on portions of the dataset on the CPU and GPU. In the end, you’ll enable Dagger to run nearly any algorithm on datasets of any size with ease and with good performance.

**Skills:** Familiarity with CPU-GPU communication, dataset partitioning

**Mentors:** [Julian Samaroo](https://github.com/jpsamaroo), and [Felipe Tomé](https://github.com/fda-tome)

**Difficulty:** Hard (350h)

Task scheduling is a complicated endeavor even when done statically, dynamism takes it to another dimension of complexity - memory pressure, resource utilization, communication density, HBM availability, and processor throughput are just some of variables that need to be taken into account. Knowing that, this project will provide you with the opportunity to tune and implement an MILP (Mixed Integer Linear Program) model that takes Dagger’s scheduler into a different realm of computational efficiency. This model will take measured or simulated metrics into account when scheduling tasks across heterogeneous resources or even a large computing cluster. Additionally, as optimizations become more computationally expensive, you will implement a metaheuristic approach to simplifying the model to maintain reasonable scheduling performance.

**Skills:** Mathematical optimization, metaheuristics solutions, performance modeling.

**Mentors:** [Julian Samaroo](https://github.com/jpsamaroo), and [Przemysław Szufel](https://szufel.pl/)

**Difficulty:** Medium (175h)

There is no possible way of solving a problem if you’re not aware of the cause and nature of it - that is where data collection comes in handy - from roofline models to simple time measurements, data analysis and visualization has been the performance engineer’s best friend from the beginning of the area until now. For this project, you will take stock of Dagger’s current set of collected metrics and identify those which are missing or overly non-specific. You will then devise and implement measurement and collection techniques to implement and refine these metrics, and implement storage and querying infrastructure to make their values observable. Finally, you will implement visualization and reporting tools that use these collected metrics to provide additional insight into Dagger’s performance on various algorithms to aid in performance tuning and scheduler development.

**Skills:** Broad understanding of parallel algorithm tuning, visualization.

**Mentors:** [Felipe Tomé](https://github.com/fda-tome), and [Julian Samaroo](https://github.com/jpsamaroo)

**Difficulty:** Hard (350h)

This project aims to explore and enhance GPU performance by integrating [Dagger.jl](https://github.com/JuliaParallel/Dagger.jl), Julia’s high-performance parallel computing framework, with GPU multistream capabilities. Dagger.jl enables task-based parallelism, allowing complex computations to be broken down into smaller, manageable tasks that can be efficiently scheduled across computing resources. By incorporating GPU multistreams, students will investigate how multiple streams can be used to overlap data transfers with kernel executions, enabling concurrent operations on the GPU. This overlapping reduces idle times, as data movement and computations occur simultaneously, thus maximizing GPU resource utilization. The project will focus on designing and implementing parallel workflows where independent tasks are executed concurrently, leveraging Dagger’s dynamic task scheduling and GPU’s ability to manage multiple streams effectively. Students will experiment with different workload patterns, measure performance improvements, and analyze the impact of multistream execution on throughput and latency. Through performance benchmarking and optimization, this project will provide hands-on experience in GPU programming, parallel algorithm design, and high-performance computing, equipping students with valuable skills for tackling real-world scientific and data-intensive applications.

There are projects now that host the building blocks: [DaggerGPU.jl](https://github.com/JuliaGPU/DaggerGPU.jl) and [Dagger.jl](https://github.com/JuliaParallel/Dagger.jl) which can serve as jumping off points.

**Skills:** Familiarity with GPU, representing execution models as DAGs, CUDA.jl

**Mentors:** [Julian Samaroo](https://github.com/jpsamaroo), and [Rabab Alomairy](https://github.com/Rabab53)

**Difficulty:** Hard (350h)

Add distributed linear algebra capabilities to Dagger.jl. This project will involve building abstractions for distributed linear algebra operations, such as matrix multiplication, matrix factorizations, and different data distribution schemes (cyclic, block-cyclic, 2D, 3D). The student will build on top of Dagger.jl to enable distributed linear algebra operations across multiple devices. The final result should demonstrate a linear algebra operation running across multiple devices in parallel via the Dagger.jl APIs.

**Skills:** Familiarity with distributed computing, numerical linear algebra, Dagger.jl

**Mentors:** [Felipe Tomé](https://github.com/fda-tome), and [Rabab Alomairy](https://github.com/Rabab53)

**Difficulty:** Hard (350h)

Dynamic scheduling for Mixture of Experts (MoE) in LLM faces significant challenges due to the irregular computation patterns induced by expert routing, leading to load imbalances, underutilization of compute resources, and high communication overhead. Each token in MoE is routed to only a subset of experts, causing varying batch sizes and unbalanced workload distribution across experts. The traditional static scheduling approach does not efficiently handle these dynamic task assignments. By using Dagger.jl, we can implement a more dynamic, task-based scheduling system that assigns tokens to experts based on real-time compute availability, ensuring a more balanced workload. Dagger’s asynchronous scheduling allows for efficient parallel execution by dynamically distributing the tasks across multiple devices or compute units, improving GPU utilization and reducing bottlenecks. Furthermore, optimizations such as load balancing algorithms, soft routing mechanisms, and fine-grained task prioritization could be applied to maximize resource utilization and minimize execution time. Solving these optimization problems will not only enhance performance but also improve scalability, making MoE models more efficient and suitable for large-scale deployments.

**Skills:** Familiarity with GPU, representing execution models as Flux.jl, DAGs, and CUDA.jl

**Mentors:** [Julian Samaroo](https://github.com/jpsamaroo), and [Rabab Alomairy](https://github.com/Rabab53)

**Difficulty:** Hard (350h)

Add a distributed training API for Flux models built on top of [Dagger.jl](https://github.com/JuliaParallel/Dagger.jl). More detailed milestones include building Dagger.jl abstractions for [UCX.jl](https://github.com/JuliaParallel/UCX.jl), then building tools to map Flux models into data parallel Dagger DAGs. The final result should demonstrate a Flux model training with multiple devices in parallel via the Dagger.jl APIs. A stretch goal will include mapping operations with a model to a DAG to facilitate model parallelism as well.

There are projects now that host the building blocks: [DaggerFlux.jl](https://github.com/FluxML/DaggerFlux.jl) and [Distributed Data Parallel Training](https://github.com/DhairyaLGandhi/ResNetImageNet.jl) which can serve as jumping off points.

**Skills:** Familiarity with UCX, representing execution models as DAGs, Flux.jl, CUDA.jl and data/model parallelism in machine learning

**Mentors:** [Julian Samaroo](https://github.com/jpsamaroo), and [Dhairya Gandhi](https://github.com/DhairyaLGandhi)

**Difficulty**: Medium to Hard.

**Length**: 175 to 350 hours depending on the project.

[Agents.jl](https://juliadynamics.github.io/Agents.jl/stable/) is a pure Julia framework for agent-based modeling (ABM). It has an extensive list of features, excellent performance and is easy to learn, use, and extend. Comparisons with other popular frameworks written in Python or Java (NetLOGO, MASON, Mesa), show that Agents.jl outperforms all of them in computational speed, list of features and usability.

In this project, contributors will be paired with lead developers of Agents.jl to improve Agents.jl with more features, better performance, and overall higher polish. We are open to discuss with potential candidate a project description and outline for it!

Possible features to implement are:

GPU and/or HPC support in Agents.jl by integrating existing ABM packages (Vanaha.jl or CellBasedModels.jl) into Agents.jl API.

Differentiation / parameter fitting of ABMs in Agents.jl by utilizing StochasticAD.jl or similar frameworks.


**Pre-requisite**: Having already contributed to a Julia package either in JuliaDynamics or of sufficient relevance to JuliaDynamics.

**Recommended Skills**: Familiarity with agent based modelling, Agents.jl and Julia's Type System, and achieving high-end computational performance within Julia. Familiarity with complex systems or nonlinear dynamics is not required but would be a positive.

**Expected Results**: Well-documented, well-tested useful new features for Agents.jl.

**Mentors**: [George Datseris](https://github.com/Datseris).

**Difficulty:** Easy to Medium to Hard, depending on the project.

**Length**: 175 to 350 hours, depending on the project.

[DynamicalSystems.jl](https://juliadynamics.github.io/DynamicalSystems.jl/latest/) is an [award-winning](https://dsweb.siam.org/The-Magazine/Article/winners-of-the-dsweb-2018-software-contest) Julia software library for dynamical systems, nonlinear dynamics, deterministic chaos, and nonlinear time series analysis. It has an impressive list of features, but one can never have enough. In this project, contributors will be able to enrich DynamicalSystems.jl with new algorithms and enrich their knowledge of nonlinear dynamics and computer-assisted exploration of complex systems.

Here is a list of high-impact, Hard (350 hours) projects that we want to prioritize.

Local and global continuation in dynamical systems combined in one. This will be a ground-breaking feature, combining cutting edge research on multistable dynamical systems with the established bifurcation-continuation analysis.


Other than that, we do not outline more possible projects here, and instead we invite interested candidates to explore the documentation and list of open features of any of the subpackages of DynamicalSystems.jl. Then the candidates can reach out to one of the developers of the subpackage to devise a project outline. We strongly welcome candidates that already have potential project ideas in mind already irrespectively of the open list of issues.

**Pre-requisite**: Having already contributed to a Julia package either in JuliaDynamics or of sufficient relevance to JuliaDynamics.

**Recommended Skills**: Familiarity with nonlinear dynamics and/or differential equations and/or timeseries analysis based on the Julia language.

**Expected Results**: Well-documented, well-tested new algorithms for DynamicalSystems.jl.

**Mentors**: [George Datseris](https://github.com/Datseris)

[JuliaGenAI](https://github.com/JuliaGenAI) is an organization focused on advancing Generative AI research and looking for its applications within the Julia programming language ecosystem. Our community comprises AI researchers, developers, and enthusiasts passionate about pushing the boundaries of Generative AI using Julia's high-performance capabilities. We strive to create innovative tools and solutions that leverage the unique strengths of Julia in handling complex AI challenges.

**IMPORTANT:** There will not be any projects mentored this year by Jan Siml (`svilupp`

) and Cameron Pfiffer (`cpfiffer`

) due to time constraints, but we will be happy to answer any questions you might have - see below how to contact us.

There is a high overlap with other organizations, you should definitely check out these projects:

[Projects in Reinforcement Learning](https://julialang.org/jsoc/gsoc/machine-learning/)- For projects around AlphaZero.jl[Projects with FluxML](https://fluxml.ai/gsoc/)- For projects around Flux.jl, the backbone of Julia's deep learning ecosystem

Probably the easiest way is to join our [JuliaLang Slack](https://julialang.org/slack/) and join the `#generative-ai`

channel. You can also reach out to us on [Julia Zulip](https://julialang.zulipchat.com/#narrow/stream/423470-generative-ai) or post a GitHub Issue on our website [JuliaGenAI](https://github.com/JuliaGenAI/juliagenai.org).

The [JuliaGeo](https://github.com/JuliaGeo) collaboration

Mentors: [Anshul Singhvi (JuliaHub)](https://julialang.org/anshul.singhvi@juliahub.com), Milan Klöwer (Oxford)

Observations and simulations of the Earth produce vast amounts of data, complicating analysis. Efficient data analysis often includes visualization, either in early stages to inspect features in the data but also to produce publication-ready graphs and animations. Given the (approximately) spherical shape of Earth, visualization software ideally supports data and operations thereof in spherical coordinates. Some data may come in the form of point measurements or polygons and gridded data is represented through large sets of polygons (so-called grids) covering the sphere. Many different grids are used for various reasons and purposes: regular and unstructured, based on triangles, quadrilaterals or hexagons, some are equal-area others have two north poles, to give some examples. In Julia, the JuliaGeo organisation together with MakieOrg and GeoMakie cover already a lot of this functionality. But more needs to be done to allow for seamless visualisations of geographic data on the sphere.

Quite a bit of foundational work needs to be done for spherical visualizations to be seamless. Students will work on the GeoMakie.jl spherical axis, using the principles of spherical and Cartesian geometry to create a smooth, interactive globe viewer. Work may include:

Spherical horizon culling for map tiles in 3D space, a la Google Maps

Switching from a three-dimensional globe to a two-dimensional projection (again, a la Google Maps or Mapbox)

Implementing a Cartopy-style projection interface in Julia, including known projection boundary polygons

Implementing a nice coordinate / geometry transformation composition interface to facilitate this, also like what Mapbox does.


Reach out to the mentors to learn more!

[GeometryOps.jl](https://github.com/JuliaGeo/GeometryOps.jl) is a new framework for geometry processing on the plane and the sphere. There are many algorithms that remain to be implemented (e.g. [concave hull], [line merging], [polygon validation]), and you could also propose an algorithm that you want to implement or improve!

Some other areas of interest are:

Wrapping Google's

`s2geometry`

library in Julia, either by building a C API to s2geometry or s2geography, or by building a

WrapIt.jl or CxxWrap.jl wrapper for s2.

Improving the operation interface for GeometryOps and creating a declarative (a la CoordinateTransformations.jl, e.g.

`(Segmentize(Spherical(), max_distance = 1000) * ConcaveHull(threshold) * Area())(geom)`

, which can pre-allocate and apply the required preparations at once, instead of piecemeal.Any other projects an interested student might want to pick up!


JuliaHealth is an organization dedicated to improving healthcare by promoting open-source technologies and data standards. Our community is made up of researchers, data scientists, software developers, and healthcare professionals who are passionate about using technology to improve patient outcomes and promote data-driven decision-making. We believe that by working together and sharing our knowledge and expertise, we can create powerful tools and solutions that have the potential to transform healthcare.

**Description:** HealthLLM.jl is a Retrieval-Augmented Generation (RAG) framework that provides a foundation for domain-specific LLM workflows across JuliaHealth. The long-term vision for HealthLLM.jl is to enable workflows across JuliaHealth that lower the barrier to health data analysis while maintaining the reproducibility and auditability that health research demands. Validation efforts will focus on FunSQL.jl queries for a testing harness, while the architecture is designed to generalize to broader JuliaGenAI LLM tooling for JuliaHealth.

**Mentor:**Jacob S. Zelko (aka TheCedarPrince) [email: jacobszelko@gmail.com]**Difficulty:**Medium**Duration:**175 hours**Suggested Skills and Background:**Experience with Julia

Strong expertise with LLM and RAG pipelines

Experience with the following is necessary:

FunSQL.jl

PromptingTools.jl or other Julia-native GenAI tooling

Vector database technologies (e.g. PgVector, FAISS, Qdrant)


Comfort with the OMOP CDM or health informatics concepts


**Outcomes:**Refactor the RAG pipeline into modular components (retrieval, generation, post-processing, evaluation) with improved prompt templates, error handling, and logging

Survey and evaluate multiple LLMs on FunSQL-based query generation tasks using standardized metrics (accuracy, latency, cost)

Provide comprehensive documentation, reproducible evaluation scripts, and final experimental results

Design and implement an abstract interface supporting multiple vector database backends, with benchmarking across backends (stretch goal)



No projects this year!


**Difficulty:** Hard / Ambitious **Duration:** 350 hours (22 weeks) **Mentor:** Jakub Mitura **Technology Stack:** Julia, Lux.jl, NNlib.jl, ChainRules.jl, LogExpFunctions.jl

Deep learning in medical diagnostics suffers from a well-known trust gap. Models often behave as black boxes and may produce physiologically implausible predictions — for example simultaneously predicting cachexia and obesity. This lack of interpretability and clinical consistency limits adoption of AI systems in healthcare environments.

Neurosymbolic artificial intelligence (NeSy) addresses this limitation by integrating structured logical knowledge directly into neural models. However, many existing approaches struggle with numerical stability, scalability, and GPU efficiency when deployed in realistic clinical settings.

KLAY-Core is a high-performance logical constraint layer designed for Lux.jl. It enables domain experts and developers to encode clinical knowledge as differentiable logical constraints integrated directly into neural network architectures.

Using the Knowledge Layers (KLAY) architecture, the project introduces static linearization of logical circuits (d-DNNF) into optimized tensor buffers. Circuit evaluation is reduced to sequences of NNlib.scatter operations and tensor indexing, significantly improving GPU parallel efficiency while ensuring physiologically consistent predictions.

The project follows a "compile once, evaluate often" paradigm for efficient integration of symbolic knowledge into neural models.

**Yggdrasil and JLL Integration**

High-performance symbolic compilers (e.g., d4, SDD) will be distributed as precompiled binaries via Yggdrasil and JLL packages. This guarantees a fully Julia-native workflow without requiring Python environments or local C++ toolchain configuration.

**Level-Order Flattening**

A dedicated algorithm groups logical graph nodes into layers based on structural height. This converts hierarchical logical circuits into flat GPU-friendly buffers, eliminating recursion and enabling efficient parallel execution.

**Solving the Derivative Bottleneck**

Custom adjoints (rrule) implemented using ChainRules.jl ensure backward-pass efficiency comparable to standard neural layers while avoiding excessive memory overhead typical of recursive automatic differentiation.

To reduce usability barriers for clinicians and developers, the package introduces a domain-specific DSL macro supporting full Boolean logic and weighted relationships where w ∈ [0,1].

Unlike Python-based frameworks such as Dolphin, which rely on object-oriented logic definitions, KLAY-Core offers a declarative macro interface integrated directly with the Julia compiler. This improves readability, auditability, and interdisciplinary collaboration between clinicians and AI engineers.

**Supported Logical Operators:**

AND (

`&`

) — logical conjunctionOR (

`|`

) — logical alternativeNOT (

`!`

) — logical negationImplication (

`->`

) — logical implication

**Constraint Types:**

*Hard Constraints (w = 1.0):* Strict logical rules ensuring physiological consistency.

*Soft Constraints (w < 1.0):* Probabilistic correlations or clinical risk relationships.

**Explicit Layer Design**

Implementation of an AbstractExplicitLayer where circuit structure is stored in the layer state while constraint strengths remain trainable parameters. This supports determinism, transparency, and reproducibility required in medical AI systems.

**Log-Space Numerical Stability**

Logical gates are evaluated in logarithmic space using logsumexp (OR) and summation (AND), preventing numerical instability and vanishing-gradient effects.

| Feature | KLAY-Core (Julia) | Dolphin (Python/PyTorch) | DeepProbLog / LTN | Juice.jl (Julia) |
|---|---|---|---|---|
| GPU Parallelism | Native scatter-reduce | Standard PyTorch ops | Mostly sequential | Limited optimized kernels |
| Integration | Native Lux.jl | Wrapper-style integration | Python–C++ bridges | Independent library |
| Ecosystem | JLL / Yggdrasil | Pip / Conda environments | Mixed dependencies | Native Julia ecosystem |
| Interface | High-level DSL macro | Python API definitions | Logic-heavy syntax | Low-level graph APIs |
| Gradient Stability | Custom rrule | Standard AD | Potential instability | Variable stability |

**Competitive Edge:** KLAY-Core combines Julia's performance, macro system, and binary artifact ecosystem with a modern explicit deep learning framework (Lux.jl). Rather than functioning as an external wrapper, it becomes an integral neural network component, simplifying deployment, improving reproducibility, and reducing operational complexity in clinical AI environments.

**Phase 1 (Weeks 1–4):**Development of the @clinical_rule DSL and Yggdrasil/JLL integration.**Phase 2 (Weeks 5–9):**Flattening logical circuits into recursion-free GPU buffers.**Phase 3 (Weeks 10–13):**Custom rrule differentiation and log-space stability optimization.**Phase 4 (Weeks 14–17):**Validation using the Heart Failure Prediction Dataset with focus on: Accuracy, Brier Score, Expected Calibration Error (ECE), AUROC, and Constraint violation rates.**Phase 5 (Weeks 18–20):**Performance benchmarking against Dolphin, DeepProbLog, and Juice.jl.**Phase 6 (Weeks 21–22):**Final documentation, testing, and publication in the Julia General Registry.

Alam, S., et al. (2026). Constraint-aware neurosymbolic uncertainty quantification with Bayesian deep learning for scientific discovery. arXiv preprint (arXiv:2601.12442).

Chicco, D., & Jurman, G. (2020). Machine learning can predict survival of patients with heart failure from serum creatinine and ejection fraction alone. BMC Medical Informatics and Decision Making, 20, 16.

Dang, M., et al. (2021). JUICE: A Julia package for logic and probabilistic circuits. In Proceedings of the AAAI Conference on Artificial Intelligence, 35(14).

Fedesoriano. (2021). Heart failure prediction dataset [Dataset]. Kaggle.

Lagniez, J.-M., & Marquis, P. (2017). An improved decision-DNNF compiler (d4). In Proceedings of the 26th International Joint Conference on Artificial Intelligence (IJCAI 2017).

Maene, J., & Derkinderen, V. (2024). KLAY: Accelerating arithmetic circuits for neurosymbolic AI. arXiv preprint (arXiv:2410.11415).

Manhaeve, R., Demeester, T., Rocktäschel, T., & De Raedt, L. (2018). DeepProbLog: Neural probabilistic logic programming. In Advances in Neural Information Processing Systems (NeurIPS 2018).

Pal, A. (2023). Lux: Explicit parameterization of deep neural networks in Julia [Software]. Zenodo.


**Difficulty:** Hard **Duration:** 350 hours **Mentor:** Jakub Mitura **Technology Stack:** Julia, Lux.jl, MedPipe3D.jl, KernelAbstractions.jl, CUDA.jl, MLUtils.jl, MoonCake.jl

3D Capsule Network layer primitives (dynamic routing, locally-constrained routing) as reusable Lux.jl modules

Two full architectures: 3D SegCaps and 3D SegCaps-UNet hybrid

Custom GPU-accelerated routing kernels via KernelAbstractions.jl

End-to-end training/evaluation pipeline integrated with MedPipe3D.jl

Comprehensive benchmarks (Dice, HD95, cross-task transfer) across all 10 Medical Segmentation Decathlon tasks vs. 3D U-Net baseline

Documentation, pretrained weights, and reproducible experiment scripts contributed to JuliaHealth


This project is scoped for a 350-hour GSoC timeframe (approximately 12–13 weeks). The following milestones and success criteria outline the expected progression.

**Community Bonding (pre-coding period)**

Finalize detailed project plan and milestones with mentors.

Familiarize with Lux.jl, MedPipe3D.jl, KernelAbstractions.jl, and existing MedPipe3D pipelines.

Set up development environment, GPU access, and reproduction of a baseline 3D U-Net on a subset of the Medical Segmentation Decathlon.


**Weeks 1–3: Core Capsule Primitives and 3D Extensions**

Implement and test core capsule network building blocks in Lux.jl:

Squash nonlinearity, routing coefficients, and routing-by-agreement loops.

Pose and activation representations suitable for 3D convolutional capsules.


Extend these primitives to 3D convolution capsules (pose matrices, shared transformation matrices).

Unit tests validating tensor shapes, numerical stability, and differentiability.

Success criterion: Stable forward and backward passes for 3D capsule layers on synthetic 3D data.


**Weeks 4–6: SegCaps Architectures and Integration**

Design and implement:

A 3D SegCaps encoder–decoder architecture.

A 3D SegCaps–UNet hybrid that replaces CNN blocks with capsule blocks while retaining skip connections.


Integrate architectures with MedPipe3D.jl data loading and preprocessing (NIFTI/DICOM I/O, patching/tiling).

Implement basic training scripts (single-task training on 1–2 Decathlon tasks).

Success criterion: End-to-end training runs to convergence on at least one Decathlon task, with validation metrics logged.


**Weeks 7–9: Efficient Routing and GPU Optimization**

Implement locally-constrained routing strategies to reduce computational cost and memory usage for volumetric data.

Prototype and benchmark custom GPU-accelerated routing kernels using KernelAbstractions.jl.

Profile training to identify and remove performance bottlenecks (e.g., memory layout, batching strategy).

Success criterion: Capsule models train with acceptable throughput (within 2–3× of 3D U-Net) on a modern GPU and fit into GPU memory for standard Decathlon volumes.


**Weeks 10–11: Benchmarking and Cross-Task Transfer**

Train and evaluate 3D SegCaps and SegCaps–UNet models across all 10 Medical Segmentation Decathlon tasks.

Implement cross-task transfer experiments (pretrain on one organ/modality, fine-tune on another).

Compare performance against a strong 3D U-Net baseline using Dice, HD95, and cross-task transfer performance.

Success criterion: Complete benchmark tables/plots and clear analysis of where capsule models help or hurt relative to U-Net.


**Week 12+: Documentation, Polish, and Upstreaming**

Clean and document code, ensuring idiomatic Julia and Lux.jl usage.

Write user-facing documentation and examples (e.g., minimal training script, configuration templates).

Prepare pretrained weights, experiment configuration files, and reproducibility instructions (including random seeds and environment description).

Submit pull requests to relevant JuliaHealth repositories and iterate based on maintainer feedback.

Success criterion: Merged contributions into JuliaHealth repositories plus a project report summarizing methods, experiments, and lessons learned.


This project implements 3D Capsule Network (CapsNet) architectures within the Julia ecosystem using Lux.jl and MedPipe3D.jl for volumetric medical image segmentation. The core work involves building a SegCaps (Segmentation Capsules) layer abstraction supporting dynamic routing-by-agreement, extending it to 3D convolution capsules with equivariance-preserving pose matrices. We will implement two key variants: (1) a 3D SegCaps U-Net hybrid that replaces encoder/decoder conv blocks with capsule layers while retaining skip connections, and (2) an efficient locally-constrained routing variant to manage the quadratic computational cost of full capsule coupling in volumetric data. Custom CUDA kernels via KernelAbstractions.jl will accelerate the routing procedure, and the full pipeline—preprocessing, training, and evaluation—will integrate with MedPipe3D.jl's NIFTI/DICOM I/O and metric infrastructure.

The central hypothesis is that capsule networks' explicit encoding of part-whole spatial hierarchies and viewpoint-equivariant pose vectors yields superior cross-domain generalization compared to standard CNNs, which rely on max-pooling and thus discard spatial relationships. We will rigorously benchmark 3D SegCaps against a 3D U-Net baseline across all 10 tasks of the Medical Segmentation Decathlon (covering CT and MRI across brain, liver, lung, pancreas, etc.), measuring not only per-task Dice/HD95 but critically cross-task transfer: models pretrained on one organ/modality and fine-tuned on another. We expect capsule routing to better preserve geometric structure across domains, improving few-shot adaptation. All code, pretrained weights, and reproducible experiment scripts will be contributed to the JuliaHealth ecosystem under MIT license.

Sabour, S., Frosst, N., & Hinton, G. E. (2017).

*Dynamic Routing Between Capsules*. Advances in Neural Information Processing Systems (NeurIPS).[https://arxiv.org/abs/1710.09829](https://arxiv.org/abs/1710.09829)Hinton, G. E., Sabour, S., & Frosst, N. (2018).

*Matrix Capsules with EM Routing*. International Conference on Learning Representations (ICLR).[https://openreview.net/forum?id=HJWLfGWRb](https://openreview.net/forum?id=HJWLfGWRb)LaLonde, R., & Bagci, U. (2018).

*Capsules for Object Segmentation*. (SegCaps).[https://arxiv.org/abs/1804.04241](https://arxiv.org/abs/1804.04241)Simpson, A. L., Antonelli, M., Bakas, S., et al. (2019).

*A Large Annotated Medical Image Dataset for the Development and Evaluation of Segmentation Algorithms*. (Medical Segmentation Decathlon).[http://medicaldecathlon.com/](http://medicaldecathlon.com/)/[https://arxiv.org/abs/1902.09063](https://arxiv.org/abs/1902.09063)Çiçek, Ö., Abdulkadir, A., Lienkamp, S. S., Brox, T., & Ronneberger, O. (2016).

*3D U-Net: Learning Dense Volumetric Segmentation from Sparse Annotation*. Medical Image Computing and Computer-Assisted Intervention (MICCAI).[https://arxiv.org/abs/1606.06650](https://arxiv.org/abs/1606.06650)Lux.jl: A deep learning library for Julia.

[https://github.com/JuliaAI/Lux.jl](https://github.com/JuliaAI/Lux.jl)MedPipe3D.jl: A modular 3D medical imaging pipeline in Julia.

[https://github.com/JuliaHealth/MedPipe3D.jl](https://github.com/JuliaHealth/MedPipe3D.jl)KernelAbstractions.jl: A vendor-neutral GPU programming model for Julia.

[https://github.com/JuliaGPU/KernelAbstractions.jl](https://github.com/JuliaGPU/KernelAbstractions.jl)

MedPipe3D was created to improve integration between other parts of the small ecosystem (MedEye3D, MedEval3D, and MedImage). Currently, it needs to be expanded and adapted to serve as the basis for a fully functional medical imaging pipeline.

**Mentor:** Jakub Mitura [email: jakub.mitura14@gmail.com]

**Difficulty:** Hard **Duration:** 12 weeks

Strong knowledge of the Julia programming language is required.

Experience with the following Julia packages is highly desirable:

MedPipe3D.jl

MedEye3D.jl

MedEval3D.jl

MedImage.jl


Familiarity with the following packages would be a valuable asset:

Lux.jl

TensorBoard

Logging.jl



Implement comprehensive logging with TensorBoard Integration and Error and Warning Logs with Logging.jl for better tracking and debugging.

Improve the performance of augmentations.

Enable per-layer memory usage inspection of Lux models.

Enable gradient checkpointing of chosen layers to save memory.

Support loading tabular data (e.g., clinical data) together with the image into the supplied model.

Enhance documentation with in-depth tutorial, code examples, and a refined README for easy onboarding.


This set of changes, although time-consuming to implement, should not pose a significant issue to anyone with experience with the Julia programming language. Each feature will be implemented using existing Julia libraries and frameworks where possible. However, implementing these changes will be a huge step in making the Julia language a good alternative to Python for developing end-to-end medical imaging segmentation algorithms.

**Logging:**Implement logging to track the progress and debug issues - 2 weeks.**Performance Improvements:**Optimize the performance of augmentations to ensure efficient processing - 2 weeks.**Memory Usage Inspection:**Enable per-layer memory usage inspection of Lux models to monitor and optimize memory consumption - 2 weeks.**Gradient Checkpointing:**Enable gradient checkpointing of chosen layers to save memory during training - 4 weeks.**Tabular Data Support:**Support loading tabular data (e.g., clinical data) together with the image into the supplied model - 1 week.**Documentation:**Improve documentation to provide clear instructions and examples for users - 1 week.

**Total estimated time:** 12 weeks.

Implementing these features is crucial for advancing medical imaging technology. Enhanced logging with TensorBoard integration will allow for better insight into model training. Performance improvements ensure reliable and efficient processing of large datasets. Improved documentation and memory management make the tools more accessible and usable for medical professionals, facilitating better integration into clinical workflows. Supporting tabular data alongside imaging allows for comprehensive analysis, combining clinical and imaging data to improve diagnostic accuracy and patient outcomes.

For each point, the mentor will also supply the person responsible for implementation with examples of required functionalities in Python or will point to the Julia libraries already implementing it (that just need to be integrated).

[JuliaReach](https://github.com/JuliaReach) is the Julia ecosystem for reachability computations of dynamical systems. Application domains of set-based reachability include formal verification, controller synthesis and estimation under uncertain model parameters or inputs. For further context reach us on the [JuliaReach zulip](https://julialang.zulipchat.com/#narrow/stream/278609-juliareach) stream. You may also refer to the review article [Set Propagation Techniques for Reachability Analysis](https://www.annualreviews.org/doi/abs/10.1146/annurev-control-071420-081941).

**Difficulty**: Medium.

**Description.** [ReachabilityAnalysis](https://github.com/JuliaReach/ReachabilityAnalysis.jl) is a Julia library for set propagation of dynamical systems. This project aims at integrating ReachabilityAnalysis with the numerical modeling ecosystem in Julia.

**Expected Results.** The proposal is to let the user specify models defined in [ModelingToolkit.jl](https://github.com/SciML/ModelingToolkit.jl) from the [SciML](https://github.com/sciml) ecosystem, and solve them using reachability methods. This first iteration would cover purely continuous systems; a second iteration would cover systems with discrete transitions (hybrid systems).

**Expected Length.** 175 hours.

**Recommended Skills.** Familiarity with Julia and Git/GitHub is mandatory. Familiarity with [LazySets](https://github.com/JuliaReach/LazySets.jl) and [ReachabilityAnalysis](https://github.com/JuliaReach/ReachabilityAnalysis.jl) is welcome but not required.

**Mentors**: [Marcelo Forets](https://github.com/mforets), [Christian Schilling](https://github.com/schillic).

**Difficulty**: Medium.

**Description.** [LazySets](https://github.com/JuliaReach/LazySets.jl) is the core library of JuliaReach. It provides ways to symbolically compute with geometric sets, with a focus on lazy set representations and efficient high-dimensional processing. The library has been described in the article [LazySets.jl: Scalable Symbolic-Numeric Set Computations](https://proceedings.juliacon.org/papers/10.21105/jcon.00097).

The main interest in this project is to implement algorithms that leverage the structure of the sets. Typical examples include polytopes and zonotopes (convex), polynomial zonotopes and Taylor models (non-convex) to name a few.

**Expected Results.** The goal is to implement certain efficient state-of-the-art algorithms from the literature. The code is to be documented, tested, and evaluated in benchmarks. Specific tasks may include (to be driven by the interets of the candidate): efficient vertex enumeration of [zonotopes](https://juliareach.github.io/LazySets.jl/dev/lib/sets/Zonotope/#LazySets.Zonotope); operations on polynomial zonotopes; operations on [zonotope bundles](http://archive.www6.in.tum.de/www6/Main/Publications/Althoff2011f.pdf); efficient disjointness checks between different set types; [complex zonotopes](https://ieeexplore.ieee.org/document/7525593).

**Expected Length.** 175 hours.

**Recommended Skills.** Familiarity with Julia and Git/GitHub is mandatory. Familiarity with [LazySets](https://github.com/JuliaReach/LazySets.jl) is recommended. Basic knowledge of geometric terminology is appreciated but not required.

**Mentors**: [Marcelo Forets](https://github.com/mforets), [Christian Schilling](https://github.com/schillic).

**Difficulty**: Medium.

**Description.** [ReachabilityAnalysis](https://github.com/JuliaReach/ReachabilityAnalysis.jl) is a Julia library for set propagation of dynamical systems. One of the main aims is to handle systems with mixed discrete-continuous behaviors (known as hybrid systems in the literature). This project will focus on enhancing the capabilities of the library and overall improvement of the ecosystem for users.

**Expected Results.** Specific tasks may include: problem-specific heuristics for hybrid systems; API for time-varying input sets; flowpipe underapproximations. The code is to be documented, tested, and evaluated in benchmarks. Integration with [ModelingToolkit.jl](https://github.com/SciML/ModelingToolkit.jl) can also be considered if there is interest.

**Expected Length.** 175 hours.

**Recommended Skills.** Familiarity with Julia and Git/GitHub is mandatory. Familiarity with [LazySets](https://github.com/JuliaReach/LazySets.jl) and [ReachabilityAnalysis](https://github.com/JuliaReach/ReachabilityAnalysis.jl) is welcome but not required.

**Mentors**: [Marcelo Forets](https://github.com/mforets), [Christian Schilling](https://github.com/schillic).

**Note: FluxML participates as a NumFOCUS sub-organization. Head to the FluxML GSoC page for their idea list.**

Time: 175h

Develop a series of reinforcement learning environments, in the spirit of the [OpenAI Gym](https://gym.openai.com). Although we have wrappers for the gym available, it is hard to install (due to the Python dependency) and, since it's written in Python and C code, we can't do more interesting things with it (such as differentiate through the environments).

A pure-Julia version of selected environments that supports a similar API and visualisation options would be valuable to anyone doing RL with Flux.

Mentors: [Dhairya Gandhi](https://github.com/DhairyaLGandhi/).

Much of science can be explained by the movement and interaction of molecules. Molecular dynamics (MD) is a computational technique used to explore these phenomena, from noble gases to biological macromolecules. [Molly.jl](https://github.com/JuliaMolSim/Molly.jl) is a pure Julia package for MD, and for the simulation of physical systems more broadly. The package is currently under development with a focus on proteins and differentiable molecular simulation. There are a number of ways that the package could be improved:

**Machine learning potentials (duration: 175h, expected difficulty: easy to medium):**in the last few years machine learning potentials have been improved significantly. Models such as ANI, ACE, NequIP and Allegro can be added to Molly.**Alchemical simulation features (duration: 175h, expected difficulty: medium):**binding free energy methods are now used routinely in drug discovery. Appropriate potentials and protocols could be added to Molly based on software like OpenFE.**Reactant compatibility (duration: 175h, expected difficulty: medium to hard):**Reactant.jl allows improved performance and Enzyme support. Molly could be made compatible with Reactant to access these features.

**Recommended skills:** familiarity with computational chemistry, structural bioinformatics or simulating physical systems.

**Expected results:** new features added to the package along with tests and relevant documentation.

**Mentor:** [Joe Greener](https://github.com/jgreener64)

**Contact:** feel free to ask questions via [email](http://jgreener64.github.io) or #juliamolsim on the [Julia Slack](https://join.slack.com/t/julialang/shared_invite/zt-2a5wdtotu-H52pQQTMDOa4NwsTSgQ_lQ).

Clifford circuits are a class of quantum circuits that can be simulated efficiently on a classical computer. As such, they do not provide the computational advantage expected of universal quantum computers. Nonetheless, they are extremely important, as they underpin most techniques for quantum error correction and quantum networking. Software that efficiently simulates such circuits, at the scale of thousands or more qubits, is essential to the design of quantum hardware. The [QuantumClifford.jl](https://github.com/Krastanov/QuantumClifford.jl) Julia project enables such simulations.

Simulation of Clifford circuits involves significant amounts of linear algebra with boolean matrices. This enables the use of many standard computation accelerators like GPUs, as long as these accelerators support bit-wise operations. The main complications is that the elements of the matrices under consideration are usually packed in order to increase performance and lower memory usage, i.e. a vector of 64 elements would be stored as a single 64 bit integer instead of as an array of 64 bools. A Summer of Code project could consist of implement the aforementioned linear algebra operations in GPU kernels, and then seamlessly integrating them in the rest of the QuantumClifford library. At a minimum that would include [Pauli-Pauli products](https://github.com/Krastanov/QuantumClifford.jl/blob/v0.4.0/src/QuantumClifford.jl#L725) and certain [small Clifford operators](https://github.com/Krastanov/QuantumClifford.jl/blob/v0.4.0/src/symbolic_cliffords.jl), but could extend to general [stabilizer tableau multiplication](https://github.com/Krastanov/QuantumClifford.jl/blob/v0.4.0/src/QuantumClifford.jl#L1385) and even [tableau diagonalization](https://github.com/Krastanov/QuantumClifford.jl/blob/v0.4.0/src/QuantumClifford.jl#L985). Some of these features are already implemented, but significant polish and further improvements and implementation of missing features is needed.

**Recommended skills:** Basic knowledge of the [stabilizer formalism](https://krastanov.github.io/QuantumClifford.jl/dev/references/) used for simulating Clifford circuits. Familiarity with performance profiling tools in Julia and Julia's GPU stack, including [KernelAbstractions](https://github.com/JuliaGPU/KernelAbstractions.jl) and [Tullio](https://github.com/mcabbott/Tullio.jl).

**Mentors:** [Stefan Krastanov](https://github.com/Krastanov) [<stefan@krastanov.org>](mailto:stefan@krastanov.org) and QuantumClifford.jl team members

**Expected duration:** 175 hours (but applicants can scope it to a longer project by including work on GPU-accelerated Gaussian elimination used in the canonicalization routines)

**Difficulty:** Medium if the applicant is familiar with Julia, even without understanding of Quantum Information Science (but applicants can scope it to "hard" by including the aforementioned additional topics)

Quantum Error Correcting codes are typically represented in a form similar to the parity check matrix of a classical code. This form is referred to as a Stabilizer tableaux. This project would involve creating a comprehensive library of frequently used quantum error correcting codes and/or implementing syndrome-decoding algorithms for such codes. The library already includes some simple codes and interfaces to a few decoders – adding another small code or providing a small documentation pull request could be a good way to prove competence when applying for this project. The project can be extended to a much longer one if work on decoders is included. A large part of this project would involve literature surveys. Some suggestions for codes to include: color codes, higher-dimensional topological codes, hyper graph product codes, twists in codes, newer LDPC codes, honeycomb codes, Floquet codes. Some suggestions for decoders to work on: iterative, small-set flip, ordered statistical decoding, belief propagation, neural belief propagation.

**Recommended skills:** Knowledge of the [stabilizer formalism](https://krastanov.github.io/QuantumClifford.jl/dev/references/) used for simulating Clifford circuits. Familiarity with tools like python's `ldpc`

, `pymatching`

, and `stim`

can help. Consider checking out the `PyQDecoders.jl`

julia wrapper package as well.

**Mentors:** [Stefan Krastanov](https://github.com/Krastanov) [<stefan@krastanov.org>](mailto:stefan@krastanov.org) and QuantumClifford.jl team members

**Expected duration:** 175 hours (but applicants can scope it as longer, depending on the list of functionality they plan to implement)

**Difficulty:** Medium. Easy with some basic knowledge of quantum error correction

Applying an n-qubit Clifford gate to an n-qubit state (tableaux) is an operation similar to matrix multiplication, requiring O(n^3) steps. However, applying a single-qubit or two-qubit gate to an n-qubit tableaux is much faster as it needs to address only one or two columns of the tableaux. This project would focus on extending the left-multiplication special cases already started in [symbolic_cliffords.jl](https://github.com/Krastanov/QuantumClifford.jl/blob/master/src/symbolic_cliffords.jl) and creating additional right-multiplication special cases (for which [the Stim library is a good reference](https://github.com/Krastanov/QuantumClifford.jl/commit/d3e84c16b7b08ef6f1bc24e2bcf98641c2fff1ab#r67183201)).

**Recommended skills:** Knowledge of the [stabilizer formalism](https://krastanov.github.io/QuantumClifford.jl/dev/references/) used for simulating Clifford circuits. Familiarity with performance profiling tools in Julia. Understanding of C/C++ if you plan to use the Stim library as a reference.

**Mentors:** [Stefan Krastanov](https://github.com/Krastanov) [<stefan@krastanov.org>](mailto:stefan@krastanov.org) and QuantumClifford.jl team members

**Expected duration:** 175 hours (but applicants can scope it as longer if they plan for other significant optimization and API design work)

**Difficulty:** Easy

The QuantumClifford library already has some [support for generating different types of circuits related to error correction](https://github.com/QuantumSavory/QuantumClifford.jl/blob/v0.8.19/src/ecc/circuits.jl) (mostly in terms of syndrome measurement circuits like Shor's) and for evaluating the quality of error correcting codes and decoders. Significant improvement can be made by implementing more modern compilation schemes, especially ones relying on flag qubits.

**Recommended skills:** Knowledge of the variety of flag qubit methods. Some useful references could be [a](https://link.aps.org/accepted/10.1103/PhysRevLett.121.050502), [b](https://www.nature.com/articles/s41534-018-0085-z), [c](https://journals.aps.org/prxquantum/pdf/10.1103/PRXQuantum.1.010302), and this [video lecture](https://www.youtube.com/watch?v=etA9l2NUCXI).

**Mentors:** [Stefan Krastanov](https://github.com/Krastanov) [<stefan@krastanov.org>](mailto:stefan@krastanov.org) and QuantumClifford.jl team members

**Expected duration:** 175 hours (but applicants can scope it as longer if they plan more extensive work)

**Difficulty:** Hard

The MBQC model of quantum computation has a lot of overlap with the study of Stabilizer states. This project would be about the creation of an MBQC compiler and potentially simulator in Julia. E.g. if one is given an arbitrary graph state and a circuit, how is this circuit to be compiled in an MBQC model.

**Recommended skills:** Knowledge of the MBQC model of quantum computation. This [paper and the related python library](https://arxiv.org/pdf/2212.11975.pdf) can be a useful reference. Consider also [this reference](https://quantum-journal.org/papers/q-2021-03-25-421/).

**Mentors:** [Stefan Krastanov](https://github.com/Krastanov) [<stefan@krastanov.org>](mailto:stefan@krastanov.org) and QuantumClifford.jl team members

**Expected duration:** 175 hours (but applicants can scope it as longer if they plan more extensive work)

**Difficulty:** Hard

The graph states formalism is a way to work more efficiently with stabilizer states that have a sparse tableaux. This project would involve creation of the necessary gate simulation algorithms and conversions tools between graph formalism and stabilizer formalism (some of which are [already available in the library](https://github.com/QuantumSavory/QuantumClifford.jl/blob/master/src/graphs.jl)).

**Recommended skills:** Understanding of the graph formalism. This [paper can be a useful reference](https://arxiv.org/abs/quant-ph/0504117).

**Mentors:** [Stefan Krastanov](https://github.com/Krastanov) [<stefan@krastanov.org>](mailto:stefan@krastanov.org) and QuantumClifford.jl team members

**Expected duration:** 175 hours (but applicants can scope it as longer if they plan more extensive work)

**Difficulty:** Medium

There are various techniques used to augment Clifford circuit simulators to model circuits that are only "mostly" Clifford. Particularly famous are the Clifford+T gate simulators. This project is about implementing such extensions.

**Recommended skills:** In-depth understanding of the Stabilizer formalism, and understanding of some of the extensions to that method. We have some [initial implementations](https://github.com/QuantumSavory/QuantumClifford.jl/blob/master/src/nonclifford.jl). This [IBM paper](https://arxiv.org/pdf/1808.00128.pdf) can also be a useful reference for other methods.

**Mentors:** [Stefan Krastanov](https://github.com/Krastanov) [<stefan@krastanov.org>](mailto:stefan@krastanov.org) and QuantumClifford.jl team members

**Expected duration:** 175 hours (but applicants can scope it as longer if they plan more extensive work)

**Difficulty:** Hard

Magic states are important non-stabilizer states that can be used for inducing non-Clifford gates in otherwise Clifford circuits. They are crucial for the creation of error-corrected universal circuits. This project would involve contributing tools for the analysis of such states and for the evaluation of distillation circuits and ECC circuits involving such states.

**Recommended skills:** In-depth understanding of the theory of magic states and their use in fault tolerance.

**Mentors:** [Stefan Krastanov](https://github.com/Krastanov) [<stefan@krastanov.org>](mailto:stefan@krastanov.org) and QuantumClifford.jl team members

**Expected duration:** 175 hours (but applicants can scope it as longer if they plan more extensive work)

**Difficulty:** Hard

The most common way to represent and model quantum states is the state vector formalism (underlying Schroedinger's and Heisenberg's equations as well as many other master equations). The [QuantumOptics.jl](https://github.com/qojulia/QuantumOptics.jl) Julia project enables such simulations, utilizing much of the uniquely powerful DiffEq infrastructure in Julia.

Much of the internal representation of quantum states in QuantumOptics.jl relies on standard dense arrays. Thanks to the multiple-dispatch nature of Julia, much of these objects can already work well with GPU arrays. This project would involve a thorough investigation and validation of the current interfaces to make sure they work well with GPU arrays. In particular, attention will have to be paid to the "lazy" operators as special kernels might need to be implemented for them.

**Recommended skills:** Familiarity with performance profiling tools in Julia and Julia's GPU stack, potentially including [KernelAbstractions](https://github.com/JuliaGPU/KernelAbstractions.jl).

**Mentors:** [Stefan Krastanov](https://github.com/Krastanov) [<stefan@krastanov.org>](mailto:stefan@krastanov.org) and QuantumOptics.jl team members

**Expected duration:** 175 hours (but applicants can scope it as longer if they plan more extensive work)

**Difficulty:** Medium

Autodifferentiation is the capability of automatically generating efficient code to evaluate the numerical derivative of a given Julia function. Similarly to the GPU case above, much of this functionality already "magically" works, but there is no detailed test suite for it and no validation has been done. This project would involve implementing, validating, and testing the use of Julia autodiff tools in QuantumOptics.jl. ForwardDiff, Enzyme, Zygote, Diffractor, and AbstractDifferentiation are all tools that should have some level of validation and support, both in ODE solving and in simple operator applications.

**Recommended skills:** Familiarity with the [Julia autodiff stack](https://juliadiff.org/) and the SciML sensitivity analysis tooling. Familiarity with the difficulties to autodiff complex numbers (in general and specifically in Julia). Understanding of the AbstractDifferentiation.jl package.

**Mentors:** [Stefan Krastanov](https://github.com/Krastanov) [<stefan@krastanov.org>](mailto:stefan@krastanov.org) and QuantumOptics.jl team members

**Expected duration:** 175 hours (but applicants can scope it as longer if they plan more extensive work)

**Difficulty:** Easy-to-Medium

SciML is the umbrella organization for much of the base numerical software development in the Julia ecosystem. We already use many of their capabilities, but it would be beneficial to more closely match the interfaces they expect. This project would be heavily on the software **engineering** side. Formal and informal interfaces we want to support include: better support for [DiffEq problem types](https://github.com/qojulia/QuantumOptics.jl/issues/298) (currently we wrap DiffEq problems in our own infrastructure and it is difficult to reuse them in SciML); better support for broadcast operations over state objects (so that we can treat them closer to normal arrays and [we can simply provide an initial state to a DiffEq solver without having to wrap/unwrap the data](https://github.com/qojulia/QuantumOpticsBase.jl/pull/16)); relying more heavily on [SciMLOperators](https://docs.sciml.ai/SciMLOperators/stable/) which have significant [overlap with our lazy operators](https://github.com/qojulia/QuantumOpticsBase.jl/issues/99).

**Recommended skills:** Familiarity with the SciML stack.

**Mentors:** [Stefan Krastanov](https://github.com/Krastanov) [<stefan@krastanov.org>](mailto:stefan@krastanov.org) and QuantumOptics.jl team members

**Expected duration:** 175 hours (but applicants can scope it as longer if they plan more extensive work)

**Difficulty:** Easy

[Rimu.jl](https://github.com/RimuQMC/Rimu.jl) is a Julia package for finding ground states (and low-lying excited states) of quantum many-body problems with projector quantum Monte Carlo (using a flavour called full configuration interaction quantum Monte Carlo, FCIQMC) and with exact diagonalisation.

**Difficulty**: Easy to medium (if the recommended skills are available)

**Project size**: 175 - 350 hours

**Problem**: [Rimu.jl](https://github.com/RimuQMC/Rimu.jl) provides an interface for defining a custom quantum many-body Hamiltonian and currently implements a selection of model Hamiltonians (e.g. variants of the Hubbard model and the Fröhlich polaron model). The high-level goal of the project is to implement the required functionality to solve ab-initio quantum chemistry problems with [Rimu.jl](https://github.com/RimuQMC/Rimu.jl) and embed the package into the [JuliaMolSim](https://github.com/JuliaMolSim) ecosystem, in particular with [ElemCo.jl](https://github.com/fkfest/ElemCo.jl).

**Minimum goal**: A minimum goal would be to enable reading in the relevant information about the molecular orbital basis set and integrals that define the molecular Hamiltonian from a file (in the standard FCIDUMP format) and defining an appropriate Hamiltonian type for Rimu.jl that enables its usage for exact diagonalisation and FCIQMC.

**Extended goal**: An extended goal would be to make the molecular Hamiltonian efficient for FCIQMC, e.g. by finding and implementing an appropriate strategy for an excitation generator, e.g. a variant of (precomputed) heat-bath sampling. Another worthwhile extension would be to implement variants of the Configuration Interaction (CI) method by filtering the configurations to a relevant subspace (e.g. CI-SD, selctive CI, etc.) for the exact-diagonalisation part of Rimu.jl.

**Recommended skills**:

prior exposure to or strong interest in quantum chemistry

good to excellent Julia coding skills


**Mentors**: [Joachim Brand](https://github.com/joachimbrand), [Daniel Kats](https://github.com/dnkats), [Elke Pahl](https://github.com/ElkePahl)

If you are interested please get in touch by [email](mailto:j.brand@massey.ac.nz).

**Difficulty**: Medium to hard

**Project size**: 175 - 350 hours

**Problem**: [Rimu.jl](https://github.com/RimuQMC/Rimu.jl) parallelises the workload of FCIQMC by making extensive use of native threading for shared-memory parallelism. In high-performance computing environments the primary data structure containing information about the sampled configurations and their amplitudes can further be distributed across nodes, which communicate using the MPI protocol in every time step (making use of [MPI.jl](https://github.com/JuliaParallel/MPI.jl)). In the current implementation the distribution of configurations to nodes is done passively (in a pseudo-random fashion using a hashing algorithm). While this is fast and easy and usually leads to a fairly even distribution of data and work across the nodes, it does not scale very well when employing hundreds of nodes as every MPI rank has to wait for the slowest one to complete the work done at each time step.

**Minimum goal**: Implement an active load-balancing approach where load information of each MPI rank is monitored and work load is shifted between nodes to even out the workload.

**Extended goal**: Explore other load-balancing strategies like agent-based approaches, possibly even exploring algorithmic alternatives (e.g. continuous-time Monte Carlo). Design communication protocols that take into account the network topology.

**Recommended skills**:

experience with HPC environments and MPI-style programming

good to excellent Julia coding skills


**Mentors**: [Matija Čufar](https://github.com/mtsch), [Joachim Brand](https://github.com/joachimbrand)

If you are interested please get in touch with [Matija](mailto:matijacufar@gmail.com) or [Joachim](mailto:j.brand@massey.ac.nz).

Extending Satisfiability.jl with more SMT-LIB theories and expanded capabilities.

**Time Commitment:** 175h **Difficulty:** Medium

Satisfiability modulo theories (SMT) is a powerful logic programming tool used (among other things) to formally verify programs and hardware for correctness and security. Currently, most solvers (that follow the SMT-LIB standard) require input to be specified in the SMT-LIB specification language, which is not really human-readable.

[🔗 Satisfiability.jl](https://elsoroka.github.io/Satisfiability.jl/dev/) s a high-level interface that allows users to specify complex SMT formulas in pure, idiomatic Julia, and directly interfaces with solvers (e.g. Z3 or CVC5). Satisfiability.jl is **not** a solver; it is an interface to SMT solvers in the same sense that Convex.jl and Jump.jl are interfaces to numerical-optimization solvers. No experience with SMT solving algorithms is required for this project.

This project aims to extend Satisfiability.jl, a Julia package that provides an native, direct interface to SMT (Satisfiability Modulo Theories) solvers via the SMT-LIB specification language. Currently, Satisfiability.jl supports only three theories, and this project will implement one major additional theory (Arrays, Floating-point Numbers, or Strings) to bring the package closer to supporting all SMT-LIB theories.

This work will enhance the Julia ecosystem for formal verification and constraint satisfaction, allowing researchers and developers to interact with SMT solvers directly in pure

Approach

Consult the SMT-LIB standard to design a clean, idiomatic Julia API

Implement the selected theory with appropriate Julia types and operators

Create comprehensive tests to ensure correctness and usability

Write thorough documentation and examples to help users understand the new functionality


Main goals

A fully implemented SMT-LIB theory with 100% test coverage

Documentation and examples demonstrating usage

An API design that feels natural in Julia and consistent with the package


Stretch goals

Implementing a second theory

Automated logic detection

Improved parser for SMT solver output

Performance benchmarking


**Skills:** Familiarity with automated reasoning/formal verification software such as Z3 or CVC5. Ideally, familiarity with the SMT-LIB language but this can be learned!

**Expected results:** new features added to the package along with tests, documentation, and a few examples demonstrating new features.

**Mentors:** [Emi Soroka](https://github.com/elsoroka/) and [Romeo Valentin](https://page.romeov.me/).

**Contact:** ping either mentor on the Julia slack.

The goal of this project is to develop a new language server for Julia, currently called [JETLS](https://github.com/aviatesk/JETLS.jl), that enhances developer productivity through advanced static analysis and seamless integration with the Julia runtime.

JETLS has made significant progress and now implements a broad set of core LSP features. Type-sensitive diagnostics are powered by [JET.jl](https://github.com/aviatesk/JET.jl), which uses [JuliaInterpreter.jl](https://github.com/JuliaDebug/JuliaInterpreter.jl) to load and analyze code. Features like code completion, workspace symbols, find references, and rename are built by running [JuliaLowering.jl](https://github.com/JuliaLang/julia/tree/master/JuliaLowering) as a post-analysis step on top of the module context that JET/JuliaInterpreter has established.

The next major milestone is to feed JuliaLowering-generated code directly into JET's analysis, rather than running JuliaLowering as a post-processing step. This deeper integration, combined with [Revise.jl](https://github.com/timholy/Revise.jl) for incremental analysis, will enable advanced features such as type-on-hover, inlay type hints, and argument-type-aware completions, as well as more precise diagnostic locations (currently reported at line granularity rather than column-precise positions).

During GSoC, we expect the contributor to work on these deeper integrations and implement the advanced language features that depend on them. As preparation, we hope that by the time GSoC starts, you have studied the implementations of JETLS.jl and related tools: [JET.jl](https://github.com/aviatesk/JET.jl), [JuliaInterpreter.jl](https://github.com/JuliaDebug/JuliaInterpreter.jl), [Revise.jl](https://github.com/timholy/Revise.jl), and [JuliaLowering.jl](https://github.com/JuliaLang/julia/tree/master/JuliaLowering).

**Expected Outcomes**: Advanced language server features built on top of full JuliaLowering/JET/Revise integration, such as type-on-hover, inlay type hints, and argument-type-aware completions.**Skills Required**:Proficiency in Julia programming and familiarity with its compiler and runtime systems

Deep understanding of Julia's compiler internals, including lowering, type inference, and abstract interpretation as implemented in JET.jl, JuliaInterpreter.jl, and JuliaLowering.jl

Interest in and/or experience with LSP and developer tooling


**Difficulty**: Hard**Contact**:[Shuhei Kadowaki](https://github.com/aviatesk)

[TopOpt.jl](https://github.com/JuliaTopOpt/TopOpt.jl) is a [topology optimization](https://en.wikipedia.org/wiki/Topology_optimization) package written in pure Julia. Topology optimization is an exciting field at the intersection of shape representation, physics simulations and mathematical optimization, and the Julia language is a great fit for this field. To learn more about `TopOpt.jl`

, check the following [JuliaCon talk](https://www.youtube.com/watch?v=sBqdkxPXluU).

The following is a tentative list of projects in topology optimization that you could be working on in the coming Julia Season of Contributions or Google Summer of Code. If you are interested in exploring any of these topics or if you have other interests related to topology optimization, please reach out to the main mentor [Mohamed Tarek](https://github.com/mohamed82008) via email.

**Project difficulty**: Medium

**Work load**: 350 hours

**Description**: The goal of this project is to improve the unit test coverage and reliability of TopOpt.jl by testing its implementations against other software's outputs. Testing and benchmarking stress and buckling constraints and their derivatives will be the main focus of this project. Matlab scripts from papers may have to be translated to Julia for correctness and performance comparison.

**Knowledge prerequisites**: structural mechanics, optimization, Julia programming

**Project difficulty**: Medium

**Work load**: 350 hours

**Description**: There are numerous ways to use machine learning for design optimization in topology optimization. The following are all recent papers with applications of neural networks and machine learning in topology optimization. There are also exciting research opportunities in this direction.

[DNN-based Topology optimization: Spatial Invariance and Neural Tangent Kernel](https://openreview.net/pdf?id=DUy-qLzqvlU)[NTopo: Mesh-free Topology Optimization using Implicit Neural Representations](https://openreview.net/pdf?id=bBHHU4dW88g)[TONR: An exploration for a novel way combining neural network with topology optimization](https://www.sciencedirect.com/science/article/pii/S004578252100414X?via%3Dihub)

In this project you will implement one of the algorithms discussed in any of these papers.

**Knowledge prerequisites**: neural networks, optimization, Julia programming

**Project difficulty**: Medium

**Work load**: 350 hours

**Description**: Currently in TopOpt.jl, there are only unstructured meshes supported. This is a very flexible type of mesh but it's not as memory efficient as uniform rectilinear grids where all the elements are assumed to have the same shape. This is the most common grid used in topology optimization in practice. Currently in TopOpt.jl, the uniform rectilinear grid will be stored as an unstructured mesh which is unnecessarily inefficient. In this project, you will optimize the finite element analysis and topology optimization codes in TopOpt.jl for uniform rectilinear grids.

**Knowledge prerequisites**: knowledge of mesh types, Julia programming

**Project difficulty**: Medium

**Work load**: 350 hours

**Description**: Topology optimization problems with more mesh elements take longer to simulate and to optimize. In this project, you will explore the use of adaptive mesh refinement starting from a coarse mesh, optimizing and only refining the elements that need further optimization. This is an effective way to accelerate topology optimization algorithms.

**Knowledge prerequisites**: adaptive mesh refinement, Julia programming

**Project difficulty**: Medium

**Work load**: 175 or 350 hours

**Description**: All of the examples in TopOpt.jl and problem types are currently of the linear elasticity, quasi-static class of problems. The goal of this project is to implement more problem types and examples from the field of heat transfer. Both steady-state heat transfer problems and linear elasticity problems make use of elliptic partial differential equations so the code from linear elasticity problems should be largely reusable for heat transfer problems with minimum changes.

**Knowledge prerequisites**: finite element analysis, heat equation, Julia programming

[Trixi.jl](https://github.com/trixi-framework/Trixi.jl/) is a Julia package for adaptive high-order numerical simulations of conservation laws. It is designed to be simple to use for students and researchers, extensible for research and teaching, as well as efficient and suitable for high-performance computing.

**Difficulty**: Medium

**Project size**: 175 hours or 350 hours, depending on the chosen subtasks

Visualizing and documenting results is a crucial part of the scientific process. In [Trixi.jl](https://github.com/trixi-framework/Trixi.jl/), we rely for visualization on a combination of pure Julia packages (such as [Plots.jl](https://github.com/JuliaPlots/Plots.jl) and [Makie.jl](https://github.com/MakieOrg/Makie.jl)) and the open-source scientific visualization suite [ParaView](https://www.paraview.org). While the Julia solutions are excellent for visualizing 1D and 2D data, ParaView is the first choice for creating publication-quality figures from 3D data.

Currently, visualization with ParaView is only possible after a simulation is finished and requires an additional postprocessing step, where the native output files of Trixi.jl are converted to [VTK](https://vtk.org) files using [Trixi2Vtk.jl](https://github.com/trixi-framework/Trixi2Vtk.jl). This extra step makes it somewhat inconvenient to use, especially when the current state of a numerical solution is to be checked during a long, multi-hour simulation run.

The goal of this project is therefore to make such visualizations easier by introducing two significant improvements:

Add the capability to write out native

[VTKHDF](https://docs.vtk.org/en/latest/design_documents/VTKFileFormats.html#vtkhdf-file-format)files directly during a simulation, in serial and parallel.Enable parallel in-situ visualization of the results, i.e., to visualize results by connecting ParaView to a currently running, parallel Trixi.jl simulation using the

[Catalyst API](https://catalyst-in-situ.readthedocs.io/en/latest/index.html).

Both tasks are related in that they require the student to familiarize themselves with both the data formats internally used in Trixi.jl as well as the visualization pipelines of VTK/ParaView. However, they can be performed independently and thus this project is suitable for either a 175 hour or a 350 hour commitment, depending on whether one or both tasks are to be tackled.

This project is good for both software engineers interested in the fields of visualization and scientific data analysis as well as those students who are interested in pursuing graduate research in the field of numerical analysis and high-performance computing.

**Recommended skills**: Some knowledge of at least one numerical discretization scheme (e.g., finite volume, discontinuous Galerkin, finite differences) is helpful; initial knowledge about visualization or parallel processing; preferably the ability (or eagerness to learn) to write fast code.

**Expected results**: Scalable, production quality visualization of scientific results for Trixi.jl.

**Mentors**: [Michael Schlottke-Lakemper](https://github.com/sloede), [Benedict Geihe](https://www.mi.uni-koeln.de/NumSim/dr-benedict-geihe/), [Johannes Markert](https://github.com/jmark)

**Difficulty**: Medium

**Project size**: 175 hours or 350 hours, depending on the chosen subtasks

The high performance of modern scientific software is built on parallel computing using MPI and GPUs. The communication speed has not kept up with the exponential increase in compute speed and algorithms are often communication bound, leading to underutilization of hardware capabilities. Asynchronous computing avoids communication bottlenecks by performing non-blocking sends and using algorithms that can give reliable results using the currently available data. This approach gives great scalability on parallel computing systems.

[Trixi.jl](https://github.com/trixi-framework/Trixi.jl/) currently performs distributed memory parallelization using [MPI.jl](https://github.com/JuliaParallel/MPI.jl), and has experimental GPU capabilities using [CUDA.jl](https://github.com/JuliaGPU/CUDA.jl) and [KernelAbstractions.jl](https://github.com/JuliaGPU/KernelAbstractions.jl). The goal of this project is to implement a subset of features of [Trixi.jl](https://github.com/trixi-framework/Trixi.jl/) that can perform parallel simulations asynchronously.

The possible subtasks in this project include:

Explore and implement a simple code for asynchronous algorithms for solving the 1D advection equation or 1D compressible Euler equations using the API of

[Trixi.jl](https://github.com/trixi-framework/Trixi.jl/).Taking the simple code as a prototype, explore and implement an asynchronous algorithm starting with the basic

[TreeMesh](https://trixi-framework.github.io/Trixi.jl/stable/meshes/tree_mesh/)type in[Trixi.jl](https://github.com/trixi-framework/Trixi.jl/)and potentially extending up to[P4estMesh](https://trixi-framework.github.io/Trixi.jl/stable/meshes/p4est_mesh/).Explore and implement asynchronous algorithms for a multi-GPU setup, in the 1D prototype and in

[Trixi.jl](https://github.com/trixi-framework/Trixi.jl/).Explore and implement asynchronous algorithms using

[Remote Memory Access Programming using MPI.jl](https://juliaparallel.org/MPI.jl/dev/reference/onesided/).Optimize and compare the performance of the above implementations across different hardwares.


This project is good for both software engineers interested in the fields of scientific computing, machine learning and numerical analysis as well as those students who are interested in pursuing graduate research in the field.

**Recommended skills:** Some knowledge of GPU or MPI programming. Knowledge of any numerical analysis (e.g., finite differences) will help, but is not strictly required.

**Expected results:** Draft of a working subset of the functionality of [Trixi.jl](https://github.com/trixi-framework/Trixi.jl/) efficiently using asynchronous computing.

**Mentors**: [Arpit Babbar](https://github.com/arpit-babbar), [Hendrik Ranocha](https://github.com/ranocha), [Michael Schlottke-Lakemper](https://github.com/sloede)

**Difficulty**: Hard

**Project size**: 175 hours or 350 hours, depending on the chosen subtasks

[Dynamic parallelism](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#cuda-dynamic-parallelism) is designed for applications with either a variation of work across space or a dynamically varying workload over time. It is perfect for tasks like mesh refinement. When a thread discovers that an area needs to be refined, it can launch a new grid to perform computations on the refined area without the overhead of terminating the current grid, reporting to the host, and launching the new grid from the host.

[Adaptive mesh refinement (AMR)](https://trixi-framework.github.io/Trixi.jl/stable/tutorials/adaptive_mesh_refinement/) is applied in [Trixi.jl](https://github.com/trixi-framework/Trixi.jl/) to dynamically refine the mesh during simulations, ensuring finer resolution in critical regions for improved accuracy. Currently, the mesh refinement process is performed on CPUs using parallelism with [MPI.jl](https://github.com/JuliaParallel/MPI.jl). The goal of this project is to migrate AMR to GPUs using dynamic parallelism for acceleration with [CUDA.jl](https://github.com/JuliaGPU/CUDA.jl).

The possible subtasks in this project include:

Implementing the abstract tree initialization process on GPUs.

Exploring the

initialization processes on GPUs based on the implementation of the first task and combining them.`TreeMesh`

Integrating the above into

in the simulation using`AMRCallback`

[dynamic parallelism](https://cuda.juliagpu.org/stable/api/kernel/#Dynamic-parallelism)(via CUDA.jl).Optimizing the code for data transfer, kernel launch overhead, occupancy, etc.

Starting the above work in 1D and then expanding it to 2D and 3D problems.

(Optional) Try similar work for

in 2D and 3D.`P4estMesh`


This project is good for people who are interested in GPU programming, parallel computing, parallel algorithm optimization, and scientific computing.

**Recommended skills:** GPU programming, knowledge of CUDA dynamic parallelism, and familiarity with mesh refinement. (For beginners or those unfamiliar with dynamic parallelism, it is recommended to start with the [CUDA quadtree example](https://github.com/NVIDIA/cuda-samples/tree/master/Samples/3_CUDA_Features/cdpQuadtree).)

**Expected results:** A working example of AMR running on GPUs.

**Mentors**: [Huiyu Xie](https://github.com/huiyuxie), [Jesse Chan](https://github.com/jlchan), [Hendrik Ranocha](https://github.com/ranocha)

[Turing.jl](https://turinglang.org/) is a universal probabilistic programming language embedded in Julia. Turing allows the user to write statistical models in standard Julia syntax, and provides a wide range of sampling-based inference methods for solving problems across probabilistic machine learning, Bayesian statistics, and data science. Since Turing is implemented in pure Julia code, its compiler and inference methods are amenable to hacking: new model families and inference methods can be easily added.

For GSoC 2026 we offer projects from core AD work to scalable inference and user-facing tools.

If a project interests you, contact the mentors listed below or open a discussion on the relevant GitHub repo. Please drop a short introduction message in the [ #turing](https://julialang.slack.com/archives/CCYDC34A0) channel on the

Also cross-posted on [Turing Blog](https://turinglang.org/news/).

| Mentor | Slack Contact |
|---|---|
| Hong Ge |
|

**Mentors**: [Hong Ge](https://github.com/yebai) and [Xianda Sun](https://github.com/sunxd3)

**Project difficulty**: Medium

**Project length**: 350 hrs

Gibbs sampling is one of the most widely used inference strategies in Bayesian computation, but Turing.jl's current Gibbs implementation is tightly coupled to its internals and difficult to extend.

This project is about designing a clean, composable Gibbs sampler built on top of the [AbstractMCMC.jl](https://github.com/TuringLang/AbstractMCMC.jl) interface so that it works perfectly across both Turing.jl and [JuliaBUGS.jl](https://github.com/TuringLang/JuliaBUGS.jl). Work will include:

Agreeing on a minimal AbstractMCMC-compatible interface for conditional samplers.

Implementing the new Gibbs combinator and verifying correctness on standard models.

Migrating existing Turing.jl Gibbs usage to the new interface.

Ensuring JuliaBUGS.jl can plug in its own conditional samplers without modification.


**Mentors**: [Hong Ge](https://github.com/yebai) and [Xianda Sun](https://github.com/sunxd3)

**Project difficulty**: Medium to Hard

**Project length**: 350 hrs

[Mooncake.jl](https://github.com/chalk-lab/Mooncake.jl) is a source-to-source reverse-mode AD package for Julia. Two open issues currently limit its performance and applicability in real-world workloads.

The first is that every hand-written `rrule!!`

must allocate scratch memory on every call ([issue #403](https://github.com/chalk-lab/Mooncake.jl/issues/403)). Derived rules already avoid this by carrying persistent state between calls, but hand-written rules have no such mechanism. The fix is a `StatefulRRule`

struct that holds a `Stack`

of saved state, constructed via a `build_primitive_rrule`

function. Rule authors implement `stateful_rrule!!`

, which receives the current state (or `nothing`

on the first call) and returns updated state alongside the usual outputs – stack push/pop is handled automatically. The work is to (1) add a test that fails when a primal is allocation-free but its `rrule!!`

is not, (2) audit all existing hand-written rules with that test, and (3) convert the offenders.

The second is that Mooncake currently errors on any code using `Threads.@threads`

([issue #570](https://github.com/chalk-lab/Mooncake.jl/issues/570)). Even a race-condition-free primal can produce race conditions on the reverse pass – two threads may concurrently increment the same tangent element, so increments must be atomic. Additionally, rule caches (the stacks inside `OpaqueClosure`

s) must be Task-specific; sharing them across Tasks causes pushes and pops to interleave incorrectly. The work involves writing rules for the `ccall`

s that enter and exit threaded regions, ensuring atomic tangent updates, and making rule caches Task-local without relying on `threadid()`

.

**Mentors**: [Xianda Sun](https://github.com/sunxd3)

**Project difficulty**: Medium to Hard

**Project length**: 350 hrs

[Pigeons.jl](https://github.com/Julia-Tempering/Pigeons.jl) implements parallel tempering and related algorithms that are particularly effective for multimodal and high-dimensional posteriors. This project has two related goals that together make Pigeons a first-class citizen of the TuringLang ecosystem.

The first part is documentation and examples. Turing.jl models can already be used as targets for Pigeons, but the combination is under-documented. The contributor will produce reproducible tutorials that walk through common use cases – multimodal posteriors, hierarchical models, models with difficult geometry – and compare Pigeons against HMC/NUTS on the same problems. These will be published on the Turing website and any integration rough edges found along the way will be fixed.

The second part is implementing the efficient Gibbs sampler from [arXiv:2410.03630](https://arxiv.org/abs/2410.03630) in [JuliaBUGS.jl](https://github.com/TuringLang/JuliaBUGS.jl). The paper shows that by exploiting the structure of the compute graph (rather than the graphical model), the time per sweep of a full-scan Gibbs sampler on GLMs can be reduced from to in the number of parameters – making high-dimensional GLMs feasible where traditional Gibbs is not, and outperforming HMC on effective samples per unit time in many regimes. JuliaBUGS already exposes the graph structure this approach relies on. The implementation must be correct and performant, validated against standard benchmarks with comparisons to both traditional Gibbs and HMC.

**Mentors**: Community

If you have an idea not listed here, propose it. Submit a short proposal with motivation, a concise plan, expected deliverables, and a timeline. Maintainers and mentors will review and help turn it into a plan. Be prepared to discuss scope with mentors early.

To discuss proposals and next steps, contact [Shravan Goswami](https://julialang.slack.com/team/U04UZB5U740) on the [Julia Slack](https://julialang.org/slack/).
