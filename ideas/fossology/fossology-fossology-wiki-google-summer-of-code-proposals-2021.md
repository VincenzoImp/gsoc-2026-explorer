# GSoC 2021 Microservice Proposal

**Parent:** FOSSology — Project Ideas
**Source:** https://github.com/fossology/fossology/wiki/Google-Summer-of-Code-Proposals-2021
**Scraped:** 2026-03-10T16:58:40.264623

---

## GSoC 2021 Run Students and Topic Links

| Name | Topic | Link |
| --- | --- | --- |
| Shruti Agarwal | UI | https://github.com/Shruti3004/fossology/wiki |
| Avinal Kumar | Build system | https://github.com/avinal/fossology/wiki |
| Aman Dwivedi | UI | https://github.com/Aman-Codes/fossology/wiki |
| Shreya Singh | Minerva | https://github.com/SinghShreya05/fossology/wiki |
| Sarita Singh | Scancode | https://github.com/itssingh/fossology/wiki |
| Omar AbdelSamea | Microservice | https://github.com/OmarAbdelSamea/fossology/wiki |
| Kaushlendra Pratap | Copyright | https://github.com/Kaushl2208/fossology/wiki |

## Intro

We from the fossology project would like to apply for GSOC. Please see two main resources for finding out more FOSSology in general:

* https://www.fossology.org
* https://github.com/fossology/fossology/wiki

Meetings: Checkout the [Meetings table](https://github.com/fossology/fossology/wiki/Google-Summer-of-Code-Proposals-2021#meetings-table)

## Interested in Application? - Getting Grip

If you are interested in an application - great! We encourage your application. So the question is how to get started with the topic, just a few points:

* Check https://www.fossology.org and these Github pages https://github.com/fossology/fossology/wiki
* Maybe check some initial intro at https://github.com/fossology/fossology/wiki/New-at-FOSSology%2C-You-Could-...
    * https://www.fossology.org/get-started/basic-workflow/
    * https://www.fossology.org/get-started/basic-training/
    * https://fossology.github.io/
* Try to install fossology, either using vagrant or docker
  + Check out our YouTube video for installation from source: https://youtu.be/q12KwmPYZG4
* Read the proposed topics
* Use the mailing list fossology-devel@fossology.org or contact proposed mentors for further steps
* [Slack invite link](https://join.slack.com/t/fossology/shared_invite/enQtNzI0OTEzMTk0MjYzLTYyZWQxNDc0N2JiZGU2YmI3YmI1NjE4NDVjOGYxMTVjNGY3Y2MzZmM1OGZmMWI5NTRjMzJlNjExZGU2N2I5NGY)
* [GitHub discussion](https://github.com/fossology/fossology/discussions/1881)
* If you are interested in trying to make contributions, see out issues with the label [good first issue](https://github.com/fossology/fossology/contribute). Maybe you could sort out the workflow and make a first pull request.

## Examples from Last Year

We were awarded three slots last year, please see here what was the result of it:

* Ayush and Kaushlendra's work on the [Atarashi](https://github.com/fossology/atarashi) license scanner and [Nirjas](https://github.com/fossology/Nirjas)
    - https://github.com/hastagAB/GSoC-2020
    - https://github.com/Kaushl2208/GSoC-2020
* Darshan's work on Dashboard: https://github.com/darshank15/GSoC_2020_FOSSOlogy/wiki

Also - very much fun - There are some YouTube videos created:
- Ayush made a youtube video / interview style of his experience: https://youtu.be/C8f_etew-yc
- Hypnos invited Darshan for an interview: https://youtu.be/_KbQ83JK7Q0

## Mentors

So far, the following users have opted themselves

* @ag4ums (Anupam)
* @GMishx (Gaurav)
* @shaheemazmalmmd (Shaheem)
* @mcjaeger (Michael)
* @viv9k (Vivek)
* @NicolasToussaint (Nicolas)
* @sjha2048 (Sahil)
* @hastagAB (Ayush)
* @vasudevmaduri (Vasudev)
* (Klaus Gmeinwieser)

Interested in becoming a mentor? please reach out to us!

## Topic Proposals

Following are the topics from last year. Please edit this wiki/reach out to us to add more proposals for GSoC 2021.

1. [Atarashi: Generating OSS License dataset](https://github.com/fossology/fossology/wiki/Google-Summer-of-Code-Proposals-2021#Atarashi-Generating-OSS-License-dataset)
1. [Migrating more pages to new UI](https://github.com/fossology/fossology/wiki/Google-Summer-of-Code-Proposals-2021#Migrating-more-pages-to-new-UI)
1. [Copyright False Positive Recognition with ML](https://github.com/fossology/fossology/wiki/Google-Summer-of-Code-Proposals-2021#Copyright-False-Positive-Recognition-with-ML)
1. [Migrate from Travis Github Actions](https://github.com/fossology/fossology/wiki/Google-Summer-of-Code-Proposals-2021#Migrate-from-Travis-to-Github-Actions)
1. [Integration of Open Source Review Toolkit](https://github.com/fossology/fossology/wiki/Google-Summer-of-Code-Proposals-2021#Integrating-Open-Source-Review-Toolkit)
1. [Integration of Scancode Toolkit](https://github.com/fossology/fossology/wiki/Google-Summer-of-Code-Proposals-2021#Integrating-Scancode-Toolkit)
1. [Integration of Reuse Project](https://github.com/fossology/fossology/wiki/Google-Summer-of-Code-Proposals-2021#Integration-of-Reuse-Project)
1. [Making FOSSology architecture more microservice friendly](https://github.com/fossology/fossology/wiki/Google-Summer-of-Code-Proposals-2021#making-fossology-architecture-more-microservice-friendly)

### Atarashi: Generating OSS License dataset

**Goal:** To create/generate OSS License dataset for [Atarashi](https://github.com/fossology/atarashi)

To implement any Machine learning/Deep learning algorithm we need a better and bigger dataset of [SPDX Licences](https://spdx.org/licenses/). But unfortunately, there exists no such dataset for open source licenses on the web.

There is a loose implementation of n-gramming different permutations and combinations of license text paragraphs. Ref: [SPDX-OSS Dataset](https://github.com/hastagAB/SPDX-OSS-Dataset). This method needs further improvement to make the dataset more accurate and realistic. 

Few suggested improvements: 
- Shifting from txt files to SPDX JSON endpoint
- Differentiating License Header from Full Text
- Adding FOSSology Nomos agent [STRINGS.in](https://github.com/fossology/fossology/blob/master/src/nomos/agent/STRINGS.in) regex in dataset creation
- Apart from these we strongly encourage students to pitch in some new ideas/methods/algorithms to achieve more accurate results. 

Resources: 
- [Atarashi](https://github.com/fossology/atarashi)
- [SPDX Licences](https://spdx.org/licenses/)
- [SPDX-OSS Dataset](https://github.com/hastagAB/SPDX-OSS-Dataset)
- [STRINGS.in](https://github.com/fossology/fossology/blob/master/src/nomos/agent/STRINGS.in) 
 
| Category | Rating |
| ---- | ---- |
| Low Hanging Fruit | - |
| Risk/Exploratory | ** |
| Fun/Periphial | ** |
| Core Development | ** |
| Project Infrastructure | - |

### Migrating more pages to new UI

FOSSology already have template based UI with the help of Symfony-Twig. In addition, FOSSology is using jQuery-UI, datatable, etc. to generate the pages. These are running for long and FOSSology needs a fresh view. Idea is to rewrite the UI using new technologies like Angular, Bootstrap, Vue.js or ReactJS. The twig-based templating could be considered for reuse.

The FOSSology UI initiated very HTML-90s style which works but does not look good today. A simple HTML has also the advantage that it runs from a variety of machines and different platform. Moreover, some of the PHP scripts even do not return HTML but just character streams. Today, the user base of FOSSology has grown and many persons use the Web UI. **The goal of this project** is to consistently provide a new UI technology to FOSSology which help to build more modern pages.

We have already worked on few pages of UI using bootstrap, Look at [PR - 1774](https://github.com/fossology/fossology/pull/1774). This can be referred as well with Angular Or ReactJS.

And last year, Sahil [proposed a design](https://xd.adobe.com/view/5a36e175-6496-48d7-4b9b-3221c85df525-2c07/) which can be referred for a fresh look. Also, Vivek has created a [proposal wiki](https://github.com/viv9k/fossology/wiki/Rewrite-fossology-UI-into-angular---proposal) which can give a good start into new approach.

| Category | Rating |
| ---- | ---- |
| Low Hanging Fruit | - |
| Risk/Exploratory | * |
| Fun/Periphial | * |
| Core Development | *** |
| Project Infrastructure | - |

### Copyright False Positive Recognition with ML

Fossology has copyright scanner to scan for the new copyrights from a file/packages. The current scanner findings are based on RegExp and has few false-positive findings as well.

The goal of this project is to find a machine learning technique/s that shall improve the copyright finding by detecting the false-positives.

| Category | Rating |
| ---- | ---- |
| Low Hanging Fruit | - |
| Risk/Exploratory | *** |
| Fun/Periphial | ** |
| Core Development | *** |
| Project Infrastructure | * |

### Migrate from Travis to Github Actions

The FOSSology project needs a continuous integration system to automate builds and tests. Since the beginning on the github, FOSSology has used only the free travis service for OSS projects. 

Now, it seems that using the Github Actions as general workflow automation will provide more versatile ways for implementing concrete continuous build and test services. As such, the current contious integration builds implemented with travis would be required to be migrated to Github Actions. In addition, it would be desirable to update the continuous build targets and used platforms to most recent versions.

| Category | Rating |
| ---- | ---- |
| Low Hanging Fruit | - |
| Risk/Exploratory | * |
| Fun/Periphial | * |
| Core Development | * |
| Project Infrastructure | *** |

### Integrating Open Source Review Toolkit

Build systems fetch the required dependencies (library/artifact) for a project while building the project. Its important to get an insight of these dependencies for license compliance check.

The [OSS Review Toolkit](https://github.com/oss-review-toolkit/ort) is an open source project helps to find dependencies in a project.
 
the goal of this project is to render the project dependencies created by ort and display those in the fossology-UI. Dependencies can be scheduled directly from the UI and scan with fossology.

| Category | Rating |
| ---- | ---- |
| Low Hanging Fruit | - |
| Risk/Exploratory | - |
| Fun/Periphial | ** |
| Core Development | *** |
| Project Infrastructure | * |

### Integrating Scancode Toolkit

The scancode toolkit is a very established license scanner similar to nomos or monk. It implements a number of different approaches and integrates these into one application for identify and classifying license relevant content in packages.

The basic idea is to use the command line interface from the scancode package in order to be called right from the fossology application. Fossology will pass a single file and takes the result from the scanscode command line call.

Major work will be required to adapt the existing integration of atrashi, in order reuse the efforts for a same integration with the scancode.

Important links:
* https://github.com/nexB/scancode-toolkit
* https://scancode-toolkit.readthedocs.io/en/latest/
* https://scancode-toolkit.readthedocs.io/en/latest/getting-started/install.html
* PR with atarashi external software integration that could serve as a blue print: https://github.com/fossology/fossology/pull/1634

| Category | Rating |
| ---- | ---- |
| Low Hanging Fruit | ** |
| Risk/Exploratory | * |
| Fun/Periphial | ** |
| Core Development | ** |
| Project Infrastructure | * |

### Integration of Reuse Project

Integrating [REUSE](https://reuse.software/) with fossology

Copyright and licensing is difficult, especially when reusing software from different projects that are released under various different licenses. REUSE make it easier for you to declare the licenses under which your works are released, but they also make it easier for a computer to understand how your project is licensed.
This specification defines a standardized method for declaring copyright and licensing for software projects.
REUSE also helps in creating a bill of materials with just one simple command. 

**The goal of this project**
* check license and copyrights for each files of package.
* List of files without licensing information, can to notified to the user of that package.  

Important links
- https://github.com/fsfe/reuse-tool
- https://reuse.software/spec/
- https://git.fsfe.org/reuse/tool

Existing issues:
- _Integrate REUSE standard_: #1592
- _Support the `SPDX-FileCopyrightText` keyword explicitly in the copyright agent_ #1513 
- _Detect 'foobar.license' files, as part of RESUE.Software standard_ #1833
 
| Category | Rating |
| ---- | ---- |
| Low Hanging Fruit | - |
| Risk/Exploratory | ** |
| Fun/Periphial | ** |
| Core Development | *** |
| Project Infrastructure | - |

### Making FOSSology architecture more microservice friendly

FOSSology is designed in modular fashion but it certainly does not follow micro-service architecture. For example, if there is a change in monk's logic, the whole source code has to be built again and installed. Whereas in micro-service architecture, only monk needs to be built and installed/deployed.

**Existing behavior:** In the current state, FOSSology is capable enough to run in a cluster mode. It can connect to other nodes in a cluster over SSH and execute agents. But it is not very flexible and has following drawbacks:

- When adding or removing a node, scheduler needs to be restarted.
- Every node needs to have same set of agents.
  + For example, you can not have one machine running only monk and one running only copyright.
- Because of the current version check mechanism on scheduler, for a single change, the whole code base needs to be redeployed to get new version string.
- The current architecture requires `fo-postinstall` to run on every new deployment to ensure correct DB schema and migrations.
  + Even though it is not a big push back, but it causes problems for some implementations. See [#1841](https://github.com/fossology/fossology/issues/1841), [#1818](https://github.com/fossology/fossology/issues/1818) and [#1809](https://github.com/fossology/fossology/issues/1809).

**Goal:** When the FOSSology follows more microservice friendly architecture, it can be deployed on Kubernetes and be able to scale-out or scale-in based on demand.

Resources:

- Cluster setup documentation: https://github.com/fossology/fossology/blob/master/debian/fossology-common.README.Debian#L19
- Further discussion: https://lists.fossology.org/g/fossology/topic/32746251
 
| Category | Rating |
| ---- | ---- |
| Low Hanging Fruit | - |
| Risk/Exploratory | *** |
| Fun/Periphial | ** |
| Core Development | ** |
| Project Infrastructure | *** |

# Meetings table
All the GSoC calls sorted on topics. Keeping the meetings open for everyone to join.

| Topic(s) | Timings | Meeting link | ICS |
| :--- | :--- | :---: | :--- |
| General meeting | *Thursdays* 15:30 - 16:30 UTC | [Microsoft Teams](https://teams.microsoft.com/l/meetup-join/19%3ameeting_NGQ1M2JlYTQtNDZiYy00NDZiLWEyNzMtNWIyMTUyN2NkZWI3%40thread.v2/0?context=%7b%22Tid%22%3a%2238ae3bcd-9579-4fd4-adda-b42e1495d55a%22%2c%22Oid%22%3a%226e60847e-e7c5-42c4-afae-746f2471a53a%22%7d) | [.ics](https://s.gmishx.in/y5zd5) |
| FOSSology UI Project | *Wednesdays* 15:30 - 16:30 UTC | [Microsoft Teams](https://teams.microsoft.com/l/meetup-join/19%3ameeting_ZjdmMDU4ODQtYWNmOS00ZmUyLWEzNzctOTdjYTc3MTAzYjE2%40thread.v2/0?context=%7b%22Tid%22%3a%2238ae3bcd-9579-4fd4-adda-b42e1495d55a%22%2c%22Oid%22%3a%227f1979f2-e3e3-40d0-8a77-bcef842abf7e%22%7d) | [.ics](https://s.gmishx.in/q6i84) |
| [Atarashi – Minerva](https://summerofcode.withgoogle.com/projects/#6705523560284160) | ~Wednesdays~ *Fridays* 12:30 - 13:30 UTC | [Microsoft Teams](https://teams.microsoft.com/l/meetup-join/19%3ameeting_M2Y5NmVmMDMtMDg5Ni00YmJkLThlZTItMjQwYjJhNGI3ZTU0%40thread.v2/0?context=%7b%22Tid%22%3a%2238ae3bcd-9579-4fd4-adda-b42e1495d55a%22%2c%22Oid%22%3a%22a2c4f566-cad3-46d5-9146-26004cf4bc7c%22%7d), [jitsi](https://meet.gmishx.in/GSoC21AtarashiCopyrightMicroservice) | [.ics](https://s.gmishx.in/7dww1) |
| [Copyright False Positive Detection Using ML](https://summerofcode.withgoogle.com/projects/#5794572136873984) ||||
| [Making FOSSology architecture microservice friendly](https://summerofcode.withgoogle.com/projects/#5361505685471232) ||||
| - | - | - | - |
| [New Build System and improving CI/CD workflow](https://summerofcode.withgoogle.com/projects/#4535841440923648) | *Fridays* 11:30 - 12:30 UTC | [Microsoft Teams](https://teams.microsoft.com/l/meetup-join/19%3ameeting_NWQ3YTE3ZGQtZTcyYi00ZTM2LWIxNTYtYTg5MDUzYmE0NGRh%40thread.v2/0?context=%7b%22Tid%22%3a%2238ae3bcd-9579-4fd4-adda-b42e1495d55a%22%2c%22Oid%22%3a%22a2c4f566-cad3-46d5-9146-26004cf4bc7c%22%7d) | [.ics](https://s.gmishx.in/mb12w) |
| [Integrating ScanCode Toolkit](https://summerofcode.withgoogle.com/projects/#6550787498442752) | *Tuesdays* 09:30 - 10:00 UTC | [Microsoft Teams](https://teams.microsoft.com/l/meetup-join/19%3ameeting_MmEzZTA0ZWQtMzYyNy00ODFlLTg3ZWQtMzgwNDhhOWJlNjkz%40thread.v2/0?context=%7b%22Tid%22%3a%2238ae3bcd-9579-4fd4-adda-b42e1495d55a%22%2c%22Oid%22%3a%226e60847e-e7c5-42c4-afae-746f2471a53a%22%7d) | [.ics](https://s.gmishx.in/lb8mq) |
| - | - | - | - |
