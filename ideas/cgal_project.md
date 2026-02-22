# CGAL Project — Project Ideas

**Source:** https://github.com/CGAL/cgal/wiki/Project-Ideas
**Scraped:** 2026-02-22T23:28:47.589291

---

-
[Notifications](https://github.com/login?return_to=%2FCGAL%2Fcgal)You must be signed in to change notification settings -
[Fork 1.5k](https://github.com/login?return_to=%2FCGAL%2Fcgal)

# Project Ideas

[68 revisions](https://github.com/CGAL/cgal/wiki/Project-Ideas/_history)

-
[GSoC 2026 Projects](https://github.com#gsoc-2026-projects)[Topological Filtering of Features in Triangle Meshes](https://github.com#topological-filtering-of-features-in-triangle-meshes)[Adding Support for New File Formats for Meshes](https://github.com#adding-support-for-new-file-formats-for-meshes)[Efficient k-DOPs](https://github.com#efficient-k-dops)[Approximate Convex Decomposition of Meshes with Collision-Aware Concavity and Tree Search](https://github.com#approximate-convex-decomposition-of-meshes-with-collision-aware-concavity-and-tree-search)[Ray Marching for Mesh Generation](https://github.com#ray-marching-for-mesh-generation)[Optimizing Geometric Operations](https://github.com#optimizing-geometric-operations)[Enhancing the 2D Regularized Boolean Operation Demo](https://github.com#enhancing-the-2d-regularized-boolean-operation-demo)[Enhancing CGAL Python Bindings](https://github.com#enhancing-cgal-python-bindings)[Implementing a 3D Arrangement of Planes Data Structure](https://github.com#implementing-a-3d-arrangement-of-planes-data-structure)[Isotropic Remeshing of Surface Triangle Meshes](https://github.com#isotropic-remeshing-of-surface-triangle-meshes)[Intersection of a Cellular Complex with a Plane](https://github.com#intersection-of-a-cellular-complex-with-a-plane)[Robust Discrete Differential Operators for Wild Geometry](https://github.com#robust-discrete-differential-operators-for-wild-geometry)[Shaders for Basic Viewer](https://github.com#shaders-for-basic-viewer)[Spatial Searching on GPU](https://github.com#spatial-searching-on-gpu)

[Information Candidates Should Supply](https://github.com#information-candidates-should-supply)[Previous Project Ideas and Successful Projects](https://github.com#previous-project-ideas-and-successful-projects)

The CGAL Project is a candidate mentoring organization of the [Google Summer of Code](https://summerofcode.withgoogle.com) 2026.
On this page we present some project ideas as well the [information](https://github.com#information-candidates-should-supply) applicants have to provide us.
**GSoC applicants are welcome to propose other ideas and check if a mentor is interested in supervising it**. For new project
proposals, contact us at [gsoc-cgal@inria.fr](mailto:gsoc-cgal@inria.fr).

**Mentor**: Sebastien Loriot

**Project description:**

Remeshing algorithms in CGAL requires the proper extraction of sharp features so that they can be represented in the output mesh ([like here for example](https://doc.cgal.org/latest/Mesh_3/index.html#fig__figuretwo_spheres_mesh)).
Classical method to detect sharp features are based on collecting edges with sharp dihedral surface angles. However, depending on
the quality of the input mesh, some noisy edges might be detected, or some edges might be detected.
To workaround these issues, it might be interesting to rely on tools from Topological Data Analysis, like for example persistence.
Indeed, extra data or missing data are all related to a notion of scale at which the problem is looked at. The goal of this project is
to implement such a strategy for provide curated feature edge graph to the meshing algorithm of CGAL. If time allows, extension to
detection of significant handles might also be looked at.

Resources:

[A Practical Solver for Scalar Data Topological Simplification](https://arxiv.org/abs/2407.12399)[To cut or to fill: a global optimization approach to topological simplification](https://www.cse.wustl.edu/~taoju/research/cutfill.pdf)[Topological Simplification of Nested Shapes](https://www.cs.wustl.edu/~taoju/research/nested_self.pdf)[Gudhi library](https://gudhi.inria.fr/)

**Required Skills:** C++17, Mesh Processing, Topological Data Analysis

**Contact:** [sebastien.loriot@cgal.org](mailto:sebastien.loriot@cgal.org)

**Duration:** 350h

**Mentors**: Andreas Fabri and Mael Rouxel-Labbé

**Project description:**

The CGAL library provides several functions to read and write meshes (surface and volume) in the [Stream Support package](https://doc.cgal.org/latest/Stream_support).
The list of currently supported file format is available [here](https://doc.cgal.org/latest/Stream_support/IOStreamSupportedFileFormats.html).
The goal of this project is to add support to more file formats. We could for example add support for glTF, gmsh format, 3mf v2, ...
The duration of the project will depend on the file format proposed for addition.

**Required Skills:** C++17

**Contact:** [sebastien.loriot@cgal.org](mailto:sebastien.loriot@cgal.org)

**Duration:** 90h, 175h, or 350h

**Mentors:** Gabriel Zachmann, Rene Weller, University of Bremen

**Project description:**

A nice generalization of AABBs are k-DOPs, which can bound geometry much tighter than AABBs by adjusting the parameter k. We have implemented algorithms that can create such kDOPs to bound a given set of polygons; also, our code can check two k-DOPs for overlap, even when they are rotated, i.e., no longer given over a common set of generating vectors. Finally, our code can make use of SSE/AVX instructions, which can give a good performance boost.

The task in this GSOC project will be to CGAL-ify our code. This means using the CGAL data structures (e.g., those for points, vectors, polygons, etc.). Also, an important part will be writing unit tests that can be run in an automated environment and test the correctness of the code. This can be a little challenge in the case where the pair of k-DOPs are rotated arbitrarily, but CGAL's convex hull algorithms should be helpful for that (the unit tests do not necessarily need to have optimal running times).

**Resources:**

[https://cgvr.cs.uni-bremen.de/papers/iros2019/iros2019_paper.pdf](https://cgvr.cs.uni-bremen.de/papers/iros2019/iros2019_paper.pdf)[https://cgvr.cs.uni-bremen.de/papers/vrais98/vrais98.pdf](https://cgvr.cs.uni-bremen.de/papers/vrais98/vrais98.pdf)- Section 3.5.9 in
[https://cgvr.cs.uni-bremen.de/papers/zachmann_diss/zachmann_diss.pdf](https://cgvr.cs.uni-bremen.de/papers/zachmann_diss/zachmann_diss.pdf)

**Required Skills:** C++17, experience with CGAL, Computational Geometry

**Contact:** {zach, weller}@cs.uni-bremen.de

**Duration:** 350h

**Mentors**: Léo Valque and Sebastien Loriot

**Project description:**

Approximate convex decomposition aims to partition a 3D shape into a set of nearly convex components whose convex hulls approximate the input geometry. This representation enables efficient collision detection and physical simulation, as many geometry processing algorithms are optimized for convex shapes.
The project is to implement an existing method described [here](https://arxiv.org/pdf/2205.02961) within CGAL. The algorithm relies on a plane-based decomposition strategy combined with a concavity metric that measures deviation from convexity using approximate symmetric Hausdorff distance between the surface and its convex hull. The algorithm iteratively cuts the mesh by planes to minimize global concavity. The algorithm selects the cutting planes using a Monte-Carlo Tree Search startegy.

Resources:

[The publication](https://arxiv.org/pdf/2205.02961)- [The implementation of the publication](/ideas/cgal-project/https-github-com-sarahweiii-coacd-https-github-com-sarahweiii-coacd))

**Required Skills:** C++17, Mesh Processing

**Contact:** [sebastien.loriot@cgal.org](mailto:sebastien.loriot@cgal.org)

**Duration:** 175h-350h

**Mentors:** Sven Oesau and Mael Rouxel-Labbé

**Project description:**

Some packages in CGAL need to compute the intersections of segments, rays, or lines with an implicit function. This is generally done through naive bisection algorithms. For some configurations however, we know that the implicit function is a signed distance field (offset meshing, alpha wrapping, ...), or an harmonic function (Poisson reconstruction). In these configurations, we can do better than bisection algorithms. The goal of this project is to implement these marching algorithms for the 3D Mesh Generation, Poisson Surface Reconstruction, and Alpha Wrapping packages, and identify other relevant packages, and possible improvements on these algorithms.

**Resources:**

[https://en.wikipedia.org/wiki/Ray_marching](https://en.wikipedia.org/wiki/Ray_marching)[https://iquilezles.org/articles/](https://iquilezles.org/articles/)[https://markjgillespie.com/Research/harnack-tracing/HarnackTracing.pdf](https://markjgillespie.com/Research/harnack-tracing/HarnackTracing.pdf)

**Required Skills:** C++17, Computer Graphics, Computational Geometry

**Contact:** [mael.rouxel.labbe@geometryfactory.com](mailto:mael.rouxel.labbe@geometryfactory.com)

**Duration:** 175h

**Mentor**: Efi Fogel and Sébastien Loriot

**Project Overview:**
This project focuses on the optimization of fundamental geometric operations, such as intersection detection for various families of curves in the 2D Arrangement package and perhaps also in the core of CGAL.

**Technical Context:**
The 2D Arrangement package relies on a flexible design utilizing several geometry traits class templates to support various families of curves, e.g., linear segments, conic curves, and Bézier curves. Each traits class template consists of a set of functors that implement specific geometric operations for a given curve family. Most popular kernels of CGAL include implementations of various operations on linear objects, such as segments. This project aims to improve the efficiency and robustness of these underlying operations across different curve types.

**Required Skills:** geometry, code development tools (e.g., git), and C++17 proficiency

**Contact:** [efifogel@gmail.com](mailto:efifogel@gmail.com)

**Duration:** 350h

**Mentor**: Efi Fogel

**Project description:**
The new demonstration program of the "2D Regularized Boolean Operations" package demonstrates various operations on polygons, such as union, intersection, and Minkowski sum. It also demonstrates the application of several operations in a pipeline fashion. The demo has not been published yet; it requires a few enhancements, such as the support of Boolean operations on general polygons bounded by non-linear curves.

**Required Skills:** Qt6, geometry, code development tools (e.g., git), and C++17 proficiency

**Contact:** [efifogel@gmail.com](mailto:efifogel@gmail.com)

**Duration:** 350h

**Mentor**: Efi Fogel

**Project description:**
Recently, we have developed a system that can generate Python bindings for several functions and class template instances in CGAL.
This project includes the following tasks:

- Adding Python bindings that are currently missing.
- Adding docstrings.
- Porting of CGAL examples to Python.

**Required Skills:** code development tools (e.g., git), C++17 proficiency, CMake, and Python

**Contact:** [efifogel@gmail.com](mailto:efifogel@gmail.com)

**Duration:** 350h

**Mentor**: Efi Fogel and Sven Oesau

**Project description:**
The goal of this project is to design and implement a data structure representing the subdivision of three-dimensional space induced by a set of planes. Unlike the 2D case, where the topology is maintained via a Halfedge Data Structure (HDS), this implementation will leverage CGAL's Combinatorial Maps package (specifically, 3-maps or Linear Cell Complexes) to handle the higher-dimensional topology (volumes, faces, edges, and vertices). The work will mainly consist of bridging the gap between the topological representation (Combinatorial Maps) and the geometric predicates required to construct, maintain, and operate on such an arrangement.

**Required Skills:** code development tools (e.g., git), C++17 proficiency, Linear Algebra

**Contact:** [efifogel@gmail.com](mailto:efifogel@gmail.com)

**Duration:** 350h

**Mentor**: Jane Tournois

**Project description:**

This project focuses on improving the surface isotropic remeshing algorithm for triangle meshes within the CGAL library. The work will include benchmarking the existing implementation on the Thingi10K dataset, preventing the creation of self-intersections during remeshing, and enhancing the edge-flipping stage to improve mesh quality. The project starts from a functional CGAL implementation used as a baseline.

Resources:

[CGAL::isotropic_remeshing()](https://doc.cgal.org/latest/Polygon_mesh_processing/group__PMP__meshing__grp.html#ga66cb01cf228ed22f0a2a474cfa2aeb3f)[A Remeshing Approach to Multiresolution Modeling - Botsch, Kobbelt](https://www.graphics.rwth-aachen.de/media/papers/remeshing1.pdf)[Thingi10K](https://ten-thousand-models.appspot.com/)

**Required Skills:** C++17, Mesh Processing

**Contact:** [jane.tournois@geometryfactory.com](mailto:jane.tournois@geometryfactory.com)

**Duration:** 175h-350h

**Mentor**: Sébastien Loriot and Simon Lopez

**Project description:**
The goal of this project is to propose and implement a generic framework to slice a cellular complex (a 3D grid, a tetrahedron mesh, a hex-(dominant)-mesh, ...).
The cells of the complex are assumed to be convex. More precisely, we are interested in the intersection polygons of each cell with the plan.
Depending on the requested output, the code will either generate a soup of polygons or a polygon mesh. A key functionality is to be able to transfer the cell id to each polygon.
The nature of the problem make it trivially parallel on CPU. If time allows, a GPU version can be made for real-time display.

**Required Skills:** C++17, Mesh Processing

**Contact:** [sebastien.loriot@cgal.org](mailto:sebastien.loriot@cgal.org)

**Duration:** 175h-350h

**Mentor**: Andreas Fabri and Mario Botsch

**Project description:**
The goal of this project is to implement the [paper](https://cg.cs.tu-dortmund.de/publications/2025-robust.pdf) by Mario Botsch and Sven Wagner in CGAL,
starting from Sven's [code](https://github.com/sdwagner/wildDDG). This project is co-mentored by a core CGAL developer, and the author of the publication.

**Required Skills:** C++17, Geometry Processing

**Contact:** [andreas.fabri@geometryfactory.com](mailto:andreas.fabri@geometryfactory.com)

**Duration:** 175h-350h

**Mentor**: Guillaume Damiand an Jason Fong

**Project description:**
Project description: Since CGAL 4.13, it has been possible to visualize various CGAL data structures using a simple global draw() function. This visualization capability was further enhanced in CGAL 6.0 with the introduction of the Basic Viewer package, which allows users to develop their own visualization code. The rendering is performed using OpenGL shaders, with different shaders available for drawing vertices, edges, and faces in various modes. For example, one shader enables transparent rendering of parts of an object, making it possible to visualize the interior of a 3D model.

However, the current version of these shaders has some limitations:

- The initial size of the drawn object is sometimes incorrectly calculated, depending on whether the object is 2D or 3D and its overall dimensions.
- The edges of meshes are rendered as rectangles, which can lead to visual artifacts.

The goal of this project is to improve the shaders used in the Basic Viewer and address these issues. We will also explore solutions implemented in major software tools like MeshLab or ParaView to determine if existing approaches can be directly applied to resolve these challenges.

**Required Skills:** C++17, OpenGL Shaders

**Contact:** [guillaume.damiand@cnrs.fr](mailto:guillaume.damiand@cnrs.fr)

**Duration:** 175h

**Mentor**: Mael Rouxel-Labbé, Sven Oesau, and Pierre Alliez

**Project description:**
CGAL, as of now, is entirely CPU-oriented. Both the advancements in software and hardware for GPUs make it an attractive target architecture to port and develop computation geometry algorithms. Internally, a few projects have already attempted to use GPU computing, with promising results.

The goal of this project is to continue work on a series of prototypes for axis-aligned bounding box (AABB) trees on GPUs, and more generally spatial searching structures on GPUs. The end goal is to adapt a typical AABB-heavy algorithm such as self-intersection detection to the new architecture.

Resources:

**Required Skills:** C++17, GPU design proficiency

**Contact:** [mael.rouxel.labbe@geometryfactory.com](mailto:mael.rouxel.labbe@geometryfactory.com)

**Duration:** 350h

The application process has several steps. Before contacting anybody verify that you are eligible (Check section 7.1 of the official [rules](https://summerofcode.withgoogle.com/rules)). The next step is to contact the mentor
of the project you are interested in. You have to convince him that you are the right person to get the job
done. The next step is to work out more details and to contact the mentoring organization by providing
the following information by email to [gsoc-cgal@inria.fr](mailto:gsoc-cgal@inria.fr):

-
Project:

- Select a project in the list and provide your personal and detailed description. If you wish to work on another idea of your own, we are pretty open as long as this serves the goal of consolidating CGAL as a whole.
- Provide a proposal of a technical solution with your envisioned methodology. The more detailed the better.
- Explain how the solution will be available to the user, in which form. Do not forget the documentation, unitary tests and cross-platform aspects.
- Provide a realistic schedule with objectives (one every two weeks for example) and deadlines. Focus on mid-term objectives as well as on the final evaluation.

-
Personal data:

- First name, last name, affiliation and geographical location.
- A brief list of the main studies and programming courses attended, with ranking.
- List of the most important software projects contributed and success.
- Which are your best skills in terms of programming and scientific computing?
- In general what is your taste in terms of programming? language, methodology, team work, etc.
- Is there anything that prevents you from working full time on the project during the program period?
- How do you see your involvement after the program ends? Do you see yourself pushing the project further, or do you see yourself contributing to other CGAL projects?
- Are you more interested in the theory/scientific aspect of CGAL, or do you feel more like a hacker?
- What are your long-term wishes in terms of job?



**General Information**

[Information for New Developers](https://github.com/Information-for-New-Developers)- Developing with Git
- Structure of a CGAL Package
- Building
[Concurrency in CGAL](https://github.com/Concurrency-in-CGAL)[License](https://github.com/License)[Documentation Guidelines](https://github.com/Documentation-Guidelines)- Reviewing Process
[Testing](https://github.com/Testing)- Miscellaneous

[Tools](https://github.com/Tools)[Scripts](https://github.com/Scripts)[Libraries](https://github.com/Libraries)[Infrastructure](https://github.com/Infrastructure)- Releases
- Miscellaneous
