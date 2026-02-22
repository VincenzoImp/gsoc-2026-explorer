# ScummVM — Project Ideas

**Source:** https://www.scummvm.org/gsoc-2026-ideas
**Scraped:** 2026-02-22T23:28:47.593408

---

# Summer of Code/GSoC Ideas 2026

If you'd like to get involved in ScummVM, we'd love to help you get started!

We've had a lot of successful student projects as part of Google's Summer of Code in previous years -- we hope to inspire you to work with us and (hopefully) add your own success.

We often get asks by participants with no experience with ScummVM whether they have the necessary skills to participate with us. The idea of GSoC is to introduce students to open source development, so we are not expecting you to have experience with ScummVM. You will have time during the application and community bonding periods to familiarize yourself with the project. The technical skills required to work with us varies from task to task. For any work on ScummVM, you'll probably need to already be comfortable with a basic level of C++. Some of the tasks might need more specialized knowledge (working on a 3D game engine may need you to understand some OpenGL and 3D math, and some engine tasks may require some assembly or reverse engineering knowledge); we give our thoughts about this alongside each suggested task, below.

Most importantly, we'd like you to join our community. There are many previous GSoC participants who are still involved in our project, and whether or not you participate as part of Summer of Code, we'd love for you to get involved too.

You should come to our [Discord Server](https://www.scummvm.org/index.php?title=Discord_Server) and introduce yourself in the #scummvm-gsoc channel! We're friendly, and it's often the easiest way to ask questions about the tasks and the code in general. The channel is the main form of everyday communication for the project, and there will almost always be developers there who can discuss your project ideas, answer questions and help out.

You can find more information about what we expect from you before you apply at [GSoC Application](https://www.scummvm.org/index.php?title=GSoC_Application).

## Introduction

We have a list of potential tasks further down on this page, but before you look at them, perhaps you'd like to take a look at some of the successful projects from previous years! We encourage all of our students to maintain a blog during their summer work, which is a nice way to get some sense of what they accomplished.

One popular type of task is to improve our support for the games you love, whether this means a new game engine, or helping us to perfect an existing one.

Sometimes source code is available - in recent summers, students integrated code supporting games such as [QdEngine](https://www.scummvm.org/index.php?title=QdEngine) ([blog](https://blogs.scummvm.org/kunxl/)) and [Unrest](https://www.scummvm.org/index.php?title=Unrest) ([blog](https://blogs.scummvm.org/hax0kartik/))into ScummVM. In fact, our support for the [Wintermute](https://www.scummvm.org/index.php?title=Wintermute) engine was not only started by a GSoC student ([blog](http://summermute2012.blogspot.com/)), who integrated the code into our tree, but also [drastically improved](https://www.scummvm.org/index.php?title=Wintermute/Games) by another student a year later ([blog](https://icodelikeacow.wordpress.com/)).

A more challenging (but hopefully rewarding) idea is to start (or continue) reverse engineering a game where no source is available. Two good examples are the pair of students who drastically improved support for Escape from Monkey Island ([blog](http://diggingemi.blogspot.com/), [blog](http://akzgsoc.blogspot.com/)), and the work on improving [Operation Stealth](https://www.scummvm.org/index.php?title=Operation_Stealth) ([blog](https://buddhahacks.wordpress.com/)). Another option is to work on merging (and improving) someone else's reverse engineering work, such as was done with the [ZVision](https://www.scummvm.org/index.php?title=ZVision) engine ([blog](http://richiesams.blogspot.com/search/label/ScummVM)).

If you'd prefer to improve ScummVM more directly, there are even more options available there; in the past, students have (to give some examples) improved our OpenGL support, added support to keymapper to multiple engines ([blog](https://blogs.scummvm.org/markhor/)), improved our scaler code ([blog](http://singron.blogspot.com/)), written a new GUI framework, added loadable modules for embedded platforms ([blog](http://tonypuccinelli.blogspot.com/search/label/ScummVM)), rearchitected our keyboard input code ([blog](http://kenny-gsoc.blogspot.com/)) and added support for high-colour (16bpp and above) graphics. It's difficult for us to imagine ScummVM as it was before some of these projects, you can make a huge difference!

## Tasks

General contacts: Our Discord server our mailing list, or contact [sev](https://www.scummvm.org/index.php?title=User:Sev), [Arnaud Boutonné](https://www.scummvm.org/index.php?title=User:Strangerke)

The ideas here are meant to be just that - **ideas**. We hope they help inspire your proposals, but you should also consider suggesting your own completely new project ideas. Pick something you really want to see improved/fixed, and come and talk to us about it!

If you're looking for more inspiration for ideas, beware of our [TODO](https://www.scummvm.org/index.php?title=TODO) (and the other TODO lists linked from there) and our [OpenTasks](https://www.scummvm.org/index.php?title=OpenTasks) pages. Many of the tasks listed there might be incomplete or outdated, or too difficult for a new developer. The best thing to do is to come and talk to us!

## Game Tasks

Technical contacts: Our Discord channel, our mailing list, or contact [sev](https://www.scummvm.org/index.php?title=User:Sev), [John Willis](https://www.scummvm.org/index.php?title=User:DJWillis), [Arnaud Boutonné](https://www.scummvm.org/index.php?title=User:Strangerke), [Filippos Karapetis](https://www.scummvm.org/index.php?title=User:Md5),

If you already have reverse engineering experience, you could consider working on one of the external in-development game engines, or even on support for a new game. However, doing this kind of work is very difficult and time-consuming - you would have to convince us that you have the necessary skills to actually be sufficiently productive, probably by demonstrating some actual progress first.

If you don't feel quite up to that level of challenge, we have lots of other suggestions:

### Macromedia Director

- Technical contacts:
[sev](https://www.scummvm.org/index.php?title=User:Sev) - Difficulty level: Medium. You'll need a reasonable level of programming experience, and probably some
[Director](https://www.scummvm.org/index.php?title=Director)games. - Size: 175 or 350 hours

[Many 90s-era adventure games](https://www.scummvm.org/index.php?title=Director/Games) were developed using the Macromedia (now Adobe) Director tool. We added so far support for Director 3 and Director 4, but there is much more work related to the specific Xtras, increasing compatibility and working on Director 5 support.

These days, due to the relatively high compatibility our approach is taking an interesting Director title, trying to play it and fix any issues along the way, thus making the process pretty fun. During playback, we often compare the titles and behaviors with the original.

Often, we implement stubs for XObjects, which are extensions for Director functionality.

Besides the core engine development, there is a lot of work on the visual source level debugger, written with use of ImGUI.

### Amnesia: The Dark Descent and A Machine for Pigs (HPL2 engine)

- Technical contacts
[aquadran](https://www.scummvm.org/index.php?title=User:Aquadran)or[sev](https://www.scummvm.org/index.php?title=User:Sev) - Difficulty level: Hard. OpenGL knowledge is required
- Size: 350 hours

Frictional Games has released full sources for their [HPL2 engine](https://en.wikipedia.org/wiki/Frictional_Games#HPL_Engine) under GPLv3 license. In 2022 we added HPL1 engine and now we could consider adding HPL2. The size of the task is huge since the engines are 275k and 240k lines of code respectively, but we already have experience from working on Penumbra.

The purpose of this project is to port the HPL2 engine to ScummVM, with the goal of supporting *Amnesia: The Dark Descent* and *Amnesia: A Machine for Pigs*.

### Finishing implementation of incomplete engines

- Technical contacts:
[sev](https://www.scummvm.org/index.php?title=User:Sev)or[strangerke](https://www.scummvm.org/index.php?title=User:Strangerke) - Difficulty level: Medium or High
- Size: 175 hours or 350 hours

ScummVM currently has a number of engines that are very close to completion. Many of them were parts of previous GSoCs. For them, we need a playthrough and slight bug fixing, or additional portability fixes.

Some of the engines are:

[Glk](https://www.scummvm.org/index.php?title=Glk), Need to expose font and graphics controls, improve font rendering[Avalanche](https://www.scummvm.org/index.php?title=Avalanche), some engine parts like Outro are not finished. Complete list is[here](https://www.scummvm.org/index.php?title=Avalanche#TO-DO)[DM](https://www.scummvm.org/index.php?title=DM)[Comprehend](https://www.scummvm.org/index.php?title=Comprehend), finishing support for Transylvania (V2), and adding support for the 16-color Apple IIgs versions[Lilliput](https://www.scummvm.org/index.php?title=Lilliput)[Lure](https://www.scummvm.org/index.php?title=Lure), Need to cross-check functionality versus the original assembly code that was published after we complete our reimplementation

### Porting ADL to ScummVM

- Technical contacts:
[sev](https://www.scummvm.org/index.php?title=User:Sev) - Difficulty level: Medium or High
- Size: 350 hours

ADL (Adventure Definition Language, not to be confused with [Sierra's ADL](https://www.scummvm.org/index.php?title=ADL)) was created in 1987 by Tim Brengle and Ross Cunniff and released as freeware. Subsequent modifications to the engine have been made since and released under GPL. Documentation as well as a compiler and interpreter can be found [at this link](https://adl.sourceforge.net/).

Only one commercial game is known to have been released using ADL: Transylvania III. The previous 2 entries in the series use the [Comprehend](https://www.scummvm.org/index.php?title=Comprehend) engine.

The purpose of this task is to port this engine to ScummVM's Glk engine.

### Porting ACK engine to ScummVM

- Technical contacts:
[sev](https://www.scummvm.org/index.php?title=User:Sev) - Difficulty level: Medium
- Size: 350 hours

[ACK (Adventure Creation Kit)](https://mozomedia.com/ack/) was a Pascal-written game development system. Its sources were [released](http://www.80sgaming.org/ack/) under Public Domain, and there is [a port](https://github.com/neutromancer/ackfree) to Free Pascal. The whole solution is mid-size, around 16k lines of code, but it must be converted to C++ before porting. A program such as p2c (Pascal-to-C) converter could be used for the initial code conversion, but then, the manual work on making things work will follow.

There are several RPG-like games build on the engine, the most notable one is Ultima-like games.

The purpose of this task is to port this engine to ScummVM as a separate engine engine.

### Porting Ambermoon/Amberstar engine to ScummVM

- Technical contacts:
[sev](https://www.scummvm.org/index.php?title=User:Sev) - Difficulty level: Hard / Very Hard
- Size: 350 hours

[Ambermoon](https://www.mobygames.com/game/10789/ambermoon/) and [Amberstar](https://www.mobygames.com/game/3160/amberstar/) were nice Amiga RPGs created by Thalion Software GmbH, a German company in early 90s. There are complete sources released for both games: [here](https://github.com/historicalsource/ambermoon) and [[here](https://github.com/historicalsource/amberstar). It is technically possible to rewrite them in C++.

The task will require learning or knowledge of the beautiful Motorola Assembly language and some knowledge on how Amiga worked with graphics and sound.

### Porting iBASS engine to ScummVM

- Technical contacts:
[sev](https://www.scummvm.org/index.php?title=User:Sev) - Difficulty level: Medium
- Size: 350 hours

The [sky](https://www.scummvm.org/index.php?title=Sky) engine is one of the oldest engines in ScummVM. However, later Revolution Software released the game for iPhones with enhanced controls. The game is built on top of the current engine but contains significant enhancements; thus, porting efforts are required. The code was published under GPLv2. Besides C++ skills, the task will involve reading Objective-C.

### Porting Skeldal engine to ScummVM

- Technical contacts:
[sev](https://www.scummvm.org/index.php?title=User:Sev) - Difficulty level: Medium/High
- Size: 350 hours

Czech game [[Brány Skeldalu](https://store.steampowered.com/app/3533830/Brny_Skeldalu/)] had its sources [[fully published](https://sourceforge.net/projects/skeldal/)] under GPLv3. This project would require porting over the game engine (not the editor) to ScummVM. C++ skills are required.

### Bring your own Adventure or RPG Reimplementation (only existing games)

- Technical contacts: Talk to us on Discord, or send us an email.
- Difficulty: Hard. You'll need good knowledge of C++, as well as knowledge of (reading) assembly.
- Size: 350 hours

Our project consists of re-implementations of classic games, and we have listed a number of potential new game engines that you could work on here on our ideas page. However, you may have a classic 2D Adventure game or Role Playing Game (RPG) you are interested in yourself that is suitable for ScummVM that you would like to reverse engineer and re-implement. If so, great!

Adding a completely new game engine is not easy, and you will have to convince us that you are aware of the challenges involved, that the game you are interested in is feasible, and that you have the necessary skills. Preferably, you will already have done some preliminary investigation, into for example data file formats, disassembly, etc.

Please come talk to us to see if we have a mentor who would be interested in working with you on such a game. We'd be happy to help out.

## Smaller Tasks

### Add Keymapper to more games

- Technical contacts: sev
- Difficulty: Easy
- Size: 175 or 350 hours, depending on the number of games

ScummVM includes a global fully configurable keymapper, but this requires engines to be adapted to use it. The feature documentation: [Keymapper](https://www.scummvm.org/index.php?title=Keymapper), some reference implementations: Wintermute has [per-game keymaps](https://github.com/scummvm/scummvm/blob/master/engines/wintermute/keymapper_tables.h); [a pull request](https://github.com/scummvm/scummvm/pull/2428) with adding keymapper to HDB engine; [a commit](https://github.com/scummvm/scummvm/commit/cce713ee4c73504e97eba8b0ca9190e47d279e69) with adding Keymapper to a simpler engine, Griffon.

The current status can be found at [Keymapper_and_TTS_status](https://www.scummvm.org/index.php?title=Keymapper_and_TTS_status) page.



### Add Text-to-Speech to more games

- Technical contacts: sev
- Difficulty: Easy
- Size: 175 or 350 hours, depending on the number of games

ScummVM has [Text-to-Speech](https://en.wikipedia.org/wiki/Text-to-speech) (TTS) functionality that we are using for the games that have no speech (or limited options for speech). That improved the usability of the games and, obviously, their accessibility.

The current status per engine can be found on the [Keymapper_and_TTS_status](https://www.scummvm.org/index.php?title=Keymapper_and_TTS_status) page.

For each engine, the task varies from straightforward to a mid-complexity:

- Identify routines that show text on the screen
- Potentially, clean up text from things like colors and fonts
- Feed this text to TTS
- Define GUI options for triggering the option

### Porting ALIS engine to ScummVM

- Technical contacts:
[sev](https://www.scummvm.org/index.php?title=User:Sev) - Difficulty level: Medium
- Size: 175 hours

ALIS (Actor Language Integrated System) is an engine that was used by [Simlarils](https://en.wikipedia.org/wiki/Silmarils_(company)) for most of their games and about 17 of them are expected to work on this engine. There is an engine that is almost complete, it is pretty small, less than 10k lines of code and is distributed under MIT license. [Engline](https://github.com/maestun/alis) and we also have Ghidra projects for the engine.

The purpose of this task is to port this engine to ScummVM as a separate engine engine.

### YAGA engine

- Technical contacts:
[sev](https://www.scummvm.org/index.php?title=User:Sev)or[strangerke](https://www.scummvm.org/index.php?title=User:Strangerke) - Difficulty level: Medium.
- Size: 175 hours

This engine was used for two later [Humongous Entertainment](https://www.scummvm.org/index.php?title=Humongous_Entertainment) games, [Pajama Sam: Life is Rough When You Lose Your Stuff](https://www.scummvm.org/index.php?title=Pajama_Sam:_Life_is_Rough_When_You_Lose_Your_Stuff) and [Putt-Putt: Pep's Birthday Surprise](https://www.scummvm.org/index.php?title=Putt-Putt:_Pep%27s_Birthday_Surprise). The engine is basically an extension of Python 2.2. There exists an almost complete reimplementation by cyx [on GitHub](https://github.com/cyxx/linyaga) (which we have permission to use) that can be used as a base, and we also have the complete source code for the original game.

The task is relatively straightforward, the only difficulty with it is adding Python as an external dependency, but a mentor is there to help. Implementing the missing "Lip Sync" feature will be the main part of this task.

The goal is to bring cyx's code to ScummVM and use the original code as a reference later.
