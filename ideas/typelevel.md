# Typelevel — Project Ideas

**Source:** https://typelevel.org/gsoc/ideas.html
**Scraped:** 2026-02-22T23:28:47.582290

---

# Google Summer of Code

Our community has identified project ideas that we believe will significantly enhance the Typelevel ecosystem. Nothing is set in stone: we may be able to adjust a project’s length and difficulty to make it the right fit for you. So if you see something here that interests you or have an idea of your own, please [get in touch](https://typelevel.org/cdn-cgi/l/email-protection#6e091d010d2e1a171e0b020b180b0240011c09)!

Serverless integrations for Feral

Feral is a Typelevel library for building serverless functions that currently supports AWS Lambda and Google Cloud Run Functions. We want to add support for more types of serverless events and more cloud providers.

**Prerequisites**

Scala, ideally experience with serverless

**Expected Difficulty**

Medium.

**Expected Length**

Medium (~ 175 hours)

**Mentors**

[@armanbilge](https://github.com/armanbilge) [@bpholt](https://github.com/bpholt) [@Chingles2404](https://github.com/Chingles2404)

**Related Repositories**

[feral](https://github.com/typelevel/feral)

Native I/O backend for FS2 JVM

FS2 on the JVM currently implements its networking API using JDK NIO. Unfortunately this indirection incurs a non-trivial performance penalty. We want to replace the use of JDK NIO with direct calls to system I/O APIs such as epoll and kqueue.

**Prerequisites**

Scala, ability to read C

**Expected Difficulty**

Medium.

**Expected Length**

Long (~ 350 hours)

**Mentors**

[@antoniojimeneznieto](https://github.com/antoniojimeneznieto) [@djspiewak](https://github.com/djspiewak) [@mpilquist](https://github.com/mpilquist) [@armanbilge](https://github.com/armanbilge)

**Related Repositories**

[fs2](https://github.com/typelevel/fs2)

FS2 Connection API

TCP-based protocols are common (e.g. HTTP, Postgres, Redis) and are implemented by clients to interface with these services (e.g. Ember, Skunk, Rediculous). The goal of this project is to create a connection API that supports pooling, error conditions, and metrics and can be shared by all of our client libraries.

**Prerequisites**

Scala, ideally some knowledge of networking

**Expected Difficulty**

Hard.

**Expected Length**

Long (~ 350 hours)

**Mentors**

[@mpilquist](https://github.com/mpilquist) [@armanbilge](https://github.com/armanbilge)

**Related Repositories**

[fs2](https://github.com/typelevel/fs2)

Web Components for Calico

Calico is a reactive UI library built with Cats Effect and FS2. Web Components are a standard for creating framework-agnostic, reusable UI elements. The goal of this project is to enable Calico users to access the vast array of web components available by improving its DSL and code-generation.

**Prerequisites**

Scala, ideally experience with Web APIs

**Expected Difficulty**

Medium.

**Expected Length**

Long (~ 350 hours)

**Mentors**

[@armanbilge](https://github.com/armanbilge)

**Related Repositories**

[calico](https://github.com/armanbilge/calico)

Upgrade sbt-typelevel to sbt 2

sbt-typelevel is a plugin for sbt, the Scala build tool, used by hundreds of open source and enterprise projects. sbt 2 is in the final stages of development. We want to upgrade sbt-typelevel to sbt 2 and adopt its new features, such as project matrix for cross-building.

**Prerequisites**

Scala

**Expected Difficulty**

Medium.

**Expected Length**

Long (~ 350 hours)

**Mentors**

[@mzuehlke](https://github.com/mzuehlke) [@armanbilge](https://github.com/armanbilge)

**Related Repositories**

[sbt-typelevel](https://github.com/typelevel/sbt-typelevel)

Refresh Davenverse projects

The Davenverse is a collection of several popular Typelevel libraries, including Mules and cats-scalacheck. Unfortunately, we have fallen behind on their maintenance. We want to move these libraries under the Typelevel org, refresh their build tooling, and bring them up-to-date to ensure their longevity.

**Prerequisites**

Scala

**Expected Difficulty**

Medium.

**Expected Length**

Medium (~ 175 hours)

**Mentors**

[@armanbilge](https://github.com/armanbilge) [@valencik](https://github.com/valencik)

**Related Repositories**

[davenverse](https://github.com/davenverse)

Cats Effect & FS2 on Wasm/WASI

Web Assembly and its System Interface are emerging technologies for deploying secure, modular applications. The goal of this project is to prototype porting the Cats Effect runtime and FS2 streaming I/O to the Wasm/WASI platform, also possibly generating feedback for the Scala WASM and WASI teams.

**Prerequisites**

Scala, ideally some experience with Wasm/WASI

**Expected Difficulty**

Hard. Wasm/WASI support in Scala is experimental.

**Expected Length**

Long (~ 350 hours)

**Mentors**

[@armanbilge](https://github.com/armanbilge) [@tanishiking](https://github.com/tanishiking) [@valencik](https://github.com/valencik)

**Related Repositories**

[cats-effect](https://github.com/typelevel/cats-effect) [fs2](https://github.com/typelevel/fs2)

Laika enhancements for typelevel.org

Laika is a purely functional site and e-book generator and customizable text markup transformer. We recently migrated the Typelevel website from Jekyll to Laika. The goal of this project is improve and streamline Laika's support for generating non-documentation websites, such as blogs.

**Prerequisites**

Scala

**Expected Difficulty**

Medium.

**Expected Length**

Medium (~ 175 hours)

**Mentors**

[@armanbilge](https://github.com/armanbilge) [@valencik](https://github.com/valencik)

**Related Repositories**

[Laika](https://github.com/typelevel/Laika) [typelevel.org](https://github.com/typelevel/typelevel.github.com)

A faster immutable list datatype

Immutable linked lists are a core datatype in functional programming languages. The goal of this project is to explore implementing a list-like datatype with enhanced performance. Along the way, you will learn about algebraic datatypes, Cats typeclasses, and mechanical sympathy.

**Prerequisites**

Interest in functional programming

**Expected Difficulty**

Medium. This is a good project for beginners!

**Expected Length**

Long (~ 350 hours)

**Mentors**

[@armanbilge](https://github.com/armanbilge) [@johnynek](https://github.com/johnynek)

**Related Repositories**

[Cats Collections](https://github.com/typelevel/cats-collections)

Doodle Immediate Mode Algebra

Design and implement an API for Doodle that allows low-level bitmap based operations.

**Prerequisites**

Proficient with Scala and some understanding of computer graphics.

**Expected Difficulty**

Medium

**Expected Length**

Medium (~ 175 hours)

**Mentors**

[@noelwelsh](https://github.com/noelwelsh)

**Related Repositories**

[Doodle](https://github.com/creativescala/doodle/issues/93)

Doodle Skia Backend

Add a Skia backend to Doodle, greatly improving the performance and expressivity available on the JVM.

**Prerequisites**

Proficient with Scala and some understanding of computer graphics. This involves working with a library (Skija) that is not well documented and itself wraps a C++ library with patchy documentation. Hence a willingness to dive into foreign code bases is necessary.

**Expected Difficulty**

Medium

**Expected Length**

Medium (~ 175 hours)

**Mentors**

[@noelwelsh](https://github.com/noelwelsh)

**Related Repositories**

[Doodle](https://github.com/creativescala/doodle/issues/175)

Are you interested in working on a GSoC project with mentorship from Typelevel maintainers?

[Submit Proposal](https://typelevel.org/cdn-cgi/l/email-protection#9ff8ecf0fcdfebe6effaf3fae9faf3b1f0edf8)
