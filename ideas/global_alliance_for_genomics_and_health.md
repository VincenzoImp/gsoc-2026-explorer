# Global Alliance for Genomics and Health — Project Ideas

**Source:** https://docs.google.com/document/d/1SeDP5Ny7Gt42g5oY9jdN15Wx6RXtJ9dDcaPeYBvKBcE/edit?tab=t.0#heading=h.qflicizcqlm
**Scraped:** 2026-02-22T23:28:47.612807

---

GA4GH Projects for GSoC 2026

[Project Name: GA4GH ServiceInfo Sidecar](https://docs.google.com#h.tymwyox83rvg)

[Core Sidecar Implementation (175h and 350h project)](https://docs.google.com#h.3ebopsvj8qb3)

[Extensions & Security (350h project only)](https://docs.google.com#h.nnjdjw5ozbc)

[Project Name: GA4GH-RegBot: An LLM-Powered Compliance Assistant for Genomic Data Sharing](https://docs.google.com#h.lqnx2xuvovtq)

[Project Name: Advanced Workflow Logging Parser](https://docs.google.com#h.8g1phicfiy4h)

[Project Name: GA4GH-aligned Trustworthy Federated AI](https://docs.google.com#h.pvx7js20uh5j)

Workstream | Cloud |
Mentor names/emails | - Alexander Kanitz (
[alexanderkanitz@gmail.com](mailto:alexanderkanitz@gmail.com)) - Javed Habib (
[javed@pacificanalytics.com](mailto:javed@pacificanalytics.com)) - Anurag Gupta (
[aguptaking@gmail.com](mailto:aguptaking@gmail.com))
|
Difficulty | Medium (175h) / Hard (350h) |
Requirements | Python, LLM |
Workload | 175h or 350h |
Project Description | |
## Project overviewThe However, currently there exists a critical gap: the majority of workflows available via TRS-enabled workflow registries such as Retroactively “cloudifying” the thousands of publicly available computational workflows in the life sciences manually would be a gargantuan task. We therefore want to build Workflow Clinic, an agentic AI-powered tool suite that provides two core functionalities: - The Workflow Critic informs workflow developers about “cloudification” gaps in their workflows
- The Workflow Doctor proposes code changes that address the gaps identified by the Workflow Critic functionality
## MilestonesYou can choose between a 175h and a 350h project, of medium and hard difficulty, respectively. The former only addresses the core tool and the Workflow Critic functionality. The latter additionally covers the Workflow Doctor functionality. Workflow Critic (175h and 350h project): - Core CLI tool created in Python and integrated with AI agent
- Agent team integrated to generate structured gap reports for workflows of one type, e.g., Nextflow, Snakemake, Airflow, Workflow Definition Language (WDL), Common Workflow Language (CWL)
- Agent team integrated to create gap report issues in workflow repositories
- Agent teams integrated to generate gap reports for 2-3 additional workflow types
- Project fully published and documented
Workflow Doctor (350h project only) - Agent team integrated to generate fixes for issues identified in gap report, for one workflow type
- Agent team integrated to create PRs to propose fixes in workflow repositories
- Agent team integrated to generate fixes for issues identified in gap report, for 2-3 additional workflow types
- Doctor features fully documented
Finally, the tool should be run to generate issues across all supported workflow repositories (Workflow Critic), and, if applicable, to raise PRs to address these issues (Workflow Doctor). ## ImpactThe Workflow Clinic will bridge the gap between static code repositories and functional cloud research by: - Automating Portability: Eliminates the huge manual task of cloudifying thousands of legacy workflows, making them instantly compatible with modern cloud storage and containerized environments.
- Enhancing Interoperability: Directly supports GA4GH standards (TRS/WES), ensuring life science tools can move seamlessly across national and organizational boundaries.
- Improving Code Quality: Empowers developers with an automated "Critic" to identify technical debt and a "Doctor" to provide actionable fixes via PRs, significantly raising the standard of public bioinformatics registries.
- Accelerating Research: By making workflows "cloud-ready," this tool reduces the time scientists spend on infrastructure troubleshooting, allowing them to focus on data analysis and discovery.
- Standards Improvement: The project will likely lead to the suggestion of multiple improvements for both the TRS (e.g., reporting/feedback functionality) and WES (e.g., supporting input/output description schemas), which may inform the design of cloud research platforms in the future.
## A Good Proposal…- Concisely describes an overall systems architecture for the project (code structure, data models, tool stack including agentic AI)
- Concisely describes all portability blockers after deep researching available a number of life science workflows and related literature
- Proposes a detailed, comprehensive models for structured “cloudification” gap reports
- Outlines a way how issues (and PRs, for the 350h project) can be automatically generated in the workflow repositories
- Emphasizes coding best practices that will be employed wrt to continuous testing and documentation
- Proposes a realistic timeline that accounts for contingencies and leaves time for comprehensive reviews
|

Workstream | Cloud |
Mentor names/emails | - Pavel Nikonorov (
[pavel@jandigitrust.org](mailto:pavel@jandigitrust.org)) - Alexander Kanitz (
[alexanderkanitz@gmail.com](mailto:alexanderkanitz@gmail.com))
|
Difficulty | Medium (175h) / Hard (350h) |
Requirements | Python, Go or Rust, OpenAPI/Swagger, networking (reverse proxies/middleware), REST APIs; knowledge of TEEs/Attestation is a plus for the 350h project |
Workload | 175h or 350h |
Project Description | |
## Project overviewThe Currently, every new implementation of a GA4GH standard must manually "bake in" the Service Info logic. This leads to fragmented implementations, inconsistent metadata, and a high barrier to entry for supporting emerging requirements – such as Trusted Execution Environments (TEEs) and Attested TLS as being defined by We aim to build the GA4GH ServiceInfo Sidecar: a high-quality, production-grade proxy/middleware solution. Instead of modifying core service code, developers can deploy this sidecar alongside any GA4GH-compliant product to handle ServiceInfo requests and security extensions automatically. ## The "Sidecar" ApproachThe project involves creating a lightweight service that intercepts incoming traffic. - The Core: Implements the standard GA4GH Service Info model.
- The Proxy: Forwards standard requests to the backend service while intercepting /service-info calls.
- The Middleware: Allows "plugging in" service-specific extensions (e.g., specific TES/WES metadata) and security features like Attested TLS.
## MilestonesYou can choose between a 175h and a 350h project. The former focuses on the core proxy and standard compliance, while the latter introduces advanced security and service-specific extensions. ## Core Sidecar Implementation (175h and 350h project)- MVP Proxy: Create a functional reverse proxy in Python or Go that handles routing between a client and a mock GA4GH service.
- Standard Compliance: Implement the core GA4GH Service Info OpenAPI specification within the sidecar.
- Configuration Engine: Develop a system to easily configure static service metadata (name, organization, contact) via YAML/JSON.
- Documentation: Comprehensive guide on deploying the sidecar with existing GA4GH services (e.g., via Docker/Kubernetes).
## Extensions & Security (350h project only)- Plugin Architecture: Implement a middleware system that allows the sidecar to "poll" or "inject" service-specific metadata from the backend service (e.g., WES-specific engine versions).
- Remote Attestation Middleware: Integrate a middleware layer for Attested TLS. This ensures the service can prove its identity, state, and integrity via hardware-backed claims.
- Integration Testing: Demonstrate the sidecar working in front of at least two different GA4GH service implementations (e.g., a TES and a WES instance).
- Advanced Security Docs: Document the attestation flow and how to verify the "trustworthiness" of the proxied service.
## ImpactThe GA4GH ServiceInfo Sidecar will transform how genomic services are deployed: - Write Once, Reuse Anywhere: Provides a "gold standard" implementation that saves hundreds of developer hours across the GA4GH ecosystem.
- Version Agility: Simplifies the transition between different versions of GA4GH standards without requiring backend code changes.
- Hardened Security: Lowers the floor for implementing Remote Attestation, making secure, confidential computing more accessible to the genomics community.
- Clean Architecture: Promotes a separation of concerns, keeping core bioinformatics logic separate from administrative and discovery metadata.
## A Good Proposal…- Clearly defines an architectural blueprint, containing the choice of language (Python vs. Go) and the networking library (e.g., FastAPI, Flask, or Go’s httputil)
- Demonstrates a solid understanding of how to merge or extend OpenAPI schemas dynamically
- Explains how the sidecar will handle request routing and headers without introducing significant latency
- Includes a plan for containerization, security hardening, deployment (overriding any available Service Info implementation) to ensure the sidecar is production-ready
- Outlines a basic understanding of TEE VMs (Intel TDX or AMD SEV) and how attestation reports can be served via API (for 350h project only)
|

Workstream | Regulatory and Ethics Work Stream (REWS) |
Mentor names/emails | - Dedy Effendi Lingga (dedyli@iscb.org)
|
Difficulty | Medium Workload 175 hours |
Requirements | - Python (Intermediate)
- Basic NLP / LLMs (Familiarity with LangChain,
- LlamaIndex, or similar)
- Vector Databases (ChromaDB / FAISS)
- Basic UI implementation (Streamlit)
|
Workload | 175h |
Project Description | |
The Problem: Researchers want to share genomic data responsibly, but mapping their specific consent forms against the dense legal text of GA4GH frameworks (like the Framework for Responsible Sharing) is manual, slow, and error-prone. The Solution: We want to build a lightweight “Compliance Assistant” that does the heavy lifting. The goal is to create a RAG (Retrieval-Augmented Generation) tool where a researcher can upload their project’s data use letter, and the AI will check it against GA4GH standards to flag gaps. The Work: The student will build a Python-based pipeline using open-source LLMs (e.g., Llama 3 or Mistral). The core challenge is not just chatting with the document, but ensuring the bot cites the exact clause in the GA4GH policy that supports its advice. This The tool will lower the barrier for researchers globally to adopt our standards. |

Workstream | Cloud |
Mentor names/emails | - Landfried Kraatz (landfried.kraatz@bih-charite.de)
- Valentin Schneider-Lunitz (valentin.schneider-lunitz@bih-charite.de)
- Sven Olaf Twardziok (sven.twardziok@bih-charite.de)
|
Difficulty | medium |
Requirements | Python or similar language, OpenAPI beneficial, Snakemake / Nextflow / CWL experience helpful |
Workload | 175h |
Project Description | |
Life science workflows are often written in workflow engines like Snakemake, Nextflow or CWL. The GA4GH Workflow Execution Service (WES) API provides a unified interface for workflow execution in various execution backends. The current API version 1.1.0 supports basic access to raw workflow output, however these logs are unstructured and engine-specific. The community demands richer, structured logging that supports debugging, monitoring and automated analysis of workflow executions. The goal of this project is to extend WES with a unified, structured log representation. As a proof of concept, part of the project is to extend an existing WES implementation to support the extended WES API for at least two widely used workflow engines. This includes the development of engine-aware log parsers that convert raw runtime output and task artifacts into the unified schema. This is a direct contribution to GA4GH WES, used in medical healthcare and computational biology. It will provide a foundation for future work on self-healing workflows, parameter auto-tuning and automated orchestration of workflows. The project is part of the ELIXIR-on-Cloud initiative. For this project, the use of AI is permitted and endorsed for research and exploring the code base. Code generation using AI is not forbidden, but generated code must be fully understood and reviewed thoroughly. GitHub repo: Documentation: ELIXIR-on-Cloud: |

Workstream | Cloud |
Mentor names/emails | Andrew Gearhart (andrew@nimbusinformatics.com), Javed Habib (javed@pacificanalytics.com), Alexander Medvedev (alex@genxt.network), Pavel Nikonorov (pavel@jandigitrust.org) |
Difficulty | Hard |
Requirements | Python, familiarity with ML frameworks (e.g. PyTorch, Flower), and basic DevSecOps practices |
Workload | 350h |
Project Description | |
Motivation and context Federated learning (FL) has emerged as a practical approach for collaborative biomedical and genomic research, enabling institutions to jointly train models without centralising sensitive data. Recent work has demonstrated that production-grade FL systems can deliver meaningful predictive performance while preserving data locality and privacy (Kolbkov et al., Efficacy of federated learning on genomic data: a study on the UK Biobank and the 1000 Genomes Project, Frontiers in Big Data, 2024). Despite this promise, adoption of federated AI in genomics remains limited in real-world deployments. A key barrier is not the learning algorithms themselves, but the lack of interoperable, standards-aligned infrastructure for identity, authorisation, workload trust, and secure execution across organisations. Many potential participants face high integration costs and uncertainty around trust, compliance, and operational security when attempting to deploy federated AI pipelines in regulated research environments. Project focus This project aims to address this gap by aligning an existing open-source, production-oriented federated learning genomics pipeline (FLAN, Technical objectives - Mapping the federated learning workflow onto GA4GH-compliant components and execution models.
- Investigating the applicability of the Model Context Protocol (MCP) for expressing execution context, metadata, constraints, and policies for federated AI workloads.
- Integrating existing Attested TLS components to establish verifiable, workload-level trust between federated nodes.
- Exploring how attestation evidence and execution context can be surfaced to GA4GH-compatible middleware and policy layers.
Expected outcome and impact The expected outcome is a documented reference integration and prototype demonstrating how federated learning systems can be deployed in GA4GH-aligned environments with improved trust, interoperability, and reproducibility. By lowering the barrier to secure, standards-based deployment, this work directly addresses a major obstacle to near-term adoption of federated AI within the biomedical research community. |
