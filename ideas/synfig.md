# Synfig — Project Ideas

**Source:** https://github.com/synfig/synfig-docs-dev/blob/master/docs/gsoc/2026/ideas.rst
**Scraped:** 2026-02-22T23:28:47.628577

---

.. _ideas:

Ideas List
=====================


This year we plan to apply to Google Summer of Code. Currently we are looking for project ideas. If you are a contributor, you are welcome to explore existing project ideas towards the GSoC application phase. There are ways to reach out to mentors, and many projects have lists of newcomer friendly issues you can start from. Contributors are also welcome to propose their own project ideas.

Projects Ideas
--------------

Synfig Android Version (350hrs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:**
This project aims at providing a solid ground for a Synfig Android version. It aims to do so through two main parts.

1- Prototype UI (Using Qt for android) that uses synfigapp and -in turn- synfig-core

There are two main goals here:
1. To have a basic android UI for synfig working. 
2. While making this prototype certain parts of the synfig api would be fixed. Which would make SynfigApp and Synfig-Core able to be used with any other UI not just the current gtkmm UI (synfig-studio).

2- Add more features to the UI
Synfig is quite a huge application. Most likely this app would start with only very basic needed synfig features added. Then gradually adding more features from synfig-studio to the new prototype UI.

**Where to begin:**

1. Start out by understanding and gathering the basic features for animation in synfig. In your proposal include these features and expand on how you plan to include them. 
2. Research the available mobile/tablet animation apps and prototype a ui design using any ui design software (e.g. canva). This is not required but it will definetly help your proposal.


**Expected outcome**

- Prototype Synfig Android Version
- Improved synfig-app and (possibly) synfig-core that can work with any other UI.

**Difficulty:** Medium/High

**Skills required/preferred:** C++, gtkmm, Qt, using Qt for Android

**Possible mentor(s):** `Mohamed Adham <https://github.com/mohamedAdhamc>`_ , `Rodolfo Ribeiro <https://github.com/rodolforg>`_

**Expected size of project:** 350 hours

Exporter to Spine file format (175hrs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:**

The goal of this project is to implement a feature in Synfig Studio that enables exporting skeleton-based animations to the Spine file format.
This would allow users to seamlessly transfer their Synfig animations, those created using bone-based rigs and skeleton systems, to Spine for additional refinement or game engine integration.
This would involve creating an export function in Synfig that outputs the necessary JSON or binary format that Spine can read.
The project will ensure that all essential animation data, such as bone movements, and keyframe timing, are accurately preserved during the export.
Thus, users can leverage Synfig's powerful animation tools while taking advantage of Spine's advanced features, such as runtime support in various game engines.

**Where to begin:**

1. Check Synfig skeleton layer code
2. Check Spine JSON format (https://en.esotericsoftware.com/spine-json-format)
3. Try to add new menu option "Export to Spine format" to Skeleton layer, which should create basic Spine JSON file.

**Expected outcome**

* A fully functional export tool in Synfig Studio capable of converting skeleton-based animations into the Spine file format.

* The exported Spine file should retain all key elements of the animation, including bones, mesh deformation, and animation keyframes.

* The ability to open and refine the exported Spine animation in Spine's editor or integrate it directly into a game engine.

* Plus: Import Spine file to Synfig :)

**Difficulty:** Medium

**Skills required/preferred:** Python (or C++), XML and JSON, understanding of Synfig's animation system, especially skeleton-based animation and bone rigs, and Synfig file format.

**Possible mentor(s):** `Rodolfo Ribeiro <https://github.com/rodolforg>`_ , `Mohamed Adham <https://github.com/mohamedAdhamc>`_

**Expected size of project:** 175 hours


New audio backend (175h)
~~~~~~~~~~~~~~~~~~~~~~~~

**Description:**

Currently we use MLT++ as our audio playback framework, but we do not use none of its features but simple audio mixing (volume and delay).
The intention here is to replace it with its own backend: SDL (SDL_audio, specifically) in both versions: the classic SDL2 and the new SDL3.

**Where to begin:**

1. Check how to play audio from file with SDL2 AND SDL3.
2. Take a look how we use audio in SoundProcessor class.
3. Try to allow our both building systems to select what audio backend we want: none, MLT++, SDL2 or SDL3.

**Expected outcome:**

* Remove MLT++ dependency;

* Be able to reproduce audios in SynfigStudio, but via SDL2 or SDL3 (choose in building/compilation time)

* Be able to export video+audio via ffmpeg target, but via SDL2 or SDL3 (choose done in building/compilation time)

**Dificulty:** Medium

**Skills required/preferred:** C++, SDL2/SDL3 audio playback

**Possible mentor(s):** `Rodolfo Ribeiro <https://github.com/rodolforg>`_ , `Mohamed Adham <https://github.com/mohamedAdhamc>`_

**Expected size of project:** 175 hours

2D Free-Form Deform (175h)
~~~~~~~~~~~~~~~~~~~~~~~~

**Description:**

Allow artist to set up a grid and animate by deforming on moving this lattice points.

**Where to begin:**

1. Check Skeleton Deformation layer works

2. Check how handles work (duckmatic class)

**Expected outcome:**

* A new deformation layer by grid, not by bones.

* Visual control points to deform.

**Dificulty:** Medium

**Skills required/preferred:** C++.

**Possible mentor(s):** `Rodolfo Ribeiro <https://github.com/rodolforg>`_ , `Mohamed Adham <https://github.com/mohamedAdhamc>`_

**Expected size of project:** 175 hours


Propose a Project
------------------
If you have a project idea, edit the "Project Ideas" section below by filling the required details and sending a pull request (this page is editable at  https://github.com/synfig/synfig-docs-dev/blob/master/docs/gsoc/2025/ideas.rst), even if you could not mentor (we will find a mentor).

**Required information for project proposal**

::

    A descriptive title (175 or 350 hrs)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    **Description**

    A brief description about the project

    **Expected outcome**

    What benefit this deliver?

    **Difficulty** Easy | Medium | High

    **Skills required/preferred:** Knowledge Prerequisite

    **Possible mentor(s):** Put your name if you are willing to mentor + other mentors.

    **Expected size of project:** 90, 175 or 350 hours

*Please mention the following as comment on your proposal pr*

:Your name: :)
:Your profile: github | linkedin | etc
:Your role: I am a making this proposal as a <student | mentor | community member | contributor | etc>

Contacts
--------

https://www.synfig.org/contact/
