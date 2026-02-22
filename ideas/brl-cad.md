# BRL-CAD — Project Ideas

**Source:** https://github.com/opencax/GSoC/issues?q=is%3Aissue+is%3Aopen+label%3A%22GSoC+2026%22
**Scraped:** 2026-02-22T23:28:47.616972

---

## #115: Improving ManifoldCAD

## Outline

ManifoldCAD is a web app for modeling using manifold's typescript API. The goal of this project is to improve the usability of ManifoldCAD.

## Details

To work on some of the tasks in https://github.com/elalish/manifold/issues/1460, need discussion on task details.

## Expected Outcome

## Future Possibilities <!-- optional -->

## Project Properties

### Skills

Frontend skills, e.g., html/css/javascript/typescript.

### Difficulty <!-- easy, medium, hard -->

Easy/Medium

### Size <!-- medium (175h), long (350h) -->

Medium

### Additional Information

* Potential mentor(s): @pca006132 @elalish 
* Organization website: https://github.com/elalish/manifold
* Communication channels: https://github.com/elalish/manifold/discussions

---

## #114: Improving CI and benchmarking for manifold

**Labels:** Difficulty: Easy, Lang: Javascript, Size: Medium (175h), Project: Manifold, GSoC 2026, Lang: TypeScript

## Outline

Improving the CI setup and providing benchmark results for manifold.

## Details

1. Add more checks to the CI, e.g., address sanitizer, deterministic results across platforms.
2. Add continuous benchmarking using GitHub action, and write the frontend interface for displaying benchmark results.
3. Port benchmarks from projects such as OpenSCAD.

Also see https://github.com/elalish/manifold/issues/1498

## Expected Outcome

See above.

## Future Possibilities <!-- optional -->

## Project Properties

### Skills

- GitHub action
- Frontend (HTML, CSS, JavaScript/TypeSCript)

### Difficulty <!-- easy, medium, hard -->

Easy

### Size <!-- medium (175h), long (350h) -->

medium

### Additional Information

* Potential mentor(s): @pca006132 @elalish 
* Organization website: https://github.com/elalish/manifold
* Communication channels: [https://github.com/elalish/manifold/discussions
](https://github.com/elalish/manifold/discussions)

---

## #113: Integrate AI chat for helping users creating OpenSCAD scripts

**Labels:** Project: OpenSCAD, Difficulty: Medium, Lang: C/C++, Size: Long (350h), GSoC 2026

## Outline

Add optional AI support that can help users writing OpenSCAD scripts. There are a number of ways AI models can help, e.g. by assisting with trigonometry and other math problems, explaining existing scripts users want to modify or describing image output for vision impaired users.

## Details

There is already a simple prototype for a [chat window](https://github.com/openscad/openscad/pull/6118) that can be used a the base for the project.

Scope of the project:
* Focus on interfacing with local models (e.g. via a local Ollama instance)
* Basic chat interaction
* Optional sending the current script with the chat message
* Optional sending of the current view-port along with the chat message

Non-Goals:
* Integrating with commercial cloud providers
* Training or modifying AI models
* Using Python for AI interactions

## Expected Outcome

Simple functionality for AI chat with some basic support for interacting with the current OpenSCAD project.

## Future Possibilities <!-- optional -->

Extend the functionality by allowing the AI to interact directly with the current code using function calling.

## Project Properties

### Skills

* Programming language is C++
* Understanding of network APIs using JSON for encoding data
* Basic understanding on AI and how it is accessed from an application

### Difficulty <!-- easy, medium, hard -->

Medium

### Size <!-- medium (175h), long (350h) -->

Long (350h)

### Additional Information

Potential mentor(s): [Marius Kintel](https://github.com/kintel) ([IRC](https://web.libera.chat/?channel=#openscad): kintel), [Torsten Paul](https://github.com/t-paul/) ([IRC](https://web.libera.chat/?channel=#openscad): teepee), [Ryan Colyer](https://github.com/rcolyer) ([IRC](https://web.libera.chat/?channel=#openscad): InPhase)
    Organization website: https://www.openscad.org/

Links:
* Prototype Pull Request: https://github.com/openscad/openscad/pull/6118
* Ollama API: https://github.com/ollama/ollama/blob/main/docs/api.md
* Ollama tool calling: https://docs.ollama.com/capabilities/tool-calling

---

## #112: Create a minimal web application using the OpenSCAD WASM build

**Labels:** Project: OpenSCAD, Difficulty: Medium, Size: Long (350h), GSoC 2026, Lang: TypeScript

## Outline

OpenSCAD has a WASM build for quite some time and it's used in some nice websites like https://ochafik.com/openscad2/ . The scope of the project is to create a minimal, easy to use package that can be integrated into the https://openscad.org/ website.

## Details

Goals:
- Easy to add to existing web pages
- Allow picking up SCAD scripts from URL or text area
- Generate and show the model in a 3D view (e.g. via Three.js)
- Optional: download the generated model

Non-Goals:
- Customizer
- Full-featured editor
- Upload of files and or libraries

## Expected Outcome

One example covering the project goals would a sequence of pages presenting the different scripts from chapter 2 of the [OpenSCAD Tutorial](https://en.wikibooks.org/wiki/OpenSCAD_Tutorial/Chapter_2). 

## Project Properties

### Skills

* Programming in TypeScript
* Understanding how to use WASM binaries
* Package modules for use in plain HTML pages

### Difficulty <!-- easy, medium, hard -->

Medium

### Size <!-- medium (175h), long (350h) -->

Long (350h)

### Additional Information

Potential mentor(s): [Marius Kintel](https://github.com/kintel) ([IRC](https://web.libera.chat/?channel=#openscad): kintel), [Torsten Paul](https://github.com/t-paul/) ([IRC](https://web.libera.chat/?channel=#openscad): teepee), [Ryan Colyer](https://github.com/rcolyer) ([IRC](https://web.libera.chat/?channel=#openscad): InPhase)
    Organization website: https://www.openscad.org/

---

## #111: Add OpenSCAD support for exporting models in STEP format

**Labels:** Project: OpenSCAD, Difficulty: Hard, Lang: C/C++, Size: Long (350h), GSoC 2026

## Outline

The STEP format is widely used in the industry to transfer CAD data between different systems. Currently OpenSCAD does not support STEP import or export. Adding STEP export would open up a number of new usecases or simplify the workflow as no external conversion tools are needed to convert to STEP. This includes the design of 3D models for other CAD tools, e.g. for KiCAD where STEP models are used to render 3D representations of PCBs. Other use cases are for manufacturing where sometimes only STEP files are accepted as input, e.g. for CNC milling services.

## Details

The main focus of this project is to get the ground work done for exporting more detailed models, as opposed to just exporting the fully rendered single mesh which is the normal case right now.

Topics that need to be solved
* Research options of usable libraries
* Investigate what type of STEP files are accepted as input by various tools
* Select library and integrate into OpenSCAD
* Implement base functionality to export single meshes
* Add test cases to verify the new export functionality
* Update build system to include the new library into installers
* Prototype how more advanced models can be exported

## Expected Outcome

* OpenSCAD supports exporting single meshes as STEP
* (optional) Understanding/Plan of how to support additional features supported by STEP

## Project Properties

### Skills

* Programming language is C++
* Understand and use APIs from external libraries
* Integrate new libraries into the build system for the 3 supported platforms
* Add test cases with files using the new features to allow regression testing

### Difficulty

Hard

### Size

Long (350h)

## Additional Information

* Potential mentor(s): [Marius Kintel](https://github.com/kintel) ([IRC](https://web.libera.chat/?channel=#openscad): kintel), [Torsten Paul](https://github.com/t-paul/) ([IRC](https://web.libera.chat/?channel=#openscad): teepee), [Ryan Colyer](https://github.com/rcolyer) ([IRC](https://web.libera.chat/?channel=#openscad): InPhase)
* Organization website: https://www.openscad.org/

Known libraries:
* StepCode - http://stepcode.org/  (https://github.com/stepcode/stepcode)
* OpenCASCADE - https://www.opencascade.com/

---

## #110: Integrated language help feature in OpenSCAD

**Labels:** Project: OpenSCAD, Difficulty: Easy, Lang: C/C++, Size: Medium (175h), GSoC 2026

## Outline

Add more interactive help features for built-in functions and modules. Right now there's already a nice summary of parameters linked as [cheat sheet](http://www.openscad.org/cheatsheet/). Scope of this projects would be to use this information in extended form and make it available in a more direct way in the editor.

## Details

* Convert the cheat sheet information into machine readable format
* Find a way to generate the existing HTML format based on the core data
* Add context help to editor giving help for built-in functions and modules, e.g. by adding formatted help output to the console window, including the links to further documentation like the language manual on Wikibooks

## Expected Outcome

Cheat sheet is integrated into the application and additional context help for built-in functions and modules is available.

## Project Properties

### Skills

* Programming language is C++
* GUI programming with the Qt framework

### Difficulty <!-- easy, medium, hard -->

Easy

### Size <!-- medium (175h), long (350h) -->

Medium (175h)

### Additional Information

* Potential mentor(s): [Marius Kintel](https://github.com/kintel) ([IRC](https://web.libera.chat/?channel=#openscad): kintel), [Torsten Paul](https://github.com/t-paul/) ([IRC](https://web.libera.chat/?channel=#openscad): teepee), [Ryan Colyer](https://github.com/rcolyer) ([IRC](https://web.libera.chat/?channel=#openscad): InPhase)
* Organization website: https://www.openscad.org/

---

## #109: "Vibe Coding" GCV: Agentic Modernization of BRL-CAD’s Geometry Conversion Suite

**Labels:** Project: BRL-CAD, Difficulty: Medium, Difficulty: Hard, Lang: C/C++, Lang: Python, GSoC 2026

## Outline

This is a genuine research project.  Do not apply if you are unfamiliar with agentic coding and its current limitations.

BRL-CAD’s libgcv is the central "Swiss Army knife" for converting geometry between BRL-CAD’s CSG format and external formats (STL, OBJ, STEP, etc.). However, many converters rely on legacy codebases with inconsistent APIs. This project will use AI coding agents (e.g., Aider, Cursor, or custom LLM pipelines) to refactor these converters, implement new modern formats, and standardize the plugin architecture through a "vibe coding" workflow—where the developer provides high-level geometric intent and the agent manages the implementation details.

## Details

The project focuses on leveraging autonomous agents to handle the "heavy lifting" of C/C++ development:
- **Agentic Refactoring:** Deploying agents to identify and fix memory leaks, standardize error handling, and migrate legacy converters into the unified libgcv plugin API.
- **Vibe-Driven Prototyping:** Using high-level natural language prompting to rapidly scaffold new converters for modern formats like glTF, USD, or MaterialX.
- **Automated Testing & Edge Cases:** Using agents to analyze geometric specifications and automatically generate exhaustive test suites that verify conversion fidelity for specific formats, complex NURBS, mesh entities, etc.
- **Knowledge Distillation:** Creating an agent-driven "GCV Developer Guide" that can help future contributors "vibe code" their own conversion plugins by providing context-aware code snippets and API mapping.

## Expected Outcome

- A modernized, clean libgcv library API with significantly reduced complexity for adding new formats.
- Updated libgcv API that tracks important geometry characteristics like representation format conversions, preservation of hierarchy, solidity, object counts, physical properties, and attribute metadata.
- At least three new functional conversion plugins (e.g., glTF or USD) developed primarily through agentic workflows.
- A set of "vibe coding" templates and system prompts optimized for BRL-CAD’s unique C/C++ architectural style.

## Future/Stretch-Goal Possibilities <!-- optional -->

- **Self-Healing Converters:** Agents that can automatically adjust conversion tolerances when a "leaky" mesh is detected.
- **Natural Language Conversion:** A CLI interface where users can "describe" how they want their geometry converted (e.g., "Export this to STL but simplify the mesh density by 50%").
- **Research Paper:** An academic research paper summarizing the findings.

## Project Properties

### Skills

Languages: C/C++ (Core), Python (for agent orchestration).
Tools: AI Coding Agents (Aider, Cursor, OpenDevin), LLM Prompt Engineering.
Domain: 3D Geometry formats and conversion logic.

### Difficulty <!-- easy, medium, hard -->

Medium/Hard (While the AI does the writing, the dev must have a deep understanding to "steer" the agent through complex C/C++ logic and data structure changes.)

### Si

*[truncated]*

---

## #108: Stabilize Appleseed Rendering

**Labels:** Difficulty: Easy, Difficulty: Medium, Lang: C/C++, Project: Appleseed, GSoC 2026

Stabilizing Appleseed Rendering Resolving Dependency Regressions and (potentially) Windows-Specific Rendering Bugs

## Outline

Our Appleseed renderer prototype is currently hampered by a significant bug likely introduced during recent upgrades of core dependencies like OSL and Boost. This bug manifests most prominently on Windows, often resulting in crashes or incorrect memory handling during the initialization of the appleseed optics pipeline. This project aims to perform a deep-dive forensic debug of the codebase to identify the changed API or incompatible logic, fix the regression, and establish a more robust dependency-tracking system to prevent future breakage.

## Details

The project will follow a structured debugging and stabilization path:
- **Forensic Environment Setup:** Establishing a Windows-based development environment that reproduces the bug using the latest BRL-CAD trunk and specific versions of OSL and Boost.
- **Root Cause Analysis:** Using advanced debugging tools (e.g., Visual Studio Debugger, WinDbg, or Valgrind on Linux) to determine if the issue stems from:
-- OSL API Changes: Regressions in how Appleseed passes intersection data to the latest OSL RendererServices.
-- Symbol Visibility: Incompatibilities in how Boost or OSL symbols are exported/imported on Windows (DLL hell).
-- Boost Migration: Breaking changes in Boost.Filesystem or Boost.System utilized by the appleseed bridge.
- **Patch Implementation:** Refactoring the bridge logic to accommodate the updated dependencies.

Contingency/Stretch Goals: If the fix is straightforward, the project will pivot to:

- **CI Robustness:** Enhancing Appleseed's CI/CD to catch dependency regressions earlier.
- **Feature Parity:** Implementing missing command-line flags (e.g., specific AOV outputs) in BRL-CAD's "art" Appleseed-based renderer.

## Expected Outcome

- A report on the specific incompatibility found and the logic used to resolve it.
- A fully functional appleseed/art renderer that works reliably with current versions of OSL and Boost across all platforms (specifically Windows).

## Future Possibilities <!-- optional -->
- **Automated Regression Testing:** Creating a "golden image" test suite that runs automatically upon dependency updates.
- **Plugin Architecture:** Moving Appleseed toward a more modular plugin system to isolate it from dependency updates.

## Project Properties

### Skills

Languages: C++, CMake.
Tools: Debugging on Windows (Visual Studio/MSVC), dependency management.
Domain Knowledge: Basic understanding of how renderers interface with external libraries (OSL/Boost).

### Difficulty <!-- easy, medium, hard -->

Easy/Medium

### Size <!-- medium (175h), long (350h) -->

Medium

### Additional Information

* Potential mentor(s): Sean Morrison
* Organization website: https://brlcad.org
* Communication channels: https://brlcad.zulipchat.com

---

## #107: Production-Ready PBR: Integrating BRL-CAD geometry ray tracing with Appleseed rendering

**Labels:** Project: BRL-CAD, Difficulty: Hard, Lang: C/C++, Size: Long (350h), Project: Appleseed, GSoC 2026

## Outline

BRL-CAD recently introduced "art," a command-line renderer that integrates the appleseed rendering engine. While BRL-CAD provides the geometry and intersection logic, appleseed handles the light transport and shading. Currently, "art" is in an experimental state, supporting only basic, single-file Open Shading Language (OSL) shaders. This project aims to bring "art" to production-readiness by implementing support for complex shader networks (OSL and MaterialX), advanced material properties like subsurface scattering and emission, and robust texture mapping for BRL-CAD primitives.

## Details

The focus of this project is to transition "art" from a prototype to a reliable production tool. Key development areas include:

- Shader Network Integration: Move beyond single-file .osl shaders to support full shader networks and MaterialX files. This involves creating a robust mapping system between BRL-CAD material properties and appleseed’s shading nodes.
- Texture Mapping & UVs: Solving the "mapping problem" by ensuring that BRL-CAD’s implicit primitives (ellipsoids, tori, etc.) correctly pass coordinate data to appleseed for procedural and image-based texturing.
- Advanced Light Transport: Implementing and testing advanced optics features within the "art" framework, including:
-- Emission: Allowing BRL-CAD geometry to act as light sources.
-- Subsurface Scattering (SSS): Essential for realistic skin, wax, and plastic.
-- Volumetrics: Basic support for fog or smoke within the appleseed optics pipeline.

## Expected Outcome

- A production-stable version of the art utility capable of rendering complex scenes with full PBR fidelity.
- Support for OSL shader networks, allowing users to use industry-standard material workflows.
- A suite of "Production-Ready" demo scenes showing off complex materials (translucency, metallic flakes, textures) rendered directly from BRL-CAD .g files.
- Documentation for the updated material system and an "art" manual page for PBR rendering in BRL-CAD.

## Project Properties

### Skills

**Languages:** C++, Open Shading Language (OSL).
**Concepts:** Physically-Based Rendering (PBR), Light Transport (Path Tracing), MaterialX.
**APIs:** appleseed API, BRL-CAD librt.

### Difficulty <!-- easy, medium, hard -->

Hard (Reasoning: Requires a deep understanding of path tracing math and the ability to bridge two very different software architectures.)

### Size <!-- medium (175h), long (350h) -->

Long (350h)

### Additional Information

* Potential mentor(s): Sean Morrison
[Erik Greenwald](mailto:devs@brlcad.org)
* Organization website: https://brlcad.org
* Communication channels: https://brlcad.zulipchat.com

---

## #106: Automated Surface Skinning in BRL-CAD

**Labels:** Project: BRL-CAD, Difficulty: Medium, Difficulty: Hard, Lang: C/C++, GSoC 2026

# Automated Surface Skinning: Exterior Mesh Extraction and Simplification for BRL-CAD Models

## Outline

BRL-CAD models often consist of complex, nested CSG hierarchies that are computationally expensive to render or export for external applications. "Skinning" refers to the process of generating a simplified, watertight exterior polygonal mesh that represents the outer boundary of a model while discarding internal geometry. This project aims to implement a tool—either through a new algorithm or the integration of license-compatible libraries—to automate the creation of these exterior "shells."

## Details

The project will focus on transforming internal CSG representations into optimized boundary representations (B-Reps). Key technical components include:

- **Algorithm Selection:** Evaluating and implementing algorithms such as Voxel-based Shrink-wrapping, Alpha Shapes, or Visible Surface Manifold extraction.
- **Internal Geometry Pruning:** Developing logic to identify and ignore "hidden" internal components that do not contribute to the exterior silhouette.
- **Mesh Simplification:** Once the skin is generated, implementing decimation techniques (like Quadratic Error Metrics) to reduce polygon count while preserving visual fidelity.
- **Integration:** Creating a standalone CLI tool or a dedicated command within MGED/Archer. If a semi-automated route is chosen, this would involve a GUI allowing users to "paint" or select focus areas for skinning.

## Expected Outcome

- A functional BRL-CAD utility (e.g., g-skin or new GUI) that accepts a .g database and outputs a simplified, manifold .g or .gltf file.
- A robust method for handling "gaps" or "leaks" in the mesh to ensure the output is watertight.
- Documentation covering the algorithm's constraints and a performance comparison against raw mesh exports.

## Future Possibilities <!-- optional -->

- LOD Generation: Automatically creating various "Levels of Detail" (LOD) for real-time visualization.
- Thermal/CFD Pre-processing: Enhancing the tool to produce meshes specifically optimized for simulation solvers.
- GUI Plugin: A full integration into the MGED or Archer interface with real-time "shrink-wrap" previews.

## Project Properties

### Skills

- Languages: C/C++
- Mathematics: Computational geometry and mesh topology optional but helpful.
- APIs: Familiarity with BRL-CAD's librt and libwdb libraries and related conversion commands optional to know in advance but necessary for implementation.

### Difficulty <!-- easy, medium, hard -->
Medium or Hard depending on whether you plan to implement your own algorithm or glue

### Size <!-- medium (175h), long (350h) -->

Long (350h)

### Additional Information

* Potential mentor(s): Sean Morrison
[Erik Greenwald](mailto:devs@brlcad.org)
* Organization website: https://brlcad.org
* Communication channels: https://brlcad.zulipchat.com

---

## #105: Ensure OpenSCAD and BRL-CAD compatibility

**Labels:** Project: OpenSCAD, Project: BRL-CAD, Difficulty: Medium, Lang: C/C++, Size: Long (350h), GSoC 2026

# Enhancing Cross-CAD Interoperability: Ensure OpenSCAD Language Compatibility in BRL-CAD

## Outline
OpenSCAD is a popular functional-language-based CAD tool used extensively for parametric 3D design. While BRL-CAD is an incredibly powerful solid modeling system, there remains a gap in its ability to natively interpret or fully replicate OpenSCAD’s unique syntax and geometric operations. This project aims to close that gap by identifying missing entities, operations, and actions in BRL-CAD and implementing them to ensure seamless compatibility.

## Details
The project involves three primary phases:

1. Gap Analysis: Researching the OpenSCAD language specification against BRL-CAD’s current command set and primitive library to identify missing features (e.g., specific Minkowski operations, 2D-to-3D extrusions, or complex hull operations).
2. Implementation of Entities & Operations: Extending BRL-CAD’s internal logic to support these missing features. This includes:
  - CSG Operations: Refining how BRL-CAD handles nested transformations and Boolean operations to match OpenSCAD's behavior.
  - Geometric Primitives: Mapping OpenSCAD primitives (like polyhedron) to BRL-CAD equivalents or creating new ones where necessary.
  - Functionality: Implementing OpenSCAD-specific actions like minkowski(), hull(), and linear_extrude().
3. Parser/Bridge Refinement: Enhancing the existing importer or bridge logic to ensure that an .scad file renders identically within the BRL-CAD environment.

## Expected Outcome
A robust set of libraries or tools within BRL-CAD that support OpenSCAD syntax and operations.

The ability to import and render complex OpenSCAD scripts in BRL-CAD with 1:1 geometric parity.

Documentation detailing the newly implemented features and a test suite of .scad files successfully converted to BRL-CAD .g databases.

## Future Possibilities
Bi-directional Sync: Enabling changes in BRL-CAD to reflect back into the OpenSCAD script.

Performance Optimization: Utilizing BRL-CAD’s high-performance ray-tracing to speed up the previewing of complex OpenSCAD designs.

Full Library Support: Extending compatibility to popular OpenSCAD libraries like MCAD or BOSL2.

## Project Properties
Languages: C/C++ (BRL-CAD’s core)
Concepts: Constructive Solid Geometry (CSG), Lexing/Parsing (Lex/Yacc or Lemon), Geometry Kernels.
Tools: Familiarity with both BRL-CAD and OpenSCAD environments.

### Difficulty
Hard (Reasoning: This requires a deep understanding of two different geometric engines and the ability to map complex mathematical operations between them.)

### Size
Long (350h)

### Additional Information
* Potential mentor(s): Sean Morrison, Daniel Rossberg, Ali Haydar
* Organization website: [https://brlcad.org](https://www.google.com/search?q=https://brlcad.org)
* Communication channels: [https://brlcad.zulipchat.com](https://www.google.com/search?q=https://brlcad.zulipchat.com)

---

## #103: Support for arbitrary parametric objects

**Labels:** Difficulty: Easy, Difficulty: Medium, Lang: Python, Project: IfcOpenShell, Size: Medium (175h), Size: Short (90h), GSoC 2026

## Outline

3D geometry is currently defined by a data schema known as IFC. This project is to build an interface and feature in Blender to link an object's geometry to any external geometry source (e.g. Blend file, OBJ, STL, etc).

This means people can use their preferred modeling tool or parametric object generation script and the result can still be synchronised with the building model.

## Expected Outcome

A new interface panel in Blender, and an established convention on how to read and sync these external data sources.

### Skills

Python, some Blender

### Difficulty <!-- easy, medium, hard -->

Easy to medium

### Size <!-- medium (175h), long (350h) -->

Medium

### Additional Information

* Potential mentor(s): Dion Moult
* Organization website: https://ifcopenshell.org
* Communication channels: https://osarch.org/chat

---

## #102: Improving the k-File to BRL-CAD Converter

**Labels:** Project: BRL-CAD, Difficulty: Medium, Lang: C/C++, Size: Medium (175h), Size: Long (350h), Size: Short (90h), GSoC 2026

## Outline

In the past years, we put some effort in the development of a LS-DYNA keyword file to BRL-CAD converter. Although we made great progress there, we still can't convert every k-file to g, i.e. the native BRL-CAD format. The goal of this project is to increase the number of covertable k-files. 

## Details

The sources of the current k-file to BRL-CAD converter can be found in the brlcad repository at [src/conv/g](https://github.com/BRL-CAD/brlcad/tree/main/src/conv/k-g). You have to compile BRL-CAD from its sources to work on this project and see the effects of your changes.

Examples of k-files, which cannot be converted with k-g, can be found here: [THUMS](https://www.toyota.co.jp/thums/) You can however use your own examples.

## Expected Outcome

We expect an improved k-g LS-DYNA keyword file to BRL-CAD converting program as the outcome from this project.

## Project Properties

### Skills

* C/C++
* LS-DYNA or a similar FE solver software, which can read k-files (needed as reference for how the geometry should look like)

### Difficulty

medium

### Size

This project could have any size, short (90h), medium (175h) or long (350h), depending on the amount of functionality you want to add.

### Additional Information

* Potential mentor(s):
[Ali Haydar](mailto:devs@brlcad.org)
[Daniel Rossberg](mailto:devs@brlcad.org)
[Erik Greenwald](mailto:devs@brlcad.org)
* Organization website: https://brlcad.org
* Communication channels: https://brlcad.zulipchat.com

---

## #99: Create a compelling interface and functionality for the IfcOpenShell WASM / pyodide module

**Labels:** Difficulty: Medium, Lang: Python, Lang: Javascript, Project: IfcOpenShell, Size: Medium (175h), Size: Long (350h), Size: Short (90h), GSoC 2026

## Outline

IfcOpenShell is a software module for BIM/AEC (Building Information Modelling, Architecture Engineering and Construction) with extensive functionality implemented in python for the wide variety of multi-disciplinary tasks in construction. Therefore we have primarily looked at pyodide (a WASM distribution of CPython) to bring ifcopenshell to the client-side web.

There is now a demo-application online, the applicant is expected to enrich this demo-application with some of the existing ifcopenshell functionality and at the same time work on a more idiomatic Javascript API that wraps the IfcOpenShell objects as they are proxied by pyodide.

http://wasm.ifcopenshell.org/

## Expected Outcome

Enrich the demo application with, e.g:

- Rich parametric authoring
- Validation (IDS, schema, custom, ...)
- Some of the other pre-existing functional modules, e.g clash detection (geometric interference of building elements), costing, scheduling
- Something else :)

### Skills

Python, JavaScript

### Difficulty

Difficulty and scope based on applicant interests

### Size

Difficulty and scope based on applicant interests

### Additional Information

* Potential mentor(s): @aothms
* Organization website: https://ifcopenshell.org
* Communication channels: https://osarch.org/chat

---

## #98: Authoring interface for IFC4.3 alignment geometry in Bonsai

**Labels:** Difficulty: Medium, Lang: Python, Project: IfcOpenShell, Size: Medium (175h), Size: Long (350h), Size: Short (90h), GSoC 2026

![Image](https://github.com/user-attachments/assets/9f59b304-468c-4db0-96d6-924f228d2cf3)

### Outline

Industry Foundation Classes (IFC) offer the ability for rich information exchanges between modeling, analysis, planning, and other software tools in the Architecture, Engineering, and Construction (AEC) industry.  Specifically, the latest release of IFC (version 4.3, also referred to as IFC4X3) adds linear referencing via alignment modeling, which is core to describing the construction and maintenance of infrastructure assets such as roads, bridges, and railways.

### Details

Alignment import (read) capabilities have been added to IfcOpenShell and the Bonsai add-in for Blender. They have reached a state of maturity such that the next logic step is to enable alignment authoring (write) capabilities.  

### Expected Outcome

Alignment authoring will take place in Blender via the Bonsai add-in.  A user-focused workflow has been developed and documented, along with preliminary user interface mockups. This project would add alignment authoring capabilities via new panels and other items within Blender.  The ifcopenshell.api namespace will also need to be enhanced incrementally to support the new user interface tools.

### Project Properties

#### Skills

Understanding and general working knowledge of python.

#### Difficulty

Medium

#### Size

##### Medium (175 h)

The participant focuses on authoring horizontal alignments via the PI method.  This could be via interactive icons or primarily through a table-based interface.  The user would need to be able to add, edit, and remove PI (point of intersection) points.  Additionally the user would need to be able to adjust the radius that corresponds to each PI point. Though not strictly required for this project, the authoring tool would also enable definition and editing of entry and exit transition curve type (clothoid, sine spiral, polynomial spiral, etc.) and length.

##### Long (350 h)

PI-based alignment would be added for vertical and cant as well.  A basic corridor modeling UI tools would be implemented to allow for sweeping geometry (open or closed profile) along an alignment curve to generate 3D linear geometry via IfcSectionedSolidHorizontal and related IFC entities.

#### Additional information

Mentors: Rick Brice @RickBrice & Scott Lecher @civilx64

Organization website: https://ifcopenshell.org

Communication channels: https://github.com/IfcOpenShell/IfcOpenShell/discussions

Technical resources:

https://docs.bonsaibim.org/guides/development/index.html

[Blender 4.3: Precise Modeling for Architecture, Engineering, and 3D Printing](https://a.co/d/cdryOQQ)

[Python Scripting in Blender](https://a.co/d/3us1PuT)

---

## #97: Manifoldness repair

**Labels:** Difficulty: Hard, Lang: C/C++, Size: Long (350h), Project: Manifold, GSoC 2025

## Outline

Repair triangle soup that are not manifold.

## Details

Basically, a valid solid mesh should be both manifold and has no self-intersection. However, models from the internet may contain defects. This project is about coming up with an algorithm that converts and repair a triangle soup into a manifold mesh.

This will contain a lot of heuristics, basically what we need is:

- Stitching faces together, and maybe join faces that are close enough.
- Fill holes.
- Duplicate vertices and edges such that the result is a manifold in terms of connectivity.

## Expected Outcome

Implementation of said algorithm.

## Future Possibilities <!-- optional -->

## Project Properties

### Skills

- C++
- Graph data structure.
- Algorithms.

### Difficulty <!-- easy, medium, hard -->

Hard.

### Size <!-- medium (175h), long (350h) -->

Long (350h)

### Additional Information

* Potential mentor(s): @elalish @pca006132 
* Organization website: https://manifoldcad.org/
* Communication channels: https://github.com/elalish/manifold/discussions

---

## #96: Overlap removal

**Labels:** Difficulty: Hard, Lang: C/C++, Size: Long (350h), Project: Manifold, GSoC 2025

## Outline

Remove overlaps in meshes that contain self-intersection, assuming the mesh is a manifold.

## Details

Basically, a valid solid mesh should be both manifold and has no self-intersection. However, models from the internet may contain defects. This project is about coming up with an algorithm that removes self-intersections.

See https://github.com/elalish/manifold/issues/289 for details about ideas for the algorithm.

## Expected Outcome

Implementation of said algorithm.

## Future Possibilities <!-- optional -->

## Project Properties

### Skills

- C++
- Graph data structure.
- Algorithms.

### Difficulty <!-- easy, medium, hard -->

Hard.

### Size <!-- medium (175h), long (350h) -->

Long (350h)

### Additional Information

* Potential mentor(s): @elalish 
* Organization website: https://manifoldcad.org/
* Communication channels: https://github.com/elalish/manifold/discussions

---

## #94: Creation of an IFC geometry library in IfcOpenShell that uses Manifold

**Labels:** Difficulty: Medium, Lang: C/C++, Project: IfcOpenShell, Size: Medium (175h), Size: Long (350h), Size: Short (90h), GSoC 2026

## Outline

For the past 10 years, IfcOpenShell has had a tight coupling with OpenCASCADE as its only geometry library and OCCT providing the datatypes in the IfcOpenShell C++ APIs.

In IfcOpenShell v0.8 an additional abstraction is introduced over the geometric concepts in IFC (`taxonomy.h`) and the evaluation of such concepts using pre-existing geometry libraries (`AbstractKernel`). 

Also in v0.8, CGAL is introduced as an additional runtime selectable choice besides OpenCASCADE, because of (a) it's extensive set of modules for analysis (e.g convex decomposition, skeleton, ...) and (b) it's arbitrarily robust (and precise) implementation of boolean operations using Nef polyhedra on a number type represents a binary tree of operands taking part in the construction of that number.

Both OpenCASCADE and CGAL are high quality efforts, but quite complex and resulting in fairly large compiled object sizes. This project proposal aims at introducing Manifold as a 3rd geometry library implementation. Manifold is modern, efficient and robust.

https://github.com/elalish/manifold

cc @elalish just fyi.

## Expected Outcome

Another AbstractKernel implementation that uses Manifold to evaluate a small set of geometrical concepts (boolean, extrusion, brep for example) in IFC. Expecting reasonable outcomes on a small building model (such as the Duplex A model) without necessarily resolving all complexities and corner cases encountered in that model.

## Future Possibilities

Comparison between implementations and development of a hybrid composition of these libraries that based on prior inspection picks the most suitable implementation for a specific IfcProduct or representation item. For example, OpenCASCADE will likely still excel at curved surfaces (e.g nurbs), but suffers a monumental performance overhead when ingesting detailed triangular meshes (that are also prevalent in IFC) due the overheads of it BRep data model.

### Additional Information

* Potential mentor(s): Thomas Krijnen (aothms)

---

## #93: Turn BlenderBIM into a client for remote BIM-collaboration on existing OpenCDE-API-server with a graph backend

**Labels:** Difficulty: Hard, Lang: Python, Project: IfcOpenShell, Size: Long (350h), Lang: Cypher, GSoC 2026

## Outline

The project aim is to turn BlenderBIM into a client for remote BIM-collaboration and a client for remote BIM-model-sharing through a Common Data Environment (a CDE working as BIM/IFC-server) using the already developed OpenCDE API server and the OpenCDE API specifications provided by buildingSMART: BCF API and Documents API.

OpenCDE API:s are open standards. This project will hence enable usage of BlenderBIM as a client on other BIM-servers that implements the OpenCDE API:s.

## Details

An OpenCDE API server that implements all buildingSMART OpenCDE API:s (BCF API, Documents API and Foundation API) has been developed in python and the FastAPI framework. Solibri Office was used as a client for testing this server software during development.

The code of the OpenCDE server is located in the IfcOpenShell repository here: https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.7.0/src/opencdeserver

The OpenCDE API:s is a set of open API-specifications provided by buildingSMART. https://github.com/buildingSMART/OpenCDE-API

- BIM Collaboration Format (BCF) API is used for collaboration on shared BIM models through a remote BCF-server. BCF API has the same purpose as BCF XML (which is a file format) but the difference is that the data is communicated as JSON through a BCF-server, instead of sending XML-files. https://github.com/buildingSMART/BCF-API
- Documents API is used communication between a client and a CDE (acc. ISO 19650-1). The purpose is a common data environement for sharing models, documents et.c. https://github.com/buildingSMART/documents-API
- Foundation API is used for authentication et.c. and must be implemented by any client or server that implements anyone of the other two OpenCDE API:s. https://github.com/buildingSMART/foundation-API

To summarize: The model (the IFC data) will normally be shared to the server using Documents API, and downloaded form the server using Documents API. BCF API can be used for remote collaboration on the models located on the server et.c.

The purpose of the open API specification is to enable independent development of clients and servers that can communication with eachother. A server has already been developed and shared as open source on IfcOpenShell. However, at the moment there is no open source client with a graphical user interface for the OpenCDE API:s. A python library for BCF API communication is available: https://pypi.org/project/bcf-client/.

The aim of this project is to turn BlenderBIM into a OpenCDE-client (a client that already have BIM-capabilities) that can communicate remotely with (and make use of) the existing open source OpenCDE-server on: https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.7.0/src/opencdeserver

An add-on for GIT-collaboration have already been developed:
- https://blenderbim.org/docs/users/git_support.html
- https://www.youtube.com/watch?v=cJZhSCSSWdA

Collaboration using Documents API and BCF API is just another way of c

*[truncated]*

---

## #91: Geometry Verification and Validation GUI in Qt (AI Project)

**Labels:** Project: BRL-CAD, Difficulty: Easy, Difficulty: Medium, Lang: C/C++, Size: Medium (175h), Size: Long (350h), GSoC 2026

## Outline

Help develop a new GUI application that checks geometry for common issues and/or helps fix them. 

## Details

A new GUI is in prototype development (built on Arbalest) that checks geometry files for common verification and validation (V&V) issues such as topology errors, solidity errors, and more.  It's very much an experimental work in progress and we'd like your help to make it complete.  The overarching goal of this effort is to extend our prototype in a significant way, either improving usability, checking for more issues, improving the Qt GUI infrastructure integration, integrating workflow(s) for review and repair, or leveraging AI to identify and/or fix issues.

## Expected Outcome

You will propose a complete project description that identifies the specific objectives you'll aim to achieve.  It's expected that you'll leverage the previous work (talk with us to get access to those materials).  The proposal should identify 3-10 primary objectives that are researched and specific, starting with our previous effort.

We essentially want a tool that "compiles" geometry reporting warnings and errors for issues encountered, akin to compiling source code in Visual Studio or Eclipse.  There are questions of application architecture to resolve (e.g., whether to extend 'arbalest', integrate 'qged', integrate 'gist', etc).  We want the tool to be graphical and interactive.  We want it to have the ability to generate reports for auditing.  Some of those capabilities exist in isolation, but none exist as a tool tailor-made for 3D geometry V&V.

## Future Possibilities <!-- optional -->

This is a long term priority project with future possibilities in:
- GUI infrastructure
- AI integration
- geometry healing and repair workflows
- geometry auditing
- geometry standards development

### Skills
Qt, C/C++

### Difficulty <!-- easy, medium, hard -->
Easy or Medium depending on the objectives

### Size <!-- medium (175h), long (350h) -->
long (350h) preferred, but medium (175h) also possible

### Additional Information

* Potential mentor(s): [Sean Morrison](mailto:devs@brlcad.org)
* Organization website: https://brlcad.org
* Communication channels: https://brlcad.zulipchat.com
* https://brlcad.org/design/v&v/

---

## #90: Neural Rendering (AI Project)

**Labels:** Project: BRL-CAD, Difficulty: Hard, Lang: C/C++, Size: Long (350h), GSoC 2024

## Outline
Use neural net during ray tracing as an acceleration method.

## Details

Ray tracing involves computationally expensive calculations and geometry with varying degrees of complexity.  The idea for this project is to use neural networks during 3D rendering as an acceleration method.

This work is intended to build on research AMD presented in 2023 High Performance Graphics (Fujieda et. al) and later worked on in BRL-CAD by Texas A&M students.  The general idea is to train a neural net on a model that is otherwise expensive to render (e.g., a NURBS model or complex hierarchical model), then use that neural net for ray intersection queries.  The hypothesis being explored is whether neural nets can be leveraged for arbitrary shot line queries, accurately and more efficiently than via direct computation.

## Expected Outcome

The expected outcome is subject to discussion but probably involves a suite of performance testing, and integration of a trained neural net with BRL-CAD ray tracing.

## Project Properties

AI/ML, neural networks, ray intersection testing, high performance graphics

### Skills
C/C++

### Difficulty <!-- easy, medium, hard -->
Hard

### Size <!-- medium (175h), long (350h) -->
long (350h)

### Additional Information

* Potential mentor(s): [Sean Morrison](mailto:devs@brlcad.org)
* Organization website: https://brlcad.org
* Communication channels: https://brlcad.zulipchat.com
* https://brlcad.org/design/neural/

---

## #88: Blender UI / integration with voxelisation toolkit software

**Labels:** Difficulty: Medium, Lang: Python, Project: IfcOpenShell, Size: Medium (175h), GSoC 2026

## Outline

There is software known as the [Voxelisation Toolkit](https://github.com/opensourceBIM/voxelization_toolkit) (`pip install voxec`). It converts the 3D model into voxels (e.g. 3D cubes that represent geometry), analyses and transforms those voxels, and outputs statistics (e.g. distance between voxels, etc).

![Image](https://github.com/user-attachments/assets/c346cb17-c894-425e-8cc8-36bc9b2192dc)

![Image](https://github.com/user-attachments/assets/1ebe2874-9e8e-4080-bbf9-c7ae91a1464b)

Voxels are super cool and can be used to calculate head heights, resolve complex non-manifold geometry, egress distances, or concrete formwork areas and strutting distances, and air volume for mechanical calculations. All of this stuff is useful for engineers and construction professionals.

This project is to add a UI in Blender to start making this general purpose analysis tool available to non-programmers.

## Details

You will be expected to design an interface for the voxelisation toolkit, prepack some simple recipes, and write scripts that take the output (currently visualised as images or plots) and instead visualise the results in 3D by generating 3D coloured meshes that represent the output.

## Expected Outcome

 1. Bundle the voxelisation toolkit software with Blender.
 2. A UI to execute the voxelisation toolkit.
 3. Simple presets to run the toolkit.
 4. Visualise the output of the voxelisation analysis as a 3D coloured mesh.

## Future Possibilities <!-- optional -->

Bundle scripts for common usecases, like formwork calculation, air volume calculation, or external / internal metadata addition.

## Project Properties

### Skills

 - Python

### Difficulty <!-- easy, medium, hard -->

Medium

### Size <!-- medium (175h), long (350h) -->

Medium to Long

### Additional Information

* Potential mentor(s): Dion Moult, Thomas Krijnen
* Organization website: https://blenderbim.org http://ifcopenshell.org
* Communication channels: https://osarch.org/chat

---

## #86: Features for CG artists to visualise beautiful IFC models in Blender

**Labels:** Difficulty: Easy, Difficulty: Medium, Lang: Python, Project: IfcOpenShell, Size: Medium (175h), Size: Long (350h), GSoC 2026

## Outline

The architecture, engineering, and construction industry creates 3D models of buildings. These models are generally quite poor and do not contain any textures, lighting, or high quality objects that are suitable for 3D rendering. They often hire artists to help create beautiful renders of their designs.

This project will build utility functions and workflows to easily get beautiful pictures of 3D models.

## Details

3D artists typically do the following steps to make a 3D model look beautiful. They:

 1. Set camera angles with specific camera settings, with "clay" (e.g. all white colours) materials.
 2. Add lights and sun / sky settings.
 3. Add simple colours and textures.
 4. Remodel low quality geometry
 5. Add new objects (e.g. entourage) to decorate the scene, like trees, grass, people, extra furniture, walruses, shrimp, etc.
 6. Set common compositing and post processing rules

You will use the Blender Python API to set simple presets for most of these steps to allow less skilled artists to quickly setup renders. You will also setup a workflow to guide artists on how to organise their files relative to the IFC model and keep the IFC model separate so that when the IFC model is changed, the artists doesn't need to start from scratch or play spot the difference.

**You do not need to be an expert in 3D modeling or CG visualisation or rendering**. You will be taught what type of settings and options are appropriate for presets and the details of the workflow. However, you will be expected to automate that detail (every aspect of the Blender settings can be set using Python trivially).

You will also be expected to create a Blender interface to interact with the settings, e.g. a button to add camera, a button to set a preset sky, etc.

## Expected Outcome

Note: scope is flexible and you may achieve less or more or different to the below:

 1. A graphical interface in Blender that relate to the 6 steps above
 2. Buttons to add cameras, set common camera aspect ratios and settings. Buttons to add common types of lights, set sun angles and sky settings with bundled HDRI textures.
 3. Buttons to add simple material presets.
 4. Buttons to mark an object to be replaced by another
 5. A few preset assets using Blender's built in asset tools to drag and drop in entourage.

## Future Possibilities <!-- optional -->

## Project Properties

### Skills

 - Python (definitely required!)
 - Artistic sense (do you like 3D graphics? rendering?) If you have ever rendered a 3D scene before, this is the project for you!

### Difficulty <!-- easy, medium, hard -->

Easy to Medium

### Size <!-- medium (175h), long (350h) -->

Medium to Long

### Additional Information

* Potential mentor(s): Dion Moult
* Organization website: https://blenderbim.org http://ifcopenshell.org
* Communication channels: https://osarch.org/chat

---

## #84: Implement 3D mesh offset

**Labels:** Difficulty: Hard, Lang: C/C++, Size: Long (350h), Project: Manifold, GSoC 2025, GSoC 2026

## Outline

Implement efficient 3D mesh offset, instead of using minkowski sum with high resolution spheres. (https://github.com/elalish/manifold/issues/192)

## Details

3D mesh offset is a useful feature that many users asked for, but is difficult to implement efficiently. Many users use minkowski sum with sphere to perform positive offset, but this can be very slow due to the need for exact convex decomposition.

Our approach will only work for positive offset, negative offset can be implemented by performing additional mesh boolean operations, so this is not an issue. The approach has four phases:

1. Figure out all pairs of faces that do not share any vertex and may overlap after offsetting. (let's call them conflict pairs)
2. Cut the mesh in a way such that for each part, no two faces are in the same conflict pair. (decomposition step, requires monte carlo tree search)
3. Perform the positive offset on each part, using a modified algorithm from [Offset Triangular Mesh Using the Multiple Normal Vectors of a Vertex](https://www.cad-journal.net/files/vol_1/CAD_1(1-4)_2004_285-291.pdf). Note that we need to figure out how to blend the surfaces for smooth results.
4. Union the parts.
## Expected Outcome

A fast 3D mesh decomposition algorithm!

## Project Properties

### Skills

- C++
- Graph data structure.
- Algorithms.

### Difficulty <!-- easy, medium, hard -->

- Hard.

### Size <!-- medium (175h), long (350h) -->

- Long.

### Additional Information

* Potential mentor(s): @elalish @pca006132 @zalo
* Organization website: https://manifoldcad.org/
* Communication channels: https://github.com/elalish/manifold/discussions

---

## #71: Physically-Based Rendering (PBR) advanced shaders

**Labels:** Project: BRL-CAD, Difficulty: Medium, Lang: C/C++, Project: Appleseed, GSoC 2026

## Outline

Get BRL-CAD physically-based rendering working with advanced shaders.

## Details

BRL-CAD recently integrated with Appleseed which provides physically-based rendering.  It's presently a command-line renderer called 'art'.  For art rendering to work, a shader and colors are specified on geometry.  BRL-CAD has preliminary support for material objects including OSL shaders and MaterialX shaders in art, however their support has only been tested with basic shaders such as the Disney Principled Shader.  It's hard-wired to single-file shaders.

## Expected Outcome

The goal of this task will be to make art read and work with any OSL or MaterialX shader networks, including ones using texturing, emission, subsurface scattering, etc. applied to BRL-CAD geometry.

## Project Properties

### Skills

- Decent C/C++ skills
- Some basic familiarity with PBR.
- Basic familiarity with shaders.

### Difficulty <!-- easy, medium, hard -->

medium

### Size <!-- medium (175h), long (350h) -->

long

### Additional Information

* Potential mentor(s): [Sean Morrison](mailto:devs@brlcad.org)
[Erik Greenwald](mailto:devs@brlcad.org)
* Organization website: https://brlcad.org
* Communication channels: https://brlcad.zulipchat.com

---

## #70: Robust CSG Boolean Evaluation  (a.k.a. Robust Facetization for Geometry Export)

**Labels:** Project: BRL-CAD, Difficulty: Hard, Lang: C/C++

## Outline

Make CSG Boolean evaluation work 100% of the time!

## Details

Central to BRL-CAD's geometric representation is the ability to evaluate Constructive Solid Geometry (CSG) Boolean expressions on geometry (i.e., "UNION", "INTERSECTION", and "SUBTRACTION").  There are many possible techniques but BRL-CAD does not yet have an implementation that reliably works all the time except for ray tracing which is robust and numerically deterministic.

Your goal will be to implement a new/unexplored method that will always work for evaluation to an explicit surface geometry representation (e.g., NURBS or polygonal mesh).  This can be something based on any existing method including BSP-based methods in polygonal space, intermediate evaluation in voxel space, interval arithmetic, NURBS evaluation, error tracking methods, or simply re-implementation an existing method (e.g., Weiler’s n-manifold method) with exhaustive unit testing.

For example, OpenVDB has a boolean evaluation method implementation that works in voxel space.  One could create an evaluator that voxelizes BRL-CAD geometry using ray tracing (which is 100% reliable), evaluates in OpenVDB, and then converts to polygons.

Alternative example, BRL-CAD has NURBS boolean evaluation logic that works some of the time, but hasn't been extended to cover all cases of surface-surface intersection.  One could create a test suite that identifies all configurations and their current status, and work towards resolving failures one by one.

Yet another example, BRL-CAD has an implementation of n-manifold geometry boolean evaluation.  You could work on re-implementing the boolean evaluation from scratch with an eye towards unit testing and performance.

## Expected Outcome

Robust export of geometry to triangle mesh format using some method that reliably works every time.

## Future Possibilities <!-- optional -->

- Expanded unit testing, coverage testing.
- Accelerate boolean evaluation on the GPU.
- Create an online conversion service.

## Project Properties

### Skills

C/C++

### Difficulty <!-- easy, medium, hard -->

hard

### Size <!-- medium (175h), long (350h) -->

long (350h)

### Additional Information

* Potential mentor(s): [Sean Morrison](https://github.com/opencax/GSoC/devs@brlcad.org)
* Organization website: https://brlcad.org
* Communication channels: https://brlcad.zulipchat.com

---

## #69: Improve FreeCAD Hidden Line Removal

**Labels:** Difficulty: Hard, Lang: C/C++, Project: IfcOpenShell, Size: Long (350h), GSoC 2026

## Outline
FreeCAD's Technical Drawing module (TechDraw) relies heavily on the OpenCascade Hidden Line Removal algorithms.  These algorithms can be very slow, do not provide progress reporting and do not provide any linkage between the input shape and the output.

## Details
The TechDraw module provides projections, section views and detail views of 3D model components and assemblies developed in FreeCAD modules such as Part, PartDesign and Draft.

## Expected Outcome
a) develop new code for projecting shapes and creating the geometry for technical drawings. 
-or-
b) modify the existing OpenCascade code as an enhancement.

## Project Properties
Both OpenCascade and TechDraw are written in C++.

### Skills
The student should have a good knowledge of C++ and be familar with graphics topics such as the painters algorithm, face detection and hidden line removal.
Knowledge of technical drawing standards and previous exposure to Qt will be helpful.  Familiarity with OpenCascade is a definite plus.

### Difficulty <!-- easy, medium, hard -->
Hard

### Size <!-- medium (175h), long (350h) -->
long

### Additional Information

*  Potential mentor(s): wandererfan
*  Organization website: https://freecadweb.org
*  Communication channels: https://forum.freecadweb.org

---

## #67: Continuation of a prior BRL-CAD GSoC effort

**Labels:** Project: BRL-CAD, Difficulty: Easy, Difficulty: Medium, Lang: C/C++, Lang: Python, Lang: Javascript, Size: Medium (175h), Size: Long (350h), Project: Appleseed, GSoC 2026

## Outline

BRL-CAD has been participating in GSoC for over 10 years with nearly 100 students!  Any past accepted projects can be submitted as a continuation project.
  
## Details

You can find all past participants [documented on BRL-CAD's wiki](https://brlcad.org/wiki/Google_Summer_of_Code) by selecting a given year (e.g., [2018](https://brlcad.org/wiki/Google_Summer_of_Code/2018)).  Even the most successful and completely integrated projects have room for improvement!  If any of those past efforts for any prior year sound very interesting to you, you can propose a continuation effort for it.

Of course, you will need to research the prior effort to determine the status of the work, whether code was integrated or is sitting pending integration in a patch, whether it's functional or was in an intermediate state, etc.  You'll also want to come [chat with us on Zulip](https://brlcad.zulipchat.com) to make sure there is mentoring support for it, but there usually is if you're passionate and independently productive.

For your proposal, note that it's a continuation effort.  Explain what you are doing and how it relates to the prior effort.  It's strongly recommended that your development plan focus on production-quality integration aspects such as making sure there are no usability or user experience (UX) issues, no build integration issues, that testing is covered adequately, and with focus on UX.

## Expected Outcome

The expected outcome of a continuation effort is new capability and features that are "complete", integrated, bug-free, and issue-free, in the hands of users.  This means your project covers all vertical integration aspects of development integration including build system and usability / UX concerns.  Not prototyped.  Not simply rewritten or re-attempted.

If the prior effort was integrated, your outcome will be specific polish, adaptiveness, and robustness improvements.

If the prior effort was not integrated, your outcome will be issue-free integration that addresses prior issues preventing integration (which will require research and understanding on your part).

## Project Properties

### Skills

This varies greatly by continuation.  There are continuation projects for C/C++, Python, Javascript/Node.js, Tcl/Tk, OpenCL, OpenGL, Qt, GPGPU, and more.

### Difficulty <!-- easy, medium, hard -->

Varies.

### Size <!-- medium (175h), long (350h) -->

You are welcome to scope your project medium (175h) or long (350h) depending on the objectives and development scope.

### Additional Information

* Potential mentor(s): Morrison (contact [devs@brlcad.org](mailto:devs@brlcad.org))
[Erik Greenwald](mailto:devs@brlcad.org)
* Organization website: https://brlcad.org
* Communication channels: https://brlcad.zulipchat.com

---

## #66: Integrate STEPcode into IfcOpenShell

**Labels:** Difficulty: Hard, Lang: C/C++, Project: IfcOpenShell, Size: Medium (175h), Size: Long (350h), GSoC 2026

## Outline

IfcOpenShell is a software library for IFC building models. This open standard IFC is largely based on the STEP family of standards, ISO 10303. There is a well-known parser and code generator for that called STEPcode. IfcOpenShell currently uses it's own parser for the model files (C++) and the schema files (Python) but would like to offer support for STEPcode in the means of an additional parser that can be selected at runtime.

## Expected Outcome and future Possibilities

Advantages of completing this project include:

- Express schema parsing in C has advantages with respect to latebound (selecting a novel schema at runtime) parsing (which is now only possible in Python and then doesn't support geometry processing)
- Conformance to the SDAI standard to offer a uniform interface for access to the parser and model
- Consolidated effort to implement some of the remaining functionality such as support for imperative code embedded in the schema file (where rules, functions, and derived attributes)

## Project Properties

### Skills

C++

Parsing

### Difficulty <!-- easy, medium, hard -->

Medium

### Size <!-- medium (175h), long (350h) -->

Size

Applicants can choose to approach this proposal either as a Medium-sided project or Long.

#### Medium (175h)

The applicant focuses on integrating STEPcode, predominantly intended to evaluate its usage and advantages. The result can be a demonstrator where the current parser is simply replaced without any effort in a generalized effort and runtime selection mechanism of the parser.

#### Long (350h)

The applicant aims to provide a runtime selection mechanism of the parser and general code architecture to facilitate both parsers.

### Additional Information

Potential mentor(s): Thomas Krijnen @aothms

Organization website: http://ifcopenshell.org/

Communication channels: https://sourceforge.net/p/ifcopenshell/discussion/

---

## #65: Implement AP242 STEP geometry importer for BRL-CAD

**Labels:** Project: BRL-CAD, Difficulty: Hard, Lang: C/C++, Size: Medium (175h), Size: Long (350h), GSoC 2026

## Outline

Implement a geometry importer for the [ISO 10303 STEP](https://en.wikipedia.org/wiki/ISO_10303) AP242 standard.

## Details

BRL-CAD has geometry import support for STEP AP203 (v1), but AP242 has emerged as its industry replacement.  This project entails implementing as comprehensive import support as possible in BRL-CAD.

In order to track implementation progress and manage development risk, you will need to track [implementation coverage](https://www.cax-if.org/cax/vendor_info.php?file_id=3&comp_id=0) by setting up a dashboard similar to what is used by the [CAx-IF](https://www.cax-if.org/cax/vendor_info.php) -- it can be a simple text file or web page.

Existing conversion support can be examined for AP203 and other formats in BRL-CAD's repository under [src/conv/step](https://github.com/BRL-CAD/brlcad/tree/main/src/conv/step)

## Expected Outcome

New AP242 importer that converts STEP entities into BRL-CAD's .g geometry file format.

## Future Possibilities <!-- optional -->

AP242 export support...

## Project Properties

### Skills

C/C++
STEPcode

### Difficulty <!-- easy, medium, hard -->

Hard.

### Size <!-- medium (175h), long (350h) -->

This project can be scoped medium (175h) or long (350h) depending on your familiarity and expertise, or you can propose a subset of entities in a shorter timeframe (note though that advanced boundary representation entities should be prioritized).

### Additional Information

* Potential mentor(s): Morrison (contact devs@brlcad.org)
* Organization website: https://brlcad.org
* Communication channels: https://brlcad.zulipchat.com

---

## #52: BRL-CAD Python bindings

**Labels:** Project: BRL-CAD, Difficulty: Easy, Difficulty: Medium, Lang: C/C++, Lang: Python, Size: Medium (175h), Size: Long (350h), GSoC 2026

## Outline
Implement bindings for the BRL-CAD functionality to Python programming language

## Details
There are long time on-going efforts to wrap BRL-CAD functionality with python code, e.g.
* https://github.com/kanzure/python-brlcad
* https://github.com/nmz787/python-brlcad-tcl

These projects are however still in early development stages.

## Expected Outcome
A Python module which can read and write BRL-CAD databases, and provide access to their contents to read, create, and modify the objects.

## Project Properties

### Skills
* C/C++
* Python

### Difficulty
This project may be of easy or medium difficulty, depending on your familiarity and expertise.

### Size
This project can be scoped medium (175h) or long (350h), depending on the amount of functionality you want to include.

### Additional Information
* Potential mentor(s):
[Daniel Rossberg](mailto:devs@brlcad.org)
[Sean Morrison](mailto:devs@brlcad.org)
* Organization website: https://brlcad.org
* Communication channels: https://brlcad.zulipchat.com

---

## #42: Scripts for generating simple animations (e.g. appear / disappear, bounce, appear left to right, fade in from above, etc)

**Labels:** Difficulty: Easy, Lang: Python, Project: IfcOpenShell, GSoC 2026

<!-- template for GSoC project ideas
     feel free to remove optional sections when you have no content for them
     and remove comments before submitting
-->
## Outline

Often, construction firms need to visualise animations of construction sequencing. A project timeline will be created, and related to individual model elements. For example, when a concrete slab is poured, it is linked to a 3D object called a slab. We need the ability to automatically generate animations from Blender where objects appear / disappear in various different ways when they start / end their task in the project timeline. The systems for describing project timelines is already in place, so now we need a little animation generator!


## Details


## Expected Outcome

A series of small scripts that take objects and can automatically animate the visibility, locations, or staggered appearances of building elements, as well as sub elements, and basic scripts that correlate real world time to animation frames, and frames per second, and generate an animated timeline bar in various styles.

## Future Possibilities <!-- optional -->

This animation system can be then used from BIM models either in Blender, FreeCAD, or via other software altogether, so it has quite a large impact on the ecosystem.

### Skills

 - Basic knowledge of the principles of animation (keyframing)
 - Basic Blender animation (you can do some tutorials and get up to speed pretty quick)
 - Python
 - Artistic sense! We should offer beautiful and elegant animations!

### Difficulty <!-- easy, medium, hard -->

Easy

### Additional Information

* Potential mentor(s): Dion Moult
* Organization website: https://ifcopenshell.org
* Communication channels: https://community.osarch.org , ##architect on Freenode , and https://github.com/IfcOpenShell/IfcOpenShell/issues

---

## #32: NURBS Editing Support in BRL-CAD

**Labels:** Project: BRL-CAD, Difficulty: Medium, Difficulty: Hard, Lang: C/C++, Size: Long (350h), GSoC 2026

## Outline
Implement the prerequisites for NURBS editing in BRL-CAD's GUIs

## Details
BRL-CAD has support for raytracing of NURBS surfaces implemented, but they are handed over as BLOBs to the openNURBS library.  Beyond basic operations such as rotation and translation, the BRL-CAD core has no ability to edit them.  This project would implement support for editing NURBS curves and surfaces in the BRL-CAD core, thus creating the prerequisites to handle them with higher level (i.e. GUI) tools.

See this task's description in former GSoCs for some more information: https://brlcad.org/wiki/NURBS_Editing_Support

The key-feature would be to have ged command(s) that lets you build NURBS objects from scratch.  This could be done by having a declarative ASCII description of these entities and/or wrapping the openNURBS library by a scripting language.

Describe in your proposal which approach you want to use and why.  You may let inspire you by solutions in other programs:
* NURBS-Python: https://github.com/orbingol/NURBS-Python
* Blender: https://blender.stackexchange.com/questions/7020/create-nurbs-surface-with-python
* Web3D: https://www.web3d.org/x3d/content/examples/Basic/NURBS/
* 3DSMax/Maya: https://help.autodesk.com/view/3DSMAX/2016/ENU/?guid=__files_GUID_75CD4DE9_8024_4E25_B147_0A0EC8B10031_htm
* Ayam: http://ayam.sourceforge.net/docsdraft/ayam-6.html

## Expected Outcome
Implementing the necessary logic for NURBS handling in librt, libbrep, and libged

## Future Possibilities
Implementing a visual NURBS editor in a BRL-CAD GUI (mged, Archer, Arbalest)

## Project Properties
### Skills
* C/C++

### Difficulty
medium

### Size <!-- short (175h), long (350h) -->
long (350h)

### Additional Information
* Potential mentor(s): [Daniel Rossberg](mailto:devs@brlcad.org), [Sean Morrison](mailto:devs@brlcad.org)
* Organization website: https://brlcad.org
* Communication channels: https://brlcad.zulipchat.com

---

## #27: New BRL-CAD GUI

**Labels:** Project: BRL-CAD, Difficulty: Medium, Lang: C/C++, Size: Medium (175h), Size: Long (350h), GSoC 2026

## Outline

Develop further the new GUI for BRL-CAD!

## Details

BRL-CAD has two main graphical applications called 'mged' and 'archer' which look like they were developed in the 80's and 90's respectively (because they were).  We need a modern GUI, ideally using Qt.

This new GUI will need to leverage our existing libraries in a big way.  This includes the C++ core interface in MOOSE (see https://github.com/BRL-CAD/MOOSE) and LIBGED (see src/libged).  The latter is basically all commands available to both mged and archer.

During past GSoCs an amazing start was made with [arbalest](https://github.com/BRL-CAD/arbalest). Based on this, the development of a GUI called 'qged' (see src/qged) was started, which you should include in your considerations too. This program implements the traditional BRL-CAD workflow under a modern Qt-based user interface.

You may propose a complete different approach, but we recommend to use arbalest as starting point for your work.  Which additions would you like to program in this years GSoC?  You can use the results of the former prototype CAD GUI Google Code-in tasks (http://brlcad.org/gci/data/uncategorized/, search for CAD_GUI there) for inspiration.

Keep your proposal lean and simple.  The main emphasis should be on adding features and/or improvements to our next generation GUI.
## Expected Outcome

An improved BRL-CAD GUI.

## Project Properties

### Skills

* C/C++
* Qt

### Difficulty <!-- easy, medium, hard -->

medium

### Size

This project can be scoped medium (175h) or long (350h), depending on the amount of functionality you want to include.

### Additional Information

* Potential mentor(s):
[Daniel Rossberg](mailto:devs@brlcad.org)
[Himanshu Sekhar Nayak](mailto:devs@brlcad.org)
[Sean Morrison](mailto:devs@brlcad.org)
* Organization website: https://brlcad.org
* Communication channels: https://brlcad.zulipchat.com

---

## #26: Online Geometry Viewer (OGV)

**Labels:** Project: BRL-CAD, Difficulty: Hard, Lang: C/C++, Lang: Javascript, Size: Medium (175h), Size: Long (350h), GSoC 2026

## Outline
Write a proposal that leverages a rewrite of the existing application in the latest tech stack for the frontend and backend.

## Details
We have been working on [OGV](https://github.com/BRL-CAD/OGV) for over many years. It started with PHP and then was revamped to meteor.js. We want to focus on the backend of OGV, making sure it works properly, converts the models properly, and basically finish a 1.0 version of OGV so we can launch it for the masses! For that, we are planning to change the legacy backend to be rewritten along with the frontend.

You can use any tech stack (react, vue) for the frontend and node, and  C/C++ for the backend. We faced some problems like removing certain deprecated dependencies and adding new features with Meteor. We are planning to port the application and add all specified features.

For more detailed specifications please check ([link](https://github.com/BRL-CAD/OGV/wiki/Technical-Specification-Document-(TSD))). Please make sure to read the note.

### Possible New Features
- Integrating BRL-CAD **[GCV(Geometry Conversion Vocabulary)](https://github.com/BRL-CAD/brlcad/tree/main/src/libgcv)** to add support for more file formats like .stl, .obj, and .3dm.
- Automated Conversion for Web Display. Convert uploaded files automatically into polygonal formats for web visualization. Ensure smooth rendering and compatibility with web-based 3D viewers.
- Implementing a Model Repository-based project architecture for storing and downloading 3d models.
- Conduct a full STIG compliance audit (Security Technical Implementation Guide), which involves ~200+ security checks.
  - Run security scans using OWASP and Dependency-Check, addressing any reported vulnerabilities.

However, you don't have to limit yourself to those ideas. Some of them are shared here in [detail](https://github.com/BRL-CAD/OGV/wiki/OGV-Plan). Please make sure to read the note.

### Checklist to write a proposal for OGV
* Download and clone OGV from https://github.com/BRL-CAD/OGV
* **main** branch is cleaned for the new updates.
* To check the legacy version checkout [legacy_meteor_based_version](https://github.com/BRL-CAD/OGV/tree/legacy_meteor_based_version)
* Setup and Run OGV on your local machine.
* Fork OGV repo
* Understand the flow of the existing application
* Talk to mentors
* Choose a list of issues that you would like to solve this summer
* Make a detailed weekly implementation plan
* Share your proposal with your mentors
* Submit it to the GSoC website

## Expected Outcome
You're expected to propose an outcome useful to end-users. That is a broad range of possibilities that will depend on your interests and experience level. For example, you might propose focusing on the backend conversion to triangles for display (C/C++/Node.js). Or you might propose changing the backend to NURBS surfaces (C/C++) and using verbnurb or three.js (Javascript) to display them instead of triangles. Or you might propose keeping the backend the way it is and f

*[truncated]*

---

## #24: Coherent (Faster) Raytracing

**Labels:** Project: BRL-CAD, Difficulty: Hard, Lang: C/C++, Size: Medium (175h), Size: Long (350h), GSoC 2024

## Outline
Utilize cache coherency and parallelization techniques in BRL-CAD's ray tracing pipeline, and demonstrate graphically.

## Details
BRL-CAD has one of the oldest and fastest parallel ray tracing implementations around but we don't currently leverage modern techniques that minimize context switching and data access.  With implicit geometry and constructive solid geometry (CSG) Boolean operations, we also have a very specific set of validation and performance challenges.

Your project is to help make the pipeline more data-coherent using ray bundling, cache-coherent processing, and OpenCL. Currently, the ray tracer evaluates one ray at a time (in parallel).  There is experimental work with OpenCL in a branch.

Your primary objective for this project is to make the ray tracer evaluate groups of rays at a time (e.g., 32x32 "postage stamps") coherently, calculate and demonstrate changes made to performance, and get ray tracing via OpenCL working.  A secondary stretch objective is to demonstrate performance graphically using one of several options we've explored in the past (OSPRay, O3DE, and Qt).

Your proposal should be aware of, improve upon, and/or incorporate previous year efforts:
* [2020 OpenCL GPGPU Raytracing](https://brlcad.org/wiki/Google_Summer_of_Code/2020#OpenCL_GPGPU_Raytracing)
* [2018 Improving Raytracing Performance](http://brlcad.org/wiki/Google_Summer_of_Code/2018#Improving_raytracing_performance)
* [2017 GPU Boolean Evaluation](http://brlcad.org/wiki/Google_Summer_of_Code/2017#GPU_Boolean_Evaluation_for_CSG_Ray-Tracing)
* [2016 GPGPU Support for Boolean Evaluation](http://brlcad.org/wiki/Google_Summer_of_Code/2016#GPGPU_Support_for_Boolean_Evaluation_Used_in_Ray_Tracing)
*  [2015 GPU Accelerated Ray Trace Rendering](http://brlcad.org/wiki/Google_Summer_of_Code/2015#GPU_Accelerated_Ray_Trace_Rendering_for_BRL-CAD)


## Expected Outcome

Demonstrate improved ray tracing performance via bundling and OpenCL.  Demonstrate performance graphically through a prototype interactive GUI (using OSPRay, O3DE, or Qt).

## Project Properties

### Skills

* C/C++
* OpenCL
* Intel Threading Building Blocks (TBB) (optional)
* OSPRay (optional)

### Difficulty

hard

### Additional Information

* Potential mentor(s): [Vasco Costa](mailto:devs@brlcad.org)
* Organization website: https://brlcad.org
* Communication channels: https://brlcad.zulipchat.com/

---

## #14: FreeCAD-BRLCAD integration

**Labels:** Project: BRL-CAD, Difficulty: Hard, Lang: C/C++, Lang: Python, Project: FreeCAD, Size: Long (350h)

This page is dedicated  to the description of the [Google Summer of Code|Google Summer of Code 2019](https://www.freecadweb.org/wiki/Google_Summer_of_Code) project idea of integrating FreeCAD and BRL-CAD.

## Outline

[FreeCAD](https://www.freecadweb.org) and  [BRL-CAD](http://www.brlcad.org) are very complementary applications: BRL-CAD is a powerful engine which could do with a better modeling UI, and FreeCAD has an increasingly vast modeling UI but could make great use of the support for large models that BRL-CAD can offer.

FreeCAD being highly modular, and BRL-CAD having a C/C++ API, building a BRL-CAD module for FreeCAD is totally possible. This way, it would be possible to open BRL-CAD models (that are usually called geometry databases, because they are often made of a collection of models) in FreeCAD, and it would also be possible to use FreeCAD as a modeling tool for BRL-CAD.

This project idea will require a reasonable knowledge of C/C++, and, since it involves two different applications, a versatile mind able to learn quickly and navigate between many different concepts, as they are implemented differently in both applications.

This project would be mentored commonly by both FreeCAD and BRL-CAD developers.

## Details

* Get familiar with how FreeCAD and BRL-CAD work, what are their strengths and limitations, how they differ, how parametric modelling works in both of them
* Successfully compile both applications
* Get familiar with the BRL-CAD API
* Understand how FreeCAD parametric objects (features) are constructed and work, and how the view provider system works. We will basically be constructing FreeCAD view providers around BRL-CAD objects
* Also study the command-line interface tools offered by BRL-CAD, and assess if and how any of these could be put into use
* Implement basic import: Allow to open a BRL-CAD database and display its contents in FreeCAD
* Implement a couple of BRL-CAD-based objects: Or, how to use the FreeCAD modelling tools to produce BRL-CAD objects
* Implement basic saving: How the BRL-CAD-based FreeCAD objects can be saved to a BRL-CAD database, and design a strategy for possible support of other FreeCAD objects

## Expected Outcome

* Documentation. Since this is a large task, that might not fit in a single GSOC project, other people (or yourself) will likely work on this project after the GSOC period ends. They must be able to take on the work where it has been stopped. Also, the first steps of this project will involve a lot of research, that should be made as available as possible to others.
* A basic prototype, that allows to open and visualize BRL-CAD databases in FreeCAD, and shows how modelling and saving BRL-CAD objects can work in FreeCAD

## Future Possibilities

Such an integration could go a very long way, as both applications are very complex, and if the "wedding" works well, new possible fields of use could emerge. Also, we think this kind of inter-project integrati

*[truncated]*

---

## #12: Non-planar printing

**Labels:** Project: Slic3r, Difficulty: Medium, Lang: C/C++

## Outline

Implement techniques for non-planar printing.

## Project Properties

### Skills

* C++

### Difficulty

Medium

## Additional information

* slic3r/Slic3r#3442

---

## #11: Manual support creation

**Labels:** Project: Slic3r, Difficulty: Hard, Lang: C/C++, Lang: Perl

## Outline

Allow users to place and move support pillars by clicking in the 3D GUI.

## Project Properties

### Skills

* C++/Perl

### Difficulty

Medium/Hard

## Additional information

* slic3r/Slic3r#3062

---

## #10: Wireframe printing

**Labels:** Project: Slic3r, Difficulty: Medium, Lang: C/C++

## Outline

Implement the wireframe printing algorithm.

## Project Properties

### Skills

* C++

### Difficulty

Medium

## Additional information

* slic3r/Slic3r#2274

---

## #9: Fix bugs of the Boost.Voronoi library

**Labels:** Project: Slic3r, Difficulty: Medium, Lang: C/C++

## Outline

The good but unmaintained Boost.Voronoi library has a couple minor issues affecting Slic3r's results. Interesting task for learning the Voronoi algorithm and how to troubleshoot a computational geometry issue.

## Project Properties

### Skills

* C++

### Difficulty

Medium

## Additional information

* slic3r/Slic3r#2948

---

## #8: Port the SVGNest library to C++

**Labels:** Project: Slic3r, Difficulty: Easy, Lang: C/C++

## Outline

The SVGNest library provides an algorithm for polygon nesting. It's written in JavaScript and a C++ port of it would improve Slic3r's auto-arrange feature. 

## Project Properties

### Skills

* C++

### Difficulty

Easy

## Additional information

* slic3r/Slic3r#3237

---

## #7: Port the Slic3r GUI to C++

**Labels:** Project: Slic3r, Difficulty: Easy, Lang: C/C++

## Outline

The Slic3r GUI is currently coded in Perl using wxWidgets and our goal is to have it ported to C++. The wxWidgets API is almost identical between Perl and C++, so it's an easy task. There are a couple things where we use the dynamic features of Perl which are trickier and interesting to port.

## Project Properties

### Skills

* C++/wxWidgets

### Difficulty

Easy

## Additional information

---
