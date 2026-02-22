# Project Mesa — Project Ideas

**Source:** https://github.com/mesa/mesa/wiki/GSoC-2026-Project-Ideas
**Scraped:** 2026-02-22T23:28:47.626539

---

Tentative Projects & Mentors

* [Behavioral framework](#behavioral-framework) Size: Medium/Large Mentors: @EwoutH/@quaquel
* [Mesa-Geo Update](#modernizing-mesageo-propertylayer-refactor-aggregationapi-and-visualizationoverhaul) Size: Medium/Large Mentors: @wang-boyu/@jackiekazil
* [Mesa-LLM iteration to push to production](#Mesa-LLMs-iteration-to-push-to-production) Size: Medium Mentors: @colinfrisch/@jackiekazil
* [Meta Agents](#meta-agents) Size: Medium Mentors: @tpike3/@EwoutH
* [Mesa Examples Revival](#reviving-mesa-examples) Size: Small/Medium Mentors: @jackiekazil/@EwoutH

More info:
- [Mesa's Google Summer of Code 2026 guide](/ideas/project-mesa/google-summer-of-code-2026)
- [GSoC 2026 ideas discussion](/ideas/project-mesa/mesa-mesa-discussions-2927)

# Extended descriptions
## Behavioral framework
### Summary
This project evaluates how well Mesa currently supports building agent models based on established behavioral theories. The suggested approach is hands-on: implement example models, document what works and what doesn't, and identify improvements that would help the most users. When similar models exist in other ABM platforms, compare and learn from them.

### Motivation
Many agent-based models need agents with realistic behavioral patterns - animals balancing hunger and fear, people making economic decisions, or entities learning from experience. Theories like Belief-Desire-Intention (BDI), needs-based architectures, and reinforcement learning provide proven frameworks for this. But we don't have a clear picture of how well Mesa supports these patterns today. This project finds out through actual implementation rather than guesswork.

### Historical context
Mesa started with simple discrete time steps but has grown more capable. The DiscreteEventScheduler and DEVSimulator enable flexible timing and event-driven modeling. Recent discussions have explored continuous states ([#2529](https://github.com/projectmesa/mesa/discussions/2529)), tasks with duration and interruption ([#2526](https://github.com/projectmesa/mesa/discussions/2526)),  and a unified behavioral framework ([#2538](https://github.com/projectmesa/mesa/discussions/2538)). Experimental work on observables and signals ([PR #2547](https://github.com/projectmesa/mesa/pull/2547)) adds more building blocks. This project aims to move these discussions forward with practical experience.

### Overall goal
Produce a clear picture of what Mesa does well and where it falls short for behavioral modeling. Capture this in example models, tutorials, and documentation that help current users and guide future development. Optionally, propose and implement focused improvements that benefit multiple behavioral modeling approaches.

### Potential approaches
Pick two or three behavioral theories to explore. For each, build an example model in Mesa and document the experience: What was easy? What needed workarounds? What was genuinely hard? Good candidates include predator-prey with needs-based behavior, market agents using BDI reasoning, or learning agents using reinforcement approaches.

Where comparable models exist in NetLogo, GAMA, Agents.jl, or other platforms, study how they solve the same problems. What can Mesa learn from their approaches?

Based on what you find, you might propose targeted improvements: documentation, utility functions, or new components. Any additions should be justified by your implementation experience and useful across multiple behavioral theories, not just one narrow case.

### Possible outcomes
* Example models as PRs to mesa-examples
* Tutorials showing how to implement behavioral theories in Mesa
* Documentation of what works, what's awkward, and what's missing
* Comparisons with other ABM platforms
* Optionally, PRs introducing broadly useful building blocks for behavioral modeling

### Useful skills
Contributors should have solid Python programming experience and familiarity with object-oriented design patterns. Prior experience with agent-based modeling concepts is valuable, whether through Mesa or other platforms. Interest in behavioral theories from psychology, economics, or artificial intelligence will help in selecting and implementing meaningful examples. Experience with technical writing will support the documentation aspects of the project. Familiarity with other ABM platforms (NetLogo, GAMA, Agents.jl) is helpful for comparison work but not required.

### Getting Started
Read the linked discussions ([#2529](https://github.com/projectmesa/mesa/discussions/2529), [#2526](https://github.com/projectmesa/mesa/discussions/2526), [#2538](https://github.com/projectmesa/mesa/discussions/2538)) to understand current thinking. Explore Mesa's DEVS module and signals work. Try extending Wolf-Sheep with basic needs-based decisions to get hands-on experience. Look at mesa-examples to understand contribution patterns. Think about which behavioral theories interest you and what models would test Mesa effectively. Join the Mesa community on GitHub or chat to refine your ideas.

### Suggested size
- Medium (focused on evaluation & documentation)
- Large (evaluation, documentation and feature implementation)
### Mentors (committed)
- Ewout ter Hoeven (@EwoutH) & Jan Kwakkel (@quaquel)

## Modernizing Mesa‑Geo: PropertyLayer Refactor, Aggregation API and Visualization Overhaul

### Summary

Mesa‑Geo is Mesa's geospatial extension, providing CRS‑aware agents, raster and vector layers and geometry queries. Its current design predates Mesa's modern discrete‑space architecture and stores raster values as per‑cell Python attributes. This project will refactor Mesa‑Geo to follow Mesa's new `PropertyLayer` abstraction for raster data, expose a fluent API for aggregation and random sampling, clarify cell coordinate semantics, and upgrade the visualisation pipeline to Mesa ≥ 3.3. The goal is a faster, more intuitive framework that aligns with Mesa's evolving space model and prepares Mesa‑Geo for future integration.

### Motivation

Mesa‑Geo carries technical debt from its early implementation. Raster data are stored as individual Python attributes rather than vectorised arrays, neighbourhood aggregation is ad‑hoc, and the package duplicates grid logic that Mesa's core has since generalised. Issues [#201](https://github.com/mesa/mesa-geo/issues/201), [#91](https://github.com/mesa/mesa-geo/issues/91) and [#81](https://github.com/mesa/mesa-geo/issues/81) highlight the need for a `PropertyLayer`‑based `RasterLayer` with file I/O helpers and random point sampling; issue [#295](https://github.com/mesa/mesa-geo/issues/295) shows that GeoSpace's visualisation should be updated for Mesa 3.3; and PR [#299](https://github.com/mesa/mesa-geo/pull/299) underscores confusion around coordinate property names. Addressing these themes will align Mesa‑Geo with Mesa’s modern space model, simplify user code and improve performance.

### Historical Context

Mesa‑Geo was first released in 2018 and later expanded in 2022 to provide GIS support for Mesa. It introduced `GeoSpace` for raster/vector layers and `GeoAgent` with CRS‑aware geometries, at a time when Mesa lacked a unified discrete‑space API. Since then Mesa has developed a new space model featuring first‑class `Cell` objects, `CellCollection` views and vectorised `PropertyLayer`s. Mesa‑Geo has not yet adopted these concepts, which leads to duplicated grid code and difficulty keeping up with changes such as the Solara‑based visualisation system in Mesa 3.x. Past issues and PRs mentioned above illustrate interest in aligning Mesa‑Geo with these newer abstractions.

### Overall Goal

Deliver a Mesa‑Geo release that is intuitive and aligned with Mesa's modern space architecture. The project will:

- Replace per‑cell Python attributes with `PropertyLayer` arrays for raster storage, keeping CRS and affine metadata intact.
- Provide convenient APIs for loading and saving raster bands, and for sampling random coordinates within cells.
- Introduce a fluent aggregation API for per‑cell operations, filtering, mapping and neighbourhood statistics on raster data.
- Clarify coordinate semantics by introducing explicit properties such as `cell.xy`, `cell.grid_pos` and `cell.rowcol`, and emitting deprecation warnings for legacy names.
- Migrate GeoSpace and raster rendering to Mesa's `SpaceRenderer`/Solara backend to ensure compatibility with Mesa 3.3 and later.
- Explore, as time permits, how Mesa‑Geo can plug into Mesa's upcoming multi‑space design and position/index translation hooks.

### Expected Outcomes

#### Core Improvements

- **Property‑Layer RasterLayer:** Refactor `RasterLayer` to store each band as a `PropertyLayer`, with methods to add/remove bands and convert existing raster cells into property descriptors.

- **Raster I/O & Sampling:** Provide `RasterLayer.from_file` and `RasterLayer.to_file` using rasterio or rioxarray (optional dependency) and implement `get_random_coord(cell)` for random sampling within a cell's geometry.

- **Aggregation API:** Extend Mesa's `CellCollection` patterns to raster layers, with functions such as `do(fn)` for per‑cell operations, `select(predicate)`, `map(fn)` and `aggregate(func, by=None)` to compute statistics over groups or neighbourhoods.

- **Coordinate Semantics:** Add Cell properties such as `cell.xy`, `cell.grid_pos` and `cell.rowcol`, emit deprecation warnings for `cell.pos` and `cell.indices`, and document the migration path.

- **Visualisation Overhaul:** Update Mesa-Geo visualization to work reliably with Mesa's SolaraViz environment and current rendering expectations. Applicants are encouraged to propose a good GeoSpace visualization architecture and API. The proposal should ideally specify (1) the public API exposed to users, (2) how it plugs into `SolaraViz`, and (3) how raster + vector layers and agents are rendered.

   Note: The solution does not have to mirror Mesa's `SpaceRenderer` API; it only needs to integrate cleanly with SolaraViz's rendering system.

#### Enhancements & Stretch Goals

- **Alternative Grids:** Investigate irregular or hexagonal grid support, and test integration of H3 or axial coordinate systems with property layers and the aggregation API.

- **Integration Proof of Concept:** Prototype a `GeoSpace` redesign that follow https://github.com/mesa/mesa/discussions/2585#discussioncomment-11732488.

#### Documentation

- Update Mesa‑Geo documentation to describe the new raster API, aggregation methods and coordinate properties.

- Provide tutorials showing how to load raster bands from files, visualise them with `SpaceRenderer`, and implement a simple cellular automaton using the aggregation API.

#### Testing & Quality Assurance

- Create unit tests for the refactored `RasterLayer`, including property‑layer creation, coordinate conversions, file I/O and deprecation warnings.
- Add tests for aggregation and random sampling functions to ensure correctness and reproducibility.
- Integrate visualisation tests into Mesa‑Geo's CI to verify compatibility with Mesa ≥ 3.3 and maintain performance benchmarks.

### **Skills Required**

**Required:**

- Strong Python programming and experience with object‑oriented design.
- Knowledge of GIS concepts such as CRS, affine transforms and raster vs vector data.
- Experience with Mesa and/or Mesa‑Geo, including the new discrete space and PropertyLayer APIs.
- Comfort with NumPy for vectorised operations.

**Preferred:**

- Experience using rasterio, rioxarray or xarray for raster I/O and CRS handling.
- Familiarity with Shapely and GeoPandas for geometric operations.
- Exposure to Solara or Altair for interactive web visualisation.

### Project Size

Medium/Large

### Mentors

- **Primary:** Boyu (@wang-boyu)
- **Backups:** Jackie (@jackiekazil)

### **Getting Started**

1. Review issues [#201](https://github.com/mesa/mesa-geo/issues/201), [#91](https://github.com/mesa/mesa-geo/issues/91) and [#81](https://github.com/mesa/mesa-geo/issues/81) and PR [#299](https://github.com/mesa/mesa-geo/pull/299) to understand the motivations.
2. Study Mesa's discrete space and `PropertyLayer` implementations (`mesa.discrete_space`, `CellCollection`, `AgentSet`) to inform the aggregation API design.
3. Experiment with `SpaceRenderer` using Mesa's tutorials to understand how property layers are rendered.
4. Refactor a small raster model (e.g. a land‑use cellular automaton) to use `PropertyLayer` manually; note challenges and open questions.

## Mesa LLMs iteration to push to production 

### Summary
Mesa-LLM integrates Large Language Models (LLMs) into the Mesa framework, allowing for agents with complex cognitive architectures and communication capabilities. This project aims to stabilize the library as well as enhance its features, documentation, and *ease of use* to make it a reliable tool for researchers and developers.

### Motivation
Generative Agents represent a paradigm shift in ABM. However, implementing them currently requires significant  coding to handle API connections, prompt history, and parsing text outputs into simulation actions. Mesa-LLM needs to bridge the gap between LLM text generation and the deterministic logic required to obtain reliable results in an ABM simulation.

### Historical Context
Mesa-LLM was created as a 2025 GSoC project to address the growing demand for "smart" agents within Mesa. Initial ideas were initiated in [Discussion #2773](/ideas/project-mesa/mesa-mesa-discussions-2773) and [Discussion #2775](/ideas/project-mesa/mesa-mesa-discussions-2775) after GSoC selection process. The project has since seen contributions from various developers, but it remains in an experimental state with open issues and areas for improvement.


### Overall Goal
Create a stable, well-tested, and fully-featured version of Mesa-LLM that seamlessly integrates with Mesa (including preparing to the breaking changes from the future update to mesa 4.0.0) while maintaining its versatility. This includes expanding documentation, improving test coverage, and simplifying processes that can still be hard for the user to understand (with reasoning, memory and other simple functionalities).

**Core Features:**

1. Address outstanding issues in the mesa-llm repo
2. Improve LLM tool modularization and extensibility
3. Create a stable release cadence aligned with Mesa's releases
4. Improve continuous integration and testing infrastructure
5. Optimize ollama and local inference support

**Documentation:**

1. Expand tutorials with advanced usage examples
2. Create migration guides from Mesa to Mesa-llm
3. Add performance/cost optimization guidelines
4. Document integration patterns with other Mesa extensions
5. Build examples (if possible sourced from existing scientific papers) showcasing complex agent architectures using mesa-llm and comparison with non-LLM agents

Testing & Quality Assurance: Improve current comprehensive test suite covering all features and add new tests and edge cases

### Skills Required
**Required:**
* Strong Python programming skills.
* Deep understanding of LLM APIs (OpenAI, Anthropic, Gemini, etc.) and local model usage (Ollama, huggingface).
* Experience with Prompt Engineering and Context Window management.
* Understanding of Asynchronous programming (asyncio).

**Preferred:**
* Familiarity with Mesa core architecture.

**Level:** Medium/Hard
**Size:** 175 / 350 hours

### Mentors
* **Primary:** Jackie (@jackiekazil)
* **Backup:** Colin (@colinfrisch)

### Getting Started
1. Get familiar with the Mesa framework: [Mesa Documentation](https://mesa.readthedocs.io/)
2. Explore the Mesa-LLM repository: [mesa-llm GitHub](https://github.com/mesa/mesa-llm)
3. Analyze current issues regarding API latency and memory handling.
4. Implement one or more basic models using the current version to identify friction points in the API.

## Meta Agents 
### Summary
Complex systems often have multiple levels of components. An organization is not one entity, but is made of departments, sub-departments,
and people. A person is not a single entity, but it is made of microbiomes, organs, and cells. A city is not a single entity, but it is made of districts, neighborhoods, buildings, and people. A forest comprises an ecosystem of trees, plants, animals, and micro-organisms. This reality is the motivation for meta-agents. It allows users to represent these multiple levels, where each level can have agents with `constituting_agents`. 

### Motivation 
Enhancing meta-agents into a optimally working module that allows users to create complex adaptive networks can fundamentally aid complexity research. It can allow for more elegant models where agents are in a active and dormant networks and who's behavior is changing based on stimulus allowing for greater opportunity for emergent behavior. In addition, as best Mesa can tell meta-agents is a unique functionality to Mesa, we also want to capitalize on this uniqueness and further build this capability.

### Historical Context 
Currently, `meta-agents` is a rapidly thrown together prototype. It needs to be enhanced to optimally integrate with Mesa and it needs to allow for greater functionality and optimization.  

### Overall Goals
Develop meta-agents to: 
- robust, sustainable, and modular base architecture 
- Determine optimizations meta agent employment and for registry management

### **Getting Started**
- See the examples [Alliance Formation](https://mesa.readthedocs.io/latest/examples/advanced/alliance_formation.html) and [Warehouse](https://github.com/mesa/mesa-examples/tree/main/examples/warehouse)
- Be familiar with the [base code ](https://github.com/mesa/mesa/tree/main/mesa/experimental/meta_agents)
- Build you own meta-agent model


### Project Size

* Medium

### Mentors

- **Primary:** Tom (@tpike3)
- **Backups:** Ewout (@EwoutH)

## Reviving Mesa-examples
### Summary
After moving core examples to the main Mesa repository ([#2358](https://github.com/projectmesa/mesa/pull/2358)), the [mesa-examples](https://github.com/projectmesa/mesa-examples) repository needs a clear purpose and sustainable maintenance strategy. This project defines what mesa-examples should be, makes it attractive to contribute to and use, and sets up systems to keep examples working over time.

### Motivation
Mesa-examples contains dozens of user-contributed models showcasing different Mesa features and ABM techniques. But without the core examples driving regular maintenance, the repository risks bit rot: examples breaking silently as Mesa evolves, outdated patterns persisting, and contributors uncertain whether their PRs will be reviewed. Meanwhile, users struggle to find examples relevant to their needs or trust that what they find actually works. A healthy examples ecosystem benefits everyone: users get working code to learn from, contributors get their work showcased, and Mesa gets real-world validation of its features.

### Historical Context
Examples were originally part of the main Mesa repository, then split into mesa-examples to reduce maintenance burden and encourage community contributions. In late 2024, core "seminal" examples (Boltzmann Wealth, Wolf-Sheep, Schelling, etc.) were moved back to Mesa ([#2349](https://github.com/projectmesa/mesa/pull/2349), [#2358](https://github.com/projectmesa/mesa/pull/2358)) where they receive full CI testing and guaranteed compatibility. This left mesa-examples as a "show and tell gallery" of community models, but without clear guidelines, testing infrastructure, or maintenance commitments. The tracking issue [#2364](https://github.com/projectmesa/mesa/issues/2364) documents the integration work done for core examples; similar attention is now needed for the community repository.

### Overall Goal
Transform mesa-examples into a thriving community gallery where contributors want to share their models, users can easily find and run working examples, and maintenance stays manageable. This means defining clear standards, building infrastructure to catch breakage early, improving discoverability, and lowering barriers to contribution.

### Potential Approaches
Several questions need answers, and a good proposal might focus on one or more:

* **Keeping examples working:** How do we ensure examples don't silently break? Options include pinned dependencies (requirements.txt or environment.yml per example), version compatibility markers, automated weekly CI against Mesa releases, or compatibility matrices showing which examples work with which Mesa versions.
* **Making contribution attractive:** What would make someone want to contribute an example? Clear templates, fast PR reviews, recognition (featured examples, contributor credits), lower standards than core Mesa (working > perfect), or themed contribution drives could help.
* **Improving discoverability:** How do users find relevant examples? Better categorization (by feature, complexity, domain), search/filter on a documentation site, integration with Mesa docs, or a gallery page with screenshots and descriptions could address this.
* **Sustainable maintenance:** What level of maintenance is realistic? Options range from "best effort, use environment files" to "community maintainers for categories" to "automated PRs for simple fixes." The answer shapes everything else.

Consider studying how other projects handle community examples: NetLogo's Models Library, Julia's model zoo repositories, or scikit-learn's examples gallery all offer lessons.

### Possible Outcomes
Depending on the approach, outcomes might include:

- Clear contribution guidelines and templates for mesa-examples
- CI/CD infrastructure that tests examples against Mesa releases
- Per-example environment files or version compatibility markers
- Improved README and documentation with better categorization
- A gallery or catalog page making examples browsable
- Automated tools (bots, scripts) to help maintain examples
- Migration of examples to updated patterns or Mesa versions
- Analysis of what's working in other ABM example ecosystems

The specific deliverables should match the problems you choose to tackle.

### Useful skills
Python packaging and dependency management. Familiarity with CI/CD systems (GitHub Actions). Experience with Mesa or willingness to learn quickly. Technical writing for documentation and guidelines.

### Getting Started
Browse [mesa-examples](https://github.com/projectmesa/mesa-examples) and try running several examples: note what works, what breaks, and what's confusing. Read the original discussion in [#2330](https://github.com/projectmesa/mesa/discussions/2330) and the core examples integration ([#2349](https://github.com/projectmesa/mesa/pull/2349), [#2358](https://github.com/projectmesa/mesa/pull/2358)) to understand the history. Look at open PRs and issues in mesa-examples to see what contributors want and where things are stuck. Compare with example galleries in other projects. Then pick an angle that interests you and sketch a concrete plan.

### Suggested size
- Small (focused on specific aspect)
- Medium (more broad/integral approach)

_Large might also be possible in consultation mentors_
### Mentors (committed)
- Jackie Kazil (@jackiekazil) & Ewout ter Hoeven (@EwoutH)

Archive: 
Discussions: [Discussion #2927](/ideas/project-mesa/mesa-mesa-discussions-2927) | [Matrix chat](https://matrix.to/#/#GSoC:matrix.org)
