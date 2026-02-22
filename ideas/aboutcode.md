# AboutCode — Project Ideas

**Source:** https://github.com/aboutcode-org/aboutcode/wiki/GSOC-2026-project-ideas
**Scraped:** 2026-02-22T23:28:47.606808

---

-
-
[Notifications](https://github.com/login?return_to=%2Faboutcode-org%2Faboutcode)You must be signed in to change notification settings -
[Fork 237](https://github.com/login?return_to=%2Faboutcode-org%2Faboutcode)

# GSOC 2026 Project Ideas

[1 revision](https://github.com/aboutcode-org/aboutcode/wiki/GSOC-2026-Project-Ideas/_history)

See our page on applying for GSoC 2026: [https://github.com/aboutcode-org/aboutcode/wiki/GSOC-2026](/ideas/aboutcode/gsoc-2026)

[Project Ideas Index](https://github.com#project-ideas-index)[PURLdb project ideas](https://github.com#purldb-project-ideas)[vulnerablecode project ideas](https://github.com#vulnerablecode-project-ideas)[scancode.io projects ideas](https://github.com#scancodeio-project-ideas)[scancode-toolkit project ideas](https://github.com#scancode-toolkit-project-ideas)[About our Project Ideas List](https://github.com#our-project-ideas)

Here is a list of candidate project ideas for your consideration. Your own ideas are welcomed too! Please chat about them to get early feedback!

[scancode-toolkit](https://github.com/aboutcode-org/scancode-toolkit): [project ideas](https://github.com#scancode-toolkit-project-ideas)

Archived Project Ideas: [https://github.com/aboutcode-org/aboutcode/wiki/Archived-GSoC-Project-Ideas](/ideas/aboutcode/archived-gsoc-project-ideas)

We use these now and then:

- SCIO: ScanCode.io
- BOM: Bill of Material, same as SBOM
- SBOM: Software Bill of Material
- DJCD: DejaCode
- SCTK: ScanCode-Toolkit
- VCIO: VulnerableCode
- NLP: Natural Language Processing
- VDR: Vulnerability Disclosure Report
- VEX: Vulnerability Exploitability Exchange

Code Repositories: [https://github.com/aboutcode-org/purldb](https://github.com/aboutcode-org/purldb)

Description:

There are between 100 and 200 million open source projects and repos out there. Not all of them are equal. Some are much more useful than others, and some could be safely ignored. For instance, the linux kernel is more important, used and popular than a 1st year computer student school assignment project. The goal of this project is to determine when a project is popular and what are the most popular projects. If we do not know what code is used, we can spend a lot of resources to index less used code.

There are some simple approaches to this, using available statistics for downloads or Github stars, but that is not satisfying alone.

An idea would be to consider multiple factors to rank popularity and usage.

- For instance: create a (current and updated) graph of dependencies and compute something like a pagerank but for packages
- Then create with a metric on the freshness of the code like when last release and how much downloaded or based on git activity (excluding bots). This would grow for used code and decay for declining packages
- Then combine this with the dependencies "connectedness"

Or, just a use the graph connections and no download stats, just a giant graph on top of purldb

Or something like this:

- Finding strongly connected components
- Relate packages ignoring versions
- Find most connected
- Discount distant connections, boost closest
- Apply decay based on version freshness or git activity

The approach would be to start small with a single ecosystem as PoC and then extend this to all packages types.

Ideally, this should be exposed in PurlDB API and integrated in data collection operations.

Priority: High

Size: Large

Difficulty Level: Advanced

Tags:

- Python
- Django
- PostgreSQL
- Popularity

Mentors:

- @pombredanne
- @JonoYang
- @AyanSinhaMahapatra

There are two main categories of projects for VulnerableCode:

-
A. COLLECTION: this category is to mine and collect or infer more new and improved data. This includes collecting new data sources, inferring and improving existing data or collecting new primary data (such as finding a fix commit of a vulnerability)

-
B. USAGE: this category is about using and consuming the vulnerability database and includes the API proper, the GUI, the integrations, and data sharing, feedback and curation.


Code Repositories:

Description:

The project would be to provide a way to effectively mine unstructured data sources for possible unreported vulnerabilities.

For a start this should be focused on a few prominent repos. This project could also find Fix Commits.

Some sources are:

- mailing lists
- changelogs
- reflogs of commit
- bug and issue trackers

This requires systems to "understand" vulnerability descriptions: as often security advisories do not provide structured information on which package and package versions are vulnerable. The end goal is creating a system which would infer vulnerable package name and version(s) by parsing the vulnerability description using specialized techniques and heuristics.

There is no need to train a model from scratch, we can use AI models pre-trained on
code repositories (maybe [https://github.com/bigcode-project/starcoder](https://github.com/bigcode-project/starcoder)?) and then
fine-tune on some prepared datasets of CVEs in code.

We can either use NLP/machine Learning and automate it all, potentially training data masking algorithms to find these specific data (this also involved creating a dataset) but that's going to be super difficult.

We could also start to craft a curation queue and parse as much as we can to make it easy to curate by humans and progressively also improve some mini NLP models and classification to help further automate the work.

References: [https://github.com/aboutcode-org/vulnerablecode/issues/251](https://github.com/aboutcode-org/vulnerablecode/issues/251)

Priority: Medium

Size: Large

Difficulty Level: Advanced

Tags:

- Python
- Django
- PostgreSQL
- Security
- Vulnerability
- NLP
- AI/ML

Mentors:

- @pombredanne
- @tg1999
- @keshav-space
- @Hritik14
- @AyanSinhaMahapatra

Related Issues:

Code Repositories:

Description:

When large packages/containers are scanned in scancode.io it is useful to have a tree-view to explore thorugh the file-tree for that package/container to look into scan data for a particular subset of the file-tree/directory or to research more into detections and detection issues.

This would be something similar to what we have at scancode-workbench for example:
[https://scancode-workbench.readthedocs.io/en/develop/ui-reference/directory-tree.html](https://scancode-workbench.readthedocs.io/en/develop/ui-reference/directory-tree.html)

I.e. we need the following features:

- To be able to toggle showing the directory contents from the directory icon
- Show nested directory contents in a tree like structure
- Have this view ideally in a pane left to the table-view of resources
- Show only info from the selected directory in the table-view of resources

Note that we do have a ProjectCodebaseView in the projects page currently in scancode.io but this is fairly limited as it only lets you browse through the codebase one directory at a time (only shows the files/directories in one directory), and lets you navigate to directories in the current directory or the parent directory from there.

Priority: High

Size: Large

Difficulty Level: Intermediate

Tags:

- Python
- Django
- UI/UX
- File-system
- Navigation

Mentors:

- @tdruez
- @pombredanne
- @AyanSinhaMahapatra

Related Issues:

Code Repositories:

Description:

Required phrases are present in rules to make sure the rule is not matched to text in a case where the required phrase is not present in the text, which would be a false-positive detection.

We are marking required phrases automatically based on what
is present in other rules and license attributes, but this
still leaves a lot of rules without them.
See [https://github.com/aboutcode-org/scancode-toolkit/pull/3924](https://github.com/aboutcode-org/scancode-toolkit/pull/3924)
where we are also adding a script to add required phrases as
individual rules if applicable and also adding required phrases
added to other rules.

- research and choose a model pre-trained on code (StarCoder?)
- use the dataset of current SCTK rules to train a model
- Mark required phrases in licenses automatically with the model
- Test required phrase additions, improve and iterate
- Bonus: Create a minimal UI to review rule updates massively

Priority: Medium

Size: Medium

Difficulty Level: Advanced

Tags:

- Python
- ML/AI
- Licenses

Mentors:

- @AyanSinhaMahapatra
- @tg1999
- @pombredanne

Related Issues:

Here are some project related attributes you need to keep in mind while looking
into prospective project ideas, see also: [guidance on finding the right project](https://google.github.io/gsocguides/student/finding-the-right-project):

-
The repositories/projects are not sorted in order of importance, instead we have a explicit priority mentioned for each project idea and this can be: Low, Medium or High.

-
This doesn't mean we will always consider a project proposal with a higher priority idea over a relatively lower priority one, no matter the merit of the proposal. This is only one metric of selection, mostly to prioritize important projects.

-
You can also suggest your own project ideas/discuss changes/updates/enhancements based on the provided ideas, but you need to really know what you are doing here and have lots of discussions with the maintainers.


There are three project lengths:

- Small (~90 hours)
- Medium (~175 hours)
- Large (~350 hours)

If you are proposing an idea from this ideas list, it should match what is listed here,
and additionally please have a discussion with the mentors about your proposed length
and timeline. Please also open a discussion about the same, if not already present,
at [https://github.com/aboutcode-org/aboutcode/discussions/categories/gsoc](/ideas/aboutcode/aboutcode-org-aboutcode-discussions-categories-gsoc) or discuss this in
the respective issues.

We have marked our ideas with medium/large based on general estimates, but this could vary. In a few cases they are both used to mark a project as it can be both. We have made conscious effort to make sure projects are not too large, have clear deliverables and can be finished successfully, but still note that these are complex projects and you're likely underestimating the complexity (and how much we'll bug you to make sure everything is up to our standards).

You must discuss your proposal and the size of project you are proposing with a mentor as otherwise we cannot consider your proposal fairly.

We likely would only select medium/large project ideas only as the small projects are too small to get familiar with and contribute meaningfully to any of our projects.

Please also note that there is a difference in the stipend based on what you select, and it would not be fair if you're selecting and working on a large project, but getting paid for a medium one (or vice-versa).

Here are all the tags we use for specific projects, feel free to search this page using these if you only want to look into projects with specific technical background.

[Django], [PostgreSQL], [Web], [DataStructures], [Scanning], [Javascript], [UI], [LiveServer] [API], [Metadata], [PackageManagers], [SBOM], [Security], [BinaryAnalysis], [Scraping], [NLP], [Social], [Communication], [Review], [Decentralized/Distributed], [Curation]

We are generally using three levels of difficulty to characterize the projects:

- Easy
- Intermediate
- Advanced

If it is a difficult project it means there is significant domain knowledge required to be able to tackle this project successfully, and you must have prior verifiable experience on this (in the form of open source contributions, either on the same topic in our repos, or elsewhere). You must also consult with mentors/maintainers early, ask a lot of domain specific questions and must be ready to research and tackle greenfield projects in certain cases if you choose a project in this difficulty category.

Most other intermediate projects do not require this much domain knowledge and can easily be acquired during proposal writing/contributing, if you're familiar with the tech stack used in the project. But these are still not straight-forward and requires lots of feedback from the mentors. Most projects fall in this category.

There are also easy projects which only require honest time and effort from the participant, and decent knowledge about the tech stack/problem.

Please feel free to chime in at [https://github.com/aboutcode-org/aboutcode/discussions/133](/ideas/aboutcode/aboutcode-org-aboutcode-discussions-133)
or in our GSoC 2026 chatroom at [https://matrix.to/#/#aboutcode-org_gsoc2026:gitter.im](https://matrix.to/#/#aboutcode-org_gsoc2026:gitter.im)
if you have any questions related to AboutCode's participation in GSoC
or anything in this page.
