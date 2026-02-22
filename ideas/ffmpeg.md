# FFmpeg — Project Ideas

**Source:** https://trac.ffmpeg.org/wiki/SponsoringPrograms/GSoC/2026
**Scraped:** 2026-02-22T23:28:47.584214

---

# Introduction[ ¶](https://trac.ffmpeg.org#Introduction)

FFmpeg is the universal multimedia toolkit: a complete, cross-platform solution to record, convert, filter, and stream audio and video. It is used by a number of media players (including VLC and MPlayer), video websites (including YouTube and Vimeo), web browsers (including Google Chrome/Chromium and Firefox), social media (including Facebook and Twitter) and countless other software projects in the multimedia field and beyond.

This is our ideas page for [Google Summer of Code 2026](https://summerofcode.withgoogle.com/). See the [GSoC Timeline](https://developers.google.com/open-source/gsoc/timeline) for important dates.

At the end of the program you can find all the results on the [results page](https://trac.ffmpeg.org/wiki/SponsoringPrograms/GSoC/2026/Results).

# Information for Students[ ¶](https://trac.ffmpeg.org#InformationforStudents)

## Getting Started[ ¶](https://trac.ffmpeg.org#GettingStarted)

**Get to know FFmpeg.**If you are a student interested in contributing to FFmpeg, it is recommended to start by subscribing to the[ffmpeg-devel](http://ffmpeg.org/mailman/listinfo/ffmpeg-devel)mailing-list,[Forgijo](https://code.ffmpeg.org/)and visiting our !Libera.Chat IRC channels (*#ffmpeg-devel*and*#ffmpeg*although you will find most developers on the first one), and exploring both the codebase and the development workflow. Feel free to[contact us](https://trac.ffmpeg.org/wiki/SponsoringPrograms/GSoC/2026#ContactingFFmpeg)if you have any questions. Also do not hesitate to answer questions from other students on our IRC channel if you know the answer to something.

**Find a project.**Listed on this page are mentored and un-mentored projects. Mentored projects are well-defined and mentor(s) have already volunteered. Un-mentored projects are additional ideas you may want to consider, but you will have to contact us to find a mentor. You can also propose your own project, if you can think of one that better fits your interest and skill level. If a project description is unclear or you have any questions, please get in touch with its mentor and/or join our IRC channel at*#ffmpeg-devel*.

**Contact us.**If you decide on a project, get in touch with the community and let us know. If you want to work on a qualification task, let the respective mentor know so we can avoid duplicated efforts.

**Apply.**Students should apply definitely before deadline on March 31st. The "work" period begins on Mai 25th and ends in November. Take a look at[GSoC timeline](https://developers.google.com/open-source/gsoc/timeline)for additional information. Note, make sure you apply to Google before March 31st, even if you have not yet finished your qualification task. Please apply as soon as possible: Applications can be improved until the 31st of March but not afterwards!

**Note**: A friendly reminder that while the application to GSoC is important for you and GSoC, FFmpeg mentors will not base their decision solely on the GSoC application. We will judge applicants based on their qualification tasks to understand their abilities in coding, learning the tools, communication skills etc. So please do not worry about your application being perfect for us. Although it is very important to follow GSoC's application rules so they can pay you.

## Qualification Tasks[ ¶](https://trac.ffmpeg.org#QualificationTasks)

In order to get accepted you have to complete a small qualification task which in all cases include sending a patch to the development mailing list. FFmpeg development can be quite challenging and the qualification task helps us figure out whether you are motivated enough and have the potential to deliver successfully.

The qualification tasks are usually shown in the project description. Contact the respective mentor(s) for assistance on getting a related qualification task or if you want to propose your own. You can also browse the [FFmpeg Bug Tracker](https://trac.ffmpeg.org) for qualification task ideas. In general qualification tasks should include submitting a patch to the [ffmpeg-devel mailing list](http://ffmpeg.org/mailman/listinfo/ffmpeg-devel) which passes review and is accepted into the FFmpeg codebase. It will be common for such patches to need multiple iterations of submissions and reviews, so don't wait too long with the first submission! Note, please avoid picking a qualification task which another student is already working on, each student should work on a different qualification task.

## Development[ ¶](https://trac.ffmpeg.org#Development)

If you are selected for a particular project then you are not only expected to present a working implementation but you should also submit your work for inclusion for the ffmpeg codebase. This should be done at least 2-3 weeks before the end of the second work period by sending patches to the ffmpeg-devel mailing list where the ffmpeg community and your mentor will review your work. You will likely be asked to make some changes and resend improved versions. If you feel that no consensus is reached about how something should be done then follow the advice of your mentor.

In order to create good quality patches make sure to read the [Developer Documentation](http://ffmpeg.org/developer.html).

## Contacting FFmpeg[ ¶](https://trac.ffmpeg.org#ContactingFFmpeg)

If you have questions or comments feel free to contact us via our mailing list, IRC channel, or e-mail one of the FFmpeg GSoC admins:

**Mailing-list:**[ffmpeg-devel](http://ffmpeg.org/mailman/listinfo/ffmpeg-devel)**IRC:***#ffmpeg-devel*on[Libera.Chat](https://ffmpeg.org/contact.html#IRCChannels)**FFmpeg GSoC Admins:**Michael Niedermayer (*michaelni*in #ffmpeg-devel on Libera.Chat IRC,[michaelni@gmx.at](mailto:michaelni@gmx.at)), Reynaldo Verdejo (*reynaldo*in #ffmpeg-devel on Libera.Chat IRC, R Verdejo on g mail), Thilo Borgmann (*thilo*in #ffmpeg-devel on Libera.Chat, thilo.borgmann at mail dot de)

You may also contact a mentor directly if you have questions specifically related to one of the projects listed on this page.

# Mentored Project Ideas[ ¶](https://trac.ffmpeg.org#MentoredProjectIdeas)

This section lists well-defined projects that have one or more available mentors. If you are new to FFmpeg, and have relatively little experience with multimedia, you should favor one of these ideas rather than propose your own. Contact the respective mentor(s) to get more information about the project and the requested qualification task.

## WebRTC-HTTP Egress Protocol (WHEP)[ ¶](https://trac.ffmpeg.org#WebRTC-HTTPEgressProtocolWHEP)

**Description:** FFmpeg already support WHIP, this task requires WHEP implementment as specified in
[https://www.ietf.org/archive/id/draft-ietf-wish-whep-03.html#name-protocol-extensions](https://www.ietf.org/archive/id/draft-ietf-wish-whep-03.html#name-protocol-extensions),
to enable FFmpeg to receive and play WebRTC streams. The WHEP implementation should reuse the existing codebase of WHIP (such as SDP, ICE, DTLS, SRTP) as possible, keeping the overall changes minimal and maintainable.

**Expected results:** This will allow FFmpeg users to quickly receive and play the WebRTC streams.

**Prerequisites:** Good C code, basic familiarity with Git, and basic knowledge of network transport protocols.

**Difficulty:** Medium

**Qualification Task:** Fix a random bug in FFmpeg.

**Mentor:** Jack Lau (jacklau1222gm at gmail dot com)

**Backup Mentor:** Steven Liu (lingjiujianke at gmail dot com)

**Duration:** 175 hours

## EIA-608 Closed Captions Modernization[ ¶](https://trac.ffmpeg.org#EIA-608ClosedCaptionsModernization)

**Description:** EIA-608 (Closed Captions) is a standard for subtitles common in North America. FFmpeg supports a variety of Closed Captions features built over time (decoding, extraction, etc.) and individually they work decently, but there is inconsistency between these features and usability has not been a premier goal, making the common operations unfriendly to do. With some investments via refactoring, testing, and select bug fixes, Closed Captions support can be modernized and improved.

**Expected results:** Code for EIA-608 CC is consolidated in FFmpeg code base with tests, likely migrating portions to using CBS (Coded Bitstream) API.

**Prerequisites:** Good C code, basic familiarity with Git, and willingness to learn about digital video fundamentals.

**Difficulty:** Medium

**Qualification Task:** Fix a random bug in FFmpeg.

**Mentor:** Yalda

**Backup Mentor:** Devin Heitmueller

**Duration:** 200 hours

## Modernizing LibTorch Backend: Async Infrastructure, Batching, and GPU Pipelines[ ¶](https://trac.ffmpeg.org#ModernizingLibTorchBackend:AsyncInfrastructureBatchingandGPUPipelines)

**Description:** While FFmpeg's DNN module supports AI-based video processing, the current LibTorch backend is limited by synchronous execution and single-frame processing. This project aims to transition the `dnn_backend_torch`

into a high-performance, production-grade inference engine. Key technical goals include migrating the backend to the unified `DNNAsyncExecModule`

for non-blocking execution, implementing a high-throughput batch-mode engine using `at::cat()`

and `at::split()`

, and establishing a zero-copy GPU pipeline for `AV_PIX_FMT_CUDA`

frames via `at::from_blob()`

.

**Expected results:** A modernized LibTorch backend capable of handling real-time, high-resolution AI filtering with significantly reduced CPU-GPU latency and maximized hardware throughput. The project will also include a comprehensive FATE test suite and a "Lazy Reallocator" for stable dynamic stream handling.

**Prerequisites:** Strong C/C++ systems programming, experience with the LibTorch (PyTorch C++ frontend) API, familiarity with CUDA, and understanding of FFmpeg's `libavfilter`

framework.

**Difficulty:** Hard / Advanced

**Qualification Task:** Diagnose and fix the `AVOption`

registration mismatch in `vf_dnn_processing.c`

and align LibTorch infrastructure with the async module.

**Status:****Completed and Merged****Reference PR:**[Pull Request #21408](https://code.ffmpeg.org/FFmpeg/FFmpeg/pulls/21408)**Contribution History:**[Official FFmpeg Git Author Logs](https://git.ffmpeg.org/gitweb/ffmpeg.git/search/HEAD?s=Raja+Rathour;st=author)

**Mentor:** Guo Yejun (yejun.guo at intel dot com)

**Backup Mentor:** Steven Liu (lingjiujianke at gmail dot com)

**Duration:** 350 hours (Large Project)

## Improving Fate (self tests) coverage[ ¶](https://trac.ffmpeg.org#ImprovingFateselftestscoverage)

**Description:** While every pull request is tested against our full FATE suite on multiple platforms. The FATE test code coverage is only 68% of functions and 50% of branches. Improving this coverage would result in earlier detection of bugs and thus fewer bugs. Current coverage: [https://coverage.ffmpeg.org/](https://coverage.ffmpeg.org/)

**Expected results:** A significant increase in overall code coverage of our fate tests

**Prerequisites:** C programming language, shell and advanced Makefile skills as our self tests extensively use Makefiles.

**Difficulty:** Medium

**Qualification Task:** Pick 3 files which have less than 50% coverage, each from a different library and bring them to at least 90% coverage

**Mentor:** Michael Niedermayer (*michaelni* in #ffmpeg-devel on Libera.Chat IRC, [michaelni@gmx.at](mailto:michaelni@gmx.at))

**Backup Mentor:** Sean McGovern (*Sean_McG* in #ffmpeg-devel on Libera.Chat)

**Duration:** 350 hours (Large Project), but this is flexible

## Template Project[ ¶](https://trac.ffmpeg.org#TemplateProject)

**Description:** Template Description

**Expected results:** Template results

**Prerequisites:** Template prequisites

**Difficulty:**

**Qualification Task:** Template Qualification Task

**Mentor:** someone @ somehwere.net

**Backup Mentor:** someoneelse @ somewhere.net

**Duration:** 175 or 350 hours

# Unmentored Projects[ ¶](https://trac.ffmpeg.org#UnmentoredProjects)

This is a list of projects that students are encouraged to consider if a mentored project is unavailable or not within the students skill or interests. The student will have to find a mentor for the project. A student can also [propose their own project](https://trac.ffmpeg.org/wiki/SponsoringPrograms/GSoC/2026#YourOwnProjectIdea).

## Template Project[ ¶](https://trac.ffmpeg.org#TemplateProject1)

**Description:** Template Description

**Expected results:** Template results

**Prerequisites:** Template prequisites

**Difficulty:**

**Qualification Task:** Template Qualification Task

**Mentor:** someone @ somehwere.net

**Backup Mentor:** someoneelse @ somewhere.net

**Duration:** 175 or 350 hours

## Unmentored Qualification Tasks[ ¶](https://trac.ffmpeg.org#UnmentoredQualificationTasks)

### Motion Pixels Movie CD codec 2 aka MVI2 decoder[ ¶](https://trac.ffmpeg.org#MotionPixelsMovieCDcodec2akaMVI2decoder)

Reverse engineer and write a decoder for the motion pixels MVI2 codec, used on 1995 era "MovieCD" encoded discs.

more info and samples, windows binary codecs :

[https://wiki.multimedia.cx/index.php/Motion_Pixels](https://wiki.multimedia.cx/index.php/Motion_Pixels)

### Vivo Software h263 aka VIV2 decoder[ ¶](https://trac.ffmpeg.org#VivoSoftwareh263akaVIV2decoder)

Reverse engineer and write a decoder for the viv2 codec, a staple of streaming media in the early 90s before realmedia, quicktime and microsoft took over with rm, mov and asf.

more info, samples and windows binary codecs:

[https://wiki.multimedia.cx/index.php/Vivo](https://wiki.multimedia.cx/index.php/Vivo)

more information on reverse engineering with ghidra can be found at

# Your Own Project Idea[ ¶](https://trac.ffmpeg.org#YourOwnProjectIdea)

A student can also propose a self-defined project! The amount of work defined by such a project should last for the majority of the GSoC work period duration and the task must be approved by the community. Also, a capable mentor from the community must be assigned. Ideas and inspiration for such project ideas could be found by browsing bugs and feature requests on our bug tracker but are of course not limited to such.

Students can discuss an idea with the community via the [ffmpeg-devel](https://ffmpeg.org/mailman/listinfo/ffmpeg-devel/) mailing-list, the #ffmpeg-devel IRC channel, or contact the FFmpeg GSoC admins directly for more information. It is obviously of importance to start such a discussion well before the application deadline.

[Last modified](https://trac.ffmpeg.org/wiki/SponsoringPrograms/GSoC/2026?action=diff&version=12)

[11 days ago](https://trac.ffmpeg.org/timeline?from=2026-02-12T01%3A05%3A11Z&precision=second)Last modified on Feb 12, 2026, 1:05:11 AM

**Note:**See

[TracWiki](https://trac.ffmpeg.org/wiki/TracWiki)for help on using the wiki.
