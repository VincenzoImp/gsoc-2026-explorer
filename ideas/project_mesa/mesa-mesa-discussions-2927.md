# GSoC 2026 ideas discussion

**Parent:** Project Mesa — Project Ideas
**Source:** https://github.com/mesa/mesa/discussions/2927
**Scraped:** 2026-03-10T16:58:40.256883

---

[GSoC 2026 ideas](https://github.com#top)#2927

-

|
Let's start the discussion on 2026 GSoC ideas! 2025 ideas can be found here. Ones leftover from last year: **Behavioral framework:**This project aims to develop a unified behavior and state management system for Mesa, addressing the current limitation of simple discrete-time steps by enabling continuous state changes, time-consuming tasks, and sophisticated decision-making. By creating a comprehensive framework that integrates task priority scheduling, interruption capabilities, and behavioral theories, the initiative will allow modelers to simulate realistic agent behaviors—such as resource depletion and parallel activities—more effectively. The expected outcome is a robust API and event system that empowers users to build complex, theoretically grounded agent-based models with greater ease and flexibility.**Unifying geospatial Support in Mesa:**This initiative seeks to merge the standalone`mesa-geo` ([https://github.com/projectmesa/mesa-geo](https://github.com/projectmesa/mesa-geo)) package directly into the core Mesa library as a`mesa.geo` module, resolving compatibility issues arising from their separate evolution and simplifying dependency management. By leveraging Mesa's new experimental cell and continuous space architectures, the project will create a unified spatial modeling framework that supports GIS functionality, coordinate transformations, and standard file formats like GeoJSON within a consistent API. The consolidation aims to make advanced geospatial modeling a first-class feature, ensuring that property layers and spatial visualizations work seamlessly across all Mesa projects.- Key technical context includes the
[experimental cell space](https://github.com/projectmesa/mesa/tree/main/mesa/experimental/cell_space),[continuous space implementation](https://github.com/projectmesa/mesa/pull/2584), and the[Space conceptual model](https://github.com/projectmesa/mesa/discussions/2585).
- Key technical context includes the
**Mesa Blocks:**Mesa Blocks proposes the development of a low-code/no-code extension designed to help users rapidly assemble and run custom agent-based models using a visual drag-and-drop interface. Recognizing the difficulty in building complex models from scratch, this project aims to provide a system of reusable, customizable building blocks that allow users to quickly prototype valid models while retaining the ability to modify the underlying logic. The ultimate goal is to create a prototype that democratizes access to agent-based modeling, allowing for faster decision-making and model exploration through a user-friendly, modular environment.- Historical context and inspiration can be found in
[previous ecosystem attempts](https://journals-sagepub-com.mutex.gmu.edu/share/W3U6RZ3GKQNTPYFT522X?target=10.1177/00375497221077425)and[Reusable Building Blocks for ABMS](https://www.rbb4abm.com/).
- Historical context and inspiration can be found in
What more ideas and ambitions do we have? |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

## Replies: 20 comments 34 replies

-

|
We did talk about performance optimization in the past, and a Mesa performance optimization project might be interesting this year. Mesa's scalability to millions of agents depends on efficient core operations in AgentSet, spatial grids, and event scheduling. This project could systematically identify and address performance bottlenecks across the library. The first phase involves comprehensive profiling of Mesa's example models (Boltzmann Wealth, Schelling, Wolf-Sheep, Flocking) using tools like cProfile, py-spy, and memory_profiler to create a performance baseline and identify hotspots. Likely candidates include AgentSet operations ( The second phase could explore optimization strategies: expanding NumPy vectorization for batch agent operations, restructuring data layouts for cache efficiency, and evaluating Rust acceleration via PyO3 for compute-intensive components like spatial indexing, large-scale shuffling, and event queue management. Rust is particularly promising for operations with clear data boundaries (grids, coordinate math) where Python object overhead can be avoided. Deliverables could include a reproducible low-level benchmarking suite, documented performance improvements with before/after comparisons, and potentially a
|

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
These project ideas look great! I'm really interested in getting involved with Mesa for GSoC 2026. The Behavioral Framework project really caught my attention. I find it fascinating how individual agents making their own decisions can lead to complex emergent behaviors in the system. What excites me most is the challenge of taking these theoretical behavioral models - things like BDI or needs-based architectures - and turning them into something practical that people can actually use. It's basically building the "brain" for agents, which is pretty cool. - Work through the tutorial and build models that run into the behavioral limitations we're trying to solve
- Contribute some models to mesa-examples
- Deep dive into the discussions in
[Continuous States #2529](https://github.com/mesa/mesa/discussions/2529),[Tasks #2526](https://github.com/mesa/mesa/discussions/2526), and[Behavioral Framework #2538](https://github.com/mesa/mesa/discussions/2538) - Learn more about behavior trees, GOAP, BDI architectures, and related concepts
- Try building a simple proof-of-concept for a Task or State management system
One question: which existing Mesa models would you recommend looking at to see how people currently work around things like time-consuming tasks, competing priorities, or continuous state changes? I'd love to understand the current pain points from real examples. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi Building on the "Behavioral Framework" and "Performance" ideas, I'd like to propose a distinct direction for 2026 (or potential experiments in 2025): While the Behavioral Framework (BDI/GOAP) is excellent for deterministic, rule-based complexity, there is a growing need for agents that can reason dynamically via LLMs (inspired by the "Generative Agents" architecture by Park et al.).
**Orchestrates API Calls:**Seamlessly connects to Local LLMs (Ollama) or APIs (Gemini/OpenAI).**Enforces Structured Actions:**Uses the new Mesa 3.0`shuffle_do` mechanism by forcing the LLM to return valid JSON actions (e.g.,`{"action": "move", "pos": [1,2]}` ).**Manages Context Window:**Handles agent memory (summarizing past steps) so the simulation doesn't crash due to token limits.
I believe this complements the traditional Behavioral Framework by offering a "Probabilistic" alternative for scenarios where defining explicit rules is too difficult (e.g., natural language negotiation between agents or simulating social dynamics). I've already started experimenting with this using the new Mesa 3.0 syntax and ensuring strict JSON outputs. I would love to explore this further as a potential project area. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Thanks for pointing that out! Yes, I have explored My proposal is essentially to **Update Architecture:**Refactor the integration to align with the new Mesa 3.0 standards (removing schedulers, using`shuffle_do` ).**Enforce Reliability:**Implement strict**Structured Outputs (JSON)**. A common issue with basic LLM integration is "hallucinated actions"; my focus would be on robust parsing so agents don't break the simulation loop.**Local LLM Support:**Ensure native compatibility with tools like Ollama/Llama.cpp for users who can't afford API costs (crucial for students).
I’d love to take |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
I have two more: Making clean-sheet designs of how we Mesa's current ## Reimagining Model Execution and Experimental setupThe fundamental problem with The goal isn't to design a specific solution but to map the territory: What capabilities should Mesa provide natively versus enable through documented patterns? Where are the natural architectural boundaries between experiment specification, execution strategy, and result aggregation? How do we balance simplicity for beginners running local parameter sweeps against power users orchestrating thousands of replications across HPC resources? What standards exist for experiment metadata and provenance that Mesa should adopt? The project could start with a comprehensive requirements analysis, ecosystem survey, user research findings, and architectural principles that can guide Mesa 4.0's design. And if time allows, a (proof of concept) implementation. [Next-gen batch runner #2321](https://github.com/mesa/mesa/issues/2321)- (and slightly related)
[A system for managing Model/Agent default values and ranges #2268](https://github.com/mesa/mesa/issues/2268)
## Rethinking Data Collection and Management
The research phase should investigate: What data patterns do ABM researchers need to capture, and how do current workflows break down? What can we learn from how climate models, computational biology, and other simulation-heavy domains handle output management? Where does the impedance mismatch lie between ABM data patterns and standard scientific data formats? How do users currently bridge Mesa outputs to their analysis tools, and what friction exists? What performance characteristics matter most—collection overhead during simulation, storage efficiency, or query speed during analysis? The contributor should survey existing solutions, prototype integration patterns with ecosystem tools, and identify fundamental architectural questions: Should Mesa embrace lazy evaluation and streaming? How can we handle the "collect everything vs. collect strategically" tension? What's the right balance between flexibility and performance? The outcome should include a clear problem taxonomy, evaluation of how existing tools address (or don't address) ABM-specific needs, user requirements gathered from community research, and architectural recommendations for Mesa 4.0. Both projects emphasize discovery over delivery: understanding the landscape, learning from successes and failures elsewhere, and establishing principled foundations rather than rushing to implementation. One we know what we need to build and which tools we have to build it, the implementation becomes relatively easy. [The future of data collection #1944](https://github.com/mesa/mesa/discussions/1944)- (and the older, previous discussion)
[Multi-Agent data collection #348](https://github.com/mesa/mesa/issues/348)
|

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Since there is huge interest in doing things with ML/DL/RL/AI, here is something that might be interesting: A concrete research idea is to build a “Mesa Inference” layer that turns any Mesa model into a Methodologically, the first integration target could be Approximate Bayesian Computation (ABC) as a baseline and diagnostic tool, following canonical treatments such as Beaumont’s review of ABC methods (
summary learning: enabling optional autoencoder-based embeddings of high-dimensional ABM outputs while still allowing users to enforce theory-driven, interpretable summaries (e.g., stylized facts, moments, or distributional targets).A second, more exploratory research track is to support Finally, the framework should explicitly support |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi everyone, I'm Briony! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi everyone I am Joel Jose, I have prior experience working with CNN-based models and I’m particularly interested in how AI systems perceive visual information. I’m exploring the idea of introducing a minimal perception abstraction for Mesa agents. The concept would start very small: for example, agents could receive simple visual inputs, like colors or local spatial patterns, converted into numerical observations. Over time and through incremental development, agents could learn to interpret more complex observations, potentially evolving toward recognizing structured patterns or small images. The goal would be to implement this as a modular, optional extension that doesn’t affect Mesa’s core scheduler or deterministic execution, while allowing experimentation with perception-based learning in agent-based simulations. I’d love feedback from the maintainers on whether this direction aligns with Mesa’s road map or if there are existing discussions or abstractions I could build on. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

## Reviving Mesa-examplesAfter moving our core examples to the main repo (see A proposal on this topic could answer (one or more) questions like: - How can we make it attractive to contribute examples to mesa-examples?
- How can we keep them up to date?
- How can we enforce they keep working? (versioning, testing, CI, etc.)
- How can we make our examples more attractive to use? (findability, documentation, guidance, etc.)
This is my initial take, any other visions/ideas are welcome on this! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi One direction I’d like to explore (as a contributor, not as a framework proposal yet) is using new example models as a diagnostic tool for the Behavioral Framework discussion. Concretely, instead of starting from BDI / task systems / APIs, I plan to: design a small but non-trivial example model that is not currently present in Mesa, implement it using only existing Mesa primitives, and use that experience to surface where current patterns feel natural vs where behavior logic becomes awkward or overly tangled. The type of behavior I have in mind is adaptive / experience-based decision-making within a single run: agents choose between alternatives (e.g. risky vs safe actions), remember negative outcomes locally, and adjust future decisions based on that memory. This is intentionally below a full behavioral framework: no new APIs, no new abstractions, just a clean example + README that documents the pain points encountered. My goal is to contribute this as a new example, and only then reflect on what it teaches us about states, decisions, action duration, or task structure — feeding that insight back into the broader Behavioral Framework discussion. If this example-first, evidence-driven approach is useful, I’d be happy to iterate further and expand it based on feedback. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi - Reactive State: Wrapping
`mesa_signals` to create "Trigger States" (e.g.,`Hunger` emits a signal at threshold 20). This removes the need for agents to poll their own status every step. - Durative Tasks: Using the
`DEVS` simulator to give actions (Movement, Crafting) explicit duration. Crucially, I want to implement Interruption (canceling the`finish_task` event if a higher-priority`Flee` signal fires). - Pluggable Decision Systems: A standard interface (
`decide(state) -> Task` ) that allows users to swap between simple Rules, FSMs, or even LLMs without rewriting the agent.
Validation: - Current: Wolves move/eat instantly in
`step()` . - Proposed: Sheep have a
`Hunger` state (Signal) that triggers a`Graze` task (Duration). If they spot a Wolf while grazing, the task is Interrupted to trigger`Flee` .
I’m prototyping the Interruption logic using |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi everyone I'm Liyue. Based on my research needs and the recent community discussions on Scenarios ( I would love to hear any feedback or feature requests from the community! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

## Modernizing Mesa-Geo: Refactor and Visualization OverhaulGoal: Refactor Mesa-Geo to align with Mesa's modern architecture, moving from object-based raster storage to high-performance vectorized ## Phase 1: Core Data Refactor (
|

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I plan to spend the coming weeks working through existing examples (such as Wolf–Sheep, Schelling, and Sugarscape), experimenting with small extensions or new example models that stress areas like adaptive decision-making, memory, and multi-step actions. The goal is to document where current Mesa primitives feel expressive versus where behavior logic becomes awkward or overly tangled. I also find the Mesa Inference direction very exciting, particularly the idea of formalizing the simulator–inference boundary and supporting SBI/ABC workflows for calibrating ABMs against observed macro data. I’ll aim to contribute incrementally through examples, documentation, or small PRs, and share concrete findings back into this discussion rather than proposing abstractions prematurely. Looking forward to learning from and contributing to the Mesa community. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hey |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi everyone, I’ve been exploring the repository as preparation for a potential GSoC proposal around revitalizing the mesa-examples repository, and I wanted to share some findings from the work I’ve done so far. Over the past few days I audited around 20 examples locally using the latest Mesa version. While doing this I tried to systematically evaluate each example in terms of execution, dependencies, and documentation. What I have done so far For the audit I followed this process for each example: Installed the dependencies required for the example Ran the example using the command specified in the README Recorded whether the example runs successfully or fails Noted missing dependencies, outdated APIs, and documentation gaps During this process I observed several recurring issues across examples. - Legacy visualization API usage
Some examples still rely on the older visualization stack, such as: mesa.visualization.CanvasGrid mesa runserver These appear to be incompatible with current Mesa versions. - Broken or outdated run instructions
Some READMEs contain commands that no longer work or lack clear instructions for running the example. - Missing dependencies
Several examples require dependencies that are not documented in the README (for example networkx, solara, etc.). - Compatibility issues with newer Mesa versions
A few examples fail due to API changes in Mesa (for example changes in PropertyLayer or visualization components). - Documentation inconsistencies
Some examples have very detailed documentation, while others lack installation instructions or clear execution steps. Possible direction moving forward While reading the discussion about improving discoverability and adding metadata to examples, I was thinking about an additional improvement that might help long-term maintainability. One potential approach could be combining: Example metadata Adding structured metadata for each example describing things like: domain (social science, biology, economics, etc.) complexity level (beginner/intermediate/advanced) dependencies run command last verified Mesa version Example structure: name: rumor_mill dependencies: - mesa[rec]
run_command: solara run app.py tested_with: Using this metadata to power a CI workflow (e.g., GitHub Actions) that automatically: installs dependencies runs each example reports failures when examples break with new Mesa versions This could help keep the examples repository reliable and quickly identify compatibility issues when Mesa evolves. Next steps For now I plan to: finish organizing the results of the audit summarize common failure patterns experiment with a small prototype workflow that automatically runs examples Before going further, I wanted to ask the maintainers: Would an automated validation system like this be useful as part of the Mesa-examples revitalization effort? I’d really appreciate any feedback or suggestions on whether this direction aligns with the goals of the project. Thanks! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi! I'm Gaurav, a B.Tech CS student contributing to sktime. I've been reading through this discussion and the mesa-examples repo carefully. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi everyone! - PR
[Agents placed by an Agent are not added to the scheduler #344](https://github.com/mesa/mesa/issues/344)-- Hierarchical Organization Model: OrganizationAgent manages DepartmentAgents which manage EmployeeAgents — a 3-tier meta-agent hierarchy 2)PR[Python 3.4 build breaking... #353](https://github.com/mesa/mesa/issues/353)-- SEIR Epidemic Model: GovernmentAgent monitors infection rates and triggers vaccination campaigns dynamically
Both use Mesa 3.x (OrthogonalMooreGrid, CellAgent, SolaraViz). Through building these, I directly experienced the pain points around meta-agent coordination and policy enforcement. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi Following up on my recently merged PR ( I have finished my full draft covering the Raster Refactor, the Pandas-style Aggregation API, and the SolaraViz |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)
