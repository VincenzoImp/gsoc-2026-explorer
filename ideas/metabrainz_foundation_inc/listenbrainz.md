# Ideas page

**Parent:** MetaBrainz Foundation Inc — Project Ideas
**Source:** https://wiki.musicbrainz.org/Development/Summer_of_Code/2026/ListenBrainz
**Scraped:** 2026-02-22T23:28:47.630257

---

# Development/Summer of Code/2026/ListenBrainz

ListenBrainz allows users to store a list of songs that they have listened to, get personalised recommendations, and more. [Try it out.](https://listenbrainz.org/)

## Getting started

(see also: [Getting started with GSoC](https://wiki.musicbrainz.org/Development/Summer_of_Code/Getting_started))

If you want to work on ListenBrainz you should show that you are able to set up the server software and understand how some of the infrastructure works. Here are some things that we might ask you about

- Show that you understand the goals that ListenBrainz wants to achieve, which are written on its homepage
- Create an oauth application on the MusicBrainz website and add the configuration information to your ListenBrainz server. Use this to log in to your server with your MusicBrainz details
- Use the import script that is part of the ListenBrainz server to load scrobbles from last.fm to your ListenBrainz server, or the main ListenBrainz server
- Use your preferred programming language to write a submission tool that can send Listen data to your local ListenBrainz server. You could make up some fake data for song names and artists. This data doesn't have to be real.
- Try and delete the ListenBrainz database on your local server to remove the fake data that you added.
- Look at the list of tickets that we have open for ListenBrainz and see if you understand what tasks the tickets involve
- We strongly urge you to look through our ticket tracker and find some easy tickets, pick one and implement it and then send us a PR -- that way we can see how you work. Ask in IRC for clarification if you don't understand what the ticket means. Check out our
[easy first bugs tickets](https://tickets.metabrainz.org/issues/?filter=12410)

## Ideas

We're adding a number of new social features to ListenBrainz that we hope will enable people discover more music they like and users who have similar music tastes to their own. We're working on some of these features now, but we will need to get help for other features:

### Showcase MusicBrainz events in ListenBrainz

**Proposed mentors:** Ansh, Monkey

**Languages/skills:** Python, React, PostgreSQL

**Estimated Project Length:** 90/175/350 hours

**Difficulty:** Medium

**Expected outcomes:** Users are notified and can explore upcoming events for their favorite artists

**Short Description:** Add MusicBrainz events to ListenBrainz

**Full Description:**

MusicBrainz has a concept of [events](https://musicbrainz.org/series/97bbae22-34ad-44c1-99ba-bce104c73dd1) to represent concerts, festivals, competitions, etc.

We want to show this information on ListenBrainz in a few places:

- artist pages should list upcoming events (perhaps past events too) the artist appears in
- a new dedicated events page both tailored to the user and global, similarly to how the
[Fresh Releases](https://listenbrainz.org/explore/fresh-releases/)page functions - the user feed should show notifications for upcoming events for that user's top artists
- or — add a way to manually "follow" an artist and get notified of upcoming events

Associated tickets: [LB-1351](https://tickets.metabrainz.org/browse/LB-1351), [LB-757](https://tickets.metabrainz.org/browse/LB-757)

### Playlists sorting and organization

**Proposed mentors:** Ansh, Monkey

**Languages/skills:** React, Python

**Estimated Project Length:** 175 hours

**Difficulty:** Easy

**Expected outcomes:** Playlists can be organized and searched, tracks in a playlist can be sorted, and MusicBrainz collections are accessible on ListenBrainz

**Short Description:** Improve playlist management and organization

**Full Description:**

This project idea is multiple small projects in a trenchcoat, all related to how users interact with playlists.

1. **Search playlists**

Currently users cannot search in their own playlists, despite an endpoint being available for that.

There is a global playlist search option in [https://listenbrainz.org/search/](https://listenbrainz.org/search/) under a tab

2. **Playlist organizing** [LB-1302](https://tickets.metabrainz.org/browse/LB-1302)

Users have very few ways to sort and organize their [playlists](https://listenbrainz.org/my/playlists).

Some users rely heavily on playlists for their music listening, and a paginated list in not sufficient.

We would want a way to organize them at will, with tags or in some type of folder structure.

3. **Playlist ordering** [LB-1374](https://tickets.metabrainz.org/browse/LB-1374)

Within a playlist itself, a user can only play the tracks in order or reorder them manually.

We would want users to be able to reorder the tracks according to:

- date added
- original manual ordering
- track title
- artist name
- randomize?

4. **MusicBrainz collections as playlists** [LB-1231](https://tickets.metabrainz.org/browse/LB-1231), [LB-961](https://tickets.metabrainz.org/browse/LB-961)

MusicBrainz users have spent years organizing and curating their music thanks to [collections](https://musicbrainz.org/user/mr_monkey/collections).

We should make it easy for users to access those directly from ListenBrainz so that, for example, they can listen to them.

This could be behind a separate tab, and would not offer the same functionality as LB playlists (users shouldn't be able to reorganize tracks for example, but can [add/remove items](https://musicbrainz.org/doc/MusicBrainz_API#collections)).

This will be easier to implement for recording collections, but we could possibly implement release/release group collections by fetching all recordings for each album.

### User onboarding

**Proposed mentors:** Ansh, Monkey

**Languages/skills:** React

**Estimated Project Length:** 90 hours

**Difficulty:** Easy

**Expected outcomes:** New users are taken through a tour of features and how to send their listens to ListenBrainz

**Short Description:** Add getting started wizards for new users

**Full Description:**

This project requires a lot of design work. If you are not familiar or comfortable with design, please choose another project.

ListenBrainz has a lot of cool features, but they are not always easy to discover for new users. We would like to add an onboarding "wizard" style step by step introduction for new users, taking them on a tour of the website and its features. This would require you to first use the website and discover the features yourself. You would investigate existing libraries for wizards/steppers that would allow programmatic navigation through the website.

It should also make it clear to users when they can expect new content such as statistics, recommendation playlists, etc.

We also need an entry page for a new user to get their listens into ListenBrainz, where they can learn about all the different importing options and other such tools. There are many ways to interact with LB, including importing streaming history from music services (Spotify, Last.FM, Youtube Music, etc.) and many ways to send new listens depending on the platfom and music player.

Associated tickets: [LB-1644](https://tickets.metabrainz.org/browse/LB-1644), [LB-1645](https://tickets.metabrainz.org/browse/LB-1645)

## Integrate Remote Playback and Listening now

**Proposed mentors:** *jasje*

**Languages/skills**: Kotlin, Compose, Koltin Multiplatform, Android, MVVM, Figma

**Estimated Project Length:** 175 hours

**Difficulty:** Hard

**Expected outcomes:** Seamless integration of Listening now and remote playback.

**Short Description:** Integrate ListenBrainz's Listening now with Remote playback via External Audio Players into currently existing UI/UX.

**Full Description:**

ListenBrainz Mobile (currently only on Android) currently uses a [Material Scaffold](https://developer.android.com/develop/ui/compose/components/scaffold) to show mini-player view of BrainzPlayer's current state. ListenBrainz offers an REST API and Socket API which (combined) reports the current song that is being listened by the user at a given moment across their devices. Currently *Listening now* is missing from the project despite it being present in earlier iterations (API endpoint integration exists) and it is intended to add the feature back in a better way.

Remote playback is playback that is handled via external players (Spotify and Youtube in our case) and metadata provided by server is used to determine how we should play a track. This playback mechanism is already implemented, however, we would like to support continuous playback via user playlists on ListenBrainz that stay active while playback is intended in background.

BrainzPlayer is our pre-existing music player with its UI integration into Material Scaffold's front layer, an Ideal place for showing currently playing song.

We visualize a system where:

- If the user is not using BrainzPlayer, we would like to show
*Listening Now*to the user and not deal with BrainzPlayer at all. - If the user is using BrainzPlayer however, we would like to override the
*Listening Now*provided by server to show state of BrainzPlayer. - If Listening Now is active, there are two cases where that listening now could come from: 1. Some other device: Just show listening now and do not show any playlists below since we are not actually playing the songs. 2. Our Android device: We would like to show playlists that are auto played by Remote Playback integrations, i.e., via Spotify or Youtube in app. How will we detect whether its our device or some other device? Listen Submission Service.
- If BrainzPlayer is active, existing view should suffice.

Objectives of the this project:

- Create and integrate the system mentioned above in a new Kotlin Multiplatform module such that the project is compatible with both Android and iOS.
- Revamp front layer of the Scaffold.
- Implement automatic playback through remote playback integrations (Spotify SDK and Youtube music API) and show the queue in front layer of scaffold.

Accomplishing the above objectives with tests would be the ultimate goal of this project.

## Compose Multiplatform Migration

**Proposed mentors:** *jasje*

**Languages/skills**: Kotlin, Compose, Koltin Multiplatform, Android, MVVM, Figma

**Estimated Project Length:** 300 hours

**Difficulty:** Hard

**Expected outcomes:** A Compose Multiplatform project which runs on both Android and iOS.

**Short Description:** Plan and execute migration to support for Android and iOS for ListenBrainz Android achieved via Compose Multiplatform.

**Full Description:**

Currently, ListenBrainz only exists in two interfaces: Website and Android. An iOS version of ListenBrainz was conceived which was fully written in Swift + SwiftUI and launched on TestFlight to handful users in an open beta/development phase. While that project was initiated, we felt that we took on too much to achieve what has already been achieved in Android version of the app. We always aim to reduce duplicate effort but also try to provide the best experience to the user. Having these two projects means double effort to achieve the same thing, different coding style and sanity to maintain and so on. Compose Multiplatform looks very promising in our vision to serve one codebase for two platforms due to the fact that an existing Android codebase can be easily converted to multi-platform app.

Efforts to achieve this have been ongoing for a few months as of writing this idea, but complete end-to-end multi-platform project migration requires several months of effort (depending on contribution size)

We visualize an app where:

- All platform native components are multi-platform compatible (expect-actual).
- All platform libraries are replaced by multi-platform alternatives.
- Have major parts of the app's UI converted to Compose Multiplatform.
- Have a running iOS app.
- Have minimal regressions (we don't expect you to be perfect)

Accomplishing the above objectives with tests would be the ultimate goal of this project.

### Title

**Proposed mentors:**

**Languages/skills:**

**Estimated Project Length:** 90/175/350 hours

**Difficulty:** Easy/Medium/Hard

**Expected outcomes:** Description

**Short Description:** Description

**Full Description:**

Your Description here
