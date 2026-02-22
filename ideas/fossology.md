# FOSSology — Project Ideas

**Source:** https://github.com/fossology/fossology/discussions/3267
**Scraped:** 2026-02-22T23:28:47.598212

---

# Google Summer of Code 2026 application #3267

[shaheemazmalmmd](https://github.com/shaheemazmalmmd)started this conversation in

[Ideas](/ideas/fossology/categories-ideas)

-

|
Hello all! FOSSology as an org is planning to apply for Since 2022, there are some changes made by Google in the program. You can read more about it on - Three sized projects are acceptable by program:
- Small sized projects (~90 hour)
- Medium sized projects (~175 hours)
- Large projects (~350 hours)
- The program is open to 18 years and older people.
- No longer limited to college students only.
- Flexible time lines between 12 and 22 weeks.
Also, starting this year, 2026, Google has strong advice about the usage of Generative AI in the GSoC program. Please check them at: **For Mentoring Orgs:**[Usage of AI tooling in Google Summer of Code 2026 (for Mentoring Orgs)](https://docs.google.com/document/d/1jglptdn_DovOxjwuhzORn3QhYoeBcToS7ymk3IIWHKY/edit?usp=sharing)**For Contributors:**[Guidance for GSoC Contributors using AI tooling in GSoC 2026 doc](https://docs.google.com/document/d/1t9GcIBnNXPNO6klRQvU8pL8-uV6afzLo6JUAM299suA/edit?usp=sharing)
Based on the suggestions from Google, FOSSology has following guidelines for GSoC contributors: -
**Usage of AI in proposal writing:**The proposal writing is a core part of the GSoC program and it should never be offloaded to the AI completely. This is the place where you would most probably meet the organization for the first time and show your creativity, so use this space wisely.- Generative AI usage is allowed, but to do tasks like formatting, rearranging, etc.
- Usage of Generative AI is strictly prohibited for creating the proposal idea itself (includes the end goal, the approach) and proposal will be penalized if such usage found.
-
**Usage of AI in coding:**We have seen in previous contributions that people do not install FOSSology at all while they are working on their contributions. If you cannot see the tool, if you cannot test your changes, how can you validate the changes you have done are correct. It then becomes the responsibility of the maintainer to do a thorough testing, always, which takes more time than for the person contributing the changes. AI also does not know everything. Even if you are using coding agents to help you, but you cannot provide them the right input, their output will only be garbage.- For you first few PR, we require you to provide evidence of FOSSology installation by providing information like FOSSology version, screenshot/example output from the changes.
- Taking help from AI is fine, but completely relying on it is not good for the project and for you.
- Take suggestions from the AI, but always understand changes before pushing them. If you cannot understand the code generated, do not push it.
- If you are pushing the code, you are responsible for it, it does not matter a human wrote it or an AI. Thus, take your contributions seriously. We like to work with humans more than machines.
- If the code changes are not clear and without any human explanation, the maintainers hold the rights to close the PR without further explanation.
-
**Acceptance criteria:**FOSSology previously did not have defined acceptance criteria, in order to keep the application process open and accessible to everyone. However, over the past year, this approach resulted in a large number of proposals that became difficult to manage effectively. Therefore, starting this year, we are introducing the following criteria that proposals/contributor must meet in order to be considered:- There should be at least one contribution with significant enough changes (simple typo fix for example do not qualify).
- If you could not have created a PR, you should at least had communicated with one of the Org member and they should vouch for you.
- Prior to final submission of proposal, applicants must have their proposal draft reviewed by an Org member.
Please feel free to drop any questions here (or start a new discussion) you have regarding the program, you want to submit a proposal idea, you want to be mentor in the program, etc. While submitting a project idea, please tag it to be "Medium" or "Large" sized and who you'll prefer working on it "student" or "professional". [https://google.github.io/gsocguides/mentor/defining-a-project-ideas-list](https://google.github.io/gsocguides/mentor/defining-a-project-ideas-list)[https://google.github.io/gsocguides/mentor/making-your-ideas-page](https://google.github.io/gsocguides/mentor/making-your-ideas-page)[https://google.github.io/gsocguides/student/](https://google.github.io/gsocguides/student/)[https://opensource.googleblog.com/2024/10/celebrating-20-years-google-summer-of-code-nurturing-next-generation-contributors.html](https://opensource.googleblog.com/2024/10/celebrating-20-years-google-summer-of-code-nurturing-next-generation-contributors.html)
You can also check the detailed documentation of previous students from Here is the list of the people who would be volunteering as mentors & org-admins for GSoC-2026. [@EttingerK](https://github.com/EttingerK)(OrgAdmin)[@shaheemazmalmmd](https://github.com/shaheemazmalmmd)(OrgAdmin)[@GMishx](https://github.com/GMishx)(OrgAdmin)[@Kaushl2208](https://github.com/Kaushl2208)(Mentor)[@hastagAB](https://github.com/hastagAB)(Mentor)[@avinal](https://github.com/avinal)(Mentor)[@its-sushant](https://github.com/its-sushant)(Mentor)[@JanAltenberg](https://github.com/JanAltenberg)(Mentor)[@sjha2048](https://github.com/sjha2048)(Mentor)[@soham4abc](https://github.com/soham4abc)(Mentor)
Want to mentor this GSoC-2026? Please contact OrgAdmins. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

## Replies: 13 comments 18 replies

-

|
Some useful links for contributors who Are first time here : - Basic workflow -
[https://www.youtube.com/watch?v=TZqU5ZALI7U](https://www.youtube.com/watch?v=TZqU5ZALI7U) - Installation -
[https://github.com/fossology/fossology/wiki/Install-from-Source](/ideas/fossology/fossology-fossology-wiki-install-from-source) - Good first issues -
[https://github.com/fossology/fossology/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22](/ideas/fossology/fossology-fossology-issues) - Slack channel -
[https://fossology.slack.com/](https://fossology.slack.com/)
|

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

## Idea!## Title: Enhancing Nirjas & Atarashi for Accurate, Scalable License Intelligence## Goal: Improve license detection modal of Atarashi, create a new model in Nirjas to classify comments and integrate it to Atarashi.Open-source compliance tools rely heavily on accurate extraction and identification of license information embedded within source code. As software ecosystems grow and diversity, traditional rule-based and heuristic-driven approaches struggle with noisy inputs, partial license texts, modified headers, and non-standard comment formats. - Nirjas focuses on extracting comments from source code across multiple programming languages.
- Atarashi performs license identification using Machine Learning techniques using extracted text against known license data.
While both tools are effective, their current architectures leave room for improvement in accuracy, scalability, and intelligence. This proposal aims to introduce machine learning–driven classification, improved language support, and structured inference logic to significantly enhance license detection quality. -
Challenges in Current Nirjas Workflow - All extracted comments are treated equally, regardless of whether they are actual license text, developer comments, or unrelated documentation.
- License files (e.g., LICENSE, COPYING) represent an edge case and are not consistently handled alongside source comments.
- Support for newer or less common programming languages is limited, reducing coverage.
- This results in noisy downstream inputs and unnecessary computation in license identification stages.
-
Challenges in Current Atarashi Workflow - License identification is performed on the entire file content, including irrelevant or misleading text.
- There is no structured classification of license families or prioritization when multiple licenses are detected.
- Ambiguous or partial license texts are not handled with explicit confidence-based decision logic.
- These issues lead to false positives, ambiguous results, and reduced trust in automated conclusions.
-
Proposed Improvements to Nirjas
-
Machine Learning–Based Comment Classification - A dedicated machine learning model will be designed and integrated into Nirjas to intelligently classify extracted comments.
- Valid license-related comments
- Non-license source code comments
- Noise (e.g., TODOs, documentation blocks, metadata)
-
Expanded Programming Language Support - Nirjas will be extended to support additional programming languages that are currently not handled.
- Modular comment-extraction rules to allow easy onboarding of new languages.
- Special handling for license file edge cases, where the entire file may represent license text rather than comments.
- Unified abstraction to normalize comment outputs across languages.
- Proposed Improvements to Atarashi
-
Comment-Driven License Identification - Instead of analyzing the full file content, Atarashi will:
- Consume only license-relevant comments extracted and classified by Nirjas.
- Ignore irrelevant or noisy text blocks.
- This shifts Atarashi from a brute-force comparison approach to a signal-driven inference pipeline.
-
License Family & Priority Classification - Classify detected licenses into license families (e.g., GPL, MIT, Apache).
- Assign license priority based on:
- Existing license identifications
- Known compatibility rules
- Project-level conclusions
-
ML-Based License Identification Using Minerva Dataset - A machine learning classification model will be trained using the Minerva license dataset.
- Classify arbitrary license text into known license labels.
- Input:
- Arbitrary license text snippets
- Full license texts
- Partial or truncated headers
- Commented or reformatted versions
- Slightly modified license language
- Output:
- One or more license labels with associated confidence scores
- OR an explicit UNKNOWN classification
|

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

## Idea!## Title: Report Aggregation for Compliance## Goal: A new project "Report Aggregation for Compliance" which shall be integrated with FOSSology & SW360 if needed to ease and manage multiple reports.With the introduction of regulations such as the Today, compliance artifacts are often generated as multiple independent reports for example: - ReadMeOSS
- SPDX 2.3
- SPDX 3.0
- CycloneDX / CLIXML
These reports are produced at different stages, by different tools, and for different scopes. Manually managing and reconciling them is time-consuming. -
Current Challenges - Compliance data is fragmented across multiple reports
- No easy way to merge, track, or evolve combined reports
- Any update in a single report requires manual rework
- This creates friction for compliance teams and increases regulatory risk.
-
Proposed Solution: - Introduce a Report Aggregator Tool that enables organizations to combine multiple compliance reports into a single, authoritative report, while preserving traceability and editability. (Many reports in → One aggregated, report out)
- Allow users to merge N number of reports into a single consolidated report
- Support common formats listed above
- Transparent Aggregation View (UI)
- Clearly show which reports are merged
- Display the source and contribution of each report
- Allow users to inspect merged data at a high level
- Users should be able to edit or correct information in the aggregated report
- Changes should be traceable to maintain accountability
- Incremental Updates & Change Propagation
- If a source report changes, the system should:
- Detect the update
- Allow seamless incorporation into the aggregated report
- Avoid rebuilding reports from scratch
- If a source report changes, the system should:
-
Ecosystem Integration - Integration with FOSSology
- Aggregate outputs from multiple uploads or projects into one report.
- Integration with SW360
- Align aggregated reports with component and project metadata.
- Integration with FOSSology
|

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

## Idea!## Title: Enhanced Reuse Agent for Intelligent License Reuse## Goal: Create a new agent once all the agents are finished scanning in FOSSology to draw statistics, analyze type of change in files, load diff tree view, show risks etc..-
Smart Reuse of Cleared Components - Reusing previously cleared components is a powerful feature, but the current workflow places the burden on the user to manually search and select matches.
- Introduce a Smart Reuse / Suggested Matches mechanism
- System automatically searches for previously cleared components that closely match the current upload
- Suggested reuse options are presented proactively to the user
-
Enhanced Reuse agent - Introduce an Enhanced Reuse Agent that runs automatically when the user selects the reuse option, providing clear, actionable insight into differences between previously cleared components and their newer versions.
- The agent automatically compares the previously cleared version (v1) with the new version (v2) - New Diff tree view.
- Show number of licenses detected (Histogram) in v1 vs v2
- Highlight whether new licenses were introduced or existing ones changed (in different colors)
- Draw statistics (% of new licenses added compared to scanner findings in old upload)
- Number of lines changed Whether changes affect comments or license-relevant sections (per-file in New Diff tree view) / file itself is new.
- Provide a focused view of Especially changes within comments or source code.
- User shall have a option to decide all the files based upon source code change/ decide all new files with adding license text.
-
UI & REST-Level Transparency - What changed
- Where it changed
- Statistics and all the implemented features from Enhanced Reuse Agent
|

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

## Idea!## Title: Decoupling Copyright, Email, URL/Author from current Scanner## Goal: Separate out copyright,email,url, author information from copyright scanner to individual scanners.Currently, copyright, email, URL, and author extraction are triggered together, despite serving different purposes and having different levels of importance. - Observed Reality:
- Clearing experts heavily rely on copyright information
- Email, URL, and author data are used less frequently and mainly for specific investigations
- Proposed Change:
- Split the existing combined agent into:
- A dedicated Copyright Agent (enabled by default)
- Separate Metadata Agents (Email / URL / Author), enabled only when needed
|

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

## Idea!## Title: New Hybrid View creation & Re-grouping of FOSSology’s Agent Topology## Goal: To create new hybrid view (Licenses + Copyrights) for both tree view and single file view and also re-group the related agents.Over time, FOSSology has evolved into a powerful platform with multiple specialized agents such as Nomos, Monk, Ojo, License Deciders, and others. While this provides flexibility, it also introduces overhead for users, especially clearing experts and newcomers, who must understand which agent to run for basic license detection. This proposal introduces a user-centric abstraction layer that simplifies license scanning workflows while preserving the power and configurability of existing agents under the hood and also ease the clearing expert's time on navigation & reviewing multiple tabs. -
Unified License Detection Abstraction - Users see a single primary action: License Detection, License Detection with Auto Deciders.
- The system internally orchestrates relevant agents based on best practices
- Users are no longer required to understand or select individual license agents
- License Detection with Auto Deciders. shall have a shatter to understand which Auto Deciders are selected. and these shall be configurable via user's pages.
-
Hybrid view (Licenses + Copyrights) - The single file view shall also contain license and copyright evidence. and user can clean/add/update these.
- Have a folder tree with blue & red buttons to indicate the clearing.
- Integrate drag and drop functionality to copy the clearing decisions from one file to another.
- Have a histogram feature to accommodate license groups in the current upload.
- Have a file view page with highlights of all the findings (licenses + copyrights + keywords + ECC).
- Create a new READMEOSS format with (License associated with copyrights)
- All the features shall be implemented to access via REST API as well.
## Refer the basic design structure of the page.
|

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

## Idea!## Title: FOSSology & LicenseDb UX and UI design## Goal: Redesign the FOSSology & LicenseDb UX and UI to modernize its interface and enhance user-friendliness.## Understand the Primary Users**Identify user personas**: Determine who the key users of FOSSology are, such as developers, compliance officers, or open-source contributors.**Analyze pain points**: Conduct surveys, interviews, or user studies to understand the challenges users face while using the current system.
## Analyze the Current Interface**Evaluate usability issues**: Identify areas where the current interface is difficult to use or navigate.**Highlight outdated design elements**: Assess visual components and workflows that no longer align with modern design standards or user expectations.
## Identify Redesign Requirements**Define goals**: Establish clear objectives for the redesign, such as improving efficiency, accessibility, or ease of use.**Prioritize features**: Focus on addressing critical pain points and implementing high-impact improvements.
## Design Reusable Components**Catalog interface elements**: List existing components and determine which can be updated or replaced.**Ensure consistency**: Create reusable design components to maintain a cohesive user experience and simplify scalability.
## Draft Layouts and Workflows**Streamline user journeys**: Map out key workflows to reduce complexity and improve navigation.**Prototype layouts**: Create wireframes or mockups to visualize potential improvements and gather early feedback.
## Establish a Cohesive Design System**Define visual guidelines**: Standardize elements such as colors, typography, and spacing for a unified aesthetic.**Componentize the UI**: Build a library of modular components for easier development and maintenance.
## Gather Feedback and Refine**Conduct usability testing**: Engage users to validate the new designs and identify areas for improvement.**Iterate based on feedback**: Refine layouts, workflows, and components to ensure the redesign meets user needs effectively.
**Contact: |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

## Idea!## Title: Rewrite FOSSology UI using NextJS## Goal: Rewrite FOSSologyUI using NextJS- Existing
[code](https://github.com/fossology/fossologyUI)is old. in the last years GSoC some part of work has been changed to accommodate the new design. - One shall adopt to the changes made last year and carryforward the rest of the design.
- Implementation of new API'S to existing code if needed.
- Implementation designed templates.
|

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

## Idea!## Title: Improve CycloneDX support and update CycloneDX exports to spec version 1.7## Goal: Update and extend the existing CycloneDX report generation## Reasoning: To make use of the overlap between license compliance and cybersecurity requirements it would help many users to improve CycloneDX report generation- Identifiy and address gaps in the currenty implementation (currently license texts and copyright notices seem to be missing)
- Identify and address requirements from other tools, so exports can easily be reused
- Update to spec version 1.7 (Currently spec version 1.4 is supported)
- Support importing CycloneDX documents
|

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

## Idea!## Title: Autonomous Tool Intelligence Assistant leveraging Agentic AIThe goal of this project is to design and develop an The system is expected to reduce the cognitive and operational burden on maintainers, improve user experience during setup and usage, and create a sustainable mechanism for consolidating and evolving project knowledge over time. ## Problem StatementAs open-source projects grow, knowledge becomes increasingly fragmented and difficult to manage. Critical information is spread across: - Documentation (wikis, Markdown, reStructuredText)
- Issue trackers and pull requests
- Source code and implementation details
This fragmentation leads to several recurring challenges: - New users struggle with onboarding and setup, often encountering known issues
- Contributors find it difficult to understand feature behavior and code structure
- Maintainers repeatedly answer similar questions and triage duplicate issues
- Documentation becomes outdated or inconsistent with the codebase
While recent LLM-based chatbots can retrieve answers from documentation, they are largely ## Proposed SolutionWe propose building an Instead of a single conversational bot, the system should be designed as a The assistant should be able to: - Guide users through onboarding and common workflows
- Identify and recommend solutions for frequently occurring setup and usage problems
- Help developers and contributors navigate project features and their implementation
- Continuously improve and curate project knowledge
## What We Want to Achieve## 1. Improved User Onboarding- Enable new users to understand features and workflows through guided, interactive assistance
- Reduce setup failures by proactively identifying known configuration or environment issues
- Provide context-aware recommendations based on project version and usage scenario
## 2. Faster and More Reliable Problem Resolution- Surface known issues and solutions from historical discussions
- Reduce time spent manually searching through documentation and issue trackers
- Decrease duplicate issue creation by directing users to existing resolutions
## 3. Better Developer and Contributor Experience- Make it easier to explore and understand the project without deep prior knowledge
- Connect high-level features to relevant parts of the codebase and documentation
- Lower the entry barrier for new contributors
## 4. Sustainable Knowledge Consolidation- Identify gaps, inconsistencies, or outdated information in documentation
- Encourage continuous improvement of project knowledge
- Ensure that insights gained from user interactions and issues are not lost
## Scope and ExpectationsThe project is expected to focus on Some aspects, such as deep code reasoning or fully automated documentation updates, may be exploratory. However, the overall design and development should be done with these future extensions in mind. ## Why This Matters NowOpen-source projects are growing in scale and complexity faster than their support and maintenance capacity. At the same time, recent advances in large language models and agentic systems make it feasible to move beyond static documentation and reactive chatbots. This is the right moment to explore an - Users increasingly expect interactive, context-aware help rather than manual documentation search
- Maintainers face burnout due to repetitive support and issue triage tasks
- Knowledge loss occurs when insights from issues and discussions are not systematically consolidated
- Agentic AI enables systems that can reason, adapt, and improve over time rather than merely retrieve answers
By addressing these challenges now, the project can proactively shape how AI is responsibly integrated into open-source maintenance workflows, instead of retrofitting solutions later. ## Benefits for the Community## For Users- Faster onboarding and reduced frustration during setup and early usage
- Easier access to accurate, up-to-date information
- A more approachable and interactive support experience
## For Contributors- Lower barrier to entry when understanding project structure and behavior
- Reduced dependency on maintainers for basic guidance
- Clearer pathways to becoming productive contributors
## For Maintainers- Fewer duplicate issues and repetitive support questions
- Better visibility into common user pain points
- A scalable support model as the community grows
## Long-Term Community Impact- Improved project sustainability and maintainability
- Stronger contributor retention through better onboarding
- A reusable blueprint for applying agentic AI responsibly in open-source ecosystems
## Skills Needed**Programming:**Python**Machine Learning:**Knowledge of LLMs, Agentic Behaviour, RAG**Data Engineering:**Knowledge base creation and retrieval**Documentation Standards:**Familiarity with reStructuredText, Markdown, and related formats
|

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
The core problem was that FOSSology, running in a Docker container, only sees the internal HTTP connection. By respecting the |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

## Idea!## Title: Integrate licenselynx to FOSSology & LicenseDb## Goal: To have a alias names of each license stored in fossology & licenseDb- In Current implementation of FOSSology, agents create licenses even though they are alias of some existing license. Idea is to extend the agents to accommodate alias names and do not create duplicates.
- Integrate licenselynx(
[https://github.com/licenselynx/licenselynx](https://github.com/licenselynx/licenselynx)) project to FOSSology & LicenseDb to get the alias names and store it in the database. - Fix the remining issues in
[feat(spdx-expression): License Expression Support #2771](https://github.com/fossology/fossology/pull/2771)and add identifications to known expressions in nomos agent.
|

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

## Idea!## Title: Archiving in FOSSology## Goal: Add a feature to the Maintenance Agent to archive upload data and regenerate the associated information when needed.- To have a archiving feature where user can select at least one year's data to be archived from UI using maintenance agent.
- Agent creates a schema file of that one years records (Upload, decision and file information) and Its related files from file system.
- Agent Creates a downloadable Zip file with all the data.
- If the user wants to reimport. The zip file shall be used as a source to do the reimport again to FOSSology.
|

Beta
Was this translation helpful?
[Give feedback.](https://github.com)
