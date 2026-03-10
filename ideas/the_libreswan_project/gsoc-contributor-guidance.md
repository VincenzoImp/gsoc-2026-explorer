# Contributor Guidance

**Parent:** The Libreswan Project — Project Ideas
**Source:** https://github.com/libreswan/libreswan/wiki/GSoC-Contributor-Guidance
**Scraped:** 2026-03-10T16:58:40.303121

---

Submissions must comply to all GSoC [rules](https://summerofcode.withgoogle.com/rules).

You will likely find the document [What is Google Summer of Code?](https://google.github.io/gsocguides/student/),
that is part of the [GSoC Guides](https://developers.google.com/open-source/gsoc/resources/guide),
far more digestible.  It even includes a section on
[Writing A Proposal](https://google.github.io/gsocguides/student/writing-a-proposal).

We strongly urge you to read up on the [previous student
projects](https://github.com/libreswan/libreswan/wiki/Completed-Projects).

But first lets get that gnarly question out the way ...

## A.I. Policy

It's [recommended](https://docs.google.com/document/d/1jglptdn_DovOxjwuhzORn3QhYoeBcToS7ymk3IIWHKY/edit?tab=t.0#heading=h.ib59d98mnz6q) that we have an A.I. Policy.  So this it is.

Don't be lazy, the result won't impress:

- don't use AI to generate your proposal
  <br>For written English, we strongly prefer your local English dialect and its idioms over AI generated text (we are ok with tools like spell checkers; be sure to set them to your local dialect).
- don't use AI to estimate your proposal
  <br>You can use AI to help understand the code and find issues; but use human analysis to confirm its correct.
- don't use AI to write code
  <br>You won’t learn anything, and if you can’t tell if AI did it right, you shouldn’t show it to anyone else either.

## First Step

- send a brief e-mail to **gsoc at libreswan.org**
  <br>(the archives are not public)

  Please include:

  + a very brief introduction
  + the project(s) that caught your eye
    <br>Include questions if you have them.
    <br>If you don't yet have a specific project in mind, just questions, ask them instead.
  + your GitHub handle
    <br>If you don't have a GitHub account, please create one.
    <br>If using GitHub isn't possible please let us know.

  If you have additional questions, definitely include those.

  This is important.  It helps us know that we're interacting with
  a GSoC candidate, and not another
  [Jia Tan collective](https://en.wikipedia.org/wiki/XZ_Utils_backdoor).

  Please resist the temptation to contact individual developers
  directly or via social media.

  We can also be contacted by sending e-mail to the [developer mailing
  list](https://lists.libreswan.org/mailman3/lists/swan-dev.lists.libreswan.org/)
  or on [IRC](https://github.com/libreswan/libreswan/wiki/IRC).

## Next steps

- Subscribe to the [developer mailing
  list](https://lists.libreswan.org/mailman3/lists/swan-dev.lists.libreswan.org/)

  Don't worry, it is low volume.

  If there's a notable change to the code base, a heads up will be
  sent here.

  It can also be used as an alternative channel for questions.

- get Libreswan working on **your** machine

  Most Linux distros and FreeBSD provide a prebuilt Libreswan package.
  <br>On NetBSD use `pkgsrc/wip/libreswan-5`; or build from source.
  <br>On OpenBSD you'll need to build from source.

  If you don't have VPN/IPsec experience, we are happy to give you a
  client configuration to gain experience using Libreswan to a real
  VPN server.

  _Note: Libreswan does not work on Windows; neither native, nor using
  the Windows Subsystem for Linux.  We suggest you use a VM running
  Fedora._

- look through the [IKEv2
  RFC](https://datatracker.ietf.org/doc/html/rfc7296)

  To make the reading less dry, you could try aligning Libreswan's
  console log messages with the RFC.  For instance, in
  [ikev2-04-basic-x509](https://testing.libreswan.org/v5.3-1946-gf60e40255a/ikev2-04-basic-x509/)
  look at the lines that follow `initiating IKEv2 connection to
  192.1.2.23 using UDP`.

- look through the [source
  code](https://github.com/libreswan/libreswan)

  (if you haven't already) Create a local copy and build Libreswan.

  One way to get familiar with the source code is, using the
  log messages from Libreswan establishing a connection as a pointer,
  trace how Libreswan works.  To get specific, work out from the function
  `initiate_v2_IKE_SA_INIT_request()`.

  The wiki also contains notes (some getting old) about Libreswan internals

- see if you can run a single test

  The testsuite is found in `testing/pluto/` in the source tree;
  and the [Testing](https://github.com/libreswan/libreswan/wiki/Testing) page suggests several ways to get
  the testsuite running.

  _Note: We're not suggesting that, at this stage, you run the
  full testsuite. We have dedicated hardware for that._ 

  This may also prove to be a good point to come forward with any questions.

- look through Libreswan's [bug database](https://github.com/libreswan/libreswan/issues)

  If a task or bug looks interesting and you'd like to work on it (i.e.,
  submit a [Pull Request](https://github.com/libreswan/libreswan/wiki/Hacking:-Git,-GitHub,-and-Pull-Requests)),
  either drop an e-mail to gsoc@ or add a note to the bug asking about it.

  Just remember that tasks are often heavy on assumed
  context (if prompted we can provide details); and seemingly trivial
  tasks (such as output tweaks) can require a deceptive amount of work
  (such as test-suite updates).

  Once you've got one bug under your hat, you could consider a second.
  <br>But please **do not _claim_ or _hog_ bugs**.

- see if you can set things up so you're on [IRC](https://github.com/libreswan/libreswan/wiki/IRC)

- review the Preferred Skills

  The Preferred Skills list is a good starting point for further
  reading.

- prepare your (proposal)[https://google.github.io/gsocguides/student/writing-a-proposal]

  Please address the required an preferred skills.

  Please include a weekly schedule with clear milestones and
  deliverables.

Submissions that tend to be accepted and successful are those that
show from the start that the student is putting in the time to
understand the concepts (you don't have to be an expert already).
Mentors like to see students that have put in some work to understand
and try things.  It is the only reliable metric we have for new people
to indicate how serious they are to take on a project for the summer.
If implementing an RFC, read the RFC and ask us any questions you
have.


## Glossary

#### What do we mean by Difficulty?

##### Easy (90 hours)

There's a narrow skill set, and the project is relatively self
contained.

For instance, a project modifying the build system, has no expectation
that you come up-to-speed with the internals of Libreswan.

Except for Proof-Of-Concepts, we don't anticipate problems when
merging the completed project into mainline.

##### Medium (175 hours)

The project is technical.

We assume time will be spent coming up to speed both with Libreswan's
code and, where needed, concepts from Recommended Skills list.  For
the most part, the work should be able to leverage existing code (and
not involve major internal changes).  Since the mentors have a good
grasp of the work involved, they can provide plenty of guidance.

Except for Proof-Of-Concepts, we don't anticipate significant problems
when merging the completed project into mainline.

##### Hard (350 hours)

The project is technically challenging.

The work will involve research, design, and significant changes to
Libreswan (and potentially, other libraries).  While the mentors have
a broad understanding of the technical area, they are looking for you
to flesh out the details, come up with working and tested code, and
provide recommended next steps.

Since a successful project may identify additional changes to
Libreswan (pluto), merging may not be straight forward.

For instance, before merging the [Session
Resumption](https://github.com/libreswan/libreswan/wiki/Completed-Projects:-Session-Resumption) project we
changed the way Libreswan (pluto) implements an exchange, and before
merging [Extend RFC-7427 Signature Authentication support to IKEv2
with
EDDSA](https://github.com/libreswan/libreswan/wiki/Completed-Projects:-Extend-RFC-7427-Signature-Authentication-support-to-IKEv2-with-EDDSA)
we changed the way Signature Message Authentication Code (MAC) is
computed.


#### What do we mean by Skills?

Each project lists both required and recommended skills.  If you're
wondering what we mean, see below.

##### Required Skills

###### C

In addition to writing new code, we're looking for experience
understanding and modifying existing code.

###### UNIX programming

We're looking for experience with developing software on, and targeted
at, UNIX like systems (Linux, *BSD); some of the tools we use are
Make, /bin/sh, the C library, text editors, git, pthreads, libevent,
libnss (mozilla), so any familiarity in these areas is useful.

##### Recommended Skills

We're looking for some familarity.  More importantly we're looking for
a willingness to learn.

###### Network protocols

The IKE protocol is built on IP; we're looking for familiarity with
networking concepts in general, and specific protocols such as UDP
(often covered by a Networking course)

###### Cryptographic fundamentals

The IKE protocol relies on cryptography; we're looking for familiarity
with basic concepts such as Integrity, Security, and Authentication
(if you've completed an _Introduction to Cryptography_ course then
you're more than qualified).  Libreswan uses the NSS library from
Mozilla.

###### RFC interpretation

RFCs (Request For Comment) documents are both low-level and
technically detailed; we're looking for experience understanding and
implementing code using technical specification as the reference.

###### BSD networking
###### Linux networking

Familiarity with using command line networking tools, for instance to
configure network interfaces and manage routes.

###### PFKEY_V2

This is the kernel interface that Libreswan uses on BSD; FreeBSD,
NetBSD, and OpenBSD all have their differences which is why we suggest
focusing on one of the BSDs initially

###### XFRM

This is the kernel interface that Libreswan uses on Linux.


Finally, good luck, and happy coding.
