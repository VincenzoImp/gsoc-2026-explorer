# KubeVirt — Project Ideas

**Source:** https://github.com/kubevirt/community/wiki/Google-Summer-of-Code-2026
**Scraped:** 2026-02-22T23:28:47.544003

---

# Google Summer of Code 2026

"Google Summer of Code (GSoC) is a global, online program that brings new contributors into open source software organizations." - [Google Summer of Code Contributor Guide](https://google.github.io/gsocguides/student/)

The KubeVirt community is applying to be a Google Summer of Code organization, to provide mentorship opportunity to applicants interested in learning about open source software development in the cloud native ecosystem. 

See the [Google Summer of Code website](https://summerofcode.withgoogle.com/) for more information about the program.

## Key Dates

Feb 19: List of accepted organizations announced <br />
Feb 19 – Mar 15: Potential contributors discuss project application ideas with organizations <br />
Mar 31: Contributor application deadline <br />
Apr 30: Accepted GSoC contributor projects announced <br />
May 1 – May 24: Community Bonding Period <br />
May 25 – Aug 24: The Summer of Code!

See the [Google Summer of Code timeline](https://developers.google.com/open-source/gsoc/timeline) for more detailed timeline information.

## Project Ideas

KubeVirt is proposing the following project ideas as starting points for GSoC contributors to develop their own project applications.

### 1. Title: Early Enablement of CBOR
<!-- **GitHub issue**: https://github.com/kubevirt/community/issues/ -->

**Description** <br />
Kubernetes 1.32 introduced Alpha support of CBOR (Concise Binary Object Representation) for CRDs, promising a more compact format and further aiding scalability of Kubernetes and related projects.

KubeVirt aAs a project based on Kubernetes, KubeVirt can leverage this new format to possibly harvest some performance gains. The goal of this project is to build a proof of concept, integrating CBOR for our client-go, as well as enabling testing for our Scale and Performance Special Interest Group (SIG-scale) testing, paving the way for adoption once the feature graduates in Kubernetes.  
  
A successful candidate will work with the SIG-scaleSpecial Interest Group in order to adapt the new format and implement an evaluation framework to determine possible gains.  

**Goal** <br />
The main goal of this project is to create a VEP (design proposal in kubevirt/enhancements repository), integrate CBOR into Kubevirt and ensure that all functionality is preserved.  
To validate the usefulness of the PoC you will need to provide benchmark data and summarization if the performance gain is significant for the adoption. 

**Impact** <br />
This project enables KubeVirt to evaluate the potential performance benefits of the new CBOR format introduced in Kubernetes 1.32. By implementing a proof of concept and a benchmarking framework, you will provide the necessary data to determine if this change improves our scalability. The process of writing a VEP and integrating these changes offers practical experience with Kubernetes API internals and the governance of a large open source project.


**Project requirements** <br />
Project size: Medium – Large <br />
Difficult: TBA <br />
Required skills: GoLang <br />
Desired skills: Testing, Kubernetes  <br />
Mentors: <Felix Matouschek [fmatouschek@redhat.com](mailto:fmatouschek@redhat.com)>, <Ľuboslav Pivarč [lpivarc@redhat.com](mailto:lpivarc@redhat.com)>, <Victor Toso [victortoso@redhat.com](mailto:victortoso@redhat.com)>

**See the [GitHub issue](/ideas/kubevirt/kubevirt-community-issues) for more information on the project, how to get started, and to ask questions.**


### 2. Adapting [k8s.io/apiserver](http://k8s.io/apiserver) in KubeVirt
<!-- **GitHub issue**: https://github.com/kubevirt/community/issues/ -->

**Description** <br />
In the Kubernetes world it is common practice to use the [k8s.io/apiserver](http://k8s.io/apiserver) library to build secure and maintainable API servers. However, KubeVirt is historically using its own API server implementation which resulted in additional effort maintaining it, especially when addressing security issues or adopting new versions and features.

  
The goal for this project is to create a proof of concept that shows how KubeVirt’s API could be migrated to the [k8s.io/apiserver](http://k8s.io/apiserver) library. 

**Goal** <br />
The main objective is to write a comprehensive VEP (design proposal in kubevirt/enhancements repository), accompanied by a Proof of concept. The design and implementation needs to cover all needs of KubeVirt’s API, such as streaming, webhooks, etc.

**Impact** <br />
This project explores a path to modernize KubeVirt’s API layer by adopting the standard k8s.io/apiserver library. By proving feasibility through a PoC and a design proposal (VEP), you will ensure KubeVirt adheres to upstream security standards and reduce the burden of maintaining a custom API implementation. You will gain deep experience with the core libraries used to build Kubernetes, learning how to handle complex requirements like streaming and webhooks in a cloud native environment.

**Project requirements** <br />
Project size: Large (350 hours) <br />
Difficult: TBA <br />
Required skills: GoLang <br />
Desirable skills: Testing, Kubernetes <br />
Mentors: <Ľuboslav Pivarč [lpivarc@redhat.com](mailto:lpivarc@redhat.com)>, <Felix Matouschek [fmatouschek@redhat.com](mailto:fmatouschek@redhat.com)>

**See the [GitHub issue](/ideas/kubevirt/kubevirt-community-issues) for more information on the project, how to get started, and to ask questions.**

### 3. Component base testing framework
<!-- **GitHub issue**: https://github.com/kubevirt/community/issues/ -->

**Description** <br />
Today, KubeVirt contains a comprehensive unit and e2e/functional testing suites and frameworks. While unit tests provide a good guarantee of functioning small, well scoped logic, the e2e suite ensures users flows are covered and not regressing with new changes. 

The component testing framework should bridge these 2 types of tests and bring the best of both. By testing each component in isolation (only with direct dependencies) we want to bring fast, easy to write and not so resource intensive tests as unit tests but provide higher guarantees similar to e2e tests where larger scope of logic is tested (the component).

**Goal** <br />
The goal for this project is to write a re-usable framework for component testing and implement a small test suite for one component. As part of the outcome the contributor should socialize this new framework with the community and provide necessary guidelines and documentation in order for community members to increase the usage and coverage. 

**Impact** <br />
This framework optimizes the KubeVirt testing pyramid by bridging the gap between unit and E2E suites. It reduces CI resource consumption and flakiness by validating complex logic in isolation, providing a faster feedback loop for developers. For the contributor, this presents an architectural challenge of designing a scalable testing infrastructure and driving community consensus on a new standard, rather than simply writing test cases.

**Project requirements** <br />
Project size: Medium – Large <br />
Difficulty: TBA <br />
Required skills: Golang <br />
Desirable skills: Testing, Kubernetes <br />
Mentor: <Felix Matouschek [fmatouschek@redhat.com](mailto:fmatouschek@redhat.com)>, <Ľuboslav Pivarč [lpivarc@redhat.com](mailto:lpivarc@redhat.com)> 

**See the [GitHub issue](/ideas/kubevirt/kubevirt-community-issues) for more information on the project, how to get started, and to ask questions.**

### 4. Declarative validation
<!-- **GitHub issue**: https://github.com/kubevirt/community/issues/ -->

**Description** <br />
Today, KubeVirt developers need to write all validation logic by hand, making it harder to reuse common rules and hard to review the API, as validation is part of API compatibility. In recent years KubeVirt also integrated multiple architectures to the codebase, effectively multiplying these validations and today it’s integrating a multi-hypervisor support, which will further multiply the versions of validations.  
  
To alleviate the cost of adding new validations, architectures and hypervisors, the goal of this project is to explore the adoption of declarative validations in KubeVirt. The validation needs to support writing distinguish validations per architecture x hypervisors.   

**Goal** <br />
The goal of the project is to build a path forward for adopting the declarative validation and implementing at least one hypervisor, architecture combination in order to showcase feasibility of the solution. As these changes are significantly large for the project a comprehensive VEP (design proposal in kubevirt/enhancements repository) should be included in outcomes.

**Impact** <br />
Adopting declarative validation modernizes KubeVirt's API strategy, replacing manual checks with scalable rules to handle the soon expanding matrix of architectures and hypervisors. This reduces maintenance burden and simplifies API reviews. For the contributor, the project offers practical experience with current Kubernetes API standards and the opportunity to author and drive a major design proposal (VEP) for a complex distributed system.


**Project requirements** <br />
Project size: Medium – Large <br />
Difficulty: TBA <br />
Required skills: Golang <br />
Desirable skills: Testing, Kubernetes <br />
Mentor: <Ľuboslav Pivarč [lpivarc@redhat.com](mailto:lpivarc@redhat.com)>, <Felix Matouschek [fmatouschek@redhat.com](mailto:fmatouschek@redhat.com)>

**See the [GitHub issue](/ideas/kubevirt/kubevirt-community-issues) for more information on the project, how to get started, and to ask questions.**

### 5. Build System Evaluation
<!-- **GitHub issue**: https://github.com/kubevirt/community/issues/ -->

**Description** <br />
Today, KubeVirt relies on [Bazel](https://bazel.build/about/intro) to manage its complex, polyglot build requirements. While Bazel provided essential hermeticity, reproducibility and cross-language support during a period of relative immaturity in Go and Docker tooling, the ecosystem has since shifted. Currently, Bazel serves as a complex layer that few contributors can comfortably navigate, creating friction.


**Goal** <br />
The goal of the project is to resolve the "Bazel vs. Native" debate through a rigorous technical evaluation. The evaluation will consist of determining whether the current "Bazel-heavy" infrastructure still serves the project's goals of contributor accessibility and maintenance efficiency.

The outcomes will include a comprehensive audit of Bazel and its use in KubeVirt, a VEP (design proposal in kubevirt/enhancements repository) that will determine the project's future build direction, and finally, a POC according to the results of the VEP in the form of either an alternative Bazel replacement or a modernization of Bazel in the project.

**Impact** <br />
KubeVirt is at a critical scale where build-system friction directly slows down important patches and feature velocity. By addressing that issue, this project will lower the moat and allow more contributors access to a very important yet often neglected part of KubeVirt. For the contributor, this project offers the opportunity to author and drive a major VEP that spans multiple working groups in KubeVirt and essentially changes a fundamental part of it, as well as practical experience in designing and implementing a modern build system for a relatively complex codebase.


**Project requirements** <br />
Project size: Large (350 hours) <br />
Difficulty: TBA <br />
Required skills: Golang, Bash <br />
Desirable skills: Build systems, Kubernetes <br />
Mentor: <Felix Matouschek [fmatouschek@redhat.com](mailto:fmatouschek@redhat.com)>, <Adi Aloni [aaloni@redhat.com](mailto:aaloni@redhat.com)>

**See the [GitHub issue](/ideas/kubevirt/kubevirt-community-issues) for more information on the project, how to get started, and to ask questions.**

<!--  ### 6. 
**GitHub issue**: https://github.com/kubevirt/community/issues/

**Description** <br />

**Goal** <br />


**Impact** <br />



**Project requirements** <br />
Project size: 350 hours <br />
Difficulty: Medium <br />
Required skills: Golang, Bash <br />
Desirable skills: Build systems, Kubernetes <br />
Mentor: Ľuboslav Pivarč lpivarc@redhat.com, 

**See the [GitHub issue](/ideas/kubevirt/kubevirt-community-issues) for more information on the project, how to get started, and to ask questions.** -->

### Custom project proposals

You can submit your own project idea by emailing the [kubevirt-dev Google Group](https://groups.google.com/forum/#!forum/kubevirt-dev) and CC'ing Andrew Burden <aburden@redhat.com> and Petr Horáček <phoracek@redhat.com>.

If a mentor from the KubeVirt community supports the proposed project idea, we can add it to the KubeVirt project ideas list.

## Our stance on using AI for submissions
Before submitting, please read and understand the [KubeVirt AI Contribution Policy](/ideas/kubevirt/kubevirt-community-blob-main-ai-contribution-policy). 

AI assistance is becoming part of our ecosystem and we understand how it can be used for helping improve written submissions and assist in project work, however we have a strong requirement for the human to always be involved and in control. As the author, you need to completely understand and be able to verify the code you are submitting for review. If your project application is thought to be mostly AI-generated, it will likely not be considered. 

We run interviews with all promising candidates during the application process, and if selected you will have regular meetings with your mentors throughout the program.

## Prerequisites
* You have read and understood [our stance on the use of AI](https://github.com/kubevirt/community/wiki/Google-Summer-of-Code-2026/_edit#our-stance-on-using-ai-for-submissions) in this program. 
* Join our [kubevirt-dev](https://kubernetes.slack.com/messages/kubevirt-dev) slack channel and introduce yourself
* Have submitted 3 or more PRs in our org; at least 2 of which have been approved. These can be bug fixes and/or docs patches.
* You have access to x86/amd64 architecture in order to run test clusters for verification. Note that it is possible to run these tests on Mac devices however we will not be able to assist in setup or troubleshooting.
* (Suggested) Send a draft proposal and seek feedback from one of the attached mentors.
* (Suggested) Join the weekly [KubeVirt Community Call](https://calendar.google.com/calendar/u/0/embed?src=kubevirt@cncf.io) and introduce yourself. 

## How and where to find help
First, try to check [KubeVirt documentation](https://github.com/kubevirt/kubevirt/tree/main/docs), we cover many topics and you might already find some of the answers. If there is something unclear, feel free to open an issue and a PR. This is already a great start to getting in touch with the process. <br />
For questions related to KubeVirt and not strictly to the GSoc program, try to use the [#kubevirt-dev Slack channel](https://kubernetes.slack.com/archives/C0163DT0R8X) in the [Kubernetes workspace](https://slack.kubernetes.io/) and [GitHub issues](https://github.com/kubevirt/kubevirt/issues) as much as possible. Your question can be useful for other people, and the mentors might have a limited amount of time. It is also important to interact with the community as much as possible. <br />
You can also search the Slack channel archive to see if others have previously encountered the same issue.

If something doesn't work, try to document the steps and how to reproduce the issue as clearly as possible. The more information you provide, the easiest is for us to help you. If you open an issue in KubeVirt, this already guides you with a template with the kind of information we generally need.

## Tips on how to begin
1. Install KubeVirt and deploy KubeVirt VMs following the [getting started guide](https://github.com/kubevirt/kubevirt/blob/main/docs/getting-started.md)
2. Look for [good-first issues](https://github.com/kubevirt/kubevirt/issues?q=is%3Aopen+is%3Aissue+label%3Agood-first-issue) and try to solve one to get familiar with the project (if there isn’t a PR linked to it, feel free to pick it)
3. Read through our [General contributing guide](https://kubevirt.io/user-guide/contributing/) and our [Developer contributing guide](https://github.com/kubevirt/kubevirt/blob/main/CONTRIBUTING.md) for understanding of community expectations and further tips on how to get started with the project. 

## How to submit the proposal
The preferred way is to create a google doc and share it with the mentors (slack or email work). If for any reason, google doc doesn't work for you, please share your proposal by email. Early submissions have higher chances as they will be reviewed on multiple iterations and can be further improved.

## What the proposal should contain
The design and your strategy for solving the challenge should be concisely explained in the proposal. Which components you anticipate touching and an example of an API are good starting points. The updates or APIs are merely a draft of what the candidate hopes to expand and change rather than being final. The details and possible issues can be discussed during the project with the mentors that can help to refine the proposal.

The submission should have adequate detail for the review team to consider the approach and be confident that the author has come to understand the community and the project itself, and that the author has an understanding of the work they will undertake. 

It is not necessary to provide an introduction to Kubernetes or KubeVirt; instead, candidates should demonstrate their familiarity with KubeVirt by describing in detail how they intend to approach the task.

Mentors may find it helpful to have a schematic drawing of the flows and examples to better grasp the solution. They will select a couple of good proposals at the end of the selection period and this will be followed by an interview with the candidate.

The proposal can have a free form or you can get inspired by the [KubeVirt design proposals](https://github.com/kubevirt/enhancements/tree/main/veps) and [template](https://github.com/kubevirt/enhancements/blob/main/veps/NNNN-vep-template/vep.md). However, it should contain a draft schedule of the project phases with some planned extra time to overcome eventual difficulties.
