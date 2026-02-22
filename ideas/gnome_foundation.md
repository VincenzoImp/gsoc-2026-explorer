# GNOME Foundation — Project Ideas

**Source:** https://gsoc.gnome.org/2026/
**Scraped:** 2026-02-22T23:28:47.593828

---

# GNOME Project ideas for Google Summer of Code 2026

For general information on how to get involved with our project and participate in [Google Summer of Code](https://summerofcode.withgoogle.com/) with [GNOME](https://gnome.org) visit [gsoc.gnome.org](https://gsoc.gnome.org)

This is the list of project ideas that the GNOME community is interested in mentoring. GSoC interns can also propose their very own project ideas. If you are interested in proposing a project idea, please file an issue in our [Internship Project Ideas repository.](https://gitlab.gnome.org/Teams/Engagement/internship-project-ideas)

GSoC contributors proposing something original must engage with the community strongly before or during the application period to get feedback and guidance to improve the proposal.

## Project list

This project will introduce a right-click "Uninstall" option to the GNOME Shell App Grid. Currently, users must open GNOME Software or use the terminal to uninstall apps. This feature will make it simpler and quicker to uninstall apps from the app grid directly.

### Features

#### Right-Click Uninstall

- Users can right-click on an app icon and choose "Uninstall."
- A confirm message will pop up before un-installing the app.
- System apps which cannot be un-installed will provide a warning.

#### Works with Various App Types

- Handles Flatpak, Snap, APT, RPM, and DNF packages.
- Detects automatically how the app was installed and un-installs it properly.

#### Improved User Experience

- No need to open GNOME Software or the terminal.
- Simple and user-friendly with clear messages.

#### Handles Errors Smoothly

- Warns users if an app is important for the system.
- Shows error messages if the uninstall fails.
- Displays a progress notification while uninstalling.

### How It Works

#### Technologies Used

- GNOME Shell & Mutter for UI changes.
- JavaScript & C for coding.
- D-Bus to communicate with system package managers.
- Polkit to handle permissions when needed.

#### Steps

- Modify GNOME Shell to add the right-click uninstall option.
- Connect to package managers to remove apps.
- Handle errors like system app protection.
- Test and improve for smooth performance.

### Requirements

- JavaScript & C (for GNOME Shell development).
- Basic knowledge of package managers (Flatpak, Snap, APT, RPM, DNF).
- Experience with D-Bus and Polkit (for permissions and system communication).

### Communication

GitLab: @AdrianVovk, Matrix Nickname: @adrianvovk:matrix.org

### Project Length: Long (~350 hours)

### Future Improvements

- Drag & Drop Uninstall – Drag app icons to uninstall.
- Remove Multiple Apps at Once – Choose and uninstall numerous apps at once.
- App Usage Insights – Recommend apps to uninstall based on usage.

This project will simplify uninstalling apps in GNOME and make it quicker. Including this feature as part of GNOME Shell will enhance the user experience, making app management easy and effective.

Find out more in [https://gitlab.gnome.org/Teams/internship/project-ideas/-/issues/65](https://gitlab.gnome.org/Teams/internship/project-ideas/-/issues/65)

When a GPU unexpectedly resets, we currently effectively freeze rendering, as the EGL context used for compositing becomes practically defunct, with all allocated GPU memory lost. This can be improved by handling GPU resets by supporting GL_EXT_robustness (https://registry.khronos.org/OpenGL/extensions/EXT/EXT_robustness.txt) by resetting the compositor EGL context/display, re-uploading all GPU resources (Wayland shm client textures, background image, text rendering glyph caches, GNOME Shell chrome textures, ...).

### Requirements

Computer graphics, OpenGL and EGL knowledge, excellent C skills, relevant hardware (AMD)

### Communication

The #gnome-shell IRC/Matrix channel.

### Project Length: TBD

Find out more in [https://gitlab.gnome.org/Teams/internship/project-ideas/-/issues/68](https://gitlab.gnome.org/Teams/internship/project-ideas/-/issues/68)

Implement support in mutter (and its scene graph and compositing library Clutter) for unredirecting client buffers into DRM overlay planes. This involves calculating what elements of the scene graph are candidates for unredirection, without relying on anything other than the scene graph state itself, as well as plumbing the act of unredirecting via the relevant kernel mode setting API, as well as evaluating eventually using libraries such as libliftoffi.

Related GitLab issues: [https://gitlab.gnome.org/GNOME/mutter/-/issues/61](https://gitlab.gnome.org/GNOME/mutter/-/issues/61)

### Requirements

Computer graphics and scene graph knowledge, excellent C skills, KMS/DRM experience

### Communication

The #gnome-shell Matrix channel.

### Project Length: TBD

Find out more in [https://gitlab.gnome.org/Teams/internship/project-ideas/-/issues/10](https://gitlab.gnome.org/Teams/internship/project-ideas/-/issues/10)

This project is about adding support for playing and building vocab-style crossword puzzles to libipuz and GNOME Crosswords. These puzzles are solved similarly to crosswords, but are constructed/built differently. Instead of fitting words to a grid shape, a specific set of words are used and fit together as best as possible. These puzzles are commonly used in schools to teach students vocabulary for a unit or lesson.

[Here's an example (first hit on google)](https://gitlab.gnome.org/-/project/19387/uploads/6601d25ca1bfe86e1c2cf8136e4edd53/image.png) of what these puzzle-types look like.

The project involves adding support to the puzzle kind in libipuz, making sure the player can play it correctly, and then extending the editor to automatically create such puzzles.

The bulk of the internship will be spent writing code to generate compact grids that fit the constraints, adjusting the GTK UI to support it, and making sure it prints correctly.

### Components

### Requirements

Experience with C / GLib-style programming is required for this project.

### Mentors

jblandford, federico

### Project length

Short Project

### Communication

[Matrix (#crosswords:gnome.org)](https://matrix.to/#/#crosswords:gnome.org) and GitLab are best.

Find out more in [https://gitlab.gnome.org/Teams/internship/project-ideas/-/issues/69](https://gitlab.gnome.org/Teams/internship/project-ideas/-/issues/69)
