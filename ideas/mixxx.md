# Mixxx — Project Ideas

**Source:** https://github.com/mixxxdj/mixxx/wiki/GSOC-2026-Ideas
**Scraped:** 2026-02-22T23:28:47.631039

---

## Student Project Ideas for Google Summer of Code 2026

This page lists the suggested tasks to build a 90 hour (small sized) a 175 hour (medium sized) or 350 hour (large) project for [Google Summer of Code 2026](https://summerofcode.withgoogle.com/). The ideas are already assigned to example projects, but you are encouraged to use them for building your own project adding your own ideas and make it suit perfectly to you, your skills and your time line.

If you are interested in applying to GSoC, read [GSoC Advice](/ideas/mixxx/gsocadvice)
before applying or getting involved. Only beginner contributors that are active members
of the Mixxx community are accepted. If this is not the case yet, just
say hello at <https://mixxx.zulipchat.com> and discuss your Ideas and
discus cases with us.

# Adding an AI infrastructure with cross-platform hardware acceleration

Typical AI applications in the DJ environment (STEM separation, music analysis) require very high computing power. However, as the commercial DJ software DJay Pro demonstrates, it is possible to perform these on modern laptop hardware in real time with high audio quality. This is made possible by the use of the dedicated Neural Processing Unit (NPU) or powerful Graphical Processing Units (GPU).
As cross-platform software, Mixxx must be able to do this on:
* macOS (ARM M1/2 with Neural Engine NPU)
* macOS (x64 with GPU only)
* Linux with various NPU and GPU solutions from different manufacturers
* Windows with various NPU and GPU solutions from different manufacturers

Today, there is only one AI framework that supports full hardware acceleration across all these platforms, which is ONNX Runtime ([onnxruntime.ai](/ideas/mixxx/onnxruntime-ai)).
In GSoC 2025, our student Anmol Mishra not only converted the widely recognized best STEM separation model DEMUCS to ONNX, but also benchmarked the achievable performance on different hardware: https://mixxx.org/news/2025-10-27-gsoc2025-demucs-to-onnx-dhunstack/ 
As successor, this project is about the integration of ONNX Runtime with ExecutionProviders for CPU (all operating systems), as well as at least one NPU or GPU acceleration solution into Mixxx.
This project explicitly includes contributions to third-party projects, in particular to the package managers VCPKG and the Linux distribution Debian/Ubuntu, which Mixxx uses to integrate dependencies.
A further aspect to handle is, that these libraries, as well as, the AI models itself are significiantly larger than the current dependencies that come with Mixxx. This requires the development of suitable solutions for the continuous code integration (CI) and for the distribution to the end users.
* **Expected Outcome:** ONNX Runtime with ExecutionProviders for CPU (all operating systems), as well as at least one NPU or GPU acceleration solution builds within the Mixxx environment. All changes on third-party code is contributed upstream to the particuar projects. Our ONNX DEMUCS model is executable in Mixxx.
* **Skills:** Knowledge of CMake, C++. Basic experience with contributing packages to package managers/Linux distributions.
* **Possible Mentor:** Jörg
* **Difficulty:** Medium 
* **Size:** 350 h

# AI music analyzer to detect Beats, Downbeats, Phrases

While Mixxx has a solid analyzer for beat/tempo detection, it is traditionally DSP-based, while the state of the art has moved to a hybrid approach of AI models that include some DSP routines for data pre-processing. Commercial DJ software with such AI music analyzers (DJay Pro, DJ Studio) demonstrates virtually always perfect beat recognition in DJ Medien's tests, even on challenging tracks with a variety of tempo changes.
There are OpenSource music analyzer models available, nanmely https://github.com/JoergAtGithub/all-in-one (https://huggingface.co/spaces/taejunkim/all-in-one / https://taejun.kim/music-dissector/0427_justthewayyouare). While a science project with impressive results, this is a PyTorch model that cannot be used in a C++ project with support for any kind of acceleration hardware (it's based on the Demucs HT model above), also here an ONNX model is needed.
This project is about building an infrastructure that allows Mixxx developers to optimize the analyzer, check the correctness of the results and generate production-ready ONNX models for the Mixxx DJ software in an automated workflow.
In particular, the process when a user reports a track with incorrectly detected beats/downbeats/phrase-length/phrase-type and we need to optimize the model needs to be implemented. The main focus of this process is to ensure that the optimization for one track does not lead to worse recognition for other tracks.
* **Skills:** Knowledge of C/C++. Sound experience with the creation of AI models - preferably in ONNX.
* **Possible Mentor:** Daniel Schürmann 
* **Difficulty:** Difficult
* **Size:** 175 h

# Using The Harmonix Set to automatically evaluate the output of our music analyzers 
The Harmonix Set [https://github.com/urinieto/harmonixset](https://github.com/urinieto/harmonixset) repository contains human annotated labels for 912 Western Pop music tracks. This is a great base to benchmark current and future music analyzers in Mixxx.
This project is about the automatic execution of the Mixxx Analyzer in a local development environment using all tracks of the Harmonix Set, that are available on the developer's local hard disk and generate a report that visualizes the deviations.

* **Expected Outcome:** A lightweight tool or script that can be executed out-of-the-box on Windows, macOS and Linux.
* **Skills:** Experience C++ and a common scripting environment like Python
* **Music files:** The Mixxx project cannot provide the music files, so the students must have a larger number of the music files listed in The Harmonix Set available themselves.
* **Possible Mentor:** Jörg
* **Difficulty:** Easy
* **Size:** 175 h

# Graphical representation of BPM and Musical Keys in the waveform

Nowadays DJs depend more and more on visual information and metadata than on their ears and knowledge of music/tracks. Features that once were gimmicks or nice-to-haves became for a lot of DJs relying info, for others crucial.
Information as BPM and Musical Key is displayed as an one-value-field showing the most occuring / average value.
This project is about displaying the complete detailed information.
Goals: 
* BPM is now displayed as a single value, while the analysis results in a detailed overview of the beat positions, a consistent graphical representaion of the analysed BPMvalues (eg with use of Savitzky-Golay filter) as an optional overlay in the waveform. In this way the DJ will be able to see the BPM changes (Break, bridge, intermezzo) and the correct values in the waveform.
* Musical KEY is now displayed a single value while the analysis results in a detailed list of KEYS, eg refrain, bridge, break, instrumental break, intermezzo can have a different (not displayed) key. The DJ should have the option to view a graphical representation of the musical Keys in the waveform.
* As the BPM & Key representation in the waveform require a points in the waveform where the values change, these points should be showed on the waveform as POIs (Points of Interest): BPM-Change-Points & Key-Change-Points, the DJ should have the possibility to display these points, and eventually create hotcues, loops, beatjumps ... based on the position of these points.
* The data to create the graphical representation of BPM-curve, Musical KEY-curve and POIs needs to be saved in an interchangeable format for easy recreation on other systems, other CMRT (see other GSoC idea)

* **Expected Outcome:** A new visual representation of changing keys and BPMs. 
* **Skills:** Experience C++ and user interface design, OpenGL 
* **Possible Mentor:** Evelynne, Daniel 
* **Difficulty:** Medium
* **Size:** 175 h

# Cannonical Master Release Track based on the complete Chroma-Fingerprint of the track

First step in the process to share advanced DJ-metadata. This is a combined Project with MetaBrains to implement a subcluster for Cannonical Master Release Track. First step in the process to share advanced DJ-metadata.

At the moment the link between AcoustId and the MusicBrainsDatabase has a shortage: Tracks with a different mastering are linked to the same AcoustId resulting in the same MBID (MusicBrainsID) for different versions/masterings of the same track. 
In this project we want to solve this issue by creating sub-clusters clustering the same masterings in the parent MBID-cluster.
* Herefore we need to use the complete Chromaprint-Fingerprint to identify and distinguish the different masterings of a track (Cannonical Master Release Track) eg the 'Original Album'-Mastering, '7inch'-mastering, 'best of'-mastering, 'streaming'-mastering, 'video'-mastering, 'Various Artists Album'-mastering.
* In the Mixxx-analysis procedure we need to calculate the complete Chromaprint-Fingerprint and save it in a new table in the the MixxxDB together with the FingerprintDATE, Offset (pregap) and MBID.
* If the user accepts (preferences) to use & share information anonymously from/with MB, the complete fingerprint in combination with other metadata is shared/compared with information in the MBDB. If the CMRT-sub cluster (CMRT) with the complete fingerprint is already present, the offset can be calculated (pregap) and needs to be saved. 

* **Expected Outcome:**
  * Add a new table in the MixxxDB with advanced trackmetadata (complete Chromaprint-Fingerprint..)
  * Find exact doubles in the collection of the user (based on complete fingerprint)
* **Future featurese:**
  * Upgrade versions in the collection (eg replace a lossy version with the lossless verwion of the same mastering)
  * Add a new sub-clusteringsystem based on the complete Chromaprint-fingerprint in the MusicBrainsDB
  * Expand the current MusicBrainsLookup in Mixxx to retrieve and save the advanced Metadata.
  * Interchange advanced DJ-metadata through the MBDB (BPM, Musical Key...)
* **Expected Outcome:** A new visual representation of changing keys and BPMs. 
* **Skills:** Experience C++ and Database Postgres Sqlite 
* **Possible Mentor:** Evelynne, Daniel 
* **Difficulty:** Medium
* **Size:** 175 h  (or more depending on the project proposal)

# Auto completion for the Genre track metadata

Mixxx allows to assign a Genre to a track. This is currently a free text field that allows different spellings for the same Genre like Hiphop, Hip-Hop or Hip Hop. If you use all of these, you will not see all tracks when filtering. This project shall fix it. 

We have started this project last year and did some important steps regarding requirement engineering and data modeling. We initially underestimated the required work, so we have decided to split it up. The first phase ended with a working prototype not merged into the Mixxx source code.

This year we like to revise the requirement and decision by testing the prototype and start over making use of the good foundation we have created.    

The project may feature 
 * auto-complete the Genre when entering
 * add multiple Genres to a track
 * Backed up by an N-N genres relationship tree/net 
 * Genre Import from Discogs and [MusicBrainz](https://musicbrainz.org/genres) 

It is up to the contributor to focus on one ore more topic that the project scope is kept small and the goal code get merged.  

[Last years project description](/ideas/mixxx/mixxxdj-mixxx-issues-14897) 

* **Expected Outcome:** A new auto completer for the Genre edit box
* **Skills:** Basic SQLite, Good C++
* **Possible Mentor:** Daniel Schürmann
* **Difficulty:** Medium 
* **Size:** 90 h

# Rebuild the LateNight theme in QML

As we continue our work to rebuild the Mixxx UI in QML and aim to delivering a fresh user experience, we also aim to rebuild our iconic LateNight theme in QML. This will let users who prefer the classic look return to the familiar 2.x experience.

The project focuses on two key areas:
- Rebuilding all components, using the legacy components using our QWidget rendering stack, with the XML definition and style sheet serving as reference for acceptance criteria.
- Extend the C++/QML API for needed behaviour.
- Collaborating with other maintainers to develop the core theme-loading system, enabling future custom themes managed by individuals or the community.

* **Expected Outcome:** A LateNight QML theme.
* **Skills:** Basic QML and Basic C++
* **Possible Mentor:** Antoine
* **Difficulty:** Medium 
* **Size:** 350 h

# Replace the outdated portmidi library in Mixxx by libremidi
Since the begining, Mixxx uses portmidi [https://github.com/PortMidi/portmidi](https://github.com/PortMidi/portmidi) to implement the low-level MIDI communcation over USB. This cross-platform library is written in C and has a very limited feature set.
With the upcomming of the [MIDI 2.0](https://en.wikipedia.org/wiki/MIDI_2.0) standard, Mixxx needs to switch to another libray for MIDI communication. The library of choice is [https://github.com/celtera/libremidi](https://github.com/celtera/libremidi), a cross-platform MIDI library written in modern C++. libremidi offers not only MIDI and MIDI 2.0 on all platforms, but also much more sophisticated support features for device detection and hot-plugging.
As there are hundreds of MIDI mappings for Mixxx out in the field, the main point of this work is to achieve 100% compatibility. This project is not about using the new features of libremidi yet.
The project should start with improving the automatic test cases for MIDI. Once this is done, the library change itself should be done.

* **Expected Outcome:** A fully compatible Midi implementation using libremidi, with compatibility proven by systematic tests 
* **Skills:** Experience in C++ and accessing USB-MIDI devices
* **Hardware:** The Mixxx project cannot provide hardware. The student must own at least one USB-MIDI device, preferable a DJ controller.
* **Computer:** The student should have access to computers of at least two of the Mixxx supported platforms: Linux, macOS or Windows
* **Possible Mentor:** Jörg
* **Difficulty:** Medium
* **Size:** 175 h


# Test our controller scripting libraries using Fuzzing
Mixxx contains several JavaScript libraries (like [https://github.com/mixxxdj/mixxx/blob/main/res/controllers/midi-components-0.0.js](https://github.com/mixxxdj/mixxx/blob/main/res/controllers/midi-components-0.0.js)) which allow a wide area of inputs and complex decision trees. Fuzzing seems to be a promissing method to detect flaws in these libraries. 
Googles https://github.com/google/oss-fuzz might be a good platform for such a setup.

* **Expected Outcome:** A working Fuzzing setup for all JavaScript libraries in the Mixxx controller code and the proper fix of some detect bugs
* **Skills:** Practical experience with Fuzzing and systematic software testing
* **Possible Mentor:** tbd.
* **Difficulty:** Medium
* **Size:** 175 h

# Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it. We recommend
spending more than a few days using Mixxx and participating in the
community to develop a better understanding of areas where Mixxx could
use improvement. Our issue tracker is full of [feature requests](/ideas/mixxx/mixxxdj-mixxx-issues) and other
ideas scattered throughout, so if you browse through it, you may find
many more ideas for GSoC projects.

**IMPORTANT: You should [contact us](/ideas/mixxx/gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!** We
very rarely approve ideas students propose. If you're not already
experienced with DJ equipment, we recommend sticking with one of the
ideas above.
