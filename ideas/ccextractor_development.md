# CCExtractor Development — Project Ideas

**Source:** https://ccextractor.org/docs/ideas_page_for_summer_of_code_2026/
**Scraped:** 2026-02-22T23:28:47.611731

---

# Google Summer of Code (GSoC) 2026 ideas page

**Important:**Please read our

[AI Policy](/ideas/ccextractor-development/public-gsoc-ai_policy)before submitting any PRs.

For classic, niche project ideas, check out the [Classic Projects page](/ideas/ccextractor-development/classic_ideas).

**NEW: Office Hours**

Starting **February 8, 2026**, we will be holding **weekly office hours every Sunday** (depending on your timezone).
This is an open session where you can drop in, ask your questions, and have a conversation with an
**org admin and/or mentor**—maybe more. There's no need to be formal, and if you're shy, you don't even have to turn
your camera on.

To join, simply use this ** Google Meet link**. The sessions will begin at

**10:30 AM San Francisco Time**, which serves as the official reference time.


There is **no fixed agenda** for these meetings. Whether you want to ask about **GSoC, the organization, your project,
or anything else**, you're welcome to join. If others are discussing something, you can also stay and listen. We will
be available for **at least 30 minutes**, but if a conversation is ongoing at **9:00 AM San Francisco Time**, we'll
**continue as long as needed**.

Feel free to drop by, ask questions, or just hang out. We look forward to seeing you there!

Welcome to our ideas page. It's great you want to start early. Please join us in our Zulip space! (we'll leave this as an exercise for you to find --- it's on our website).

As you will see, this year has a lot of Rust. The reason is simple: Security. Our C code base has known (and we suspect, a lot of unknown) security issues caused by the usual memory management in C. Lots of people have touched the code over the years, and it shows.

There's also Flutter, which we love, and more.

We will provide resources for students --- we'll give access to a high-speed server, all our samples (we'll even ship a portable drive with them anywhere in the world, so don't worry about slow connections) and various other perks.

You are welcome to check out the page (actual ideas at the bottom of the page, with each project having it's own separate page as well) and start early in the community bonding process as well as learning a bit about our code ethics and practices. And of course, we'd love you to stay around even if we are not invited to GSoC or if we cannot invite you as a student.

#### The ideas we currently have

Important: If you have something else in mind that relates to subtitles and accessibility please get in touch. We prefer that you do something that you are passionate about even if it's something we hadn't considered.

After you check out our ideas please continue reading to the bottom of the page to get information about who we are, how we collaborate, what resources we will provide to you, etc.

#### Niche ideas

We've moved the less mainstream ideas to their [own page](/ideas/ccextractor-development/classic_ideas)
These ideas are not less important, but because they require more specialized skills (or mindsets) we've decided to
give them a place of their own :-) Please take a look after you are done with this page; maybe something there will
pick your interest.

#### CCExtractor Core

Since we are now feature complete, and the subtitles work have changed a lot (We won! Almost everything is subtitled now!) it's time to settle down, prepare a perfect, stable, battery included release so we can rest on our laurels for a bit after a fantastic run on our core tool.

| Name | Description | Tech you need to know | Tech you will learn | Difficulty | Size |
|---|---|---|---|---|---|
|

[Sample Platform NG](/ideas/ccextractor-development/public-gsoc-2026-sample_platform_ng)#### Flutter

| Name | Description | Tech you need to know | Tech you will learn | Difficulty | Size |
|---|---|---|---|---|---|
|

[support more torrent clients](/ideas/ccextractor-development/public-gsoc-flutter-more-clients)[Flood](https://flood.js.org)and[Deluge](https://deluge-torrent.org).[TaskWarrior](/ideas/ccextractor-development/public-gsoc-2026-taskwarrior)#### Systems

| Name | Description | Tech you need to know | Tech you will learn | Difficulty | Size |
|---|---|---|---|---|---|
|

[Add complex layouts to sway](/ideas/ccextractor-development/public-gsoc-2026-sway_complex)[Task Server III](/ideas/ccextractor-development/public-gsoc-2026-taskserver)#### New things we're currently interested on

| Name | Description | Tech you need to know | Tech you will learn | Difficulty | Size |
|---|---|---|---|---|---|
|

`.desktop`

files are used by app launcher to provide access to additional functionalities, typically via context menus. Ilia is an app launcher that currently doesn't support for Desktop Actions due to its keyboard based approach.#### About us

We are a small org, which means that your contribution will have a large impact. It's not going to mean a 0.5% improvement on a big project --- it's going to be more than 10% on a medium size one. If you like challenges and want a chance to shine this is your place.

We have *we think* statistically amazing continuity in the team: Most
GSoC students from all the past years are still involved, even if they
are no longer eligible as students. They still contribute code, and they
mentor both in GSoC and the sister program GCI. As mentors, they also
come to the Summer of Code summit which traditionally takes place in
October.

We have *mentors all over the world* (North America, Europe, Asia and
Australia), so time zones are never a problem. Our main channel of
communication is a [Zulip instance](/ideas/ccextractor-development/public-general-support) to
which everyone is welcome. We expect all accepted students to be
available on Zulip very often, even if you don't need to talk to your
mentor. This will help you ask questions when necessary, and you might
be able to help others out as well while working on your project.

Exception: If your country (such as **Russia**) has banned Zulip please get in touch in we'll work out a solution with you. We absolutely want you to participate.

**All our top committers will be mentoring**. Many of them are former GSoC students or winners of GCI.

#### Perks

All accepted students get a programming book or course immediately after being accepted, with the hope that they read them before the coding starts. We want to see if this increases the quality of the work. You can pick any programming book or course under 100$, and we will provide it.

#### About what we use

This is what we use **today**. It doesn't mean this is what we want
to continue using. Probably not --- we're really open to change. We're
just describing the status quo so you know what you are getting into :-)

The core tool that names the organization (CCExtractor) is a
command-line program written in **C** (not C++), and new core parts are being written in **Rust**.

The current GUI is written in **flutter**.

The testing tool we use to run regression tests is mainly written in
**Python**, but it also used Javascript, CSS and some shell
scripting. The Test suite is written in C#. One of the projects this
year is to move it from a dedicated server to GSoC and improving the scalability of test runs.

The prototype real time subtitle website is written in **NodeJS**.

We also have a number of support tools that do a number of different
things, from downloading subtitles from streaming services to
translating them with Google Translate or DeepL. Most of them are
written in **Python**, but since they are small tools that do their
job you don't need to worry much about them.

For totally new things you can use whatever tool you feel is best for the task at hand.

#### About sample media and other resources

We work with huge files. Not all of them are huge, but many are. We know that many students don't have access to high speed internet. To those students we will ship (as soon as they are selected) a portable hard drive with all our samples. So if your internet connection is not good, don't worry --- as long as you can plug a USB drive to your development computer you can participate with us.

We also have a shared Linux development server with lots of storage and a Gigabit uplink. Students get an account on it and they are welcome to use it. There's nothing there except our own work, so it's a trusted environment (for a server that is connected to internet of course).

The sample platform also hosts a bunch of samples, both which are small or decently sized.

Some projects have specific requirements, and we'll make sure that you get the resources you need: i.e. if your project requires some cloud resources (Google Compute Engine, for example), we'll make sure you get access to the resources.

In general, you are not expected to pay for anything (other than your own development computer and internet, of course) related to any project.

If you need anything not mentioned (such as a book) let us know. Within reason, we'll help you.

#### About the projects and getting accepted

Qualification: Our selection system is based on several factors. Of course no student ranks in all criteria, so don't worry when you read the list below.

**Work on our core tool**: Even if you are going to be working
on something totally different. This might seem counterintuitive,
but the thing is if you prove you can dig into our
(messy) code base, find yourself your way around it, and fix a
few bugs, you are just the kind of person we can trust to
"figure things out". GSoC is among other things, a learning
experience. No matter what project you decide to work on,
there's going to be roadblocks, things you don't know how to
do, etc. So we really like it when students embrace those
situations.

**Qualification tasks specific to the project**: The detail page
for some projects contains specific qualification tasks that
apply to them.

**Contributions to existing open source projects**: This can be
anything. From a good GitHub profile to pull-requests sent to
any other existing project, participation in hackathons, Google
Code-In, past GSoCs and so on.

**A good proposal**: This is the one criteria that is
non-negotiable. Your proposal has to be good, period.

**Project popularity**: Some ideas just have more competition,
so if participating in GSoC is a top priority for you (over
working on a specific project), consider applying to one of the
"niche" ideas. After all, that's a great way to get your foot
in the door :-)

**Best core tool tasks**

We're added a difficulty level to most of our [open issues on GitHub](https://github.com/CCExtractor/ccextractor/issues).
Best thing you can do is head there and see if you are able to fix some
of the easy ones and work your way up. We don't expect you to be able
to do the hard ones, but we'd be impressed if you did :-)

For some of the easy ones you don't even need to know C. Just being able to compile CCExtractor and dig around a bit will be enough.

The sample platform's issues are tagged with "gsoc-proposal-task", so you can easily see what you can work on.

### Take home qualification tasks

If instead of working on existing code you'd prefer to show us your
skills working on something new, you can pick one of [these projects](/ideas/ccextractor-development/public-gsoc-takehome).

#### Community etiquette

It goes without saying that everyone in the community has to be polite and respectful, and consider everyone else a member of a team and not a competitor.

All developers are part of the team, by the way. Our Zulip instance has mentors, code-in participants, other students, or developers and users that are none of the above, but they all play some kind of role in CCExtractor's community.

Part of being respectful is giving consideration to everyone else's time. Most of us have day jobs, and as such are limited in the time we can use to guide you. We'd like to spend it on quality discussions, and not on things that are for example written on this website, things that you can easily retrieve by reading documentation on used libraries or on the software's help screen. Asking this kind of questions in the Zulip instance shows little respect for our time. This doesn't mean you can't ask questions, but remember that being a clueless user and a lazy developer are two very different things. If you ask those questions you will probably get an answer as if you were a clueless user (polite no matter what), but if you apply to GSoC you will be considered a lazy developer. Google is your friend ;)

Tell things as you see them. Politely -you're not Linus-, but don't sugar-coat it. We know some parts of our code is poorly written, poorly documented, etc. It stands out, so you will know when you dig in. No one is going to be offended by having that code rewritten or refactored. Peer review applies to everybody's work and is done by everybody.

#### Cross project proposals

Because we use a number of libraries and in fact "are a library" ourselves (meaning other programs can link CCExtractor as a library, or invoke the binary) we interact with other communities and their software. From time to time there's a chance to do something interesting that affects CCExtractor and something else (FFmpeg comes to mind, but also Kodi, VLC, libGPAC, Red Hen, to mention just a few of our friends that typically participate in Summer of Code). So how does this work? As long as the work benefits CCExtractor, and it's part of your summer project, we're OK with you spending some time on the other project. For example if you are improving our MP4 support, for which we use libGPAC, and need to fix or improve something on libGPAC you are welcome to do so. If you do, make sure you submit your changes to their maintainers and follow through with their merge process.

#### Your proposal

You can propose to do any of the following ideas, or you can bring your own. In any case, make sure you run them by us before you actually submit your proposal.

At the very least your proposal needs to:

- Explain what you want to do, why it is important to you (don't make up a story here — the reason can be that you need it, that you just think it's cool, that you have an itch to work on it, etc.), and why it could be important or useful to us.
- Explain how you intend to accomplish the goal, in enough detail that makes it clear that you have done your homework. For example, "I will modify the CCExtractor binary so that it's able to convert audio to text with perfect accuracy" is the same thing as sending your proposal to the trash. You need to have a plan.
- Detail the timeline explaining what the expected progress is for each week or every two weeks (pay special attention to the milestones within the GSoC timeline itself, of course) and how we should validate the results.
- Detail what kind of support you will need from us. For example, if you are going to need test streams, hardware, access to a server, etc., let us know, so we can prepare everything for you as soon as possible.
- Detail your expected working hours in UTC. We're used to weird working schedules, so don't worry about working in the middle of the night, or weekends instead of other days, etc. Knowing your hours may help us to match you better with a mentor.
- Mention your planned absences. We don't need you to detail what you will be doing when you are not working of course, but if you are going away for any reason we need to know so we don't think you've abandoned.
- Link to your GitHub (or any other repository) profile, if you have one, so we can take a look at your previous work.
- GSoC is a coding program: This means that ideas that are about testing (unless it involves coding something to test our programs ;) ), website design, etc., are out.
- However, we want to have good documentation: Make sure you have time to write a good technical article explaining your work.
- Be realistic and honest with the timeline. Consider each week you should work around 30 hours. If your timeline reserves a lot of time for minor things we'll think that you are not going to be working full-time in GSoC. On the other hand if you promise to do things in a lot less than that it seems realistic to us, it will seem that you don't really know how much work things take.
- If you are going to be using 3rd party libraries (that's OK), make sure to validate that their license is compatible with GPLv2 (which is ours). List the libraries in your proposal. Check that they are cross-platform. If you will need to extend those libraries in any way please explain. In this case, your proposal should include time to get that extension submitted to the maintainers (we love to contribute to other projects).

Something else: Mentors often have their fingers in several pies. If you send the same proposal to several orgs everyone will know. So do yourself a favor and don't do that. You can apply to several organizations and that's totally fine, but each organization will want to see that you have put the time to write a great proposal that is focused on them.
