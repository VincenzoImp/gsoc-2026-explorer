# National Resource for Network Biology (NRNB) — Project Ideas

**Source:** https://github.com/nrnb/GoogleSummerOfCode/issues
**Scraped:** 2026-02-22T23:28:47.582082

---

## #282: AI chatbot to explore modeling resources in biology

**Labels:** JavaScript, web services, Python, BioPAX, SBML, Difficulty: Medium, COMBINE Archive, Docker, VCell, Size: 175h, LLM, GUI, typescript

### Background

Predictive mathematical modeling is an essential part of systems biology and is interconnected with information management. Systems biology information is stored in specialized formats (http://co.mbine.org/) that facilitate data storage and analysis (e.g. http://sbgn.org/, http://sbml.org/). These formats are not designed for easy human readability and thus require specialized software to visualize and interpret results. There is an RDF/XML schema for storage of each type of data. Traditionally, to understand this data, you need specific tools that perform a specific set of queries. AI allows users to explore different type of data directly https://www.nature.com/articles/s41540-025-00496-z. 

AI can help with both understanding, designing, implementing and simulating of mathematical models. The simplest example of a ChatGPT chatbot (https://chatgpt.com/g/g-n3asZvWaM-vcell-models-explorer) can explore VCell models (http://vcell.org/). The design of the Chatbot is described in the following presentation: https://drive.google.com/file/d/1jLNjl-ZxZDeGcRxVL754Oao4GYsM4u0Y/view. It is using VCell API https://vcell.cam.uchc.edu/api/v0/biomodel.

The more complicated AI site is implemented at https://github.com/virtualcell/VCell-AI. It can be easily tested using Docker, also can be installed localy (API key is required).

Finally, the non-AI interface for accessing and displaying VCell models is deployed at http://www.vcelldb.org (currently maybe working improperly), available at https://github.com/virtualcell/modelbricks-webapp. It is implemented in Handlebars, with most information retrieved via API, and some information stored locally as JSON.

### Goal

Complete and integrate AI chatbot with vcelldb website, significantly extending and modifying it. The web interface should be able to query VCell resources and provide relevant information about VCell models, modeling techniques, and using VCell software.
Here are sample queries that the chatbot answers:
* Exploring VCell database, e.g.
       * List all models by a certain user
       * List all models that have a specific type of geometry (e.g. analytic, constructed solid, etc), that use specific solver (e.g. CVODE), etc.
      * List all models that deal with Calcium
* Exploring individual models (both from the database using auth0 authorization, and uploaded by a user):
       * How many reactions are in a the model? Describe mathematics, parameters, simulations.
       * What biological papers have similar modeling mechanisms?
       * Draw the reaction diagram in SBGN format
* Assist user in using VCell:
      * How to model enzymatic reaction?
      * How to define an analytic geometry?
      *  How to plot a histogram for multiple simulations?
      * What do colors mean in spatial simulations plot?

**The tasks for this summer:**
 * Improve prompt handling
 * Improve outputs formatting
 * Add Auth0 authentication (using Google, Facebook, ORCID, etc)
 * Add AI usage control:
 

*[truncated]*

---

## #281: Automated Reporting for Systems Biology Modeling Workflows

**Labels:** Python, SBML, HTML, Difficulty: Medium, SED-ML, Size: 175h, GitHub

# Automated Reporting for Systems Biology Modeling Workflows

### Background
Computational systems biology relies heavily on standardized modeling and simulation workflows, most notably **[SBML](https://sbml.org/)** (Systems Biology Markup Language) for models, **[SED-ML](https://sed-ml.org/)** (Simulation Experiment Description Markup Language) for simulation setups or **[PEtab](https://petab.readthedocs.io/en/latest/)** for parameter optimization workflows. While robust toolchains exist for parameter estimation and sensitivity analysis, the *communication of results* remains a major bottleneck.

Currently, results are often scattered across scripts, log files, plots, and tables, making it difficult to ensure reproducibility, transparency, and accessibility for collaborators and the wider community. There is a clear need for **automated, reproducible reporting pipelines** that transform modeling workflows into human-readable, well-structured reports.

This project builds on and contributes directly to **sbmlsim**, an open-source Python framework for simulation, parameter optimization, and sensitivity analysis of SBML models:

- https://github.com/matthiaskoenig/sbmlsim
- https://matthiaskoenig.github.io/sbmlsim/

Several existing model repositories already use CI/CD workflows to execute simulations, but reporting is mostly manual or ad hoc. This project addresses this gap by integrating standardized report generation into modeling workflows. 

### Goal
The goal of this GSoC project is to design and implement an **automated reporting framework** for systems biology modeling workflows based on SBML, SED-ML, and PETab integrated into **sbmlsim**.

The project will:
- Generate **interactive web reports** using **Quarto** (interactive figures and tables).
- Generate **static PDF reports** using **Typst** (publication-ready summaries and figures).
- Integrate report generation into **CI/CD pipelines** (GitHub Actions).
- Automatically publish web reports via **GitHub Pages (github.io)**.

The final outcome will be reusable reporting modules and templates within sbmlsim that can be adopted across multiple systems biology and systems medicine projects.

### Difficulty Level: Medium
This project is rated **Medium** because it combines Python development, scientific workflows, CI/CD automation, and report generation. While advanced mathematical modeling is not required, familiarity with reproducible computational workflows is important.

### Size and Length of Project
- **medium: 175 hours**  
- **12 weeks**

### Skills
**Essential skills**
- Python  
- Markdown  
- Git / GitHub  

**Nice to have skills**
- [Quarto](https://quarto.org/)
- [Typst](https://typst.app/home/)
- CI/CD (GitHub Actions)  
- Systems biology or scientific computing background  

### Public Repository
Primary development repository:
- https://github.com/matthiaskoenig/sbmlsim
- https://matthiaskoenig.github.io/sbmlsim/

Contributing to sbmlsim on develop branch:
- https://github.com

*[truncated]*

---

## #280: Provide established Metabolic Systems Biology tooling for Reconstruction and Analysis with LLMs

**Labels:** Python, JSON, Difficulty: Medium, Docker, Size: 175h

### Background
Reconstruction and subsequent network analysis are the fundamental processes of the systems biology of genome-scale metabolic models (GEMs). A plethora of tools exist in this space, and some of them emerged as the de facto standards (specifically [COBRApy](https://github.com/opencobra/cobrapy), [CarveMe](https://github.com/cdanielmachado/carveme), [MEMOTE](https://github.com/opencobra/memote), [Cytoscape](https://github.com/cytoscape/cytoscape)). The skillful and creative usage of these tools is a prerequisite for reliable knowledge extraction and fruitful hypothesis generation using GEMs.

GEMs are graph data structures that are well-suited for loading to and querying from a graph database. Consequently, tooling to load SBML into Neo4J ([Neo4JSBML](https://github.com/brsynth/neo4jsbml)) has been developed.
 
The dominant open standards for LLM tool usage currently are the Model Context Protocol ([MCP](https://www.anthropic.com/news/model-context-protocol)) and the SKILLS.md mechanism(an intro can be found [here](https://gofastmcp.com/servers/providers/skills)). These standards are designed as lightweight mechanisms to allow LLM agents to call external software tools in pursuit of a given goal. MCP server-based tools suffer from a context bloat problem that can be mitigated using dynamic tool detection. The most important software tools in systems biology currently have no integrations available to make them available to LLM agents. Neo4J has an [official](https://neo4j.com/developer/genai-ecosystem/model-context-protocol-mcp/#neo4j) MCP server that allows an LLM to query and manipulate graph databases.
Access to API tokens for open-weight models hosted in compliance with the GDPR can be made available for the duration of the project.

GEMs, like all formal models, have large potentials as curated, focused organism databases, as well as hypothesis generating oracles. Unlike with LLMs, their "responses" are fundamentally deterministic and mechanistic, grounded in knowledge. Their accessibility and usability however is severely limited by the sheer complexity and number of tools and databases involved. Furthermore, the idiosyncratic nature of lines of inquiry into a model usually means each analysis is (at least partially) as unique a gem as the GEM it investigates.

### Goal
In this project, LLMs are not supposed to replace systems biology modeling, but to lower the cost of doing it correctly.

1. MCP Servers and/or SKILLS.md documentation for at least these reconstruction and analysis tools are made available:
- CarveMe
- COBRApy
- MEMOTE
- [refineGEMs](https://github.com/draeger-lab/refinegems)
- Cytoscape

2. A portable project setup (docker-compose.yml in case of MCP, clonable repo in case of skills + Neo4J database and MCP container setup) is made available, to minimize friction for users. The ideal is to have a single "install button" that would require little more than an API token from the user.

3.  This setup is used in co

*[truncated]*

---

## #278: Advancing Web-Based SBGN Editing and Visualization

**Labels:** JavaScript, Cytoscape.js, Difficulty: Medium, Size: 175h

### Background
[The Systems Biology Graphical Notation (SBGN)](https://sbgn.github.io/) is a standardized visual language developed to represent biological networks, providing a clear and consistent way to depict complex systems. It consists of three complementary notations: Process Description (PD), Activity Flow (AF) and Entity Relationship (ER). The associated file format, Systems Biology Graphical Notation Markup Language (SBGNML), is an XML-based standard that enables the sharing, reuse, and computational analysis of these diagrams. The scope of this project focuses on the PD and AF languages.

At present, web-based editing of SBGN diagrams is mainly done by using [Cytoscape.js](https://js.cytoscape.org/) library. Several libraries exist to convert SBGNML to [Cytoscape.js](http://cytoscape.js/), such as [sbgnml-to-cytoscape](https://github.com/PathwayCommons/sbgnml-to-cytoscape). However, converting diagrams from Cytoscape.js back to SBGNML remains challenging. [One such converter](https://github.com/iVis-at-Bilkent/sbgnviz.js/blob/master/src/utilities/json-to-sbgnml-converter-factory.js) exists within the [sbgnviz.js](https://github.com/iVis-at-Bilkent/sbgnviz.js) library, but it is tightly coupled to a specialized fork of Cytoscape.js, making it difficult to reuse or integrate into other applications. We have an initial attempt to separate that code and use it independently as in [here](https://github.com/sciluna/image-to-sbgn-analysis/blob/main/dataset/cytoscape-to-sbgnml.js), but currently it is not a proper library itself.

In addition, the [cytoscape-sbgn-stylesheet](https://github.com/PathwayCommons/cytoscape-sbgn-stylesheet) library enables visualization of Cytoscape.js graphs in SBGN-compliant notation. Currently, this stylesheet supports only PD language. We have also an attempt to add support for AF language as well [here](https://github.com/hasanbalci/cytoscape-sbgn-stylesheet), But it currently doesn't support unit of informations in biological activity nodes and also it may have some missing glyphs from both PD and AF. 

Related to these efforts, the Systems Biology Layout & Rendering Service ([SyBLaRS](https://github.com/iVis-at-Bilkent/syblars)) is a web service designed to compute layouts for SBGNML diagrams (as well as some other formats) and to generate corresponding visual outputs in JPG, PNG, or SVG formats. SyBLaRS currently accepts SBGNML as the input by using [sbgnml-to-cytoscape](https://github.com/PathwayCommons/sbgnml-to-cytoscape) and returns the updated node positions in JSON format. Due to the limitations of the existing [cytoscape-sbgn-stylesheet](https://github.com/PathwayCommons/cytoscape-sbgn-stylesheet) SyBLaRS currently supports only the SBGN PD language.   

### Goal
The goals of this project are to:

- Extract the Cytoscape.js to SBGNML conversion functionality into a standalone library, or integrate it into the [sbgnml-to-cytoscape](https://github.com/PathwayCommons/sbgnml-to-cytoscape) library, to impr

*[truncated]*

---

## #277: Improve the Validation of SBGN Diagrams

**Labels:** JavaScript, Python, XML, SBGN, Difficulty: Medium, Size: 175h

### Background 

Systems Biology Graphical Notation (SBGN) is a standard language for representing biological pathways with SBGNML being the exchange and storage format for SBGN. SBGN diagrams are created using the developed SBGN editors (Newt, CellDesigner, SBGN-ED etc.), and they can be saved as the XML-based SBGNML files. The specification that defines the rules governing SBGN can be difficult for many users. Validation tools can the ability of users to create clear SBGN diagrams that are unambiguous. Programmatic validation of SBGN is encoded in the Schematron language that can validate XML documents through an XSLT transformation; XSLT transformation is available in a variety of programming languages. 

### Goal

The goal of the project improve the validation of SBGN documents (and extend it if needed, by re-examining the SBGN specifications). Furthermore, an objective is also to update validation in common SBGN tools like Newt (written in Javascript) with any improvements. Possible improvements include 

1. Clarification to the diagnostic information provided for individual rules that help user understand rule failures,
2. Addition of missing rules (needs re-examination of SBGN specs)

#### Starting point

Make sure you can run the Schematron validation in either Python or Javascript for example diagrams. 

### Difficulty Level: Medium

Difficulty is based on the having and understanding basics of SBGN

### Size and Length of Project

* Medium: 175 hours

### Skills

Essential skills: Javascript or Python, XML  

### Public Repository

* https://github.com/sbgn/libsbgn/tree/master/validation
* https://github.com/sciluna/sbgn_dataset_generator
* https://sbgn.github.io/ (specification exist here)

### Potential Mentors

* Augustin Luna (augustin AT nih.gov)

---

## #276: Improving and Testing Software for Hybrid Mathematical Models and Machine-Learning to Predict Cell Network Dynamics

**Labels:** Python, Difficulty: Hard, Modeling, Size: 350h

### Background
Uncovering the equations that govern the network dynamics of biological systems is both a major challenge and incredibly important because it reveals the mechanisms and patterns that drive complex underlying processes. Various strategies have been developed to discover these equations. For example, our team has developed CellBox, a hybrid approach that combines explicit mathematical models of cell dynamics with a machine-learning framework. Other related approaches that fall under the umbrella of symbolic regression to search for mathematical expressions that best fits a given dataset.

### Goal
The goal of the project existing quantitative biological models described using systems biology standards in combination with existing "symbolic regression" methods to both test and improve these methods. 

### Difficulty Level: Hard
Difficulty is based on the having and understanding of symbolic regression and an understanding biological mathematical modeling to make sense of resulting models. 

### Size and Length of Project
* Large: 350 hours

### Skills
* Essential skills: Python  
* Nice to have skills: Symbolic regression frameworks, biological mathematical modeling

### Public Repository
* https://github.com/sanderlab/CellBox (https://pubmed.ncbi.nlm.nih.gov/33373583/)

### Potential Mentors
* Augustin Luna (augustin AT nih.gov)

---

## #275: openPIP 2.0: Modernizing the Open-source Protein Interaction Platform

**Labels:** PHP, Cytoscape, JavaScript, Python, Cytoscape.js, SQL, Difficulty: Medium, Django, Docker, Symfony, Size: 350h

### Background
[openPIP](https://openpip.usask.ca/) is an open‐source web portal for storing, visualizing and sharing protein–protein interaction (PPI) data. As currently implemented, it uses a LAMP/Symfony stack (PHP, JavaScript, etc.) and relies on the [PSI-MI tabular format](https://code.google.com/archive/p/psimi/wikis/PsimiTab27Format.wiki). After a decade of incremental updates, the codebase and interfaces are outdated. In this project, we want a complete rewrite of openPIP (“openPIP 2.0”) to use modern frameworks and extend its capabilities. This will improve maintainability and allow new features such as support for diverse molecular interaction data.

### Goal
the new openPIP 2.0 will be built with modern web frameworks (e.g. Python/React) and containerization, replacing the old PHP/Symfony codegithub.com. It will feature a revamped admin/upload interface and support for multiple interaction formats and types. 

**Enhanced Data Upload and Interaction Support**
The new platform will improve data handling. Currently openPIP assumes binary PPI data in the PSI-MI TAB format. We will extend this to support multiple molecular interaction data types and formats:
**• Standard formats:** In addition to PSI-MI-TAB, we will also accept a simpler tabular format (CSV file).
**• Improved upload UI:** Implement a drag-and-drop or bulk upload interface with real-time validation and progress feedback. 
**• Metadata and annotation:** Support importing molecules information from public databases.


### Difficulty Level
Medium 
The current codebase was updated several times and the documntation of the code is not deep enough to make it easy to go throug this codebase. 

### Size and Length of Project
large: 350 hours, 22 weeks

### Skills
To modernize openPIP while preserving its ease of use, we will adopt current web technologies. For example:
**• Backend:** Use Python (e.g. Django or Flask) or Node.js (Express) for the server. The original openPIP backend was PHP/Symfony, which could be replaced for better performance and community support.
**• Frontend:** Use a modern JavaScript framework (such as React or Vue.js) for a dynamic user interface, combined with visualization libraries (Cytoscape.js) for network graphs. 
**• Database/Storage:** Continue with a robust SQL database (MySQL/PostgreSQL). Docker containerization (already available in current openPIP) will be used to simplify deployment on cloud or cluster environments.

### Public Repository and Resources
[openPIP Repository](https://github.com/BaderLab/openPIP)
[openPIP website](https://openpip.usask.ca/)
[openPIP Paper](https://www.sciencedirect.com/science/article/pii/S0022283622001838)

### Potential Mentors
[Mohamed Helmy, VIDO, University of Saskatchewan](https://github.com/nrnb/GoogleSummerOfCode/mohamed.helmy@usask.ca)
[Gary Bader, University of Toronto](https://github.com/nrnb/GoogleSummerOfCode/gary.bader@utoronto.ca)

---

## #273: Migrating the Graphspace UI with modern stack like Next.js + React

**Labels:** JavaScript, HTML, Difficulty: Medium, CSS, GraphSpace, Size: 175h

### Background
[GraphSpace](http://graphspace.org/) is an easy-to-use web-based platform collaborating research groups can use for storing, interacting with, and sharing networks. A GraphSpace user can upload graphs through a REST API, import graphs created in Cytoscape, interact with graphs (view them, customize layouts, and save layouts), share graphs (create groups and add collaborators, share graphs among all members of a group or with the world), search graphs, and organize graphs using tags. GraphSpace has a comprehensive REST API that allows users to communicate programmatically with it. Overall, GraphSpace provides a rich set of user-friendly features designed to enhance network-based collaboration.

---

### Goal
This project aims to **modernise and future-proof the GraphSpace frontend** by migrating the existing JavaScript-based UI to a **Next.js + modern React stack**. The goal is to improve **developer experience, long-term maintainability, scalability, and UI consistency**, while establishing a clean and extensible frontend architecture for future feature development.

* **Rebuild GraphSpace UI with Next.js + Modern React:**  
  Migrate the existing frontend to **Next.js (App Router)** with a clean, modular design system.

* **Adopt a modern frontend foundation:**  
  Introduce **TypeScript** for type safety, **ESLint/Prettier** for consistent code quality, and modern styling solutions such as **Tailwind CSS or CSS Modules**. Optionally integrate a component library like **shadcn/ui or MUI** where appropriate.

* **Establish scalable frontend patterns:**  
  Implement a **feature-based folder structure** (routes/pages → features → components → services) and build shared UI primitives along with reusable GraphSpace-specific components such as graph lists, graph viewers, node/edge panels, filters, and controls.

* **Improve UX, accessibility, and responsiveness:**  
  Ensure the UI is fully responsive, follows **basic WCAG accessibility guidelines**, and provides a consistent, intuitive user experience across the platform.

---

### Difficulty Level
**Medium**

---

### Size and Length of Project
- **Medium: 175 hours**
- **12 weeks**

---

### Skills
[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)  
[React](https://react.dev/)  
[Next.js](https://nextjs.org/)  
[TypeScript](https://www.typescriptlang.org/)  
[HTML & CSS](https://developer.mozilla.org/en-US/docs/Web)  
[Modern CSS (Tailwind CSS / CSS Modules)](https://tailwindcss.com/)  

---

### Public Repository
https://github.com/Murali-group/GraphSpace/

---

### Potential Mentors
[Yash Agarwal](https://github.com/yash170106065)  
[Mahesh Kasbe](https://github.com/maheshkasabe)
[Daniyal Jahan Warsi](https://github.com/jahandaniyal)  


---

### IRC
Discord for GSoC 2026: https://discord.gg/AqjnwHndq8
Gitter for community: https://gitter.im/graphspace/community?utm_source=share-link&utm_medium=link&utm_campaign=share-link

---

## #264: Direct GitHub Integration from PathVisio to WikiPathways

**Labels:** WikiPathways, Java, PathVisio, Difficulty: Medium, Size: 175h, GPML, GUI, GitHub

### Background
WikiPathways (https://www.wikipathways.org/) is a collaborative platform for pathway curation in biology, supporting community-contributed models of biological processes. Recently, WikiPathways migrated its entire database and website to GitHub (https://github.com/wikipathways), embracing a more open and modern infrastructure.

However, the current pathway curation workflow in PathVisio, the desktop pathway editor, is still tied to outdated systems. This project proposes developing a new PathVisio plugin that directly connects to the GitHub-hosted WikiPathways repository. It will allow users to commit new pathways and edits directly to GitHub from within PathVisio, streamlining the contribution process and supporting the future infrastructure of WikiPathways.

### Goal
The end result will be a new PathVisio plugin that:

* Authenticates users via GitHub
* Enables users to create commit requests with new or edited pathway models (GPML files) directly from PathVisio
* Interacts with the GitHub API to create pull requests against the appropriate WikiPathways repository
* Optionally, integrates GitHub Actions to validate submissions (e.g., file format checks, metadata completeness)
* Provides clear UI/UX for biologist users unfamiliar with Git systems

The plugin will align with the workflow of the new GitHub-based WikiPathways platform, replacing the legacy submission mechanism.

### Difficulty Level: Medium
The project requires Java development experience, understanding of GitHub API interactions, and some knowledge of Git workflows. It is moderately complex due to handling authentication, GitHub API requests, and integration into an existing Java-based desktop application.

### Size and Length of Project: 
- **medium: 175 hours**
- **12 weeks**

### Skills
Essential Skills:
* Java (PathVisio plugin development)
* GitHub API usage
* Basic understanding of Git workflows

Nice to have Skills:
* Familiarity with GitHub Actions
* Experience with biological data or pathway models (GPML format)
* UI/UX design for non-technical users

### Public Repository
The new plugin will be developed under the PathVisio GitHub organization, e.g.:
https://github.com/PathVisio/WP-GitHub-Plugin (new repo to be created)

Reference to legacy plugin: https://github.com/PathVisio/WP-plugin

### Potential Mentors
[Martina Summer-Kutmon](https://github.com/mkutmon)

---

## #262: Curation Support Tools for the Creation of a Lung Cancer Disease Map

**Labels:** Python, Difficulty: Medium, Size: 175h, LLM

### Important Note
Look at Getting Started before asking questions.

### Background
Similar to other professions, biologists need fast and reliable ways of summarizing massive amounts of research content found in literature. AI agents that produce detailed, factual, and unbiased research reports with citations are highly important. Tools like OpenAI Deep Research are steps in this direction along with open-source tools like the  GPT-Researcher (https://github.com/assafelovic/gpt-researcher). One particular common type of report seeks to understand the biological networks involved in particular diseases or other processes. Communities like DiseaseMaps (https://disease-maps.io/projects/) seek to do this at the scale of diseases like Parkinson's disease which include both written material (https://pmc.ncbi.nlm.nih.gov/articles/PMC4153395/) and interactive diagrams (https://pdmap.uni.lu) that often become the source for mathematical models.

### Goal
The goal of the project develop additional features or fine-tuning capabilities for gpt-researcher to support the automatic generation of reports for the curation of disease maps. The Related Links has a list of potential resources, including examples of existing reports and automatically generated reports as well as resources (e.g., EMMAA) that remain inaccessible to current state of the art tools like Deep Research. 

### Getting Started
1. Read the entirety of this Project Description. 
2. Look at Getting Started, Goal and Related Links (especially Deep Research versus Human). 
3. Compare GPT-Researcher and Deep Research in versus the human reports (Related Links).
4. Write a feasible proposal draft that outlines at some of the differences you see between automated and human reports and presents a plan to address this subset of differences. 

**Important:** Avoid asking the generic questions such as how to start or if you can work on this project; just write a draft proposal if interested; draft feedback can be provided. Also, good proposals tend to have basic demonstrative code or point to specific code that will be enhanced/modified.

### Difficulty Level: Medium
This is a more open-ended project; it will require a proposal that is focused enough to be achievable during the time frame. 

### Size and Length of Project
- **medium: 175 hours**
- **12 weeks**

### Skills
* Essential skills: Python
* Nice to have skills: Javascript

# Related Links
* https://github.com/assafelovic/gpt-researcher
* Collections of automatically extracted interactions for diseases (including lung cancer): https://emmaa.indra.bio/
* Deep Research versus Human: Deep Research: https://drive.google.com/file/d/19z-PIz3JQLlOlv1wj-tFTgtK0px2-rqg/view?usp=sharing Human: https://pmc.ncbi.nlm.nih.gov/articles/PMC3898398/
* Example Reports: 
 * https://disease-maps.io/projects/
 * Lung Cancer Report (try to replicate this): https://link.springer.com/article/10.1007/s00335-025-10110-6 
 * SIRT1/PARP1: https://pmc.ncbi.nlm.nih.gov/arti

*[truncated]*

---

## #254: Refactor Cytosnap to use Playwright

**Labels:** JavaScript, Cytoscape.js, Canvas, Difficulty: Easy, Size: 175h

### Background
Describe the current state of the project and the main problem or issue being addressed by the proposed idea. Details should include links and references. 

- [Cytosnap](https://github.com/cytoscape/cytosnap) is a package to render and export [Cytoscape.js](https://js.cytoscape.org) graphs as various image formats.
- Cytosnap currently uses [Puppeteer](https://pptr.dev) to do this, and Puppeteer has several maintenance and compatibility issues.
- [Playwright](https://playwright.dev) is a newer alternative to Puppeteer, which would address these issues.
- [Skia Canvas](https://skia-canvas.org) is a lighter-weight alternative to Puppeteer and Playwright, which could simplify deployment.  Skia Canvas only supports rendering the HTML5 `<canvas>` API as an exported image, whereas Playwright includes a full browser environment.

### Goal
Describe what the end result of the GSoC project should be.

1. Refactor Cytosnap to use Playwright instead of Puppeteer.
2. Add [Playwright tests](https://playwright.dev/docs/intro) to ensure that the refactored Cytosnap project is working properly according to [the Cytosnap public API](https://github.com/cytoscape/cytosnap).
3. [Configure GitHub Actions](https://docs.github.com/en/actions) to automatically run the new Playwright tests on new commits and pull requests.
4. Add support for using Skia Canvas.
  1. This would be enabled with an option like `engine: 'skia'`.
  2. Use Playwright if the user specifies `engine: 'playwright'`.  Cytosnap should support both.
  3. Mark Skia Canvas and Playwright as optional dependencies.  The user can decide which to install based on which he wants to use in his project.
5. Add automated tests using Mocha for `engine: 'skia'`.

### Difficulty Level: Easy/Medium/Hard
Give a difficulty level, either Easy, Medium or Hard. Make sure to tag the issue with this difficulty.
Describe with a sentence or two why the project is this difficulty level.

Easy if:

- The applicant has prior experience with JS and Node.js.
- The applicant has experience with JS build systems, like Webpack or Vite.

### Size and Length of Project
Define the project commitment as either “small: 90 hours", "medium: 175 hours" or "large: 350 hours" and the timeline between 10 and 22 weeks, for example: 
- **medium: 175 hours**
- **12 weeks**

Note that the project length for small projects should be 10-12 weeks.

### Skills
List skills/technologies that the student should be familiar with. Also tag the issue with these.

Essential skills: 

- JS (significant experience with the language & modern tooling)


Nice to have skills, from most to least important: 

- The HTML5 canvas API
- Headless browsers / rendering: Puppeteer, Playwright, Skia Canvas, Selenium, etc.
- Build systems like Webpack or Vite
- GitHub Actions

### Public Repository
Link to a public, open-source repository for your project. _All code from accepted projects must be open source and public throughout the coding period and beyond._

*[truncated]*

---

## #248: COBRAxy: constraint-based metabolic modeling in Galaxy

**Labels:** Python, Difficulty: Medium, Size: 175h, Galaxy

### Background
Galaxy is an open-source platform designed to make advanced bioinformatics analyses accessible and reproducible. Among its many applications, constraint-based metabolic modeling (CBM) plays a pivotal role in exploring cellular metabolism through predictive simulations of flux distributions in metabolic networks.

COBRAxy is an evolving project conceived as a unifying framework for constraint-based metabolic analysis within the Galaxy ecosystem. Its long-term goal is to act as a collector and integrative hub for tools implementing COBRA-based methods, with a particular focus on the integration of omics data into genome-scale metabolic models. By leveraging Galaxy workflows, COBRAxy aims to make advanced metabolic modeling approaches accessible, reproducible, and usable by researchers without extensive programming expertise.

Beyond its current functionalities, COBRAxy is designed to be extensible and to progressively incorporate alternative constraint-based integration strategies proposed in the literature, fostering a comprehensive and modular ecosystem for COBRA analysis in Galaxy.

At present, the COBRAxy tool suite enables the comparison of metabolic flux distributions across conditions or populations, based on transcriptomic information. The tool also supports the integration of medium composition information to define nutrient availability and exchange constraints based on common commercial growth media.
Additionally, COBRAxy supports visualization of flux differences on user-defined metabolic vectorial maps. 

However, transcriptomics data integration strategies are currently limited to flux capacity constraint approaches, coupled with sampling-based methods, including corner-based sampling and hit-and-run sampling.

Moreover, the tools are primarily focused on bulk RNA-seq data and do not yet fully support single-cell RNA-seq (scRNA-seq) or spatial transcriptomics data. High-resolution single-cell and spatial data offer unprecedented opportunities to study metabolic heterogeneity and spatially localized metabolic activities, but require significant adaptations to workflows and computational tools.
Finally, there is a need to improve the computational efficiency of sampling algorithms.

This project aims to address these gaps by extending COBRAxy capabilities to support single-cell and spatial data integration, alternative integration strategies, and optimizations to statistical testing and computational efficiency.

### Goal
This project builds on the foundation of COBRAxy, a Galaxy tool suite designed for metabolic network modeling, expanding its scope to:
1.	Support single-cell metabolic analysis: Implement models like scFBA, which integrate transcriptomics data into population-based flux models to capture metabolic heterogeneity at single-cell resolution.
2.	Integrate spatial transcriptomics workflows: Enable mapping of metabolic activities onto physical tissue architectures and co-localization analyses.
3.	Improve comput

*[truncated]*

---

## #247: Improving Cytoscape.js layout utilities

**Labels:** JavaScript, Cytoscape.js, Difficulty: Hard, Size: 175h

### Background
Using graphs in the visual analysis of relational data has proven to be very important. Such visualization is only effective when graphs that are created on the fly can be automatically laid out in a nice, understandable fashion. Not only that, changes to such graphs over time should also be nicely integrated into an existing layout without destroying the user's mental map.

[Cytoscape.js](http://js.cytoscape.org/) is a highly popular and widely used graph library for visualizing relational data in various domains including biology. It comes with many layout extensions. In addition, [a utility library](https://github.com/iVis-at-Bilkent/cytoscape.js-layout-utilities) to support these layout extensions was developed to further improve the layout support of a visual software component. This library for instance can help for compactly bringing components of a disconnected graph.

### Goal
The goal of this project is to improve the existing functionality in choosing *good* initial locations for any new graph elements on evolving/changing graphs.

### Difficulty Level: Hard
This project requires CS background to understand description of some new algorithms and choosing the right data structures to implement them.

### Size and Length of Project
- **medium: 175 hours**
- **12 weeks**

Note that the project length for small projects should be 10-12 weeks.

### Skills
Essential skills: JavaScript, understanding of graph algorithms
Nice to have skills: Cytoscape.js

### Public Repository
https://github.com/iVis-at-Bilkent/cytoscape.js-layout-utilities

### Potential Mentors
Ozgun Babur
Ugur Dogrusoz

---

## #245: Assisting the creation of SBGN diagrams using large language models (LLMs)

**Labels:** JavaScript, SBGN, HTML, Difficulty: Medium, CSS, Size: 175h, LLM

### Background
Systems Biology Graphical Notation ([SBGN](https://sbgn.github.io/)) is a standard language for representing biological pathways with SBGNML being the exchange and storage format for SBGN. SBGN diagrams are created using the developed SBGN editors ([Newt](https://newteditor.org/), [CellDesigner](https://www.celldesigner.org/), [SBGN-ED](https://kim25.wwwdns.kim.uni-konstanz.de/vanted/addons/sbgn-ed/) etc.) and they can be saved as SBGNML files. However, using these editors can sometimes be a difficult process, especially for those who try to use them for the first time, due to their complicated menus and toolbars. In addition, creating an SBGN map drawn on a paper or on a tablet during a meeting or lab discussion again to save it as SBGNML requires extra time and effort. To overcome these issues, we are developing a service and sample app ([Image-to-SBGN Converter](https://github.com/sciluna/image-to-sbgn)) to automatically convert hand-drawn SBGN maps to SBGNML by utilizing large language modes (LLMs). In addition to the conversion, this tool also allows user to see the resulting converted diagram and shows node-related information (see figure). 

<img width="1146" alt="Screenshot 2025-01-10 at 8 26 53 AM" src="https://github.com/user-attachments/assets/7ae23423-7832-4a3f-8b9c-427130a81e71" />


### Goal
The goal of the project is to add some features to our app that will make the job of users easier before and after conversion and enable them to get more efficiency. These features include but are not limited to:

- Adding more conversion-related options to the Settings section
- Adding a quick edit feature if the result of the conversion has missing/wrong nodes/edges
- Providing functionality to open the converted map in an SBGN editor such as Newt for advanced editing
- Providing more detailed information about nodes and edges in Object View
- Adding layout options

### Difficulty Level: Easy-Medium
Difficulty of the required features range from easy (making UI edits) to medium (using Cytoscape.js extensiones or querying data via REST API). 

### Size and Length of Project
- **medium: 175 hours**
- **12 weeks**

### Skills

Essential skills: JavaScript, HTML/CSS, Node.js
Nice to have skills: Cytoscape.js, LLM APIs (GPT, Gemini, Ollama etc.) 

### Public Repository
https://github.com/sciluna/image-to-sbgn

### Potential Mentors
Hasan Balci
Augustin Luna

---

## #241: Getting the complexity score from SBOL files to streamline DNA synthesis using standards

**Labels:** Python, Difficulty: Medium, SBOL, Size: 175h

### Background
Synthetic biologists use the Design, Build, Test, Learn (DBTL) cycle to engineer biological systems. The Synthetic Biology Open Language ([SBOL](https://sbolstandard.org/)) was developed by the community as a standard to represent biological designs and covers the whole DBTL cycle. Although this standard is used and agreed by the community it is mostly used in its visual format and the data format has not been widely adopted, being PDF the primary format to share DNA sequences [1]. The adoption of SBOL [2] by the community can increase the reproducibility of experiments, facilitating building upon previous knowledge. 
To streamline the DBTL cycle and increase the adoption of SBOL we propose the development of a function in SBOL-utilities that allow researchers to easily check synthesizability by different synthesis providers.

[1] Mante, J., Myers, C.J. Advancing reuse of genetic parts: progress and remaining challenges. Nat Commun 14, 2953 (2023). https://doi.org/10.1038/s41467-023-38791-0
[2]Buecherl, Lukas, Mitchell, Thomas, Scott-Brown, James, Vaidyanathan, Prashant, Vidal, Gonzalo, Baig, Hasan, Bartley, Bryan, Beal, Jacob, Crowther, Matthew, Fontanarrosa, Pedro, Gorochowski, Thomas, Grünberg, Raik, Kulkarni, Vishwesh, McLaughlin, James, Mısırlı, Göksel, Oberortner, Ernst, Wipat, Anil and Myers, Chris. "Synthetic biology open language (SBOL) version 3.1.0" Journal of Integrative Bioinformatics, vol. 20, no. 1, 2023, pp. 20220058. https://doi.org/10.1515/jib-2022-0058

### Goal
To build a function to assess the complexity score of DNA sequences in SBOL using [Twist API](https://www.twistbioscience.com/tapi). Develop a function that integrates the previous function with the existing IDT complexity score function to get relevant synthesizability information.

Specific Goals:
A function that uses a SBOL file as input, interfaces the TWIST API, and outputs the complexity score.
Contribute that function to sbol-utilities by adding propper format and tests.
Develop a mediator to encapsulate functions to get complexity score for different providers (TWIST, IDT).
Document the mediator and how to add complexity score calculation for other providers.

### Difficulty Level: Medium
This project involves the understanding of an API, the development of Python functions and integrating them using unittest in the CI/CD workflow of sbol-utilities.

### Size and Length of Project
- **medium: 175 hours**
- **16 weeks**

### Skills
Essential skills: Python
Nice to have skills: API calls, Git, DevOps
### Public Repository
https://github.com/SynBioDex/SBOL-utilities

### Potential Mentors
Gonzalo Vidal (Gonzalo.vidalpena@colorado.edu)
Jake Beal

---

## #233: Cytoscape Automated Testing Suite for Biomedical Visualization

**Labels:** Cytoscape, JavaScript, Python, REST, Difficulty: Medium, Size: 175h

### Background
[Cytoscape](https://www.cytoscape.org/) is an invaluable open-source tool in the field of biomedical research, offering robust data visualization capabilities, particularly for molecular networks. Its ecosystem, enriched by over 370 specialized apps available in the App Store, facilitates diverse functionalities ranging from database access to novel analysis methods. However, the recent development of [Cytoscape Web](https://github.com/cytoscape/cytoscape-web), an online variant, has introduced complexities in maintaining the platform's integrity and quality across versions. As the ecosystem expands, the challenge of ensuring consistent and reliable product releases grows. Thus, the development of sophisticated testing tools becomes imperative to uphold the high standards of Cytoscape's offerings.

### Goal
The primary goal of this project is to create an automated testing framework tailored for Cytoscape, with a specific focus on scientific figure preparation—a critical use case for the software. This framework will utilize a collection of Cytoscape session files and [CX](https://www.cytoscape.org/cx/) documents, integral in generating figures for various scientific publications. It aims to verify whether the newest versions of both Cytoscape and Cytoscape Web can accurately reproduce these figures. A key aspect of this project involves ensuring that figures produced by Cytoscape Web are consistent with those generated by the desktop version. The framework will facilitate communication with Cytoscape Desktop through the [CyRest API ](https://apps.cytoscape.org/apps/cyrest)and automate tests on Cytoscape Web using renowned frameworks like [Playwright](https://playwright.dev/) . A significant part of the testing process will involve comparing newly generated images against established 'gold standard' figures, employing image analysis tools ([OpenCV](https://opencv.org/), [ImageMagick](https://imagemagick.org/index.php)) and advanced language models (such as Gemini and GPT-4) to produce comprehensive test reports.

### Difficulty Level: Medium

### Size and Length of Project

- 175 hours
- 12 weeks

### Skills

Javascript, TypeScript, Python, Cytoscape

### Public Repository

- https://github.com/cytoscape/cytoscape-web
- https://github.com/cytoscape/

### Potential Mentors

- Jing Chen
- Kei Ono
- Dylan Fong
- Chris Churas

---

## #229: Large Network Renderer

**Labels:** Cytoscape, JavaScript, JSON, NDEx, OpenGL, Difficulty: Medium, HiView, Hierarchical network, Size: 175h

### Background
The rise of web-based visualization tools has significantly impacted data interaction, especially in the biomedical sector. However, a major challenge persists: efficiently rendering very large networks, which often comprise 500,000 to 1 million elements, including nodes and edges. Current web visualization tools struggle with such extensive datasets, resulting in performance bottlenecks and limited user interactivity.
The "Large Network Renderer" project seeks to overcome these limitations. This JavaScript library will significantly enhance the Cytoscape Web project by enabling the effective rendering of large-scale [CX](https://www.cytoscape.org/cx/) networks in web browsers. Its key advantage is the capability to manage very large datasets while ensuring fluid performance and interactive user experience. Beyond Cytoscape, "Large Network Renderer" will serve as an indispensable tool for other web applications handling extensive network visualizations, like the [Network Data Exchange](https://www.ndexbio.org/) (NDEx) and [NDEX-IQuery](https://www.ndexbio.org/iquery/). This endeavor is vital for the progression of web-based data analysis tools, empowering researchers to delve into large, complex datasets with newfound depth.

### Goal
The objective of this project is extending  the  initial proof of concept already developed as  a [prototype](https://github.com/idekerlab/large-graph-renderer). Our focus will extend to supporting a list of commonly used visual properties in this renderer. Key tasks will include:
Adding more visualization capability to the renderer

- More basic shapes for nodes
- More supports for the edge type
- Performance Evaluation
- Iterative Optimization
- Documentation
- Examples Creation
- Automated test

This application is built on top of the popular WebGL-based data visualization framework Deck.gl. Since this is a high-level library designed to visualize large data set, you can write the additional features without deep knowledge of WebGL low-level API.

#### How to Start
Interested applicants should:

- Explore libraries/sites/repos mentioned above
- Explore https://deck.gl/ to understand the framework
- Understand the concept of [Layers](https://deck.gl/docs/developer-guide/using-layers) in Deck.gl
- Learn how to create a custom Layers

### Difficulty Level: Medium

### Size and Length of Project
- 175 hours
- 12 weeks

### Skills
 - Javascript / TypeScript
 - Knowledge of WebGL API is a plus, but not required

### Public Repository

- https://github.com/idekerlab/large-graph-renderer
- https://github.com/cytoscape/cytoscape-web
- https://github.com/idekerlab/network-viewer

### Potential Mentors
- Kei Ono 
- Dylan Fong 
- Jing Chen

---

## #223: Cytoscape.js extension template using ESM

**Labels:** JavaScript, Cytoscape.js, Difficulty: Easy, Size: 175h

### Background

[Cytoscape.js](https://js.cytoscape.org/) is a library used to visualise and analyse [networks](https://en.wikipedia.org/wiki/Graph_theory) in the browser or in Node.js.

Problems to solve:

- A lot of JS projects now, and any recent projects, use [ESM](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) (either natively in the browser or with a bundler).  The core [Cytoscape.js](https://js.cytoscape.org/) library supports ESM.  The [extensions](https://js.cytoscape.org/#extensions) do not.
- Someone using ESM would have to do complicated configurations to make the extensions work with a bundler.
- Someone using ESM directly in the browser would have to use workarounds in their own code to make extensions work.  This would not be straightforward, especially for novices.
- It’s difficult for someone to contribute an extension, unless they’re fairly well skilled technically.

Technical background:

- ESM is now the module standard for JS.
- The existing extensions largely use Webpack to build UMD (CJS, AMD, globals).  They should use Rollup to build ESM and UMD in future.
- The main library already uses Rollup to build ESM and UMD.

### Goal

- Build a template extension using a [Github template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository).
- Use your template to update the [main first-party extensions](https://js.cytoscape.org/#extensions).
- Add the template extension to the [documentation](https://js.cytoscape.org/).  A new app author should just click a button to get a new repo for their extension on GitHub.  Then they can just focus on their extension itself.

### Difficulty Level

**Easy**.  It’s straightforward to do.  The core library can be used as a reference.  It’s a laborious process, though.

### Size and Length of Project
Define the project commitment as either "medium: 175 hours" or "large: 350 hours" and the timeline between 10 and 22 weeks, for example: 
- **medium: 175 hours**
- **12 weeks**

### Skills

Essential skills: JS, attention to detail, testing
Nice to have skills: Experience using Cytoscape.js

### Public Repository

https://js.cytoscape.org/

### Potential Mentors

- Max Franz (maxkfranz@gmail.com)
- Mike Kucera (mikekucera@gmail.com)
- Christian Lopes (chrtannus@gmail.com)
- Gary Bader (gary.bader@utoronto.ca)

---

## #219: Prototype COSE Network Layout Algorithm to Support Biological Context for Layouts More Intuitive to Humans 

**Labels:** JavaScript, JSON, Cytoscape.js, Difficulty: Medium, Size: 175h

### Background
Pathway knowledge describing interactions between proteins and other biological molecules is essential for interpreting and integrating diverse genomics data, understanding disease mechanisms and informing medical decision making. Consequently, pathway visualization is very useful for biomedical research. Researchers often visualize pathways with spatial relationships in mind (i.e., proteins on the cell surface at the top and those in the nucleus (the most cell interior) towards the bottom. This spatial information is missing from most generic graph layout algorithms. 

### COSE Layout 
The CoSE (pron. "cosay", **Co**mpound **S**pring **E**mbedder) layout for [Cytoscape.js](https://js.cytoscape.org/) developed by [i-Vis Lab](http://cs.bilkent.edu.tr/~ivis/) in Bilkent University is a spring embedder layout with support for compound graphs (nested structures) and varying (non-uniform) node dimensions. A faster version of this layout style called fCoSE, also supporting user-defined placement constraints can be found [here](https://github.com/iVis-at-Bilkent/cytoscape.js-fcose).
([demo](https://raw.githack.com/cytoscape/cytoscape.js-cose-bilkent/master/demo.html), [compound demo](https://raw.githack.com/cytoscape/cytoscape.js-cose-bilkent/master/demo-compound.html)). 

Citation: U. Dogrusoz, et al, "[A Layout Algorithm For Undirected Compound Graphs](http://www.sciencedirect.com/science/article/pii/S0020025508004799)", Information Sciences, 179, pp. 980-994, 2009.

Video: fCOSE: https://www.youtube.com/watch?v=vRZVlwntzGY

### Gene Information using Gene Ontology (GO)

The [Gene Ontology](http://geneontology.org/docs/introduction-to-go) knowledgebase provides a computational representation of our current scientific knowledge about the functions, localization, and involved processes for genes. 

Example Gene Localization: https://www.genecards.org/cgi-bin/carddisp.pl?gene=ITGB4#localization-ptm

GO is an immense hierarchy, but it can be simplified to include a reduced set of terms: 

* Cellular Compartment Hierarchy (Nucleus): https://www.informatics.jax.org/vocab/gene_ontology/GO:0005634
* GO Subsets (GO Slim): http://geneontology.org/docs/download-ontology/
* Generate a GO Slim: https://github.com/owlcollab/owltools/wiki/Map2Slim

### Goal
The goal is to prototype an updated version of this algorithm that includes spatial information and makes automatic use of this information for layout purposes. 

### How to Start 
Interested applicants should: 

1. Explore libraries/sites/repos mentioned above
2. Explore code base for fCOSE
3.  Develop a proposal for incorporating GO information into fCOSE

### Difficulty Level: Medium

### Size and Length of Project
175 hours
12 weeks

### Skills
Javascript

### Public Repository
* https://github.com/iVis-at-Bilkent/cytoscape.js-fcose
* https://github.com/cytoscape/cytoscape.js

### Potential Mentors
* Augustin Luna ({first_name}_{last_name} AT hms.h

*[truncated]*

---
