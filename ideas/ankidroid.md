# AnkiDroid — Project Ideas

**Source:** https://docs.google.com/document/d/1ygIJl-Tp5_wJDKkSXrCC8h5K3WUG8D4BcJa_j70F0Zo
**Scraped:** 2026-02-22T23:28:47.567224

---

AnkiDroid’s GSoC 2026 Ideas List

[>> Direct Link to Ideas List <<](https://docs.google.com#h.sjaldbuk114s)

[AnkiDroid](https://www.google.com/url?q=https://github.com/ankidroid/Anki-Android/&sa=D&source=editors&ust=1771801024477976&usg=AOvVaw2jaDa93oIxPl81aBLEkFeZ) is a free Android flashcard app which makes remembering things easy [1] via use of spaced repetition. Because it's a lot more efficient than traditional study methods, you can either greatly decrease your time spent studying, or greatly increase the amount you learn.

Anyone who needs to remember things in their daily life can benefit from AnkiDroid. Since it is content-agnostic and supports images, audio, videos and scientific markup (via LaTeX), the possibilities are endless.

For example:

- Learning a language
- Studying for medical and law exams
- Memorizing people's names and faces
- Brushing up on geography
- Mastering long poems
- Even practicing guitar chords!

We are proud to have 4.8 stars on the [Play Store](https://www.google.com/url?q=https://play.google.com/store/apps/details?id%3Dcom.ichi2.anki&sa=D&source=editors&ust=1771801024479007&usg=AOvVaw0BgbkwbhLFL871nDBJ9QS7), and an installed audience of 4 million (as of January 2026). We have an active community of developers, with many new contributors joining every year and even new localizations. Many of the contributors discovered Android programming with AnkiDroid and we are always happy to help people contribute, independently of Google Summer of Code.

You can reach us on the [Anki Discord](https://www.google.com/url?q=https://discord.gg/qjzcRTx&sa=D&source=editors&ust=1771801024479487&usg=AOvVaw1jJsxzvFZGac9ERwhtfD5J) (#ankidroid-gsoc & #ankidroid-dev) or our [mailing list](https://www.google.com/url?q=https://groups.google.com/forum/?pli%3D1%23!forum/anki-android&sa=D&source=editors&ust=1771801024479588&usg=AOvVaw3iB3ZYUzCj5hcjYNcoQeW_).

We primarily use Discord for real-time communication, and GitHub issues for context on issues that would be useful for future contributors.

Our GSoC Mentors are:

- CriticalAY
[https://github.com/criticalAY](https://www.google.com/url?q=https://github.com/criticalAY&sa=D&source=editors&ust=1771801024479913&usg=AOvVaw2V148kU3MGR08Reylrk6Cq) - Sanjay Sargam
[https://github.com/SanjaySargam](https://www.google.com/url?q=https://github.com/SanjaySargam&sa=D&source=editors&ust=1771801024480039&usg=AOvVaw1r0it4dfNJw5snQbMmy24m)

Our Org Admins are:

Mike Hardy [https://github.com/mikehardy](https://www.google.com/url?q=https://github.com/mikehardy&sa=D&source=editors&ust=1771801024480252&usg=AOvVaw3IX1l7yrTIfNW1zSv7CPPj)

David Allison [https://github.com/david-allison](https://www.google.com/url?q=https://github.com/david-allison&sa=D&source=editors&ust=1771801024480369&usg=AOvVaw2bAamTlNE05pgzpMFoNhrT)

Our GitHub repository is: [https://github.com/ankidroid/Anki-Android/](https://www.google.com/url?q=https://github.com/ankidroid/Anki-Android/&sa=D&source=editors&ust=1771801024480529&usg=AOvVaw2e4lGRpKV3Tsvz_47hVUlo) and our Wiki contains a lot of useful information, including our [Getting Started page](https://www.google.com/url?q=https://github.com/ankidroid/Anki-Android/wiki/Development-Guide%23getting-started&sa=D&source=editors&ust=1771801024480665&usg=AOvVaw23Jh6hmxVE1slQfZPQfWVv).

In this document, you’ll find a list of projects that AnkiDroid would offer to mentor for if we are selected for GSoC in 2026.

[Redesign Deck Picker: Bottom App Bar Navigation (175/350 hours)](https://docs.google.com#h.nss20zvzsxd7)

[Experimental Open Source App Using the AnkiDroid API (175 / 350 hours)](https://docs.google.com#h.kq6i4ebqb99y)

[Experimental Wear OS – External Android App (175 / 350 hours)](https://docs.google.com#h.coccrd61d84e)

[Additional Widgets (175 hours)](https://docs.google.com#h.qt74fqeg4i9e)

[[Your Project Here] (175 hours)](https://docs.google.com#h.tg4bb877bpa3)

The current Deck Picker screen in AnkiDroid is feature-rich but can feel cluttered and difficult to navigate, especially as users add more decks and actions over time. Modern Android design guidelines encourage clearer navigation patterns and better use of bottom app bars for primary actions. Improving this screen will help both new and experienced users navigate their decks more efficiently, similar to Anki. Additionally, redesign the widgets if possible and make them better, or suggest new ones.

Redesign the Deck Picker screen using a Bottom App Bar–based navigation pattern

Improve discoverability of common actions without overwhelming the UI, and if chosen, widgets along with it, then improved/new widgets.

- Ashish Yadav
- Sanjay Sargam

AnkiDroid exposes an API (CardContentProvider) that allows external applications to interact with its data and features. However, there are limited real-world example apps that demonstrate how this API can be used effectively. An experimental app would help explore new ideas, validate the API design, and act as a reference for other developers.

Design and build a standalone, open-source Android app using the AnkiDroid API

Identify limitations or improvement areas in the existing API

- Sanjay Sargam

Wear OS devices offer quick, glanceable interactions that can complement mobile learning. Currently, AnkiDroid does not have a dedicated external Wear OS app that integrates cleanly with the main Android application. A Wear OS app would allow users to review or interact with cards in short sessions directly from their smartwatch

Build an external Wear OS application that integrates with AnkiDroid. Design interactions suitable for small screens and short usage sessions

- Sanjay Sargam

Widgets were introduced to AnkiDroid in 2010. These provide significant benefit to our power users and we started using them through GSoC 24, but there are still areas where stability,

usability, and functionality can be improved. I invite you to read last year’s contributor’s [report](https://www.google.com/url?q=https://github.com/xenonnn4w/GSoC-Report/blob/main/README.md&sa=D&source=editors&ust=1771801024486469&usg=AOvVaw1NSptcGhlzLYc57Iv-R0LG) to see what was done.


Review and improve the stability and performance of existing widgets

Android 12 Widget-based functionality is evaluated and integrated with the widgets when appropriate

- Ashish Yadav
- Sanjay Sargam

We welcome you to propose your own projects, but please get in touch with [our Mentors](https://docs.google.com#h.keijf5ilppgk) before writing your project proposal.

When you contact our mentors, you should provide a brief project description for consideration (similar to the high-level descriptions in this document).

Your project description should contain:

- Why the project matters to AnkiDroid
- What you expect to do by the end of the coding period
- Expected difficulty level
- Expected time (175, 350 hours, or maybe less than that if it is combined with another project)

- Please note: this is NOT eligible for a 90 hour project

- Technologies it will use. We use mostly Kotlin, but some JS/CSS/Rust/Java may be involved for some projects

We will not accept a project proposal that is not on the ideas list unless you have discussed it and found a mentor.
