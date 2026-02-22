# MIT App Inventor — Project Ideas

**Source:** https://github.com/mit-cml/appinventor-sources/wiki/Google-Summer-of-Code-2026
**Scraped:** 2026-02-22T23:28:47.578248

---

# Introduction

Welcome to Google Summer of Code with MIT App Inventor.

We have an application process in addition to Google's application process. You must do both. Please apply to Google for GSoC through [Google’s Website](https://summerofcode.withgoogle.com/get-started/). All applications have to go through Google.

We will be receiving applications within the timeframe allocated by GSoC. Please consult the [GSoC website](https://summerofcode.withgoogle.com/get-started/) for details. For bite-sized issues to work on as part of the community introduction phase, please see the [help wanted issue list](/ideas/mit-app-inventor/mit-cml-appinventor-sources-issues).

Below is the list of projects we are proposing for the summer; you can choose one or more projects from the list or come up with your own project. Also note that these projects could be worked on outside GSoC if you would like to volunteer during the summer.

## Information for students

### How to apply

[Our application form for GSoC 2026 is here](https://docs.google.com/forms/d/e/1FAIpQLSf_5Mn3zDPk4EL_sbO5w14DukfYfQLP0srv72jXFoXUw8EfHg/viewform?usp=dialog). Additional instructions are linked from the application form.

# Potential Projects

This is what you might expect from projects in the list below:

* Brief explanation: An explanation of what the project is about. Please note that this might be just an idea, and as part of your work in the project you will be defining and scoping the project.

* Technical Difficulty: A rough idea of how difficult the project is given knowledge of the language but not necessarily the knowledge of the frameworks involved.

* Estimated Time Commitment: An estimate for the total number of hours required to be spent on the project to produce a working solution with testing.

* Knowledge Prerequisite: A brief list of the technologies needed in order to work on this project.

* Potential Mentor: The currently active team member you will probably be working with during the summer (this can also change depending on which projects are chosen).


---

# Projects list

## Artificial Intelligence Projects

### Trainable ChatBot interface and AI component

**Brief Explanation:** App Inventor has a growing offering of artificial intelligence features and is looking to add more cutting-edge AI learning experiences. We are looking to build a tool to create a trainable and customizable ChatBot that can be imported into an App Inventor app. This would be a similar experience to our Personal Image Classifer (PIC) and Personal Audio Classifer (PAC) extensions wherein there are external websites to build and train models, and these models are then exported and imported into App Inventor.
* PIC: https://classifier.appinventor.mit.edu/
* PAC: https://c1.appinventor.mit.edu/

Familiarity with RAG implementations and SLMs will be helpful.

**Technical Difficulty:** Hard

**Estimated Time Commitment:** 350 hours

**Knowledge Prerequisites:** Java, GWT, Javascript.

**Potential Mentors:** Natalie Lao

## Component Projects

### ListView Component Update

**Brief Explanation:** The ListView component offers a sophisticated set of behavior options. It supports both the addition of simple list elements by comma-delimited string and complex items by an interactive editor in the web designer. It supports several different layouts of list elements that include strings and images. Lists elements can display in a scrolling list style or a "swipe left" single element card style. Several parts of this need to be enhanced or refactored.

**Expected Results:** Add features: New layout matching a swipe-left browser with a large central image with text below as captions; refactor of web designer list item editor to use UIBinder layout template, be more user-friendly, and be keyboard navigable; multi-select support. Update some iOS features that do not work properly.

**Knowledge Prerequisites:** Java, GWT, swift

**Technical Difficulty**: Medium

**Estimated Time:** 175 hours

**Potential Mentors:** Susan Rati Lane

###Internationalization features for applications###

**Brief Explanation:** Currently, the App Inventor designer is available in 21 languages, but the mobile apps built with it cannot be internationalized. We would like to add multiple language support features to App Inventor.

**Expected Results:** Provide a UI in the designer, blocks editor, or a separate editor type. App Developers should be able to provide string translations for more than one language. There will need to be a way to reference these internationalized strings in both the designer and blocks editor. When compiling apps, the strings will have to be placed in the appropriate locations (values-LANG for Android LANG.lproj for iOS) and make use of the system specific APIs to read and use those strings at runtime.

**Github Issue:** https://github.com/mit-cml/appinventor-sources/issues/3710

**Knowledge Prerequisites:** Java, GWT, swift

**Technical Difficulty:** Hard

**Estimated Time:** 350 hours

**Potential Mentors:** Evan Patton

## Designer Projects

Improvements for the Designer view. This part of the system is built mainly with Java using the Google Web Toolkit.

 ### Better behavior for unimplemented components
Currently, when an Android-only component is added to a project and loaded into the iOS Companion, the app just crashes. We would like our iOS Companion to be able to detect that it is trying to load an unimplemented component and present the user with useful information about it. We would also like the app to run if it is possible without the unimplemented component.

  **Technical Difficulty:** Medium

  **Estimated Time:** 175 

  **Knowledge Prerequisite:** Swift

  **Potential Mentors:** Evan Patton, Susan Lane

### Learning Management System (LMS) Integrations

**Brief Explanation:** Integrate App Inventor with one or more LMS systems such as Google Classroom and Canvas.

**Expected Results:** An interface that allows course organisers to assign course work and manage submissions and grading of App Inventor projects through an existing LMS.

**Knowledge Prerequisites:** JavaScript and Java

**Technical Difficulty:** Medium

**Estimated Time:** 175 hours

**Potential Mentors:** Jose Dominguez or Jeff Schiller

### User defined components/extensions

**Brief Explanation:** Add the ability to create user-defined components (or extensions).  By which we mean an App Inventor user could take a set of App Inventor components (and blocks using those components) and wrap them up together in a single reusable unit which exposed a set of properties, methods and events.  In the initial implementation, perhaps, those units could only be used in the project in which they are defined, but ultimately you'd like for them to be exportable/importable, so that they could be used by other users (or that same user in other projects).

**Expected Results:** App Inventor users can create reusable components.

**Knowledge Prerequisites:** App Inventor, Java, GWT, UIBinder

**Technical Difficulty**: Hard

**Estimated Time:** 350 hours

**Potential Mentors:** Mark Friedman

## Additional Projects

### Github workflow hooks

**Brief Explanation:** The appinventor-sources repository behaves differently from the Github workflow expectations. In particular, we have two branches that function as master: master and ucr (Upcoming Component Release). Changes that must be installed on devices (Android or iOS Companion) need to be released at specific times of the year, so that work is branched from and merged into ucr. Changes that affect the web designer can be released at any time and are branched into/merged into master. Github does not recognize ucr for the purpose of updating linked issues and other features. We also would like to manage other issue labels, like updating when PRs need additional review, etc.

**Expected Results:** Write Github hooks to match our dual-master workflow.

**Knowledge Prerequisites:** Python, Git, Github

**Technical Difficulty**: Medium

**Estimated Time:** 175 hours

**Potential Mentors:** Evan Patton Jeff Schiller, or Susan Rati Lane

###Image gallery for easy options of background images###

**Brief Explanation:** Currently 

**Expected Results:**

**Github Issue:** https://github.com/mit-cml/appinventor-sources/issues/724

###UI for tracking and managing permissions used by components###

**Github Issue:** https://github.com/mit-cml/appinventor-sources/issues/1879
