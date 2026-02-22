# Gambit: The package for computation in game theory — Project Ideas

**Source:** https://www.gambit-project.org/gsoc_2026/
**Scraped:** 2026-02-22T23:28:47.544846

---

The Gambit project is sumbitting projects as an organization for [Google Summer of Code 2026](https://summerofcode.withgoogle.com/).
Prospective contributors interested in working with the Gambit team should read the “Contributor Guidance” and “Project Ideas” sections below.

Google Summer of Code is a global, online program focused on bringing new contributors into open source software development. GSoC Contributors work with an open source organization on a 12+ week programming project under the guidance of mentors.


Please provide a CV and short cover letter. On your CV, include any relevant domain experience in game theory, and technical skills and experience in software engineering. We recommend to read through the Project Ideas below before submitting an application.

In your cover letter please include answers to the following questions:

- What interests you most about the Gambit project?
- Which specific project idea(s) are you most interested in and why? Note: While we do not rule out contributors proposing their own ideas, projects need to align with Gambit’s overall goals and must be feasible given the time available and your skills. Please cover how these aspects are met if you propose your own idea.
- Please provide us with details of the times of day and days of the week you intend to work on the project, to help us in scheduling regular catch ups.
- Is there anything that you’ll be studying or working on whilst working alongside us?

Prospective contributors should read through the project ideas listed below before submitting an application, following the Contributor Guidance above. Select a project based on your research interests and the technical experience you have, or would like to develop.

For each project we have listed at least two possible mentors, with the first mentioned mentor like
to be the primary one and the other one able to act as a secondary additional mentor.
Our core team of mentors for 2026 are: [Ted Turocy](mailto:ted.turocy@gmail.com), [Rahul Savani](mailto:rahul.savani@gmail.com),
and [Ed Chalstrey](mailto:echalstrey@turing.ac.uk).
Bernhard von Stengel can act as an additional mentor for ideas 3 and 6; Bernhard authored the
`draw_tree`

and `lemke`

packages that underpin these two projects, respectively.

The following table summarises our ideas, and includes links to detailed descriptions below.

| Idea/link | Title | Difficulty | Keywords |
|---|---|---|---|
|

Gambit’s graphical interface is the oldest part of the package. It traces its origins to a MS-DOS based tool written in C++ using the Borland Graphics Interface (BGI) in the early 1990s. It was ported to wxWindows (now wxWidgets) in the mid-1990s, in the early days of that package. Growing emphasis on scriptability and calculation at scale has meant the GUI has received less attention in recent years. Nevertheless, it remains important to the package and the community as it is the point of entry for many users, either through use in teaching or in manually inputting small games for exploratory analysis.

In this project, we will modernise the implementation of the graphical interface. This will involve a combination of several inter-related strands:

The history of development and maintenance of the GUI means it has not been modernised to use wxWidgets 3.x features, retaining a lot of history of 2.x (and in some places possibly even 1.x) style. We will update the implementation to use modern wxWidgets and C++17 idioms.

The interaction design of the canvas used to display game trees, and the tables used to display games in normal form, is less than ideal, with features like drag-and-drop, scrolling, and so forth being sometimes unreliable. These are due in part to legacy, in some cases dating back to the BGI implementation. We will clean up the dated parts of the interface to an application that gives a more modern appearance.

When the GUI was invented it was not possible to do meaningful analysis of games much larger than could be drawn by hand. Today Gambit supports the analysis of huge (by comparison) games. We will improve the scalability of the GUI to use the concepts we have developed for working with large games, including the ability to load and work with “standard” games from the extensive catalog of examples and benchmarks we have developed.


The key expected outcome of this project is a modernised version of the Gambit GUI.

Experience with C++ is essential; experience with wxWidgets is desirable but not essential.

We consider this a 350 hours project, especially if a student fully takes forward all 3 inter-related strands mentioned in the description. There is scope for a scaled down 175 hour project, but 90 hours does not appear enough to make enough progress to make this worthwhile.

Medium. Strands 1 and 2 should be relatively easy for someone with suitable C++ experience. The 3rd strand is more open-ended and challenging.

We have developed tools that leverage Large Language Models (LLMs) to translate natural language descriptions of games into formal game-theoretic models within Gambit. See, e.g.,

Shilong Deng, Yongzhao Wang, Rahul Savani:
*From Natural Language to Extensive-Form Game Representations*. **AAMAS 2025**: 593-601.

The method in that paper was called GameInterpreter v1; we are actively developing newer versions. In this project, a student would develop a front end that would allow users to explore the different versions of GameInterpreter.

For a blog post describing the work above see: [https://www.turing.ac.uk/blog/introducing-gambit-tool-doing-computation-game-theory](https://www.turing.ac.uk/blog/introducing-gambit-tool-doing-computation-game-theory).

A basic version of this project would provide a front end to allow users to run different translators
and compare and contrast the outputs.
An extended version would also incorporate our new methods for *automatically evaluating* the
correctness of translations.

The key expected outcome of this project is a browser-based front end that lets user explore our tools that translate natural language descriptions of game to formal game-theoretic models within Gambit.

Experience with browser-based front-end development is essential.

90 hours for the basic version; 175 hours if the extension is done too.

Easy/Medium.

Extensive form game trees differ from other kinds of trees in graph theory due to the presence of information sets, which make drawing such trees a unique challenge not addressed by other software packages. In Game Theory, in any game with “imperfect information”, where some players are not fully informed about the state of the world, information sets group decision nodes based on the information available to players.

The Gambit project team have developed `draw_tree`

, a Python package which works in tandem with `pygambit`

(Gambit’s Python implementation) to draw extensive form game trees. The package is already used in Gambit’s Python tutorial documentation, but is also intended to be used for other purposes, in particular generating publication-ready images of game trees for research papers.

The best current layout algorithm used in `draw_tree`

is based on code originally developed for Gambit’s GUI software, which doesn’t nicely render all the examples in Gambit’s catalog of games, especially large ones with many information sets. The aim of the GSoC project would be to develop a new layout algorithm that can sensibly draw games of various sizes and complexity, including many information sets.

This project would suit someone who has a particular interest in visualisation challenges. For reference, check out the [“Stripped-down poker”](https://gambitproject.readthedocs.io/en/stable/tutorials/03_stripped_down_poker.html) tutorial from the `pygambit`

documentation, which demonstrates how `pygambit`

is used to construct, and `draw_tree`

is used to visualise, a small extensive form game, including an explanation of the information sets present in the game.

The key expected outcome of this project is an implemented and tested new visualiztion algorithm for `draw_tree`

.

Experience with Python is essential; experience with “graph drawing” algorithms is desirable but not essential. Keen interest in visualization and aesthetics is essential.

[Ed Chalstrey](mailto:echalstrey@turing.ac.uk); [Ted Turocy](mailto:ted.turocy@gmail.com). Bernhard von Stengel, who designed and authored the original `draw_tree`

implementation can act as an additional supporting mentor.

350 hours.

Hard. Developing a suitable layout algorithm that works across a wide range of games and then implementing it and testing constitutes a significant project that we expect to take up a full 350-hour project and to be challenging.

SageMath is a prominent open source mathematical software system. SageMath has some existing support for Game Theory, including some interoperability with Gambit version 15. There is a desire on both the Gambit and SageMath sides to improve interoperability and to get SageMath working fully with Gambit version 16.5 and later – see the following PR: [https://github.com/sagemath/sage/pull/37809](https://github.com/sagemath/sage/pull/37809). In this project, a student would work to update that PR with a view to getting it merged by SageMath. In addition, a student could develop tutorials to demonstrate existing and new interoperability between Gambit and SageMath (see the following issue from Gambit’s repo: [#627](https://github.com/gambitproject/gambit/issues/627).

The key expected outcome of this project is a merged SageMath pull request that would see the latest versions of Gambit integragted into SageMath. Ideally the integration will also be demonstrated with tutorials and docs.

Experience with Python is essential; experience with SageMath is desirable but not essential.

90 or 175 hours. While it might be possible in 90 hours to implement the basic SageMath integration needed to get a PR merged, we would have a strong preference for a student to also produce rich materials (such as tutorials and examples) that show off the new integration, for which a 175 hour project seems more reasonable.

Easy.

Many mathematical problems that arise in game theory can be expressed in standard formulations. For example, there are many problems which can be expressed as linear programs, or the solutions to a system of polynomial equations and inequalities. Gambit has routines for solving these problems; for example, Gambit has an internal LP solver, in part because it was not straightforward to call or link with external packages circa 1994! In the modern scientific computing ecosystem, there are packages specialised to classes of mathematical programming or optimisation problems which will be far more performant.

Gambit currently has some very limited support for interfacing with some selected external tools via formulating the relevant problem in the file format required by that tool, running the tool, and then mapping the output back into game-theoretic objects. This support is ad-hoc, and limited to certain tools - for example, at the moment Gambit does not have any support to use external LP solvers.

In this project, we will develop a better framework for this process of generating the problem instance and mapping the result back into Gambit objects, that will be more extensible to different project types and different external solvers. In particular, as an important use case, we will develop the formulation of the linear programs that arise in several different places in game theory, and provide interfaces to different user-selectable LP solvers.

We are already aware from ad-hoc testing that in many cases the use of external solvers leads to huge performance gains, so success on this project would lead to a substantial increase in the size of game which is feasible to analyse.

The expected outcome of this project is an improved framework for working with external solvers in Gambit. At a minimum requirement, the existing external solvers (e.g. lrc and PHCpack) should use the new framework. As a stretch goal, an extended project could see several new external solvers integrated with Gambit via the new framework.

Experience with Python is essential; experience with mathematical optimization/programming is highly desirable.

The core outcome of an improved framework for dealing with solvers could conceivably be done in 90 hours. Integration of new external solvers within the new framework could take the project to 175 hours, or even 350 depending on the number and complexity of the new external solvers.

Medium/Hard.

Lemke’s algorithm is an important method in mathematical optimization for solving “Linear Complementarity Problems” (LCPs). Two player games, either in extensive or strategic form, the two primary game formats in Gambit, can be cast as LCPs solved using Lemke’s algorithm and variants of it. While Gambit has an in-built implementation of Lemke’s algorithm in C++, we would like to integrate a python implementation of Lemke’s algorithm by Benrhard von Stengel.

The project would have two main parts:

Improve the “lemke” package, see

[https://github.com/gambitproject/lemke](https://github.com/gambitproject/lemke), and release it as a standalone LCP solver package. That package should support both standalone tools and be a callable library, for example with work needed on argument parsing (e.g. using the “click” package). There is also scope for also improving the code to be more pythonic. In addition, a test suite should be written for the package.Integrate the new “lemke” package with core Gambit (

[https://github.com/gambitproject/gambit/)](https://github.com/gambitproject/gambit/)), as an optional dependency, and alternative to the in-built Lemke solver.

The key expected outcomes of this project are:

- A modernised standalone “lemke” package;
- Integration of the modernised package with Gambit.

Experience with Python is essential; relevant background in complementary pivoting, or at least mathematical programming methods like the Simplex method ([https://en.wikipedia.org/wiki/Simplex_algorithm](https://en.wikipedia.org/wiki/Simplex_algorithm)) are highly desirable.

[Rahul Savani](mailto:rahul.savani@gmail.com); [Ted Turocy](mailto:ted.turocy@gmail.com); the author of the Lemke package ([https://github.com/gambitproject/lemke)](https://github.com/gambitproject/lemke)), Bernhard von Stengel is also available to act as an part-time mentor on this project (in addition to having a primary and secondary mentor from the core Gambit team).

175 to 350 hours.

Medium/Hard.

There are several methods for computing Nash equilibrium which are based on numerical continuation, i.e. following a smooth (differentiable) path defined by a system of equations. Gambit has implementations of a few of these methods, but there are a number of others which have been published which Gambit does not yet include.

Two examples which are currently in Gambit’s issue list are:

*A differentiable homotopy to compute Nash equilibria of n-person games*. Herings, P. & Peeters, R. Econ Theory (2001) 18: 159. doi:10.1007/PL00004129 ([http://link.springer.com/article/10.1007%2FPL00004129](http://link.springer.com/article/10.1007%2FPL00004129) (See Gambit issue [https://github.com/gambitproject/gambit/issues/193](https://github.com/gambitproject/gambit/issues/193))

*A variant of Harsanyi’s tracing procedures to select a perfect equilibrium in normal form games*. Cao, Y. and Dang, C. (2022) 134: 127-150. [https://www.sciencedirect.com/science/article/abs/pii/S0899825622000719](https://www.sciencedirect.com/science/article/abs/pii/S0899825622000719) (See Gambit issue [https://github.com/gambitproject/gambit/issues/304](https://github.com/gambitproject/gambit/issues/304))

While ultimately we would like to have C++ implementations of these methods, it would also be useful to create Python-based prototypes (using numpy for the numerical heavy lifting), which would aid in the production of test and benchmarking suites for these methods.

(There are many other methods for computing Nash equilibria and other solution concepts; we are interested in proposals to implement any of these within Gambit.)

The expected outcome of this project is implementations of one or more new equilibrium computiation methods, with these implementaitons integrated into Gambit.

As mentioned the implementations can be in either Python or C++, so experience in one or both of those is essential.

Experience with the background in mathemetical optimization/programming behind equilibrium computation algorithms is highly desirable.


All three sizes of project are possible with this idea, depending on how many and how complex the implemented algorithms are.

Medium/Hard.

While some algorithms themselves can be quite involved, there are also potentially easier algorithms a student might choose to implement. Also, this project idea is only minimally constrained by the existing Gambit code base, and thus the challenge is really on picking, understanding, and then implementing an equilibrium computation method or methods, which can give rise to easy or hard projects, depending on the methods chosen.

[OpenSpiel](https://github.com/google-deepmind/open_spiel) is a collection of environments and algorithms for research in general reinforcement learning and search/planning in games created and maintained by Google DeepMind.

OpenSpiel already supports export to Gambit’s two primary game formats, namely the strategic, aka normal, form games (NFGs) and the extensive-form games (EFGs). However, these exporters a) have restrictions and b) are not well documented. In particular, even though OpenSpiel (and Gambit) supports payoffs at non-terminal nodes, the OpenSpiel exporters only work if all payoffs (aka rewards) are at terminal nodes.

The idea here is to develop the existing exporters to make them more general, covering non-terminal payoffs, and also better documented.

Here are pointers to the existing exporters (two for each type of game format):

[EFG exporter in python](https://github.com/google-deepmind/open_spiel/blob/master/open_spiel/python/algorithms/gambit.py)[Independent EFG exporter in C++](https://github.com/google-deepmind/open_spiel/blob/master/open_spiel/game_transforms/efg_writer)[NFG exporter written in C++](https://github.com/google-deepmind/open_spiel/blob/master/open_spiel/algorithms/nfg_writer.cc), exposed to Python and[tested](https://github.com/google-deepmind/open_spiel/blob/master/open_spiel/python/tests/nfg_writer_test.py)

As a stretch goal, a student could work on an .efg importer after finishing the exporter. Again
there is [one](https://github.com/google-deepmind/open_spiel/tree/master/open_spiel/games/efg_game/games) in OpenSpiel
but it does not support as many games as we would like.

The expected outcome of this project is a pull request to OpenSpiel that provides more general exporters. The new exporters should be well tested, including of course, on games with non-terminal payoffs.

Ideally the exporter would be written in C++ for speed, but extending the Python exporter would also be useful. So a student should be comfortable with C++ and/or Python.

It will be helpful if a student already knows what EFGs and NFGs are, which they would have learnt in any basic Game Theory course.


90 hours – that should be enough for both EFG/NFG exporters, and ideally also importers for both, along with documentation and tests.

Easy.

On this page
