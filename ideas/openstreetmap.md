# OpenStreetMap — Project Ideas

**Source:** https://wiki.openstreetmap.org/wiki/Google_Summer_of_Code/2026/Project_ideas
**Scraped:** 2026-02-22T23:28:47.598891

---

# Google Summer of Code/2026/Project ideas

[Jump to navigation](https://wiki.openstreetmap.org#mw-head)

[Jump to search](https://wiki.openstreetmap.org#searchInput)

This page lists a number of ideas for **potential Google Summer of Code 2026 projects**. This page's primary purpose is to help to give potential applicants ideas that they can build on to turn into applications for the program. Members of the OSM developer community are encouraged to identify ideas for projects, and indicate whether they would be willing to act as a mentor for a GSoC contributor attempting the project, using the

[GSoC idea template](/ideas/openstreetmap/wiki-template-gsoc_idea).

## Note on using AI tools

We recognize that generative AI tools like ChatGPT or Copilot can be a tremendous help when writing code and project proposal texts. However, always keep in mind that they are only tools. They cannot do the work for you. In that spirit, you are welcome to use generative AI tools when preparing your application and during GSoC but you must always ensure that you have read, understood and verified the output. Do not copy and paste ChatGPT answers without thoroughly rereading what it has said. We expect that you will be able to answer questions about the content at any time. Furthermore, *when you use generative AI, you must mention the tool(s) you used*.

## Participant project ideas

GSoC contributors can base their application on one of the ideas below, but we also encourage potential GSOC contributors to come up with their own ideas for projects around OpenStreetMap software. Do you have a pet annoyance you want fixed? A feature you think should be implemented? If you believe you are capable of implementing it and it fits within the time constraints and the GSOC eligibility criteria feel free to bring the idea forward.

Please get in touch with the organizers (at gsoc-orga@openstreetmap.org) as soon as possible if you want to work on something not listed here, so that we can make sure you get the best support possible. We would suggest supplying the same information as in the templates below, if you don't have a potential mentor it may be possible for us to find one for you.

## Searching

|
Suggested By
Summary
Last year we've introduced the concept of categories
Mandatory skills
Python, basic SQL
Useful skills
some knowledge of Lua
Length
350 hours
Difficulty
challenging
Possible Mentors
Notes
The goal of this project to prepare the database structure and processing chain to work with the category concepts.
Comments
Please also see the general hints for contributing to Nominatim for GSOC at
|

|
Suggested By
Summary
Importing the full OpenStreetMap planet into a Nominatim database takes 3 days by now. This is getting too long. In this project we want to explore some possible changes to how the
Skills
Python, basic SQL
Length
350 hours
Difficulty
challenging
Possible Mentors
Notes
The two main changes I have in mind here: A) Currently the main placex table has a column with the marker what needs to be updated. This means that the table is written more often than necessary. We should move the TODO list in a separate table. B) Indexing is parallelized in a way that the parallel processors all need to write to the same tables getting in each others way. We should distribute the data, so that write contentions is less likely.
Comments
Please also see the general hints for contributing to Nominatim for GSOC at
|



## Routing

|
Suggested By
SimonPoole (simon at osmfoundation.org)
Summary
closures.osm.ch was started in GSoC 2025, this year we want to integrate it more closely with at least one routing application and tie up some of the remaining loose ends (see the github repo).
Mandatory skills
python, docker, routing algorithms and knowledge of the implementation language of the target routing app.
Useful skills
Practical experience using OSM data and contributing.
Length
350 hours
Difficulty
medium
Possible Mentors
SimonPoole
Notes
Only applications that fulfill our minimum requirements will be accepted.
|

|
Suggested By
Christian Beiwinkel / Valhalla Community
Summary
We are currently introducing a multi-modal costing called "auto_walk" which combines vehicle and pedestrian routing: directions for driving to the nearest parking lot, followed by walking directions to the destination. This project aims to parse, store and use parking lot data in OSM to mark parking opportunities in the graph.
Mandatory skills
C++, basic SQL
Useful skills
Lua
Length
350 hours
Difficulty
challenging
Possible Mentors
Kevin Kreiser, Nils Nolde, Christian Beiwinkel
Notes
I'll write a lengthier issue about this in the upcoming days, in the meantime there is [this discussion](https://wiki.openstreetmap.org/wiki/Google_Summer_of_Code/2026/||Suggested ByNils NoldeSummaryWe introduced a landmark/POI-based guidance concept (e.g. "Turn right after 50 m before the next Wells Fargo branch") in a previous GSoC. However, it's not ready yet to be hosted on the
Mandatory skills
C++, basic sqlite
Useful skills
Lua
Length
175 hours
Difficulty
medium (for someone with decent C++ skills)
Possible Mentors
Kevin Kreiser, Nils Nolde, Christian Beiwinkel
Notes
Profiling the current POI ingestion performance to pinpoint improvable performance sinks and debugging the code will be part of the project.
|

|
Suggested By
Nils Nolde
Summary
We (re-)introduced public transit routing based on GTFS (only for now) in a previous GSoC. However, it's not ready yet to be hosted on the
Skills
C++
Length
350 hours
Difficulty
challenging
Possible Mentors
Kevin Kreiser, Nils Nolde, Christian Beiwinkel
Notes
This project needs a pretty strong and curious C++ developer.
|

|
Suggested By
Kevin Kreiser
Summary
Pedestrian routing is becoming increasingly important in modern applications with the tendency toward walkable cities and the rise of alternative navigation modalities such as wearables. This project aims to improve a user's ability to follow a given pedestrian route by enhancing the metadata attached to it. One of the main challenges that arises in pedestrian navigation is the lack attribution for pedestrian only ways. Sidewalks don't have names, park pathways, similarly, don't have names. While we can still give guidance in these situation it is more ambiguous, eg. "turn left". Landmark routing can certainly mitigate these scenarios but its coverage can also be lacking. This project focuses on improving the situation by enhancing the data in the graph by spatially joining metadata from nearby OSM features to the part of the graph where pedestrian attribution is lacking. This may be done by eg. copying road names to unnamed sidewalks that abut them, or by eg. marking nodes as park entrances where area features intersect.
Mandatory skills
C++
Useful skills
spatial/geometric operations
Length
175 hours
Difficulty
medium
Possible Mentors
Kevin Kreiser, Nils Nolde, Christian Beiwinkel
Notes
This is an open ended project in the sense that we may discover better opportunities for improvement during investigation and pivot to working on those instead of those already mentioned examples above.
|

## Rendering

|
Suggested By
Mike Barry
Summary
Planetiler is a tool that converts OpenStreetMap data to vector tiles that can be used with web-based mapping libraries like MapLibre GL. There are a few full-featured profiles written in Java with industry-wide adoption like
Mandatory skills
Java
Useful skills
Experience with Java and API design. Familiarity with frontend development and intrepreters a plus.
Required experience
Intermediate experience with Java
Length
350 hours
Difficulty
medium
Possible Mentors
Notes
Phases: (1) allow adding layers from a yaml config to any planetiler profile (2) config-driven feature and attribute filtering (3) convert maplibre style(s) to a filter config
(3) builds on (1) and (2) and will unlock new workflows where users can iterate on a style against a "raw" tileset then "publish" optimized tiles from it by generating a new tileset using the style as a filter.
|

|
Suggested By
Frank Elsinga / MapLibre Community
Summary
Current benchmarks for tile servers compare "apples to oranges" (e.g., cached vs. uncached responses) or rely on outdated, static snapshots.
This leads to misinformation where users choose a server based on theoretical maximums rather than their specific constraints (memory vs. CPU vs. latency). This project aims to build the Tileserver Tradeoff Observatory: an automated system that runs nightly "Performance Labs" in CI. Instead of a simple "speed test," this suite will isolate and visualize specific architectural tradeoffs that a user can choose (e.g., PostGIS vs. PMTiles vs MBTiles, gzip vs. brotli overhead). The results will be published to a self-regenerating "Living Whitepaper" website that educates users on how to configure their tileserver for their specific needs.Mandatory skills
- Docker & Scripting to set up the isolated test environments
- Frontend dev to write a nice dashboard providing insights into the tradeoffs
Useful skills
Basic knowledge of statistics
Required experience
Intermediate to advanced. Prior experience with web development, scripting and good benchmarking is required.
Length
350h
Difficulty
Medium(Requires systems thinking to ensure benchmarks are scientifically valid and reproducible in a noisy CI environment)
Possible Mentors
Notes
Existing state of the art to build upon:
|

|
Suggested By
Frank Elsinga / MapLibre Community
Summary
Add first-class DuckDB support to Martin using DuckDB’s spatial extension and native
`ST_AsMVT` / `ST_AsMVTGeom` functions. This enables efficient vector tile serving directly from analytical, file-based datasets such as GeoParquet/Flatgeobuf, without requiring PostGIS. The project focuses on a clean integration with Martin’s core architecture, useful feature parity with the transactional PostGIS backend, and clear guidance on when an analytical DuckDB backend is the right choice.Mandatory skills
Willingness to learn and dive into the rust geospatial ecosystem
Useful skills
- Rust programming skills
- SQL knowledge
- Familiarity with geospatial concepts (CRS, tiling, MVT)
- Ability to read and extend existing backend code
- Writing tests and technical documentation
Required experience
Intermediate to advanced. Prior experience with Rust backends or spatial databases is recommended, but not required.
Length
350h(Full GSoC project (medium to large scope))
Difficulty
Medium(Requires understanding Martin’s internal architecture, spatial SQL, and performance trade-offs between analytical and transactional databases.)
Possible Mentors
Notes
Initial focus is on GeoParquet-backed DuckDB databases. Support for additional DuckDB file formats is intentionally limited to keep maintenance costs low and performance predictable. Maybe other formats make sense too to add via this, like GeoArrow or Flatgeobuf.
Comments
The project emphasizes useful feature parity rather than full PostGIS compatibility. Design quality, documentation, and tests are as important as raw functionality.
|

## Editing

|
Suggested By
Bryce Cogswell (bryceco)
Summary
Go Map!! is an iPhone app used to edit OpenStreetMap in the field. The iD desktop editor has a robust set of validation functions that warn mappers when they create or modify an object in a way that is inconsistent with best practices. This project would migrate the logic used by iD (written in JavaScript) to Go Map!! (written in Swift, and with a very different architecture).
Mandatory skills
Swift, some UIKit.
Useful skills
JavaScript
Length
175 hours
Difficulty
medium
Possible Mentors
bryceco
Notes
This project requires a Mac, with development using Xcode.
Comments
It may be possible to perform parts of the port using AI, but the two projects have such different architectures that it may be of limited use.
|

|
Suggested By
SimonPoole
Summary
Develop a solution to extract text from a captured image or directly from the camera. The captured text should either be able to be used as a tag value, or to generate a set of tags that can be directly applied to an osm object. It is mandatory that this only uses resources available on device.
Mandatory skills
Java or Kotlin
Useful skills
gradle, experience with Android development
Length
350 hours
Difficulty
medium to challenging
Possible Mentors
SimonPoole
Notes
The successful candidate will need to have access to a suitably powerful Android device. Googles MLkit might be a potential starting point for text recognition. Note that the use of models and code that cannot be distributed on open terms is not possible. Vespucci repo:
|

|
Suggested By
Summary
The goal of this project would be to implement a user interface widget which should a) provide a better visual interpretation of already mapped
Mandatory skills
JavaScript
Useful skills
Experience with the D3.js framework, OSM tagging/mapping workflows, and iD development
Required experience
intermediate
Length
175 hours
Difficulty
medium
Possible Mentors
Notes
Potentially, this project could be extended by enhancing the functionality of the widget also to UI fields for tags with temporal
|

|
Suggested By
Summary
Currently, the
Mandatory skills
JavaScript
Useful skills
Front end web development & UI/UX experience, OSM tagging/mapping
Required experience
intermediate
Length
175 hours
Difficulty
medium
Possible Mentors
Notes
This tool could also provide some parts of the code that are currently directly implemented in iD in form of a library that can act as a "reference implementation" for other consumers of the tagging schema.
|

## Other

|
Suggested By
Summary
The goal is to enhance client-side rendering of 3d models and add support for editing features to improve the contributor experience at the 3D Model Repository
- Replace the current implementation of flat map view with an interactive, on globe rendering of 3D models.
- Provide an API endpoint for lower-res "thumbnail models", use it to improve site performance
- Support in-browser model editing (shift origin/rotate/re-scale) during model upload.
Mandatory skills
JavaScript, Python
Useful skills
3D graphics
Length
175 hours
Difficulty
medium
Possible Mentors
Notes
A potential contributor would have familiarity/prior experience with 3D model rendering pipelines.
|
