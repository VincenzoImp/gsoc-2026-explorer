# Wikimedia Foundation — Project Ideas

**Source:** https://www.mediawiki.org/wiki/Google_Summer_of_Code/2026#Projects
**Scraped:** 2026-02-22T23:28:47.556167

---

# Google Summer of Code/2026

## Program timeline

[[edit](https://www.mediawiki.org/w/index.php?title=Google_Summer_of_Code/2026&action=edit§ion=1)]

|
|---|

Applicants = Wikimedia mentors and/or GSoC contributors; Contributors = interns, junior developers

## Projects

[[edit](https://www.mediawiki.org/w/index.php?title=Google_Summer_of_Code/2026&action=edit§ion=2)]

Project proposals were submitted and tracked via [this Phabricator task](https://phabricator.wikimedia.org/T414121). Proposal submissions closed on January 26 2026.

*Please see the individual Phabricator link under each project for further details.*

### Bulk OCR Improvements

[[edit](https://www.mediawiki.org/w/index.php?title=Google_Summer_of_Code/2026&action=edit§ion=3)]

Wikisource is an online wiki-based digital library of free-content textual sources operated by the Wikimedia Foundation. The Bulk OCR feature aims to provide an easy way for volunteers to OCR multiple pages or, say, an entire book on Wikisource. However, the ability to perform bulk OCR on any work should be restricted only to certain groups of users. To this end, there is a need to add features to the Wikisource extension to allow authorized users to OCR multiple pages at once and insert the OCRed text back into the relevant text layer of the corresponding pages of the book on Wikisource.

- Phabricator:
[T415145](https://phabricator.wikimedia.org/T415145) - Skills required: Javascript, HTML, CSS, familiarity with object oriented programming, experience with PHP and Mediawiki are bonuses, familiarity with the
[Wikimedia OCR](https://phabricator.wikimedia.org/tag/wikimedia_ocr/)project - Mentors: Parthiv Menon (
[theprotonade](https://phabricator.wikimedia.org/p/theprotonade/)), Satdeep Gill ([SGill](https://phabricator.wikimedia.org/p/SGill/)) - Size: 350 hours
- Difficulty: Medium

### CampWiz NxT Redesign

[[edit](https://www.mediawiki.org/w/index.php?title=Google_Summer_of_Code/2026&action=edit§ion=4)]

CampWiz NXT is a comprehensive tool designed to facilitate the evaluation of media files such as images, audios, and videos uploaded to Wikimedia Commons during Wiki Loves contests. CampWiz NXT streamlines the jury process by offering a structured and efficient platform for media assessment. In the past, when it was developed, we took dual server approach with nextjs as frontend server and golang as backend server. But, now we need to migrate our frontend from nextjs to pure react with minimal functionality change.

- Phabricator:
[T414269](https://phabricator.wikimedia.org/T414269) - Skills required: Proficiency in React for building modular, maintainable user interfaces. Experience with Next.js for modern frontend development and static site generation. Familiarity with the Material UI component library for implementing accessible, consistent, and responsive designs.
- Mentors:
[Nokib_Sarkar](https://phabricator.wikimedia.org/p/Nokib_Sarkar/),[Tiven2240](https://phabricator.wikimedia.org/p/Tiven2240/) - Size: around 90 hours
- Difficulty: Medium

### Gamifying constraint violation fixes on Wikidata

[[edit](https://www.mediawiki.org/w/index.php?title=Google_Summer_of_Code/2026&action=edit§ion=5)]

Develop a game to make edits to Wikidata to fix constraint violations. The requirements for being a game here is not only that the tool is easy to use but also that there are methods that keep users engaged, such as scores, leaderboards, collaborations, and challenges. There may be aspects of community collaboration in some games.

- Phabricator:
[T387248](https://phabricator.wikimedia.org/T387248) - Skills required: Understanding of Wikidata. Game Design. SPARQL proficiency. Proficiency in Python or another scripting language.
- Mentors:
[Peter F. Patel Schneider](https://phabricator.wikimedia.org/p/Pfps/),[David Martin](https://phabricator.wikimedia.org/p/DMartin-WMF/) - Size: 350 hours
- Difficulty: Medium

### Implement lossless JPG transformations in the Commons Android App

[[edit](https://www.mediawiki.org/w/index.php?title=Google_Summer_of_Code/2026&action=edit§ion=6)]

The project aims to add picture editing capabilities with lossless transformations to the app:

- Lossless crop.
- Lossless blur: JPG images are made of many 8x8 pixel blocks. The idea here is to blur only the JPG blocks showing what the users wants to blur, without recompressing the other blocks.
- Option to automatically blur people faces and car number plates.

- Phabricator:
[T415446](https://phabricator.wikimedia.org/T415446) - Skills required: Strong Android fundamentals, Kotlin. No prior knowledge of JPG format required.
- Mentors:
[Nicolas_Raoul](https://phabricator.wikimedia.org/p/Nicolas_Raoul/)(past maintainer),[RitikaPahwa4444](https://phabricator.wikimedia.org/p/RitikaPahwa4444/)(current maintainer) - Size: 350 hours
- Difficulty: Medium

### Integration testing for extensions in Canasta

[[edit](https://www.mediawiki.org/w/index.php?title=Google_Summer_of_Code/2026&action=edit§ion=7)]

[Canasta](https://canasta.wiki/) is a fairly large MediaWiki distribution that includes, besides MediaWiki itself, over 150 extensions, 10 skins, a full LAMP stack, and a variety of other applications and libraries, like Elasticsearch. This amount of software makes Canasta a full-featured solution, but it also means that many things can go wrong. An upgrade to some component could result in that component breaking - or could even result in the entire system breaking. There is already a plan to add testing of core MediaWiki, via [this](https://github.com/CanastaWiki/CanastaBase/pull/46) pending pull request. That leaves MediaWiki extensions (and, to a much lesser extent, skins). This project would add testing of these to the Canasta continuous integration (CI) pipeline, so that testing is done of every patch, helping to ensure that no change is destructive.

- Phabricator:
[T414617](https://phabricator.wikimedia.org/T414617) - Skills required: Familiarity with integration testing required, knowledge of GitHub Actions, Docker and the PHPUnit, Jest and SonarQube testing frameworks preferred
- Mentors:
[Yaron_Koren](https://phabricator.wikimedia.org/p/Yaron_Koren/),[cicalese](https://phabricator.wikimedia.org/p/cicalese/) - Size: 350 hours
- Difficulty: Medium

### Modularization + Jetpack Compose in Android Commons App

[[edit](https://www.mediawiki.org/w/index.php?title=Google_Summer_of_Code/2026&action=edit§ion=8)]

The project aims to revamp the app architecture using Jetpack Compose.

- Phabricator:
[T415272](https://phabricator.wikimedia.org/T415272) - Skills required: Strong Android fundamentals, Kotlin, Jetpack Compose
- Mentors:
[Kaartic](https://phabricator.wikimedia.org/p/Kaartic/)(past maintainer),[Neeldoshii](https://phabricator.wikimedia.org/p/Neeldoshii/) - Size: 350 hours
- Difficulty: Medium

### Montage improvements

[[edit](https://www.mediawiki.org/w/index.php?title=Google_Summer_of_Code/2026&action=edit§ion=9)]

Montage is a photo evaluation tool for and by Wiki Loves competitions. It offers a flexible round-based workflow that is configurable to contests of all sizes, and is suited for evaluation of 10-1000s images. For the scope of GSoC, the proposal is to make multiple improvements to improve the workflows, solve existing bugs, and overall improve the experience of users (campaign organizers and jury) using the tool. Source code: [https://github.com/hatnote/montage](https://github.com/hatnote/montage)

- Phabricator:
[T415578](https://phabricator.wikimedia.org/T415578) - Skills required: Frontend: HTML, CSS, Javascript and Vue.js. Backend: Python, Clastic (
[https://python-clastic.readthedocs.io/en/latest/](https://python-clastic.readthedocs.io/en/latest/)) - Mentors:
[KCVelaga](https://phabricator.wikimedia.org/p/KCVelaga/),[Jayprakash12345](https://phabricator.wikimedia.org/p/Jayprakash12345/) - Size: 350 hours
- Difficulty: Medium

### Programs & Events Dashboard system-wide metrics and data downloads

[[edit](https://www.mediawiki.org/w/index.php?title=Google_Summer_of_Code/2026&action=edit§ion=10)]

Develop efficient system-wide metrics and key data download options for Programs & Events Dashboard

- Phabricator:
[T415608](https://phabricator.wikimedia.org/T415608) - Skills required: Ruby (required), JavaScript (helpful)
- Mentors:
[Ragesoss](https://phabricator.wikimedia.org/p/Ragesoss/),[Abishekdascs](https://phabricator.wikimedia.org/p/Abishekdascs/) - Size: 350 hours
- Difficulty: Medium

### Scribe Conjugation Application Development

[[edit](https://www.mediawiki.org/w/index.php?title=Google_Summer_of_Code/2026&action=edit§ion=11)]

The [Scribe](https://github.com/scribe-org) community makes [Wikidata](https://wikidata.org/) based mobile keyboard applications to help second language learners communicate in the languages they're learning. Till now the Scribe community has been working on keyboard applications, namely [Scribe-iOS](https://github.com/scribe-org/Scribe-iOS) and [Scribe-Android](https://github.com/scribe-org/Scribe-Android), along with the infrastructure projects that support them ([Scribe-Data](https://github.com/scribe-org/Scribe-Data) and [Scribe-Server](https://github.com/scribe-org/Scribe-Server)). We'd now like to expand the end user applications that we have on offer to include [Wikidata](https://wikidata.org/) based, multilingual verb conjugation applications. Scribe-Conjugate (see [designs on Figma](https://www.figma.com/design/c8945w2iyoPYVhsqW7vRn6/scribe_public_designs?node-id=1667-2132&t=YSEnQ9eiId51kS9h-1)) for both iOS and Android would provide users with an open-source, open-data and highly performative experience in a new version of a low barrier application that is used by language learners all over the world.

- Phabricator:
[T414862](https://phabricator.wikimedia.org/T414862) - Skills required:
[Kotlin](https://kotlinlang.org/)for Android development,[Swift](https://www.swift.org/)for iOS development - Mentors:
[AndrewTavis](https://phabricator.wikimedia.org/p/AndrewTavis/),[Henrikt93](https://phabricator.wikimedia.org/p/Henrikt93/),[DeleMike](https://phabricator.wikimedia.org/p/DeleMike/) - Size: 350 hours
- Difficulty: Hard

### Wikifile-Transfer Enhancement

[[edit](https://www.mediawiki.org/w/index.php?title=Google_Summer_of_Code/2026&action=edit§ion=12)]

Wikifile-Transfer is a Toolforge web application that helps Wikimedia contributors transfer media files (especially non-free/fair-use images) between different wiki projects. This project aims to enhance the tool by adding batch upload capability, implementing an upload history system, improving metadata extraction with category localization, and adding comprehensive test coverage to ensure code quality and reliability.

- Phabricator:
[T415562](https://phabricator.wikimedia.org/T415562) - Skills required: Python (Flask, SQLAlchemy, Celery), JavaScript/React (functional components, hooks), SQL basics (MySQL), Git version control, Docker, Redis
- Mentors:
[ParasharSarthak](https://phabricator.wikimedia.org/p/ParasharSarthak/),[Jnanaranjan_sahu](https://phabricator.wikimedia.org/p/Jnanaranjan_sahu/) - Size: 350 hours
- Difficulty: Medium

## Recommended steps for accepted candidates

[[edit](https://www.mediawiki.org/w/index.php?title=Google_Summer_of_Code/2026&action=edit§ion=13)]

See [Google Summer of Code/Participants#Accepted participants](/ideas/wikimedia-foundation-nd/participants).

## Contact

[[edit](https://www.mediawiki.org/w/index.php?title=Google_Summer_of_Code/2026&action=edit§ion=14)]

- Support forum:
[https://wikimedia.zulipchat.com/#narrow/channel/561533-GSoC2026](https://wikimedia.zulipchat.com/#narrow/channel/561533-GSoC2026) - Organization administrators for this round are:
[Lani Goto](https://meta.wikimedia.org/wiki/User:LGoto_(WMF)),[Gopa Vasanth](/ideas/wikimedia-foundation-nd/wiki-user-gopavasanth),[Mahfuza Mohona](/ideas/wikimedia-foundation-nd/wiki-user-mhmohona) - Read how to
[communicate effectively](/ideas/wikimedia-foundation-nd/wiki-new_developers-communication_tips)and[get help on technical questions](https://developer.wikimedia.org/get-help/).We encourage applicants to communicate in the public streams and refrain from sending private emails/messages whenever possible. Open communication allows fellow applicants to learn from your questions. It also gives all community members a chance to answer your queries. This way, queries get answered sooner and the administrators do not become a bottleneck. Also see our[communication tips](/ideas/wikimedia-foundation-nd/wiki-new_developers-communication_tips).

## External links

[[edit](https://www.mediawiki.org/w/index.php?title=Google_Summer_of_Code/2026&action=edit§ion=15)]

[GSoC timeline](https://developers.google.com/open-source/gsoc/timeline)- Google Open Source blog
[update](https://opensource.googleblog.com/2025/12/shape-future-with-google-summer-of-code.html)
