# https://eclipse.dev/sw360/docs/

**Parent:** SW360 — Project Ideas
**Source:** https://eclipse.dev/sw360/docs/
**Scraped:** 2026-02-22T23:28:47.622146

---

[User Guides](https://eclipse.dev/sw360/docs/userguide/)

This guide provides an overview of SW360 and how to get started with using it. It covers the basic usage, and tips for configuring SW360 to work with your software development tools.

**SW360** is a software catalogue application that has been developed to facilitate the sharing of information related to software components used by an organization. Its primary objective is to manage software license information with the support of workflows. The application employs license scanners **FOSSology**, which is integrated to analyze the source code for licenses, copyrights, and other relevant information.

SW360 has been designed to seamlessly integrate with existing software artifact and project management infrastructures. It provides separate backend services for distinct tasks and a set of portlets to access these services. To ensure a smooth and hassle-free deployment, a complete deployment unit is available, which includes a Vagrant box or Docker container that contains a complete configuration of all services and portlets.

SW360 comprises the following main use case areas:

- Project: Handling of project information with all contained Open Source SW components and other Third Party SW Components and Snippets.
- Component/Releases: Handling of information and processes related to components, e.g. name, vendor, version, ECCN information, license compliance information
- License: Handling of information regarding licenses, e.g. license texts, copyrights, acknowledgements, obligations etc.
- Vulnerability: Collecting Security Vulnerability Management Information and matching them with components stored in the component service
- License Compliance documentation: all relevant documents (e.g. Readme, source code bundle) can be created, supported by workflows.

The SW360 is a software catalogue application with which you can:

- Manage your components and projects
- Send source packages to the clearing tool Fossology
- Reuse cleared components and releases for your project
- Import cleared components with clearing reports and other documents
- Browse licenses and their obligations

SW360 is

- Based on the Open Source Liferay portal server
- Integrated with Fossology

In order to work with SW360, please note a fundamental setup in the data model when dealing with components:

- A component is a list of releases with metadata.
- A Release is a version of a component with metadata and specific attachments.
- A project refers to a number of releases of components accordingly, not components.
- A vendor is separate from a component and releases. The link to the vendor is set at the release. (think of Sun and Oracle where the owner changed with a new release)

| Name | URL | Remarks |
|---|---|---|
| Main home page |
|

This guide provides an overview of SW360 and how to get started with using it. It covers the basic usage, and tips for configuring SW360 to work with your software development tools.

SW360 Administration Guides

SW360 Deployment Guides

SW360 Development Information
