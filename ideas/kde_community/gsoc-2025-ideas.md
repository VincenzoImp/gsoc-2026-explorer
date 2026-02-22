# Last year ideas

**Parent:** KDE Community — Project Ideas
**Source:** https://community.kde.org/GSoC/2025/Ideas
**Scraped:** 2026-02-22T23:28:47.570041

---

# GSoC/2025/Ideas

See also: [GSoC Instructions](https://community.kde.org/GSoC), [Last year ideas](https://community.kde.org/GSoC/2024/Ideas)

## Guidelines

### Information for Students

These ideas were contributed by our developers and users. They are sometimes vague or incomplete. If you wish to submit a proposal based on these ideas, you are urged to contact the developers and find out more about the particular suggestion you're looking at.

Becoming accepted as a Google Summer of Code student is quite competitive. Accepted students typically have thoroughly researched the technologies of their proposed project and have been in frequent contact with potential mentors. **Simply copying and pasting an idea here will not work. Neither generating a proposal with ChatGPT or equivalent!** On the other hand, creating a completely new idea without first consulting potential mentors rarely works.

When writing your proposal or asking for help from the general KDE community don't assume people are familiar with the ideas here. KDE is really big!

If there is no specific contact given you can ask questions on the general KDE development list [[email protected]](https://community.kde.org/cdn-cgi/l/email-protection). See [the KDE mailing lists page](http://www.kde.org/mailinglists/) for information on available mailing lists and how to subscribe.



### Adding a Proposal

When adding an idea to this section, please include the following data:

- if the application is not widely known, a description of what it does and where its code lives
- a
**brief explanation**(2-5 sentences, do not just put a link to a bug) - the expected size of the project (small-90 hours, medium-175 hours or large-350 hours)
- the expected results
- pre-requisites for working on your project (skills required/preferred)
- if applicable, links to more information or discussions
- mailing list or IRC channel for your application/library/module
- your name and email address for contact (if you're willing to be a mentor)
- if possible, an easy, medium or hard rating of the project


If you are not a developer but have a good idea for a proposal, get in contact with relevant developers first.



### Project: Something that you're totally excited about

**Brief explanation:** Do you have an awesome idea you want to work on with KDE but that is not among the ideas below? That's cool. We love that! But please do us a favor: Get in touch with a mentor early on and make sure your project is realistic and within the scope of KDE. That will spare you and us a lot of frustration.

**Expected results:** Something you and KDE loves

**Knowledge Prerequisite:** Probably C++ and Qt but depends on your project

**Duration:** Mention one of ~90, ~175 or ~350 hours of effort necessary to finish the project. Use only one of these three project classes and don't come up with other numbers here.

**Difficulty:** Easy, medium or difficult project

**Mentor:** Try to see who in KDE is interested in what you want to work on and approach them. If you are unsure you can always ask in [#kde-soc:kde.org](https://matrix.to/#/#kde-soc:kde.org) on matrix.



# Ideas



## Cantor

### Project: Python virtual environments in Cantor

**Brief explanation:** Cantor is a graphical frontend for different computer algebra systems and programming languages ([https://cantor.kde.org/](https://cantor.kde.org/)). For the Python backend, it lacks the support for Python virtual environments. The purpose of this project is to implement this missing functionality.

**Expected results:** Cantor can work with multiple Python virtual environment similarly to how it's possible in other IDEs like Spider-IDE, PyCharm, etc.

**Knowledge Prerequisite:** C++

**Duration:** ~350 hours

**Difficulty:** Difficult

**Mentors:** Alexander Semke, Israel Galadima, [https://matrix.to/#/#cantor:kde.org](https://matrix.to/#/#cantor:kde.org)

## KDE PIM/Merkuro

### Project: Port account management to QML

**Brief explanation:** Currently Merkuro makes use of QtWidgets dialog for managing the type of resources (accounts), the goal is to port all (or at least a some) of the dialogs to QML

**Expected results:** Making Merkuro a step closer to be fully usable on mobile

**Knowledge Prerequisite:** QML and C++

**Duration:** ~350 hours, but we can discuss to reduce the scopes

**Difficulty:** Difficult

**Mentors:** Carl Schwan, Claudio Cambra and Aakarsh MJ. Please contact us on #merkuro:kde.org (Matrix) and not via DM

### Project: Port to resources config plugin

**Brief explanation:** Some Akonadi agents and resources have their configuration dialog as part of the program. This is problematic as we want to make the resources lighter and not depends on QWidgets anymore as well as make the resources configurable even when not running. The goal is to port these configuration dialog to seperate plugins which can then be loaded by the calling application (e.g. Merkuro or KMail).

See the current status of the porting:

**Expected results:** Ideally all remaining resources and agents ported and the old API completely removed.

**Knowledge Prerequisite:** C++

**Duration:** ~175 hours

**Difficulty:** Medium

**Mentors:** Carl Schwan, Claudio Cambra and Aakarsh MJ. Please contact us on #merkuro:kde.org or #kontact:kde.org (Matrix) and not via DM



### Project: Rework indexing

**Brief explanation:** The goal is to make the index faster and reliable, reduce the scope of what we are indexing, but make sure we are indexing it correctly and in a way that will allow us to give the most meaningful results to users queries. There was a very old merge requests for this which will require some significant rebasing and also implementing the missing parts.

See [https://invent.kde.org/groups/pim/-/milestones/9#tab-issues](https://invent.kde.org/groups/pim/-/milestones/9#tab-issues)

**Expected results:** A good search in merkuro/kmail

**Knowledge Prerequisite:** C++ (no UI code)

**Duration:** ~350 hours

**Difficulty:** Difficult

**Mentors:** Carl Schwan. Please contact us on #merkuro:kde.org or #kontact:kde.org (Matrix) and not via DM

### Project: Integrate Itinerary in Merkuro Mail

**Brief explanation:** This requires using kitinerary in mimetreeparser directly or creating a plugin system. Importantly kitinerary should remains optional. The existing implementation for KMail/Messagelib/kdepim addons can serve as inspiration

**Expected results:**Merkuro Mail is able to extract tickets information from train/flight/event tickets and hotel reservation

**Knowledge Prerequisite:** C++ and QML

**Duration:** ~175 hours

**Difficulty:** Medium

**Mentors:** Carl Schwan, Claudio Cambra and Aakarsh MJ. Please contact us on #merkuro:kde.org (Matrix) and not via DM

## KArchive

### Project: Rewrite Zip backend to use libzip

**Brief explanation:** Currently karchive uses home grown code to handle zip files. The code is not very good since it gets confused when it finds token markers in what it is actual compressed data. See [https://bugs.kde.org/show_bug.cgi?id=450597](https://bugs.kde.org/show_bug.cgi?id=450597)

**Expected results:** KArchive uses libzip for handling zip files (and there's no regressions)

**Knowledge Prerequisite:** C++

**Duration:** ~350 hours

**Difficulty:** Difficult

**Mentor:** Albert Astals Cid <[[email protected]](https://community.kde.org/cdn-cgi/l/email-protection)>



## Internationalization

### Project: Move translation files to git

**Brief explanation:** Translation files currently live in SVN, they are one of the last things in SVN, and the sysadmin team would welcome if we stop using it so they can shut down the server (also some folks have trouble using SVN since it's now starting to become old). The plan is to move files to GIT but we need to make sure the history is preserved and the associated scripts are adapted. See more at [https://invent.kde.org/teams/localization/issues/-/issues/1](https://invent.kde.org/teams/localization/issues/-/issues/1)

**Expected results:** Most/All of what is described above is done.

**Knowledge Prerequisite:** git/bash/python

**Duration:** ~350 hours

**Difficulty:** Medium

**Mentor:** Albert Astals Cid/Luigi Toscano, talk to us at [https://matrix.to/#/#kde-i18n:kde.org](https://matrix.to/#/#kde-i18n:kde.org)



## Plasma

### Project: Make KWin aware of game controllers

**Brief explanation:** Plasma could do a lot to improve support for game controllers: gamepads, fight sticks, flight sticks, and more. But before we can work on advanced features like button mapping or mouse emulation, Plasma's Wayland compositor KWin first needs to take control of controller input. The task is to modify KWin so it reads game controller input events and provides it back to games/applications unmodified. Once that's in place, the sky's the limit.

**Expected results:** KWin has access to game controller input events, games still work, and Plasma does not suspend the system as long as you use the controller ([one of our oldest bugs](https://bugs.kde.org/show_bug.cgi?id=328987))

**Knowledge Prerequisite:** C++, a little Qt, patience to dive into KWin and Wayland protocols

**Duration:** ~350 hours

**Difficulty:** Difficult

**Mentor:** Xaver Hugl. Introduce yourself on #kde-input:kde.org (Matrix) and tag user @zamundaaa

### Project: Make Plasma Virtual Keyboard production-ready

**Brief explanation:** Evolve the current proof of concept into a solution that can be shipped with Plasma by default. Currently it's based on the Qt Virtual Keyboard API [[1]](https://mail.kde.org/pipermail/plasma-devel/2024-June/123435.html) [[2]](https://mail.kde.org/pipermail/plasma-devel/2025-January/123611.html). It still needs lots of work and polish first though. That's where you come in!

**Expected results:** A virtual keyboard that works well for different languages and can be shipped with Plasma. It should be usable on phones, tablets and the likes.

**Knowledge Prerequisite:** C++, a little Qt, understanding of how Wayland works.

**Duration:** ~350 hours

**Difficulty:** Difficult

**Mentor:** Aleix Pol. Introduce yourself on #kde-input:kde.org (Matrix) and tag user @apol:kde.org

### Project: Select & use more than one input method

**Brief explanation:** Different users require different ways to input text. Some will need an on-screen keyboard for their tablet, phone, or laptop touchscreen. Some use fcitx5 or IBus to enter complex characters with their keyboard. Some would like to dictate or generate text with the help of an AI model. Some would like all of the above depending on the situation. Plasma on Wayland currently lets you select one input method as "Virtual Keyboard" in System Settings, but ideally we want many input methods to co-exist peacefully.

**Expected results:** On the less ambitious end, Plasma and KWin will let you switch between input methods / virtual keyboard on the fly. On the more ambitious end, multiple input methods can be active at the same time so you can e.g. use fcitx5 for physical keyboard input and Maliit or plasma-keyboard as on-screen keyboard.

**Knowledge Prerequisite:** C++, a little Qt, understanding of how Wayland works

**Duration:** ~350 hours

**Difficulty:** Difficult

**Mentor:** Eike Hein. Introduce yourself on #kde-input:kde.org (Matrix) and tag user @hein:kde.org

### Project: Improve input handling in ways that you're totally excited about

**Brief explanation:** Input handling is [one of the elected KDE Goals](https://phabricator.kde.org/T17433) and we're looking for all the help we can get. If you have an itch that needs scratching, and none of the other ideas on this page look quite right to you, we're still interested in your contributions. Drop by on our Matrix channel (see below) and let's discuss what your project could look like.

**Expected results:** An input-related GSoC application drafted with community input but including many of your own ideas, opinions and planned milestones. Once selected, actually delivering on those plans.

**Knowledge Prerequisite:** Depends on the project, but probably C++, Qt, and a basic understanding of Wayland

**Duration:** 90, 175 or 350 hours, depending on what you sign up for

**Difficulty:** also depends on the project

**Mentor:** Jakob Petsovits (@jpetso:kde.org) and/or other interested KDE people in the #kde-input:kde.org (Matrix) chatroom. Say hi and let's chat!

## Plasma Mobile

**Brief explanation:** Currently, Plasma Mobile has its own Wi-Fi, cellular networking and hotspot settings modules. They are very basic, and lack some features compared to their desktop equivalents (ex. enterprise Wi-Fi security). The desktop has a very functional networking settings module, but it has a large codebase and complex UI that is not easy to adapt to mobile usage.

The aim of the project is to improve the mobile networking settings so that it is functionally equivalent to the desktop experience. This includes support for enterprise Wi-Fi networks, VPN configuration, and etc. The tasks involves exposing configuration values from C++ to QML and writing some UI code around it (working heavily with NetworkManager and ModemManager). Developing a shared base with the desktop implementation and consolidating code is also a key goal.

**Expected results:** Mobile network KCMs can share more code with the desktop one and are more featureful

**Knowledge Prerequisite:** QML and C++

**Duration:** ~350 hours

**Difficulty:** Difficult

**Mentor:** Carl Schwan and rest of Plasma mobile team. [https://matrix.to/#/#plasmamobile:kde.org](https://matrix.to/#/#plasmamobile:kde.org)

## KDE Linux

### Kirigami ISO Image Writer

**Brief explanation:** Create a GUI in [Kirigami](https://develop.kde.org/frameworks/kirigami//) for [ISO Image Writer](https://apps.kde.org/fr/isoimagewriter/): [https://invent.kde.org/kde-linux/kde-linux/-/issues/132](https://invent.kde.org/kde-linux/kde-linux/-/issues/132)

**Expected results:** ISO Image Writer GUI rewrite using Kirigami.

**Knowledge Prerequisite:** QML and C++

**Duration:** ~350 hours

**Difficulty:** Difficult

**Mentor:** Harald Sitter et al. [https://matrix.to/#/#kde-linux:kde.org](https://matrix.to/#/#kde-linux:kde.org)

### Backup Prototype

**Brief explanation:** Backuping its data is important to not lose them. Whether it's duplicating locally, on the same network or on an external server to be able to retrieve them in case of bad manipulation or incident. The tool should also be robust and trustable (when it says it copied, it really copied). The projects aims to create a prototype which satisfies these conditions: [https://invent.kde.org/kde-linux/kde-linux/-/issues/131](https://invent.kde.org/kde-linux/kde-linux/-/issues/131)

**Expected results:** A prototype for a local backup solution that is robust

**Knowledge Prerequisite:** QML and C++

**Duration:** ~350 hours

**Difficulty:** Difficult

**Mentor:** Harald Sitter et al. [https://matrix.to/#/#kde-linux:kde.org](https://matrix.to/#/#kde-linux:kde.org)

### CVE/Security Tracker

**Brief explanation:** Security is one of the core values that matters to people. When we install software, we should know if the version has known vulnerabilities and if we can update it to a version that have it fixed. This project aims to create a solution that will allow to track them: [https://invent.kde.org/kde-linux/kde-linux/-/issues/134](https://invent.kde.org/kde-linux/kde-linux/-/issues/134)

**Expected results:** A system that can track security advisories. Ideally a web based solution.

**Knowledge Prerequisite:** Any programming language

**Duration:** ~350 hours

**Difficulty:** Difficult

**Mentor:** Harald Sitter et al. [https://matrix.to/#/#kde-linux:kde.org](https://matrix.to/#/#kde-linux:kde.org)

### Recovery Infrastructure

**Brief explanation:** When your computer crash or do not start, you'd like to recover as much as you can. The aim of the task is to create a tool that would allow to recover this data: [https://invent.kde.org/kde-linux/kde-linux/-/issues/135](https://invent.kde.org/kde-linux/kde-linux/-/issues/135)

**Expected results:** A prototype of a system/application to help users and OEMs recover a broken system, or at least its data.

**Knowledge Prerequisite:** QML and C++, possibly others

**Duration:** ~350 hours

**Difficulty:** Difficult

**Mentor:** Harald Sitter et al. [https://matrix.to/#/#kde-linux:kde.org](https://matrix.to/#/#kde-linux:kde.org)

### Replication Infrastructure

**Brief explanation:** When you change computer, you may want to keep some data: installed applications, configuration files, personal data... The aim of the project is to create a tool that will allow to synchronise data between two machines: [https://invent.kde.org/kde-linux/kde-linux/-/issues/136](https://invent.kde.org/kde-linux/kde-linux/-/issues/136)

**Expected results:** A prototype of a system/application to help users replicate (or move) from one system to another.

**Knowledge Prerequisite:** QML and C++

**Duration:** ~350 hours

**Difficulty:** Difficult

**Mentor:** Harald Sitter et al. [https://matrix.to/#/#kde-linux:kde.org](https://matrix.to/#/#kde-linux:kde.org)

### Karton

**Brief explanation:** KDE has developed its own [virtual machine application](https://invent.kde.org/arraybolt/karton). The aim of the project is to create a Kirigami graphical interface to the tool: [https://invent.kde.org/kde-linux/kde-linux/-/issues/133](https://invent.kde.org/kde-linux/kde-linux/-/issues/133)

**Expected results:** A polished Kirigami-based virtual machine application that can replace virt-manager and virtualbox for most users.

**Knowledge Prerequisite:** QML and C++

**Duration:** ~350 hours

**Difficulty:** Difficult

**Mentor:** Harald Sitter et al. [https://matrix.to/#/#kde-linux:kde.org](https://matrix.to/#/#kde-linux:kde.org)

### Automatic Testing

**Brief explanation:** The goal of this project is to develop automated tests which will allow to detect regressions before pushing new features/tools to the user: [https://invent.kde.org/kde-linux/kde-linux/-/issues/79](https://invent.kde.org/kde-linux/kde-linux/-/issues/79).

**Expected results:** Fully automated tests to detect regressions in KDE Linux

**Knowledge Prerequisite:** Bash, Python, Perl

**Duration:** ~350 hours

**Difficulty:** Medium

**Mentor:** Harald Sitter et al. [https://matrix.to/#/#kde-linux:kde.org](https://matrix.to/#/#kde-linux:kde.org)

### Website

**Brief explanation:** KDE Linux needs to have a website. There are already some websites in KDE done with Hugo. The aim of the task is to create a website for KDE Linux, including multiple infos such as Downloads links, Community links... More details can be found at [https://invent.kde.org/kde-linux/kde-linux/-/issues/92](https://invent.kde.org/kde-linux/kde-linux/-/issues/92)

**Expected results:** A swanky website for KDE Linux using Hugo

**Knowledge Prerequisite:** Web development, ideally using Hugo

**Duration:** ~90 hours

**Difficulty:** Easy

**Mentor:** Harald Sitter et al. [https://matrix.to/#/#kde-linux:kde.org](https://matrix.to/#/#kde-linux:kde.org)

## KDE Games

### Mankala: Bao La Kiswahili

**Brief explanation:** Add Bao La Kiswahili and create a computerized opponent with various levels of difficulty for it. Explore the use of machine learning algorithms in creating a computerized opponent. Code can be found at [https://invent.kde.org/joaotgouveia/mankala](https://invent.kde.org/joaotgouveia/mankala). Suggestions for other Mankala games or other improvements are also welcome.

**Expected results:** An additional game in Mankala or other improvments to the software.

**Knowledge Prerequisite:** C++, Qt, QML

**Duration:** ~175 hours

**Difficulty:** Medium

**Mentor:** Benson Muite contact through [https://matrix.to/#/#mancala:kde.org](https://matrix.to/#/#mancala:kde.org)

## Misc

### Project: Add more fuzzed libraries to oss-fuzz

**Brief explanation:** oss-fuzz is a SAS for fuzzying code. We have a few libraries there (karchive, kimagefomats, kcodecs), but we should add more since we have quite some code that processes file formats.

**Expected results:** As many projects/libraries as possible have been added to oss-fuzz

**Knowledge Prerequisite:** docker/compiling

**Duration:** ~350 hours

**Difficulty:** Medium

**Mentor:** Albert Astals Cid <[[email protected]](https://community.kde.org/cdn-cgi/l/email-protection)>

## GCompris

### Project: Enhancing GCompris Server with GUI Sub-Programs for Dataset Creation

**Project Overview:**
This project aims to enhance the GCompris server by integrating a set of GUI-based sub-programs specifically designed for teachers. These tools will facilitate the creation of new datasets for various educational applications.The applications targeted for dataset expansion include:

Grammar Analyses Graduated Lines Decimal Numbers Share Fractions Create

By implementing these sub-programs, educators will be able to customize learning materials more effectively to fit their pupils needs.

**Resources Required:**

Developers with experience in Qt/QML, Gitlab. Being able to compile GCompris on QT6 and use it.

**Development resources:**

The server source code is available here : [https://invent.kde.org/education/gcompris/-/tree/work/server_qt6?ref_type=heads](https://invent.kde.org/education/gcompris/-/tree/work/server_qt6?ref_type=heads)
The development guide is here: [https://invent.kde.org/education/gcompris/-/wikis/Developers-corner/Development-process](https://invent.kde.org/education/gcompris/-/wikis/Developers-corner/Development-process)

**Duration:** ~175 hours

**Difficulty:** Middle

**Mentor:** Emmanuel Charruau, Johnny Jazeix (contact on Matrix KDE Webchat)

## Kdenlive

### Project: Improving Kdenlive timeline markers

**Brief explanation:** Kdenlive already allows the user to add markers to the timeline and inside clips. The idea is to update the current code to add a duration attribute to the markers. With this change, markers will be able to represent a time range with a start and an end time, which will unlock some nice new features. See [this issue](https://invent.kde.org/multimedia/kdenlive/-/issues/614) for more technical details.

**Expected results:** An nice display of the time range markers in the timeline and monitors. The marker's time range should also be connected to existing features and extend them, like render a marker's range, or improved searching.

**Knowledge Prerequisite:** C++, Qt, will also involve some Qml

**Duration:** ~175 hours

**Difficulty:** Medium

**Mentor:** Jean-Baptiste Mardelle ([https://matrix.to/#/@j-b-m:matrix.org](https://matrix.to/#/@j-b-m:matrix.org))

## Marknote

### Project: Implement block editor

**Brief explanation:** Implement a basic block editor where each elements from markdown is transformed into a block which can be drag-and-dropped.

Inspiration can be taken from [https://rubymamistvalove.com/block-editor](https://rubymamistvalove.com/block-editor)

**Expected results:** A nice rich text editor which can then be also reused in other apps like Merkuro Mail.

**Knowledge Prerequisite:** C++, Qt, will also involve some Qml

**Duration:** ~350 hours

**Difficulty:** Medium

**Mentor:** Carl Schwan ([https://matrix.to/#/#marknote:kde.org](https://matrix.to/#/#marknote:kde.org))

## digiKam

### Project: Interface the database search engine to an AI based LLM

**Brief explanation:** The digiKam photo management program already allows the user to search items over the collections using a database. Many powerful search tools can find items by many criteria such as metadata, aesthetic contents, face, place, date, hierarchical keywords, etc. The idea is to add a new top-level interface where users can enter a human phrase which describes the contents to search. With this change, the searches can be user-friendly to use without having to pass plenty of settings used to tune the engine. The LLM must be included in the application, without using an external web-service, as it's not permitted to share data over the Internet. All the new implementations must be written in C++, not Python.

Relevant entries in bugzilla:
- [wish 497938](https://bugs.kde.org/show_bug.cgi?id=497938)
- [wish 367700](https://bugs.kde.org/show_bug.cgi?id=367700)

**Expected results:** A nice and simple view where users type a human comprehensive phrase to search items over the photo collections.

**Knowledge Prerequisite:** C++, Qt, OpenCV, AI modeling, Large Language Model

**Duration:** ~350 hours

**Difficulty:** Difficult

**Mentor:** Michael Miller ([[email protected]](https://community.kde.org/cdn-cgi/l/email-protection)), Maik Qualmann ([[email protected]](https://community.kde.org/cdn-cgi/l/email-protection)), and Gilles Caulier ([[email protected]](https://community.kde.org/cdn-cgi/l/email-protection))

## Mentorships

### Project: Help us expand the Mentorship program website

**Brief explanation:** The mentorship program aims to encourage people to become contributors to KDE, expand their technical knowledge, become comfortable working with the community, and learn about Free Software.

One of KDE's goals for the next 2 years is "KDE Needs You". It aims to ensure a regular flow of contributors to KDE and having a solid mentorship program to ease the way for said contributors is key to the success of the project.

The current website is very barebones and we need to modernise and expand it so new users can easily find out about and manage their mentorship programs.

**Expected results:** A modern-looking, user-friendly, informative site that will guide users to the program from which they will learn most and will make the most of their skills.

**Knowledge Prerequisite:** Go, HuGo, CSS, JavaScript, (web)Design

**Duration:** ~175 hours.

**Difficulty:** Easy code wise, medium design wise

**Mentor:** Farid Abdelnour <[[email protected]](https://community.kde.org/cdn-cgi/l/email-protection)>, Paul Brown ([https://matrix.to/#/@bro666:kde.org](https://matrix.to/#/@bro666:kde.org))
