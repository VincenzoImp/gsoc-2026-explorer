# JBoss Community — Project Ideas

**Source:** https://spaces.redhat.com/spaces/GSOC/pages/750884772/Google+Summer+of+Code+2026+Ideas
**Scraped:** 2026-02-22T23:28:47.564977

---

The JBoss Community is planning to participate in Google Summer of Code in 2026.

All contributors & developers are welcome to participate in the [https://summerofcode.withgoogle.com/](https://summerofcode.withgoogle.com/) program with the JBoss Community.

If you are a contributor looking forward to participating in the GSoC 2026 with the JBoss Community:

- Feel free to browse the growing idea list below.
- Please don't hesitate to contact the mentor(s) indicated in the proposal for any related clarification and to discuss proposals.
- You can have a look at
[ideas list of previous years](/ideas/jboss-community/display-gsoc-gsoc-google-summer-of-code)for inspiration. - Please see our
[contributor guide](/ideas/jboss-community/display-gsoc-google-summer-of-code-contributor-guide). - You may find a sample GSoC proposal document
[here](/ideas/jboss-community/display-gsoc-google-summer-of-code-2021-ideas)which was for[this](https://docs.jboss.org/display/GSOC/Google+Summer+of+Code+2020+ideas#GoogleSummerofCode2020ideas-Knative-AlternativeKnativeBrokerImplementationbasedonApacheKafka)idea.

Contributors: Please read the list above and also read our [contributor guide](/ideas/jboss-community/display-gsoc-google-summer-of-code-contributor-guide).

A note to mentors

MENTORS: Red Hat employees can change this page directly to add ideas. Please be extra careful to not get other mentors' edits discarded.

Red Hatters should have linked their [jboss.org](http://jboss.org) account with Red Hat and can be checked on [https://sso.jboss.org/login](https://sso.jboss.org/login)

Non-Red Hatters can add a comment to the page and admins will make sure the idea is added to the page.

__Table of Contents__

__Administrators and Mentors__

We will list the potential mentors in this place. For now, if you have any questions, please contact the GSoC administrators:

George Zaronikas ([gzaronikas](https://developer.jboss.org/people/gzaronikas)) and Sokratis Zappis (szappis AT redhat DOT com)

__Communication channels__

Gitter : [JBossOutreach/GSoC - Gitter](https://gitter.im/JBossOutreach/GSoC)

Please take note - These channels are about generic doubts. For project-specific doubts you will need to contact project mentors and channels specified in the project description.

__Idea template (for mentors)__

### Project title


**Summary of idea:**

-Idea

-Feature A

-Feature B

Knowledge prerequisite: Languages/Technologies goes here

Github repo:

Project size: medium (~175 hours) or large (~350 hours)

Skill level: Beginner/Intermediate/Advanced

Contact(s) / potential mentor(s): Mentor(s) name and contact details

Associated JBoss community project(s):

__Idea Proposals__

**WildFly Elytron - Add support for Kubernetes TLS secrets, for use in the WildFly application server**

**Summary of idea:**

Kubernetes TLS secrets are used to secure traffic between users and services. These secrets are represented by PEM files, which can be mounted into the container. The goal of this project is to add the ability to load these secrets into the WildFly application server and use them to secure applications with TLS. The code submitted for this project should not be AI generated.

Knowledge prerequisite: good experience with Java, Maven, Git

Github repo: [https://github.com/wildfly-security/wildfly-elytron](https://github.com/wildfly-security/wildfly-elytron)

Other useful links:

Project size: medium (~175 hours)

Skill level: Intermediate

Contact(s) / potential mentor(s): Darran Lofthouse <darran.lofthouse@[jboss.com](http://jboss.com)>, Diana Krepinska <dvilkola@[ibm.com](http://ibm.com)>

Associated JBoss community project(s): WildFly, WildFly Elytron

**Debezium source connector for Milvus **

**Debezium source connector for Milvus**

**Summary**: Milvus is a cloud‑native vector database widely used for high‑performance similarity search at scale. As of today, there is no Debezium source connector for Milvus; existing integrations focus on sinks into Milvus (e.g., Debezium Server Milvus sink). This project proposes a Debezium Source Connector for Milvus that reads Milvus’ ordered change stream (insert/delete and related DDL), converts it into Debezium’s standard change event envelope, and publishes it which enables downstream processing, multi‑cluster replication, audit trails, and hybrid pipelines that combine vector and relational data.


**Features**:

- Initial blocked Snapshot

- Schema Handling

- evaluate CDC strategies:

- emit CDC events from Woodpecker WAL

- emit CDC events using Milvus metadata (etcd)

**Knowledge prerequisite**: Java Language, Databases, Vector Database

**Github repo**: [https://github.com/debezium](https://github.com/debezium)[ ](https://github.com/debezium/)

**Project size**: large (~350 hours)

**Skill level**: Intermediate

**Contact(s) / potential mentor(s)**:

- Giovanni Panice <
[gpanice@ibm.com>](mailto:gpanice@ibm.com)([kmos](https://github.com/kmos))

- Vincenzo Santonastaso <
[vincenzo.santonastaso@ibm.com>](mailto:vincenzo.santonastaso@ibm.com)([vsantona](https://github.com/vsantona))

Associated JBoss community project(s): [https://debezium.io/](https://debezium.io/)

**Debezium source connector for SQLite **

**Debezium source connector for SQLite**

**Summary**: SQLite is a lightweight, in-memory relational database widely used in desktop, mobile, and edge/IoT applications. This project proposes a Debezium Source Connector for SQLite that captures table contents and ongoing mutations via a robust snapshot‑then‑incremental strategy, converts them into Debezium’s standard change‑event envelope, and publishes the stream to Kafka or Debezium Server targets. The connector will enable downstream processing, audit trails, observability for local data lifecycles, and edge‑to‑cloud pipelines; it also unlocks hybrid architectures that combine changes from SQLite with events from cloud data stores and services.

*Features*:

- Initial blocked Snapshot

- Schema Handling

- Streaming CDC event from WAL files


**Knowledge prerequisite**: Java Language, Databases, Vector Database

**Github repo**: [https://github.com/debezium/](https://github.com/debezium/)

**Project size**: large (~350 hours)

**Skill level**: Intermediate

**Contact(s) / potential mentor(s)**:

- Giovanni Panice <
[gpanice@ibm.com>](mailto:gpanice@ibm.com)([kmos](https://github.com/kmos))

- Vincenzo Santonastaso <
[vincenzo.santonastaso@ibm.com>](mailto:vincenzo.santonastaso@ibm.com)([vsantona](https://github.com/vsantona))

Associated JBoss community project(s): [https://debezium.io/](https://debezium.io/)

**Debezium CLI **

**Debezium CLI**

**Summary**: A unified Debezium CLI would provide developers and operators with a streamlined way to create, manage, and monitor CDC pipelines across heterogeneous data systems. Today, Debezium offers powerful CDC capabilities, but managing connectors, configurations, state, and observability is available only under the Debezium Platform. This project proposes a dedicated command‑line interface that simplifies pipeline lifecycle operations, exposes monitoring insights, and enables consistent workflows for both local development and production environments. By offering intuitive commands for provisioning connectors, validating configurations, and diagnosing issues, the CLI would significantly improve usability and operational efficiency.


**Features**:

- Build & prepare the environment for CDC

- Execute CDC pipeline

- Monitor CDC pipeline

**Knowledge prerequisite**: Java Language, UI, DX

**Github repo**: [https://github.com/debezium](https://github.com/debezium)[ ](https://github.com/debezium/)

**Project size**: large (~350 hours)

**Skill level**: Intermediate

**Contact(s) / potential mentor(s)**:

- Giovanni Panice <
[gpanice@ibm.com>](mailto:gpanice@ibm.com)([kmos](https://github.com/kmos))

- Mario Fiore Vitale
[<mvitale@ibm.com]> ([mfvitale](https://github.com/mfvitale))

Associated JBoss community project(s): [https://debezium.io/](https://debezium.io/)

**Host-Based Pipeline Deployment for the Debezium Platform **

**Host-Based Pipeline Deployment for the Debezium Platform**

**Summary**: Debezium Management Platform aims to simplify the deployment of Debezium to various environments in a highly opinionated manner. To achieve this goal, the platform uses a data-centric view of Debezium components.

The Debezium Platform already defines an environment-agnostic pipeline model and supports deployment on Kubernetes via the Debezium Operator. This project extends support to running Debezium on bare metal, virtual machines, and cloud services, using Debezium Server distributions (container images and standalone packages).


This enables consistent deployment, lifecycle management, and operational behavior across heterogeneous environments, and unlocks hybrid architectures that span Kubernetes and non-Kubernetes infrastructures.

**Features**:

- Automated provisioning of target environments to prepare them for running Debezium Server

- Secure remote access to target hosts for deployment and management operations

- Deployment of Debezium Server using container-based runtimes

- Centralized management of pipeline and runtime configuration

*(Optional)*Service component exposing APIs for managing the Debezium Server lifecycle (deploy, update, stop, remove)

**Knowledge prerequisite**: Java Language, SSH, Rest API, Docker

**Github repo**: [https://github.com/debezium-platform](https://github.com/debezium-platform)[ ](https://github.com/debezium/)

**Project size**: large (~350 hours)

**Skill level**: Intermediate

**Contact(s) / potential mentor(s)**:

- Mario Fiore Vitale <
[mvitale@ibm.com]> ([mfvitale](https://github.com/mfvitale))

- Giovanni Panice <
[gpanice@ibm.com](mailto:gpanice@ibm.com)>([kmos](https://github.com/kmos))

Associated JBoss community project(s): [https://debezium.io/](https://debezium.io/)

**PyDebeziumAI **

**PyDebeziumAI**

**Summary**: AI applications frequently rely on domain specific knowledge provided via retrieval-augmented generation or a similar technique that provides access to data stored in relational databases or elsewhere.

This project should research and develop Python library that will integrate as a first-class citizen into LangChain and LangGraph libraries to provide a database-backed context that would be updated immediately after the underlying database changes.

The project should implement the necessary API/SPIs and provide a bridge between Debezium sourced and target library expected data.


**Features**:

- Published Python library

- Integration with LangChain and/or LangGraph frameworks

- Seamless data conversion

- Multiple example applications demonstrating the usage

- User and developer documentation

**Knowledge prerequisite**: Python, LLM, Java

**Github repo**:

**Project size**: large (~350 hours)

**Skill level**: Intermediate

**Contact(s) / potential mentor(s)**:

- Jiri Pechanec <
[jpechane@ibm.com](mailto:jpechane@ibm.com)> ([jpechane](https://github.com/jpechane))

Associated JBoss community project(s): [https://debezium.io/](https://debezium.io/)

**JBoss Web Server - Add a Diagnostic + Configuration Validation Toolkit (“jws-diag”) for JBoss Web Server**

**JBoss Web Server - Add a Diagnostic + Configuration Validation Toolkit (“jws-diag”) for JBoss Web Server**

**Summary of idea:** If you want to learn real-world production diagnostics, this is your chance to build a tool that saves SREs and support engineers hours per incident. As a bonus, you’ll get to work on a project that sits at the intersection of Java, Linux, TLS, and container platforms.

JBoss Web Server (JWS) is Red Hat’s downstream distribution of Apache Tomcat, used widely for enterprise Java web workloads. In practice, many outages and support cases are caused not by bugs but by misconfiguration, missing visibility, and environment drift (file permissions, TLS keystores, proxy headers, native/OpenSSL setup, etc.). Operators spend time reconstructing “what is actually running” and “what configuration is effectively in use”.

The purpose of this project is to build jws-diag, a read-only diagnostic CLI that can:

- produce a concise “what’s installed + what’s running” summary

- compute and present effective configuration (not just raw XML)

- run a set of high-value validation checks with actionable findings

- optionally generate a redacted support bundle suitable for sharing**Possible tasks for this project:**

- Create a short design document describing:

- discovery strategy for CATALINA_BASE/HOME, systemd env overrides, container detection

- internal model for connectors/TLS/proxy settings

- output formats (human + JSON) and stability requirements

- redaction strategy for bundle mode

- Implement the core CLI commands (minimum viable set):

- jws-diag summary - versions, JVM, OS/container signals, native/OpenSSL status, detected base/home

- jws-diag config -parse key config (starting with server.xml) and present effective connector/TLS/proxy settings

- jws-diag validate-rules engine producing INFO/WARN/ERROR findings + exit codes (0/1/2)

- Implement test cases:

- fixture-based XML configs (good + broken)

- golden output tests (especially for JSON output)

- targeted tests to ensure “no secret leaks” in output/bundles

- Write documentation:

- quickstart usage and examples

- what data is collected, what is not collected

- mapping common findings -> fixes

- (Stretch goal) Implement jws-diag bundle:

- produce a .tar.gz bundle with configs + version manifest (+ optional logs)

- default redaction, with strict mode available

- Create a blog post giving an overview of the project and how to use it in real support / ops workflows.**Knowledge pre-requisites:**

- Experience with Java

- Git

- Maven

- Basic Linux familiarity (processes, permissions, systemd)

- Bonus: TLS basics and Tomcat/JWS configuration familiarity**GitHub repo:**

(new repo, e.g. web-servers/jws-diag)[https://github.com/web-servers](https://github.com/web-servers)

**Other useful links:**

- JBoss Web Server Operator docs:
[https://docs.redhat.com/en/documentation/red_hat_jboss_web_server/6.1/html-single/red_hat_jboss_web_server_operator/index](https://docs.redhat.com/en/documentation/red_hat_jboss_web_server/6.1/html-single/red_hat_jboss_web_server_operator/index) - Apache Tomcat:
[https://tomcat.apache.org/](https://tomcat.apache.org/)

**Project size**: Medium (~175 hours)

**Skill level**: Intermediate**Contact(s) / potential mentor(s):**

- Dimitris Soumis <dsoumis@redhat.com>

**Associated JBoss community project(s):** JBoss Web Server, JWS Operator

**Project Koku ideas**

[Project Koku](https://github.com/project-koku) is a 100% open source FinOps tool that does cloud and Kubernetes costs. It is the upstream of Red Hat Lightspeed cost management. For the first time, we are participating in Google Summer of Code. Keep reading for our ideas!

Technical note on running Koku:

- You do not need actual AWS credentials to run Koku. For data ingestion, Nise can generate fake AWS, Azure, GCP and OpenShift data for you. For running the server-side, note there's two flavors of Koku: SaaS version (which requires AWS and Trino; you typically don't need this one) and self-hosted version (which can run on vanilla OpenShift/OKD/Kubernetes; typically you want this for GSoC development).
- In the koku repository (
[https://github.com/project-koku/koku](https://github.com/project-koku/koku)) you will notice there's [Trino](https://github.com/project-koku/koku/tree/main/koku/masu/database/trino_sql)+[PostgreSQL](https://github.com/project-koku/koku/tree/main/koku/masu/database/sql)version (which is what we use in the SaaS that we run on AWS, hence the dependency on AWS credentials; but you don't want this) and there's a[pure-PostgreSQL](https://github.com/project-koku/koku/tree/main/koku/masu/database/self_hosted_sql/openshift)version (meant to run fully self-hosted, so no AWS or Trino dependencies):[https://github.com/project-koku/koku/tree/main/koku/masu/database](https://github.com/project-koku/koku/tree/main/koku/masu/database)- The easiest way to install the self-hosted version for testing is to use this Helm chart. It's in a different repository because it's work in progress:
[https://github.com/insights-onprem/cost-onprem-chart](https://github.com/insights-onprem/cost-onprem-chart) - So far, the self-hosted version only calculates OpenShift costs. You will need to create a custom Red Hat OpenShift Container Platform cost model (in the Settings page in Koku) and add a price list with custom costs (eg. CPU = 100 INR/core-hour, RAM = 30 INR/core-hour, node = 10,000 INR/core-month, etc; you don't need to use all the metrics). If you don't create a price list, you will see usage information but no costs. Work is in progress to support AWS, Azure and GCP costs in the self-hosted version. Supporting third-party Kubernetes is 100% doable and is in fact one of the GSoC ideas.

**Per-pod data**

**Per-pod data**

**Summary of idea:**

Currently Koku gathers pod-level metrics and calculates cost per pod but never exposes it. What’s exposed is the per-namespace, per-node, per-cluser and per-tag data.

This is a relatively simple project about calculating, persisting and exposing the per-pod data.

**Knowledge prerequisite: **Python, SQL (PostgreSQL/Trino), TypeScript, React

**GitHub repo:** [https://github.com/project-koku/koku](https://github.com/project-koku/koku), [https://github.com/project-koku/koku-ui](https://github.com/project-koku/koku-ui)

**Project size:** medium (~175 hours)

**Skill level: **beginner

**Contact(s):** Pau Garcia Quiles <[pgarciaq@redhat.com](mailto:pgarciaq@redhat.com)>

**Associated JBoss community projects:** Project Koku [https://github.com/project-koku](https://github.com/project-koku)

**New perspectives**

**New perspectives**

**Summary of idea:**

Koku provides perspectives to see all the Kubernetes clusters, all the Kubernetes clusters on cloud, all the AWS/Azure/GCP data, all the Kubernetes on AWS/Azure/GCP. A few convenient perspectives are currently missing:

- All (see everything, i.e. single pane of glass for all the spend across all clouds and on-prem)
- Kubernetes on premise
- KubeVirt virtual machines
- All virtual machines (cloud and KubeVirt)


This is a relatively easy project that encompasses several small tasks.

**Knowledge prerequisite: **Python, SQL (PostgreSQL/Trino), TypeScript, React

**GitHub repo:** [https://github.com/project-koku/koku](https://github.com/project-koku/koku), [https://github.com/project-koku/koku-ui](https://github.com/project-koku/koku-ui)

**Project size:** medium (~175 hours)

**Skill level:** beginner

**Contact(s):** Pau Garcia Quiles <[pgarciaq@redhat.com](mailto:pgarciaq@redhat.com)>

**Associated JBoss community projects: **Project Koku [https://github.com/project-koku](https://github.com/project-koku)

**Totally effective cost distribution type**

**Totally effective cost distribution type**

**Summary of idea:**

As of today, Koku calculates cost by looking at how many resources each pod consumes on each node, and what was the actual cost (including discounts, savings plans, etc) of that node at each moment in time. Then it checks how the user configured the cost model: distribute based on memory usage vs distribute based on CPU usage, and distribute based on request vs usage vs effective usage (greatest of usage and request).

While this approach works really well, it only allows cost distribution based on one dimension: either CPU or RAM.

This project is about introducing newer ways of distributing cost:

- Mix of CPU and memory, user-defined. I. e. Let the user decide what’s the weight of CPU and RAM (and maybe even GPU), eg. 70% CPU, 30% RAM.
- Distribute cost based on maximum relative usage per pod. I. e. If a pod used 20% of the RAM but 80% of the CPU, calculate cost based on CPU; if a pod used 60% of the RAM but 40% of the CPU, calculate cost based on RAM.
- Other alternatives you might think of?


This project is mainly backend work, with minimal frontend requisites.

**Knowledge prerequisite: **mainly Python and SQL (PostgreSQL/Trino). Minimal TypeScript and React for frontend enhancements.

**GitHub repo:** [https://github.com/project-koku/koku](https://github.com/project-koku/koku), [https://github.com/project-koku/koku-ui](https://github.com/project-koku/koku-ui)

**Project size:** large (~350 hours)

**Skill level:** intermediate

**Contact(s):** Pau Garcia Quiles <[pgarciaq@redhat.com](mailto:pgarciaq@redhat.com)>

**Associated JBoss community projects:** Project Koku [https://github.com/project-koku](https://github.com/project-koku)

**Enhancements to cost of cloud services**

**Enhancements to cost of cloud services**

**Summary of idea:**

Koku does cloud, Kubernetes and Kubernetes on the cloud costs but cloud costs have never been the focus so far. Currently, cloud costs are calculated per account, per region, per service, per tag, per organizational unit, etc but they are not itemized per resource id, ie. Koku will tell you the sum of the cost of all the Azure virtual machines running in region X or the sum of all the Azure SQL database tagged T=foo.

This project is about enhancing the cloud costs experience, adding the itemized costs of as many cloud services as possible, for one or more of the three major clouds (AWS, Azure, GCP): virtual machines (AWS EC2, Amazon Lightsail, Azure Compute, Google Compute Engine), databases (AWS RDS, AWS Aurora, Azure SQL, etc), load balancers, monitoring, etc. Since there is a computation and storage cost to generate and keep data, users (tenants admins) should be able to configure what cloud services will be itemized, and which ones will be presented only as high-level aggregates.

This project is relatively straightforward but requires database skills to make cost calculations computationally sensible and keep storage to reasonable needs.

**Knowledge prerequisite:** Python, SQL (PostgreSQL/Trino), TypeScript, React

**GitHub repo: **[https://github.com/project-koku/koku](https://github.com/project-koku/koku), [https://github.com/project-koku/koku-ui](https://github.com/project-koku/koku-ui)

**Project size: **medium (~175 hours)

**Skill level:** beginner

**Contact(s):** Pau Garcia Quiles <[pgarciaq@redhat.com](mailto:pgarciaq@redhat.com)>

**Associated JBoss community projects:** Project Koku [https://github.com/project-koku](https://github.com/project-koku)

**Support third-party Kubernetes client clusters**

**Support third-party Kubernetes client clusters**

**Summary of idea:**

Koku is the upstream of Red Hat Lightspeed cost management, targeting Red Hat OpenShift users. While there is nothing special in the data that’s gathered, how it is gathered, how it’s processed, etc, Koku relies heavily on OpenShift conventions:

- Data is gathered by a Kubernetes Operator
[https://operatorframework.io/](https://operatorframework.io/) - It relies on a Prometheus instance being present and configured in the OpenShift way, with the right data being written to it
- It relies on Kessel, Red Hat’s implementation of SpiceDB to run the server side of Koku


This complex project is about making Koku support one or more third-party Kubernetes clients: EKS, AKS, GKS, etc.

**Knowledge prerequisite: **Python, SQL (PostgreSQL/Trino), TypeScript, React

**GitHub repo: **[https://github.com/project-koku/koku](https://github.com/project-koku/koku), [https://github.com/project-koku/koku-ui](https://github.com/project-koku/koku-ui)

**Project size: **medium (~175 hours)

**Skill level: **intermediate/advanced

**Contact(s):** Pau Garcia Quiles <[pgarciaq@redhat.com](mailto:pgarciaq@redhat.com)>

**Associated JBoss community projects:** Project Koku [https://github.com/project-koku](https://github.com/project-koku)

**Forecasting enhancements**

**Forecasting enhancements**

**Summary of idea:**

Koku does basic forecasting based on the current and past month of data, and it only forecasts until the end of the current month. Also, it doesn’t do a great job when there’s cost anomalies.

This project is about coming up with better forecasting:

- Take anomalies into account
- Expand forecasting beyond the current month, ideally up to 12 months from the current moment
- Forecast non-running workloads based on infrastructure requirements


This project could be accomplished by implementing some forecasting algorithm(s) from scratch, or by using one of the many open source libraries that exist and could serve this purpose:

[Merlion](https://github.com/salesforce/Merlion), by Salesforce[Augurs](https://github.com/grafana/augurs), by Grafana[Orbit](https://github.com/uber/orbit)by Uber[Moirai (AKA uni2ts)](https://www.salesforce.com/blog/moirai/)by Salesforce (collection of models, might eventually include TimeFM)[TimeFM](https://github.com/google-research/timesfm)by Google (single model)- More?

This project is not just coding but also thinking about the best forecasting strategies that would fit the different cases, how to treat anomalies, etc.

**Knowledge prerequisite: **Python, SQL (PostgreSQL/Trino), TypeScript, React

**GitHub repo:** [https://github.com/project-koku/koku](https://github.com/project-koku/koku), [https://github.com/project-koku/koku-ui](https://github.com/project-koku/koku-ui)

**Project size:** large (~350 hours)

**Skill level:** intermediate/advanced

**Contact(s):** Pau Garcia Quiles <[pgarciaq@redhat.com](mailto:pgarciaq@redhat.com)>

**Associated JBoss community projects:** Project Koku [https://github.com/project-koku](https://github.com/project-koku)

**Cloud governance additions**

**Cloud governance additions**

**Summary of idea:**

Koku calculates costs for cloud, Kubernetes on cloud and Kubernetes on premise, and it even takes cloud savings plans, discounts, etc into account but it provides no governance features.

This is a relatively straightforward project about adding cloud governance features:

- What savings plans, reserved instances, commitments, etc I have (per account, per region, per cloud, etc)
- When do they end (and get warnings a few months in advance)
- How much money I might save by moving from pay-as-you-go to reserved/savings plan/private offer
- etc

**Knowledge prerequisite: **Python, SQL (PostgreSQL/Trino), TypeScript, React

**GitHub repo:** [https://github.com/project-koku/koku](https://github.com/project-koku/koku), [https://github.com/project-koku/koku-ui](https://github.com/project-koku/koku-ui)

**Project size:** medium (~175 hours)

**Skill level: **beginner

**Contact(s): **Pau Garcia Quiles <[pgarciaq@redhat.com](mailto:pgarciaq@redhat.com)>

**Associated JBoss community projects: **Project Koku [https://github.com/project-koku](https://github.com/project-koku)

**Other projects**

**Other projects**

**Summary of idea:**

Do you have a different idea for Koku? Would you like to add cost of VMware, Nutanix, Oracle Cloud, Alibaba Cloud or alike? Implement a custom report builder? Propose your own idea!

**Knowledge prerequisite: **Python, SQL (PostgreSQL/Trino), TypeScript, React

**GitHub repo: **[https://github.com/project-koku/koku](https://github.com/project-koku/koku), [https://github.com/project-koku/koku-ui](https://github.com/project-koku/koku-ui)

**Project size: **medium (~175 hours) / large (~350 hours)

**Skill level: **beginner/intermediate/advanced

**Contact(s):** Pau Garcia Quiles <[pgarciaq@redhat.com](mailto:pgarciaq@redhat.com)>

**Associated JBoss community projects:** Project Koku [https://github.com/project-koku](https://github.com/project-koku)
