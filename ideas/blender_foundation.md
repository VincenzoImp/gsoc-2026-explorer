# Blender Foundation — Project Ideas

**Source:** https://developer.blender.org/docs/programs/gsoc/ideas/
**Scraped:** 2026-02-22T23:28:47.628688

---

# Blender Summer of Code 2026 - Ideas[¶](https://developer.blender.org#blender-summer-of-code-2026-ideas)

This page collects potential ideas and mentors for contributor projects in the summer of 2026.

## Contacting us[¶](https://developer.blender.org#contacting-us)

You can contact us via our [developers
forum](https://devtalk.blender.org/c/contributing-to-blender/summer-of-code/15) or on
[chat.blender.org](https://chat.blender.org/#/room/#gsoc-2026:blender.org).
For matters you prefer to discuss in private, mail Thomas Dinges: thomas
at blender.org.

## General information for contributors and mentors[¶](https://developer.blender.org#general-information-for-contributors-and-mentors)

New to GSoC? Learn [how it works](https://summerofcode.withgoogle.com/how-it-works/) on the GSoC website.

The ideas list below provides ideas for projects that:

- Have an expected project size of ~90, ~175 or ~350 working hours.
- Implements a feature that developers have agreed would be a great improvement for Blender.

Submit your own proposal

Choosing an idea from this list is *not* mandatory. Contributors are
encouraged to submit their own proposals or modified versions of the
ideas from this page. To get an idea of what sort of project can be done for Blender and of
the current development direction, see:

[Code Blog](https://code.blender.org/)- Design and todo tasks listed in the Workboards of
[Blender modules](https://projects.blender.org/) - GSoC projects from previous years:
[2025](/ideas/blender-foundation/2025)-[2024](/ideas/blender-foundation/2024)-[2023](/ideas/blender-foundation/2023)-[2022](/ideas/blender-foundation/2022)-[2021](/ideas/blender-foundation/2021)-[2020](/ideas/blender-foundation/2020)-[2019](/ideas/blender-foundation/2019) [Release Notes](/ideas/blender-foundation/release_notes)

### Mentors[¶](https://developer.blender.org#mentors)

A mentor should be someone with Blender coding experience, who can guide a contributor during all stages of the work, from design to implementation.

### Contributors[¶](https://developer.blender.org#contributors)

Contributors who wish to apply should first carefully read the [Getting
Started page](/ideas/blender-foundation/getting_started) and check if all the
conditions to participate are met.

If by some reason you can not participate, your contribution outside of the program is still welcome! Feel free to develop an idea from the page as long as no contributor chose it.

We especially invite contributors to contribute based on their past experience and competencies, or based on their current research.

Nearly all project ideas will require a strong working knowledge of C and/or C++. In addition, we use Python for much of our interface code (anyone skilled in C/C++ can trivially learn enough Python to make the needed interface code changes). An exception to this are projects where only Python is required.

Get Started

## Ideas[¶](https://developer.blender.org#ideas)

### VFX & Video[¶](https://developer.blender.org#vfx-video)

#### VSE: OpenTimelineIO support[¶](https://developer.blender.org#vse-opentimelineio-support)

*Description:*built-in support for OpenTimelineIO import/export within Blender VSE. Blender Studio has[experimented with it](https://studio.blender.org/blog/opentimelineio-in-blender/)in 2021, by using and extending a 3rd party addon[vse_io](https://gitlab.com/superprod/stax_suite/vse_io). It would be useful to have built-in support for this in order to support VSE interoperability within the broader video editing ecosystem.*Expected outcomes*: Blender VSE can import and export`.otio`

files.*Skills required:*Proficient in C/C++, good familiarity with video editing workflows.*Possible mentors:*[John Kiril Swenson](https://projects.blender.org/eliphaz)*Expected project size:*350 hours*Difficulty:*medium

#### VSE: Mask Editing in VSE Preview[¶](https://developer.blender.org#vse-mask-editing-in-vse-preview)

*Description:*Allow creation and editing of mask datablocks directly inside the VSE preview. Currently, to use masks in the VSE, one must create them from the "Mask" mode in either the Image Editor or the Movie Clip Editor, which is quite hidden and unintuitive. Masks must then be manually applied to strip content with a mask modifier or effect strip. The ability to edit these datablocks directly from the Preview would speed up workflows considerably and align blender's VSE with industry standard video editors.*Expected outcomes*: New circle and square mask tools for the preview that automatically create mask modifiers on the selected strip(s). These should support drag or click to place, along with handles for scaling/rotating/translating.*Skills required:*Proficient in C/C++, familiarity with Blender UI design patterns.*Possible mentors:*[John Kiril Swenson](https://projects.blender.org/eliphaz)*Expected project size:*350 hours*Difficulty:*medium

#### VSE: Strip Transition Gizmo[¶](https://developer.blender.org#vse-strip-transition-gizmo)

*Description:*Allow editing fades/crossfades between neighboring strips with a transition gizmo. Transitions can only be created currently using special effect strips that are automatically lengthened to the gap (or overlap) in time between two strips. This is confusing when strips directly neighbor one another on the same channel, where a 0-length invisible strip is placed between them. Ideally, a user would be able to create fades by rightclicking handles and selecting it from the context menu, adding a transition widget that could be further adjusted. See comments on[issue #150688](https://projects.blender.org/blender/blender/issues/150688)for further discussion and design.*Expected outcomes*: Addition of a transition gizmo on strips that temporarily displays the offsets overlay when editing the fade in/out. Rightclicking the gizmo should change the transition type (wipe/gamma cross). Sound crossfades should also be supported.*Skills required:*Proficient in C/C++, familiarity with UI design patterns.*Possible mentors:*[John Kiril Swenson](https://projects.blender.org/eliphaz)*Expected project size:*350 hours*Difficulty:*medium

#### Compositor: New Nodes from Geometry nodes[¶](https://developer.blender.org#compositor-new-nodes-from-geometry-nodes)

*Description:*Implement compatible nodes from geometry nodes in the compositor. Node editors should be able to reuse the same nodes as much as possible. Recently, many nodes were added in geometry nodes that could also have a use case in the compositor. For example the 'Integer Math' is currently supported in geometry nodes only, but could be supported in the compositor as well. The first part of the project consists of conducting a small servey to decide which nodes should get ported and identify the consequences, e.g. a new socket type must be exposed in the compositor node API etc... The second part of the project consists in implementing the new nodes.*Expected outcomes:*Addition of more nodes in the compositor.*Skills required:*Proficient in C/C++, familiar with node editing in Blender.*Possible mentors:*[Habib Gahbiche](https://projects.blender.org/zazizizou)*Expected project size:*90-175 hours depending on the scope.*Difficulty:*easy

#### Compositor/Image Editor: Improve tools for compositing[¶](https://developer.blender.org#compositorimage-editor-improve-tools-for-compositing)

*Description:*Improve existing tools like Sampling tool or implement new one ones in the image editor. Recently, the default compositing workspace was changed from using the backdrop in the node editor to using a node editor and image editor. The goal of this GSoC project is to improve the image editor with the purpose of improving the compositing workflow. Ideas include:- Improve the Sampling tool by adding a gizmo and a permanent widget to copy-paste values from.
- Implement shortcuts to show R/G/B/A channels in the image editor.
- Implement gizmos for the existing image transforming and resizing operators.

*Expected outcomes:*Improved compositing workflow by implementing gizmos and widgets in the image editor*Skills required:*Proficient in C/C++, familiar with UI design patterns*Possible mentors:*[Habib Gahbiche](https://projects.blender.org/zazizizou)*Expected project size:*175 or 350 hours depending on the scope*Difficulty:*medium

### Modeling[¶](https://developer.blender.org#modeling)

#### Improved Mesh Smoothing[¶](https://developer.blender.org#improved-mesh-smoothing)

*Description:*Possible enhancements include:- Geometry pinning (boundaries/seams/sharp edges).
- Custom-data preserving smooth (smooth without distorting UV's and other custom-data).
- Frequency aware smooth (see the sculpt modes "Mesh Filter").
- Volume preserving smooth (with the possibility of more advanced techniques - e.g. bilateral smoothing).

*Expected outcomes:*Additional smoothing operators for mesh edit-mode.*Skills required:*Proficient in C++, Linear Algebra.*Possible mentors:*[Campbell Barton](https://projects.blender.org/ideasman42)*Expected project size:*350 hours*Difficulty:*medium

#### Improved Edge Loop Editing[¶](https://developer.blender.org#improved-edge-loop-editing)

*Description:*This task involves various enhancements, such as:**Loop Cut at Cursor Location:**Currently Loop Cut snaps to the middle of the face and lets you reposition after confirming. Change the behavior so position can be chosen dynamically before confirming. See[#41446](https://projects.blender.org/blender/blender/issues/41446).**"Clone" Support for Edge Slide:**An option for the Edge Slide tool which, when enabled, duplicates the corresponding edges first and then slides them. See[RCS#2rcbbc](https://blender.community/c/rightclickselect/2rcbbc/),[RCS#QDbbbc](https://blender.community/c/rightclickselect/QDbbbc/).**Edge Flow:**Adjusts the edge loop via spline interpolation such that it respects the flow of the surrounding geometry. See[RCS#vddbbc](https://blender.community/c/rightclickselect/vddbbc/).

*Expected outcomes:*Additional loop-editing operators available in edit-mode.*Skills required:*Proficient in C++, Linear Algebra.*Possible mentors:*[Campbell Barton](https://projects.blender.org/ideasman42),[Tariq Sulley](https://projects.blender.org/Tariq-Sulley)*Expected project size:*350 hours*Difficulty:*hard

#### Improved Face Filling Tools[¶](https://developer.blender.org#improved-face-filling-tools)

*Description:*While Blender has some fill tools (e.g. Grid Fill, Fill Holes), there is room for additional work in this area. Possible additions include:- Adding support for filling areas that do not form a perfect grid, detecting known junction patterns (1-to-3, 2-to-4) automatically.
- Grid Fill support for regions with 5 or more logical sides, with automatic pole insertion (vertices with 5+ edges).
- Creating a higher-level operator that detects the current context and uses the most appropriate fill method.
- Re-filling support to select a region and re-fill it, preserving custom-data such as UVs (already supported for Grid Fill).

*Expected outcomes:*Additional fill operators for mesh edit-mode.*Skills required:*Proficient in C++, Linear Algebra.*Possible mentors:*[Campbell Barton](https://projects.blender.org/ideasman42),[Tariq Sulley](https://projects.blender.org/Tariq-Sulley)*Expected project size:*350 hours*Difficulty:*medium

#### Replace Legacy Curve Evaluation for 3D Text[¶](https://developer.blender.org#replace-legacy-curve-evaluation-for-3d-text)

*Description:*Replace legacy "Curve" based text implementation. Support 3D text objects without using Blender's curve internals.- Besides character tessellation, replacing curve features such as bevel and extrusion with implementations that don't rely on curve data structures.
- This project should use functionality associated with geometry-nodes, to allow geometry-nodes to eventually integrate with 3D text.
- Initial support for geometry-nodes may be possible as part of this project but is not a requirement.

*Expected outcomes:*Efficient text editing that avoids redundant triangulation.*Skills required:*Proficient in C++.*Possible mentors:*[Campbell Barton](https://projects.blender.org/ideasman42)*Expected project size:*350 hours*Difficulty:*medium

### Sculpt, Paint & Texture[¶](https://developer.blender.org#sculpt-paint-texture)

#### General Brush Engine Improvements[¶](https://developer.blender.org#general-brush-engine-improvements)

*Description:*There are many features of the sculpt brushes that can be generalized across the available brushes so that further user customization is possible. Some potential areas to tackle are as follows:- Per-brush "opt-in" for scene-level brush settings settings
- Brush tip roundness (already available as part of Clay Strips Brush)
- Customizable pressure curves for all pressure-sensitive parameters
- Tablet tilt support (already available for a number of brushes)
- Customizable brush toggle ability & improved toggle display
- "Grab" brush anchored improvements to improve first stroke responsiveness and pressure sensitivity

*Expected outcomes:*More consistent and generic settings to improve feel of current brushes.*Skills required:*Proficient in C++, Linear Algebra*Possible mentors:*[Sean Kim](https://projects.blender.org/Sean-Kim)*Expected project size:*175 ~ 350 hours*Difficulty:*medium

### User Interface[¶](https://developer.blender.org#user-interface)

#### Improving Regression Test Coverage[¶](https://developer.blender.org#improving-regression-test-coverage)

*Description:*While there is support for testing the UI through event simulation, test coverage is low so far. A lot more parts of the UI could be covered to prevent/catch regressions, see[151680](https://projects.blender.org/blender/blender/issues/151680). Other ways to cover the Blender UI and the UI system with tests could be developed too (which might require some C++ knowledge, depending on the approach).*Expected outcomes:*Significant amount of new tests covering various features of the Blender UI. Potentially: New ways to test the UI.*Skills required:*Proficient in Python*Possible mentors:*[Julian Eisel](https://projects.blender.org/JulianEisel)*Expected project size:*90*Difficulty:*easy
