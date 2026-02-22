# openSUSE Project — Project Ideas

**Source:** https://github.com/openSUSE/mentoring/issues
**Scraped:** 2026-02-22T23:28:47.566236

---

## #255: Uyuni - External Authentication with RBAC Mapping

**Labels:** Uyuni, Medium Sized Project

### Goal
Implement a native Java-based LDAP authentication provider inside Uyuni to allow administrators to configure Active Directory/LDAP integration directly via the Web UI, bypassing the underlying OS (SSSD/PAM). This feature must support mapping LDAP Groups to Uyuni Roles automatically.

### Context
Currently, Uyuni relies on the operating system (SSSD) for external authentication. This forces admins to use the CLI to configure auth, and it lacks "Group Awareness", that means users get a generic role upon login and must be manually promoted by an admin. We want to move this configuration into the Web UI.

### Problem Statement
1.  **CLI Dependency:** Configuring auth currently requires root SSH access to edit `/etc/sssd/sssd.conf`.
2.  **Manual work:** Admins must manually assign permissions (e.g., "Organization Admin") to every new user.
3.  **No RBAC Automation:** There is no way to say "Everyone in the 'DevOps' AD group is automatically a 'System Group Admin' in Uyuni."

### Proposed Solution (The Task)
You will build a "Native LDAP" connector in the Java backend using the *[*UnboundID LDAP SDK** ](https://github.com/pingidentity/ldapsdk)(or [Apache Directory API](https://github.com/apache/directory-ldap-api) ). This connector will exist alongside the current PAM and Local Auth methods.

**Key deliverables:**
* **Backend:** A new authentication service that connects to LDAP, binds, searches for the user, and retrieves their group memberships (`memberOf`).
* **Database:** New tables to store the LDAP configuration (Host, Port, Bind DN) and Role Mappings.
* **Frontend:** A new page in `Admin > Setup` to configure the server and define mappings (e.g., `cn=admins,dc=example` -> `Org Admin`).

---

### Technical Implementation Guide (some hints)

**1. The Library Strategy**
* Uyuni does **not** use the Spring Framework. You should use a lightweight, standalone library like the **UnboundID LDAP SDK** to handle the connection, pooling, and searching.
* **Constraint:** Avoid wrapping the OS `sssd` commands. This must be a pure Java application-level integration.

**2. Database Changes (PostgreSQL)**
You will likely need to create migrations for:
* `auth_ldap_config`: Stores connection details (`host`, `port`, `bind_dn`, `base_dn`, `user_attribute`).
* `auth_ldap_maps`: Maps a Group DN string to an internal Uyuni Role ID.

**3. Authentication Logic (Java)**
* Look at existing authentication classes in the codebase (search for `PamAuthenticationService` or similar) to understand the current flow.
* Your new provider should:
    1.  Check if "Native LDAP" is enabled in the DB.
    2.  Connect to the LDAP server using the stored config.
    3.  Bind as the service account → Search for the user → Re-bind as the user (to verify password).
    4.  **Sync Roles:** If successful, fetch the user's groups, calculate the correct Uyuni roles based on the DB mappings, and update the user's roles in the `web_contact` table *before* the session starts.

**4. Tes

*[truncated]*

---

## #254: Uyuni integration with automation platforms

**Labels:** Uyuni, Medium Sized Project

## Project Title: Uyuni integration with automation platforms

## Description:

Uyuni is a powerful tool for configuration management and Software Defined Infrastructure. While it excels at managing thousands of servers, Uyuni currently lacks a native, flexible automation engine.

Instead of building a heavy internal automation suite, this project aims to decouple automation from the core engine. By implementing an MQTT publisher within Uyuni, we can expose real-time system events (like package updates, onboarding, or salt-states) to third-party low-code platforms like Node-RED.

## The Challenge
The goal is not to "embed" Node-RED into Uyuni, but to make Uyuni a "first-class citizen" in the automation ecosystem. This requires two distinct layers:

The Producer: A way for Uyuni to broadcast its internal state changes.

The Consumer: Specialized tools that allow users to act on those broadcasts without writing complex boilerplate code.

## Deliverables

1) Uyuni MQTT Publisher & Infrastructure
MQTT Plugin: Develop a publisher mechanism within Uyuni ecosystem that pushes events to an MQTT broker.

    Containerization: Provide a pre-configured MQTT broker container image (e.g., Mosquitto) tailored for the Uyuni ecosystem to ensure a "plug-and-play" experience.

2) Node-RED Integration (The "Consumer")
Custom Node-RED Node: A dedicated library (npm package) that wraps the Uyuni API. This allows users to drag and drop a "Uyuni Node" to trigger actions (like "Reboot Server" or "Install Patch") directly from a flow.

    Unified Container Image: A specialised Node-RED container image that comes with the Uyuni nodes and MQTT configurations pre-installed.

## Why This Matters
This project transforms Uyuni from a management tool into a hub for infrastructure automation. It allows sysadmins to create complex logic such as "If a high-priority patch is available in Uyuni, send a Slack alert and open a Jira ticket" using a visual interface rather than complex scripts.

## Mentor:
- @aaannnz
-  (looking for second mentor)

## Skills:
- Linux administration: For the basic Uyuni system deployment and debugging
- Java/Python/PostgreSQL: For the Uyuni backend publisher logic
- JavaScript/Node.js: For developing the custom Node-RED nodes
- Docker/Podman: For containerising the broker and the automation environment
- MQTT Protocol: Understanding of pub/sub patterns

## Project Size:
Medium-sized (175-hour)

## Resources:

[Uyuni Project](https://www.uyuni-project.org/)
[Uyuni GitHub repo](https://github.com/uyuni-project/uyuni/)
[Uyuni Docs](https://www.uyuni-project.org/uyuni-docs/en/uyuni/)
[Node-RED](https://nodered.org/)

## Contact:

[Gitter](https://www.uyuni-project.org/pages/contact.html#gitter)

You can use the channels [users](https://gitter.im/uyuni-project/users) and [devel](https://gitter.im/uyuni-project/devel) at Gitter to chat with us.

You can also join the Gitter rooms via Matrix: [#uyuni-project_users:gitter.im](https://matrix.to/#/#uyuni-project_

*[truncated]*

---

## #253: Improve git-workflow build results

**Labels:** Others, Larged Sized Project

**Project Title:** Improve git-workflow build results

**Description:** 
With the migration to the [git-workflow](https://en.opensuse.org/openSUSE:Git_Packaging_Workflow), we don't have the build results in the gitea directly. There's a [custom tool](https://en.opensuse.org/openSUSE:Git_Packaging_Workflow#Visualizing_build_results) that can be used to add a badge to project/package README.md.

The goal of this project is to improve that tool ([obs-status-service](https://src.opensuse.org/git-workflow/autogits/src/branch/main/obs-status-service)) to provide a better visualization and explore other integrations.

Main improvements to achieve:
 * Adapt current svg styling to gitea css, supporting dark/light theme
 * Explore the svg javascript capabilities to make the badge reactive, update the badge using ajax
 * Implement a new bot to show the build results in direct PR, getting the OBS info from staging or forwarded PR (or add this capability to current bots `obs-forward-bot` or `obs-staging-bot`)

**Deliverables:**
 * Multiple pull requests to the `autogits` repository with new tests
 * New bot to show build results badge in PR

**Mentor:** @danigm

**Communication channels**:

 * Matrix direct message: [@danigm:gnome.org](https://matrix.to/#/@danigm:gnome.org)
 * Matrix openSUSE chat channel: mention me (danigm) [openSUSE Chat](https://matrix.to/#/#chat:opensuse.org)
 * Email: daniel.garcia@suse.com

Be patient and wait one or two days before reping, I'll try to answer as soon as possible, but it's not always possible answer in the same day.

**Skills:**  svg, javascript, git, Linux

**Skill Level:** Medium

**Get started:** 
 * Get familiar with the opensuse git-workflow: https://en.opensuse.org/openSUSE:Git_Packaging_Workflow
 * Get familiar with the current `autogits` repository and different tools, look at the `obs-status-service`

---

## #252: Evaluating Cloud-Native Storage: Performance Benchmarking for Uyuni on RKE2

**Labels:** Uyuni, Larged Sized Project

## Description

As the Uyuni project transitions toward a containerized architecture on RKE2, choosing a performant and reliable storage layer is critical. Currently, Uyuni plans to officially support only one **StorageClass** to ensure long-term maintainability. However, different storage providers (Rook/Ceph, Longhorn, OpenEBS, etc.) offer varying trade-offs between I/O speed, resource consumption, and ease of management.

This project aims to develop a specialized benchmarking suite that mimics real-world Uyuni workloads—such as repository metadata generation and high-volume RPM distribution—to determine which storage solution is the most efficient. A significant focus will be placed on **PostgreSQL performance**, as the database is the heart of Uyuni's operations and is highly sensitive to storage latency and IOPS.

## The project will involve

* **Infrastructure Orchestration:** Setting up multi-node RKE2 clusters for repeatable testing.
* **Storage Deployment:** Implementing and configuring various providers, including **Rook/Ceph, OpenEBS (Mayastor & LocalPV), Longhorn, and GlusterFS**.
* **Workload Simulation:** Developing scripts to simulate I/O-intensive Uyuni tasks like `mgr-sync` and repodata generation.
* **Database Deep-Dive:** Conducting specialized stress tests on PostgreSQL to analyze transaction throughput and WAL (Write-Ahead Log) latency.
* **Comparative Reporting:** Generating data-driven insights to recommend the official storage stack for the Uyuni ecosystem.

## Deliverables

* **Uyuni-Bench Tool:** A set of automated scripts (Python/Bash) designed to trigger specific Uyuni-like I/O patterns.
* **Storage Performance Whitepaper:** A comprehensive report featuring graphs and tables comparing IOPS, throughput, and CPU/RAM overhead across all tested providers.
* **Optimized Postgres Configurations:** A set of recommended `values.yaml` or Helm configurations for PostgreSQL tailored to different storage types (e.g., separating WAL and Data).
* **RKE2 Storage Manifests:** Validated YAML/Helm files for deploying the tested storage solutions on RKE2.

## Mentor

Oscar Barrios and Pablo Gómez

## Skills Required

* **Kubernetes (RKE2/K3s):** Familiarity with PVs, PVCs, and Helm.
* **Storage Fundamentals:** Understanding of Distributed File Systems vs. Block Storage.
* **Database Management:** Basic knowledge of PostgreSQL (benchmarking with `pgbench`).
* **Scripting:** Proficiency in **Python** or **Bash** for automation and data parsing.
* **Benchmarking Tools:** Familiarity with `fio`, `kubestr`, or `iperf`.

## Skill Level

Requires a deep understanding of infrastructure and the ability to troubleshoot complex storage networking issues.

## Project Size

Large-Sized Project (350 hours)

## Get Started

**Specific Use Cases for Benchmarking:**

* **Use Case 1: Metadata Processing (Small-file I/O):** Measure the time to process and generate repository metadata (repodata) for a channel with 50,000+ RPMs. This tests metadata operatio

*[truncated]*

---

## #251: AI-Powered Intelligent Monitoring and Root Cause Analysis for Uyuni

**Labels:** Uyuni, Larged Sized Project, AI

## AI-Powered Intelligent Monitoring and Root Cause Analysis for Uyuni

## Description

Managing large-scale infrastructures with Uyuni involves monitoring a diverse range of Linux distributions (Debian, Ubuntu, Rocky, Alma, OpenSUSE, others) using Prometheus. While the current stack provides robust data collection via exporters (Node, Blackbox, Postgres, Apache) and visualization through Grafana, system administrators often struggle to interpret raw metrics during critical failures.

This project aims to integrate an **AI Monitoring Agent** into the Uyuni ecosystem. The agent will process real-time metrics from Prometheus and, when an anomaly is detected, perform a deep-dive analysis. By combining metric data with live system inspection via **SaltStack**, the AI will generate enriched alerts through **AlertManager**. These alerts won't just say "High RAM usage"; they will explain the root cause (e.g., a specific memory leak in a process) and provide actionable mitigation steps.

## The project will involve

* **Prometheus Integration:** Querying real-time data from Prometheus using PromQL.
* **AI Agent Development:** Building a logic engine (likely Python-based) that runs within the Uyuni Podman container environment to analyze metric trends.
* **SaltStack Orchestration:** Implementing automated "inspections" where the AI triggers Salt commands to gather extra context from managed clients (e.g., `ps aux` or logs).
* **Alert Enrichment:** Formatting and routing intelligent alerts to AlertManager with detailed natural language descriptions.
* **Prompt Engineering:** Designing system prompts that allow the AI to accurately diagnose issues based on multi-exporter data (Postgres, Apache, etc.).

## Deliverables

* **AI Monitoring Service:** A containerized Python application integrated into the Uyuni server environment.
* **Salt-API Integration Module:** A bridge that allows the AI agent to execute secure Salt calls for real-time troubleshooting.
* **Enriched Alert Templates:** Custom AlertManager configurations and templates for human-readable AI outputs.
* **Documentation:** Comprehensive guide on configuring the AI agent, supported metrics, and how to extend it for new exporters.
* **Test Suite:** Basic automated tests simulating system failures (like memory leaks or service crashes) to verify AI diagnostic accuracy.

## Mentor

Oscar Barrios (I might have a co-mentor)

## Skills Required

* **Python:** For building the AI agent and data processing.
* **Prometheus/PromQL:** To understand and query infrastructure metrics.
* **SaltStack:** For remote execution and gathering system state from Uyuni clients.
* **LLM Integration:** Experience with APIs (OpenAI) or local models (Ollama/LlamaCpp) for natural language generation.
* **Linux Systems:** Familiarity with different distributions (SUSE, Debian, RHEL-based).

## Skill Level

* **Large:** Requires a solid understanding of Linux internals and the ability to integrate multiple distinct technologies

*[truncated]*

---

## #245: `kubectl`-like `get` command for `mgrctl`

**Labels:** Uyuni, Medium Sized Project

**Project Title:**

`kubectl`-like `get` command for `mgrctl`

**Description:**

[Uyuni](https://github.com/uyuni-project/uyuni) is an open source systems management solution that can be used to manage various Linux distributions using a powerful web UI and API.

`mgrctl` is a tool meant  to offer API access to the Uyuni server. At the moment it provides a limited set of features and only covers raw API calls.

The goal of this task is to implement a `get` command that works like the one from `kubectl`. So users could query the API using a command like: `mgrctl get <object_type> [options]`.
* The first object types to implement could be `system`, `group` as those are central concepts of Uyuni.
* The options would provide search by name, filtering using some of the object properties and output format options.

For instance `mgrctl get system -f cpu=x86_64 -o yaml` would return a YAML file with the systems that have an x86_64 CPU. 

Note, this idea already exists as an uyuni-tools issue: https://github.com/uyuni-project/uyuni-tools/issues/238

**Deliverable:**

* The code as a PR in [uyuni-tools](https://github.com/uyuni-project/uyuni-tools/) repository.
* Documentation for the new command at least in the `mgrctl get --help`.

**Mentor:**

* @cbosdo

**Skills:**

* Good Golang knowledge.

**Skill Level:** Medium

**Project Size:**  Medium Sized Project (125 hours)

Beware this could easily turn into a rabbit hole: properly define the limits of the project with the mentor. Better have only a few objects covered correctly than a lot with many missing pieces.

**Get started:**

* Join [GitHub Discussions](https://github.com/uyuni-project/uyuni/discussions) and chatrooms: [uyuni-project/devel](https://matrix.to/#/#uyuni-project_devel:gitter.im) [uyuni-project/users](https://matrix.to/#/#uyuni-project_users:gitter.im)
* Get familiar with [uyuni](https://github.com/uyuni-project/uyuni)
* Get familiar with the [mgrctl code](https://github.com/uyuni-project/uyuni-tools/tree/main/mgrctl/cmd). Starting with the [`api` command code](https://github.com/uyuni-project/uyuni-tools/blob/main/mgrctl/cmd/api/api.go) could be a good idea.
* Check the Uyuni [API docs](https://www.uyuni-project.org/uyuni-docs-api/uyuni/index.html)
* Set up a development Uyuni server VM, e.g. with [sumaform](https://github.com/uyuni-project/sumaform).  [This page](https://github.com/uyuni-project/uyuni/wiki/Uyuni-development-in-no-time) can help you getting started. The crucial part is the network setup as it would lead to various strange problems later. Make sure to read https://github.com/uyuni-project/uyuni/wiki/Libvirt-DNS-and-DHCP-without-Avahi to help with this.

---

## #232: 101.o.o shows "Please wait for loading the projects ..."

This issue is about a problem in 101.o.o - and while it might also be a nice task for a future GSoC student, it's probably a good idea if one of the repo admins/devs fixes it before the next GSoC season starts ;-)

Instead of listing the available projects under Rancher/ibus/Uyuni etc., 101.o.o only displays "Please wait for loading the projects ..."

The browser's javascript console shows the following error:

```
Uncaught TypeError: tree is null
    convert_tree_to_html https://101.opensuse.org/assets/js/markdown.js:1556
    toHTMLTree           https://101.opensuse.org/assets/js/markdown.js:112
    toHTML               https://101.opensuse.org/assets/js/markdown.js:82
    success              https://101.opensuse.org/assets/js/github.js:42
    each                 jQuery
    success              https://101.opensuse.org/assets/js/github.js:15
    jQuery 8
        fire
        fireWith
        done
        callback
        send
        ajax
        method
        getJSON
    success              https://101.opensuse.org/assets/js/github.js:14
    jQuery 6
        fire
        fireWith
        done
        callback
        send
        ajax
    <anonymous>          https://101.opensuse.org/assets/js/github.js:8
    jQuery 9
        mightThrow
        process
        setTimeout handler*Deferred/then/resolve/<
        fire
        add
        then
        Deferred
        then
        ready
    <anonymous>          https://101.opensuse.org/assets/js/github.js:1
```

---
