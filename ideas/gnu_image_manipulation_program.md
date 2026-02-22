# GNU Image Manipulation Program — Project Ideas

**Source:** https://developer.gimp.org/core/internship/ideas/
**Scraped:** 2026-02-22T23:28:47.565468

---

# Project ideas for internship programs

This page is shared for events such as Google Summer of Code or similar
internship programs which GIMP might participate in, as a list of project ideas
for participants.
You may choose to implement exactly one of the proposed ideas, propose new ideas
inspired from this list, or suggest completely new projects (which is perfectly
fine if your proposition makes sense). Our
[roadmaps](/ideas/gnu-image-manipulation-program/core-roadmap) may also be a good source
of inspiration.

You will be selected on the quality of the proposal and on your attitude within the context of a Free Software Community. Also we prefer smaller projects which end up in our main codebase, rather than over-ambitious projects which you won’t have time to finish and might end bitrotting for years.

Please also read the [main page on internship programs with
GIMP](/ideas/gnu-image-manipulation-program/core-internship). You will want to make sure you follow the
basic requirements (such as having good communication, not using any AI
tools…) to have your project accepted and not failing.

##
[Implement a Shape Tool
](https://developer.gimp.org#implement-a-shape-tool)

- Category
- Tools, Core
- Project size (GSoC)
- Large (350 hours)
- Skills
- C, GTK
- Possible mentors
- Jehan, CmykStudent
- Difficulty
- Intermediate
- Outcome
- Initial implementation of a Shape tool

A long running request for GIMP has been to have a simple Shape tool.
While we have had the [GFig filter](https://docs.gimp.org/3.0/en/plug-in-gfig.html),
it has several drawbacks and limitations. With the implementation of vector layers
in GIMP 3.2, we now have the backend to implement a vector Shape tool.

People interested in this project can begin by reading the
[history of the issue report](https://gitlab.gnome.org/Teams/GIMP/Design/gimp-ux/-/issues/715),
with special attention to [recent comments](https://gitlab.gnome.org/Teams/GIMP/Design/gimp-ux/-/issues/715#note_2586018).
Current ideas are to either build an entirely separate tool or to modify the existing Path tool
to have shape presets - though you are always welcome to suggest your own ideas!

This is a project involving UX considerations, so you would
be expected to work with our community of designers on the `gimp-ux`

tracker, and experiment with various implementations via back-and-forth
testing.

##
[New Shortcuts Editing Dialog
](https://developer.gimp.org#new-shortcuts-editing-dialog)

- Category
- User Interface, Core
- Project size (GSoC)
- Large (350 hours)
- Skills
- C, GTK
- Possible mentors
- Jehan, CmykStudent, Aryeom
- Difficulty
- Intermediate
- Outcome
- replacement of exiting GUI in GIMP codebase

GIMP has a dialog to edit your shortcuts. It is globally working but has issues:

- It is based on
`GtkTreeView`

which is deprecated in GTK4. - It does not allow assigning several shortcuts for a single action (which is a new core feature of GIMP 3, except we don’t have a proper GUI to allow creators make their own multiple shortcuts).
- Many things are confusing in this dialog.
- The search is quite basic and not always so useful.
- Etc.

This is a project involving quite some UX considerations, so you would
be expected to work with our community of designers on the `gimp-ux`

tracker, and experiments various implementations with back-and-forth
testing.

##
[Improve Text-along-a-Path features
](https://developer.gimp.org#improve-text-along-a-path-features)

- Category
- Text, User Interface, Core, tools
- Project size (GSoC)
- Large (350 hours)
- Skills
- C, GTK, GEGL
- Possible mentors
- Liam, Jehan, CmykStudent
- Difficulty
- Intermediate
- Outcome
- implementation of the updated feature in GIMP codebase

GIMP supports bending and shaping text layers along user defined paths.
However, this is currently a destructive process with a number of limitations.
We would like to improve the user experience for this feature and add more
nice, modern abilities to it
([such as non-destructive editing](https://gitlab.gnome.org/GNOME/gimp/-/issues/136))

For a successful project, you will need to do the following:

- Study the current implementation as well as implementations in other software
- Propose a project scope with milestones
- Collaborate with our community and UX designers to test out differnt interactions
- Implement an initial version in our codebase

##
[New UI to quickly list, search and preview filters
](https://developer.gimp.org#new-ui-to-quickly-list-search-and-preview-filters)

- Category
- User Interface, Core, Tools, GEGL
- Project size (GSoC)
- Large (350 hours)
- Skills
- C, GTK, GEGL
- Possible mentors
- Jehan, CmykStudent, Aryeom
- Difficulty
- Intermediate
- Outcome
- implementation of the tool in GIMP codebase

Non-destructive filters can currently be started from menus (mixed with all sorts of other items, which may not be filters), or from the action search. Some people have discussed the idea of a more centralized interface where filters usable non-destructively could be listed, show some kind of preview of the filter (though it could just be pre-rendered images showing a typical use case). This would more likely be implemented as a dockable dialog.

Additional features which would make sense would include categorization, proper tagging, search by keyword, etc.

Such project would require a lot of UX discussions with our designers and various people on our tracker, back and forth implementations for testing and so on.

Relevant UX report: [https://gitlab.gnome.org/Teams/GIMP/Design/gimp-ux/-/issues/106](https://gitlab.gnome.org/Teams/GIMP/Design/gimp-ux/-/issues/106)

##
[Better math expressions UI/UX
](https://developer.gimp.org#better-math-expressions-uiux)

- Category
- User Interface, Core
- Project size (GSoC)
- Small (90 hours)
- Skills
- C, GTK
- Possible mentors
- Aryeom, Jehan, CmykStudent
- Difficulty
- Intermediate
- Outcome
- make maths expressions feature more discoverable and usable

Some widgets in GIMP have the ability to process math operations in
their input fields. For instance, in the “Create a New Image” dialog,
you could write `1920*2`

in “Width” field and it would be transformed to
`3840`

. The mathematics parser code currently resides in
`libgimpwidgets/gimpeevl.[ch]`

.

Though very powerful, the feature could be made more discoverable, understandable and why not even more powerful!

Reference UX discussions:

[https://gitlab.gnome.org/Teams/GIMP/Design/gimp-ux/-/issues/476](https://gitlab.gnome.org/Teams/GIMP/Design/gimp-ux/-/issues/476)[https://gitlab.gnome.org/Teams/Design/whiteboards/-/issues/328](https://gitlab.gnome.org/Teams/Design/whiteboards/-/issues/328)

You would work with our community of designers to implement a visual interface for the feature. This could mean implementing several versions for wider testing and decision.

The end implementation would be cleanly contained in code which could be easily reused in several widgets, if needed. You would then research the various widgets where this would be useful, as well as the various fields where it would be worth enabling.

It could be interesting to also contribute this to upstream GTK.

If time allows, the internal feature could also be improved where needed.

##
[Implement In-Painting Tool
](https://developer.gimp.org#implement-in-painting-tool)

- Category
- User Interface, Core, Tools, GEGL
- Project size (GSoC)
- Large (350 hours)
- Skills
- C
- Possible mentors
- Jehan, CmykStudent
- Difficulty
- Intermediate
- Outcome
- implementation of the tool in GIMP codebase

GIMP has had support for in-painting (filling in an area based on the
surrounding image) for many years with the third-party
[Resythesizer plug-in](https://github.com/bootchk/resynthesizer).
There have been many requests to implement the feature as a tool directly in
core GIMP. In addition to this algorithm, there is also the GEGL operation
[alpha-inpaint](https://gitlab.gnome.org/GNOME/gegl/-/blob/master/operations/workshop/alpha-inpaint.c)
which works similarly.

Relevant discussions that would assist with implementing this feature can be found
[here](https://gitlab.gnome.org/GNOME/gimp/-/issues/8692) and
[here](https://gitlab.gnome.org/GNOME/gimp/-/issues/4762).

- Study the Resynthesizer plug-in,
`gegl:alpha-inpaint`

operation, and other implementations - Design a potential implementation and UI
- Improve the implementation of the algorithms as needed
- Implement the tool

##
[Image Segmentation Improvements
](https://developer.gimp.org#image-segmentation-improvements)

- Category
- Core, Tools
- Project size (GSoC)
- Large (350 hours)
- Skills
- C
- Possible mentors
- Jehan, CmykStudent
- Difficulty
- Intermediate
- Outcome
- New and/or improved algorithms for selecting parts of images

GIMP has many different tools and algorithms for selecting specific sections of an image - from the standard Rectangle and Ellipse Select tools to the more advanced Paint Select and Foreground Select tools. Yet there are always new algorithms and methods for segmenting images.

- Find an existing algorithm or propose a new one
- Implement, optimize and test for real image processing work on a variety of images
- Design how it should be used in GIMP
- An additional mode in an existing tool
- A new tool entirely


##
[Update Windows Scanner and Printer API
](https://developer.gimp.org#update-windows-scanner-and-printer-api)

- Category
- Plug-ins
- Project size (GSoC)
- Large (350 hours)
- Skills
- C
- Possible mentors
- Jacob, CmykStudent
- Difficulty
- Intermediate
- Outcome
- Updated Scanner and Printer features on modern Windows platforms

GIMP is a cross-platform program that supports Linux, macOS, and Windows. In some cases, we have to add platform-specific code to access system features like printing and scanning. Currently, our Windows integration for these are out of date:

-
Our Windows scanner plug-in uses

[32-bit TWAIN rather than WIA API](https://gitlab.gnome.org/GNOME/gimp/-/issues/10930), and soon will no longer be supported on modern 64-bit systems. -
The Printer API for Windows 11 is different than earlier versions, and our printer plug-in currently has

[missing features on that OS](https://gitlab.gnome.org/GNOME/gimp/-/issues/7299).

A successful project to update these plug-ins would include:

- Study the current implementation and the newer APIs
- Design any new UI components required by the API update
- Implement and test the updated plug-ins for printing and/or scanning

##
[Improving unit testing
](https://developer.gimp.org#improving-unit-testing)

- Category
- Unit testing
- Project size (GSoC)
- Large (350 hours)
- Skills
- C
- Possible mentors
- Jehan, Jacob
- Difficulty
- Intermediate
- Outcome
- Improved unit testing infrastructure and new unit tests

Currently GIMP unit testing framework is really outdated, adding new tests is complex and therefore never happens. We should specify and code a proper framework for testing GIMP features.

This implies automated tests we can run in our Continuous Integration in Gitlab and not interactive tools (though such tools can be interesting too, as additional process, if someone has something nice to propose).

- Port existing tests to the new framework;
- Testing all libgimp functions;
- Testing GEGL operations implemented within GIMP codebase;
- Testing plug-ins (in priority the file import/export ones, but not only);
- Testing core code;
- Testing GUI code if possible;
- Writing down the procedure to add unit tests to make it a mandatory process in future development.

##
[Fuzz testing integration
](https://developer.gimp.org#fuzz-testing-integration)

- Category
- Unit testing, Security
- Project size (GSoC)
- Large (350 hours)
- Skills
- C
- Possible mentors
- Jehan, Jacob
- Difficulty
- Intermediate

In addition to unit testing, we would also like to build a robust automated fuzz testing suite. Integrating a fuzzer would help us better detect when new code could lead to a security vulnerability or incorrect behavior in GIMP. This project would cover many aspects of GIMP, from core code to plug-ins to public API.

- Study GIMP and determine what areas to cover in initial implementation
- Review fuzzing techniques and tools
- Design a test suite and process
- Implement fuzz testing suite

##
[Implement sandboxing for plug-ins
](https://developer.gimp.org#implement-sandboxing-for-plug-ins)

- Category
- Security, Plug-ins
- Project size (GSoC)
- Large (350 hours)
- Skills
- C
- Possible mentors
- Jehan, Jacob
- Difficulty
- Complicated

Many features of GIMP such as image import and export are implemented with separate plug-ins. For this project, we would like to run them in a sandbox environment for safety and security.

This is a complex project, and requires knowledge of both GIMP’s
architecture as well as extensive research into security. Mentors
would be learning alongside the student, so any interested individual
would need to be able to work well independently. Please
[contact us](https://www.gimp.org/discuss.html#irc-matrix) to
discuss your proposal for this project.

##
[Improving the text tool
](https://developer.gimp.org#improving-the-text-tool)

- Category
- GEGL, color science
- Project size (GSoC)
- Large (350 hours)
- Skills
- C
- Possible mentors
- Liam Quin
- Difficulty
- Intermediate
- Outcome
- Improvement of the text tool

**This is a project following up a few previous GSoC projects, which
deserves further work as this is a complicated topic.**

Our text tool is a bit of a UI and UX mess and deserves a proper rewrite/enhancement project:

- Re-specify text editing and formating as well as the tool option, for existing
features, but also adding new features for modern text editing (see also this
[draft](https://gui.gimp.org/index.php?title=OnCanvasTextEditing)); - Add
[OpenType support](https://gui.gimp.org/index.php?title=OpenTypeSupport). - Continue previous years experiments on a new text layout library.

##
[Implement GEGL operations for GIMP
](https://developer.gimp.org#implement-gegl-operations-for-gimp)

- Category
- GEGL, image processing
- Project size (GSoC)
- Large (350 hours)
- Skills
- C
- Possible mentors
- Jehan, Øyvind
- Difficulty
- Intermediate
- Outcome
- implementation or improvements of GEGL operations in GIMP or GEGL codebase

The migration of GIMP to use GEGL has accelerated - for some GIMP functionality the main hurdle to migrate is having GEGL ops that can act as drop in replacement for the core processing functionality (some ops would be desired directly in GIMP others could likely go directly into GEGL).

For most code involved, porting to GEGL involves understanding what the current code does; and port or reimplement it as a floating point processing operation (floating point math often ends up shorter and more readable than the 8bit equivalents.

There are also some filters which were ported to GEGL, but some people prefer the old one (e.g. the Sharpen filter). It would be worth investigating the difference and either implement the old one or improve the new one.

[Talk to us](https://www.gimp.org/discuss.html#irc-matrix) for specifics on
which operations would be a good project`.

##
[Implement OpenColorIO Color Management
](https://developer.gimp.org#implement-opencolorio-color-management)

- Category
- User Interface, Core, Tools, GEGL
- Project size (GSoC)
- Large (350 hours)
- Skills
- C
- Possible mentors
- drc, CmykStudent
- Difficulty
- Intermediate
- Outcome
- implementation of the OCIO color management system in GIMP codebase

GIMP uses industry standard [ICC Color profiles](https://www.color.org/profiles2.xalter)
to allow users to match and maintain colors for image editing and printing.
The film industry utilizes a separate standard, [OpenColorIO](https://opencolorio.org/),
which focuses more on manipulating colors in a space rather than trying to keep them
consistent across multiple devices.

This project would involve adding support for OCIO color management in addition to the existing system. This addition would improve user workflows for motion picture and animation work, as well as improve compatibility with other OCIO-supporting software like Blender and Krita. The project would involve the following:

- Research OCIO and color management systems in general
- The Krita manual has an
[excellent overview of the subject](https://docs.krita.org/en/general_concepts/colors/color_managed_workflow.html)

- The Krita manual has an
- Design and test a user interface
- Implement the code

##
[Improve Non-Destructive Editing
](https://developer.gimp.org#improve-non-destructive-editing)

- Category
- GEGL, User Interface
- Project size (GSoC)
- Large (350 hours)
- Skills
- C
- Possible mentors
- Jehan, CmykStudent
- Difficulty
- Intermediate
- Outcome
- implementation of the feature in GIMP codebase

As of version 3.0, GIMP now has initial support for non-destructive
editing with layer effects. Yet there is much more work to be done.
Our [roadmap](https://developer.gimp.org/core/roadmap/#non-destructive-filters)
provides some ideas for the next areas to improve, or you can propose your own:

- Studying the current implementation
- Design improvements to UI or functionality
- Implement the improvements

##
[Improving off-canvas editing
](https://developer.gimp.org#improving-off-canvas-editing)

- Category
- User Interface, Core
- Project size (GSoC)
- Large (350 hours)
- Skills
- C
- Possible mentors
- Jehan
- Difficulty
- Intermediate
- Outcome
- implementation of the feature in GIMP codebase

GIMP recently got the ability to view the image out of the canvas. This is still incomplete. Among the many possible improvements:

- Being able to select off-canvas.
- Being able to see off-canvas but with an effect (e.g. dimming).
- Having various tools and features working differently when “Show All” is enabled.

##
[Improve Metadata Editor and Viewer
](https://developer.gimp.org#improve-metadata-editor-and-viewer)

- Category
- Metadata, Plug-in, User Interface
- Project size (GSoC)
- Large (350 hours)
- Skills
- C
- Possible mentors
- Jehan, Jacob
- Difficulty
- Intermediate
- Outcome
- Improved metadata UI and codebase

Our image metadata viewer and editor could use some code review and improvements.
It currently supports only a subset of all valid metadata, and the UI could be
improved to allow easier editing and viewing of metadata.
There may a better, more logical, division in categories than the current one.
You could check what are the most used tags and which ones are considered
deprecated. Some discussion about this can be found
[here](https://gitlab.gnome.org/Teams/GIMP/Design/gimp-ux/-/issues/521).

Additionally, some image formats such as HEIC, FITs, and DICOM have custom metadata. Another aspect of this project might be considering how to handle these in a way that is easily extensible and maintainable.

For further inspiration, you can review open issues
[tagged with the Metadata label](https://gitlab.gnome.org/GNOME/gimp/-/issues/?label_name%5B%5D=5.%20Metadata)
in our tracker. See also relevant issues in our GIMP UX tracker, e.g. the
following:

-
Review metadata related issues

-
Discuss designs with the UX team at an early stage

-
Develop a plan what exactly you want to work on

-
Design user interface and code structure

-
Implement planned changes in the metadata plug-in


##
[Extension website
](https://developer.gimp.org#extension-website)

- Category
- Web
- Project size (GSoC)
- Large (350 hours)
- Skills
- Python, HTML, Javascript and other web technologies
- Possible mentors
- Jehan
- Difficulty
- Intermediate
- Outcome
- New website and build scripts for continuous integration

We would want a website for our future extension platform, with very specific
criteria.
Apart from some necessary dynamic parts, we want a website as static as
possible, with generated pages when possible. GIMP is a software project, which
relies on community. We don’t want to spend all our time having to maintain and
manage a website with a lot of moving parts. So we need simplicity first,
security first, with just the right amount of dynamicity. The static
website framework which we seem to want to go with the most in our
project right now is [Hugo](https://gohugo.io/).

Even though it has a “web” component, this project is also about
building a proper backend, which includes processing XML metadata
([AppStream](https://www.freedesktop.org/software/appstream/docs/)) in a
secure way (considering third-party received data as unsafe and possibly
malicious), generic static web and repository data from these
repositories, and more.

See [this
document](https://gitlab.gnome.org/Infrastructure/gimp-extensions-web/-/blob/master/docs/README.md)
for an early overview of what we are looking for.
