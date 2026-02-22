# VideoLAN — Project Ideas

**Source:** https://wiki.videolan.org/SoC_2026/
**Scraped:** 2026-02-22T23:28:47.573931

---

# SoC 2026

[Jump to navigation](https://wiki.videolan.org#mw-head)

[Jump to search](https://wiki.videolan.org#p-search)

This page gives the current list of ideas for VideoLAN project, for the [Google Summer Of Code 2026](https://summerofcode.withgoogle.com) program.

The list is long, but it is not exhaustive, and not limitative. Feel free to apply with **your own idea!**, we love original ideas and value them.

## Contents

[1 Introduction & Information](https://wiki.videolan.org#Introduction_.26_Information)[2 How to Start](https://wiki.videolan.org#How_to_Start)[3 Ideas for VLC & libVLC](https://wiki.videolan.org#Ideas_for_VLC_.26_libVLC)[3.1 Advanced Audio Filters](https://wiki.videolan.org#Advanced_Audio_Filters)[3.2 VLC Qt interface redesign](https://wiki.videolan.org#VLC_Qt_interface_redesign)[3.3 VLC Skins2 interface update](https://wiki.videolan.org#VLC_Skins2_interface_update)[3.4 VLC macOS interface redesign](https://wiki.videolan.org#VLC_macOS_interface_redesign)[3.5 VLC watchOS port](https://wiki.videolan.org#VLC_watchOS_port)[3.6 Add back netsync module](https://wiki.videolan.org#Add_back_netsync_module)[3.7 VLC iOS UI update](https://wiki.videolan.org#VLC_iOS_UI_update)[3.8 Android Medialibrary cache management](https://wiki.videolan.org#Android_Medialibrary_cache_management)[3.9 Qt integration tests](https://wiki.videolan.org#Qt_integration_tests)[3.10 Update the Lua integration](https://wiki.videolan.org#Update_the_Lua_integration)[3.11 Port the remote access webserver to VLC Desktop](https://wiki.videolan.org#Port_the_remote_access_webserver_to_VLC_Desktop)[3.12 demux Rust bindings and AVI module for VLC](https://wiki.videolan.org#demux_Rust_bindings_and_AVI_module_for_VLC)[3.13 integrate checkasm tooling and improve existing asm coverage](https://wiki.videolan.org#integrate_checkasm_tooling_and_improve_existing_asm_coverage)[3.14 Vulkan video filters: tonemapping and subtitles](https://wiki.videolan.org#Vulkan_video_filters:_tonemapping_and_subtitles)[3.15 Vulkan video filters: deinterlace, adjust and others](https://wiki.videolan.org#Vulkan_video_filters:_deinterlace.2C_adjust_and_others)[3.16 libvlc Wayland API](https://wiki.videolan.org#libvlc_Wayland_API)[3.17 Lua Declarative UI Framework for Extensions](https://wiki.videolan.org#Lua_Declarative_UI_Framework_for_Extensions)[3.18 Lua API HTTP bindings](https://wiki.videolan.org#Lua_API_HTTP_bindings)[3.19 Lua Script Test Harness](https://wiki.videolan.org#Lua_Script_Test_Harness)[3.20 Use vcpkg contribs](https://wiki.videolan.org#Use_vcpkg_contribs)

[4 Ideas for VLC dependencies](https://wiki.videolan.org#Ideas_for_VLC_dependencies)[5 Other short ideas for VLC & libVLC](https://wiki.videolan.org#Other_short_ideas_for_VLC_.26_libVLC)[6 Ideas for VideoLAN infrastructure](https://wiki.videolan.org#Ideas_for_VideoLAN_infrastructure)[7 Ideas for dav1d and dav2d](https://wiki.videolan.org#Ideas_for_dav1d_and_dav2d)[8 Ideas for libplacebo](https://wiki.videolan.org#Ideas_for_libplacebo)

## Introduction & Information

This page covers the [VideoLAN](/ideas/videolan/videolan) program as a mentoring organization for [Google Summer of Code](http://code.google.com/soc/), in order to improve [VLC](/ideas/videolan/vlc), [VLMC](/ideas/videolan/vlmc) and [dav1d](https://code.videolan.org/videolan/dav1d) (or the [libVLC](/ideas/videolan/libvlc) engine), but also the VideoLAN infrastructure and some other related projects.

We have projects in **C**, **C++**, **Rust**, **ASM**, **JS**, **Wasm**, **Go**, **Obj-C**, **GPU Shaders**, **C#**, **Java/Kotlin** and **Swift**.

### Summer of Code

Google Summer of Code is a way for anyone to work on open source projects and become top developers, while being paid by Google.

[VideoLAN](/ideas/videolan/videolan) was a *Google Summer of Code* mentoring organization in [2007](/ideas/videolan/soc_2007), [2008](/ideas/videolan/soc_2008), [2009](/ideas/videolan/soc_2009), [2010](/ideas/videolan/soc_2010), [2011](/ideas/videolan/soc_2011), [2013](/ideas/videolan/soc_2013), [2016](/ideas/videolan/soc_2016), [2017](/ideas/videolan/soc_2017), [2018](/ideas/videolan/soc_2018), [2019](/ideas/videolan/soc_2019), [2020](/ideas/videolan/soc_2020), [2021](/ideas/videolan/soc_2021), [2022](/ideas/videolan/soc_2022), [2023](/ideas/videolan/soc_2023), [2024](/ideas/videolan/soc_2024) and [2025](/ideas/videolan/soc_2025).

This page lists some ideas for Summer of Code projects on **dav1d**, **dav2d**, **libVLC** and [VLC media player](/ideas/videolan/vlc_media_player), but also on *VLC infrastructure* projects.

We accept ideas also on other multimedia projects related to [VLC media player](/ideas/videolan/vlc_media_player).

### VLC & libVLC

[VLC media player](/ideas/videolan/vlc_media_player) is a cross-platform multimedia player, encoder and streamer application. It is one of the most successful open-source projects worldwide.

[VLC media player](/ideas/videolan/vlc_media_player) is downloaded at an approximate monthly rate of 25 millions from the main website and that's not including third-party distributions (Linux)!

You can find more information on [VLC on Wikipedia](http://en.wikipedia.org/wiki/VLC_media_player) or on this [wiki](/ideas/videolan/main_page).

The engine of VLC is **libVLC**, and is used by **VLMC** and mobile versions of VLC.

### dav1d / dav2d

**dav1d** is the reference AV1 decoder that is shipped inside VLC, Chrome, Edge, Firefox, Windows and macOS/iOS.

**dav2d** is the reference AV2 decoder that is all new.

Those are very low-level codec, mostly written in C and assembly.

### Summer of Code rules

If selected and developed, SoC projects for dav1d and VLC will be included in later releases.

All projects are covered by the GPL (v2+) or LGPL (v2.1+) licenses depending on the module. Projects on dav1d and dav2d are BSD licensed.

The VideoLAN [Code of Conducts](/ideas/videolan/coc) applies to all Summer projects.

## How to Start

### Find an idea

First, you need to find an idea.

This current page gives you a list of ideas. Those ideas are **NOT exhaustive**: you can bring your own idea! Some of the best ideas we've ever had were **custom** ideas!

The duration of the projects is indicative, and can be adapted, if needed.

**TALK** to the team to get more ideas.

### Submit your idea

You need to submit your idea on the *Google Summer of Code* platform.

You should do so, very quickly, even before having finished compilation and the next steps, so that we can give you early feedback.

### Compile VLC or libVLC

This may sound trivial, but it's harder than many expect. You must compile the project you want to work on.

See [https://wiki.videolan.org/Category:Building/](/ideas/videolan/category-building) for more informations.

You should come on [IRC](/ideas/videolan/irc) to get help to compile.

### Provide a small patch

To demonstrate your skills, share a small patch with us. This will let you become familiar with [Git](/ideas/videolan/git), in case you don't know it already and our process on [our gitlab](https://code.videolan.org).

### Let's get in touch

If you have a doubt, are not sure about anything or want clarification, please get in touch with us.

We have 3 major communication channels:

- Our
[mailing-lists](https://mailman.videolan.org/mailman/listinfo)to discuss patches and further development related topics; - Furthermore, we have our
[web forums](http://forum.videolan.org)for VLC-related end-user support - a VLMC section will be created once the product is published. - Finally, there is our IRC channel
*#videolan*(for libVLC) and*#vlmc*on the*libera*network. It's open to any kind of discussion. Usage issues, questions how to compile VLC/VLMC, getting to know the fellow developers, etc.

# Ideas for VLC & libVLC

## Advanced Audio Filters

**Project Description**:
We are looking for a skilled audiophile that knows a lot about audio theory and practice to work on new audio filters for VLC.

**Duration**: 350h

**Tasks to do**:

- SRS WoW like or other 3D effects;
- channels mixing, notably upmixing, like Prologic-II;
- tracks mixing, and transitions;
- scriptable new audio filters in lua and enable users to create whatever audio filtering function they want in a Lua script;
- LADSPA or other libraries integration.

**Requirements**:
This project needs some good audio knowledge and good C experience.

**Qualification task:**
Port any audio filter from MPlayer

*Proposed mentor: unidan *

## VLC Qt interface redesign

**Project Description**:
The VLC interface is quite outdated on Linux and Windows. It has a lot of features, but some are not properly exposed.

We are currently reworking the interface, but we need help.

**Duration**: 350h

**Scope of the tasks to do**:

Use the new designs shared on the mailing list, and help developping part of those, using **Qml**.

This new interface is simpler, more user friendly, and has a better "media center" feel into it.

It requires integration with the media library and with the current interface.

Qml is the technology needed to improve the current UI.

**Requirements**:
This project requires **Qt/C++** knowledge, and qml would be a nice plus.

*Proposed mentor: Pierre*

## VLC Skins2 interface update

**Project Description**:
The VLC Skins2 interface was not updated for the latest interface and core changes for the media player and playlist engine yet.

We are currently reworking the interface, but we need help. Fixing the Winamp skins compatibilities would be nice.

**Duration**: 350h

**Scope of the tasks to do**:

- wayland integration
- video integration rework (like Qt interface)
- medialibrary integration

**Requirements**:
This project requires **Qt/C++** knowledge, and qml would be a nice plus.

*Proposed mentor: Pierre*

## VLC macOS interface redesign

**Project Description**:
The VLC interface is quite outdated on macOS and we are currently in the process of re-writing it to give it a modern feel, but also to integrate recent additions to libvlc regarding playback control and library management.

This project for the summer is to rework heavily this interface to make it beautiful and useful again.

**Duration**: 350h or 175h

**Scope of the tasks to do**:

There is a full design already done and tested.

The major hurdle is to actually implement it the way we want it to be. The iOS/tvOS interface is simpler, more user friendly, and has a better "media center" feel into it, which influenced what we want to achieve on the Mac. Note that the objective is to use AppKit. UIKit will not be part of this project.

Iterating from the current UI and closely collaborating with the team currently working on it is a requirement.

**Requirements**:
This project requires **Obj-C** knowledge, a thorough understanding of OOP and proven previous Mac development experience. You cannot use swift for this project.

*Proposed mentor: David Fuhrmann, Felix Paul Kühne*

## VLC watchOS port

**Project Description**:
VLCKit recently added support for playback of audio files on watchOS with support for http streams coming in a future update. The idea is to create a new, standalone app for watchOS that can play local files on device with a good way to synchronize those either from a computer or the app on the companion iPhone. The UI development needs to be done in SwiftUI following the restrictions of the platform.

**Duration**: 350h

*Proposed mentor: Diogo Simao Marques, Felix Paul Kühne*

## Add back netsync module

**Project Description**:
Use the new vlc clock to add back the netsync module

**Duration**: 350h

**Scope of the tasks to do**:

- Use a new network protocol: RTP Midi
- Expose some vlc_clock APIs to be used by "control" module
- Plug the vlc_clock API inside the new module

**Requirements**:
Very good C knowledge

*Proposed mentor: Thomas Guillem*

## VLC iOS UI update

**Project Description**:
We're currently in the process of rewriting and updating the entire UI for VLC iOS

There is a lot of components that need refactoring and need to get an updated UI.

The Android port of VLC has done most of that and was successful. We need the same level of features.

**Duration**: 350h or 175h

**Tasks to do**:

- Get an overview of the current App and components that need an update
- Refactor and give the appropriate components a new look
- See what is missing compared to the Android version
- Code it :

**Requirements**:
This project requires **Obj-C** and **Swift** knowledge and ideally knowledge of writing tests for iOS but this can be learned.

*Proposed mentor: Felix Paul Kühne, Diogo Simao Marques *

## Android Medialibrary cache management

**Description:**
for upcoming features, the Android port (first and then all the ports) will need a medialibrary caching mechanism. [https://code.videolan.org/videolan/medialibrary/-/issues/293](https://code.videolan.org/videolan/medialibrary/-/issues/293)

Using the new libvlc HTTP client, the medialibrary should be able to download a media, save its download state in the DB and expose all the needed APIs to the ports.

**Duration**: 350h

**Tasks to do:**
- Write the full API
- Download/delete local files
- Persist the state in the DB
- Send the download events
Requirements: This projects requires C++ and SQL knownledge. Java/JNI knowledge can help to (but can be learned)

Proposed mentor: Alaric Senat, Nicolas Pomepuy

## Qt integration tests

**Project Description**:
In order to improve the robustness of our application, we would like to develop integration tests for the Qt interfac.e The goal being to ensure that new features and refactors won't break other parts of the UI.

**Duration**: 350h or 175h

**Scope of the Tasks to do**:

- study existing solutions used in other open-source projects (
[https://invent.kde.org/sdk/selenium-webdriver-at-spi](https://invent.kde.org/sdk/selenium-webdriver-at-spi)) - adapt test framework to our environment
- write sample test cases
- study CI integration feasibility (Linux and/or Windows tests)

**Requirements**:
This project requires Qt/C++ and some scripting language (pyhton?) knowledge, Qml would be a nice plus.

*Proposed mentor: Pierre*

## Update the Lua integration

**Project description**:
The current extension implementation in Lua needs more love to make them first class citizen (they are currently loaded by GUI instead of the core).

**Duration**: 350h

**Tasks to do**:

- update libvlccore to load Lua extensions instead of the GUI
- work on a better descriptive abstraction for lua stream parsers extensions which needs to extract data from the webpage. (currently done by manual read())
- more testing infrastructure for the scripts

**Requirements**:

- Lua and C knowledge, c++ is a plus

**Proposed mentor**: Alexandre Janniaux

## Port the remote access webserver to VLC Desktop

**Description**:
To remotely access and control a VLC instance, a webserver has been developped for VLC Android. The goal is to port it to VLC desktop.

**Duration**: 350h

**Tasks to do**:

- Extract the web client code from the VLC for Android reprository to a dedicated one
- Write the server part in VLC desktop using lua scripts
- Adapt the client to be compatible with the new VLC desktop web server

**Requirements**:

- js, Vue, lua, websockets

**Proposed mentor**: Nicolas

## demux Rust bindings and AVI module for VLC

VLC has already its first Rust (logger) module: [https://code.videolan.org/videolan/vlc/-/commit/e8e46b0d915d153a58d002c9d6f19a7dbdfeeca9](https://code.videolan.org/videolan/vlc/-/commit/e8e46b0d915d153a58d002c9d6f19a7dbdfeeca9)

There was a proposal to add several Rust bindings and example: [https://code.videolan.org/videolan/vlc/-/merge_requests/2738](https://code.videolan.org/videolan/vlc/-/merge_requests/2738)

Tasks

- Adapt demux API Rust bindings to upstream VLC
- Add a new AVI demux module to test the new bindings (Using the nom crate:
[https://crates.io/crates/nom/](https://crates.io/crates/nom/))

**Duration**: 350h

**Requirements**: Good C knowledge and very good Rust knowledge

**Proposed mentors**: Thomas Guillem and Alexandre Janniaux

## integrate checkasm tooling and improve existing asm coverage

**Description**:
VLC has some amount of existing assembly (yadif, video chroma) but we lack test coverage for it and also could use more for newer architectures

**Tasks to do**:

- Integrate checkasm for validation (against a C baseline) and benchmarking (similarly to what's done in dav1d)
- Convert the existing assembly to use it
- Add new optimizations for things like audio/video format conversions, filters and also for newer arch's (riscv etc.)

**Duration**: 175h or 350h

**Proposed mentors**: Marvin Scholz, Nathan Egge, Tristan Matthews

## Vulkan video filters: tonemapping and subtitles

**Description**:

VLC has a work-in-progress Vulkan video output (branch), but it is missing features that already exist in the OpenGL output. This project focuses on integrating libplacebo tonemapping and implementing subtitle rendering through the Vulkan pipeline.

**Duration**: 350h

**Tasks to do**:

- libplacebo tonemapping: use the libplacebo API to generate Vulkan shaders for HDR tonemapping, and integrate them into VLC's Vulkan rendering pipeline;
- subtitles handling: implement a Vulkan subtitle renderer (texture upload, blending, render pass integration), based on the existing OpenGL implementation.

Requirements: This project requires good C knowledge, good Vulkan knowledge, and familiarity with graphics pipelines. OpenGL experience is a plus for reading the reference implementation.

**Proposed mentors**: Thomas Guillem

## Vulkan video filters: deinterlace, adjust and others

**Description**:
Continuing the work on VLC's Vulkan video output (branch), this project ports the remaining video filters from the OpenGL output to Vulkan. This includes the deinterlace filter and adjust-style filters (brightness, contrast, saturation, etc.).

**Duration**: 350h

**Tasks to do**:

- deinterlace filter: port the existing deinterlace filter to Vulkan, using Vulkan compute or fragment shaders for multi-field temporal processing;
- adjust and other video filters: port adjust (brightness, contrast, saturation, gamma) and other video filters to Vulkan shaders;
- all existing OpenGL video filters should be ported.

Requirements: This project requires good C knowledge, good Vulkan and OpenGL knowledge, and experience writing GPU shaders (GLSL/SPIR-V).

**Proposed mentors**: Thomas Guillem

## libvlc Wayland API

In order to allow easy integration of VLC video rendering into application that uses Wayland, similarly to what we provide for X11 or HWND.

**Duration**: 175h

**Scope of the Tasks to do**:

- Provide a method to expose external Wayland surface and additional mechanisms to libvlc.

- Write a sample application to illustrate how to use the API

**Requirements**: This project requires some good C experience

**Proposed mentor**: Pierre Lamot

## Lua Declarative UI Framework for Extensions

**Project Description**:

The current dialog API available to Lua extensions is limited to a small set of widgets (labels, buttons, text inputs, checkboxes, dropdowns, lists) placed on a fixed grid, making it difficult to build rich extension interfaces.

We want to replace this with a modern declarative UI model inspired by SwiftUI and Jetpack Compose, where the extension describes its interface as a function of state and the framework handles rendering and updates.

**Duration**: 350h

**Scope of the tasks to do**:

The project involves designing a new vlc.ui Lua module where extensions declare their interface using nested widget constructor calls that return a description table rather than imperatively creating widgets one by one. A reactive state primitive (vlc.ui.state()) should use Lua metatables to track writes and mark the UI as dirty for re-rendering.

On the C side, a bridge in modules/lua/libs/ui.c will walk the Lua widget tree, diff it against the previous tree, and emit create/update/remove operations toward a platform renderer. The initial renderer target is the Qt/QML interface, mapping abstract widgets (column, row, text, button, text_field, toggle, slider, dropdown, list, image, progress) to their QML equivalents. The framework should support layout containers with spacing, alignment and flexible sizing, a small set of semantic styles (title, body, caption, primary, destructive) rather than raw values, and efficient list rendering with a row template function.

The old vlc.dialog API must remain functional for backward compatibility. Porting one or two existing extensions to the new API will serve as validation.

**Requirements**:

This project requires strong **C** knowledge for the bridge and tree diffing
logic, familiarity with **Lua** and its C API for the module implementation,
and some experience

with **Qt/QML** for the renderer side. Understanding of reactive UI paradigms
(SwiftUI, Compose, React) is strongly recommended.


*Proposed mentor: 'Alexandre Janniaux (espresso)'*

## Lua API HTTP bindings

**Project Description**:
To make interacting with REST APIs in Lua easier and support other HTTP verbs than just GET, we need bindings
from the VLC HTTP library to our Lua script API.

This projects goal is to add a simple Lua API to do HTTP GET, POST and HEAD requests and possibly some more abstract service API, depending on project duration.

**Duration**: 350h or 175h

**Scope of the tasks to do**:

VLC already has a mostly complete HTTP API that is able to do HTTP(s) requests and handle the reply. The main task for this GSoC will involve around how to expose this very low level API in a ergonomic and easy to use fashion as Lua APIs for our Lua scripts to use. Abstract around the session handling and cookie handling and provide ways to properly construct a HTTP request from Lua, with custom HTTP headers, if desired, and a way to fetch the reply status, headers, and read the body content.

Some minor changes to the VLC HTTP library might be necessary in some cases.

**Requirements**:
This project requires strong **C** and **Lua** API knowledge, a thorough understanding of how Lua bindings and the HTTP protocol works.

*Proposed mentor: Marvin Scholz, Alexandre Janniaux*

## Lua Script Test Harness

**Project Description**:

VLC and the community ship Lua scripts (playlist parsers, service discovery, extensions, art fetchers) but has no way to test them outside of a running VLC instance. When a website changes its markup, the corresponding playlist parser breaks silently and the problem is only discovered through user bug reports.

We want a lightweight test harness that can load and exercise VLC Lua scripts against fixture data without requiring a VLC build at all.

**Duration**: 175h or 350h

**Scope of the tasks to do**:

The core idea is to build a standalone binary that embeds a Lua interpreter, registers the same `vlc.*` module tables that VLC exposes to scripts, but backs them with mock implementations instead of real VLC core calls.

A recording mode where a patched VLC session captures real HTTP responses as fixture files would make it easy to turn bug reports into reproductible regression tests for lua writers.

The deliverable is a test runner that can be use to start the different scripts,
like: vlc-lua-mock --mode=playlist --input [http://playlist.url/foo.m3u8](http://playlist.url/foo.m3u8) playlist.lua
and support extensions, and provide a "mock" framework to lua to be able to run
unittests as well.

**Requirements**: This project requires C or Rust knowledge for refactoring,
compiling and linking against VLC's Lua binding sources and writing mock
backends, and some **Lua** knowledge for the test framework, fixture engine,
and writing the actual tests.

Familiarity with test frameworks and test methodology is a plus.

*Proposed mentor: 'Alexandre Janniaux (espresso)'*

## Use vcpkg contribs

**Project Description**:
VLC depends on 130 contrib packages that are external libraries used by VLC and its modules.
A lot of these packages are also available in package systems like vcpkg. This could be an alternative way
to build VLC by using common packages. This would allow more native builds of VLC, especially on Windows
(ie without relying on a POSIX shell).

The meson build system is capable of using vcpkg packages although it's not the default mode of vcpkg.

This projects goal is to add support for as many packages as possible in the vcpkg system to match the existing contribs.

**Duration**: 350h or 175h

**Scope of the tasks to do**:

The main task will be to add package dependencies in vcpkg for all the platforms we support and then adapting the patches found in contribs to the same packages found in vcpkg. This should be usable from our meson build system.

**Requirements**:
This project requires knownledge of **meson**, **make** and **CMake** and package dependencies.

*Proposed mentor: Steve Lhomme, Marvin Scholz*

# Ideas for VLC dependencies

## Cloud integration for desktop

**Project Description**:
We want to be able to access Cloud Storage services (Dropbox, Google Drive and so on) in the VLC application.

**Duration**: 350h or 175h

**Scope of the Tasks to do**:

- revive libcloudstorage
- integrate libcloudstorage inside VLC
- write sample test cases

**Requirements**:
This project requires C++ knowledge.

*Proposed mentor: Pierre*

## Improve libnoidea and integrate in VLC

**Project description**:
Improve the libnoidea project supporting the NDI protocol to support more formats.

**Duration**: 350h

**Tasks to do**:

- Study the NDI protocol, notably more recent versions, and implement and test and integrate inside VLC.

**Requirements**:

- NDI understanding
- C knowledge.

**Proposed mentor**: j-b

## libmicrodns refactoring

Our current mDNS discoverer is working, but is not so respectful of the RFC. Possible improvements include:

- Device TTL support
- Device removal detection
- Better request pacing
- Delegate socket interactions to the caller
- Unit testing
- Fuzzing

**Requirements**: This project require **C** knowledge, as well as system programming skills

**Duration**: 175h

*Proposed mentor*: tguillem

## libspatialaudio acceleration

Our current libspatialaudio is working, but we need it to become faster

Work to be done

- Plug checkasm
- Profile functions
- Write x86 or ARM assembly to make it faster
- Test
- Repeat

**Requirements**: This project require **C** knowledge, as well as system programming skills

**Duration**: 175h

*Proposed mentor*: tguillem

## Improve the LibVLCSharp developer experience and ecosystem

libVLCSharp provides .NET bindings for libVLC and enables building cross-platform media applications in C#.

This GSoC project aims to improve the developer experience around LibVLCSharp by providing better documentation, practical UI samples, improved NuGet packaging, and stronger automated testing and CI.

Work to be done

- Audit and improve existing documentation and API guides
- Write developer-focused tutorials and usage examples
- Provide modern sample applications (WPF, WinUI/MAUI or cross-platform UI)
- Improve NuGet packaging and versioning
- Enhance CI to automatically build, test, and publish packages
- Add unit and integration tests for playback scenarios
- Improve overall project structure and contributor onboarding

**Requirements**: This project requires C# and .NET knowledge. Familiarity with cross-platform development, CI systems, and multimedia concepts is a plus.

**Duration**: 175h

*Proposed mentor*: Martin

## Improve the VLC for Unity developer experience and ecosystem

VLC for Unity is the native Unity plugin that bridges LibVLCSharp with LibVLC for performance oriented video rendering in Unity3D applications and games.

Work to be done

- macOS universal build support: Add automated macOS universal (Intel + Apple Silicon) builds to ensure seamless compatibility and distribution across all modern Mac hardware.
- Build cool demos and prototypes: Develop polished demo projects and prototypes that showcase real-world use cases such as streaming, in-game cutscenes, and immersive/360° playback to accelerate adoption.
- tvOS / Linux support: Extend the plugin to tvOS and Linux with tested native builds and documented setup steps to broaden platform coverage.
- Deeper Unity Editor integration: Implement VLC configuration tools inside the Unity Editor to simplify setup.
- CI and automated testing improvements: Introduce automated tests to prevent regressions, and maintain reliability across all supported platforms.

**Requirements**: This project requires C# and Unity knowledge. Familiarity with cross-platform development, CI systems, and multimedia concepts is a plus.

**Duration**: 175h

*Proposed mentor*: Martin

# Other short ideas for VLC & libVLC

Those ideas are not detailed, but they are ideas that we could help to spring new ideas. We can help work with you to make those more detailed.

Those ideas should be **175h** long

- Improve id3 tag and metadata handling in VLC
- Bridge module for GMI'C or other video filters
- Automated Testing Environment like ffmpeg Fate (port ?) for demuxing, non-hw decoding
- Integrate libavfilter in VLC
- Provide setups for popular streaming services / sout templates (ui ?)
- Improve cue support in VLC

# Ideas for VideoLAN infrastructure

## Improve the VideoLAN crash reporter in Go and Vue.js

The idea is to improve the current crash reporter of VLC, called [CrashDragon](https://code.videolan.org/videolan/CrashDragon).

The tasks are the following:

- Review the current code
- Improve the API in Go
- Write a new Vue.js frontend

Those will be done in **Go** and **JS**

**Duration**: 350h

*Proposed mentor: David and j-b*

# Ideas for dav1d and dav2d

## dav1d RISC-V optimizations

Improving the performance of the AV1 decoder is very important for VLC and the whole ecosystem.

It requires to:

- Understand of RISC-V assembly
- Understand a bit what a video decoder is
- Write RISC-V functions

**Requirements**: This project requires **C** and **ASM** knowledge, as well as system programming skills

**Duration**: 175h

Contact 'j-b'



## dav2d RISC-V optimizations

Improving the performance of the AV2 decoder is very important for VLC and the whole ecosystem.

It requires to:

- Understand of RISC-V assembly
- Understand a bit what a video decoder is
- Write RISC-V functions

**Requirements**: This project requires **C** and **ASM** knowledge, as well as system programming skills

**Duration**: 175h

Contact 'j-b'



## dav2d ARM optimizations

Improving the performance of the AV2 decoder is very important for VLC and the whole ecosystem.

This is less complex than what it seems!

It requires to:

- Understand of ARM assembly
- Understand a bit what a video decoder is
- Write ARM functions

**Requirements**: This project requires **C** and **ASM** knowledge, as well as system programming skills

**Duration**: 175h

Contact 'j-b'

## dav1d statistics extractions

The [dav1d](https://code.videolan.org/videolan/dav1d) AV1 decoder is a new high performance AV1 decoder by
VideoLAN.

Current open source tools for AV1 analysis use instrumentation in the reference decoder [libaom](https://aomedia.googlesource.com/aom) to extract decode-time metadata for display and reporting, but support for sophisticated analysis is lacking.

To speed development of AV1 tools like the rav1e, it would be helpful to add similar decoder metadata extraction APIs to the dav1d decoder so that rapid testing of encoder algorithms is easier. This includes the ability to quickly produce statistics, visualizations and other reporting that can be used for tuning encoder parameters or guiding development. Advanced ideas include adding similar encoder metadata API to rav1e that add encode-time visualizations.

**Requirements**: This project requires **C** knowledge.

**Duration**: 175h

Contact 'unlord'

# Ideas for libplacebo

## Direct3D 11 backend

**Project Description:**

libplacebo uses a GPU abstraction with a number of backends. The goal would be to add a new backend based on Direct3D 11, since Vulkan and OpenGL support on Windows are often of limited quality, especially for older hardware.

Lots of example code for how this implementation would look can be found [as part of the mpv project ](https://github.com/mpv-player/mpv/blob/master/video/out/d3d11/ra_d3d11.c).

Large parts can be copy/pasted and adapted to the libplacebo API.

**Tasks to do:**

- Add a new `pl_gpu` backend based on Direct3D 11
- Integration into the build system, test framework and CI infrastructure

**Requirements:**

- Knowledge of
**C**as well as, ideally, graphics API fundamentals. (But the latter can be learned as part of the project) - Ability to develop and test on Windows

**Duration**: 175h

Contact 'haasn'

## Dolby Vision Profile 5 (IPT-PQ)

**Project Description:**

Dolby IPT-PQ is a HDR color space similar to ITU-R ICtCp, but with proprietary Dolby modifications (reshaping algorithm). Your goal is to implement this reshaper in the form of a GLSL shader, using knowledge from known Dolby patents and dumped headers.

**Tasks to do:**

- Figure out, and (if necessary) reverse engineer the stream format for the Dolby reshaping algorithm described in several of their patents.
- Implement this algorithm in GLSL
- Integration into libplacebo (optional)
- Test against reference implementations of Dolby Vision profile 5

**Requirements:**

- Knowledge of
**GLSL**and**C**. Knowledge of colorspaces in general is an obvious plus, but the theory here is not important - only the implementation. - (Possibly) Ability to reverse engineer any still-unknown or differing-from-patents parts of the stream headers.

Knowledge of libplacebo internals is not required, since the skeleton code for this already exists - what's missing is the reshaping algorithm.

**Duration**: 350h

Contact 'haasn'

## GPU motion interpolation (mvtools)

**Project Description**

Your goal is to develop GPU shaders for motion-adaptive frame interpolation in the style of [mvtools](https://wiki.videolan.org/SoC_2026/[https:/github.com/dubhater/vapoursynth-mvtools](https:/github.com/dubhater/vapoursynth-mvtools)).

This is an open-ended project. If not completed, any progress towards this goal is good enough.

**Sub-goals:**

- Recreate the motion vector search algorithms from MAnalyze
- Implement the pixel masking and pixel flow algorithms from MFlowFps

These can be tackled and complete out-of-order.

**Requirements:**

- Good knowledge of both C and GLSL, especially compute shaders and other GPGPU techniques. (CUDA or OpenCL skills also transfer, though the shader will have to be GLSL)
- Ideally, general knowledge of video processing techniques (e.g. motion vector search) - at least enough to be able to understand what mvtools code is doing.

**Duration**: 350h

Contact 'haasn'





|
|
