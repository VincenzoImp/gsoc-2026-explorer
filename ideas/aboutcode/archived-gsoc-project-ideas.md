# https://github.com/aboutcode-org/aboutcode/wiki/Archived-GSoC-Project-Ideas

**Parent:** AboutCode — Project Ideas
**Source:** https://github.com/aboutcode-org/aboutcode/wiki/Archived-GSoC-Project-Ideas
**Scraped:** 2026-02-22T23:28:47.607087

---

***
## All Other/Archived Project Ideas

These are lower priority project ideas from all the projects or older
project ideas from previous year GSoC, archived here. 

***

## PURLdb: Add UI and deploy a live public server

Repository: https://github.com/nexB/purldb

Project code: https://github.com/nexB/purldb/tree/main/purldb

Size: Large

Difficulty Level: Intermediate

Tags: [Django], [PostgreSQL], [Javascript], [Web], [UI], [LiveServer]

Mentors: 
 - @jyang
 - @tdruez
 - @pombredanne
 - @tg1999

Related Issues:
 - https://github.com/nexB/purldb/issues/20

Description:

There are two tasks here:

1. Add UI:

Add a basic django UI for the project supporting queary by packages, scanning and matching.
We would be heavily reusing elements from scancode.io and vulnerabelcode to give it the
same look and feel.

2. Deploy a public server similar to https://public.vulnerablecode.io/ as a demo with packageDB
data. See https://github.com/nexB/vulnerablecode for reference. 


***

### VulnerableCode/scancode.io: return SPDX or CycloneDX report for VEX (Category B)

Repository: https://github.com/nexB/vulnerablecode and https://github.com/nexB/scancode.io

Reference: https://ntia.gov/files/ntia/publications/vex_one-page_summary.pdf

Size: Medium

Difficulty Level: Intermediate

Tags: [Python], [Security], [Vulneribility], [SBOM]

Mentors: 
 - @dmclark
 - @pombredanne

Description:

`vex` stands for vulnerability exploitability.

The goal of this project is to provide export capabilities to product VEX documents
that comply with industry-recognized formats. This can be in scancode.io enriching
the already existing Cyclonedx/SPDX outputs (or vulnerablecode?).

See the example VEX at
https://github.com/CycloneDX/bom-examples/blob/master/VEX/vex.json

There is a descriptive overview of the CycloneDX approach to VEX here
https://github.com/CycloneDX/bom-examples/tree/master/VEX


***
### VulnerableCode: Create a purl "virtual" database, library and service. (Category B)

A key attraction of VulnerableCode is its built-in support for purl. 
The goal of this project is to make purl more accessible and visible and:

- enhance the purl2url and url2purl support of the packageurl Python library
such that it can process more common package types
- enhance the packageurl Python library to convert more purl-like data to purl
and in particular the OSV format, the new NVD 5.0 reference, the ORT coordinates, etc. 
- enhance the purl2cpe VulnerableCode utility such that it can process more
cases to create better purls. Create script to  publish of a continuously updated
repository with the purl2pce data.
- expose a url2purl API service in VulnerableCode to help create correct
purls
- expose a purl2url API service in VulnerableCode to help return a list of URLs
given a purl.
- publish 

This is a large size project idea.



***
### VulnerableCode: Create a Vulnerability review app (Category B)

The goal of this web app (integrated in the core VulnerableCode) would be to
assist in the curation of vulnerabilities and the operation of VulnerableCode.

The UI would enable reviewers to triage, refine, improve and curate vulnerability data.
This could include linking and displaying remote references in place.

The UI should also help display importers and improvers errors and provide to
act on these to fix errors that require data resolution.

There are also data models needed to support an efficient review queue.

This is a large size project idea.

***
### VulnerableCode: Vulnerability code scanners (e.g. static code analysis): (Category B)

Create scanners which would verify whether a codebase is vulnerable to a
vulnerability. Once we know that a vulnerable package is in use, a scanner could
check for whether the vulnerable code is called, or if environmental conditions
or configuration are conducive to the vulnerability, etc. This could be based
on yara rules, OpenVAS or similar. Or based on Eclipse Steady and deeper code
analysis, static or dynamic.



***
### ScanCode.io: external storage and archival of scanned code.

This project should extend ScanCode.io such that it can use external storage for the scanned code.
The problem is that when you run a large number of projects the volume of storage that is
used in ScanCode.io grows a lot. For this we can now archive projects, but we cannot archive
the corresponding code that was scanned. The goal of this project is to add a new option
in ScanCode.io to also archive to some blob storage the code that was scanned such that:

- this can be done at the same time a project is archived

- it can be possible to restore from this archival a state that is essentially the same as 
the original project state in terms of files and data

- it would mean to archive the code input of a project or the whole workspace of a project

- as a bonus it should also export the projects data, codebase resources, packages and
  other models, such that this can be imported in another instance of the same version of Scancode.io

This is a medium or large size project idea.


***
### ScanCode.io: create a system and web UI to scan ALL the packages from Debian and fix and review all of them

This project would become a prototype to help scan and curate the package licensing of a specific ecosystem.
It would include:

- specific pipelines tuned to collect lists of all the packages and organize the scans of these correctly
- specific UI to visualize the queue of scan projects
- specific libraries to detect common licensing issues of this package type
- a UI to organize the community/peer review of all these package scans and issues
- extension to create reports and update the package type manifests (here Debian machine readable copyright files)

-See also [Create web application for massive scanning campaign of a whole package ecosystem](https://github.com/aboutcode-org/aboutcode/wiki/Project-Ideas-Scanning-Campaign-app)


This is a large size project idea.

***
### ScanCode.io: [Integrate alternative code analysis tools and scanners](https://github.com/aboutcode-org/aboutcode/wiki/Project-Ideas-Integration-with-other-code-analysis-tools-and-scanners)

In particular, this project could add a new pipeline for integration with external matching services
This would include tool such as SoftwareHeritage or Scanoss and other Component
or package identification integration. The goal would be to create "pipes"
and an improved package scanning pipeline that would include matching.


***
### ScanCode.io: [Integrate ORT dependency resolution in ScanCode.io](https://github.com/aboutcode-org/aboutcode/wiki/Project-Ideas-ORT-integration)

This is a large project idea.



***
### ScanCode.io: Add web service for software package and project evaluations and comparisons (djangopackages-like)

This project would build on the djangopackages/opencomparison code to provide:

  - a general purpose and easy way to create and share package comparison grids
  - their scanning integration in ScanCode.io

This is a large or medium project idea.


***
### ScanCode Toolkit: [Improve Copyright detection accuracy and speed in ScanCode](https://github.com/aboutcode-org/aboutcode/wiki/Project-Ideas-Improve-Copyright-Detection-Accuracy-and-Speed)

This is a medium size project idea.


***
### ScanCode Toolkit: [Create a high performance multi-pattern matching automaton](https://github.com/aboutcode-org/aboutcode/wiki/Project-Ideas-High-performance-string-matching)

This is to have faster license and copyright detection using less memory.


This is a large size project idea.

***
### TraceCode/ScanCode Toolkit/ScanCode.io: Source to binary reverse engineering

  This project is about the integration of multiple existing plugins and tools
  with a singular to find which source code used to create a compiled using symbols, 
  debug symbols, strings or more.

This is a large size project idea and this requires quite a bit of knowledge
of binaries and source and build processes.


***
### ScanCode Toolkit: License Language Server Protocol server for IDE integration

This project would implement a Language Server Protocol server for license and copyright
that would be usng ScanCode toolkit and provide live license and copyright feedback
directly in IDEs. It would also provide a plugin for integration in at least one
IDE such Atom, VSCode or Eclipse.

This is a large size project idea.

***
### Univers: Validate that the univers library can handle all the versions and ranges of all the packages! 

Project(s) in this domain would consist in building test suites and fix them for all the versions in univers.
Practically this means to download all the version of all the packages of an ecosystem (for instance PyPI) 
and validate that we can compare the version as good as the package management tool 
of reference for this ecosystem. For instance in alpine, 
https://git.alpinelinux.org/apk-tools/tree/test/version.sh?h=v2.12.9

Some specific highlights would cover:

- writing code that can collect the list of all the versions of all the packages
in a given package ecosystem (for instance PyPI, npm,etc). This code would be
likely in FetchCode or ScanCode Toolkit packagedcode module. This could be
extended to collect all the version ranges.

- write an automated test harness to ensure that the univers library can properly
parse (and unparse) all the versions and version ranges of all the packages.

- write an automated test harness to ensure that the univers library can properly
sort all the versions of each package in an ecosystem.

- Update the univers library accordingly and create a unit test suite as needed


***
### Package URL:  Chrome and Firefox extension to support browsing Package URL. 
Browsing pkg:pypi/packageurl-python/ should go to https://pypi.org/project/packageurl-python/

And create/register a Duck Duck Go bang mapper for 
https://github.com/package-url/packageurl-python/blob/main/src/packageurl/contrib/purl2url.py
Also add multiple URLs in purl2url.py


***
### DependentCode: [Create a mostly universal Package dependencies resolver](https://github.com/aboutcode-org/aboutcode/wiki/Project-Ideas-DependentCode-A-Mostly-Universal-Package-Dependency-Resolver)


***
### FetchCode/ScanCode.io: [Build a SoftwareHeritage API Client library](https://github.com/aboutcode-org/aboutcode/wiki/Project-Ideas-SoftwareHeritage-API-Client-Library)

***
### AboutCode Toolkit: [Improve AboutCode Toolkit with New/Enhance Features](https://github.com/aboutcode-org/aboutcode/wiki/Project-Ideas-Improve-AboutCode-ToolKit-with-New-and-Enhance-Features)



***
### CommonCode: Package name and version inference from a file name: get package name and version reliably

This project would provide a more reliable way to infer a package name and
version from a package archive name. For instance the simple cases of "log4j-1.2.3.jar"
could yield type:maven, name:log4j, version:1.2.3
Existing regex-based code in commoncode at https://github.com/nexB/commoncode/blob/main/src/commoncode/version.py
is a bit complex to maintain. The project could possibly use some machine learning.
In all case part of the project is to collect a test dataset of a large number of
released archives names from various sources (sf.net, SWH, Debian, Fedora) to use
as test (and possibly training set for ML)


***
### In search of popularity and prominence metric for software packages

See https://github.com/nexB/aboutcode/wiki/Project-Ideas-Project-popularity
