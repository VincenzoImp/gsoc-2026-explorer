# this one

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/wiki/GSoC-2015-Application-Sudhanshu-Mishra:-Assumptions
**Scraped:** 2026-02-22T23:28:47.570472

---

## Table of contents

* [Basic Information](#basic-information)
* [Contributions to SymPy](#contributions-to-sympy)
* [The Project](#the-project)
* [Execution](#execution)
* [Timeline](#timeline)
* [Background Work and Programming Skills](#background-work-and-programming-skills)
* [Notes](#notes)
* [References](#references)

---

## Basic Information

* **Name**: Sudhanshu Mishra
* **Email**: mrsud94@gmail.com
* **University**: BITS Pilani, India
* **Gitter/IRC**: debugger22
* **GitHub**: [debugger22](http://github.com/debugger22)
* **Blog**: http://blog.sudhanshumishra.in
* **Timezone**: IST (UTC +5:30)
* **RSS Feed**: http://blog.sudhanshumishra.in/feeds/posts/default/-/sympy

---

### Contributions to SymPy

I've created 53 pull requests out of which 41 have been merged. You can see all of them [here](https://github.com/sympy/sympy/pulls?q=is%3Apr+author%3Adebugger22+is%3Aclosed).

---

### The Project

This project aims to pick up the work started by [Aaron](https://github.com/asmeurer) of replacing old assumptions system with the new one. Although this is a lot of work and might not complete in the summer, I'll be working on it as long as it takes to complete. Since it will change the API, I think it's good to ship it before 1.0.

I saw this project on ideas page and I find it necessary and challenging. I also have a lot of things for the headstart which have already been done by Aaron. For e.g. ref. [8] and ref. [9].

[Here's](https://groups.google.com/forum/#!topic/sympy/PHR136kdxc4) the link to the topic on mailing list.

After reading a bit about various implementations of new assumptions, it's evident that the handler system won't scale. ATM, it's best to go with `sathandlers` ref. [8]. One major drawback with `satask` is that this implementation is slow.

Here's the comparison of three implementations:

```
Old assumptions:

In [3]: time Symbol('x', positive=False, real=True).is_negative
CPU times: user 0 ns, sys: 0 ns, total: 0 ns
Wall time: 184 µs

New assumptions:

In [4]: time ask(Q.negative(x), ~Q.positive(x) & Q.real(x))
CPU times: user 24 ms, sys: 4 ms, total: 28 ms
Wall time: 26.9 ms

satask (asmeurer/sympy:newassump):

In [3]: time satask(Q.negative(x), ~Q.positive(x) & Q.real(x))
CPU times: user 32 ms, sys: 0 ns, total: 32 ms
Wall time: 85.8 ms
```

To overcome this, Aaron suggested a tiered handler system. Handlers are fast but they do not provide provide features like testing inconsistencies by using know facts which SAT solvers do. We should have a system which should start from handlers and eventually go to SAT solver till it finds the answer. You can read ref. [1] to know more about why handlers are not sufficient.


---

### Execution

1. Identify inconsistencies between old and new assumptions and eliminate them by having a consensus over them mainly by discussing on the mailing list. See ref. [6] and [7] for instance.

  This won't be as easy as it sounds. The effect of these changes will break the code wherever they have been used. We'll have to make changes at all those places including the test suite.

  Considering the pace at which decisions are taken in open source communities, I'll also be working on other aspects of my project along with this.


2. Making new assumptions read old assumptions.

    For example:
    ```
    >>> n = Symbol('n', integer=True)
    >>> ask(Q.integer(n))
    True
    ```
  There are multiple ways of doing it. Ref. [10] suggests to do it by storing the assumptions set on `Symbol` in `global_assumptions` so that it becomes available to the new assumptions. But this approach has a blocking issue(ref. [11]). This is important to use weak referencing in order to facilitate garbage collection otherwise it will result in memory leak. This method will make a nontrivial change in the API such as `Symbol('x') == Symbol('x', positive=True)` as mentioned at various places. We can keep it unchanged by checking assumptions on the object in comparison methods.

 Another way is to let the `Symbol` objects have assumptions on them but enable a lazy accumulation of assumptions. This will run code only when it is needed making things faster. It'll have some limitations too e.g. it won't be able to detect inconsistency in `assume(Q.positive(Symbol('x', negative=True))` where as the previous one will do. Although this method has lesser barrier for implementation, it'll create problem while removing old assumptions in the long run.

3. Remove assumptions from the core as much as possible. The downside here is if assumptions stay in the core they add too much overhead in the computation. Perhaps, this is primarily because they are called too many times. I realized this in practice while working on [#9179](https://github.com/sympy/sympy/pull/9179).

 This is important to boost the performance. Old assumptions is used heavily in the core for automatic simplification which slows things down. `refine` is the new way of doing so which uses new assumptions. We can use `refine` to do the autosimplification and make it optional.

4. Making API of old assumptions call new assumptions internally. The target would be to achieve minimum ripple effect throughout the codebase as the changes are made.Once both assumption systems are consistent, replacing old assumptions with new assumptions would be just find and replace. Though easy, we'll have to take care of the regression and performance.

---

### Timeline

From my past experiences I can say that things can change in a very small period of time. For example, some bug comes up which has to be fixed before anything more can be done. However, I'll propose a tentative timeline for this one too after discussing the plan of execution with my mentor. This, at least, helps in keeping tab on how much you are lagging.


##### Pre GSoC period

Start working towards merging ref. [8] and work on ways to improve SAT solvers.

Start working on am experimental idea to write done the combinations of common facts and then pre-compute the possible results in a different thread at bootp. Later on, this can be used to deduce answers a little faster by just checking in the table. As of now, I'm not sure how it'll affect performance of normal routines. I'll post a report very soon. This is similar to caching except that cache system replaces old/unused stuff in the memory.

I would also like to give my idea a try on managing context without using assuming. This can be done by having another name in Symbols say `assump_name` and using this one to store in `global_assumptions` rather than the original one.

For example:

```
>>> # Since there is no x in global_assumptions yet, this will set
>>> # assump_name to 'x_0' 
>>> x = Symbol('x', real=True)
>>> def my_func():
>>>     x = Symbol('x', positive=True)
>>>     # This will check global_assumptions for 'x_0', if found it'll set
>>>     # the assump_name to 'x_<next_index>' and have the
>>>     # assumptions in global_assumptions with the same name.
```

##### Community Bonding Period

As I'm already a SymPy developer I'll not waste time learning basic things about SymPy. I can use this time to start working on my project. The speed might be slow as I'll have exams during this period. In this period I'll start fixing inconsistencies between both assumptions.

##### Week 1, 2, 3

In this period I'll mainly focus on improving ref. [8] and get it merged into the master. I'll also try to complete ref. [5].

##### Week 4, 5, 6

Work on exec. 1. i.e. enabling new assumptions to read old assumptions. I'll start with first method proposed in exec. 2. This includes fixing the blocking cache issues. The target of this period will be to have this one working with full tests and documentation.

##### Week 6, 7, 8, 9

Separate out assumptions from the core and also fix inconsistencies if any. Disabling autosimplification will break a lot of things which might take time to fix. This will also include fixing issues listed in issue tracker related to core and assumptions.

##### Week 10, 11, 12

Catch up time.

* I'll spend this time towards merging unmerged work.
* Documenting everything.
* Do anything left to kickstart new assumptions.
* Writing regression tests and benchmarks.

---

### Background and Programming Skills

I am a third year undergraduate student of Information Systems at BITS Pilani, India. I've been contributing to SymPy for over an year and was accepted as a student in GSoC'14. The basic version of my project was shipped in the latest release. It's not fully complete though. I'll try to improve it in future.

I use Ubuntu in general. I keep switching the desktop environment for mixed reasons. I've also used FreeBSD and CentOS as servers. I use Sublime Text for development and vim/nano for SSH sessions. I'm also well versed with IntelliJ IDEA as I've been working on Android apps for quite some time.

I've done basic engineering courses on Mathematics. Few more courses that are best suited for the project:

    * Logic in Computer Science
    * Data Structures and Algorithms
    * Principles of Programming Language
    * Discrete Mathematics in Computer Science
    * Software Engineering
    * Software Testing

Other than these I've also done courses like Operating systems, compilers, etc.

I'll be devoting my full time during the summer. As of now I've nothing planned for the summer.

Following are some of the open source projects that I created using Python:
* [BinPy](https://github.com/BinPy/BinPy) For electronics computation and simulation. It is a library to provide a base to develop circuit based applications and educational software on top of it. We were a mentoring organization under the umbrella of PSF in GSoC'14 which was mentored by my college seniors.

* [Jarvis](https://github.com/IEEE-BITSG/Jarvis) A small attempt to clone Jarvis like system using Google's STT and TTS. *It doesn't work now because Google deprecated its free speech engine. :(*

* [Sentiment Analyzer](https://github.com/debugger22/sentiment-analyzer) A sentiment analyzer especially for tweets.

I've also deployed two Android apps on Google Play which I created with my friends.

* [Lenx](http://www.lenxapp.com) It simulates long exposure photography on Android. It uses OpenCV for that purpose. We've also used Google's RenderScript and C++ to boost performance.

* [Potential](https://play.google.com/store/apps/details?id=com.paranoidgems.potential) It's a web based application which syncs battery, wifi and bluetooth across all your devices. We've used Java for Android and JavaScript for backend.

Some of my other projects that I did for my courses can be seen [here](https://github.com/debugger22?tab=repositories).

Python has very shallow learning curve. I like it mainly because it is an interpreted language which gives you freedom to do so much things dynamically. Prototyping anything in Python is very easy and requires less man-work than any other programming language. I've used IPython notebooks to give lectures while teaching Python to fellow students in my college. Since I started programming as a web developer, I used `django` all the time which made me familiar with Python in the beginning.

I like `itertools` because of its magical functions which are written to handle iteration based algorithms. They are fast and use memory efficiently.

From a developer point of view I love the object oriented hierarchy of SymPy. This really helps the developers in extending SymPy. As a user I like the feature which shows steps of integration on sympy gamma.

I've been using git and GitHub for more than two years and I think that I've mastered the basics.

---

### Notes

* Some part of this proposal has been taken directly from [Aaron's post](https://groups.google.com/forum/#!topic/sympy/PHR136kdxc4) on the mailing list as I agree with them.

* Although not stated in the timeline, I'll be sending pull requests often to make sure that reviewing is easier. This also increases the chance of getting things merged into the master.

* I have no commitment during summer which means I'm free to work completely on my project.

* I am enthusiastic about seeing my work getting used by people. If by any chance my work doesn't get merged in the master by the end of the summer, I would work towards merging it beyond the summer.

---

### References

[1]. [GSoC 15: Improving Assumptions](https://groups.google.com/forum/#!topic/sympy/PHR136kdxc4)

[2]. [A plan for the assumptions](https://groups.google.com/forum/#!msg/sympy/wlXB4jngnW0/8G5QNz3Kf0EJ)

[3]. [Migrate from old assumptions to new assumptions](https://github.com/sympy/sympy/issues/6730)

[4]. [Assumptions handlers](https://github.com/sympy/sympy/wiki/assumptions_handlers)

[5]. [Documenting new assumptions](https://github.com/sympy/sympy/pull/2538)

[6]. [Contradictory facts about infinities in the new assumptions](https://github.com/sympy/sympy/issues/5976)

[7]. [S.Zero.is_imaginary should be True](https://github.com/sympy/sympy/issues/7649)

[8]. [Proof of concept for the new assumptions](https://github.com/sympy/sympy/pull/2508)

[9]. [Proof of concept: new assumptions check old assumptions for Symbol](https://github.com/sympy/sympy/pull/7925)

[10]. [Add symbol's assumptions to the global_assumptions context](https://github.com/sympy/sympy/pull/7926)

[11]. [Can't use both weakref's & cache](https://github.com/sympy/sympy/issues/8825)

[12]. [Assumptions (wiki)](https://github.com/sympy/sympy/wiki/Assumptions)
