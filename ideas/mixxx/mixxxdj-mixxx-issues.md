# feature requests

**Parent:** Mixxx — Project Ideas
**Source:** https://github.com/mixxxdj/mixxx/issues?q=is%3Aopen+is%3Aissue+label%3Afeature
**Scraped:** 2026-03-10T16:58:40.258009

---

## #16128: Absolute mode Needle Drop at Beginning of Vinyl

**Labels:** vinylcontrol

If "Vinyl" mode Absolute is the setting, a needle drop at the beginning of media should toggle back to Vinyl Mode Absolute. "period".  The keyboard short cut (Ctrl+Shift+[Y][U]) to toggle Vinyl Absolute mode is clunky.  

Almost all DJ software will fall back to Vinyl Mode Absolute when a needle is dropped at the beginning of a song.  

Yes, looping or cue points will knock off Vinyl Absolute Mode but a needle drop at the start of media should fall back to Vinyl Absolute Mode.

I using 2.5.4 and 2.7 Beta Mixxx.

---

## #16126: ARM64: Audio thread missing flush-to-zero (FPCR FZ bit) causes full-volume digital noise with stacked effects

### Bug Description

## Description

### Summary

On ARM64, Mixxx's audio processing thread runs without the FPCR flush-to-zero (FZ) bit set. This causes denormal float operations in effects with feedback loops to stall the CPU, leading to buffer underruns that produce full-volume digital noise. The issue triggers when two or more effects are active simultaneously.

### Environment

- **Mixxx version**: 2.5.4+dfsg-1+b1 (Debian arm64)
- **Platform**: Raspberry Pi 4 (Cortex-A72), Debian 13 Trixie, PREEMPT_RT kernel
- **Audio**: Traktor Kontrol S4 MK2 (USB Audio), ALSA backend, 44100 Hz
- **Build flags**: `-ffast-math -funroll-loops -O3`

### Steps to Reproduce

1. Run Mixxx on any ARM64/aarch64 system
2. Load a track on a deck
3. Enable two or more effects on that deck's effect unit (e.g., echo + reverb, or any chain with feedback-based effects)
4. Play the track and engage the effects

**Result**: Intermittent blasts of full-volume digital noise (max-amplitude samples sent to DAC).

**Expected**: Clean effect processing, same as on x86.

### Root Cause

On ARM64, the FPCR (Floating Point Control Register) is per-thread and not inherited by child threads. This is a key difference from x86, where the SSE MXCSR register (containing FTZ/DAZ flags) IS inherited via `pthread_create`.

Mixxx is compiled with `-ffast-math`, which causes GCC to link `crtfastmath.o`. This CRT object contains a constructor that sets `FPCR.FZ = 1` but only for the main thread. The audio engine thread, created later via `pthread_create`, starts with `FPCR = 0x0` (FZ bit off, denormals active).

Effects with feedback loops (echo, reverb, phaser, flanger, Moog ladder filter) produce signal tails that decay to denormal float values (~10^-38). Without FTZ, each denormal operation takes 10-100x longer on ARM. When multiple effects are stacked, these accumulated stalls cause audio buffer processing to exceed the real-time deadline, resulting in buffer underruns. The DAC interprets the stale/uninitialized buffer contents as maximum-amplitude output.

#### `-ffast-math` verification bypass

Issue #16053 addressed the denormal-to-zero assertion failing under Valgrind. The runtime check in `callbackProcessClkRef()` verifies FTZ by testing `DBL_MIN / 2 == 0.0`. However, on ARM64 hardware (outside Valgrind), this check likely never catches the problem because:

1. Mixxx is compiled with `-ffast-math`, which tells GCC it can assume denormals are flushed to zero
2. GCC then optimizes `DBL_MIN / 2 == 0.0` to always-true at compile time (since under `-ffast-math` semantics, denormals "don't exist")
3. The runtime verification passes without ever reading the actual FPCR register
4. No warning is logged even though FPCR.FZ is actually 0 on the audio thread

The binary does contain ARM64 FPCR code (`mrs/msr fpcr` instructions and the string `"aarch64 FPCR: setting bit 24 to 1"`), but the "Denormals to zero mode is working/not working" messages never appear in `mixxx.log`. This is consistent with

*[truncated]*

---

## #16123: Remove libmp4v2 as a dependency

### Feature Description

Not sure if this should be a bug or a feature, but the request is to remove `libmp4v2` as a dependency since it no longer appears to be needed.

https://github.com/mixxxdj/mixxx/issues/10019#issuecomment-1225429593 and https://mixxx.discourse.group/t/compiling-mixxx-on-linux-ubuntu-20-04-2-lts/21227/2 suggests that the use of `ffmpeg` replaced `libmp4v2` a while ago. AFAICT the only build script that still uses `libmp4v2` is [`rpm_buildenv.sh`](https://github.com/mixxxdj/mixxx/blob/67fbbfcdc8eab04ff1a70e644969f442b9302ddd/tools/rpm_buildenv.sh#L49), but that script also installs `ffmpeg-devel` so the build should support the `ffmpeg` approach?

Also on the RPM/Fedora side of things, [the wiki](https://github.com/mixxxdj/mixxx/wiki/Mixxx-On-Fedora) states that Mixxx isn't available directly but the source it quotes now says that it's OK and [it is available in the repos](https://packages.fedoraproject.org/pkgs/mixxx/mixxx/). The fusion repo [linked from here](https://github.com/mixxxdj/mixxx/wiki/Ubuntu-and-Fedora-Support-Policy) is also retired/orphaned. It's also stated that [Arch requires libmp4v2](https://github.com/mixxxdj/mixxx/wiki/Compiling%20on%20Linux#arch--derivatives) but they have [dropped it as a dependency too](https://gitlab.archlinux.org/archlinux/packaging/packages/mixxx/-/commit/9aae05131a99cbbc5fa41db531c115bbe9d7785f).

---

## #16121: Rekordbox formated USB appears blank in Mixxx

**Labels:** rekordbox

### Bug Description

Hey there,

I've been trying to read my playlists that I have exported with rekordbox onto my USB hard drive. The hard drive shows up under the rekordbox tab, but is unfortunately blank. If I go through the file browser the tracks are found but do not have my memory cues and loops. I used Rekordbox 7.2.11 to create the USB hard drive.

I've tried everything (formatting in FAT32, exFAT, HFS, using different Mixxx version) but the result is always the same.

Is this a bug or am I too stupid?

<img width="1063" height="302" alt="Image" src="https://github.com/user-attachments/assets/88b506fc-608f-40b9-a0de-6056c95d1e1d" />
<img width="1321" height="304" alt="Image" src="https://github.com/user-attachments/assets/dc24623e-df72-4361-a362-1df4c3ac06db" />

### Version

2.5.2, 2.6

### OS

MacOS Tahoe 26.2 (25C56)

---

## #16120: STEM loading cuases a cpu spike and a small drop-out

**Labels:** engine, stems

### Bug Description

Noticed today when playing a set that someimes when I loaded a song mixxx had a little dropout...

It happens everytime I load a stam file (I don't have many).

The CPU meter goes red for an instant and there is the dropout

I'm on windows 11 with the numark party mix mk2 at 5ms latency

### Version

2.6-beta-216-g3c0399d5cd

### OS

windows 11

---

## #16114: Do not zip GitHub action artifacts twice

**Labels:** developer experience, github_actions

In former times GitHub required every artifact to be compressed as zip file, this is no longer the case:
https://github.blog/changelog/2026-02-26-github-actions-now-supports-uploading-and-downloading-non-zipped-artifacts/

It would simplify to use patch files, Mixxx installers and VCPKG buildenvs, if we don't use this second compression - and probably reduce CI CPU time.

---

## #16110: create option to disable recording splitting

**Labels:** preferences, easy, confirmed, recording

### Feature Description

Right now there is no option to disable recording splitting even though there's no reason modern OSes can't write huge files.  We should add this.

---

## #16101: library scanning

**Labels:** scanner

### Bug Description

The Scan Dialog jumps up and down while scanning the library.

https://github.com/user-attachments/assets/348b0a0b-7295-408c-a28e-ec36e97f0132

### Version

2.6 Beta newest version

### OS

Windows 11

---

## #16090: Linux desktop file: wrong StartupWMClass for x11

**Labels:** linux

### Bug Description

PR https://github.com/mixxxdj/mixxx/pull/12424 added this line to the desktop file: `StartupWMClass=org.mixxx.mixxx`

This is fine for Wayland, i guess, but very wrong for x11. Xprop shows: `WM_CLASS(STRING) = "mixxx.bin", "Mixxx"`
Because of that wrong ID i cannot add Mixxx to Plank-Reloaded, for example.
But if i change it to: `StartupWMClass=Mixxx` - everything works like a charm.

OS: Linux Mint 22.3
DE: Cinnamon, Mate
Installation: repo (mixxx 2.4.0), flatpak (mixxx 2.5.2)

### Version

2.5.4

### OS

Linux

---

## #16077: Support Lower Latency Setting of Audio Interfaces

**Labels:** engine, preferences

### Feature Description

First of all Mixxx 2.5.4 improvements with DVS is a blessing.  Thank You.  Let's take the responsiveness of Mixxx further by including lower latency setting of the software beyond the 96KHz sample rate and 1.3ms Audio Buffer setting in the ASIO Preferences.  Mixxx is getting closer to "feeling" like vinyl but is not there yet. I need software that "feels" like vinyl to beat match, cue, scratch all the things that DJ do while never missing a beat.  Latency has crept into software, Mixxx needs to keep lowering latency.

I used a software utility RTL (Round Trip Latency Utility) which gives me the loop-back time of the audio signal output-input.  With the Mixxx setting of 96KHz, 1.3ms the RTL is 2.865msec (~ 1.3ms X 2) but my audio interface with a fast CPU can support even faster, i.e. lower latency, settings.  

Here's results from my Lynx Audio E44 audio interface
Sample Rate   Audio Buffer size (msec)   RTL(msec)
96KHz             128 Samples (1.3ms)         2.865
96KHz               64 Samples (0.7ms)         1.531
96KHz                32 Samples (0.3ms)         0.865

192kHz             256 Samples (1.3ms)          2.755
192kHz             128 Samples (0.7ms)          1.422
192kHz               64 Samples (0.3ms)          0.755
192kHz                32 Samples (0.2ms)         0.422

Btw, I was able to use DJ software with settings below 1ms but this other software (VDJ) is full of bugs when it comes to DVS. 

A desktop CPU, e.g. Ryzen 7800 X3D, I'm able to easily go beyond the 96KHz 1.3msec setting of Mixxx.

---

## #16075: Overview cue upate regression after #15968

**Labels:** blocker, waveform, overview

### Bug Description

_filing this in addition to my comment in the PR so we have a blocker bug_

Unfortunately #15968 introduces some update regressions in the overview.
Hotcues:
* set hotcue1 -> no update in overview
* set hotcue2 -> hotcue1 pops up in overview

Loop cues:
* updated/shown after seek in the overview (repaint?)

Same delay after clearing hotcues: they're removed only after forced repaint (hover overview)

[mixxx-overview-hotcues-delayed-update.webm](https://github.com/user-attachments/assets/c148a54c-f87e-4dc1-be04-3587e56b64e4)



### Version

_No response_

### OS

_No response_

---

## #16070: allow to join History playlists of two Mixxx computers

**Labels:** history

### Feature Description

Let's say two (or more) Mixxx DJs play a back-to-back session, each on his PC.
It would be cool if we could somehow merge the two+ session playlists.

on computer A:
1. export a History playlist with timestamps as well as the tracks (to one new directory)
2. copy that dir onto a USB drive, SD card, whatever

on computer B:
1. attach USB, copy the History directory to the music dir
2. in Mixxx, right-click History root item, "Import external session"
   * select a dir
   * import the track files, insert them into a new History playlist, use timestamp from playlist
(map tracks from m3u to new track ids, pick first track's timestamp as "created" date)
3. allow to "Merge playlist with ..."
-> insert imported tracks according to their timestamp
-> this probably has to be different than the existing "Join with previous" as both playlist are not necessarily

---

## #16069: Add shortcuts for addition to last used crates/playlists

### Feature Description

The current system of manually going through submenus to select which crates/playlists one wants to add selected tracks is great for general multi crate/playlist tiding and organizing. 

However, when it comes to creating a specific crate/playlist from a messy list (like a set for a gig), its obnoxious af, since one has to repeat the same "right click>add to crate/playlist>select crate/playlist" over and over with each track or selection. 

If there's a hotkey one could just press to add the selected tracks to the last used (or maybe a preselected "default" for the session) crate/playlist, that would make the job soooo much easier and streamlined. :)

I dunno, maybe having a QuickSetBuild mode or something where it automatically offers to send all selected tracks to the crate/playlist that was used by pressing something like CTRL+1 (maybe all numbers could be prefconfigured with a playlist/crate for example).
Or having a "Current Session New Crate/playlist" created when the hotkeys are pressed where all the tracks go, and then one can just rename that or whatever.

---

## #16067: macOS 12 AudioUnit crash on startup

**Labels:** effects, crash, macos

### Bug Description

Hi all, I'm getting this crash on Mixxx startup on macOS Monterey (see detailed log below). I've tried installing the app via mixxx.org and using brew but both give the same result. When starting Mixxx, I just see the loading indicator with the logo for a split second, then it crashes instantly.

I've also tried launching with `--safeMode` option but the issue persists, though I do see some linking error printed out in the console as well as some warnings tied to loading Audio Units.

<details>

<summary>Terminal output</summary>

```
/Applications/Mixxx.app/Contents/MacOS/Mixxx --safeMode
dlopen error : dlopen(libjack.0.dylib, 0x0001): tried: 'libjack.0.dylib' (no such file), '/usr/local/lib/libjack.0.dylib' (no such file), '/usr/lib/libjack.0.dylib' (no such file), '/Users/tonell_m/Library/Containers/org.mixxx.mixxx/Data/libjack.0.dylib' (no such file)
dlopen error : dlopen(/usr/local/lib/libjack.0.dylib, 0x0001): tried: '/usr/local/lib/libjack.0.dylib' (no such file)
Using preferences ScaleFactor 1
Selected Qt style: "macos"
Setting Qt plugin search path to: "/Applications/Mixxx.app/Contents"
Loading resources from  "/Applications/Mixxx.app/Contents/Resources/"
Configuration file is now at the current version "2.5.4"
BroadcastSettings - Found 1 profile(s)
warning [Main] Audio Unit "TAL-Reverb-2" could not be instantiated: -3000 (Check https://www.osstatus.com for a description)
warning [Main] Instantiated Audio Unit "TAL-Reverb-2"  is null, despite not erroring on initialization, something's wrong
warning [Main] Audio Unit "Eos 2" could not be instantiated: -3000 (Check https://www.osstatus.com for a description)
warning [Main] Instantiated Audio Unit "Eos 2"  is null, despite not erroring on initialization, something's wrong
warning [Main] Audio Unit "Digitalis" could not be instantiated: -3000 (Check https://www.osstatus.com for a description)
warning [Main] Instantiated Audio Unit "Digitalis"  is null, despite not erroring on initialization, something's wrong
warning [Main] Audio Unit "ValhallaFreqEcho" could not be instantiated: -3000 (Check https://www.osstatus.com for a description)
warning [Main] Instantiated Audio Unit "ValhallaFreqEcho"  is null, despite not erroring on initialization, something's wrong
warning [Main] Audio Unit "Supercharger" could not be instantiated: -3000 (Check https://www.osstatus.com for a description)
warning [Main] Instantiated Audio Unit "Supercharger"  is null, despite not erroring on initialization, something's wrong
warning [Main] Audio Unit "Phasis" could not be instantiated: -3000 (Check https://www.osstatus.com for a description)
warning [Main] Instantiated Audio Unit "Phasis"  is null, despite not erroring on initialization, something's wrong
[1]    73050 bus error  /Applications/Mixxx.app/Contents/MacOS/Mixxx --safeMode
```

</details>

<details>

<summary>Crash report</summary>

```
-------------------------------------
Translated Report (Full Report Below)
---------------------

*[truncated]*

---

## #16060: Feature request: support for Matroska (mka) files

**Labels:** confirmed

### Feature Description

Today I went to load a track I wanted to play and was surprised to find that it wasn't already in my library and that manually trying to add it failed! I looked up the [supported formats ](https://manual.mixxx.org/2.7/en/chapters/library.html#compatible-file-formats) for 2.7 and searched the issue tracker and couldn't find any mention of it (I did find some old forum posts asking the question, but no actual issue), so I'm filing this issue to request support for [Matroska](https://www.rfc-editor.org/rfc/rfc9559) files.

Matroska (more commonly known by the file extension used for video, mkv, or audio, mka) is a wrapper format that is already widely used and supported for audio, particularly among archivists. In particular I would like to request support for Matroska containing FLAC or Opus audio (which is what the files I have use as the underlying codec), but other formats already supported by Mixxx could also be put into Matroska files (See [draft-ietf-cellar-codec](https://datatracker.ietf.org/doc/draft-ietf-cellar-codec/)).

As a stretch goal it would be nice if the file metadata could be read from the Matroska metadata (as opposed to the Vorbis comment embedded in the underlying FLAC or Opus stream), I've seen MKA files which encode metadata in both ways, unfortunately (the container native way and the underlying codec way). For information on standard Matroska tag mappings, see [draft-ietf-cellar-tags](https://datatracker.ietf.org/doc/draft-ietf-cellar-tags/).

This would potentially also give us free support for WEBM files (which use a profile of Matroska), see #12832.

Thank you for your consideration.

**EDIT:** I should mention that, for now, I have just converted the file to FLAC, which is an easy enough work around. This is not a blocker or anything. It would still be nice to have native Matroska support though!

---

## #16057: Unable to find HERCULES MK4 mapping

**Labels:** incomplete

### Bug Description

Bonjour , J'ai un contrôleur HERCULES MK4 et le mapping a disparu , il n'existe plus dans les propositions offertes dans les paramètres  du logiciel . Du coup je ne peux plus utiliser ce contrôleur .
Pouvez vous m'aider ???
Merci beaucoup 

### Version

{1B2848C0-65D0-44BC-9298-8905E6CA9C82}

### OS

Windows 11

---

## #16055: column deleagtes not deletd on exit

**Labels:** easy, confirmed

### Bug Description

We use "QAbstractItemView::setItemDelegateForColumn()" which does not take ownership of the delegate. 
When Mixxx is closed these delegates are not deleted and left behind. This is not an issue in this case but bad practice. Instead we should use uniqe_ptr to have a dedicated owner a std::vector member variable in WTrackTableView.
 
This has been caught by valgrind: 
```
==12711== 8 bytes in 1 blocks are indirectly lost in loss record 365 of 9,758
==12711==    at 0x60B3F95: operator new(unsigned long) (vg_replace_malloc.c:488)
==12711==    by 0x4A86800: BPMDelegate::BPMDelegate(QTableView*) (bpmdelegate.cpp:39)
==12711==    by 0x499CAE7: BaseTrackTableModel::delegateForColumn(int, QObject*) (basetracktablemodel.cpp:360)
==12711==    by 0x4738FF3: WTrackTableView::loadTrackModel(QAbstractItemModel*, bool) (wtracktableview.cpp:278)
==12711==    by 0x4A3FDD4: DlgHidden::DlgHidden(WLibrary*, QSharedPointer<ConfigObject<ConfigValue> >, Library*, KeyboardEventFilter*) (dlghidden.cpp:39)
==12711==    by 0x4451525: MixxxLibraryFeature::bindLibraryWidget(WLibrary*, KeyboardEventFilter*) (mixxxlibraryfeature.cpp:145)
==12711==    by 0x4438EF2: Library::bindLibraryWidget(WLibrary*, KeyboardEventFilter*) (library.cpp:469)
==12711==    by 0x4AFA242: LegacySkinParser::parseLibrary(QDomElement const&) (legacyskinparser.cpp:1706)
==12711==    by 0x4AFE518: LegacySkinParser::parseNode(QDomElement const&) (legacyskinparser.cpp:638)
==12711==    by 0x4B001DA: LegacySkinParser::parseSplitter(QDomElement const&) (legacyskinparser.cpp:682)
==12711==    by 0x4AFE55E: LegacySkinParser::parseNode(QDomElement const&) (legacyskinparser.cpp:634)
==12711==    by 0x4B009F9: LegacySkinParser::parseChildren(QDomElement const&, WWidgetGroup*) (legacyskinparser.cpp:747)
```





### Version

2.5.4

### OS

_No response_

---

## #16045: Print metadata to textfile

### Feature Description

I'm a streamer, and I'd like to use Mixxx for my music player, but I'd like a 'now playing' option. All I need is an option that prints the same format that goes into the title bar at the same time into a textfile, and I can call that in stream for a text element.

---

## #16024: EngineOS export doesn't handle variable bpm tracks correctly

### Bug Description

I have tracks with variable bpm, I analyzed them as such and the beat grid looks fine in mixxx.
Once I load the track onto my denon sc live 4, running engineOS 4.3.4, the beatgrid is off.
The track I tested it with rn is this one: https://video.building29.net/watch?v=PbEGWtcUnK0
Initially at 135bpm, but goes up to 160bpm. The deck shows me a constant 143bpm.

@mr-smidge you've got insight into the libinterop stuff, can you help?

### Version

2.5.4

### OS

NixOS25.11

---

## #16020: waveform menus; Simple at top?

### Feature Description

a) I think it would be more intuitive if the order of the main waveform preferences were redone,

currently;
- Filtered
- HSV
- RGB
- Simple
- Stacked
- VSyncTest


suggested;
- Simple
- Filtered
- HSV
- RGB
- Stacked
- VSyncTest

currently the overview waveform list is
- Filtered
- HSV
- RGB
- Stacked

so it would match that in part

and b) the corollary would be a Simple at the top of the overview waveforms menu

so, a two-in-one really, to make proper sense

---

## #16015: Memory Leak

### Bug Description

I have a massive memory leak that keeps growing until the whole software crashes.

<img width="467" height="110" alt="Image" src="https://github.com/user-attachments/assets/60b7dad5-8a0f-4996-87ad-c1ced359f03e" />

<img width="481" height="89" alt="Image" src="https://github.com/user-attachments/assets/842de033-8070-4adc-937a-aee57eb0ba06" />



### Version

2.5.4

### OS

Windows 11

---

## #16007: Auto-DJ is not running

### Bug Description

Since a few days Autodj stopped working for me

<img width="2880" height="1920" alt="Image" src="https://github.com/user-attachments/assets/e94dd91f-2be9-478a-9e60-4c5049c99aa0" />

It doesn't even load a track.

[mixxx.log](https://github.com/user-attachments/files/25399299/mixxx.log)

The Command line shows 
"warning [Engine] underflowHappened code: 24
warning [Engine] underflowHappened code: 25
"
when I activate the Auto-DJ

### Version

2.6 beta 198

### OS

Ubuntu Studio 25.10

---

## #15997: menubar: make Maximize Library a window shortcut

_This is just a heads up and question for now because currently ~~the bug~~ unexpected behavior probably only happens with some dialogs in #13842. It may also be in 2.5/main but I didn't test each and every dialog in these branches._

### The bug

On my production branch with #13842 I noticed that `Space` key doesn't work anymore to press dialog buttons (Cancel, Okay, ..)
-> instead the library is maximized.

For example in Track Info (= QDialog) -- but it still works in some confirm dailogs (QMessageBox).

So even though that dialog has focus, the key event seems to be sent to the main window's menubar. Turns out this happens because
* the [shortcutContext](https://doc.qt.io/qt-6/qt.html#ShortcutContext-enum) of the Maxmize action in the menubar is (implicitly) [`Qt::WidgetShortcut`](https://doc.qt.io/qt-6/qt.html#ShortcutContext-enum), and
* due to the changed parent structure of some dialogs in #13842 [^1]

FWIW Space still works in QMessageBox, for example the popups for confirming track deletion etc.

### The Fix
is to use `Qt::WindowShortcut`
= the shortcut only works if the menubar's window (MixxxMainWindow) has focus.

So my
### Question is:
shall we use `Qt::WidgetShortcut` for _all_ menubar actions?
Or is there a use case where users expect _menubar_ shortcuts to work -- even though some other Mixxx window has focus ?eg. show key wheel, toggle recoding, toggle AutoDJ

[^1]: this branch uses the main skin widget as parent for some dialogs so they can inherit its stylesheet:
MixxxMainWindow->centralWidget()

---

## #15996: waveform type name confusion/dilemma; Stacked = Filtered

### Bug Description

the relationship between Filtered and Stacked has been really confusing, as has the relationship between HSV and RGB (and tbh the relationship between Stacked and RGB)

for years I thought "Filtered" meant the colour was filtered. it took help recently to actually dig in and figure out the exact behaviour of the system

- Filtered = audio signal filtered into three EQd bands that get visually layered as three overlapping lines
     - Filtered is monochrome by convention, the default being grayscale, but themes can set the three values
- Stacked means exactly the same thing, but with palette set B, aka the RGB palette
    - RGB is straight RGB by default, but themes can set the three values

there is no functional difference between the two modes, just an alternate three colour palette

(maybe "Filtered" is so unintuitive that it was forgotten that it's the original descriptive name for a 3-band layering)

I believe that "Stacked" is a more immediately descriptive and generally understandable term

I would suggest that "Filtered" be renamed "Stacked (monochrome)", and "Stacked" renamed to "Stacked (RGB)"

(tbf, "HSV" could instead be "HSV (monochrome)" and "RGB" could be "HSV (RGB)", but that's not on the cards right here)

edit: todo, check if #12449 persists, same for #14813, make PR for #15581, maybe for #12449 and #12326

---

## #15989: Updates to JS engine are missing after MidiController::makeInputHandler()

**Labels:** controller backend

### Bug Description

When `MidiController::makeInputHandler()` is used, some changes to the JS engine have no effect. This issue contains a reproducible demo showing that `volume` does not update under certain circumstances.

#### Prerequisites
1. `MidiController::makeInputHandler()` is used to register a fader (`volume`) and a button (press: `volume_set_zero` / release: `volume` = 0.5) for deck 1.
2. The mute button is pressed => Deck 1 is muted.
3. The mute button is released => Deck 1 is unmuted.
4. The volume fader is moved => Volume of deck 1 changes.
5. The mute button is pressed => Deck 1 is muted.
6. The mute button is released.

#### Expected behavior
Deck 1 is unmuted.

#### Actual behavior
The volume of Deck 1 does not change, the deck stays muted.

#### Additional context
* The issue does not occur when `MidiController::makeInputHandler()` is not used.
* The issue does not occur when `volume` is set to `0` (instead of using `volume_set_zero`).

####  Test case
<details>
  <summary>XML demo: broken</summary>
  
```xml
<?xml version="1.0" encoding="utf-8"?>
<MixxxControllerPreset schemaVersion="1" mixxxVersion="2.6+">
  <info>
    <name>Volume Demo Broken</name>
  </info>
  <controller id="VolumeDemoBroken">
    <scriptfiles>
      <file filename="midi-components-0.0.js" />
      <file filename="volume-demo-scripts.js" functionprefix="VolumeDemoBroken" />
    </scriptfiles>
  </controller>
</MixxxControllerPreset>
```
</details>

<details>
  <summary>XML demo: working</summary>
  
```xml
<?xml version="1.0" encoding="utf-8"?>
<MixxxControllerPreset schemaVersion="1" mixxxVersion="2.6+">
  <info>
    <name>Volume Demo OK</name>
  </info>
  <controller id="VolumeDemoOK">
    <scriptfiles>
      <file filename="midi-components-0.0.js" />
      <file filename="volume-demo-scripts.js" functionprefix="VolumeDemoOK" />
    </scriptfiles>
    <controls>
      <control>
        <group>[Channel1]</group>
        <key>VolumeDemoOK.muteButton.input</key>
        <status>0x90</status>
        <midino>0x11</midino>
        <options>
          
        </options>
      </control>
      <control>
        <group>[Channel1]</group>
        <key>volume</key>
        <status>0xB0</status>
        <midino>0x31</midino>
      </control>
    </controls>
  </controller>
</MixxxControllerPreset>
```
</details>
  
<details>
  <summary>JavaScript</summary>

```javascript
/*
 * Behavior:
 *  Script is loaded, no MIDI control was touched yet.
 *  Button [0x90, 0x11] is pressed => Deck 1 is muted
 *  Button [0x90, 0x11] is released => Deck 1 volume is set to 0.5
 * 
 *  Volume is changed via MIDI fader [0xB0, 0x31].
 *  Button [0x90, 0x11] is pressed => Deck 1 is muted
 *  Button [0x90, 0x11] is released => Deck 1 STAYS MUTED
 * 
 */
MuteButtonHolder = {
  muteButton: new components.Button({
      group: "[Channel1]",
      midi: [0x90, 0x11],
      type: components.Button.prototype.types.toggle,
  })
}
MuteButtonHolder.muteButton.input = function(_

*[truncated]*

---

## #15983: Crash when moving free-scanned track to trash

## Bug Description
Mixxx crashes when moving a free-scanned track to trash.

## Steps to Reproduce
1. Drag a music file from outside library directories into Mixxx
2. Right-click on the track → "Move to trash"
3. Crash occurs

## Additional Context
Found while testing PR #15972. Only affects tracks that aren't in any configured library directory.

---

## #15982: White Noise causes channel dropout and lower gain

**Labels:** effects

### Bug Description

I recently encountered (twice) a somewhat annoying bug with a Quick Effect chain that has White Noise, but I did not yet manage to reproduce it.
I'll try to explain the setting:
* controller attached, S4mk3 with QuickEffect selector (1-2-3-4-Filter)
* deck2 assigned to effect unit 2, only Filter is active but Super knob centered (no LP or HP effect)
* a Quick Effect chain that has White Noise
* load that preset for deck2
* twist the Super knob fully left-right so the controller knob picks up the engine knob
  -> a lot of noise (expected ; )
  -> then suddenly (while turning the knob? not sure) left channel killed entirely
   + right channel lowered siginificantly
* disable the Quick Effect -> left channel is back but as low as the right channel
* disable Filter -> left/right channel volume restored

Once I get back to my controller I'll check which preset that is and post the full config.

### Version

_No response_

### OS

_No response_

---

## #15980: Address sanitizer detects double-free in HID access

**Labels:** linux, hid

I was running `main` with the address sanitizer to investigate an unrelated issue and got a double-free:

```
==60273==ERROR: AddressSanitizer: attempting double-free on 0x512000414dc0 in thread T76 (Thread (pooled)):
    #0 0x7f04323fc4d8 in free ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:52
    #1 0x7f042ba8c5f3 in hid_init (/lib/x86_64-linux-gnu/libhidapi-hidraw.so.0+0x35f3) (BuildId: a2de51574ffc7e2e8791a3d4e255ae0fa2c23778)
    #2 0x7f042ba8c696 in hid_enumerate (/lib/x86_64-linux-gnu/libhidapi-hidraw.so.0+0x3696) (BuildId: a2de51574ffc7e2e8791a3d4e255ae0fa2c23778)
    #3 0x7f042ba8cee8 in hid_open (/lib/x86_64-linux-gnu/libhidapi-hidraw.so.0+0x3ee8) (BuildId: a2de51574ffc7e2e8791a3d4e255ae0fa2c23778)
    #4 0x558c8424d0b8 in operator() /workspaces/mixxx/src/controllers/hid/hidcontroller.cpp:416
    #5 0x558c8424d0b8 in __invoke_impl<void, HidController::fetchReportDescriptorInBackground()::<lambda()>&> /usr/include/c++/13/bits/invoke.h:61
    #6 0x558c8424d0b8 in __invoke<HidController::fetchReportDescriptorInBackground()::<lambda()>&> /usr/include/c++/13/bits/invoke.h:96
    #7 0x558c8424d0b8 in invoke<HidController::fetchReportDescriptorInBackground()::<lambda()>&> /usr/include/c++/13/functional:113
    #8 0x558c8424d0b8 in operator() /usr/include/x86_64-linux-gnu/qt6/QtConcurrent/qtconcurrentstoredfunctioncall.h:116
    #9 0x558c8424d0b8 in __invoke_impl<void, const QtConcurrent::StoredFunctionCall<HidController::fetchReportDescriptorInBackground()::<lambda()> >::runFunctor()::<lambda(std::decay_t<HidController::fetchReportDescriptorInBackground()::<lambda()> >)>&, HidController::fetchReportDescriptorInBackground()::<lambda()> > /usr/include/c++/13/bits/invoke.h:61
    #10 0x558c8424d0b8 in __invoke<const QtConcurrent::StoredFunctionCall<HidController::fetchReportDescriptorInBackground()::<lambda()> >::runFunctor()::<lambda(std::decay_t<HidController::fetchReportDescriptorInBackground()::<lambda()> >)>&, HidController::fetchReportDescriptorInBackground()::<lambda()> > /usr/include/c++/13/bits/invoke.h:96
    #11 0x558c8424d0b8 in __apply_impl<const QtConcurrent::StoredFunctionCall<HidController::fetchReportDescriptorInBackground()::<lambda()> >::runFunctor()::<lambda(std::decay_t<HidController::fetchReportDescriptorInBackground()::<lambda()> >)>&, std::tuple<HidController::fetchReportDescriptorInBackground()::<lambda()> >, 0> /usr/include/c++/13/tuple:2302
    #12 0x558c8424d0b8 in apply<const QtConcurrent::StoredFunctionCall<HidController::fetchReportDescriptorInBackground()::<lambda()> >::runFunctor()::<lambda(std::decay_t<HidController::fetchReportDescriptorInBackground()::<lambda()> >)>&, std::tuple<HidController::fetchReportDescriptorInBackground()::<lambda()> > > /usr/include/c++/13/tuple:2313
    #13 0x558c8424d0b8 in runFunctor /usr/include/x86_64-linux-gnu/qt6/QtConcurrent/qtconcurrentstoredfunctioncall.h:120
    #14 0x558c82494145 in QtConcurrent::RunFunctionTaskBase<void>::run() /usr/include/x86_

*[truncated]*

---

## #15969: Bold playlist highlighting only works with "Open Sans" font

### Bug Description

I love the feature where, when selecting a track in a playlist, all playlists that contain it are highlighted in bold.

However, I've noticed that the "bold" only really works properly with the standard "Sans Serif" font. If any other font is selected for the "Library font", the highlighting is so subtle that it is almost impossible to see. Here are some screenshots, where you can see the difference.

**Sans Serif:**

<img width="466" height="448" alt="Image" src="https://github.com/user-attachments/assets/d0c5a037-cfd1-4bf4-a7a6-832545c69929" />

**Roboto:**

<img width="488" height="328" alt="Image" src="https://github.com/user-attachments/assets/fbd29326-ce4b-406a-b56f-fd8d94af57cb" />

**Cantarell:**

<img width="430" height="418" alt="Image" src="https://github.com/user-attachments/assets/589ae0c1-a249-4bae-8158-de769d3a3685" />

**Inter:**

<img width="466" height="332" alt="Image" src="https://github.com/user-attachments/assets/54e88f11-91d5-401e-a6d1-4cac586bd37e" />

I would love to use a different font than "Sans Serif", as that is clearly the ugliest of the lot.

It looks as if instead of loading the bold variant of the font, Mixxx is trying to turn the loaded variant into bold, with poor results.

### Version

2.5.4

### OS

NixOS

---

## #15967: [Skin],show_intro_outro_cues does not work for scrolling waveforms

### Bug Description

The expected behaviour is that the cue buttons and waveform overlay in overview and scrolling type disappear. 
This does not work for the scrolling waveform. 

### Version

2.6

### OS

_No response_

---

## #15966: Tests are not executed for Android build

**Labels:** Android

### Feature Description

<img width="448" height="283" alt="Image" src="https://github.com/user-attachments/assets/95700191-6e5a-42d9-ac13-6e3f49d03a1f" />

---

## #15962: debug assert loading track when autodj players become invalid

**Labels:** autodj

### Bug Description

**steps to reproduce:**

1. enable autodj
2. while audodj is playing, make decks 1 and 2 crossfader-middle, which makes them invalid for autodj
3. manually load a track into either deck.

**what we expect to happen:**
after the crossfader change, autodj should automatically disable itself because the decks are no longer valid. (autodj requires decks at crossfader left and right and refuses to start if this is not the case). 

**what does happen:**
we hit a debug assert, which crashes in a debug build.

```
critical [Main] DEBUG ASSERT: "pFromDeck && pToDeck" in function void AutoDJProcessor::calculateTransition(DeckAttributes*, DeckAttributes*, bool) at ./src/library/autodj/autodjprocessor.cpp:1266
critical [Main] DEBUG ASSERT: "pFromDeck && pToDeck" in function void AutoDJProcessor::calculateTransition(DeckAttributes*, DeckAttributes*, bool) at ./src/library/autodj/autodjprocessor.cpp:1266
critical [Main] DEBUG ASSERT: "pFromDeck && pToDeck" in function void AutoDJProcessor::calculateTransition(DeckAttributes*, DeckAttributes*, bool) at ./src/library/autodj/autodjprocessor.cpp:1266

Thread 1 "mixxx" received signal SIGSEGV, Segmentation fault.
AutoDJProcessor::playerTrackLoaded (this=0x55555d432130, pDeck=0x55555f54e5b0, pTrack=std::shared_ptr<Track> (use count 16, weak count 1) = {...}) at /home/owen/src/github/mixxx/src/library/autodj/autodjprocessor.cpp:1623
1623	        if (!fromDeck->isPlaying() && fromDeck->playPosition() >= 1.0) {
(gdb) bt
#0  AutoDJProcessor::playerTrackLoaded (this=0x55555d432130, pDeck=0x55555f54e5b0, pTrack=std::shared_ptr<Track> (use count 16, weak count 1) = {...}) at /home/owen/src/github/mixxx/src/library/autodj/autodjprocessor.cpp:1623
#1  0x0000555555fe4c59 in QtPrivate::FunctorCall<QtPrivate::IndexesList<0, 1>, QtPrivate::List<DeckAttributes*, std::shared_ptr<Track> >, void, void (AutoDJProcessor::*)(DeckAttributes*, std::shared_ptr<Track>)>::call
    (arg=0x7fffffffcdf0, o=0x55555d432130, f=<optimized out>) at /usr/include/x86_64-linux-gnu/qt6/QtCore/qobjectdefs_impl.h:135
#2  QtPrivate::FunctionPointer<void (AutoDJProcessor::*)(DeckAttributes*, std::shared_ptr<Track>)>::call<QtPrivate::List<DeckAttributes*, std::shared_ptr<Track> >, void> (arg=0x7fffffffcdf0, o=0x55555d432130, f=<optimized out>)
    at /usr/include/x86_64-linux-gnu/qt6/QtCore/qobjectdefs_impl.h:172
#3  QtPrivate::QSlotObject<void (AutoDJProcessor::*)(DeckAttributes*, std::shared_ptr<Track>), QtPrivate::List<DeckAttributes*, std::shared_ptr<Track> >, void>::impl
    (which=<optimized out>, this_=<optimized out>, r=0x55555d432130, a=0x7fffffffcdf0, ret=<optimized out>) at /usr/include/x86_64-linux-gnu/qt6/QtCore/qobjectdefs_impl.h:383
#4  0x00007ffff1f83d9b in ??? () at /lib/x86_64-linux-gnu/libQt6Core.so.6
#5  0x0000555555fd4430 in DeckAttributes::trackLoaded (_t2=std::shared_ptr<Track> (use count 16, weak count 1) = {...}, _t1=<optimized out>, this=<optimized out>)
    at /home/owen/src/github/mixxx/cbuild/mixxx-lib_autog

*[truncated]*

---

## #15954: crash during track load

**Labels:** critical bug, crash

### Bug Description

this is with a pretty custom branch but the crash itself is in waveform code. I'll attach a backtrace

this feels similar to the last time I found a crasher, when hitting quantize: https://github.com/mixxxdj/mixxx/issues/11709



### Version

_No response_

### OS

_No response_

---

## #15953: Epic: Replace all code that needs qt5compat

Currently we need qt5compat for, but qtcompat is deprecated an will be removed in future Qt releases:

- [ ] big-codecs
- [ ] codecs
- [ ] qml
- [ ] textcodec

---

## #15950: Crash Win On Wayland

**Labels:** party stopper, waveform

### Bug Description

I had a probably waveform related crash with the current main. 
The crash happens spontaneously in the middle of a track without touching anything. This is the tail of mixxx.log:  

```
debug [Main] Processing QEvent::FutureCallOut for object QFutureWatcherBase(0x5c8128f33c20) running in thread: "Main" took 10 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 14 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 13 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 14 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 13 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 14 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 17 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 13 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 15 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 10 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 12 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 10 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 18 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 12 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 12 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 11 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 13 ms
debug [Main] Processing QEvent::MetaCall for object WaveformWidgetFactory(0x5c80fdaabd00) running in thread: "Main" took 18 ms
corrupted size vs. prev_size while consolidating
```

Wayland 
4.6 (Compatibility Profile) Mesa 23.2.1-1ubuntu3.1~22.04.3 (Mesa Intel(R) Graphics (MTL))

RGB accelerated stereo waveforms 

I have tried to reproduce the issue but is a one time crasher so far. Also GDB does not crash.  

### Version

2.7-alpha 

### OS

Ubuntu Jammy

---

## #15946: Make available the ID/names of the FX loaded on the FX rack (as well as their controlling parameters)

### Feature Description

Trying to simulate a beat/quantize function for my beat knob by linking it to specific parameter controls in each FX, but mixxx doesn't provide these for the loaded FX, so would be great to have something like:

    [EffectRack1_EffectUnit1_Effect1],effect_name (read-only string)
    [EffectRack1_EffectUnit1_Effect1],effect_id (read-only string)

---

## #15943: Option to reset Quick Effect knob on track load

### Feature Description

Currently (tested in version 2.5.4), Mixxx has a preference (Preferences > Mixer > Deck Equalizers section) to reset the EQ or gain on track load to the default center position.
However, it seems that there is no way to automatically reset the Quick Effect knob to the middle position as well. For my workflow, this would be helpful and also consistent with the behavior of the other knobs when using the auto-reset option.

---

## #15933: Add "Spiral" filter to FX

**Labels:** effects, easy, confirmed

### Feature Description

Can this implementation of the Spiral filter in mixxx be introduced as a single FX? 

**edit** (ronso0) forum reference, Spiral proposal by @Be-ing https://mixxx.discourse.group/t/pioneer-spiral-fx-equivalent/18156/2
<img width="753" height="449" alt="Image" src="https://github.com/user-attachments/assets/645bcaa6-6c9e-4435-a219-734071b11ffb" />

Using a whole rack just for a single effect is annoying if you arent a single trick pony lol

---

## #15930: General analysis issues. Including freezing with loading new tracks that already have analysis metadata

### Bug Description

The analysis engine really kills the program making it unusable when importing new files. Even when loading tracks that were already analyzed by either mixxx on another pc, or another software (rb, serato) don't display their parameters, and force an analysis to get bpm/key data (this doesnt happen with all files tho, some appear with their data some not).

Isnt there a way to separate the processing load from the mixing and the analyzing engines so they don't overlap, or maybe introduce a CPU threshold for analysis that doesnt bleed onto the rest of the software making it a background process? 

### Version

2.6

### OS

win11 ltsc

---

## #15928: Mixxx issues when using Rekordbox's playlist from USBs exported for Pioneer consoles.

**Labels:** library, analyzer, rekordbox

### Bug Description

Had another event with forced Mixxx use on random DJS >:D . This time with four RB users.

The  discovered issues:

1. When loading USB Rekordbox playlists exported for Pioneer consoles, the program freezes **like hell** in what seems as an incredibly unoptimized analysis processing on tracks that are supposedly already analyzed for bpm, keys, grids, etc by rekordbox. The freezing times were worse on older USBs (And I thought Serato was a PITA when playing and analyzing the library of the next DJ at the same time).
2. When files were WAV this was **WAY WORSE**, had to basically alt+f4 a handful of times. 
3. Playlist/Crates functions not available when accessing the playlists from the USBs themselves (songs werent marked as played for example)
4. Grids/tempo behaved weirdly on some tracks (they basically changed real time on progressive house tracks with constant tempo that didn't present this behavior on consoles/rekordbox).





### Version

2.6

### OS

W11 LTSC

---

## #15925: add option to disable Sync half/double feature

### Feature Description

Aparently it's not always desired to auto-halve/double BPM when syncing, see https://mixxx.discourse.group/t/turning-off-half-double-bpm-sync/33250

What about adding an option to Preferences -> Decks for this?

---

## #15921: wording of disable library "rescan on start" option forgets there is another kind of library rescan on start. also; add option to disable the other rescan?

### Bug Description

checking for new files is a scan

checking for missing files is a scan

disabling the "rescan on start" option still results in Mixxx still rescanning on start to check library files exist, with a progress dialog

a) the option needs better wording to properly describe what the change is and what what it is not

b) it would be great to be able to disable the missing file rescan on start and have the failure highlighted on attempted file load

(idk why it is that no missing file track text loads in the library after the missing scan finishes, but then next start it does load, because there is no change in what Mixxx knows after the point of the end of the scan, so it can surely display all missing tracks as red from there on? or maybe I missed or misremember something)

### Version

_No response_

### OS

_No response_

---

## #15916: Flathub Version Out of Date

Current version in Flathub is 2.52 instead of the current stable release 2.54

---

## #15913: Auto DJ: Intermittently ignores negative transition offset and starts at Cue point

**Labels:** autodj

### Bug Description

I am using Auto DJ with a -3.0s transition time (to create a 3-second gap between tracks) and the "Cut Silence" option enabled.
I have identified a specific bug in how Mixxx determines the start position of the incoming track. Normally, Mixxx identifies the first sound (Cue point) and starts the track 3 seconds before that point (the gap). However, randomly (every few tracks), Mixxx ignores this -3s offset and triggers the incoming track exactly at the Cue point, resulting in no gap at all.

Expected Behavior: Mixxx should consistently apply the negative transition offset (-3s) relative to the detected Cue point of every incoming track.
Attached Log: I have attached my mixxx.log from a session where this occurred.
Thank you for looking into this!

[mixxx.log](https://github.com/user-attachments/files/24880455/mixxx.log)

### Version

2.5.4

### OS

macOS Sequoia 15.7.3

---

## #15911: Detect track/song structure

### Feature Description

Would be nice to detect track structure to understand better the song/track and where to enter/exit.

---

## #15910: Allow move/drag playlist to crates

**Labels:** library, playlist

### Feature Description

Now you have to export playlist if you want to move to a crate (in catalan is called "caixes").

---

## #15909: Allow to change playlist/crate sort order

**Labels:** library, confirmed, playlist

### Feature Description

Could be nice to could sort playlists by name

---

## #15908: Unable to use DJ Control MP3 E2 on macOS (2.5.4)

**Labels:** macos, controller backend

### Bug Description

Controller is recognized and visible in the settings panel, but moving a controller doesn't do anything at all. Looking at the controller debugging logs:

```
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " serial # "" - LIBUSB_ERROR_NOT_FOUND
 controller.djcontrolmp3e2.output:warning [Controller] Unable to send data to "DJ Control MP3 e2 " s

*[truncated]*

---

## #15900: Mixxx does not find 3rd party LV2 plugins

**Labels:** effects, linux

### Bug Description

Mixxx seems to ignore installed LV2 plugins instead of showing them.

Stept to reproduce:

- Install Mixxx 2.5.2
- Install chowtape 2.11.1
  - This places the plugin into /usr/lib/lv2/CHOWTapeModel.lv2/CHOWTapeModel.so
- Starting Mixxx
  - Checking in Preferences - Effects - Visible Effects: This lists plenty of LV2 plugins, but Chowtape is missing
  - Running Mixxx with --log-level trace and --developer generates lots of output. Scanning for 'LV2' shows the built-in plugins, but no hint of Chowtape or Mixxx scanning a directory for more plugins.

It looks like Mixxx is silently ignoring the LV2 plugin.

It looks like I'm not the only affected user: https://www.reddit.com/r/MIXXX/comments/1qkpi88/has_anyone_gotten_lv2_effects_in_linux_working_or/

### Version

2.5.2

### OS

Linux Ubuntu 22.04 LTS

---

## #15892: Echoing when playing music on live broadcast

### Bug Description

Pls help ... listeners complaining that when music is played it is echoing  . and one said echoing may be overdubbed. 


### Version

_No response_

### OS

_No response_

---
