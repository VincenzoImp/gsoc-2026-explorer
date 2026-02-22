# Cuneiform Digital Library Initiative (CDLI) — Project Ideas

**Source:** https://gitlab.com/cdli/framework/-/wikis/Google-Summer-of-Code-GSoC-2026-Cuneiform-Digital-Library-Initiative-(CDLI)-ideas-list
**Scraped:** 2026-02-22T23:28:47.613008

---

On this page you will find project ideas for Google Summer of Code 2026. We currently offer four projects in total: 2 350-hour projects and 2 175-hour projects. You can learn more about these projects by joining the community and discussing them with mentors

## Disclaimer: AI Usage and Community Participation

CDLI expects contributors to be transparent about any use of AI tools during the proposal and contribution period. AI can be used as a learning or productivity aid, but all submitted work must be reviewed, understood, and explainable by the contributor. Selection decisions focus on the contributor’s understanding, engagement, and ability to actively participate in the community.

- Any use of AI tools must be disclosed by the contributor
- Raw or unreviewed AI-generated content is not acceptable
- Contributors must be able to clearly explain any code or text they submit
- Active participation in the CDLI community is required (asking questions, discussions, communication with mentors)
- Proposals are only one part of evaluation; engagement and demonstrated understanding carry significant weight

## Page Contents

[1. Getting Started](https://gitlab.com#getting-started)[2. About the Cuneiform Digital Library Initiative](https://gitlab.com#2-about-the-cuneiform-digital-library-initiative)[3. List of Potential Project Ideas](https://gitlab.com#3-list-of-potential-project-ideas)-
[4. 350 Hour Projects](https://gitlab.com#350-hour-projects) -
[5. 175 Hour Projects](https://gitlab.com#175-hour-projects) [6. Mentors](https://gitlab.com#6-mentors)

## 1. Getting Started

*Please go through Getting Started carefully. If you get blocked, feel free to reach out to Nisheal.*

-
Join our community and GSoC contact page:


[Join the Community and GSoC Contact](https://gitlab.com/cdli/framework/-/wikis/Join-the-Community-and-GSoC-Contact) -
Read our proposal guide:


[Writing a GSoC proposal for CDLI](https://gitlab.com/cdli/framework/-/wikis/Writing-a-GSoC-proposal-for-CDLI)

Once you’ve joined the community, feel free to post your questions in the **#gsoc** channel.

## 2. About the Cuneiform Digital Library Initiative

The Cuneiform Digital Library Initiative (CDLI) enables the collection, preservation, and accessibility of image files, textual annotation, and metadata for ancient Near Eastern artifacts inscribed with cuneiform. With over 334,000 artifacts, CDLI hosts approximately two-thirds of all known cuneiform sources worldwide. Data is publicly available at [https://cdli.earth](https://cdli.earth) and serves scholars, students, museum staff, and learners.

CDLI is central to Assyriological research, functioning as a data hub and repository. The platform receives ~3,000 monthly users across 10,000 sessions and 100,000 pageviews, with 78% returning visitors.

CDLI brings together developers, language scientists, ML engineers, and cuneiform specialists to build tools for linguistic analysis and translation. Current efforts focus on framework modernization and machine translation of ancient languages using NLP and Linked Open Data.

## 3. List of Potential Project Ideas

This year we offer a small set of focused projects. We look forward to shaping them together based on contributor interests and open needs.

### 350 Hour Projects

### 175 Hour Projects

## 4.1 Revamping CDLI Mobile App (React Native) – 350h

**Mentors:** [Daksh Paleria](https://gitlab.com#daksh-paleria) (Ex GSoC | SDE, Blinkit), [Nisheal John](https://gitlab.com#nisheal-john) (Head of Engineering | SellerGeni AI)

Difficulty: Medium - Hard

Project Size: 350 hours

#### Project Overview

The Cuneiform Digital Library Initiative (CDLI) currently maintains separate Android and iOS tablet applications that allow users to explore curated cuneiform tablet collections, view artifact images, read metadata, and access featured highlights. These applications are actively used by researchers, educators, and the public.

Over time, maintaining two independent mobile codebases has become increasingly difficult. Feature development is duplicated, bug fixes must be applied twice, and keeping both platforms in sync requires significant effort.

This project proposes rebuilding the CDLI tablet applications using React Native, enabling a single shared codebase for Android and iOS while preserving existing functionality. At the same time, the application will be tightly integrated with the CDLI framework and admin panel so tablet content can be managed centrally and delivered directly to mobile users.

The result will be a production-ready cross-platform tablet application backed by a unified content management pipeline.

#### Project Goals

Build a single React Native application for Android and iOS that replaces the existing native apps and connects directly to the CDLI framework and admin panel, allowing curators to manage tablet content centrally while users consume it through a modern mobile experience.

#### Deliverables

The student will implement a React Native application that allows users to browse curated tablet collections, swipe between artifacts, view high-resolution tablet images with zoom support, and read associated metadata in an interactive reading panel.

The application will provide:

- Browsing of curated tablet collections
- Swipe-based navigation between artifacts
- High-resolution image viewing with pinch-to-zoom
- Search for tablets by title or keywords
- Highlighted featured content
- Sharing tablet links through messaging, email, and social apps
- Onboarding and About screens
- Help and Feedback submission
- Local image caching for performance
- Responsive layouts for phones and tablets in portrait and landscape
- Proper navigation handling including Android back behavior
- Splash screen and branding
- Graceful handling of poor network connectivity

The same project also includes building and integrating the framework admin panel used to manage tablet content. This allows curators and contributors to create, edit, and delete tablet entries from a web interface.

Admin panel functionality includes:

- Managing tablet entries (create, update, delete)
- Uploading and displaying artifact images
- Editing tablet metadata, descriptions, and publish dates
- Input validation and formatting
- Listing entries with pagination and search
- Ordering content by date for mobile delivery
- Returning structured JSON responses consumed by the mobile app

Updates made through the admin panel will immediately reflect in the React Native application without requiring redeployment.

#### Expected Outcomes

By the end of GSoC:

- CDLI will have a single React Native application replacing both Android and iOS apps
- All existing user-facing functionality will be preserved
- Tablet content will be centrally managed through the admin panel
- Mobile apps will consume live framework data
- Maintenance overhead will be significantly reduced
- Future development will be faster and easier

## 4.2 Search & Discovery Improvements – 350h

**Mentors:** [Vedant Wakalkar](https://gitlab.com#vedant-wakalkar) (Ex GSoC | SDE, Jio)

**Difficulty:** Medium - Hard

**Project Size:** 350 hours

### Project Overview

The Main search CDLI Framework currently uses Elasticsearch for search inside its CakePHP backend. While it works, indexing is heavy, updates are inefficient, and many search pages still depend on database queries. Even small data changes can trigger large reindex jobs, making the system slower and harder to scale.

This project modernizes CDLI search by migrating to OpenSearch and redesigning indexing to be incremental and event driven. Instead of rebuilding full indexes, only the records affected by a change will be updated. At the same time, more application data will be moved into OpenSearch so search and listing views can be served directly from the index rather than the relational database.

It involves redesigning how data flows from the database into the search layer, refactoring backend APIs, and updating frontend search behavior so OpenSearch becomes the primary system for searching, filtering, sorting, and pagination. The database remains the source of truth for writes and detailed records.

### Project Goals

- Migrate from Elasticsearch to OpenSearch while preserving existing search functionality.
- Redesign indexing to be incremental, so only changed records are updated instead of rebuilding large indexes.
- Introduce event-driven synchronization using database create/update/delete events.
- Move key searchable and display-ready data into OpenSearch, including:
- core entity fields (publications, collections, proveniences, periods, inscriptions)
- commonly used filters and sort fields
- permission and visibility fields
- related metadata needed to render search result pages without extra DB queries

- Refactor backend search APIs so OpenSearch becomes the primary source for:
- keyword search
- filtering
- sorting
- pagination

- Update frontend search views to consume the new APIs and fully rely on OpenSearch-powered results.
- Prepare the architecture for future improvements such as relevance tuning, highlighted matches, autocomplete, and search suggestions.

### Deliverables

- OpenSearch integration with carefully designed index mappings for all major searchable entities.
- Migration of existing Elasticsearch logic and query builders to OpenSearch.
- A production-ready indexing pipeline that supports:
- incremental updates
- partial reindexing of related records when shared metadata changes
- safe retries and idempotent operations

- A background indexing process that reacts to database changes and updates only impacted OpenSearch documents.
- Refactored backend search endpoints that fully use OpenSearch for search and listing pages.
- Expanded OpenSearch documents that include denormalized fields required for UI display, filters, and sorting, reducing database dependency.
- Frontend search updates to support faster filtering, pagination, and richer result presentation.
- Developer documentation covering:
- OpenSearch setup
- index design
- indexing workflows
- reindexing strategies
- local development environment


### Expected Outcomes

- Significantly faster search performance, with OpenSearch handling search workloads instead of the database.
- Efficient, reliable indexing where only changed data is updated.
- Reduced database load on search-heavy pages.
- A cleaner and more maintainable search architecture.
- A system ready for future scale, larger datasets, and advanced discovery features.
- Clear documentation so contributors can extend search without deep coupling to database queries.

### Required Skills

- Strong backend development experience (PHP preferred, CakePHP a plus)
- Familiarity with search engines (Elasticsearch or OpenSearch)
- Experience with data modeling and indexing concepts
- Experience with background jobs or event-driven systems is a plus

## 5.1 CDLI MCP Server and Agent – 175h

**Mentors:** [Jayanth Kumar](https://gitlab.com#jayanth-kumar) (IIT Bombay | CTO, Stealth), [Émilie Pagé-Perron](https://gitlab.com#emilie-page-perron) (Assyriologist & Digital Scholar | Engineer, Archaeology Data Service)

Difficulty: Medium–Hard

Project Size: 175 hours

### Project Overview

CDLI already provides a framework API client that gives programmatic access to its data. However, using this data in AI workflows still requires custom integrations and manual effort. This project aims to change that by building a Model Context Protocol (MCP) server on top of the existing client, turning CDLI into a set of discoverable tools that AI agents can use directly.

The MCP server will expose practical CDLI capabilities such as searching by artifact ID, transliteration text, period, or location, along with fetching related metadata like museum collections and bibliographic references. Instead of hardcoding integrations, agents will be able to discover these tools at runtime and call them when needed.

To demonstrate this in practice, a small demo agent using an open-source language model will be created. The agent will use MCP tools to answer CDLI-related questions, fetch transliterations and metadata, and export datasets. This enables scholars, students, and cultural heritage workflows to interact with CDLI using natural language while still receiving precise, structured data.

The outcome is a reusable MCP layer that makes CDLI easily accessible to AI systems and research tools.

### Project Goals

- Build a production-ready MCP server on top of the existing CDLI framework API client.
- Expose CDLI functionality as a registry of tools that agents can discover and use in real time.
- Support structured search and retrieval across common CDLI use cases such as artifact lookup, transliterations, periods, and proveniences.
- Ensure tool responses are consistent and predictable, so language models can safely build on them.
- Add pagination and batch support to handle large result sets efficiently.
- Develop a lightweight agent that uses these tools to perform real research tasks, not just demos.

### MCP Tools

**Search**

Provide full-text and filtered search using existing CDLI endpoints, including artifact IDs, transliteration text, period, and location. Results are returned in structured formats that agents can easily refine.

**Access Metadata**

Allow agents to fetch complete records or selected metadata fields, including linked information such as museum collections and bibliographic references. Support batch requests for multiple artifacts.

**Export**

Enable exporting search results or selected artifacts as JSON or CSV. Users can choose fields and generate citation-ready outputs for further study or sharing.

### Deliverables

- An MCP server built on top of the current CDLI API client.
- MCP tools for search, metadata access (including links and references), and export.
- Environment-based configuration and authentication.
- Pagination, batching, and clear error handling across all tools.
- A small demo agent powered by an open-source model that:
- discovers MCP tools at runtime
- makes structured calls for CDLI queries
- turns tool responses into readable answers and exports


Example workflows demonstrating:

- summarizing groups of artifacts
- retrieving transliterations across tablets
- extracting timelines by region
- generating bibliographic overviews

### Expected Outcomes

- CDLI becomes accessible through MCP for any compatible client, without custom integrations.
- Users and agents can reliably search, retrieve, and export CDLI content in a standard way.
- AI workflows gain grounded access to CDLI data instead of relying on hallucinated knowledge.
- A working agent demonstrates real-world interaction with CDLI through MCP.
- A strong foundation is created for future AI-powered CDLI applications and research tools.

### Skills Required

- TypeScript or Python
- REST API integration
- MCP server and tool design
- JSON schema and input validation
- Working with open-source language models
- Understanding of search concepts like filtering and pagination
- Linux and Docker fundamentals

## 5.2 Scalable Email Infrastructure – 175h

**Mentors:** [Vishv Kakadiya](https://gitlab.com#vishv-kakadiya) (Ex GSoC | SDE-2, Microsoft)

**Difficulty:** Easy-Medium

**Project Size:** 175 hours

### Project Overview

The CDLI framework currently sends emails directly during web requests. This tightly couples application performance with SMTP availability, making email delivery fragile and hard to debug. There is also limited visibility into which emails were sent, failed, or retried, and templates are basic and inconsistent.

This project aims to redesign the email system into a reliable, background-driven pipeline with better templates, delivery tracking, and basic spam protection. The work will build on the existing Postfix relay setup and focus on practical improvements using mostly open-source tools.

By the end of the project, email will become a first-class, observable system rather than a side effect of user actions.

### Project Goals

- Move email sending out of the request lifecycle and into background jobs, ensuring user actions never block on SMTP delays or failures.
- Introduce retry logic and structured failure handling so important emails are not silently dropped.
- Improve email presentation through consistent layouts and responsive HTML templates, while maintaining plain-text fallbacks.
- Provide basic analytics and visibility into email activity, including delivery status, failures, and backlog.
- Add protection against abuse by rate-limiting sensitive email flows and enforcing consistent sender policies.
- Strengthen operational reliability with health checks, clearer configuration errors, and better logging.

### Deliverables

- Background email processing using a queue (Redis or database-backed) and a dedicated worker.
- Refactored application email flows to enqueue jobs instead of sending directly.
- Retry support with backoff and a record of failed emails that can be reviewed or retried manually.
- A shared email design system with reusable layouts for existing messages (welcome, password reset, admin notifications).
- An admin-facing dashboard showing sent, failed, and pending emails, along with basic error details.
- Rate limiting for password reset and similar endpoints to prevent spam or accidental floods.
- Enforced sender rules to improve deliverability (single From domain with Reply-To support).
- Improved Postfix configuration for safer relaying and TLS enforcement to the upstream SMTP provider.
- Health checks for the mail pipeline and documentation covering setup, debugging, and common failure scenarios.

### Expected Outcomes

- Faster and more stable application behavior since email delivery no longer blocks user requests.
- Higher email reliability through retries and clearer failure reporting.
- Better-looking, consistent emails that improve user experience.
- Increased transparency into email operations, making debugging and monitoring straightforward.
- Reduced risk of spam, abuse, and misconfiguration-related outages.
- A cleaner and more maintainable email architecture that can be extended in the future.

### Skills Required / Preferred

**Required**

- PHP and basic CakePHP knowledge
- SQL and database fundamentals
- Docker and Linux basics

**Preferred**

- Experience with queues or background workers
- Familiarity with Postfix or SMTP concepts
- HTML email design
- Logging or metrics systems
- Basic security concepts such as rate limiting and input validation

## 6. Mentors

*Use the community communication channels to reach out to mentors.*

-
#### Émilie Pagé-Perron

Assyriologist & Digital Scholar | Engineer, Archaeology Data Service


[https://epageperron.info/](https://epageperron.info/) -
#### Nisheal John

Ex GSoC | Head of Engineering, SellerGeni AI


[https://github.com/NishealJ](https://github.com/NishealJ) -
#### Jayanth Kumar

IIT Bombay | CTO, Stealth


[https://jaykmr.com/](https://jaykmr.com/) -
#### Vishv Kakadiya

Ex GSoC | SDE-2, Microsoft


[https://www.linkedin.com/in/vishv07/](https://www.linkedin.com/in/vishv07/) -
#### Vedant Wakalkar

Ex GSoC | SDE-2, Jio


[https://www.linkedin.com/in/karna98/](https://www.linkedin.com/in/karna98/) -
#### Daksh Paleria

Ex GSoC | SDE, Blinkit


[https://www.linkedin.com/in/daksh-paleria-606211190/](https://www.linkedin.com/in/daksh-paleria-606211190/) -
**TBD by 18/02/26, Status: Shortlisting** -
**TBD by 18/02/26, Status: Shortlisting**
