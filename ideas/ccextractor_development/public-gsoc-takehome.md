# these projects

**Parent:** CCExtractor Development — Project Ideas
**Source:** https://ccextractor.org/public/gsoc/takehome
**Scraped:** 2026-02-22T23:28:47.612664

---

# Take-home qualification tasks

We know that working on existing codebases can be daunting, and you might end up working on a new project anyway, so this year we have some alternative qualification tasks (we'll add more soon, so come back).

You can still opt for the standard ones (such as fixing issues on GitHub) --- these are just alternatives that are available.

Note: You might be wondering why we don't add links to anything here. It's just to make sure that you know how to find things yourself :-)

### sway configuration override

sway is a replacement for the popular i3 windows manager in Linux. We care a lot about it because a very successful project from GSoC '22 integrated it in Regolith linux, a ubuntu based distribution that we love.

A configuration option that sway has (and i3 as well) is to include partial configuration files from directories, like this:

File: /etc/regolith/sway/config

```
###############################################################################
# sway Config Partials
###############################################################################
# Include any regolith sway partials
include /usr/share/regolith/sway/config.d/*
# Include any user sway partials
include $HOME/.config/regolith2/sway/config.d/*
```


Note that it first imports the global configuration, then the user configuration, which often overlaps. We want to add a new directive called include_one that would work like this:

```
include_one $HOME/.config/regolith2/sway/config.d/* /usr/share/regolith/sway/config.d/*
```


Note that both directories are passed to the same include_one. It would include all the files in the first directory and then from the second directory it would only import the files that weren't import before. So if the first directory contains a file called for example, "70_bar" then such file would be skipped when processing the second directory.

### Meetup auto-RSVP

Language: Any Must work in: **Linux**

This task is relatively simple (in theory), but it will help us assess your code organization abilities.

Write a program for meetup.com that sends an auto-RSVP to specific groups. For example, suppose you are a member of 7 different Meetup groups, some of which have very popular events that fill up quickly. You want to sign up for them as fast as possible to ensure that you get a spot.

Your program needs take care of authentication, searching for events in configured groups (not all), and automatically signing up on the user's behalf in a timely manner. Usage of existing Meetup client libraries is permitted.

It's OK for your program to be a simple command-line tool that needs to be run from cron once an hour or something like that.

### Export data from MyFitnessPal to Grafana

Language: Any Must work in: Linux (anything server side)

MyFitnessPal is a mobile app used to track food & energy intake, exercise, and more. It supports CSV data export (e.g. through email) to facilitate archival, but this style is a bit antiquated for manual viewing.

A simple website that accepts CSV exports and renders nice visual representations using Grafana would be much better for users. This should be feasible to complete in a few days since all of the major components already exist.

### Compile Flutter on Mac

If you have a Mac, prepare distributables for any of our Flutter programs for Mac. If it doesn't work, fix it and send a PR. acon").

### Face Condition Detection in Any Lighting

Language: Flutter

Must work in: Android, iOS (OK if you can just test in one, but we will test in both and if it doesn't work, we'll send you the debug info so you can fix it).

Write a Flutter app that detects a person's face and analyzes its condition in real-time, even in different lighting environments.

For example: The app should identify if the person looks tired, stressed, happy, or sad. It should also detect if the lighting is too bright or too dim and adjust the face detection accordingly.

It must be fast and work in all lighting conditions!

### Rust: Help i3status-rs release 0.30

i3status-rs is a fantastic status bar for i3/sway written completely in Rust. They're in the process of migrating to async rust.

There's a few open issues on GitHub. Your job is to solve any 2 (coding, not documentation) and send a PR. There's a few with the tag "good first issue" so you can just do them.

In general they're easy - they could take a couple of hours, and you'd be helping a popular project!

### Rust: Fix our build system on GitHub

Our build system is currently failing due to a bug in the crate that we use for FFmpeg. You can get details here:

[https://github.com/zmwangx/rust-ffmpeg-sys/issues/42](https://github.com/zmwangx/rust-ffmpeg-sys/issues/42)

It's just .unwrap() being called on None, so *possibly* it's not a lot of effort to figure it out.

We like people who can troubleshoot - just because the fix won't have -hopefully- a lot of code don't think this task is not important. It is, and solving it qualifies you.

### C/C++: Update our libGPAC dependency

GPAC is the library we use to handle MP4. It's vendored (that means we just took it and added it to source tree instead of linking it as an external dependency). The -historic and maybe no longer valid- for this is that importing dependencies in Windows is a nightmare (it's called DLL hell for a reason).

Anyway, for the time being, we'd be happy to just update our vendored libGPAC for the current version.

Usually this work takes a few hours.
