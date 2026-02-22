# TracWiki

**Parent:** Django Software Foundation — Project Ideas
**Source:** https://code.djangoproject.com/wiki/TracWiki
**Scraped:** 2026-02-22T23:28:47.630924

---

# The Trac Wiki System


#### Table of Contents


Trac has a built-in wiki system which you can use for organizing knowledge and information in a very flexible way by [creating pages](https://code.djangoproject.com/wiki/WikiNewPage) containing an intuitive and easy to learn textual markup. The wiki markup is used throughout Trac, so not only in [wiki pages](https://code.djangoproject.com/wiki/TitleIndex), but also in [ticket](https://code.djangoproject.com/wiki/TracTickets) description and comments, [version control](https://code.djangoproject.com/wiki/TracChangeset) log messages, [milestone](https://code.djangoproject.com/wiki/TracRoadmap) descriptions, [report](https://code.djangoproject.com/wiki/TracReports) descriptions and even in third-party extensions.
It allows for formatted text and hyperlinks in and between all Trac modules.

Editing wiki text is easy, as compared to complex markup languages like HTML, using any web browser and simple [formatting](https://code.djangoproject.com/wiki/WikiFormatting). The motivation for wiki markup is that HTML, with its large collection of nestable tags, is too complicated to allow fast-paced editing, and distracts from the actual content of the pages. Note that Trac also supports [HTML](https://code.djangoproject.com/wiki/WikiHtml), [reStructuredText](https://code.djangoproject.com/wiki/WikiRestructuredText) and [Textile](https://txstyle.org) as alternative markup formats, which can be used in parts of a page, so called wiki blocks.

The main goal of the wiki is to make editing text easy in order to *encourage* people to contribute to a project. Trac also provides a simple toolbar to make formatting text even easier, and supports the [universal edit button](http://universaleditbutton.org/Universal_Edit_Button) of your browser.

The wiki itself does not enforce any structure, but rather resembles a stack of empty sheets of paper, where you can organize information and documentation as you see fit, and later reorganize if necessary.
As contributing to a wiki is essentially building hypertext, general advice regarding HTML authoring apply here as well.
For example, the * Style Guide for online hypertext* explains how to think about the

[overall structure of a work](https://www.w3.org/Provider/Style/Structure.html)and how to organize information

[within each document](https://www.w3.org/Provider/Style/WithinDocument.html). One of the most important tips is to "make your HTML page such that you can read it, even if you don't follow any links".

Learn more about:

[WikiFormatting](https://code.djangoproject.com/wiki/WikiFormatting)rules, including advanced topics like[WikiMacros](https://code.djangoproject.com/wiki/WikiMacros)and[WikiProcessors](https://code.djangoproject.com/wiki/WikiProcessors).- How to use
[WikiPageNames](https://code.djangoproject.com/wiki/WikiPageNames)and other forms of[TracLinks](https://code.djangoproject.com/wiki/TracLinks)which are used to refer to any resource within Trac.

If you want to practice editing, please use the [SandBox](https://code.djangoproject.com/wiki/SandBox). Note that not all Trac wiki pages are editable by anyone, this depends on the local policy; check with your Trac administrators.

Before saving your changes, you can *Preview* the page or *Review Changes* you have made.
You can get an automatic preview of the formatting as you type when you activate the *Edit Side-by-side* mode. There is a [configurable delay](https://code.djangoproject.com/wiki/TracIni#/auto_preview_timeout) between when you make your edit and when the automatic preview will update.

Some more information about wikis on the web:

- A definition of
[Wiki](https://wikipedia.org/wiki/Wiki)according to Wikipedia. - The
[history](http://c2.com/cgi/wiki?WikiHistory)behind the original wiki. - A wiki page explaining
[why wiki works](http://www.usemod.com/cgi-bin/mb.pl?WhyWikiWorks).

See also: [TracGuide](https://code.djangoproject.com/wiki/TracGuide)

[Last modified](https://code.djangoproject.com/wiki/TracWiki?action=diff&version=6)

[2 years ago](https://code.djangoproject.com/timeline?from=2024-01-24T09%3A58%3A09-06%3A00&precision=second)Last modified on Jan 24, 2024, 9:58:09 AM

**Note:**See

[TracWiki](https://code.djangoproject.com/wiki/TracWiki)for help on using the wiki.
