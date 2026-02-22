# roadmaps

**Parent:** GNU Image Manipulation Program — Project Ideas
**Source:** https://developer.gimp.org/core/roadmap/
**Scraped:** 2026-02-22T23:28:47.565606

---

# Roadmaps

##
[Feature Prioritization
](https://developer.gimp.org#feature-prioritization)

This page shows roughly how the core development team plans GIMP evolution. The absence of features from these roadmaps doesn’t mean we are not interested: since GIMP is developed as a community, all it takes to revise priority is for someone to contribute.

**Our roadmaps are not “holy truth”, they are flexible and evolving.**

The bottom line is that GIMP is what we all make of it. There is no single company or entity heading the software (code admission is based on quality and usefulness, not dictated by someone’s business).

##
[GIMP 3.2
](https://developer.gimp.org#gimp-32)

List of features which we will have in GIMP 3.2 (we are in feature-freeze period):

| Feature | Status | Comments |
|---|---|---|
| Link layers | done |
|

**done**[!773](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/773). Back-end exists since 2006, UI was inadequate.**done**[MR !2359](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/2359)(except Spectral Blending features, see[#14441](https://gitlab.gnome.org/GNOME/gimp/-/issues/14441))##
[GIMP 3.4
](https://developer.gimp.org#gimp-34)

List of features for which some work was started and we hope to have in GIMP 3.4:

| Feature | Status | Comments |
|---|---|---|
| Modern default set of resources | WIP | See
|

[!2528](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/2528)[!2522](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/2522)[!2379](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/2379)and[early experiments](https://fosstodon.org/@CmykStudent/114073031868807701). Also see[the main GIMP FAQ](https://www.gimp.org/docs/userfaq.html#i-do-a-lot-of-desktop-publishing-related-work-will-you-ever-support-cmyk)for details[Some legacy effects](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/2023)only are supported right now). Depends on Photoshop descriptor handling ([!2338](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/2338)).[GSoC 2024 work](https://developer.gimp.org/core/internship/archive/#robust-opencl-operations)and recent work on OpenCL in GIMP core’s GEGL ops ([!2414](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/2414)and[!2415](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/2415)), we may experiment re-enabling OpenCL[comment on issue 2912](https://gitlab.gnome.org/GNOME/gimp/-/issues/2912#note_431542)The Foreground selection interaction should be reworked as a tool to select particles or object borders##
[GIMP 3.6
](https://developer.gimp.org#gimp-36)

List of features for which some work was started and we hope to have in GIMP 3.6:

| Feature | Status | Comments |
|---|---|---|
| Core animation | WIP | Animation plug-in is dropped, this is being rewritten as a core feature |
| Page support | WIP | Proper document’s “page” concept (instead of using layers) |
| Inpainting tool | No | Feature long-available with resynthesizer third-party plug-in; would deserve GEGL-based core implementation |

##
[Development Focus
](https://developer.gimp.org#development-focus)

We have several focus projects these days. These will happen on minor point releases (when the second number of the version increases) as micro point releases (third number increment) is for bug fixes.

The features are gathered per topic below, though they may be spread through several releases.

###
[Non-destructive editing
](https://developer.gimp.org#non-destructive-editing)

Some work has been started already around new types of layers, which
will also be the start point for new tools (such as a *Shape Tool* which
makes sense as a vector tool).

| Feature | Status | Comments |
|---|---|---|
| Shape tool | No | Easily create circles, rectangles, N-side polygons, stars etc. Either a new tool or a rewrite of the path tool with shape options |
| Less destructive transform | WIP | Squash successive transforms into a single matrix and merge the result as just-on-time before other types of edits |

###
[Non-destructive filters
](https://developer.gimp.org#non-destructive-filters)

A first implementation of non-destructive filters was released in **GIMP 3.0**!

Note that both adjustment layers and layer effects/styles are the terminologies currently used in requests by users.

| Feature | Status | Comments |
|---|---|---|
| Better GUI for layer effects | Specified |
See
|

[gimp-ux#240](https://gitlab.gnome.org/Teams/GIMP/Design/gimp-ux/-/issues/240).###
[Animation and multi-page support
](https://developer.gimp.org#animation-and-multi-page-support)

Long-term work has been done around animation concepts. It will also bring multi-page ability.

| Feature | Status | Comments |
|---|---|---|
| Story-board mode | WIP | |
| Improved export | WIP | More ability to export full-document, per-page, per layers… Web exports and alternative views were also discussed. |

###
[Macros (script recording)
](https://developer.gimp.org#macros-script-recording)

Ultimate continuation of a work which started in GIMP 2.10 and 3.0, where we started to
store parameters of every successful filter’s runs and plug-in’s runs.
Same should happen for tool usage.
Finally we need the proper infrastructure to allow [replaying
actions](https://gitlab.gnome.org/GNOME/gimp/-/issues/8).

| Feature | Status | Comments |
|---|---|---|
| Action storage infrastructure | No | Class (`GimpMacro` ?) to handle a “recording” which can be replayed |
| Store GEGL ops, plug-in runs, GIMP actions and tool use | WIP | These must be recordable in a `GimpMacro` |
| On-disk storage | No | A `GimpMacro` must be serializable and deserializable across sessions |
| Script-export | No | A `GimpMacro` should also be exportable in “code form” which can be reused as a plug-in |
| Macro tweak | No | A `GimpMacro` should be viewable and tweakable: e.g. you could trigger a recorded drawing at a higher resolution! |
| Script recording and playback | No |
|

###
[Extensions
](https://developer.gimp.org#extensions)

The work was started for GIMP 3.0 for which we originally hoped to finalize the
new concept of “GIMP extensions”, a new wrapper format (`.gex`

) which can embed
plug-ins, brushes, dynamics, themes and other data, (un)installable in 1 or 2
clicks.

The core infrastructure is already present since GIMP 3.0, but we also want to make this public with a new online infrastructure, allowing third-party extension creators to upload their extensions and everyone to browse available ones.

| Feature | Status | Comments |
|---|---|---|
| Icon themes in extensions | done |
|
| Themes in extensions | done |
|
| Brushes in extensions | done |
|
| Plug-ins in extensions | nearly done | plug-ins cannot be disabled or enabled live (without GIMP restart) yet |
| GEGL operations in extensions | No | |
Installing extensions from `.gex` file |
done |
|
| Extension website | WIP | A
|

[!120](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/120)Allow core to send signals for plug-ins to react###
[Space Invasion
](https://developer.gimp.org#space-invasion)

“Space Invasion” is the codename for a long-lived project, started with GIMP
2.10 development, i.e. [back in
2012](https://gimpfoo.de/2012/04/17/goat-invasion-in-gimp/). The concept is to
make GIMP more than a sRGB editor. First we focused on anyRGB, but nowadays we
are even more into anySpace support. We want to be able to edit images with CMYK
backend too (right now, we can do CMYK 🗘 RGB roundtrips which is nice but not
enough), also allowing random channels (e.g. spot color channels), and of course
why not CIELAB images or whatever could be useful.

HDR support is definitely also a good target eventually.

| Feature | Status | Comments |
|---|---|---|
| Spot Color support | No | Ability to add more channels for printing. |
| Reviewing/Improving Indexed color mode | No | Our Indexed mode is limited and not so well maintained. Make a review of how people use it and how to improve it would be a nice project. |

###
[Tools
](https://developer.gimp.org#tools)

We have been planning several new interesting tools or tool enhancements. Some are still only conceptual, though some already have experimental implementations which we consider not in a releasable state.

| Feature | Status | Comments |
|---|---|---|
| Seamless Clone tool | playground | Released as experimental in 2.9.2, needs work |
| N-point deformation tool | playground | Released as experimental in 2.9.2, needs work |
| Text tool re-work | WIP | This tool deserves a big rewrite of interaction (closer to well-known interactions, such as in LibreOffice); see also a
|

[proposal in-progress](https://gui.gimp.org/index.php?title=OpenTypeSupport)###
[Painting
](https://developer.gimp.org#painting)

Various interesting topics have been raised across the years and would be worth investigating for improving GIMP’s painting abilities.

| Feature | Status | Comments |
|---|---|---|
| Better palettes | WIP | High bit depth, multi-format, etc. Some core work was already done in 3.0 |
| Better brushes | WIP | High bit depth, color spaces, animations, other… |
| New Brush Engine | No | Some work from
|

[#1319](https://gitlab.gnome.org/GNOME/gimp/-/issues/1319)[#498](https://gitlab.gnome.org/GNOME/gimp/-/issues/498)though a more complete GUI solution (radial menu?) could be studied###
[Canvas
](https://developer.gimp.org#canvas)

Since GIMP 2.10, we added some advanced canvas concept, such as the ability to see and even work off-canvas. This is still incomplete, and we still intend to add new concepts of either auto-growing layers or even infinite layers.

| Feature | Status | Comments |
|---|---|---|
| Off-canvas selection | No | |
| “Show All” contextual actions | WIP | The “View > Show All” action should change more widely how various features interfere with the image. |

###
[GUI
](https://developer.gimp.org#gui)

GIMP’s interface has always been very customizable, though it can always be
improved. For instance while the “single window mode” ([since
2.8](https://www.gimp.org/release-notes/gimp-2.8.html#single-window-mode)) was
very welcome, in many case, we wished for a mix of the single and multi window
modes. Moreover a horizontal toolbar is often wished for, as well as
improvements of dockable management. These are all topics which could be
redesigned and worked on.

| Feature | Status | Comments |
|---|---|---|
| Improved toolbox | No | Simpler customization, draggable to other area, detachable, ability to show more than display size with `…` icon, etc. |
| Toolbar | No | Customizable to set quick buttons to any possible action |
| Better window management | No | Rather than a SWM vs MWM, both able to do some things the other can’t, we should have a single window mode which can do everything |
| Dockable interaction review | No | Review and change how we can create, lock, unlock and reorganize dockables |

##
[Miscellaneous
](https://developer.gimp.org#miscellaneous)

Many of these features are on contributors wishlist and can be implemented in a branch and merged into the main development branch as we go, especially since we loosened up the “no new features in stable releases” policy. Please talk to us, if you want to work on any of those.

| Feature | Status | Comments |
|---|---|---|
| Optionally save undo history in the XCF | No |
|

[Milestone “Future” in Gitlab](https://gitlab.gnome.org/GNOME/gimp/-/milestones/1)

##
[Archived Roadmaps
](https://developer.gimp.org#archived-roadmaps)

###
[GIMP 3.0
](https://developer.gimp.org#gimp-30)

The focus of this version was to complete the GTK+3 port and reduce technical debt in used technologies.

Benefits:

- Better maintained version of GTK
- Better graphics tablet support
- Better handling of HiPPI displays
- Wayland support on Linux
- Refactored code, easier to build new features upon

| Feature | Status | Comments |
|---|---|---|
| Port to GTK3 | done |
(except minor API usage, but no major tasks anymore) |
| Port away from intltool | done |
We are now full gettext |
| Port to meson build | done |
Autotools was removed |
| Redesign API for scripts/plug-ins | done |
GObject Introspection introduced, along with refactoring, no wire protocol redesign in the end, big API improvements |
| Wayland support | done |
Various bugs still happen, especially in window management area (broken sizes and positions), color management, but mostly because of missing protocols in Wayland… |
| Space invasion | done |
Various color management improvements, CMYK support (not as core image format, but import/export and picking/choosing/viewing)… |
| Multi-layer selection | done |
Most code is multilayer aware… |
| Less “floating selection” | done |
Discussed on the
|

**done****done**[#32](https://gitlab.gnome.org/GNOME/gimp/issues/32)- auto-growing layers are[part of gsoc 23 (#9314)](https://gitlab.gnome.org/GNOME/gimp/-/issues/9314)**done**[!843](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/843)(GIMP 3.0)**done**[!958](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/958):[started](https://fosstodon.org/@CmykStudent/110357425899091109)as[part of gsoc 23 (#9244)](https://gitlab.gnome.org/GNOME/gimp/-/issues/9244)**done**[!1376](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/1376)###
[GIMP 2.10.x series
](https://developer.gimp.org#gimp-210x-series)

The 2.10.x series coexisted with the ongoing work to port GIMP to GTK+3 and cleanup obsolete API.

We tried to backport fixes and new features to 2.10.x when we could.

| Feature | Status | Comments |
|---|---|---|
| High bit depths | done |
Released in 2.9.2 |
| Preview filters on canvas | done |
Released in 2.9.2 |
| OpenCL support | done |
Released in 2.9.2, more plugins need OpenCL version |
| Turn the IWarp plug-in into an on-canvas tool | done |
Initial version released in 2.9.2. Improved version released in 2.9.6. |
| Merge basic transformation tools | done |
Unified Transform tool, released in 2.9.2 |
| Canvas rotation and flipping | done |
Released in 2.9.2 |
| MyPaint Brush tool | done |
Released in 2.9.4. No brush create/edit support (
|

**done****done****done****done****done****done****done****done****done****done****done****done****done**
