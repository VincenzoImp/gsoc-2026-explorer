# Tips for writing a good GSoC proposal

**Parent:** GNU Mailman — Project Ideas
**Source:** https://wiki.list.org/DEV/SPAM
**Scraped:** 2026-02-22T23:28:47.587840

---

# Student Proposals Augmenting Mailman

SPAM us at `<mailman-developers AT python DOT org>`.


## How Not to SPAM

Don't do this:

To: mailman-developers@python.org Subject: I want a Mailman mentor for GSoC Dear Mailman: I want to be a GSoC student. Please take me, please, please, please, please? Yours truly, A. N. Unlikely Candidate

Like all GSoC projects, we're looking for students who *care* about Mailman, and want to improve *Mailman*. The application above screams "I need money!" Yes, we know that, and there's nothing wrong with wanting money. Almost everybody does (if only because they could give it to somebody else). But there are candidates who we can tell will do a good job for us. They need money too, you know.


## How to SPAM

Briefly, you need to

- Find out about Mailman.
- Decide which part of Mailman you want to contribute to.
Decide on a particular task,

*i.e.*, a problem to solve.- Propose a plan to solve the problem:
- Tell us who you are.
- Tell us what you want to do for Mailman.
- Tell us what code you will write to get it done.
- Tell us when you'll get it done.


This is what software professionals do over and over again at work. (Except for part 4a, but they have to do that once, just like you.) One of the purposes of the GSoC is to provide mentors who can help you accomplish those preliminary tasks, as well as produce excellent finished code.


## A Few Hints

Step 1: Find out about [Mailman](http://www.list.org/). Mailman started out as a mailing list manager: it keeps a database of lists, subscribers, and posts; moderates and distributes the posts to the subscribers; and maintains an archive of past posts that users can access by mail or web. It is written in the [Python](http://www.python.org/) programming language. You are welcome to ask questions either on the [Mailman users' list](http://mail.python.org/mailman/listinfo/mailman-users) or on the [Mailman developers' list](http://mail.python.org/mailman/listinfo/mailman-developers). Other things equal, we prefer to mentor students who have shown interest in working on Mailman before applying (but it's not at all required).

**Do** feel free to ask the mentor team about early drafts of your proposal. You must write it yourself, but we can tell you if you're writing about the right things, and if you are providing the right details.

Step 2. Decide where you'd like to contribute. [Mailman 3](https://wiki.list.org/DEV/Mailman%203.1) is written in Python. It is divided into three main subprojects, whose development trunks are on [GitLab](http://gitlab.com/mailman):

[Mailman 3 core](https://gitlab.com/mailman/mailman): implements- the list and subscriber databases, and the mail distribution functionality.

[Postorius](https://gitlab.com/mailman/postorius): a[RESTful](https://advanced-python.readthedocs.org/en/latest/rest/what-is-rest.html)web interface for managing the list and subscriber databases.

[HyperKitty](https://gitlab.com/mailman/hyperkitty): the- archive manager and web interface to the archives.


While the developers all communicate with each other, especially in developing shared APIs, actual design and coding takes place in smaller groups organized around these subprojects. There is a list of [suggested tasks](https://wiki.list.org/DEV/Google%20Summer%20of%20Code%202022) for GSoC.

Step 3. Pick a task. Why you pick a task is up to you. But feel free to ask the mentors or the lists. Maybe you just want the help the developers by doing something we'd do otherwise. Ask on the [developers' list](http://mail.python.org/mailman/listinfo/mailman-developers) for our priorities and advice on what's actually do-able in the GSoC time frame. Maybe you want to implement a new feature. Check [GitLab](http://gitlab.com/mailman) for feature requests, and maybe review the [users' list](http://mail.python.org/mailman/listinfo/mailman-developers) archives and [the FAQ](https://wiki.list.org/DOC/Frequently%20Asked%20Questions). Ask the developers if it can be done in time.

Step 4. [SPAM](https://wiki.list.org/DEV/SPAM#How_to_SPAM.2C_in_Detail) us!

See also [How Not to SPAM](https://wiki.list.org/DEV/SPAM#How_Not_to_SPAM).


## How to SPAM, in Detail

"SPAM" is a "Student Proposal Augmenting Mailman." Perhaps you've contributed to an old-style open source project or done an internship where developers hack on code and simply commit it to the mainline repository when they're pretty sure there aren't any bugs in the new code. Sure, Linus did it that way -- but don't expect to get *your* code in *his* kernel that way! The trend is to more formal processes including explicit design and review stages. Pragmatically, GSoC requires some formality because Google requires us to report on interns' progress and review their code. But we also need some documentation to ensure that we make the best use of the few interns we are assigned, and we're used to it because many changes to our favorite language, Python, require [Python Enhancement Proposals](http://www.python.org/dev/peps/pep-0001/).

A SPAM is not as formal as a PEP. However, you should take care in preparing yours, because it's one of the few things we have to go on in deciding which students to accept. A SPAM should contain certain specific information, there's a lot of more or less optional information you can include to improve both your chances of acceptance and the project itself, and it probably won't hurt to organize it as described below.

Do **not** worry if you can't write an accurate design or plan yet. Planning and design are arts, and probably the most important things a mentor can help a student to learn to do. That's really what GSoC is about. And, of course, some students won't know that much about Mailman to start with. So just do the best you can now to give us an idea of what you want to do, and your mentors will help you whip it into shape during the "get to know each other" preliminary phase.

But if you *do* come up with a good design and schedule by yourself, that's very attractive to mentoring orgs (not just Mailman, believe me!) What follows are some hints on what to aim for in your proposal.


### Self-Introduction

Tell us about yourself. Full name, school affiliation, year in school, of course. Previous programming experience, including languages used and publicly documented projects you've worked on, if any. URLs for any web resources about yourself are useful, including anything from Facebook pages to GitHub projects.

You will eventually need a [GitLab](http://gitlab.com/) login to publish and submit your contribution for review and integration. That and your email address, as well as a phone number, are essential contact information. It is often helpful to have a stable IRC nick that you can use on the Mailman channel (#mailman on [Libera](https://web.libera.chat)).


### Coding Proposal: Theme

Robert Townsend wrote in *Up the Organization*: "[Top management] knows that any proposal affecting their business can be explained in one minute." My colleagues were horrified to be compared to management of any ilk, but the principle holds. It's both possible, and important, to be able to express what your proposal is about relatively briefly. Provide both a one-line summary that can serve as a title for your project, as well as a slightly more detailed (around 5 lines) explanation of how you propose to accomplish your task.

We have a number of [suggested tasks](https://wiki.list.org/DEV/Google%20Summer%20of%20Code%202022). You are welcome to select one that appeals to you. If you *do* choose one of these tasks, your ideas about the task, and an original description of the task, are important to convince us you have thought about the task. Don't just copy our description into your proposal. Rewrite it in your own words, adding your own ideas.


### Coding Proposal: Design

This is a very high-level design. You can express it as prose or as pseudo-code. More important than an exact description of the code you propose to write is showing us *how little* you need to do to accomplish your goal. Tell us about existing modules on [PyPI](http://pypi.python.org/), [GitLab](http://gitlab.com/), or [GitHub](http://github.com/) that can do "90% of the work". (Don't worry, you'll be wrong. There will be *plenty* of work left for you to do.) Explain how these modules and your implementation will hook into the rest of Mailman. (This is usually the hardest part, because most students know little about Mailman to start, and don't know where to start. Please ask! That's what IRC and the lists are for!)

You will not be done with the design, yet, so don't worry. You *will* need to refine it somewhat, in order to complete your [schedule](https://wiki.list.org/DEV/SPAM#Coding_Proposal:_Schedule).


### Coding Proposal: Schedule

Perhaps unlike anything you've done before, GSoC has several deadlines that you *must* meet or *you will get fired* (*i.e.*, **not paid**). While many [curmudgeons](http://en.wikipedia.org/wiki/curmudgeon) will argue that *getting fired* is a "valuable educational experience", it reflects as badly on your mentors as it does on you. We do **not** want that to happen. We have come close to firing a student at the midterm in the past; it *can* happen. Accurate scheduling is important to *you*.

First, review the official GSoC deadlines. They are posted on the [GSoC site](http://summerofcode.withgoogle.com/). Add them to your personal GSoC schedule.

Second, for each official GSoC deadline, add a date one week before to confer with your mentor about your progress in general, and any specific milestones you need to complete to pass your reviews. This is a date where, if your mentors don't get in touch with you, you must get in touch with them. If you can't reach the mentors, get in touch with the Mailman org representative, Stephen Turnbull (yasegumi on #mailman), or the alternate org representative, Abhilash Raj (maxking on #mailman). Add these dates to your personal GSoC schedule.

Third, set milestones for yourself. A *milestone* is a subtask that can be objectively verified. For example, "coding is 50% complete" is *not* a milestone, because you don't know how much code you have left to write, you can only estimate it inaccurately. "Coding is complete, documentation is complete, unit and integration tests all pass, branch pushed to GitLab, and a merge request filed" is a milestone, because all of the above are easily verified events. In fact, this is the most important milestone, which you should schedule for September 5 right now, because it is the criterion for passing your final review.

In a perfect world, a student would set about one milestone per week, which is pretty convenient for both our evaluations and your self-evaluations. However, as a practical matter, setting milestones depends on a detailed design, and you probably won't produce a detailed design until after you've been approved for the program. In your application to us, it is very helpful if at least you are able to provide your midterm milestone (dated July 25).

In order to produce milestones other than final completion, you need to have a somewhat detailed design. At this point, go back and revise your design, then pick some specific task and set it as a milestone. To get to your midterm milestone, think of it as the set of your earlier milestones. As you add each milestone, consider how much work that set of milestones represents. If that's not enough to constitute half the work, revise your design again, and set another milestone.

**Do** feel free to ask the Mailman mentor team about your milestones. Few developers find it a natural way to think about development at first. We can and will help you with it as you develop your proposal.

The fourth step in scheduling requires the most care. Look at your private schedule, and see what is going to cause conflicts with your GSoC schedule. Maybe you have a summer course at school. Or your school's spring examination schedule conflicts with GSoC. Maybe your older brother is getting married on the other side of the world from where you are. We don't need to know *what* it is, but you need to tell us *when* it is, and *adjust your GSoC schedule* to accommodate your private plans. Of course you can't change the GSoC deadlines, and there's really no leeway there for us, either. What *you* can do is to adjust the timing of your milestones, and what *we* can do is adjust our expectations for the midterm review.

Note that this is an adjustment in timing, not an adjustment in the size of the completed project expected. Software work is like that for many developers: sometimes they work a 5x8 week, and other times they work a 15+15+10+0+0 week. *We* understand that reality. But *you* need to think in terms of picking up the pace before and after if you take time off. On the other hand, if your time off is too great, you will **not** be able to catch up. Really -- we've been there.

And be realistic. If you have extensive other plans for your summer, you probably should give up on GSoC. Google expects you to treat your internship as a full-time job during the coding period. (Of course you can always change your other plans if GSoC is important to you!)

Be honest with yourself, and be honest with us. You will have a much more enjoyable *and profitable* summer that way. If your plan crowds too many milestones into the first half or second half of the summer, we won't believe you can do it, and you won't be asked to participate. If you pretend that you can keep a better balance than is realistic given other commitments, you will fail a review. We've seen it happen before.
