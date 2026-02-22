# feature requests

**Parent:** Mixxx — Project Ideas
**Source:** https://github.com/mixxxdj/mixxx/issues?q=is%3Aopen+is%3Aissue+label%3Afeature
**Scraped:** 2026-02-22T23:28:47.631497

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

## #16008: Heap corruption crash with main

### Bug Description

This happens with current main 

double free or corruption (out)
```
#0  __pthread_kill_implementation (no_tid=0, signo=6, threadid=140728814523968) at ./nptl/pthread_kill.c:44
#1  __pthread_kill_internal (signo=6, threadid=140728814523968) at ./nptl/pthread_kill.c:78
#2  __GI___pthread_kill (threadid=140728814523968, signo=signo@entry=6) at ./nptl/pthread_kill.c:89
#3  0x00007ffff1e42476 in __GI_raise (sig=sig@entry=6) at ../sysdeps/posix/raise.c:26
#4  0x00007ffff1e287f3 in __GI_abort () at ./stdlib/abort.c:79
#5  0x00007ffff1e89677 in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7ffff1fdbb77 "%s\n") at ../sysdeps/posix/libc_fatal.c:156
#6  0x00007ffff1ea0cfc in malloc_printerr (str=str@entry=0x7ffff1fde790 "double free or corruption (out)") at ./malloc/malloc.c:5666
#7  0x00007ffff1ea2e70 in _int_free (av=0x7ffff201ac80 <main_arena>, p=0x7ffde0015110, have_lock=<optimized out>) at ./malloc/malloc.c:4588
#8  0x00007ffff1ea56ad in __GI___libc_free (mem=<optimized out>) at ./malloc/malloc.c:3391
#9  tcache_thread_shutdown () at ./malloc/malloc.c:3227
#10 __malloc_arena_thread_freeres () at ./malloc/arena.c:1003
#11 0x00007ffff1ea81ca in __libc_thread_freeres () at ./malloc/thread-freeres.c:44
#12 0x00007ffff1e9494f in start_thread (arg=<optimized out>) at ./nptl/pthread_create.c:456
#13 0x00007ffff1f268d0 in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:81
``` 

### Version

main 

### OS

Ubuntu Jammy

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

## #15998: DDJ-FLX4: SHIFT+CUE should jump to track start and pause

### Bug Description

On DDJ-FLX4, pressing SHIFT+CUE jumps to beginning of the track and starts playing (see code [here](https://github.com/mixxxdj/mixxx/blob/a3a4bc4efae4f6064203b735b0123cf17366ad31/res/controllers/Pioneer-DDJ-FLX4.midi.xml#L160) and [here](https://github.com/mixxxdj/mixxx/blob/a3a4bc4efae4f6064203b735b0123cf17366ad31/res/controllers/Pioneer-DDJ-FLX4.midi.xml#L180)). This behavior is:

* mildly inconvenient - at least to me, jumping to start is a preparatory action so it seems more useful/expected _not_ to play automatically
* inconsistent with regular CUE (without SHIFT) - pressing CUE jumps to main cue point and _pauses_ playing
* inconsistent with virtually all other controller mappings where SHIFT+CUE jumps to track start and pauses (indeed, jumping to track start and pausing is the default action of SHIFT+CUE in the Components library, so any mapping based on it will behave this way unless modified explicitly)

I suggest mapping SHIFT+CUE to `start_stop` rather than `start_play`. It's a trivial modification, so I can submit a PR, but I'm fairly new to mixxx, so I'd like to have someone confirm first that my suggestion is sensible.

I don't use Windows, so I did not check how Rekordbox or Serato behave, but I did test it on Rekordbox Android app. In that one, SHIFT+CUE jumps to track start but does not affect the playing status: if the track was playing before, it resumes playing; if it was paused, it remains paused. However, given that most mixxx mappings map to `start_stop` (which also sounds the most logical to me), I'm still strongly leaning towards sticking to such behavior with DDJ-FLX4 as well.

### Version

2.5.4

### OS

Linux (Gentoo)

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
          <script-binding/>
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

## #15896: Sample deck/Jingles

### Bug Description

 Volume is resetting every time, the first 2 row only and the rest stay's steady

### Version

_No response_

### OS

Windows 11

---

## #15892: Echoing when playing music on live broadcast

### Bug Description

Pls help ... listeners complaining that when music is played it is echoing  . and one said echoing may be overdubbed. 


### Version

_No response_

### OS

_No response_

---

## #15886: Stopping and starting with long audio buffer causes a waveform shake

### Bug Description

When pressing pause, the waveform jumps one bugger size ahead. When starting again it jumps back the same amount. This is only a visual issue, probably cause by the anti waveform jerking filter. that predicts future waveform positions. 

### Version

2.5.4

### OS

All

---

## #15882: Cover art is not shown

### Bug Description

<img width="2880" height="1920" alt="Image" src="https://github.com/user-attachments/assets/feed37f2-67c4-434a-896f-a7392378d5cf" />

As you see this happened in Auto-DJ mode. I have this issue like once every two weeks. 
When I load the file again the cover is shown

### Version

2.6 beta

### OS

Ubuntu Studio 25.10

---

## #15879: Please add SHOUTcast Version 2 Streaming

### Feature Description

Greetings, I have not been able to connect to my SHOUTcast Server on Mixxx with the SHOUTcast v1. The stream has no Login/Username, so why does it have a field for "Login" ? Only the Server login on the server website has a username.  Why doesn't Mixxx have the V2.x mode option? Also why does it have a "Mount" field instead of a "Stream ID" field ?

<img width="382" height="262" alt="Image" src="https://github.com/user-attachments/assets/f832f4cc-7547-4f6e-992f-db5d8253cbd6" />

Streaming on WinAmp with the SHOUTcast Source DSP actually works. Although WinAmp does keep building up RAM usage indefinitely and eventually crashes. 
<img width="322" height="521" alt="Image" src="https://github.com/user-attachments/assets/c580efdf-29b2-4c7a-8a82-faaf34871faa" />

By the way, can both the Feature and Bug tags be added to the same issue post? 

Thank you, Shalom.

---

## #15873: Test failure on ARM 64 Windows 11: SoundSourceProxyTest.regressionTestCachingReaderChunkJumpForward

**Labels:** windows, crash, soundsource

### Bug Description

https://github.com/mixxxdj/mixxx/actions/runs/21100430613/job/60683840310
```
2026-01-17T20:48:05.7963259Z info [Qt mainThread] Opened file "C:/a/mixxx/mixxx/src/test/id3-test-data/cover-test-itunes-12.3.0-aac.m4a" using provider "Microsoft Media Foundation 10.0.26100.7309"
2026-01-17T20:48:05.7964779Z unknown file: error: SEH exception with code 0xc0000005 thrown in the test body.
```



### Version

_No response_

### OS

_No response_

---

## #15871: BPM-normalized keys

**Labels:** confirmed

### Context  

The context is about using the keys information to select the next track. It's sometimes called "mixing in key", but this is confusing a method with the desired result.  

I have noticed that I can sometimes wonder "chat about this track?", and see that its key does not match with the playing key, but once decelerated/accelerated to the playing BPM,  it does.

So now I have in mind that:  

- accelerating a tracks changes the key by +7 or -5
- decelerating a tracks changes the key by +5 or -7

and I sometimes check if I can find a track in these extra BPM ranges.

I wondered if it was possible to bring this idea in Mixxx and… 

### (Potential) solution

It might be a good idea to create a "BPM-normalized key".  
So something like `KEY_100 = key(freq(KEY) * 100 / BPM)`.
Where:

- `KEY` and `BPM` are the track values (from the library)
- `KEY_100`  is the BPM-normalized key (on 100 BPM for example)  
- `key` and `freq` are conversion functions

So this is information is computed only once, right after the BPM and KEY analysis, and can be therefore be stored in the library.

### (Potential) use

I have considered two search option:

1. ordering the library by `BPM`/`KEY` so it's easy to find potential track to mix by simply navigating 
2. using the "similar track" search (right lick on the track)

In both case we could use `KEY_100` instead of the `KEY`.

This would allow to find this extra tracks that are at the proper key once adjusted to the mix BPM.

### Final

Note that I might be able to edit the code myself, but first I need to be sure this idea is good, and then I need clear instructions (especially which files needs to be edited).

Cheers!

---

## #15869: Feature Request: Configurable metadata broadcast volume threshold for live streaming

**Labels:** easy, confirmed, broadcast

### Feature Description

**Problem:**
When live streaming/broadcasting, Mixxx updates metadata based on which deck has the highest volume every second. The current hardcoded threshold is 20% volume before a track is considered "audible."

For techno/minimal mixing styles that use long blends with extended drum layering at 70-80% volume, this causes metadata to flip back and forth repeatedly between tracks during transitions, spamming incorrect track names to the stream/chat.

**Current Behavior:**
- Track metadata updates based on highest volume deck
- 20% volume threshold is hardcoded
- Updates happen every second
- No user control over when metadata broadcasts

**Requested Feature:**
Add a preference setting under Preferences → Live Broadcasting to control metadata updates:

1: Adjustable volume threshold slider (20% - 90%)
2: Manual metadata update control (button/hotkey to trigger metadata change)
 3: Delay timer (e.g., "only update if track stays loudest for X seconds")

**Use Case:**
I DJ techno /house live in virtual worlds (Open Simulator) where track metadata displays in nearby chat. During long blends or mashups where I layer drums from the next track at 70-80% (or full) volume, the current system causes track names to spam back and forth in chat every time I adjust faders, which is confusing for listeners.

**Additional Context:**
This primarily affects DJs who:
- Don't use crossfaders
- Do extended blends and mashups with channel faders
- Layer elements at high volume before full transitions
- Stream to platforms that display "now playing" metadata

---

## #15868: repetetive track lookup when opening track menu

### Bug Description

When I right-click a track in the library (Tracks) to open the track menu I see 7 failed attempts to resolve the track, the 8th succeeds

I see this 7 times, note `Evicting track` and `Deleting Track`
```
debug [Main] GlobalTrackCache - Resolving track by id 134620
debug [Main] GlobalTrackCache - Resolving track by canonical location "/media/tracks/mid-side-mix-demo.flac"
debug [Main] GlobalTrackCache - Cache miss - allocating track  TrackRef {"/media/tracks/mid-side-mix-demo.flac","/media/tracks/mid-side-mix-demo.flac",134620}
debug [Main] GlobalTrackCache - Cache miss - inserting new track into cache  TrackRef {"/media/tracks/mid-side-mix-demo.flac","/media/tracks/mid-side-mix-demo.flac",134620} QObject(0x0)
debug [Main] Successfully deserialized Beats ("BeatGrid-2.0")
debug [Main] Successfully deserialized KeyMap
debug [Main] SoundSourceProxy - SoundSourceProvider "Xiph.org libFLAC" created a SoundSource for file "/media/tracks/mid-side-mix-demo.flac" of type "flac"
debug [Main] BaseTrackCache(0x55bb8a740470) updateIndexWithQuery took 1 ms
debug [Main] GlobalTrackCache - Evicting track  TrackRef {"/media/tracks/mid-side-mix-demo.flac","/media/tracks/mid-side-mix-demo.flac",134620} Track(0x55bb84ec5680)
debug [Main] GlobalTrackCache - Deleting Track(0x55bb84ec5680)
```
then it succeeds
```
debug [Main] GlobalTrackCache - Resolving track by id 134620
debug [Main] GlobalTrackCache - Resolving track by canonical location "/media/tracks/mid-side-mix-demo.flac"
```

When I double-click to load I see the resolve part only once 🤷‍♂️ 

What's happening here?

### Version

2.6, didn't check 2.5

### OS

_No response_

---

## #15867: Peak detect

### Feature Description

Hi mixxx people,

I searched around this topic and didn't find, sorry if this was discussed earlier.
One nice and helpful feature for me would be mixxx being able to point out and/or highlight the loudest seconds in a track.
How should this happen ? Something visual or just a mm:ss hint or a marker or something else, idk.
If you don't like this because you think it would make mixxxers even more lazy, I'll take it  :D 

Thanks !

---

## #15866: Metadata corruption om MP4?

### Bug Description

I am not entirely sure if this is an issue with Mixxx, but thought I will open this to see if this has been happening to other users.

I have playlists with stems, with all of them correctly working when this playlist was created. However, it seems they are slowly stopping to function.

After investigation, it looks like the `stem` MP4 atom is getting some additional blank space added to it. 

For some context, every time you appends new metadata to an MP4, these will be added under the `udta` box. Because MP4 atoms contains offset to other atoms, this will require updating all offset, and may sometime lead to the creation of padding boxes (called `free`) to prevent doing this all the time. 
So in short, this could be an issue with TagLib.

I should also add that apart from Mixxx, I am not reading or editing these files with any other software (not audio library or tag editor) 

For reference, here is a valid STEM file, which loads in Mixxx:

<img width="1506" height="535" alt="Image" src="https://github.com/user-attachments/assets/5e63284a-4710-4521-9ffa-e21ac18bd767" />

Here is a corrupted one which used to load and now has this blank padding:

<img width="1506" height="594" alt="Image" src="https://github.com/user-attachments/assets/d16a7aa7-9452-4625-8187-7a6432248bec" />

## Note on workaround

To get them back working, I have added [a trim](https://doc.qt.io/qt-6/qstring.html#trimmed) to the box content to allow me continue using these stems. Not sure we want this workaround in `main``/2.6` as it would simply obfuscate a potentially larger issue we have with MP4 and tags.  

### Version

2.6

### OS

Fedora

---

## #15863: MIxxx crashes on OpenGLES2 only system, run directly on DRM/KMS (linux)

**Labels:** waveform

### Bug Description

Given a previous conversation about graphics acceleration in zulip, I compiled and tried to start Mixxx (latest master) on aarch64 with OpenGLES(-only) support via the DRM/KMS backend.

Qt environment was set to:
```
QT_QPA_PLATFORM=eglfs
QT_QPA_EGLFS_INTEGRATION=eglfs_kms
```

GDB backtrace on the (hopefully correct) current thread:
```
#0  __pthread_kill_implementation (threadid=281474805223456, signo=signo@entry=6, no_tid=no_tid@entry=0)
    at ./nptl/pthread_kill.c:44
#1  0x0000fffff22b7e64 in __pthread_kill_internal (threadid=<optimized out>, signo=6) at ./nptl/pthread_kill.c:89
#2  0x0000fffff2266980 in __GI_raise (sig=sig@entry=6) at ../sysdeps/posix/raise.c:26
#3  0x0000fffff2251ac4 in __GI_abort () at ./stdlib/abort.c:73
#4  0x0000fffff289c2d0 in ??? () at /lib/aarch64-linux-gnu/libQt6Core.so.6
#5  0x0000fffff287aae8 in QMessageLogger::fatal(char const*, ...) const () at /lib/aarch64-linux-gnu/libQt6Core.so.6
#6  0x0000ffffeb1dfef4 in QEglFSWindow::create() () at /lib/aarch64-linux-gnu/libQt6EglFSDeviceIntegration.so.6
#7  0x0000ffffeb1dff98 in QEglFSIntegration::createPlatformWindow(QWindow*) const ()
    at /lib/aarch64-linux-gnu/libQt6EglFSDeviceIntegration.so.6
#8  0x0000fffff30e3a8c in QWindowPrivate::create(bool) () at /lib/aarch64-linux-gnu/libQt6Gui.so.6
#9  0x0000fffff30e3eb0 in QWindowPrivate::setVisible(bool) () at /lib/aarch64-linux-gnu/libQt6Gui.so.6
#10 0x0000fffff4ceb6c4 in QWindowContainer::event(QEvent*) () at /lib/aarch64-linux-gnu/libQt6Widgets.so.6
#11 0x0000fffff4c82058 in QApplicationPrivate::notify_helper(QObject*, QEvent*) ()
    at /lib/aarch64-linux-gnu/libQt6Widgets.so.6
#12 0x0000aaaaab564718 in MixxxApplication::notify (this=0xfffffffff160, pTarget=0xaaaab6ee5910, pEvent=0xffffffffe9f8)
    at /home/mirko/src/mixxx/src/mixxxapplication.cpp:217
#13 0x0000fffff290e394 in QCoreApplication::notifyInternal2(QObject*, QEvent*) () at /lib/aarch64-linux-gnu/libQt6Core.so.6
#14 0x0000fffff4ccb040 in QWidgetPrivate::show_helper() () at /lib/aarch64-linux-gnu/libQt6Widgets.so.6
#15 0x0000fffff4ccc41c in QWidgetPrivate::setVisible(bool) () at /lib/aarch64-linux-gnu/libQt6Widgets.so.6
#16 0x0000aaaaab98284c in WGLWidget::showEvent (this=0xaaaab6d19ab0, event=0xffffffffede8)
    at /home/mirko/src/mixxx/src/widget/wglwidgetqopengl.cpp:44
#17 0x0000fffff4cce760 in QWidget::event(QEvent*) () at /lib/aarch64-linux-gnu/libQt6Widgets.so.6
#18 0x0000fffff4c82058 in QApplicationPrivate::notify_helper(QObject*, QEvent*) ()
    at /lib/aarch64-linux-gnu/libQt6Widgets.so.6
#19 0x0000aaaaab564718 in MixxxApplication::notify (this=0xfffffffff160, pTarget=0xaaaab6d19ab0, pEvent=0xffffffffede8)
    at /home/mirko/src/mixxx/src/mixxxapplication.cpp:217
#20 0x0000fffff290e394 in QCoreApplication::notifyInternal2(QObject*, QEvent*) () at /lib/aarch64-linux-gnu/libQt6Core.so.6
#21 0x0000fffff4ccb040 in QWidgetPrivate::show_helper() () at /lib/aarch64-linux-gnu/libQt6Widgets.so.6
#22 0x0000fffff4ccc41c in QWidgetPrivate:

*[truncated]*

---

## #15859: Loops: allow growing/shrinking by 1 beat

**Labels:** looping

### Feature Description

Uneven loop lengths allows some fun transitions (for tempo changes) but this is currently only possible with script functions afaik (or by typing sizes in beatloop size box of course)

Would be great to have `[ChannelN],beatloop_size_minus_one/_plus_one`.
Or make `beatloop_size` a ControlPotmeter with step size 1?

---

## #15858: Mixxx 2.5.4 (.deb/ppa) crashes on integrated Intel Graphics under Linux Mint 22.3

**Labels:** linux, crash

### Bug Description

Mixxx 2.5.4 (.deb/ppa) crashes on integrated Intel Graphics under Linux Mint 22.3.

The Problem occurs when starting AutoDJ Function. Another Notebook with integrated Radeon Graphics doesn't crash. Both have Linux Mint 22.3 installed. The affected Notebook has a Intel i5 - the Notebook without Crashes has a Ryzen 5. I can provide more Details if the Problem is not reproducable.

### Version

2.5.4

### OS

Linux Mint 22.3 x64

---

## #15857: need some explanation for the GUI freeze when closing multi-track properties dialog

### Bug Description

I know the GUI lag when updating tracks is currently inevitable.
However I don't understand when this happens.
I hope someone can explain it -- and maybe even propose a workaround.
Not sure if the issue is caused by DlgTrackInfoMulti..
It's created via WTrackTableView -> [WTrackMenu](https://github.com/mixxxdj/mixxx/blob/9c10a05ea775104700c9ae1b613d793cac87ee3c/src/widget/wtrackmenu.cpp#L2732)-L2743 -> DlgTrackInfoMulti

* select many tracks
* open Track Properties
* move dialog so you can see the tag column you're about to change
* change eg. Genre, Apply
  -> table view is updated quickly, freeze for ~.5 sec
* hit Cancel or Okay
  -> GUI freeze for 2-3 sec

Happens even if I don't have "Syncronize library track metadata from/to file tags" enabled.
-> delay is much longer when this is enabled

Furthermore I see _almost (!)_ all track rows being updated twice, at least according to calls of `WLibraryTableView::dataChanged`.

Log ===============================================

when applying, this is logged for each track:
```
debug [Main] BaseTrackCache(0x5614346d6090) updateIndexWithQuery took 0 ms
```

when clicking Cancel or Okay or Esc (hiding/closing DlgTrackInfoMulti), this is logged for each track:
```
debug [Main] GlobalTrackCache - Evicting track  TrackRef {"/media/das/some-track.mp3","/media/das/some-track.mp3",134550} Track(0x56145af5d430)
debug [Main] TrackCollectionManager - Saving track "/media/das/some-track.mp3" in internal collection
debug [Main] TrackDAO - TrackDAO: Saving track 134550 "/media/das/some-track.mp3"
debug [Main] TrackDAO - TrackDAO: Updating track in database 134550 "/media/das/some-track.mp3"
debug [Main] SqlTransaction - Started new SQL database transaction on "MIXXX-1"
debug [Main] SqlTransaction - Committed SQL database transaction on "MIXXX-1"
debug [Main] BaseTrackCache(0x5614346d6090) updateIndexWithQuery took 0 ms
debug [Main] GlobalTrackCache - Deleting Track(0x56145af5d430)
```
plus this one:
```
debug [Main] Processing QEvent::DeferredDelete for object 0x56145b048f90 took 2823 ms
```

### Version

_No response_

### OS

_No response_

---

## #15856: NS6 DJ Controller Mapping not Found

### Bug Description

Numark NS6II is there but not the NS6. Is there reason why?

Oh and I installed a Windows 10 driver of Numark NS6 for a Windows 11. Is there a more recent driver for my dj controller? Is this a windows 11 fault?

### Version

2.5.4

### OS

Windows 11

---

## #15855: CPU load indicated, when instead the soundsystem is causing lag

### Bug Description

<img width="3200" height="1080" alt="Image" src="https://github.com/user-attachments/assets/b402af8b-fbe0-4dcf-9321-eab24f51398b" />

mixxx goes into yellow "CPU LOAD" mode, without any cpu load at all.

The sound-sub-system, in this case pipewire, seem to be the real cause if the used output device has congestion.

This is of course very hard to determine on user and dev side, so i took a some screenshots who all show no load on the cores. I observed the issue with pw-top ( pipewire-top) showing some lag on the output device ( bluetooth in this case ). 

No idea if you can decide between cpu lag and audio sys lag. If you can, the indicator should be changed.

### Version

2.5.4

### OS

Fedora42

---
