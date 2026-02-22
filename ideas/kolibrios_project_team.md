# KolibriOS Project Team — Project Ideas

**Source:** https://wiki.kolibrios.org/wiki/Ideas_Page
**Scraped:** 2026-02-22T23:28:47.588697

---

# Ideas Page

[Jump to navigation](https://wiki.kolibrios.org#mw-head)

[Jump to search](https://wiki.kolibrios.org#searchInput)

## Introduction

This is our ideas page for new developers who want to participate in the Google Summer of Code event by contributing to KolibriOS. It also contains a description of the process and requirements to participate.

A general information about Google Summer of Code can be found here: [Google Summer of Code](https://summerofcode.withgoogle.com/)

## Google Summer of Code'26 Contributor Requirements

Prospective contributors are required to register [on our developers forum](https://board.kolibrios.org) and submit a small bugfix / improvement [to our Git](/ideas/kolibrios-project-team/get_source_code) in order for their application to be considered. Examples of such tasks can be obtained by asking on the developers forum or on our IRC channel (#kolibrios @ irc.libera.chat), [Discord server](https://discord.com/invite/FeB2NvE6bF) or [Telegram chat](https://t.me/kolibri_os). This requirement is only to show us that you are able to work with [our Git](/ideas/kolibrios-project-team/get_source_code) and interact with our developers if you are selected.

**This task has to be completed before contributor proposal deadline (8 April 18:00 UTC).**

In addition, contributors need to answer the following questions when applying:

- Full Name (First + Last Name).
- E-mail address.
- Nickname you plan to use on our forums, Git repository or IRC chat.
- Age.
- Country + city of residence (Russia and Belarus residence are not allowed according to GSoC terms)
- Human languages you speak (write all languages and knowledge level - basic/intermediate/expert/mother tongue).
- Name of college or university you are accepted into or enrolled in + link to their website (if applicable).
- Name of program (or faculty, or department) in that college/university you are accepted into or enrolled in (if applicable).
- Your current timezone in UTC/GMT terms (for example, Paris is UTC/GMT +1 hours right now).
- Have you been involved with any open-source project in the past? If yes, which one, and what have you done for that project?
- Code samples - please provide links to code that you have written. It can be your high school project, contribution to open-source organization, your college/university task or anything like that.
- The task you are willing to work on from our list of Summer of Code 2026 ideas (or suggest your own idea, if you don't like any of the proposed ideas).
- What other time commitments, such as school work, another job, planned vacation, etc., will you have between May 8 and November 19?

## Organization

You can find the organizers at our forum: [https://board.kolibrios.org](https://board.kolibrios.org)

Name
|
Nickname
|
Role
|
| Ivan Baravy |
|

[hidnplayr](/ideas/kolibrios-project-team/user-hidnplayr)[Punk_Joker](/ideas/kolibrios-project-team/user-punk_joker)[Leency](/ideas/kolibrios-project-team/user-leency)## Ideas

| Idea Name | Area | Programming Language | Mentors |
|---|---|---|---|
|

[Widget toolkit](https://wiki.kolibrios.org#Widget_toolkit)[Finish Mbed TLS port](https://wiki.kolibrios.org#Finish_Mbed_TLS_port)[Port FLTK](https://wiki.kolibrios.org#Port_FLTK)[FASMG port](https://wiki.kolibrios.org#FASMG_port)[Unicode library](https://wiki.kolibrios.org#Unicode_library)[Virt-IO driver](https://wiki.kolibrios.org#Virt-IO_driver)[Loop device driver](https://wiki.kolibrios.org#Loop_device_driver)[RSS/Atom news reader](https://wiki.kolibrios.org#RSS/Atom_news_reader)[Add HTML forms to WebView](https://wiki.kolibrios.org#Add_HTML_forms_to_WebView)[J2ME Emulator](https://wiki.kolibrios.org#J2ME_Emulator)[Rust library development for KolibriOS](https://wiki.kolibrios.org#Rust_library_development_for_KolibriOS)[WebAssembly runtime development](https://wiki.kolibrios.org#WebAssembly_runtime_development)[MIDI subsystem implementation](https://wiki.kolibrios.org#MIDI_subsystem_implementation)[Git client development](https://wiki.kolibrios.org#Git_client_development)### File system improvement

**General Description**

KolibriOS has already implemented support for many file systems, both write and read, but at the same time support for some systems leaves a lot to be desired and opens up a vast scope for work.

**What it gives us**

Support for more file systems, particularly write support, will greatly expand the functionality of KolibriOS, especially when working with files on third-party drives.

**Other information**

- Goals:
- Primary: Add write support for ext4 file system (ext4 reading and ext2 writing are already supported).
- Additional: Improve write support for NTFS file system.

- Language:
**Assembler/FASM**. - Difficulty:
**Intermediate**, you need to be familiar with how file systems work in general, and writing drivers. - Time/Size:
**175 hours**. - Links:

### Widget toolkit expansion

**General Description**

At the moment KolibriOS has its own library (box_lib) for implementing various GUI widgets (input fields, checkboxes, scrolls, etc.). However, its functionality is far from complete, and its extension would be very useful for further application development.

**What it gives us**

Extended functionality of the library would help developers in the future to create applications with more complex interface, spending less effort on it, as well as to unify interface components in existing applications.

**Other information**

- Goals:
- Primary: Extend box_lib (a set of separate widgets) to create a full-featured widget toolkit, design it's architecture and implement focus handling, callbacks and other core ideas.
- Additional: Integrate created box_lib widgets to the C-framework, extend framework with font handling, layout manager

- Language:
**Assembler/FASM, C**(Framework). - Difficulty:
**Intermediate**, you need to be familiar with library development and FASM Assembler. - Time/Size:
**175 hours**. - Links:

### Finish Mbed TLS port

**General Description**

Mbed TLS is an implementation of the TLS and SSL protocols and associated cryptographic algorithms and support code that aims to be "easy to understand, use, integrate and extend".

**What it gives us**

The implementation of MbedTLS support will significantly expand the capabilities of the KolibriOS networking stack and allow it to be used in more networking scenarios, for example, HTTPS support.

**Other information**

- Goals:
- Primary: Finish MbedTLS port (headers for FASM, get ceritificates working) (
[TODOs](https://board.kolibrios.org/viewtopic.php?p=76983#p76983)). - Additional: Update HTTP library (written in FASM) to support HTTPS by using mbedtls.obj.

- Primary: Finish MbedTLS port (headers for FASM, get ceritificates working) (
- Language:
**C, Assembler/FASM**. - Difficulty:
**Intermediate**, you need to be familiar with library porting. - Time/Size:
**175 hours**. - Links:

### FLTK Port

**General Description**

FLTK, or Fast Light Toolkit, is a cross-platform GUI toolkit. It is designed to provide modern GUI functionality without overkill and supports 3D graphics via OpenGL and native GLUT emulation.

**What it gives us**

FLTK provides a wide and convenient enough choice of plugins to implement a complex GUI, and is also cross-platform, and therefore its support in KolibriOS will make it easier to write applications. Also, compared to other UI libraries, FLTK uses a lighter design and is limited to GUI functionality.

**Other information**

- Goals:
- Primary: Make a working port of FLTK widget library and add it to the automatic build system.
- Additional: Port Scintilla source code editing component (minimum working version).

- Language:
**C++, C--, Assembler/FASM** - Difficulty:
**Intermediate**, you need to be familiar with library porting. - Time/Size:
**175 hours**. - Links:

### FASMG port

**General Description**

In 2018 Tomasz Gryshtar (creator of FASM) introduced FASMG, a new assembler engine with more advanced features for simplified writing of complex code. It is quite a powerful and useful tool, and so it would be nice to support its new syntax in KolibriOS.

**What it gives us**

The kernel, drivers and many programs in KolibriOS are written exactly in FASM Assembler, and porting FASMG would make life easier for developers who work on improving the OS functionality.

**Other information**

- Goals:
- Primary: Write FASMG application like FASM one. Port standard KolibriOS macros to FASMG syntax.
- Additional: Implement macros for compatibility with FASM.

- Language:
**Assembler/FASM/FASMG** - Difficulty:
**Intermediate**, you need to be familiar with FASM Assembly language. - Time/Size:
**175 hours**. - Links:

### Unicode library

**General Description**

Unicode is a character encoding standard that includes characters from almost all written languages of the world. The standard is currently prevalent on the Internet and is also frequently used in modern operating systems. The main advantage of Unicode is that it supports a huge number of characters, which allows it to be used for encoding and storing almost any textual information.

**What it gives us**

Unicode is a large and complex standard, nevertheless, modern OS should provide libraries with Unicode related routines like NFC, NFD, sorting, comparing, etc. Support for this standard in KolibriOS would greatly increase its compatibility with various data sources, and make new application scenarios available.

**Other information**

- Goals:
- Primary: Write a tiny Unicode library with core Unicode algorithms and example application.
- Additional: Update existing applications to use the new library.

- Language:
**Assembler/FASM** - Difficulty:
**Intermediate**, you need to be familiar with writing libraries and FASM Assembler language. - Time/Size:
**175 hours**. - Links:

### VirtIO driver

**General Description**

VirtIO is a virtualization standard for network and disk device drivers where just the guest's device driver "knows" it is running in a virtual environment, and cooperates with the hypervisor. This enables guests to get high performance network and disk operations, and gives most of the performance benefits of paravirtualization.

**What it gives us**

Because there is no easy way to automatically install KolibriOS on a hard disk, it is often used specifically in a virtualized environment, and therefore improving support and device performance in this situation would be extremely beneficial to it.

**Other information**

- Goals:
- Primary: Write kernel driver for any VirtIO device, for example - Ethernet card.
- Additional: Also write drivers for any another VirtIO devices.

- Language:
**Assembler/FASM** - Difficulty:
**Intermediate**, you need to be familiar with writing drivers and FASM Assembly language. - Time/Size:
**175 hours**. - Links:

### Loop device driver

**General Description**

Loop device, vnd (vnode disk), or lofi (loop file interface) is a pseudo-device that makes a computer file accessible as a block device. After mounting a file that holds a file system, the files in that system can be accessed through the usual file system interface of the operating system, without any need for special functionality, such as reading and writing to ISO images, in applications.

**What it gives us**

Loop device drivers allow for mounting a file that holds a file system, making the files within that file system accessible. It also provides a block device on top of a file (or another block device, optionally with remapping). Lastly, if the file contains an encrypted file system, the loop device can be the decrypted version of the original encrypted file and can therefore be mounted as if it were a normal file system.

**Other information**

- Goals:
- Primary: Write loop device driver and example application to manage loop devices.
- Additional: Prepare a set of disk images to be used in filesystem unit tests.

- Language:
**Assembler/FASM**. - Difficulty:
**Intermediate**, you need to be familiar with writing drivers and FASM Assembly language. - Time/Size:
**175 hours**. - Links:

### RSS/Atom news reader

**General Description**

RSS and Atom are web feeds that allow users and applications to access updates of websites in a standardized, computer-readable format. For the average user, it can be used primarily as a news/update feed, where the user can subscribe to channels of interest and receive news or other updates from different sources in one place. They are based on XML and can easily be processed using AsmXml library. User application for reading RSS/Atom feeds would be a good addition to usability of KolibriOS, as it will allow users to read news feeds from different sources without need to manually open news websites.

**What it gives us**

RSS/Atom feed can be a great addition to the KolibriOS functionality, as it allows users to conveniently receive updates from different sources, including even on very weak devices, where opening the source of interest in the browser is impossible or problematic.

**Other information**

- Goals:
- Primary: Write RSS news reader as a standalone KolibriOS application.
- Additional: Also add Atom standart support to the app.

- Language: Any, but
**Assembly/FASM**is preferable. - Difficulty:
**Easy**, you need to be familiar with XML processing and HTTP requests, as well as general app development for KolibriOS. - Time/Size:
**90 hours**. - Links:

### Add HTML forms support to WebView

**General Description**

Despite supporting many basic HTML features, the WebView browser does not currently support HTML forms (<form>, <input>, etc.). This makes its use extremely limited and prevents it from utilizing the functionality of many popular sites. Therefore, it would be great to implement this functionality in WebView.

**What it gives us**

Because of the lack of form support, WebView can't even use search engines directly (currently only indirect use of Google in the address bar is possible). This alone would be a great addition to its capabilities and would make its use much more convenient and intuitive. In addition, forms could also be used on sites like online libraries or forums, thus giving KolibriOS users a more complete access to the Internet.

**Other information**

- Goals:
- Primary: Add support for <form>, <input> tags for types that was prior to HTML5.
- Additional: Add input types that was introduced in HTML5.

- Language:
**C--**. - Difficulty:
**Easy**, you need to be familiar with HTML parsing and web requests. - Time/Size:
**90 hours**. - Links:

### J2ME Emulator

**General Description**

J2ME (Java Platform, Micro Edition) is a version of the Java platform for devices with limited resources, such as cell phones, pocket computers, etc. It was especially popular in the 00s, when most mobile phones ran on it. Accordingly, a large number of software for this platform was created at that time, and it would be quite nice to have its support in KolibriOS.

**What it gives us**

There are already quite a lot of emulators for various retro platforms, which makes it possible to use it, including for retro gaming. Therefore, support for another popular platform will certainly not hurt, especially since in addition to a lot of great games for J2ME also released other programs that can be useful.

**Other information**

- Goals:
- Primary: Port JVM and java.microedition.* runtime.
- Additional: Make it run most of popular J2ME games.

- Languages:
**C**,**Java**. - Difficulty:
**Hard**, you need to be familiar with emulators porting and Java Runtime Enviroment. - Time/Size:
**350 hours**. - Links:

### Rust library development for KolibriOS

**General Description**

At the moment, the Rust library for KolibriOS is in the early stages of development - it doesn't support all system functions, and it doesn't know how to work with system libraries. You can do a great thing, and help in the design and development of this library!

**What it gives us**

Rust is a modern programming language that has been actively gaining popularity in recent years, and the number of its users is growing. In addition, it is positioned as fast and compact, which fits perfectly with the KolibriOS ideology. Therefore, it would be very good to have its support as another tool for potential developers.

**Other information**

- Goals:
- Primary: Implement other system functions support. Make wrappers for DLL's.

- Languages:
**Rust**,**Assembly/FASM (optional)**. - Difficulty:
**Intermediate**, you need to be familiar with Rust development. - Time/Size:
**350 hours**. - Links:
- Working repository:

### WebAssembly runtime development

**General Description**

WebAssembly is a low-level assembly-like language with a compact binary format that runs with near-native performance and provides languages such as C/C++, C# and Rust with a compilation target so that they can run on the web. A proper runtime will allow running such code in KolibriOS without need of massive rewrite and adaptation.

**What it gives us**

WebAssembly is a unique tool, that combines the performance of low-level languages and web portability, as it allows running tons of programs written in multiple languages in one single runtime. Thus, it will be a great addition for such a system as KolibriOS, where performance and compact size are very important.

**Other information**

- Goals:
- Primary: Implement minimalistic WASM runtime.

- Languages:
**Assembly/FASM**. - Difficulty:
**Intermediate**, you need to be familiar with WASM and runtime technologies. - Time/Size:
**175 hours**. - Links:

### MIDI subsystem implementation

**General Description**

Musical Instrument Digital Interface (MIDI) is a standard to transmit and store music, originally designed for digital music synthesizers. MIDI does not transmit recorded sounds. Instead, it includes musical notes, timings and pitch information, which the receiving device uses to play music from its own sound library.

**What it gives us**

Previously, KolibriOS had limited support of MIDI, allowing to play mono-tone compositions through the system speaker. A new proper subsystem with the possibility of playing sound through dynamics and having multiple instrument support would greatly increase the possibilities of KolibriOS as a multimedia system.

**Other information**

- Goals:
- Primary: Implement a MIDI-to-audio synthesizer (like fluidsynth, for example).
- Secondary: Develop a proper compositions player with support for MIDI files.

- Languages: Any, but
**Assembly/FASM**is preferable. - Difficulty:
**Intermediate**, you need to be familiar with MIDI format, as well as general audio signal processing. - Time/Size:
**175 hours**. - Links:

### Git client development

**General Description**

Git is a free and open-source version control system used to handle small to very large projects efficiently. Git is used to track changes in the source code, enabling multiple developers to work together on non-linear development.

**What it gives us**

Git is the most popular version control system, and it is also the version control system used in KolibriOS development. Thus, an in-system Git client will not only make the system more attractive for tech-enthusiasts, but also make development of KolibriOS and software for it much easier.

**Other information**

- Goals:
- Primary: Implement a working Git client with support for main version control functionality.
- Secondary: Add functionality of SSH authorization to work with protected repositories.

- Languages: Any, but
**Assembly/FASM**is preferable. - Difficulty:
**Intermediate**, you need to be familiar with web-protocols, such as HTTP and SSH, as well as general software development. - Time/Size:
**175 hours**. - Links:

## Completed Ideas

Below are examples of ideas successfully completed during KolibriOS's previous participation in GSoC.

### GSoC 2024

[SDL2 library port](https://summerofcode.withgoogle.com/programs/2024/projects/U7cf4oma)was succesfully completed by[arnavbhatt288](https://board.kolibrios.org/memberlist.php?mode=viewprofile&u=14954).[NVMe driver implementation](https://summerofcode.withgoogle.com/programs/2024/projects/W1VYwf7j)was succesfully completed by[ramenu](https://board.kolibrios.org/memberlist.php?mode=viewprofile&u=15061).

For more information see [GSoC 2024 Results](/ideas/kolibrios-project-team/gsoc_2024_results).
KolibriOS Project Team at [GSOC'2024](https://summerofcode.withgoogle.com/archive/2024/organizations/kolibrios-project-team).

### GSoC 2016

[Bit torrent client](https://summerofcode.withgoogle.com/archive/2016/projects/6132971438342144)was successfully completed by[Utsav_Chokshi](http://board.kolibrios.org/memberlist.php?mode=viewprofile&u=6843).[GUI-based FTP client](https://summerofcode.withgoogle.com/archive/2016/projects/6252078934523904)was successfully completed by[nisargshah95](http://board.kolibrios.org/memberlist.php?mode=viewprofile&u=6844).[C layer](https://summerofcode.withgoogle.com/archive/2016/projects/6693475676323840)was successfully completed by[punk_joker](https://board.kolibrios.org/memberlist.php?mode=viewprofile&u=4485).[TLS/SSL library](https://summerofcode.withgoogle.com/archive/2016/projects/4568246669803520)was successfully completed by[DenisKarpenko](https://board.kolibrios.org/memberlist.php?mode=viewprofile&u=6848).

KolibriOS Project Team at [GSOC'2016](https://summerofcode.withgoogle.com/archive/2016/organizations/5678701068943360).

### GSoC 2014

[FT232 chip driver for KolibriOS](https://www.google-melange.com/archive/gsoc/2014/orgs/kolibrios/projects/gtament.html)was successfully completed by[gtament](https://board.kolibrios.org/memberlist.php?mode=viewprofile&u=5793).[Port NetSurf and Improve Build System](https://www.google-melange.com/archive/gsoc/2014/orgs/kolibrios/projects/ashmew2.html)was successfully completed by[ashmew2](https://board.kolibrios.org/memberlist.php?mode=viewprofile&u=6211).

KolibriOS Project Team at [GSOC'2014](https://www.google-melange.com/archive/gsoc/2014/orgs/kolibrios).

## Rough Guide for Prospective Contributors

- As the kernel is written in FASM, ability to write and understand i386-assembly code is very useful.
- C is also a plus as some applications/libraries and components are written in C. Also, C is useful to interface with assembly at times.
- Familiarity with the GNU landscape like Autotools, GCC etc are also a plus to have (especially for porting software)
- The desire to take challenging problems and solve them is also required as several parts of the code base require thought for design and implementation. (The mentors can help you with that :) )
- Hanging out on LiberaChat's #kolibriOS and
[our forum](https://board.kolibrios.org)where developers mostly hang out. - Languages used for communication are English and Russian (although most developers are bilingual, and you can always ask someone for help)
- Get in touch with other developers via IRC / Forums and enjoy your stay!

## I'm a potential GSoC contributor. I'm scared of all the assembly and docs here! Where should I start?! :'(

Start here : [http://wiki.kolibrios.org/wiki/HowTo](/ideas/kolibrios-project-team/howto)
This will help you set up KolibriOS. Easiest will be to use either Qemu or VirtualBox as most developers use it and thus will be able to help you with eventual problems. Feel free however to try something else and let us know how it goes!

## I'm a potential GSoC contributor. What is this test task?!

Regarding the test mentioned above, it is for assessing your current skill set and their relevance regarding the project that you want to eventually work on. In most cases, your potential mentor will assign you a task via IRC / Forum but another developer can do this as well. Meanwhile, In case you are waiting for a test task, you can go through our [bug tracker](https://git.kolibrios.org/KolibriOS/kolibrios/issues) and find a small task to work on yourself, or learn about KolibriOS by going through example code.

## I want to play with the code but my college blocks Git

If you are have trouble accessing official Git repository, please do mention it on the forums. You can temporarily use this backup Git repository:

Or our official GitHub mirror:

## All the ideas seem interesting, But...

Feel free to suggest your own idea! This is encouraged largely both in GSoC and KolibriOS. The mentors will be glad to such an idea and assess it's feasibility/usability for KolibriOS.

## Great Guide! But I still don't understand X

Please read Documentation / Development pages on this Wiki. If you have any doubts, feel free to connect with other KolibriOS users and developers through Forum Chat or #kolibrios on LiberaChat.

Please ask developers / mentors on Forum Chat or IRC. Please be patient on IRC and Forum as developers are on different time zones and it might take a few hours to get back to you. You can also start a Forum thread if it is about something you feel is a general issue.

And most importantly... Have Fun!
