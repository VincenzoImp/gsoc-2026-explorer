# LibreOffice — Project Ideas

**Source:** https://wiki.documentfoundation.org/Development/GSoC/Ideas
**Scraped:** 2026-02-22T23:28:47.552214

---

# GSoC Ideas

[Development](https://wiki.documentfoundation.org/Development)|

[GSoC](https://wiki.documentfoundation.org/Development/GSoC)

[TDF](https://www.documentfoundation.org/)
[LibreOffice](https://www.libreoffice.org/)
[Document Liberation Project](https://www.documentliberation.org/)
[Community Blogs](https://planet.documentfoundation.org/)
[Weblate](https://translations.documentfoundation.org/languages/en)
[Nextcloud](https://nextcloud.documentfoundation.org/)
[Redmine](https://redmine.documentfoundation.org)
[Ask LibreOffice](https://ask.libreoffice.org)
[Donate](https://www.libreoffice.org/donate/)


This page lists the project ideas for Google Summer of Code, see the [general info about LibreOffice and GSoC](https://wiki.documentfoundation.org/Development/GSoC). All applicants are required to complete at least one [easy hack](https://wiki.documentfoundation.org/Development/EasyHacks).

All tasks on this page already indicate mentors for the task. New tasks on this page should be added only by those with the experience and time to invest in mentoring new developers.

Applicants should not use an LLM AI when writing proposals. Please study our [AI policy](https://wiki.documentfoundation.org/Development/AI_policy) in its entirety.

Note that the LibreOffice project selects GSOC projects that are well researched and show a good understanding of the scope of the problem. It is also possible to create a project proposal not based on the ideas given below, if the application of the contributor shows good understanding of the problem. In fact, if you apply with one of the prepared ideas below, we expect you to show you did research beyond the abstracts given below even more.

When doing that please use this template:

=== Title of the task === Some detailed description of the things to accomplish. Don't hesitate to provide details if you have some like code pointers, links to specifications, etc. Goal(s) - the expected outcome of the project. ;Required skills / knowledge: C++, Reading other's code, and any other useful skill required go here. ;Size: 90, 175 or 350 hours ;Difficulty: Range among easy, medium, hard ;Potential mentors :''Joe Devel'', IRC: jdevel, mail: {{nospam|joe|devel.org}}

Please move successfully completed projects to [Development/GSoC/Successfully Implemented Ideas](https://wiki.documentfoundation.org/Development/GSoC/Successfully_Implemented_Ideas).

## User Experience

The design team collected a number of ideas in in the pad [http://pad.documentfoundation.org/p/UX-GSoC_Ideas](http://pad.documentfoundation.org/p/UX-GSoC_Ideas). Not for all ideas mentors have committed so far. If you are interested in a task that has no mentor you would need to find someone. If the topic needs further refinement feel free to contact the UX team in order to prioritize the usability engineering. Some examples for full-featured topics:

### Improve snapping and object selection

Snapping in LibreOffice is a bit awkward, and doesn't work as expected in some cases. There is also no advanced snapping supported (taking into account multiple object positions and distances), which would make object position and sizing much easier for the user. This idea involves investigating the existing implementation for snapping in the svx module and work on it.

Goal:

Make snapping and object selection pleasant to use.

Extended goal for this idea is to look into object selection and handles rendering, consistency and UX. In some cases the selection and selection handles aren't properly rotated with the object, sometimes an outline of the selection isn't rendered or rendering could be improved.

- Required skills / knowledge
- (C++, Reading other's code)?

- Size
- 350 hours

- Difficulty
- Hard

- Potential mentors
*Tomaž Vajngerl*, IRC: quikee, mail: quikeegmail.com

### Re-design Notebookbar using Native Toolkit Widgets

The task here is to redesign the Notebookbar to use [vcl weld mechanism](https://wiki.documentfoundation.org/Development/VCL/weld) instead of custom widgets. The issue is filed as [tdf#163988](https://bugs.documentfoundation.org/show_bug.cgi?id=163988) in Bugzilla.

Currently, although Notebookbar uses Glade UI files, it uses [custom widgets](https://dev.blog.documentfoundation.org/2024/11/14/notebookbar-part-1-custom-widgets-for-the-tabbed-interface/), and most of the logic is done in C++ code.

Although the result looks nice with GTK3 and some other UI plugins, it has some drawbacks as described in [tdf#163988](https://bugs.documentfoundation.org/show_bug.cgi?id=163988). Specially in GTK4, the result is not interesting. Also, changing the Notebookbar in the Glade interface designer is not easy/possible with this approach.

The task here is to re-design the Notebookbar, using native toolkit widgets and make sure that is usable with VCL weld mechanism. Doing modifications in the C++ code to make it usable in LibreOffice UI is not part of this task, so that people who only know how to design, but are not familiar with C++ can also do the task. To make the result usable with LibreOffice, additional coding/refactoring is needed which does not fit into this project.

One can start by creating a dialog box with `GtkNotebook`

, and then add appropriate icons and other GTK widgets to reach to a reasonable UI, comparable to what is available with the custom widgets.

Please note that not each and every GTK widget is supported by VCL weld, so you have to go step by step to make sure that the result works well with VCL weld mechanism.

A preview can be generated by both `glade-previewer -f notebook.ui`

and also by using the ui file with [minweld example](https://wiki.documentfoundation.org/Development/VCL/minweld). One may test the result, after putting the UI file in `instdir/share/config/soffice.cfg/`

and changing the `minweld`

example to reflect the name of the UI and the ID of the dialog.

`./bin/run minweld`


Goal:

Re-design Notebookbar using native widgets.

- Required skills / knowledge
- UI Design, Glade UI designer, Reading other's code

- Size
- 175 hours

- Difficulty
- Medium

- Potential mentors
*Hossein Nourikhah*, IRC: hossein, mail: hosseinlibreoffice.org

## Base

## Basic

### BASIC IDE code auto-completion

LibreOffice BASIC has a built-in code completion feature, that while useful, is very limited, and is not really helpful in practice.

The current feature is available via "Tools > Options > LibreOffice > Code Completion". Then, you may write something like this:

```
Sub Main
Dim aPicker As com.sun.star.ui.dialogs.XFilePicker
aPicker.
End Sub
```


After typing `aPicker`

and then `.`

(dot), you should be able to see the code completion popup.

The task here is to provide better code complete feature. These are some of the required features:

- Be able to handle various types of objects, and not only UNO objects in certain conditions.
[tdf#165786](https://bugs.documentfoundation.org/show_bug.cgi?id=165786)describes the need for ctrl+space code completion, alongside "." dot code completion which is described in[tdf#66185](https://bugs.documentfoundation.org/show_bug.cgi?id=66185). - Add the "Quick Info" and "Parameter Info" functionality, as described in
[tdf#92253](https://bugs.documentfoundation.org/show_bug.cgi?id=92253) - Make BASIC IDE code completion enabled by default, filed as
[tdf#165780](https://bugs.documentfoundation.org/show_bug.cgi?id=165780)

- Goal

Better code completion for LibreOffice BASIC IDE editor

- Required skills / knowledge
- C++, UNO, BASIC, Reading other's code

- Size
- 350 hours

- Difficulty
- Hard

- Potential mentors
*Hossein Nourikhah*, IRC: hossein, mail: hosseinlibreoffice.org

## Draw

## Impress

### Attach animations to styles

Currently, Impress styles control most of the visual shape appearance, but not the slideshow animation effect. Which is a pity, as the styles concept is pretty powerful inside LibreOffice, and provides a nice way to change animation settings and type for a great number of objects simultaneously. For a slightly different view onto the same problem, see [this](https://bz.apache.org/ooo/show_bug.cgi?id=73090) bug report, and [this one](https://bugs.documentfoundation.org/show_bug.cgi?id=41572) from the LibreOffice side.

Original patch from GSoC 2010: [https://cgit.freedesktop.org/libreoffice/build/tree/patches/dev300/sd_effects_styles.diff?h=master-backup](https://cgit.freedesktop.org/libreoffice/build/tree/patches/dev300/sd_effects_styles.diff?h=master-backup)

Goal:

Make styles animatable.

- Required skills / knowledge
- C++, Reading other's code

- Size
- 350 hours

- Difficulty
- Hard

- Potential mentors
*Thorsten Behrens*, IRC: thorsten, mail: thorsten.behrensallotropia.de*Katarina Behrens*, IRC: bubli, mail: bublibubli.org

## LibreOfficeKit

### LibreOfficeKit Qt

LibreOfficeKit is a way of embedding LibreOffice functionality in other applications. It can do document conversion with its stable API, and tile-based rendering makes it possible to edit the documents using its unstable API.

The task here is to create a custom Qt widget that uses LibreOfficeKit unstable tile rendering API to do display and edit LibreOffice documents, and also a Qt application that uses the custom Qt widget.

The final result should provide functionalities similar to what LibreOfficeKitGtk offers in GtkTiledViewer application.

The resulting code is expected to be around 3-5K C++ code. It should not depend on any external libraries except Qt, and of course the LibreOfficeKit itself.

To get started faster, a basic LibreOfficeKit Qt widget and application will be provided, which can be the base of the final implementation.

- Required skills/knowledge
- C++, Qt, reading other people's code

- Size
- 350 hours

- Difficulty
- Medium to hard

- Potential mentors
*Hossein Nourikhah,*IRC: hossein, mail: hosseinlibreoffice.org*Jonathan Clark*, IRC: jonclark, mail: jonathanlibreoffice.org

## Calc

## Common

### Accessibility checker for Impress and Calc

We have an accessibility checker sidebar in Writer, but not in Impress and Calc. The accessibility checker triggers a check of the document for accessibility issues and displays those in the sidebar, with helpful hints how to resolve those issues. Accessibility issues include checks of the document metadata (name, description), document structure, objects in the document, as well as check of contrast (font color vs. background color). A lot of issues apply for Impress and Calc too, but some are Writer specific and there as some that are unique to Impress and Calc.

Goal:

Add accessibility sidebar to impress (move code from writer to common code into svx or sfx2), implement a trigger to re-run a check when an object changes, go through the accessibility checks for writer and investigate which check also applies to Impress, add the accessibility check to common code and adapt if necessary (for example to work in editeng and not writer model). If there is still time, repeat the same for Calc.

- Required skills / knowledge
- C++, Reading other's code, Debugging,

- Size
- 350 hours

- Difficulty
- Medium to Hard

- Potential mentors
*Tomaž Vajngerl*, IRC: quikee, mail: quikeegmail.com

### Extend support for document theme colors

Support for theme colors is already implemented for Writer, Impress/Draw and Calc, however some colors weren't extended to support theme colors properly. Also when we define gradients we don't support theme colors there so support for theme color gradients would need to be added.

Goal:

Search for properties or parts of properties where we use colors, but we don't support to set a ComplexColor (used for theme colors). Implement a property that works with a ComplexColor for that property, add support to change the color in ThemeColorChanger, write a round-trip test and adapt the import/export filters (for ODF and OOXML) to support saving the theme color for the property. Repeat.

- Required skills / knowledge
- C++, Reading other's code, Debugging

- Size
- 350 hours

- Difficulty
- Hard

- Potential mentors
*Tomaž Vajngerl*, IRC: quikee, mail: quikeegmail.com

## Filters

## UNO

UNO is the LibreOffice component model, cross-language and intra- as well as inter-process. It is somewhat similar to Corba and COM. It is used to extend LibreOffice via document-related scripts and more general extension packages, as well as to use LibreOffice functionality remotely from another process.

UNO's cross-language abilities are implemented by bridging between various language-specific environments and a binary runtime representation (with a C API).

### Documentation support for Codemaker tools

Codemaker tools, including cppumaker, javamaker, netmaker and recently, pythonmaker are the tools that are used to generate language specific representations of the IDL files.

In C++/Java, the output from codemaker tools is needed to write code that uses LibreOffice API. In Python, one needs them to have auto-completion support in an IDE. This IDE auto-completion support is also true for C++ and Java. Currently, `codemaker`

tools lack the ability to process the documentation comments inside IDL code and turn them into appropriate documentation output. This is what Doxygen does for generating HTML documentation.

The result is both useful for getting help, and also better IDE auto-completion. Further information can be found

Goal:

Add documentation support to one pr more of the Codemaker tools to get better code auto-completion using the documentation from IDL specifications.

- Required skills/knowledge
- C++, Python, reading other people's code

- Size
- 350 hours

- Difficulty
- Medium to hard

- Potential mentors
*Hossein Nourikhah,*IRC: hossein, mail: hosseinlibreoffice.org

## Tests

### Improve word processor test coverage

LibreOffice Writer is the foremost Free and Open Source word processing program. During our 39 year development history, we're proud to have added comprehensive support for world languages, word processor use cases, and interoperability with other office suites. However, offering so many features has a cost in source code size and complexity. One of our greatest challenges today is managing this complexity.

The goal for this project is to develop automated tests for LibreOffice Writer features that currently do not have tests.

- Use a test coverage report and C++ skills to identify features that require more tests.
- Use C++ debugging skills to create LibreOffice Writer documents that exercise target code.
- Use C++ to develop automated tests that assert the correct program behavior.
- File bug reports with detailed instructions and example documents, as needed.

- Required skills / knowledge
- C++, Reading code written by others

- Size
- 175 hours

- Difficulty
- Medium

- Potential mentors
*Jonathan Clark*, IRC: jonclark, mail: jonathanlibreoffice.org

## Ideas without a mentor

A number of ideas from previous years can be found at the [Development/GSoC/Ideas without a mentor](https://wiki.documentfoundation.org/Development/GSoC/Ideas_without_a_mentor) page. Please note that you need to find a mentor willing to mentor the task. There is no guarantee that anyone in the community is going to mentor one of these tasks this year.
