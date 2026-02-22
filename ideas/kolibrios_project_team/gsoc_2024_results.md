# GSoC 2024 Results

**Parent:** KolibriOS Project Team — Project Ideas
**Source:** https://wiki.kolibrios.org/wiki/GSoC_2024_Results
**Scraped:** 2026-02-22T23:28:47.589094

---

# GSoC 2024 Results

[Jump to navigation](https://wiki.kolibrios.org#mw-head)

[Jump to search](https://wiki.kolibrios.org#searchInput)

## Introduction

In 2024, KolibriOS participated in [Google Summer of Code](https://summerofcode.withgoogle.com/) for the 3rd time, after 2014 and 2016 [[1]](https://summerofcode.withgoogle.com/programs/2024/organizations/kolibrios-project-team).

This page presents the results of the participation, including implemented [ideas](https://wiki.kolibrios.org/wiki/Ideas_Page) and comments from the participants.

## Completed Ideas

In result of preliminary selection, two task slots were allocated by Google for KolibriOS:

by arnavbhatt288[SDL2 library port](https://summerofcode.withgoogle.com/programs/2024/projects/U7cf4oma)by ramenu[NVMe driver implementation](https://summerofcode.withgoogle.com/programs/2024/projects/W1VYwf7j)

Both task were successfully completed by participants and contributed to KolibriOS.

### SDL2 library port

**Why it is important for KolibriOS**

Having support for SDL2 in KolibriOS will not only allow developers to develop new applications using the updated functionality of the library, but also to port a huge number of existing open source programs (mostly emulators and games) from other platforms, as SDL2 is often used to implement frontend/graphics in such applications.

**Test task**

As a test task, arnavbhatt288 fixed a bug in PokeMini emulator for KolibriOS, which is written in C using SDL which made working with it close to the main task [[2]](https://github.com/KolibriOS/kolibrios/issues/18).

**Implementation status**

- Primary goal: Make a working port of SDL2.
- Was successfully implemented during the course of GSoC'24, by porting SDL2 (version 2.30.6) library to KolibriOS.

- Additional goal: Port additional SDL2 libraries: SDL2_image, SDL2_mixer, SDL2_ttf, etc.
- Was successfully implemented during the course of GSoC'24, by porting SDL_image (version 2.8.2), SDL_mixer (2.8.0) and SDL_ttf (2.22.0) additional libraries to KolibriOS.

- Extra goal: Port SDL 1.2 compatibility layer to run old apps on new version of library.
- Wasn't implemented during the course of GSoC'24.


**Result**

With both basic libraries and all main additional libraries being ported, it is now possible to fast develop applications with advanced frontend for KolibriOS, as well as port many open-source programs, that are based on SDL2.

As an example, during the course of GSoC'24 arnavbhatt288 ported a [LakeSnes](https://github.com/dinkc64/LakeSnes) SNES emulator, as demonstration of library functionality and replacement for current ZSNES emulator, that has some bugs [[3]](https://github.com/KolibriOS/kolibrios/issues/12).

**Contributor's comment**

> What were your impressions of our project? The project seemed interesting to dive into as though I ported software/libraries to different platforms earlier in the past, I never did one on a particularly niche platform. Learning about that KolibriOS has libc, my interest for this project grew further. > How did working process go? It went quite smooth, I faced some setbacks here and there, but I managed to overcome it. > What have you liked and disliked about this project? What I liked: Simplicity of the OS, the fact that it has a libc support (quite a feat for a niche OS), well-made toolchain and simple syscalls What I disliked: Lack of good documentation. While the source code has some documentation about stuffs like syscalls, they weren't well detailed.

**Source code**

### NVMe driver implementation

**Why it is important for KolibriOS**

In recent years, the use of NVMe drives has become increasingly popular in personal computers, and the implementation of their support is very important in terms of KolibriOS compatibility with modern hardware and keeping the system up-to-date.

**Test task**

As a test task, ramenu started implementation of the NVMe driver itself and worked on device initialization.

**Implementation status**

- Primary goal: Write basic NVMe device driver to support NVMe SSD.
- Was successfully implemented during the course of GSoC'24, by writing NVMe driver from scratch.

- Additional goal: Add support of namespaces.
- Was successfully implemented during the course of GSoC'24, as part of written from scratch driver.


**Result**

Written driver supports all basic and some additional NVMe functions, as well as all controllers versions, which allows usage of NVMe drives in KolibriOS.

Also, ramenu intends to continue working on driver even after the end of GSoC'24, fixing possible bugs and adding support for additional features.

**Contributor's comment**

> Would you mind giving a little comment on your participation in GSoC 2024 as a KolibriOS contributor? What were your impressions of our project, how did it go, maybe things you liked and disliked? As for how the project went, it was fantastic! And I really enjoyed working on it. The entire community is very competent, so it taught me some humility. In the beginning I was honestly not completely sure if I could finish the task as I found the NVMe spec quite intimidating. Up until this point, my experience with operating systems relied exclusively on OSDev tutorials and articles already written with code samples in a nice condensed format. Luckily, @punk_joker was able to help me here, and his guidance was extremely crucial for getting the driver in the state it is today (as well as Burer's extensive testing). In the start, I wasn't sure what I should focus on and what I should implement, because there are too many features in the spec. If I had wasted time implementing an unnecessary feature, then it could have been costly. But honestly, I feel very much indebted to the entire community, because the amount of knowledge I've gained from now relying on specifications and manuals and assembly is a lot, and has been extremely useful for my own personal projects. One part that could be improved is the fragmented communication method. A lot of the time, if I wanted to talk to developer X, I have to ask developer Y to contact X for me because I'm not sure how to contact them myself. I'm aware that there is a Telegram and Discord, which I have not joined, so maybe that's where communication happens. But nonetheless, maybe in the future contributors could be asked to join whatever platform the developers prefer (only if they desire, again, just to serve as a reference that this is where most of the developers are, in case they want to reach out), and of course still leave the option for private mentor/student conversations somewhere else.

**Source code**

## Results

As a result of GSoC'24 two important features were implemented in KolibriOS:

- Support of SDL2 library and it's additional libraries.
- Support of NVMe controllers with additional features.

Thus, thanks to the active work of the participants, the system gained new opportunities for application development and hardware support, which made it much more functional for both developers and ordinary users.
