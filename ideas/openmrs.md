# OpenMRS — Project Ideas

**Source:** https://openmrs.atlassian.net/wiki/spaces/RES/pages/752844801/Summer+of+Code+2026
**Scraped:** 2026-02-22T23:28:47.607342

---

# Summer of Code 2026

## Write Code. Save Lives.

[OpenMRS](http://openmrs.org/) is hoping to be a mentoring organization for [Google Summer of Code™](http://g.co/gsoc) 2026! Since 2007, we've enjoyed participating in this great program and we're extremely excited about the projects and mentorship opportunities available this year. Coding for OpenMRS is a great way to practice your coding skills and, at the same time, help benefit people in developing countries who are on the front lines of public health challenges.

If you are new to **OpenMRS**, we recommend starting with our [Guide to the New & Curious](/ideas/openmrs/wiki-spaces-docs-pages-25477628). It will introduce you to our community, the tools and spaces we use, and help you get to know the different squads and teams working on various community projects. For a more detailed history of who we are and what we do, please see [here](http://guide.openmrs.org/en/Introduction/a-brief-history.html). If you’re new to OpenMRS or wondering how to get started with your GSoC application, this video should help answer a lot of your questions:

**On this page ....**

**Google Summer of Code at OpenMRS **[om.rs/gsoc](http://om.rs/gsoc)

Learn more about Google Summer of Code 2026:[Google Summer of Code website](https://summerofcode.withgoogle.com/)


**Helpful Links**

Community GSOC Slack Channel:

on**#gsoc**[OpenMRS Slack](https://slack.openmrs.org/)GSOC Topics on the

[OpenMRS Forum](https://talk.openmrs.org/c/community/gsoc/9)

## GSoC 2026 Program Administrators

@beryl @Jayasanka Weerasinghe

Please see [GSoC Admin Guidelines](/ideas/openmrs/wiki-spaces-res-pages-26270205) for more information, or [ Org Admin Tips](https://developers.google.com/open-source/gsoc/help/oa-tips) and

[.](https://summerofcode.withgoogle.com/rules)

**Program Rules**## Project Ideas for GSoC 2026

Talk Thread for Idea collection:

[Brainstorming GSoC 2026 Project Ideas](https://talk.openmrs.org/t/brainstorming-gsoc-2026-project-ideas/47974)**Guide: Defining a Project Ideas List**[Defining a Project (Ideas List) | Google Summer of Code Guides](https://google.github.io/gsocguides/mentor/defining-a-project-ideas-list)

The following ideas are not fully finalized, and their requirements may change or they may be removed. Most of these projects didn’t make it into last year’s GSoC list, but that doesn’t mean they should be forgotten. If you’re passionate about any of them, you’re very welcome to start exploring and working on them with the community.

|
|
|
|
|
|
|
|---|---|---|---|---|---|---|
Medium | Growth Charts are a common need in Primary Health Care for children (pediatrics). Growth Charts are available in O2, but never yet added to O3. With more and more implementers using O3 for care that involves infants, babies, and young children, we need Growth Charts in O3!
| React | @Anjula Samarasinghe |
|
| |
Medium | This project aims to enforce stricter TypeScript configurations across OpenMRS repositories, ensuring developers follow best practices for strong typing. The primary goal is to eliminate the use of By implementing stricter TypeScript settings and refining type definitions, this project will enhance code maintainability, reduce runtime errors, and improve the overall developer experience. | React, Typescript | @Christopher Lumu |
|
| |
Integrating Data Filter for Data Segregation / Multi-tenancy | Large | Data Filter is a powerful module that uses Hibernate’s filtering APIs to add additional where clauses to various SELECT statements. The use-case for this is to allow system-wide filters to be applied to the data added. Currently Data Filter includes a default set of filters that restrict the availability of data on patients to a set of locations a user has access to. The point of this project would be to expand on these capabilities to add things like: an administrative UI for associating users and patients with specific locations, additional rules to account for the various modules used in the O3 RefApp, templates for additional rules that may be useful (i.e., tie the ability to see obs with certain codes to certain privileges). | Java, Hibernate | @Joshua Nsereko
| @Wyclif Luyima |
|
Large | In the scope of the project would be (depending on the progress we make using other contribution channels): Adjust codebase across core and O3 modules to use a new storage service described [here](https://talk.openmrs.org/t/new-storage-service/44655).Adjust code in core and O3 modules to use distributed caching Experiment with Hibernate Search using OpenSearch as backend instead of a local Lucene index.
| Java, Hibernate | @Rafal Korytkowski |
|
| |
Improved Appointments Calendar View | Medium | We have an appointments calendar that is meant to give an overview of appointments. Unfortunately, it is currently less useful than it should be. A few things we need to address: the ability to drill-down into, e.g., monthly, weekly, and daily views; the ability to see all appointments, not just the number per service, instead of changing screens when clicking on a day or service, the app should likely display a modal; the calendar view should not be hard-coded around the Gregorian calendar, but support the various calendars from the @internationalized/date package. | React | TBA |
|
|
Medium | We have a service queues app in O3, which is functional, but needs some attention, both to the frontend design and to the backend APIs that are used to populate it. The goal here would be to fix various UI issues and improve the overall performance and reliability of the queue module. The Service Queues view is incredibly useful for managing outpatient clinics, allowing users to track who is waiting for service, how long they’ve been waiting for etc. | React, Java | @Ian Bacher |
|
| |
| Medium | Many OpenMRS implementers have used HTML Forms (HFE) for many years. Some organizations have **dozens or even hundreds**of OpenMRS forms encoded in HTML. This makes it intimidating to consider moving to O3, since O3 uses a custom Form Schema.There was a previous community project with scripts that help convert HTML forms into the O3 Form Schema for the Angular Form Engine. This did not convert 100% of the form into the new schema, but got most of it done (60-80%) so that it is faster for a team to work on the transition. This project needs to be (1) updated to enable implementers to convert HTML forms into the newer *React*Form Engine schema, and (2) documented to explain how to use it.
|
| @nethmi |
|
|
Dynamic EHR: Custom Home screen (and other screens) based on User roles, locations and other values. (
| Medium | We would like to show UI elements on the O3 home page and other pages that are most relevant to the user. Currently, there is ability to do so based on User privilege. However, this is limiting and not general enough. We would like to define what to show based on other values, such as Location, currenting displayed Visit / Encounter, etc… More generally, this can be solved by having a way to write custom logic (in the form of a reduced set of JavaScript expressions) to define whether an Extension should be shown. There is actually something (what?) similar in O2 already. We should be able to inject dynamic variable
| React |
|
|
|
(Definitely a priority - either GSOC 2026 or anyone who’s interested in meantime) | Large | Voiding in OpenMRS is a form of soft-deleting. We basically set a binary column to |
| @dkayiwa |
|
|
Better way to receive feedback from clinicians / users
|
|
|
|
|
|
|
Postgres support? |
|
|
| @Wikum Weerakutti |
|
|
Patient Visit Summary Printing | Medium | Requested by the Uganda team, the DRC team, and Palladium [Requirements](/ideas/openmrs/wiki-spaces-projects-pages-edit-v2-473333762)are documented and readyBuilds on the recently completed printing support Addresses real implementation needs
| Java, Hibernate, Spring
| @Veronica Muthee |
|
|
A Native O3 Frontend for the Audit Trail. | Small |
| React, Typescript | SolDevelo |
|
|


## Program Timeline

Look [here](https://developers.google.com/open-source/gsoc/timeline) for more info on the full GSoC 2026 program timeline.

In Progress

**GSoC 2026 preparations:**Community Brainstorming

## Guidelines

**Student's guidelines****Mentor's guidelines****Mentor Guide**[https://google.github.io/gsocguides/mentor/](https://google.github.io/gsocguides/mentor/)**Roles and Responsibilities**[https://developers.google.com/open-source/gsoc/help/responsibilities](https://developers.google.com/open-source/gsoc/help/responsibilities)**Org Admin Tips**[https://developers.google.com/open-source/gsoc/help/oa-tips](https://developers.google.com/open-source/gsoc/help/oa-tips)**Defining a Project Ideas List**[https://google.github.io/gsocguides/mentor/defining-a-project-ideas-list](https://google.github.io/gsocguides/mentor/defining-a-project-ideas-list)**Program Rules**[https://summerofcode.withgoogle.com/rules](https://summerofcode.withgoogle.com/rules)**GSoC Discord Chat channel**[discord.gg/google-dev-community](http://discord.gg/google-dev-community)


## OpenMRS resources to know

GitHub:

[https://github.com/openmrs](https://github.com/openmrs/openmrs-core)Talk Forum:

[https://talk.openmrs.org](https://talk.openmrs.org)Help Desk:

[https://help.openmrs.org](https://help.openmrs.org)Issue Tracker (JIRA):

[https://issues.openmrs.org](https://issues.openmrs.org/browse/LBAC-25)
