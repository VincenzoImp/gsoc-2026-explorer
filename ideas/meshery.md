# Meshery — Project Ideas

**Source:** https://meshery.io/programs/gsoc/2026
**Scraped:** 2026-02-22T23:28:47.622260

---

### Project 1. Migration of docs.meshery.io from Jekyll to Hugo

#### Description:

The Meshery documentation [docs.meshery.io](https://docs.meshery.io) is a critical resource for users and contributors. Currently built using Jekyll, the site faces limitations in build speed, scalability, and long-term maintainability. Hugo, a modern static site generator, offers significantly faster build times, better content organization, and an improved developer experience. This internship focuses on migrating the entire [docs.meshery.io](https://docs.meshery.io) site from Jekyll to the Hugo framework, using docs.layer5.io (already implemented in Hugo) as a reference architecture. The migration will involve porting all documentation content, assets, layouts, and configuration while preserving URLs, SEO, contributor workflows, and existing auto-generated documentation files.

#### Expected outcomes:

- Revamp of documentation set information architecture. Alignment with Diataxis framework.
- Updated contributor docs.
- {"All self-documenting aspects accounted for"=>["Compatibility tests of Meshery Adapters.", "End-to-end tests of Meshery UI.", "Integration of Meshery Catalog and all designs.", "Publication of community discussion forum activity per category.", "Integration of Meshery Models (Integrations)"]}

**Recommended Skills:**Static site generators (Jekyll and Hugo), Markdown, HTML/CSS, Git/GitHub workflows, documentation engineering, basic Go templating (Hugo), CI/CD familiarity.**Expected project size:**medium (~175 hour projects)**Mentors:**[Kate Suttons](https://github.com/suttonskate),[Lee Calcote](https://github.com/leecalcote)**Issue:**[https://github.com/meshery/meshery/issues/17095](https://github.com/meshery/meshery/issues/17095)

### Project 2. Relationships for AWS services

#### Description:

Meshery Models are declarative representations of infrastructure and applications. Within these models, Relationships define how different Components (e.g., Kubernetes resources, Cloud services) interact and depend on each other. These relationships are crucial for visualizing, understanding, and managing complex cloud native systems. This internship focuses on significantly expanding the breadth and depth of Meshery Relationships across a wide array of technologies supported by Meshery. As Meshery continues to integrate with more cloud-native technologies (Kubernetes, public clouds, and all CNCF projects), there’s a growing need to accurately model the intricate relationships between their components - vital for providing users with comprehensive insights and control over their deployments.

#### Expected outcomes:

- A multitude of new relationships defined both intra and inter AWS services.
- {"Policy Contribution"=>"For advanced interns, there may be opportunities to contribute to the Rego policies that evaluate and enforce these relationships."}

**Recommended Skills:**DevOps, systems administration, solutions architecture. Experience with Kubernetes, AWS and its services.**Expected project size:**medium (~175 hour projects)**Mentors:**[Sangram Rath](https://github.com/sangramrath),[Lee Calcote](https://github.com/leecalcote)**Issue:**[https://github.com/meshery/meshery/issues/17096](https://github.com/meshery/meshery/issues/17096)

### Project 3. Adapter for AI and LLMs

#### Description:

Meshery is the open-source cloud native manager that empowers platform engineers to design and operate infrastructure. As infrastructure complexity grows, the need for intelligent assistance becomes critical. This project focuses on developing and enhancing a dedicated AI Adapter and AI Connections for Meshery. This adapter serves as the bridge between Meshery’s core orchestration engine and various Large Language Models (LLMs). The goal is to enable “Natural Language to Infrastructure” capabilities, allowing users to describe their architectural intent (e.g., “Deploy a highly available Kubernetes cluster on AWS with Prometheus monitoring”) and have Meshery auto-generate the visual topology and configuration manifests. The intern will work on decoupling the AI logic from the core platform, allowing users to “Bring Your Own Model” (BYOM)—supporting both cloud-based providers (OpenAI, Anthropic) and local inference runners (Ollama, LocalAI).

#### Expected outcomes:

- A fully functional AI Adapter (or Connection) integrated into the Meshery ecosystem.
- Demonstrable capability for users to swap between at least two different LLM providers (e.g., OpenAI vs. a local Llama 3 model).
- Implementation of a feature where natural language queries result in a rendered design.
- Merged pull requests (PRs) including code, tests, and documentation.

**Recommended Skills:**Proficiency in Golang (Go) is essential, as Meshery’s backend is written in Go.Familiarity with MCP Servers, REST APIs, LLM APIs (OpenAI, Vertex AI), local inference servers (Ollama).Basic understanding of Kubernetes, Docker, and Infrastructure-as-Code (IaC) concepts.Experience with REST, GraphQL, and gRPC.Nice to have Experience with React (for frontend integration in Meshery UI).**Expected project size:**medium (~175 hour projects)**Mentors:**[Rian Cteulp](https://github.com/ritzorama),[Lee Calcote](https://github.com/leecalcote)**Issue:**[https://github.com/meshery/meshery/issues/17097](https://github.com/meshery/meshery/issues/17097)

### Project 4. Graph Database Integration

#### Description:

Meshery’s *MeshSync* component acts as the real-time discovery engine, maintaining an up-to-date snapshot of all managed infrastructure. Currently, mapping the complex relationships between these resources (e.g., a Service selecting Pods which are mounted to PVCs) relies on relational or in-memory lookups that can become inefficient at scale. This project involves integrating a dedicated graph database (or an embedded graph processing library) into Meshery’s architecture. The goal is to ingest discovered Kubernetes resources as “nodes” and their associations (OwnerReferences, Label Selectors, Annotations) as “edges.” This shift will enable highly efficient traversal and querying of infrastructure data, powering more advanced capabilities like topology visualization, impact analysis, and dependency mapping.

#### Expected outcomes:

- Fully-functional datastores of discovered cluster data into a graph structure.
- Benchmarks demonstrating improved performance for complex relationship queries compared to the existing relational implementation.
- Successful rendering of the infrastructure topology in Meshery UI using data fetched from the new graph backend.
- Comprehensive documentation covering the new graph schema and query patterns.

**Recommended Skills:**Strong proficiency in Golang as both MeshSync and Meshery's Kubernetes operator are written in Go.Understanding of openCypher, graph theory and Graph Databases (e.g., NebulaGraph, or embedded Go graph libraries like `gonum` or `cayley`).Strong familiarity with Kubernetes Controllers, Informers, and the Object Model (GVK/GVR).Experience and competency with GraphQL**Expected project size:**medium (~175 hour projects)**Mentors:**[James Horton](https://github.com/hortison),[Lee Calcote](https://github.com/leecalcote)**Issue:**[https://github.com/meshery/meshery/issues/17098](https://github.com/meshery/meshery/issues/17098)

### Project 5. Workflow Engine in Meshery

#### Description:

Integrate a new architectural component into Meshery: a workflow engine, using Temporal. This project involves shifting Meshery off of sqlite over to postgres using gorm (golang). Interns will familiarize with concepts of orchestration engines, including chaining workflows, and content lifecycle management.

#### Expected outcomes:

**Recommended Skills:**Golang, Temporal, ReactJS**Expected project size:**medium (~175 hour projects)**Mentors:**[Marcus Ringblom](https://github.com/marblom007),[Lee Calcote](https://github.com/leecalcote)**Issue:**[https://github.com/meshery/meshery/issues/17099](https://github.com/meshery/meshery/issues/17099)
