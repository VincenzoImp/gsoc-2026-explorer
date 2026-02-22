# GSoC idea template

**Parent:** OpenStreetMap — Project Ideas
**Source:** https://wiki.openstreetmap.org/wiki/Template:GSoC_idea
**Scraped:** 2026-02-22T23:28:47.599321

---

# Template:GSoC idea

[Jump to navigation](https://wiki.openstreetmap.org#mw-head)

[Jump to search](https://wiki.openstreetmap.org#searchInput)

This template is used on [project ideas pages](https://wiki.openstreetmap.org/wiki/Category:Google_Summer_of_Code_ideas) for Google Summer of Code.

### Parameters

`title`

– Title of project idea (use this as a reference in communication with mentors and organizers)`suggestor`

– User who suggests the idea (not necessarily the same as the software maintainer or mentor)`summary`

– Give a short description what the idea is about and outline the work involved.`skills`

– Mandatory skills or knowledge the candidate is expected to have to be considered.`useful_skills`

– Additional skills and knowledge that are helpful for a smooth execution of the project.`experience`

– beginner (has done some courses but no experience with real software projects) / intermediate (has done some work on software projects) / advanced (has worked more long-time on projects with other people)`length`

– 90/175/350 hours (Currently, GSoC projects come in three different lengths, so the scope of the project idea should reflect that.)`difficulty`

–`easy`

(implementation is obvious for anybody with the required skills) /`medium`

(some research is expected and smaller road blocks that need to be solved independently) /`hard`

(candidates is expected to develop their own solutions to the given problem, do extensive research and/or acquire new skills)`mentors`

– Add yourself here if you are interested in mentoring the project. In addition drop the organizers a mail at gsoc-orga@openstreetmap.org.`notes`

– Add additional references and links here that might be useful to understand the context of the project.`comments`

– Any further information, requirements etc. that don't fit anywhere else.

### GSoC proposal for OpenStreetMap

This project aims to modernize the 3D Model Repository (3DMR) by adopting glTF as the standard format for 3D models, upgrading the Django and OAuth implementations, and enhancing the website UI and API for improved usability. These updates will ensure better integration with renderers like OSM2World, improve maintainability, and provide a more user-friendly experience for contributors. The project will also streamline the backend architecture to align with modern development standards, making 3DMR more efficient and scalable:

| You type | {{GSoC idea |title=Modernize the 3D Model Repository |suggestor=Tordanik |summary=The 3D Model Repository (3DMR) is a website that enables users to upload openly licensed 3D models and associate them with OSM data. Renderers such as OSM2World can utilize these models to generate 3D representations of real-world locations. This project aims to modernize 3DMR by transitioning to glTF as the standard format for 3D models, upgrading the existing Django and OAuth implementations, and improving the website UI and API for better usability. |skills=Python, Django, JavaScript, 3D graphics, Next.js(Frontend Framework), React.js, DBMS Knowledge, REST APIs |useful_skills=Experience with 3D modeling formats (glTF), API design, front-end development |experience=Intermediate experience with Python and Django |length=350 hours |difficulty=Medium |mentors=[https://wiki.openstreetmap.org/wiki/User:Lonvia Lonvia], [https://wiki.openstreetmap.org/wiki/User:Tordanik Tordanik] |notes=Applicants are required to set up a local copy of the current codebase before applying to ensure familiarity with the project. |comments=This project will significantly enhance the usability and maintainability of 3DMR by updating its core technologies and improving the user experience. }} |
|---|
