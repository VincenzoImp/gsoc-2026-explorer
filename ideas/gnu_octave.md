# GNU Octave — Project Ideas

**Source:** https://wiki.octave.org/wiki/index.php?title=Summer_of_Code_-_Getting_Started#Suggested_projects
**Scraped:** 2026-02-22T23:28:47.623775

---

# Summer of Code - Getting Started

[Jump to navigation](https://wiki.octave.org#mw-head)

[Jump to search](https://wiki.octave.org#searchInput)

[mentoring organization for GSoC 2026](https://summerofcode.withgoogle.com/programs/2026/organizations/gnu-octave).

Since 2011 the GNU Octave project has successfully mentored:

in [Summer of Code](/ideas/gnu-octave/summer_of_code) (SoC) programs by [Google](https://summerofcode.withgoogle.com/) and [ESA](https://esa.int/).

Those SoC programs aim to advertise open-source software development and to attract potential new Octave developers.

# Steps toward a successful application

- 😉💬
**We want to get to know you (before the deadline). Communicate with us.**- Join
or**Octave Discourse**[IRC](/ideas/gnu-octave/irc)for general discussion and to ask questions (Please do not use the bug tracker for general GSOC inquiries unrelated to specific bugs found with Octave.) Using a nickname is fine. - Show us that you're motivated to work on Octave 💻. There is no need to present an overwhelming CV 🏆; evidence of involvement with Octave is more important.
**If you never talked to us, we will likely reject your proposal**, even it looks good 🚮

- Join
- 👩🔬
**Get your hands dirty.**- We are curious about your programming skills 🚀
- Your application will be much stronger if you
[fix Octave bugs](https://savannah.gnu.org/bugs/?group=octave)or[submit patches](https://savannah.gnu.org/patch/?group=octave)before or during the application period. - You can take a look at the
[short projects](/ideas/gnu-octave/short_projects)for some simple bugs to start with.

- Your application will be much stronger if you
**Use Octave!**- If you come across something that does not work the way you like ➡️ try to fix that 🔧
- Or if you find a missing function ➡️ try to implement it.


- We are curious about your programming skills 🚀
- 📝💡
**Tell us what you are going to do.**- Do not write just to say what project you're interested in. Be specific about what you are going to do, include links 🔗, show us you know what you are talking about 💡, and ask many
[smart questions](http://www.catb.org/esr/faqs/smart-questions.html)🤓 - Remember,
**we are volunteer developers and not your boss**🙂

- Do not write just to say what project you're interested in. Be specific about what you are going to do, include links 🔗, show us you know what you are talking about 💡, and ask many
- 📔
**Prepare your proposal with us.**- Try to show us as early as possible a draft of your proposal 📑
- If we see your proposal for the first time after the application deadline, it might easily contain some paragraphs not fully clear to us. Ongoing interaction will give us more confidence that you are capable of working on your project 🙂👍
- Here’s a sample proposal outline that you can use as a reference when drafting your own application.
[Sample Proposal](https://docs.google.com/document/d/1kGtT9_f0FrXdCKwyKEWwOV6R-AU90bkd/edit?usp=sharing&ouid=115736651221450989198&rtpof=true&sd=true) - Then submit the proposal following the applicable rules, e.g. for
[GSoC](https://google.github.io/gsocguides/student/writing-a-proposal). 📨


# How do we judge your application?

Depending on the mentors and SoC program there are varieties, but typically the main factors considered would be:

**You have demonstrated interest in Octave and an ability to make substantial modifications to Octave**- The most important thing is that you've contributed some interesting code samples to judge your skills. It's OK during the application period to ask for help on how to format these code samples, which normally are Mercurial patches.


**You showed understanding of your topic**- Your proposal should make it clear that you're reasonably well versed in the subject area and won't need all summer just to read up on it.


**Well thought out, adequately detailed, realistic project plan**- "I'm good at this, so trust me" isn't enough. In your proposal, you should describe which algorithms you'll use and how you'll integrate with existing Octave code. You should also prepare a project timeline and goals for the midterm and final evaluations.


# What you should know about Octave

GNU Octave is mostly written in C++ and its own scripting language that is mostly compatible with Matlab. There are bits and pieces of Fortran, Perl, C, awk, and Unix shell scripts here and there. In addition to being familiar with C++ and Octave's scripting language, you as successful applicant will be familiar with or able to quickly learn about Octave's infrastructure. You can't spend the whole summer learning how to build Octave or prepare a changeset and still successfully complete your project 😇

You should know:

- How to build Octave from its source code using
[the GNU build system](http://en.wikipedia.org/wiki/GNU_build_system).- Read in this wiki:
[Developer FAQ](/ideas/gnu-octave/developer_faq),[Building](/ideas/gnu-octave/building) - Tools to know:
[gcc](https://en.wikipedia.org/wiki/GNU_Compiler_Collection),[make](https://en.wikipedia.org/wiki/Make_(software))

- Read in this wiki:
- How to submit patches (changesets).
- Read in this wiki:
[Contribution guidelines](/ideas/gnu-octave/contribution_guidelines),[Mercurial](/ideas/gnu-octave/mercurial) - Tools to know:
[Mercurial (hg)](https://en.wikipedia.org/wiki/Mercurial),[git](https://en.wikipedia.org/wiki/Git)

- Read in this wiki:

# Suggested projects

The following suggested projects are distilled from the [Projects](/ideas/gnu-octave/projects) page for the benefit of potential SoC participants. You can also look at our [completed past projects](/ideas/gnu-octave/summer_of_code), or the current [| Octave Development Roadmap](https://hg.savannah.gnu.org/hgweb/octave/file/tip/etc/ROADMAP.md) for more inspiration.

**propose your own projects**. If you are passionate about your project, it will be easy to find an Octave developer to mentor and guide you. Please note that for such a proposal to be successful it will almost certainly involve initiating pre-proposal discussion over at the

[Octave Discourse forum](https://octave.discourse.group).

## Custom re-implementation of the texi2html (v.1.82) command line tool

Implement a compiled .oct function to relax the dependency of the pkg-octave-doc package on texi2html (v.1.82) command line tool, which is no longer maintained or further developed but also not readily available to all linux distributions. The idea is to have a `texi2html` function within the pkg-octave-doc package that will replace the functionality of the texi2html (v.1.82) command line tool. This will also help improve the speed of pkg-octave-doc processing large packages, which contain specific tags (such as @math) which are currently handled within Octave code.

**Project size**[[?]](https://wiki.octave.org#Project_sizes)and**Difficulty**

- ~350 hours (hard)

**Required skills**

- Perl, C++, Octave, Texinfo, HTML

**Potential mentors**

## Add **anova** object to the statistics package

Implement anova classdef including its methods and extend the functionality of the statistics package for Analysis of Variance. More information about this project can be found at the related [issue](https://github.com/gnu-octave/statistics/issues/265) in the statistics repository.

**Project size**[[?]](https://wiki.octave.org#Project_sizes)and**Difficulty**

- ~350 hours (hard)

**Required skills**

- Octave, analysis of variance, statistics, classdef

**Potential mentors**

## Add **LinearModel** and **CompactLinearModel** objects to the statistics package

Implement LinearModel and CompactLinearModel classdefs including their methods and extend the functionality of the statistics package for linear regression by refactoring the existing fitlm function and implementing the missing stepwiselm function. More information about this project can be found at the related [issue](https://github.com/gnu-octave/statistics/issues/266) in the statistics repository.

**Project size**[[?]](https://wiki.octave.org#Project_sizes)and**Difficulty**

- ~350 hours (hard)

**Required skills**

- Octave, linear models, statistics, classdef

**Potential mentors**

## Implement missing ODE capabilities to support Chebfun

[Chebfun](https://www.chebfun.org/) uses interpolation to approximate functions to very high accuracy, giving numerical computing that feels like symbolic computing. The software is implemented as collection of “classdef” classes and is licensed under the BSD license. In the past several years, we’ve made an effort to get Chebfun working on Octave; [see the current progress here](https://gitlab.com/chebfun-octave/chebfun). However, Chebfun does not yet fully work, largely due to differences and issues with missing Octave classdef and ODE related features. We plan to continue that effort, with a focus on implementing missing ODE functionality in Octave itself. Work may include improving or extending the ODE capabilities of Octave via the SUNDIALS package, patches to Chebfun itself, or general improvement to Octave’s “classdef” implementation, depending on interest.

**Project size**[[?]](https://wiki.octave.org#Project_sizes)and**Difficulty**

- ~350 hours (hard)

**Required skills**

- Octave, numerical differential equations, polynomial interpolation and approximation theory, C++.

**Potential mentors**







# Project sizes

As of 2024, possible project sizes are 90 (small), 175 (medium), or 350 hours (large) [1].
