# Haiku — Project Ideas

**Source:** https://www.haiku-os.org/community/gsoc/2026/ideas
**Scraped:** 2026-02-22T23:28:47.589953

---

# GSoC project ideas

For information about Haiku's participation in GSoC this year, please see [this page](/ideas/haiku/community-gsoc-2026).

Qualifying students can apply for a Haiku project (see the list of *suggested* projects below).
For details about how to apply, please check out [How to Apply for a Haiku Idea](https://www.haiku-os.org/community/gsoc/2026/contributors).

The most successful *Google Summer of Code* projects are often those proposed by the participants themselves.
The following list represents some of our ideas and wishes for the project. However, suggesting your own idea is always encouraged!

Be aware: API design and kernel-related work requires a higher level of skill, and user interface design usually involves a lot more thought than other work. A significantly more convincing proposal is required for tasks involving those. Getting started with the design early (before the application period ends) is recommended, to maximize your chances of being selected, and allow a larger part of the coding period dedicated to coding tasks.

If you find one of the "big"/"hard" ideas interesting, but feel that you cannot complete it within the allotted coding time, feel free to suggest splitting it into smaller parts for your proposal.

Note that Haiku currently [does not accept contributions generated using LLMs](/ideas/haiku/community-organization-policies) due to concerns
over copyright and licensing.

### Project Areas

### Applications

#### Improving Haiku's WebKit video and audio support

##### Idea description

The WebPositive browser bundled with Haiku uses the WebKit engine (shared with Apple's Safari and a few other browsers) to render webpages. This engine allows several parts of the work to be implemented using existing system libraries, allowing better integration with the existing operating system and reduced overhead.

In particular, the audio and video support for Haiku should be implemented by using Haiku's Media Kit, which is a framework designed for such tasks. This would allow WebPositive to play audio and video on websites such as Youtube.

The current experimental code in WebKit uses the Game Kit and only some parts of the Media Kit, it has problems such as blocking the web browser while downloading the video, out of sync audio and video, and unability to seek inside a video.

Other applications such as [StreamRadio](https://github.com/haikuarchives/streamradio) show that it is possible to use the Media Kit with better
buffering techniques to obtain a smoother experience.

- Project size: 175 hours with possible extensions for 350 hours (adding for example fullscreen video support, work on WebRTC, ...)
- Difficulty: medium
- Skill set: userland development, multimedia (audio/video) programming
- Possible mentors/knowledgeable people: PulkoMandy
- Expected outcome: working video and audio support, including fullscreen video, without freeze of the browser during media loading.
[Sourcecode of WebKit ported to Haiku](https://github.com/haiku/haikuwebkit/)

#### Improving Haiku's WebKit2 port

##### Idea description

Haiku has a native WebKit port which uses the "WebKit1" legacy API to interface with WebKit. This API is now deprecated, and the browser should switch to "WebKit2", a new way to interface the browser and its engine. This new system does not run the entire web browser inside a single process, instead, the work is separated between a network process, a web process (doing the page rendering) and the browser itself (which is just a "shell" to render the pages on screen).

Major progress was done during GSoC 2024 to get WebKit2 running on Haiku. This results in a minimal functional browser that can render web pages and process user inputs (mouse and keyboard). However, it is very unstable (many page will trigger assertion failures in WebKit code), and also has glitches and performance issues (scrolling webpages or resizing the browser window results in flickering).

The goal of this project is to stabilize WebKit2 and fix the remaining problems, making it usable for the WebPositive browser that ships with Haiku.

##### Why we need this

The web browser is an important part of the operating system today. It is difficult to attract and retain users if we don't provide a good web browser. The WebKitLegacy API is being deprecated by the developers of WebKit, with all new features (ad blockers, for example) only being available for WebKit2. Migration to the new API will provide a better path for the future of the WebPositive browser.

##### Further reading

- Skill set: userland development, exploring a large code-base (WebCore)
- Possible mentors/knowledgeable people: PulkoMandy
- Project size: 175 or 350 hours, as there is always more things to do in WebKit
- Difficulty: medium
- Expected outcome: stabilization of WebKit2, better web browsing experience with the MiniBrowser test application, more tests passing.
[Sourcecode of WebKit2 work in progress](https://github.com/haiku/haikuwebkit/tree/haiku-webkit2)[GSoC 2024 blog](/ideas/haiku/blog-zardshard)[Opened tickets](https://dev.haiku-os.org/query?status=assigned&status=in-progress&status=new&status=reopened&component=%5EApplications%2FWebPositive)

#### Better XMPP instant messaging client for Haiku

##### Idea description

XMPP is a modern communication protocol for instant messaging. It has open standards and several free software client and server implementations.

Currently, the available native clients for Haiku are quite simple and don't even allow to replace all IRC features. The goal of this project is
to improve [Renga](https://github.com/haikuarchives/renga), one of such clients, to make it possible to migrate Haiku discussion channels over to XMPP instead of IRC.

The main features to implement are more complete support for multi-user chat (in particular, moderation aspects, allowing to manage channel permissions, kick and ban users, etc) as well as any other feature considered useful: message history browsing, message reactions, activity notification, pictures and file sharing, whiteboard collaboration, …

##### Why we need this

Most of Haiku communication channels are currently hosted on IRC servers. IRC is a simple protocol, but it lacks modern features and is difficult to use from unstable connections or using mobile phones. As a result, IRC is less popular, and a part of the Haiku community doesn't use it anymore.

Since we prefer to support open source software and usage of Haiku, XMPP is a good candidate, if we can have a working native client allowing to use it. We don't want people to instead use closed-source software or undocumented protocols.

##### Further reading

- Skill set: userland development, user interface design
- Possible mentors/knowledgeable people: PulkoMandy, waddlesplash, KapiX
- Project size: 175 hours or 350 hours depending on the XMPP feature set being implemented
- Difficulty: easy
- Expected outcome: improvements to the Renga XMPP client, implementing the full MUC (Multi-User Chat) XEP including moderation aspects, and/or a selection of XEPs (XMPP extensions specifications) to be determined during the GSoC application period.
[Renga XMPP client for Haiku](https://pulkomandy.tk/projects/renga)

#### Kexec system feature

Kexec permits booting a new kernel at reboot instead of requiring a full reboot cycle. Adding this would allow Haiku developers to shorten build/test cycles.

Some other operating systems like Linux and FreeBSD implement kexec. The architecture specifics should be separated from the generic kernel code. An implementation for x86_64 would suffice.

- Kernel syscall.
- Skill set: kernel development, userland development, possibly x86 assembly
- Possible mentors/knowledgeable people: korli, ?
[Enhancement ticket](https://dev.haiku-os.org/ticket/5342)- Project size: 350 hours
- Difficulty: medium/hard
- Expected outcome: Ability to warm reboot with another x86_64 kernel.

#### Devices preferences/Hardware manager

Haiku is meant to be an easy to use graphical operating system. It should provide a GUI to manage devices and drivers. This is currently implemented in the "Devices" preferences, however it does little more than listing devices found on the machine.

The goal of this project is to extend the functionality of Devices preferences to make it a more complete and useful tool. This includes working on the following features:

- Telling wether a driver is loaded for a given device and where the matching /dev entry is
- Giving user readable information on the device type and subtype
- Allowing to block/disable the driver for a given device
- Support for bluetooth devices (currently not listed at all)
- Improved support for USB devices, allowing to inspect interface descriptors (like listusb -v), HID report formats, ...)
- Generation of a "compatibility report" to help populate a hardware compatibility database for Haiku

Note that a lot of the work may be in making the required information available from the drivers and existing device management infrastructure, and not just in building the GUI itself.

- Skill set: user interface, kernel and drivers interfacing (ioctl, devfs...)
- Possible mentors: waddlesplash
- Existing code:
["Devices"](https://cgit.haiku-os.org/haiku/tree/src/apps/devices) - Project size: 350 hours
- Difficulty: easy/medium
- Expected outcome: finalized version of Devices application, showing extra information about devices, including but not limited to the driver in use for each device.

#### Other applications

There are many open source 3rd party applications for Haiku that could use improvements. Whether it is resolving bugs, adding features, updating the coding style, updating them to use the Locale and Layout Kits, or anything else imaginable! Writing applications from scratch is also possible.

[Chat-O-Matic](https://github.com/JadedCtrl/Chat-O-Matic)(IM client)[Torrentor!](https://github.com/HaikuArchives/Torrentor)(bittorrent P2P client)[Calendar](https://github.com/HaikuArchives/Calendar)[Many applications at HaikuArchives](https://github.com/HaikuArchives)[Lots of abandonned projects for BeOS looking for a maintainer](http://pulkomandy.tk/~beosarchive/)

- Skill set: userland development, user interface design, exploring an existing code base, others depending on the application retained.
- Possible mentors/knowledgeable people (depends on chosen application): PulkoMandy, Scott McCreary, Sean Healy, waddlesplash, KapiX
- Project size: 175 or 350 hours depending on the application being worked on
- Difficulty: easy, depending on the application chosen
- Expected outcome: new release of the chosen application, including fixes to existing tickets from the respective application bugtracker, and/or other features discussed with mentors and the Haiku community during the application period.

### Drivers

#### eMMC storage support

eMMC is a standard for communicating with flash mass storage chips. It is used in cheap laptops where NVMe or SATA are too complex to implement, and sometimes in non-standard hardware like Chromebooks or ARM single board computers.

Haiku currently cannot use these mass storage devices, which limits hardware compatibility. The basic layers (SDHC controller) are already in place, and can be used to access SD cards. eMMC needs a slightly different initialization sequence, and would also benefit from adding support for "advanced DMA" and other parts of the SDHC controller that allow for high speed operations.

The interface for eMMC devices and for SDHC controllers is well documented and standardized. This means just one driver should be able to cover a lot of hardware. However, there may be some "quirks" (workaround for specific devices) depending on the hardware you will be testing with.

- Requirements:
[Some testing can be done with QEMU](https://www.qemu.org/docs/master/system/devices/emmc.html), so no specific hardware is needed. - Skill set: kernel and driver development, C and C++ development
- Possible mentors: PulkoMandy
- Project size: 175 hours for basic support, extensible for faster DMA usage
- Difficulty: medium
- Expected outcome: Haiku can read (and ideally also write) the user data area on eMMC devices.

#### FreeBSD compatibility layer for FDT attached network devices

Haiku relies on FreeBSD and OpenBSD drivers for most network devices. Currently, this support is
limited to devices attached to the PCI bus, with [work in progress support to also allow usage of
USB network drivers](https://review.haiku-os.org/c/haiku/+/9598).

On many ARM based devices, there is no PCI bus, instead the hardware is mapped at fixed addresses
directly in the system-on-chip, and discovered through a *flattened device tree*, that is,
a data structure describing what type of hardware is available and how to access it.

Haiku already handles parsing of the FDT for its own drivers. However, the compatibility layer used for FreeBSD drivers is restricted to PCI and USB, and cannot currently be used for ARM machines relying on FDT. This is especially annoying as these machines tend to use a wide variety of implementations, which means a lot of drivers would benefit from this support.

The goal of this project is to adjust the FreeBSD compatibility layer for at least one such driver.

- Requirements: access to a device with an FDT mapped Ethernet interface, preferrably already supported by FreeBSD
- Skill set: kernel and driver development, C and C++ development
- Possible mentors: PulkoMandy
- Project size: 175 hours for basic support, extensible for porting more drivers, finalization of USB compatibility layer support, or other tasks related to ARM support
- Difficulty: medium
- Expected outcome: Haiku can use an FDT network interface (tested for example by
[network booting](/ideas/haiku/guides-network_booting)).

#### Universal Flash Storage support

Haiku lacks a driver to support the [Universal Flash Storage Host Controller Interface (UFSHCI)](https://www.jedec.org/standards-documents/docs/jesd223f).
The goal of this project is to add a driver between the PCIe UFSHCI device and the SCSI bus interface.

- Requirements:
[Some testing can be done with QEMU](https://github.com/qemu/qemu/blob/master/hw/ufs/ufs.c) - Skill set: kernel and driver development, C and C++ development
- Project size: 175 hours
- Difficulty: medium
- Possible mentors: korli

#### GPU acceleration support

Haiku does not currently support GPU acceleration, for 3D or otherwise. Reusing most of the DRM drivers from Linux, and Mesa's Gallium userspace components, the goal of this project is to enable the use of GPU-accelerated OpenGL, and eventually also OpenCL and Vulkan.

Haiku's current video drivers are mostly modesetting-only, and split in two parts: the driver itself, which is quite minimal and only provides low level access to the video card, and the "accelerant", which runs inside app_server and communicates with the driver in order to configure the card and use its features.

Porting the DRM drivers from Linux will be a rather daunting task, as they use a large subset of the Linux kernel APIs. It may be possible to reuse OpenBSD's or DragonFlyBSD's work rather than writing our own Linux API compatibilty layer; more investigation is needed here.

- Skill set: kernel and driver development, Mesa graphics stack
- Possible mentors/knowledgeable people: waddlesplash
- Project size: 350 hours
- Difficulty: hard
- Expected outcome: proof of concept running an accelerated 3D rendering application based on the ported driver.

### Kernel

#### Improving the btrfs filesystem

Haiku has great support for its own file system, but most others are only available read-only. It is way better for interoperability with other systems to be able to write to these disks from Haiku.

The goal of this project is to complete the btrfs filesystem, to allow it to write btrfs volumes (reading works already). During GSoC 2017 and 2018, students got as far as creating directories, but it is not possible yet to write files. The first part of the work is to review the existing code, and report on the current status and the work needed to get everything in place.

After completion of this project, it should be possible to read and write files to btrfs volumes, making sure they are interoperable with Linux (mount without errors, file data is accessible, fsck detects no problems). Stress-testing should also be performed using bonnie++, and other test suites may also be used.

- Skill set: kernel, and driver development
- Possible mentors/knowledgeable people: PulkoMandy, Sean Healy, Hy Che
[Sourcecode](https://git.haiku-os.org/haiku/tree/src/add-ons/kernel/file_systems/btrfs)[GSoC 2017 log](/ideas/haiku/blog-hyche)[GSoC 2018 log](/ideas/haiku/blog-brj)[Existing btrfs patches to start from](https://review.haiku-os.org/q/status:open+btrfs)- Project size: 175 or 350 hours depending on the number of features planned to implement
- Difficulty: medium
- Expected outcome: write support for the btrfs filesystem.

#### Adding write support for more filesystems

##### Idea description

Some filesystems can only be read, but not written, from Haiku. The goal of this idea is to add write support for one of these filesystems (of your choice, from the list below).

[XFS](http://en.wikipedia.org/wiki/Xfs)([Development community](http://xfs.org/index.php/Main_Page),[homepage](http://oss.sgi.com/projects/xfs/index.html)) is a filesystem originally developed for the IRIX operating system. Today it is commonly used by Haiku developers who build Haiku from Linux, because of its better support for extended filesystem attributes (unlike ext4). The read-only support is generally complete but does not use any caching yet. Adjusting the filesystem to use the block and file caches would be a good way to start this project.[UFS2](http://en.wikipedia.org/wiki/Unix_File_System)([FreeBSD implementation](https://github.com/freebsd/freebsd/tree/master/sys/ufs/ufs),[u2fstools for windows](http://sourceforge.net/p/ufs2tools/code/HEAD/tree/trunk/ufs2tools/)) is the default filesystem in FreeBSD, commonly used by some Haiku developers as well. It is closely based on the original Unix filesystem, which is implemented in many other operating system. The original design is quite simple, however the different implementations in various systems make it a bit more complex to handle all cases. Focusing specifically on the FreeBSD variant is acceptable for this project if needed. In its current state, the UFS2 driver works in fs_shell but crashes when used as an actual filesystem in Haiku, investigating and fixing this problem would be a good way to start this project.- ExFAT is an improved version of Microsoft's FAT filesystem. It is designed for removable drives and used on large size USB thumb drives and SD cards. There is not yet any write support in Haiku's ExFAT driver.

##### Why we need this

In its current state, Haiku is rarely used as the single operating system on a computer. It is common to dual boot it with other systems such as Linux or FreeBSD. In this setup, it is very convenient when each system can access and modify the other's files. Disk partitions and data can then be shared more easily.

##### Further details

- Skill set: data structures, C++
- Possible mentors/knowledgeable people: PulkoMandy, waddlesplash
- Project size: 175 or 350 hours (in 175 hours only partial progress will be possible)
- Difficulty: medium
- Expected outcome: write support for the selected filesystem

#### Filesystems benchmarking and stress-test

Some of the filesystems (or specific features of them) in Haiku are relatively new, and not considered perfectly tested and stable yet. The goal of this project is to define a procedure for testing the filesystems and identifying bugs (especially leading to on-disk data corruption) and performance bottlenecks.

Tools like [bonnie++](https://en.wikipedia.org/wiki/Bonnie%2B%2B), [xfstests](https://github.com/kdave/xfstests),
and the existing tests in src/tests/add-ons/kernel/file_systems in Haiku sources should be explored to determine their respective usefulness.
Then, an automated way to run the tests should be defined (unit tests, integration tests on a running system, etc.)

Then, the filesystems should be modified to fix the performance problems and/or bugs that were found in the process.

- Skill set: C++ development, testing
- Possible mentors/knowledgeable people: PulkoMandy
- Project size: 175 hours
- Difficulty: easy
- Expected outcome: benchmark results, analysis of bottlenecks, implementation of changes to improve the filesystem and related code (VFS, caches, ...) in Haiku.

### Network

#### Bluetooth Stack Improvements

Haiku's Bluetooth stack implements a basic subset of general Bluetooth functionality. This functionality needs to be completed and Bluetooth 2.X and later possibilities explored. This task involves investigating the current state of the Bluetooth code, improving the existing code on newer devices (pairing, etc), and improving the stack to make it more useful by implementing driver(s) for Bluetooth device(s) of your choice (file transfers, audio, HID, networking, etc).

- Requirements: Bluetooth-enabled Haiku system
- Skill set: C++, kernel development, userland development, global bluetooth stack knowledge (optional)
- Possible mentors/knowledgeable people: waddlesplash
- Project size: 175 hours or 350 hours (depending on how much of the stack is added)
- Difficulty: medium
- Expected outcome: the Bluetooth stack can be used for more than just pairing devices. For example, bluetooth audio or bluetooth HID drivers can be used.

### User Interface

#### Modular edit view (BIG)

The current solution for text editing in Haiku is the BTextView. It is a rather simple view providing basic text editing features and limited styling. This is, however, not powerful enough for most serious uses. The goal of this project is to design a complete replacement for BTextView, which should be designed to cover more use cases.

The edit view design should be modular and extensible to make it easy to implement e.g. following features:

- Advanced text decorations and formatting: wavy underlines, strikethrough, exponents, ...
- spell checker, line numbers, ruler
- working on an input stream rather than on an input file, e.g. to be able to open files ~100Mb without loading them into memory in one go
- Including pictures in the text flow
- Automatic line breaks using locale specific rules (insertion of word breaks, handling of language with no whitespace between words)
- Ability to load and save data in different formats such as RTF, ODT, ... (using the Translation Kit)

##### Existing work

The HaikuDepot application includes [preliminary work on a rich text view](https://cgit.haiku-os.org/haiku/tree/src/apps/haikudepot/textview),
which it uses to provide the description of packages. This could be used as a
starting point for this work.

- Skill set: C++, API design, UI development
- Possible mentors: waddlesplash, Sean Healy, scottmc, KapiX
- Project size: 350 hours (175 hours if working only on a much smaller subset)
- Difficulty: hard
- The edit view is more widely available for Haiku applications, and implement a selection of the items outlined in the list above (to be selected during the application period after discussion with the mentors and community)

### Other

#### Improvements to Haiku-format coding style checker

Haiku has its own [coding guidelines](/ideas/haiku/development-coding-guidelines)
which describe how the code should be formatted. There is [a tool](https://github.com/owenca/haiku-format) (based on clang-format) for reformatting
or checking if code follows these guidelines, used in the continuous integration and code review process.

However, the tool does not fully implement the coding style and currently suggests many changes that are, in fact, not correct. The goal of this project is to improve the tool to get it closer to Haiku's code style.

- Skill set: REST APIs, code formatting tools
- Possible mentors: PulkoMandy, KapiX

#### Improve automated test coverage and system documentation

##### Idea description

Haiku's regular CI testing is limited to checking whether the code builds, but not whether it works as expected. There is an existing test suite in Haiku repository but its coverage is limited. Some tests have been created along with new features over the years, but this has been an exception rather than a rule.

##### Why we need this

Having automated tests will reduce amount of regressions, simplifying release process and improving developer confidence when refactoring code.

##### Further details

First part of this project is to identify missing coverage, develop a plan to fill the test gaps, and/or propose tests that would test functionality in new ways.

The goal is to implement missing tests, improve existing ones if necessary, ensure they are stable and included in regular testing cycles.

Stretch goal is to develop a plan and integrate code coverage tools.

- Skill set: C++, userland development, unit testing
- Possible mentors: KapiX

#### Multiple monitors output in app_server

app_server is Haiku's graphics server and the equivalent of X11 or Wayland on other UNIX systems. It currently supports only one video output, but should be able to do more.

While the API already allows this for the most part (with the BScreen class), there is no actual implementation behind it and parts of the code assume only a single screen.

Some drivers implement minimal support for multiple displays, but not all of them. This task may involve updating the video drivers to handle multiple monitors correctly.

- Skill set: C++, graphics development
- Possible mentors/knowledgeable people: PulkoMandy, KapiX
- Project size: 350 hours
- Difficulty: medium/hard
- Expected outcome: implementation of the needed changes in app_server APIs and accelerant APIs to properly support multiple displays. Reference implementation either in test_app_server or in one of the existing graphics drivers on real or emulated hardware.

#### Complex font rendering in app_server

app_server is the graphics server in Haiku. It handles the rendering and display of application windows, desktop, and everything that is shown on screen.

Freetype (in combination with agg) is used to render text. While it provides good results for latin and cyrillic alphabets, Freetype is not enough on its own to properly render other scripts with more complex rules, such as Devanagari or Arabic.

The goal of this task is to integrate Harfbuzz into app_server, so that the complex rules for text rendering are properly applied. This would allow rendering of complex languages as mentioned above, as well as mixing different languages (picking appropriate fonts automatically).

This task can be further extended with investigations of API changes required in the interface kit (and in particular BView and BFont) to properly handle right to left text.

- Skill set: C++
- Possible mentors: PulkoMandy
- Project size: 175 hours
- Difficulty: easy/medium
- Expected outcome: working font rendering for arabic or devanagari or other script with "complex" rendering rules.
