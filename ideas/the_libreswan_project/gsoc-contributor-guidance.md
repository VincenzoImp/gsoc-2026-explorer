# Contributor
Guidance

**Parent:** The Libreswan Project — Project Ideas
**Source:** https://github.com/libreswan/libreswan/wiki/GSoC-Contributor-Guidance
**Scraped:** 2026-02-22T23:28:47.597409

---

Submissions must comply to all GSoC rules.

We strongly urge you to read up on the [previous student
projects](https://github.com/libreswan/libreswan/wiki/Completed-Projects).

Here are our suggested next steps for submitting a proposal:

- send us an e-mail at **gsoc at libreswan.org** (it's not public)

  Let us know who you are and the project that has caught your eye.

  If you have questions, please feel free to ask.

  We can also be contacted on the [developer mailing
  list](https://lists.libreswan.org/mailman/listinfo/swan-dev) or the
  **\#libreswan** channel on the **LiberaChat IRC** network.

- see if you can get Libreswan working on your machine

  Most Linux distros, and FreeBSD, provide a libreswan package.  On
  NetBSD see wip/libreswan-5.  On OpenBSD you'll need to build from
  source.

  If you don't have VPN/IPsec experience, we are happy to give you a
  client configuration to gain experience using libreswan to a real
  VPN server.

- have a look at the [code
  base](https://github.com/libreswan/libreswan) and [test
  framework](https://github.com/libreswan/libreswan/wiki/Testing).

  Create a github account, clone the project, and try building.

  You could even look through the bug database (it's on github)

- review the Preferred Skills

  The Prefered Skills list is a good starting point for further
  reading.

- prepare your submission

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


### Glossary

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
implementing code using technical specification as the reference

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
