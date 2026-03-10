# Tiled — Project Ideas

**Source:** https://github.com/mapeditor/tiled/wiki/GSoC-2026#project-ideas
**Scraped:** 2026-03-10T16:58:40.244550

---

# Google Summer of Code 2026
Tiled has been accepted as mentoring organization in the [Google Summer of Code](https://summerofcode.withgoogle.com/how-it-works) 2026! 

This page contains the list of projects we'd suggest, but we're also open to other proposals! Applications will be open from 16th - 31st of March.

> **Our policy on AI:** In your own best interest we ask you not to use AI to write your code. You will learn much better when you do it yourself and we'd much rather deal with your human mistakes than to point out the mistakes the AI has made for you. Thank you!

### Contents

* [Project Ideas](#project-ideas)
    * [New Hardware Renderer](#new-hardware-renderer)
    * [Enhanced World Editing](#enhanced-world-editing)
    * [glTF Export for Maps](#gltf-export-for-maps)
    * [Next-generation Tiled Extensions](#next-generation-tiled-extensions)
    * [New Cross-platform Style](#new-cross-platform-style)
* [Application Process](#application-process)
* [Organization](#organization)

# Project Ideas

We are open to your ideas! If you have your own ideas for improving Tiled, you are more than welcome to send them. Below are listed our suggestions, representing large areas of improvement.

## New Hardware Renderer

Modernize the rendering engine to use the [Qt Scene Graph](https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html) instead of [`QPainter`](https://doc.qt.io/qt-6/qpainter.html). This would also enable using declarative UI for describing the map view.

**Expected outcome:** Tiled performs better and is more flexible thanks to a new renderer based on a modern graphics API.\
**Required skills:** Qt, C++ (preferred: Qt Quick, experience with modern graphics APIs)\
**Possible mentors:** bjorn\
**Expected size:** 350 hours\
**Difficulty:** Medium

Full project description: [New Hardware Renderer](/ideas/tiled/new-hardware-renderer)

## Enhanced World Editing

Tiled 1.2 added displaying multiple maps within the same view by [setting up a World](https://doc.mapeditor.org/en/stable/manual/worlds/). Since Tiled 1.4, a basic "World Tool" was added, which enabled [basic editing of the world](https://doc.mapeditor.org/en/stable/manual/worlds/#editing-worlds). This project is about making several improvements to the world editing functionality.

**Expected outcome:** Worlds are a natural and convenient part of creating game content with Tiled.\
**Required skills:** C++ (preferred: Qt)\
**Possible mentors:** bjorn, dogboydog\
**Expected size:** 350 hours (or 175 hours, by selecting a sub-set of listed improvements)\
**Difficulty:** Medium

Full project description: [Enhanced World Editing](/ideas/tiled/enhanced-world-editing)

## glTF Export for Maps

Implement a glTF export feature for maps, allowing them to be quickly imported for use in other frameworks without that framework needing to implement support for all of Tiled's features.

**Expected outcome:** Maps can be exported in glTF format as a quick way of rendering them in multiple frameworks.\
**Required skills:** C++ or JavaScript (preferred: glTF)\
**Possible mentors:** bjorn, dogboydog\
**Expected size:** 350 hours (or 175 hours, for somebody who already knows glTF very well)\
**Difficulty:** Medium

Rendering a Tiled map generally consists of determining the texture coordinates for each tile and setting up a mesh for each layer and tileset. At each step, a host of Tiled-specific properties and behaviors have to be taken into account, from tileset margin and spacing to  map orientation and tile alignment.

With the growing support for glTF in many engines and frameworks, all this application-specific logic could be performed ahead of time, greatly simplifying the importing of a Tiled map in a game. Hence, this project is about writing a Tiled plugin, preferably in C++ but could also be done in JavaScript, to enable exporting a map, or an entire world, to the glTF format.

Special considerations include how to handle tile animations, logic-related layers and in general dynamic changes to the glTF scene when used in a game. In addition, for optimal rendering performance we'll probably want to look into texture packing and creating an optimized tileset.

Related issue: [#2741](/ideas/tiled/mapeditor-tiled-issues-2741)

## Next-generation Tiled Extensions

> _This project is currently being worked on as part of [Winter of Code](https://winter-of-code.tech/) 5.0, but there will likely be plenty of work remaining._

Tiled can be extended by using JavaScript, using either plain .js files or JavaScript modules (.mjs). However, Qt provides [QML](https://doc.qt.io/qt-6/qmlapplications.html), a powerful declarative language. It would be great if we could use it to declare custom actions, file formats, tools, etc. Additionally, we could ship the necessary QML modules to enable extensions to implement custom UI.

**Expected outcome:** Tiled extensions can be written in a convenient declarative language and can define custom UI.\
**Required skills:** Qt, C++ (preferred: JavaScript, Qt Quick)\
**Possible mentors:** bjorn, dogboydog\
**Expected size:** 175 hours when excluding UI work, or 350 hours for the full project\
**Difficulty:** Medium

[Read more...](/ideas/tiled/next-generation-tiled-extensions)

## New Cross-platform Style

Tiled currently ships with "Tiled Fusion", a cross-platform style introduced in [Tiled 0.17](https://discourse.mapeditor.org/t/tiled-0-17-0-released/1574). While it has served us well, it is showing its age. This project is about creating and polishing a modern replacement style with improved readability, consistent spacing, and better configurability across platforms.

**Expected outcome:** Tiled ships with a modern, polished, and configurable cross-platform style that improves readability and usability on Windows, Linux, and macOS.\
**Required skills:** Qt, C++ (preferred: Qt Widgets styling, visual design sense)\
**Possible mentors:** bjorn\
**Expected size:** 175 hours (or 350 hours, depending on scope and amount of widget coverage)\
**Difficulty:** Medium

Scope can include completing and refining styling for core controls (buttons, tabs, menus, sliders, combo boxes, checkboxes/radio buttons, dock widgets, line edits, scroll bars), validating behavior in both light and dark themes, and ensuring the style works as intended on all supported platforms. A successful proposal should also include a plan for visual regression checks (screenshots) and iterative UX feedback.

Finally, this project could include a refresh of the icon theme, based for example on open source icons from https://lucide.dev/.

A small start has already been made on a new style in the this pull request: [A new cross-platform style #3597](https://github.com/mapeditor/tiled/pull/3597)


# Application Process

If you are interested in any of our projects and looking forward to join us in improving Tiled further, follow the below guidelines to apply.

* Sign-up in our [forum](http://discourse.mapeditor.org/) and [introduce yourself](https://discourse.mapeditor.org/t/google-summer-of-code-2026/7732).

* Tell us in which project you are interested.

* Tell us a little bit about yourself. We are interested to hear:
    - Why you would like to work with us.
    - What previous programming experience you have.
    - What projects you have worked on before (and which languages and technology you used for them).
    - Whether you worked in a team or alone.
    - Whether you have done any contribution to any open source project before.
    - Whether you have any prior experience with C++ and Qt.
    - What project(s) you have in a public repository that we could can take a look at.

  (_None of the above information is mandatory, but the better our impression is the more confident we will be that you can succeed in your proposal. If you have a personal website or a CV/resume online, feel free to include a link._)

* Try to find at least two small things to improve about Tiled. Feel free to browse the [open issues](/ideas/tiled/mapeditor-tiled-issues) for inspiration. Show us you can set up your development environment and know how to contribute a change. Don't be shy to ask for help!

* **Do not use AI to write your proposal!** Be sure you understand in depth what your project is about and show it off with a thoughtful document that has "done by a human" written all over it.

* Submit your proposal during the application period (March 16-31, but don't wait till the last moment!)

Note that we're not just looking at your skills! What we're looking for are people who:

* are motivated by personal interest rather then money,
* see value in releasing their work as free software and welcoming others to contribute,
* will think things through rather than just following instructions,
* and who are critical of their own work and perfecting it before waiting for feedback.

Please also understand that we are a relatively small team that will only be able to accommodate a few projects.

# Organization

Since Tiled's [first release](https://www.mapeditor.org/2004/06/15/tiled-030-released.html) back in 2004, it was intended to be a tile map editor generic enough to be useful for many kinds of games. Today it is used by thousands of game developers every day, because it is a free and powerful editor, independent of the engine or technology they use to develop their game.

The Tiled organization is committed to maintaining this editor and also helping others contribute any improvements they need. Tiled is also a perfect project for new developers learn the benefits of free software and get to know the related technology (Qt, C++).

### Mentors

The following people are available as mentors for this year's Google Summer of Code:

- [bjorn](http://discourse.mapeditor.org/u/bjorn)
- [dogboydog](http://discourse.mapeditor.org/u/dogboydog)
