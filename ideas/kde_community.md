# KDE Community — Project Ideas

**Source:** https://community.kde.org/GSoC/2026/Ideas
**Scraped:** 2026-02-22T23:28:47.569708

---

# GSoC/2026/Ideas

See also: [GSoC Instructions](/ideas/kde-community/gsoc), [Last year ideas](/ideas/kde-community/gsoc-2025-ideas)

## Guidelines

### Information for Students

**Read https://community.kde.org/GSoC#Instructions_for_potential_contributors**
It contains important information about the process and KDE stance on AI.

These ideas were contributed by our developers and users. They are sometimes vague or incomplete. If you wish to submit a proposal based on these ideas, you are urged to contact the developers and find out more about the particular suggestion you're looking at.

Becoming accepted as a Google Summer of Code student is quite competitive. Accepted students typically have thoroughly researched the technologies of their proposed project and have been in frequent contact with potential mentors. **Simply copying and pasting an idea here will not work. Neither will generating a proposal with ChatGPT or equivalent!** On the other hand, creating a completely new idea without first consulting potential mentors rarely works.

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



## Mankala

Mancala games are played all over the world and have many variants.

### Add a new Mancala Variant to Mankala Engine

**Project type:** Coding

**Brief explanation:** Add a new variant to Mankala Engine.

**Expected results:** An incomplete list of variants can be found on [[Wikipedia](https://en.wikipedia.org/wiki/List_of_mancala_games)]. Add a variant and test it out with people that play the know how to play the game.

**Knowledge Prerequisite:** C++

**Duration:** 175 hours

**Difficulty:** Medium

**Mentor:** Benson Muite, talk to me at [https://matrix.to/#/#mancala:kde.org](https://matrix.to/#/#mancala:kde.org)

### Enable Tournaments in Mankala

**Project type:** Coding

**Brief explanation:** Add a new variant to Mankala Engine.

**Expected results:** Build upon QXmpp to enable tournaments for mancala games in Mankala engine. The tournaments will be held online and can be run over several days during which people will play against each other or against computer opponents to find a champion. For inspiration see [https://kibao.org/](https://kibao.org/)

**Knowledge Prerequisite:** C++

**Duration:** 175 hours

**Difficulty:** Medium

**Mentor:** Benson Muite, talk to me at [https://matrix.to/#/#mancala:kde.org](https://matrix.to/#/#mancala:kde.org)

## Okular

Okular is a universal document viewer developed by KDE. Okular works on multiple platforms, including but not limited to Linux, Windows, Mac OS X, *BSD. Contact the Okular developers.

### Implement font subsetting when saving PDF files

**Project type:** Coding

**Brief explanation:** PDF files can contain annotations/forms. Users can write arbitrary text on those, meaning we need to embed the font to the PDF so other users on other systems can open those files. At this point we are embedding the full font when saving, which is non optimal space wise since modern fonts can be huge. PDF has this concept of subsetting in which only the characters needed for that particular text are added. We want to implement that. Most of the work will be done in poppler.

**Expected results:** When saving a PDF file with a new annotation that contains 4 characters, instead of embedding the full font to the PDF, only a font with those 4 characters is added to the PDF.

**Knowledge Prerequisite:** C++

**Duration:** 350 hours

**Difficulty:** Medium

**Mentor:** Albert Astals Cid <[[email protected]](https://community.kde.org/cdn-cgi/l/email-protection)>, talk to me at [https://matrix.to/#/#okular:kde.org](https://matrix.to/#/#okular:kde.org)

### PDF Image Alt text support via Structured information

**Project type:** Coding

**Brief explanation:** PDF files can contain structured information about the file. Poppler, the library we use to work with PDF files, reads it (at least partially). But the qt frontend of Poppler does not expose that information. The project would involve exposing that information in poppler-qt and then using it in Okular to be able to use it.

**Expected results:** The pdf file from bug 512838 shows ALT text as a tooltip

**Knowledge Prerequisite:** C++

**Duration:** 350 hours

**Difficulty:** Medium

**Mentor:** Albert Astals Cid <[[email protected]](https://community.kde.org/cdn-cgi/l/email-protection)>, talk to me at [https://matrix.to/#/#okular:kde.org](https://matrix.to/#/#okular:kde.org)

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

## Plasma Mobile

**Brief explanation:** Currently, Plasma Mobile has its own Wi-Fi, cellular networking and hotspot settings modules. They are very basic, and lack some features compared to their desktop equivalents (ex. enterprise Wi-Fi security). The desktop has a very functional networking settings module, but it has a large codebase and complex UI that is not easy to adapt to mobile usage.

The aim of the project is to improve the mobile networking settings so that it is functionally equivalent to the desktop experience. This includes support for enterprise Wi-Fi networks, VPN configuration, and etc. The tasks involves exposing configuration values from C++ to QML and writing some UI code around it (working heavily with NetworkManager and ModemManager). Developing a shared base with the desktop implementation and consolidating code is also a key goal.

**Expected results:** Mobile network KCMs can share more code with the desktop one and are more featureful

**Knowledge Prerequisite:** QML and C++

**Duration:** ~350 hours

**Difficulty:** Difficult

**Mentor:** Carl Schwan and rest of Plasma mobile team. [https://matrix.to/#/#plasmamobile:kde.org](https://matrix.to/#/#plasmamobile:kde.org)

## Drawy

### Implement Rich Text

**Brief explanation:**
The current text tool in Drawy is limited to plain text. Formatting applies to the entire text block, and it is not possible to use different styles for different parts of the text. The code is hard to extend and needs refactoring to support richer editing features and better maintainability.

Several important features are also missing. The text tool does not support spell checking, text alignment, or proper word wrapping. It also has limited support for international input and should allow different input methods, including dead keys required by many languages.

**Expected results:**
An improved rich text tool that allows different styles within the same text, supports text alignment, and integrates Sonnet (KDE's spell checking framework) for spell checking. The tool should support multiple input methods, implement word wrapping, and provide improved keyboard navigation.

**Knowledge Prerequisite:**
C++ and Qt

**Duration:**
~350 hours

**Difficulty:**
Difficult

**Mentor:**
Laurent Montel <[[email protected]](https://community.kde.org/cdn-cgi/l/email-protection)>

## Kdenlive

### Improve effect widgets

**Brief explanation:** Kdenlive is an advanced video editor. We support several libraries for our effects, but the effects user interface is managed in Kdenlive. Some effects currently don't have a proper user interface, and we would like to improve the situation. for example, libavfilter provides an effect allowing to adjust the color curves for each channel (red, green, blue, etc). We would need a proper widget allowing to edit curves with tabs to handle each channel. Another effect requires creating an arbitrary number of color gradients, so we need a widget to handle this. Speed ramp could also benefit from a nice UI to adjust speed of a video clip. We also use Qml overlays on the monitor which allow tweaking some parameters, so some work is also possible here.

**Expected results:** Nice looking, intuitive and powerful widgets to adjust effect parameters.

**Knowledge Prerequisite:** Qt (mostly QWidgets, some Qml) and C++.

**Duration:** ~350 hours.

**Difficulty:** medium

**Mentor:** Jean-Baptiste Mardelle <[[email protected]](https://community.kde.org/cdn-cgi/l/email-protection)>, helped by other Kdenlive devs. [#kdenlive-dev:kde.org](https://matrix.to/#/#kdenlive-dev:kde.org) on matrix.

## KStars

### AI-Powered Guiding Assistant

**Brief explanation**: Autoguiding is critical for long-exposure astrophotography, compensating for tracking errors by sending corrective pulses to the telescope mount. However, optimal guiding performance requires careful tuning of multiple parameters (aggressiveness, hysteresis, minimum move, declination mode) that vary significantly between mounts due to mechanical differences, periodic error, backlash, and non-linear response characteristics. The goal of this project is to develop an AI Guiding Assistant that learns mount-specific behavior and dynamically optimizes guide corrections in real-time.

The AI Guiding Assistant will:

**Augment Existing Guide Pulses**: Intercept guide pulses calculated by the EKOS Guide Module and apply learned corrections before sending to the mount via INDI. This preserves all existing guiding physics while adding intelligent optimization.

**Learn Mount Characteristics**: Analyze guide pulse history and mount response to build a model of mount-specific quirks including backlash patterns, periodic error signatures, declination drift behavior, and non-linear response curves.

**Real-time Parameter Optimization**: Dynamically adjust guiding aggressiveness, filtering, and response based on current seeing conditions, mount behavior, and guide star characteristics without requiring manual tuning.

**Training and Inference Modes**: Provide a training mode where the assistant learns mount behavior over multiple sessions, and an inference mode where it applies learned corrections. Users can enable/disable the assistant at any time for testing and comparison.

**Performance Metrics and Visualization**: Display RMS error improvements, correction patterns, and confidence metrics to help users understand the assistant's behavior and effectiveness.

The implementation will be based on [recent research in this domain](https://arxiv.org/pdf/2407.08046) and will utilize lightweight machine learning frameworks suitable for embedded systems.

**Expected results**:

- AI Guiding Assistant module integrated into EKOS Guide Module with enable/disable toggle
- Training mode to collect and analyze mount behavior data
- Real-time guide pulse augmentation with learned corrections
- Persistent model storage for mount-specific profiles
- Performance comparison tools showing improvement over standard guiding
- Documentation and user guide for optimal usage

**Knowledge Prerequisite**: C++, Qt, Machine Learning basics (PyTorch/TensorFlow or C++ ML libraries), Signal Processing, Control Systems

**Duration:** 350 hours

**Difficulty:** Hard

**Mentor**: Jasem Mutlaq ([KDE Web Chat](https://webchat.kde.org/#/room/#kstars:kde.org): Jasem)

## Lokalize

[Lokalize](https://invent.kde.org/sdk/lokalize) is KDE's translation system, enabling the translation of KDE programs as well as other external projects. All Lokalize tasks are mentored by Finley Watson (@fin-w:private.coffee , ask on [https://matrix.to/#/#kde-mentorship:kde.org](https://matrix.to/#/#kde-mentorship:kde.org) and I'll respond).

**WARNING:** I will reject all applications written by LLMs. If you can't be bothered to write it, I can't be bothered to read it. The purpose of contributing to KDE is for you to grow and learn.

### Project 1: Adapt PO file read / write to use libgettextpo

**Description:** The PO file format [is changing slightly](https://lists.gnu.org/archive/html/bug-gettext/2025-06/msg00018.html). Lokalize's PO file parser also has multiple problems with it (see the bug reports below). The mentee should research how viable [libgettextpo](https://www.gnu.org/software/gettext/manual/gettext.html) is to use as a replacement for the current parser, and decide if the library is suitable to integrate with existing PO read / write capability, and be prepared to work on a challenging task.

**Expected Results:** Bugs are fixed, Lokalize uses libgettextpo to read and write PO files, and the existing data structures in Lokalize are adapted to work with libgettextpo. Robust read / write ability, with new tests that cover bug report examples and confirm expected behaviour.

**Knowledge Prerequisite:** C++, QtWidgets, understand PO file format, test-driven development might be useful here

**Duration:** 350 hours

**Difficulty:** Difficult

**Related Bug Reports:**

[https://bugs.kde.org/show_bug.cgi?id=490802](https://bugs.kde.org/show_bug.cgi?id=490802)[https://bugs.kde.org/show_bug.cgi?id=76495](https://bugs.kde.org/show_bug.cgi?id=76495)[https://bugs.kde.org/show_bug.cgi?id=510320](https://bugs.kde.org/show_bug.cgi?id=510320)

### Project 2: Integrate Weblate API

**Description:** Weblate offers [an API](https://docs.weblate.org/en/latest/api.html) to load and save translations. A successful mentee will add a new project type, with the ability to log in to Weblate servers, and *at the very least* load and save translations to and from the remote server, allowing a translator to submit, review and approve translations for a project stored online. Glossary syncing would be a bonus, but not essential. You should consider [whole-file syncing](https://docs.weblate.org/en/latest/api.html#get--api-translations-(string-project)-(string-component)-(string-language)-file-) or per translation unit syncing. Assessment of relevant parts of the API is expected in the mentee's application, linking them to the relevant parts in the current codebase, in addition to examples of successful use of the API (e.g. with *curl* or another command-line tool).

**Knowledge Prerequisites:** C++, QtWidgets, REST APIs

**Duration:** 350 hours

**Difficulty:** Difficult

**Related Bug Reports:**

### Project 3: Redesign the translation memory tab

**Description:** The translation memory tab allows you to pick a TM (saved translation pairs from previous translation jobs / files) to search through, and shows the results in the list below. The UI needs redesigning to enable searching multiple memories at once by selecting the TMs you want to search, rather than picking only one from a drop-down. The selected TMs to search should be saved per-project, so translators can customise their translations per-project (e.g. only use translation memories with formal language for one specific project). Additionally, the "Manage translation memories" button opens a TM manager which should be merged into the tab instead of existing separately e.g. by moving TM-specific entries into the right-click menu, and adding more general buttons into the TM tab page, or the toolbar that is specific to the TM tab.

**Stretch Goal(s):** Fix the results list so the selected entry is highlighted with the correct colour from the theme (it seems broken?), and make entry rows only one line tall instead of many lines, when entry text is long.

**Expected Result:** A list of all TMs to pick instead of a drop-down, each entry checkable with a checkbox. Save selected TMs to the project data. Filter searches per TM grouping, searching each TM and sorting results sensibly.

**Knowledge Prerequisites:** C++, QtWidgets, UI design is beneficial

**Duration:** 350 hours

**Difficulty:** Medium

**Related Bug Reports:**
