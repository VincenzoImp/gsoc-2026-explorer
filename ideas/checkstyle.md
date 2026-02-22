# checkstyle — Project Ideas

**Source:** https://github.com/checkstyle/checkstyle/wiki/Checkstyle-GSoC-2026-Project-Ideas
**Scraped:** 2026-02-22T23:28:47.591367

---

* [Java 25 Language Feature Support](#project-name-java-25-language-features-support)
* [Improve Google Style coverage on false negatives](#project-name-improve-google-style-coverage-on-false-negatives)
* [Enhancement For Website](#project-name-automated-website-generation)
* [Implementation of auto-fix Recipes](#project-name-implementation-of-auto-fix-recipes)


* [AI-Powered XPath Generator for Checkstyle Suppressions](#project-name-ai-powered-xpath-generator-for-checkstyle-suppressions)
* [Markdown Javadoc Support](#project-name-markdown-javadoc-support)
* [Optimization of distance between methods in single Java class](#project-name-optimization-of-distance-between-methods-in-single-java-class)
* [Reconcile formatters of Eclipse , NetBeans and IntelijIdea IDEs by Checkstyle config](#project-name-reconcile-formatters-of-eclipse--netbeans-and-intellij-idea-ides-by-checkstyle-config)
* [Coverage of Documentation Comments Style Guide and performance improvement](#project-name-coverage-of-documentation-comments-style-guide-and-performance-improvement)
* [Open JDK Code convention coverage](#project-name-open-jdk-code-convention-coverage)
* [Spellcheck of Identifiers by English dictionary](#project-name-spellcheck-of-identifiers-by-english-dictionary)
* [Patch Suppression improvement](#project-name-patch-suppression-improvement)
* [Extend Checker Framework Integration](#project-name-extend-checker-framework-integration)
* [Eliminate Maven Plugin Usage](#project-name-eliminate-maven-plugin-usage)


***

### Project Name: Implementation of auto-fix Recipes

**Skills required**: intermediate Java 

**Project type**: new feature implementation.

**Project goal**: implement new modules, test it on real projects

**Project size**: large (350 hours)

**Complexity Rating**: hard

**Mentors**: Ruslan Diachenko, Timur Tibeyev

**Description**:
Checkstyle is known as tool that raises numerous minor issues. There are so many of these and they are so minor that it is hard to find time and engineer to fix them. Most of the issues are so easy to fix but navigation to certain part of the code and making the fix takes time. Engineers could spend this time doing something more valuable. Implementation of an auto-fix functionality could significantly simplify introduction of checkstyle to project as it will do most tedious work automatically.

Last year we made decision to use OpenRewrite to implement auto-fix features. Base foundation is done and now [project](https://github.com/checkstyle/checkstyle-openrewrite-recipes) is ready to scale with implementations for each specific Checkstyle's Check. 

**Deliverables**:
- Implementation of 17 auto fix recipes ( we noticed that it takes about 4 days to make single auto fix module) for Checks that are marked as TBD at [page](https://github.com/checkstyle/checkstyle-openrewrite-recipes?tab=readme-ov-file#openrewrite-recipe-coverage-for-checkstyle-checks).

**QnA**: https://discord.com/channels/845645228467159061/1214569225247793282 ([invite](https://discord.gg/F6MkcwvZT8))


***

### Project Name: Java 25 Language Features Support

**Skills required**: Java, basic understanding of testing principles, basic understanding of static analysis

**Project goal**: Support static analysis of Java 25 language features

**Project size**: large (350 hours)

**Complexity Rating**: hard

**Mentors**: Roman Ivanov, Andrei Paikin

**Description**:

Developers are enthusiastic about leveraging Java's latest language features, which offer more powerful, declarative,
and expressive code; these features
include [Flexible constructor bodies (JEP 513)](https://openjdk.org/jeps/513), [JEP 512: Compact Source Files and Instance Main Methods](https://openjdk.org/jeps/512). However, Checkstyle currently lacks robust support for these
features. This project aims to bridge this gap by updating existing checks and potentially introducing new ones to
ensure thorough coverage of Java 25 syntax and conventions proposed by the JEPs associated with these language
advancements. The objective is to deliver comprehensive support for the new language features through revising check
modules, exhaustive testing, and detailed documentation updates. This effort not only aligns Checkstyle with
cutting-edge best practices in the Java community but also contributes to the project's ongoing evolution.
Users sharing big interest in [module-info.java support](/ideas/checkstyle/checkstyle-checkstyle-issues-8240) that was introduced long time ago in Java but Checkstyle never had chance to add support of it.


**Deliverables**:

- Analysis of new language features and possible Java parser update to support new features 
- Analysis of possible static analysis coverage (new Checks) for new language features
- Updates in existing Checks to ensure no false positives and negatives for new language features
- Update build process to support compilation and all Continuous Integration jobs on jdk25
- Cleanup our parsing [issues](/ideas/checkstyle/checkstyle-checkstyle-issues).

**QnA**: https://discord.com/channels/845645228467159061/1469487812226056354 ([invite](https://discord.gg/ZsJhmBGy8e))


***


### Project Name: Enhancement For Website

**Skills required**: Java, basic understanding of testing principles, technical writing, continuous integration

**Project goal**: organize documentation and automate its maintenance

**Project size**: medium (175 hours)

**Complexity Rating**: intermediate

**Mentors**: Roman Ivanov, Baratali Izmailov, Mauryan Kansara

**Description**:

During GSoC 2025 we automated a lot and now web content is taken from java sources (javadoc of classes, tests). 
This year project is designed to tackle the persistent challenge of
maintaining accurate and current documentation in our dynamic development environment. Acknowledging the limitations of
manual documentation processes, this initiative introduces automation to streamline content creation, with a focus on
ensuring consistent formats and robust verification checks. In the previous year we improved experience of contributors
who write new Checks/Modules. This year's goal is to provide Checkstyle users with reliable,
standardized, and fully updated documentation with Examples on how to use and benefit each settings of Check/Module.
By elevating documentation practices, this project aligns with
industry best practices, fostering clarity for both users and contributors within the Checkstyle project.
We see a rise of Checkstyle usage in the education process, so having all documentation to be up-to-date and all examples 

**Deliverables**:

- Add missed examples for all Check/Modules, [issue](/ideas/checkstyle/checkstyle-checkstyle-issues-17449).
- Make consistent all examples of Check/Modules, [issue](/ideas/checkstyle/checkstyle-checkstyle-issues-18435).
- HTML Enhancements for our website to ease navigation and user experience by [search toolbar](/ideas/checkstyle/checkstyle-checkstyle-discussions-16214)
- Fix users' complaints about our web-site, [issues](/ideas/checkstyle/checkstyle-checkstyle-issues-2).  

**QnA**: https://discord.com/channels/845645228467159061/1214574452021530686 ([invite](https://discord.gg/F6MkcwvZT8))


***

## Project Name: Improve Google Style coverage on false negatives

**Skills required**: Java, basic understanding of testing principles, basic understanding of static analysis

**Project goal**: improve quality of google style guide implementation

**Project size**: large (350 hours)

**Complexity Rating**: hard

**Mentors**: Roman Ivanov, Mauryan Kansara

**Description:**

During GSoC'25, we successfully updated our implementation of google style guide to the latest version of Apr 25, 2025.
[google_checks.xml](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml) is the configuration file where our google java style guide is implemented.
Though we have covered almost all rules of the google style guide, users have reported bunch of issues pointing out flaws in our implementation, these issues are labeled as [google style](/ideas/checkstyle/checkstyle-checkstyle-labels-google-20style) issues, we need to solve them, majority of such issues are "false-negatives" (supposed to be violation, but not happening).
On top of this, Google Style Guide is [updated in September 2025](https://github.com/google/styleguide/commits/gh-pages/javaguide.html), we need to update our [coverage page](https://checkstyle.org/google_style.html#Coverage_table) to match latest requirements.

**Deliverables:**

- Resolve all issues labeled as [google style](/ideas/checkstyle/checkstyle-checkstyle-labels-google-20style)
- Reduce "Blue Tick" rules by analyzing the rule and our coverage for that rule and provide solutions for them.
- Investigate the issues related to Modules/Checks in issue tracker of Checkstyle repository which are used in [google_checks.xml](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml),
if the Module/Check configuration found in the issue is same as present in [google_checks.xml](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml) then that issue is qualified for the project,
it should be reported to us and marked by [google style](/ideas/checkstyle/checkstyle-checkstyle-labels-google-20style) label.

**QnA**: https://discord.com/channels/845645228467159061/1338510140277522442 ([invite](https://discord.gg/EqbuAmZA3q))



***

### Project Name: AI-Powered XPath Generator for Checkstyle Suppressions

**Skills required**:
- Java (advanced)
- Knowledge of XPath
- Experience with machine learning frameworks
- Basic understanding of Abstract Syntax Trees (AST)
- Familiarity with Docker

**Project goal**:
Develop a local LLM-based solution that generates optimal XPath queries to suppress specific Checkstyle violations based on user prompts, violation details, and code context.

**Project size**: large (350 hours)

**Complexity Rating**: hard

**Mentors**: Ruslan Diachenko, Roman Ivanov, Andrei Paikin, Timur Tibeyev

**Description**:
Creating XPath expressions to suppress Checkstyle violations is a complex task requiring deep understanding of both XPath syntax and AST structure. This leads to either overly broad suppressions hiding important issues or overly specific rules needing frequent updates. This project aims to create an AI-powered system to convert Checkstyle violations and user instructions into precise XPath expressions for violation suppression. The core focus is on developing a containerized LLM-based solution that can understand both the violation context and user intent to generate accurate XPath queries.

A preliminary [proof of concept (PoC)](https://github.com/rdiachenko/checkstyle-xpath-llm-poc) demonstrates the basic feasibility of using LLMs for XPath generation. While this PoC serves as an experimental starting point, the GSoC project will require a complete redesign and implementation to create a production-ready solution.

**Deliverables**:
- Containerized LLM-based solution for XPath generation
- Command-line interface for basic interaction
- Basic documentation for setup and usage
- Fix for all issues with "xpath" label in the Checkstyle repository


**QnA**: https://discord.com/channels/845645228467159061/1338507765207007242 ([invite](https://discord.gg/FWBzr9kZZE))



***

### Project Name: Markdown Javadoc Support

**Skills required:** Java, basic understanding of testing principles, basic understanding of static analysis

**Project type:** new feature implementation.

**Project goal:** Integrate support for Markdown Javadoc comments in Checkstyle.

**Project size:** large (350 hours)

**Complexity Rating:** hard

**Mentors**: Roman Ivanov

**Description:**

 With the introduction of [JEP 467](https://openjdk.org/jeps/467), Java supports Markdown-style documentation comments. 
 This feature modernise Java's documentation capabilities but is not currently supported in Checkstyle.
 The current Javadoc parsing in Checkstyle is tightly coupled to the traditional `/** ... */` syntax and HTML-based formatting,
 presenting challenges in extending support for Markdown's structure. 
 This project aims to enhance Checkstyle by introducing new grammar and update exisiting checks to support Markdown Javadoc comments.
 
**Deliverables**

- New implementation of grammar for Markdown Javadoc Comments
- New tokens to identify and validate elements specific to Markdown Javadoc syntax.
- New Checkstyle Checks for new format of javadoc, ideas on what should be validated should be taken from existing Checks.
- Creation of new checks (if necessary): Create new checks to enforce Markdown-specific best practices.

**QnA**: https://discord.com/channels/845645228467159061/1338509670255562772 ([invite](https://discord.gg/8Pwv8RPKqs))



***

### Project Name: Optimization of distance between methods in single Java class

**Skills required**: basic Java , good analytical abilities, good background in mathematics.

**Project type**: new feature implementation.

**Project goal**: to make quality practices automated and publicly available.

**Project size**: large (350 hours)

**Complexity Rating**: hard

**Mentors**: Roman Ivanov, Baratali Izmailov, Ruslan Diachenko

**Description**:

This task is ambitious attempt to improve code read-ability by minimizing user jump/scrolls in source file to look at details of method implementation when user looks at method first usage.

It is required to analyse a lot of code and find a model to minimize distance between methods first usage and method declaration in the same file and respect users preferences to keep grouped overloaded and overridden methods together. Some other preferences may appear during investigation of open-source projects.

First step is already done by our team, we created a web service that already calculate distances between methods and make [DSM](https://en.wikipedia.org/wiki/Design_structure_matrix) matrix to ease analysis - [methods-distance](https://github.com/sevntu-checkstyle/methods-distance). We already practice it in our project.

As a second step it is required to use a matrix of distances between methods and optimize it by some empiric algorithm to allow user define expected model of class by arguments. This will allow to use this algorithm as a Check to enforce code structure automatically during build time.

**Prove of necessity**: we have a number of PRs where contributors put new methods at any possible place in a class but better place is close to first usage. [Example #1](https://github.com/checkstyle/checkstyle/pull/2845#issuecomment-176775813), [Example #2](https://github.com/checkstyle/checkstyle/pull/1518#issuecomment-137070056), [Example #3](https://github.com/checkstyle/checkstyle/pull/1228#issuecomment-113699926), ....

**Deliverables**:
- new Checkstyle's Check with optimization algorithm to share the algorithm with whole java community.
- analytical report that proves reason why default values for Check parameters are selected  
- article with all details of analysis and algorithm details;

**QnA**: https://discord.com/channels/845645228467159061/1214569693336182864 ([invite](https://discord.gg/F6MkcwvZT8))

***


### Project Name: Reconcile formatters of Eclipse , NetBeans and IntelliJ IDEA IDEs by Checkstyle config.

**Skills required**: basic Java.

**Project type**: new feature implementation, analysis of existing IDE features.

**Project goal**: to make well-known quality practices publicly available.

**Project size**: large (350 hours)

**Complexity Rating**: hard

**Mentors**: Roman Ivanov, Andrei Paikin, Mauryan Kansara

**Description**:

Usage of different IDEs in the same team is already a serious problem, as different IDEs format code base on their own rules and configurations. Unwanted formatting changes happen to code which complicate code-review process. Problem become more acute when project use static analysis tool like Checkstyle that has a wide range of code formatting Checks.
 
It is required to make it possible to use the same Checkstyle config to work in IDEs without conflicts with IDEs internal formatters.
This will help team members be independent on IDE choice but at the same time keep the same format and code style throughout the team.

Main focus of this project is the analysis of formatting abilities of IDEs (indentation, imports order, declaration order, separator/operator wrap, .....) . Update existing Checkstyle Rules to be able to work in the similar and non-conflicting way.

**Deliverables**:
- create configuration for IDEs for Checkstyle project to let Checkstyle team use it and auto-format code to conform with checkstyle_check.xml file that is used by Continuous Integration.
- create Checkstyle config that follows default Eclipse formatting + inspection rules
- create Checkstyle config that follows default IntelliJ IDEA formatting + inspection rules
- create Checkstyle config that follows default NetBeans formatting + inspection rules
- Deep refactoring of Indentation Check to fix its numerous problems. 


**Prove of necessity**: [mail-list post #1](https://groups.google.com/forum/#!searchin/sevntu-checkstyle/formatter/sevntu-checkstyle/tl7ZKsk-Lss/UK0IAvb-j7oJ), [mail-list post #2](http://checkstyle.2069334.n4.nabble.com/CheckStyle-to-Eclipse-formatter-td2070054.html), [mail-list post #3](https://groups.google.com/forum/#!searchin/checkstyle/Idea/checkstyle/7zJ4drblSd8/fu1kyJHMGpAJ) , [discussion #1](https://github.com/google/styleguide/issues/27#issuecomment-104002872) 

**QnA**: https://discord.com/channels/845645228467159061/1214571037451100180 ([invite](https://discord.gg/F6MkcwvZT8))

***


### Project Name: Open JDK Code convention coverage

**Skills required**: basic Java.

**Project type**: new feature implementation.

**Project goal**: to make well-known quality practices publicly available.

**Project size**: large (350 hours)

**Complexity Rating**: hard

**Mentors**: Roman Ivanov, Baratali Izmailov, Daniel Mühlbachler, Mauryan Kansara

**Description**:

[OpenJdk Code Convention](https://www.oracle.com/java/technologies/javase/codeconventions-contents.html) was one of the first guidelines on how to write Java code. OpenJdk Code Convention is marked as outdated (because of date of last update made in it) but best practices described there do not have an expiration date. [New OpenJDK Java Style Guidelines](http://cr.openjdk.java.net/~alundblad/styleguide/) is close to the final version and most likely will be successor of OpenJdk Code Convention. But there is a number of projects in Apache that still follow OpenJdk rules, so both configurations are in need by community.

OpenJdk Code Convention is already partly covered by Checkstyle, known as Sun Code Convention. A lot of validation Rules were added and changed in Checkstyle from the time when Sun's configuration was created ([2004 year](https://github.com/checkstyle/checkstyle/commits/18f6ebbcad23e88e3ae30fc79be464b8b7772a0d/sun_checks.xml)). 

During the project it is required to review both documents in detail and prove publicly that Checkstyle covers all guideline rules. Missed functionality needs to be created, blocking bugs need to be fixed. Page [OpenJdk Java Style Checkstyle Coverage](http://checkstyle.sourceforge.net/sun_style.html) needs to be updated. New page "New OpenJDK's Java Style Checkstyle Coverage" need to be created. Both pages need to be formatted in the same way as it is done for [Google's Java Style Checkstyle Coverage](http://checkstyle.sourceforge.net/reports/google-style/guava/).


**Prove of necessity**: [javadoc issues on github](/ideas/checkstyle/checkstyle-checkstyle-issues-3);  [request from users for Openjdk coverage support](/ideas/checkstyle/checkstyle-checkstyle-issues-6490).
Big projects (Apache Spark) use this style guide , search for "Code style guide" in https://spark.apache.org/contributing.html

**Deliverables**:
- embedded config file with all modules that are required for coverage
- html page that explains how each paragraph in style guide is covered by Checkstyle 

**QnA**: https://discord.com/channels/845645228467159061/1214571550783840307 ([invite](https://discord.gg/F6MkcwvZT8))

***

### Project Name: Coverage of Documentation Comments Style Guide and performance improvement

**Skills required**: basic Java.

**Project type**: new feature implementation.

**Project goal**: to make well-known quality practices publicly available.

**Project size**: large (350 hours)

**Complexity Rating**: hard

**Mentors**: Roman Ivanov, Baratali Izmailov, Mauryan Kansara

**Description**:

Project will mainly be focusing on automation of [Documentation Comments (javadoc) guidelines](http://www.oracle.com/technetwork/articles/java/index-137868.html) by Checkstyle Checks. Reliable comments parsing  was a major improvement in Checkstyle during GSoC 2014, archived results need to be reused to reliably implement automation of Javadoc best practices.

Separate configuration file with newly created Checks need to be created. Best practices in documentation make sense not for all projects. Javadoc validation matters only for library projects that need to expose online documentation in web publicly.

Performance improvement of existing javadoc parser are expected, see details at https://github.com/checkstyle/checkstyle/issues/11193 .

**Deliverables**:
The result of this project will be a configuration file with the maximum possible coverage of Comment style guide. Report should look like [Google's Java Style Checkstyle Coverage](http://checkstyle.sourceforge.net/google_style.html).
Performance improvements of javadoc parsing.
If there will be time left we can focus on coverage of guidelines from https://blog.joda.org/2012/11/javadoc-coding-standards.html

**Prove of necessity**: [javadoc issues on github](/ideas/checkstyle/checkstyle-checkstyle-issues-3).

**QnA**: https://discord.com/channels/845645228467159061/1214571282776064130 ([invite](https://discord.gg/F6MkcwvZT8))

***

### Project Name: Spellcheck of Identifiers by English dictionary 

**Skills required**: intermediate Java.

**Project type**: new feature implementation.

**Project goal**: implement spell checking for java code for all identifiers .

**Project size**: large (350 hours)

**Complexity Rating**: hard

**Mentors**: Roman Ivanov, Andrei Paikin

**Description**:

The correct spelling of words in code is very important, since a typo in the name of method that is part of API could result in serious problem.
Mistakes in names also make reading of code frustrating and misleading, especially when a typo in one letter makes developer to read javadoc or even implementation of the method.
Two most popular IDEs (Eclipse and IntelliJ IDEA) already have spell-check ability. It will be beneficial for Checkstyle to have the same functionality that could be used in any Continuous Integration system by Command Line Interface or as part of build tool (maven, ant, gradle, ....) with wide range of options to customize to users needs.
Features of existing spell-checkers need to be analyzed -  
[IntelliJ IDEA Spellchecking](https://www.jetbrains.com/help/idea/using-code-editor.html#spellchecking) , 
[Eclipse Spelling](http://help.eclipse.org/mars/index.jsp?topic=%2Forg.eclipse.platform.doc.user%2Freference%2Fref-36.htm). 
There are numbers of open-source projects that do spell-check. It is ok to reuse them if license is compatible. Examples: https://code.google.com/archive/p/bspell/ , http://www.softcorporation.com/products/spellcheck/, ...
https://github.com/giraciopide/shellcheck-maven-plugin, https://github.com/codespell-project/codespell

**Deliverables**:
- regular Checkstyle module that does validation
- such module should be applied to all sources of our Code
- disablement of shell based implemnetation of spellcheck in our project for java sources.
- documentation on how to use module

**QnA**: https://discord.com/channels/845645228467159061/1214572273038786631 ([invite](https://discord.gg/F6MkcwvZT8))


***

### Project Name: Eliminate Maven Plugin Usage

**Skills required**: Java, Groovy, Maven

**Project goal**: remove all usages of maven-checkstyle-plugin in our tools

**Project size**: medium (175 hours)

**Complexity Rating**: intermediate

**Mentors**: Roman Ivanov, Daniel Mühlbachler,

**Description**:

Checkstyle serves as a widely used library across various tools, with a notable dependency on
the [maven-checkstyle-plugin](https://maven.apache.org/plugins/maven-checkstyle-plugin/) for continuous integration and
regression testing. However, this reliance on an external tool has restricted our ability to introduce breaking changes
to the Checkstyle project, given the potential disruptions it causes in testing. Consequently, we've had to implement
workarounds to maintain the connection and dependence on the maven-checkstyle-plugin. To foster autonomy and minimize
dependencies, Checkstyle is undertaking efforts to break away from this plugin and shift towards relying solely on tools
under our maintenance. The list of connected issues below outlines specific areas that require modification to
facilitate this transition.

**Deliverables**:

 - Remove all usages of maven-checkstyle-plugin in our tools
 - Update documentation to reflect changes
 - Update build, CI, and regression testing to use internal tools exclusively

**Connected Issues**:
 - [Launch/Diff Groovy should remove use of maven-checkstyle-plugin](https://github.com/checkstyle/contribution/issues/273)
 - [Convert sevntu-checkstyle-check to ant run](/ideas/checkstyle/checkstyle-checkstyle-issues-5385)
 - [Convert regressions that use maven-checkstyle-plugin to CLI based](/ideas/checkstyle/checkstyle-checkstyle-issues-11602)

**Example of Plugin Issue**: [Upgrade XML logger to XML 1.1](/ideas/checkstyle/checkstyle-checkstyle-issues-5168)

**QnA**: https://discord.com/channels/845645228467159061/1214574180591214592 ([invite](https://discord.gg/F6MkcwvZT8))


***

### Project Name: Patch Suppression improvement

**Skills required**: basic Java 

**Project type**: extension of existing feature implementation.

**Project goal**: implement new strategies for existing filter/suppression module or improve existing 

**Project size**: large (350 hours)

**Complexity Rating**: hard

**Mentors**: Roman Ivanov, Ruslan Diachenko

**Description**:
Introducing Checkstyle to a project can be a challenging and NOT an easy job, especially when a project has massive amount of code, very active in development, and there are no resources to start a new process of code cleanup. It may require an extensive effort, especially when there is legacy code from previous contributors that becomes a monotonous job, that everyone tries to avoid. It is easy to say how code should look like, but may be hard to actually enforce rules in existing codebase.

For example [Guava is not following google style](https://github.com/google/guava/issues/1891), and it is easy to say how code should look like but hard to assign somebody to fix ALL problems from previous contributors. It is very boring activity that all will try to avoid. [Good practice from openjdk](http://cr.openjdk.java.net/~alundblad/styleguide/index-v6.html#toc-when-to-reformat-code) actually discourage code changes without good reason. 

Better approach is to let existing code be as is and validate only new code. Checkstyle already has a wide array of filter functionality that could suppress certain violations if user classify a violation as “won’t fix”. Just getting started with setting up the initial suppressions still requires a huge effort to review all the violations, or organize a team on special cleanup process.

This project was originally done at [GSOC 2020](/ideas/checkstyle/checkstyle-gsoc-2020-project-ideas), but during usage of this [project](https://github.com/checkstyle/patch-filters) we found problems that 
checkstyle violations are still going beyond changed code that creates avalanche of change so it complicate usage of it in real project. 

We need to invest focus on parsing of patch files to get more precise location of changes and be able skip violation if fix for it goes outside of changed lines. For example: user changing line wrapping of long signature of method and we should not demand decreasing of amount of parameters or fixing names, as this will trigger changes in other part of code.

As proof of success for this project, it is required to get some open source project onboard to use checkstyle and this new feature. It would be good to try collaborate one more time with Guava project or we can ask our friends in Eclipse-CS or Spring or Hbase project.

**Deliverables**:
- new Filter in Chekstyle that is applied to our code base.
- documentation on how to use new filter.
- apply filer to eclpse-cs project to work on each update (address feedback from usage). 

**QnA**: https://discord.com/channels/845645228467159061/1214572538043043890 ([invite](https://discord.gg/F6MkcwvZT8))

***

### Project Name: Extend Checker Framework Integration

**Skills required**: Java, basic understanding of testing principles, basic understanding of Java type system

**Project goal**: Further usage of Checker Framework and increase internal knowledge base

**Project size**: large (350 hours)

**Complexity Rating**: hard

**Mentors**: Roman Ivanov

**Description**:

The goal of this project is to advance the integration of the [Checker Framework](https://checkerframework.org/) into our existing codebase, enhancing
code quality, correctness, and maintainability. In addition to refining the setup already present in our build, the
project will focus on incorporating the Checker Framework's type system into key components of our code and creating
comprehensive documentation and best practices to guide developers in utilizing the framework effectively.
We identified https://github.com/checkstyle/checkstyle/issues/18482 as additional challenge to address only concerns
that practical.

**Deliverables**:

- Integrate Checker type system with codebase
- Refine existing build
- Develop internal documentation about our usage of Checker
- Provides examples, guidelines and best practices for developers to follow

**QnA**: https://discord.com/channels/845645228467159061/1214572824736571472 ([invite](https://discord.gg/F6MkcwvZT8))
