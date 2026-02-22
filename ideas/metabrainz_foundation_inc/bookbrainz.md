# ideas page

**Parent:** MetaBrainz Foundation Inc — Project Ideas
**Source:** https://wiki.musicbrainz.org/Development/Summer_of_Code/2026/BookBrainz
**Scraped:** 2026-02-22T23:28:47.630196

---

# Development/Summer of Code/2026/BookBrainz

BookBrainz is a database of book metadata. [Try it out.](https://bookbrainz.org/)

## Getting Started

(see also: [Getting started with GSoC](https://wiki.musicbrainz.org/Development/Summer_of_Code/Getting_started))

The first thing to do to get started with BookBrainz is to get familiar with the website, and start editing. The help page and user guide are good starting points.

We also have a testing website at test.bookbrainz.org, with its own separate database. You can create an account there and use it to get familiar with the website and database.

The next step is to clone the [bookbrainz-site](https://github.com/metabrainz/bookbrainz-site) GitHub repository, and follow our [developer documentation](https://bookbrainz-dev-docs.readthedocs.io/en/latest/) to get the site up and running on your computer.

When you feel ready to try your hand on some bugs, we have a [“good first bug”](https://tickets.metabrainz.org/issues/?filter=11910) category on our ticket tracker.

Come and speak to us in the BookBrainz [IRC](https://wiki.musicbrainz.org/IRC) (Libera.Chat/#bookbrainz) if you finish all of that, or get stuck!

## Ideas

A list of suggestions to help applicants to develop proposals for Google's Summer of Code, for BookBrainz. You are not limited to these ideas - if you use BookBrainz and find an area that needs improvement, you can propose your own.

## Use Solr search server

**Proposed Mentors:** monkey, lucifer

**Languages/skills:** Solr search, Typescript

**Estimated Project Length:** 350 hours

**Difficulty:** hard

Expected outcomes: A functional multi-entity search server with the same features as the existing search functionality

Other MetaBrainz projects use Solr search server, while BookBrainz was created using ElasticSearch and has not evolved since. This creates some extra overhead by running two separate search infrastructures and prevents us from optimizing resources.

For this project, you would entirely replace the search server infrastructure and adapt the existing search to work with Solr. This makes for a project relatively isolated from the rest of the website, the only surface of contact being [this file](https://github.com/metabrainz/bookbrainz-site/blob/master/src/common/helpers/search.ts) handling most of the indexing and ElasticSearch-specific logic, and [this file](https://github.com/metabrainz/bookbrainz-site/blob/master/src/server/routes/search.tsx) which adds the website routes that allows users and the website to interact with the search server.

One relevant point of detail is that we want to maintain multi-entity search (search for authors, works, edition, etc all in one go) compared to the MusicBrainz search for example which requires selecting an entity type before performing a search. This would need to be investigated.

## Set up BookBrainz for internationalization

**Proposed Mentors:** monkey

**Languages/skills:** Javascript/Typescript

**Estimated Project Length:** 175 hours

**Difficulty:** easy

**Expected outcomes:** Full translation project and workflow set up, with as much as possible of the website text captured for translation

BookBrainz is currently only in english language, which stops us from reaching a wider audience.

Thankfully, the MusicBrainz team has had a long experience with internationalization and recently moved to using Weblate.

You can see this translation server here: [https://translations.metabrainz.org/](https://translations.metabrainz.org/) and more general documentation here: [https://musicbrainz.org/doc/Internationalization](https://musicbrainz.org/doc/Internationalization)

For this project, you would help set up a new translation project on the same Weblate server, and integrate Weblate into BookBrainz.

You will need to evaluate the best options for how to implement this in BookBrainz.

Promising frameworks with React support include (but not limited to) [Fluent](https://projectfluent.org/) and [i18next](https://www.i18next.com/)

## New Calibre plugin

**Proposed Mentors:** monkey

**Languages/skills:** python

**Estimated Project Length:** 175/350 hours depending on proposed features

**Difficulty:** medium

**Expected outcomes:** An installable Calibre plugin with basic features, allowing searching for editions by name and author, and improving metadata of e-book files

[Calibre](https://calibre-ebook.com/about) is an established open source e-book library manager.

There was once a BookBrainz plugin for Calibre ([CaliBBre](https://github.com/bookbrainz/CaliBBre)) which has since been abandoned.

This project would see the revival of this plugin, rewritten from scratch considering the code is 8-9 years old.

See plugin development documentation here: [https://manual.calibre-ebook.com/creating_plugins.html](https://manual.calibre-ebook.com/creating_plugins.html)

Some experience using Calibre and e-books is required for this project.

Optional goals: sync collections between Calibre and BookBrainz
