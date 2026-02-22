# ns-3's 2026 GSoC Contributor guide

**Parent:** The ns-3 Network Simulator Project — Project Ideas
**Source:** https://www.nsnam.org/wiki/GSOC2026ContributorGuide
**Scraped:** 2026-02-22T23:28:47.554423

---

# GSOC2026ContributorGuide

[Jump to navigation](https://www.nsnam.org#mw-head)

[Jump to search](https://www.nsnam.org#searchInput)

[Main Page](https://www.nsnam.org/wiki/Main_Page) - [Roadmap](https://www.nsnam.org/wiki/Roadmap) - [Summer Projects](https://www.nsnam.org/wiki/Summer_Projects) - [Project Ideas](https://www.nsnam.org/wiki/Project_Ideas) - [Developer FAQ](https://www.nsnam.org/wiki/Developer_FAQ) - [Tools](https://www.nsnam.org/wiki/Tools) - [Related Projects](https://www.nsnam.org/wiki/Related_Projects)

[HOWTOs](https://www.nsnam.org/wiki/HOWTOs) - [Installation](https://www.nsnam.org/wiki/Installation) - [Troubleshooting](https://www.nsnam.org/wiki/Troubleshooting) - [User FAQ](https://www.nsnam.org/wiki/User_FAQ) - [Samples](https://www.nsnam.org/wiki/Category:Samples) - [Models](https://www.nsnam.org/wiki/Category:Models) - [Education](https://www.nsnam.org/wiki/Education) - [Contributed Code](https://www.nsnam.org/wiki/Contributed_Code) - [Papers](https://www.nsnam.org/wiki/Papers)


[ns-3's GSoC contributor guide][GSoC 2026 project ideas page][GSoC contributor application template][List of past summer projects]Get in contact with the ns-3 team:[ns-developers mailing list]|Chat[https://ns-3.zulipchat.com]

# Guidelines

This webpage highlights the expectations and requirements for applicants for ns-3's Google Summer of Code (GSoC) 2026 effort.


## Project Expectations

The ns-3 team is looking for three things from every successful GSoC project:

- Developing code that can be incorporated back into the main codebase, useful to future users.
- Mentoring contributors that will remain part of the team and contribute to the ns-3 effort even *after* GSoC ends. That is, we're looking for long-term contributors and maintainers for the project.
- Providing GSOC contributors with experience and ideas that will be useful to them in their careers.

## Contributor Expectations

- At the beginning of the program, the contributor will be required to provide a detailed plan of work covering the duration of GSoC. This should be developed with the help of the mentor. Contributors will have to setup a wiki page for their project, and cover important aspects of their proposal's design, the strategy to implement it, a list of deliverables, and lastly, update the wiki page as and when each milestone is achieved. This page along with the code repository allows the community to keep track of the contributor's efforts.
- The contributor will be expected to produce mergeable code (either merged completely at the end of the project, partially at the end of the project, or not merged yet but with no major roadblocks foreseen to merge shortly after the program ends).
- The contributor will be expected to follow ns-3 design guidelines (follow coding style, write tests, documentation).
- Contributors are required to submit weekly reports on the mailing list, covering the progress they've made or the obstacles they've run into. This will help the community keep track of the contributor's efforts, and help as needed.
- The contributor will have his or her code reviewed by the ns-3 community. The reviews will be taken prior to the Google evaluations and will look at issues such as scope, public API, test plan, and open issues. All contributors will be briefed on a checklist of things to prepare for these reviews. Between these reviews, mentors will periodically (at least weekly) review the contributor's output and will provide guidance where needed, and track this progress in a public place such as a wiki entry or the mailing list.
- If a contributor drops the project before the GSoC program ends, is under-performing, or isn't communicating enough with the mentor and development team, he or she will not be passed (will not receive final payment from Google).

## Expected Background

ns-3 development typically requires proficiency in C++ and a debugger such as gdb or ddd. It is also required that the contributor knows how to use Git (at least forks, branches, merge requests), as ns-3 uses git for most of its development. The valgrind suite of tools, and a system profiler such as oprofile, are typically useful. Python may be necessary for some projects, but is generally an optional component. Domain knowledge of the components pertaining to the project is also expected.

## Application Development

In years past, many prospective applicants have tried to work privately with a mentor to develop their applications, sending many private PMs and emails. This is understandable because GSoC is a competitive process, but by working this way, the rest of the mentors and the ns-3 community do not have an opportunity to learn about the applicant, and private communication can be considered as possibly an unfair advantage. In an open source project, it is more preferable to work in public as much as possible. Therefore, some mentors may decline to help applicants in private with their application, and only respond to requests in public forums such as Zulip chat or the developers mailing list.

## AI use

The use of AI tools to draft the proposals is neither suggested, nor discouraged. However, the candidate must use the tools responsibly and:

- Be the principal driver of the proposal,
- Disclose the use of AI tools in the proposal submission (how the AI has been used, and to generate what).

In other words, using an AI as a tool to validate or improve a proposal is acceptable, using an AI to write a proposal without fully understanding the proposal itself is not acceptable, and will result in a rejection.

## The Selection Process

Selection of contributors for GSoC will be competitive. Acceptance ratios are low (typically in the range of 10-25%) and the applications that are selected are very well developed.

The contributors will be selected by a selection committee which will consist of the candidate mentors (listed on the Project Ideas page). Other mentors can participate in the application development phase and provide input to the final evaluations. Applications will be evaluated and scored according to the following criteria:


- 1) Overall technical quality of application, including whether the project seems feasible and properly scoped, whether the contributor appears knowledgeable about ns-3, C++, the models that are being proposed, sample code submitted, and the project plan including proposed milestones.
- 2) Availability of a mentor for the suggested project.
- 3) Impact and relevance to future users of ns-3? (e.g. does the proposed project support an active field of research? Are results of the project broadly applicable? Does it bring unique capabilities to ns-3?)
- 4) Participation and involvement in the community and with prospective mentors.

High scoring applicants may be asked to discuss their project details over email, chat, or online meetings. When the evaluation process concludes, the organization administrator will determine the highest ranking applicants and if there are close rankings or concerns, hold a meeting among selection committee members to resolve tiebreakers.

The ns-3 project will then rank and recommend a set of students for GSoC slots, and Google will then decide how many slots to fund for ns-3.

## Where to begin

Contributors are expected to have worked through [the ns-3 tutorial](https://www.nsnam.org/docs/tutorial/html/index.html) and to have read through and executed the code in their areas of interest.

If you need help with ns-3, you can contact the ns-3 community (either through email or Zulip). You can, and indeed you are encouraged to, interact with the ns-3 community as soon as you can, even before the GSoC period,

The [ project ideas](https://www.nsnam.org/wiki/GSOC2026Projects) that we list are starting points for contributors to develop further, with help from mentors, but we are not going to provide a specific checklist or plan; that is for applicants to develop. We are also open to ideas not found on the list; if you are excited to work on something specific, let us know and we will give you some feedback on it, and check whether there is someone available to mentor the project.

The best applications are provided by contributors who have a desire to accomplish specific goals in the project (usually aligned with their own research or interests outside of GSoC), who can articulate an understanding of the issues involved, who get involved with mentors during the application process to help refine the application, and who provide some evidence that they have a reasonable plan and the coding skills to make progress on the goals.

After you decide which ideas you would like to explore, join the [development mailing list](https://groups.google.com/g/ns-developers) or enter the ns-3 room on Zulip chat to discuss ideas with us.

You are more likely to get help if you ask specific questions that demonstrate that you have tried to make progress on a topic. A question such as "I am interested in ns-3; can you tell me how to begin?", or one that just asks generically about a project idea (e.g. "I am interested in the project idea 'DSR RFC compliance' on the wiki; can you please guide me as to how to begin?") is not likely to generate helpful guidance. A better example of a question more likely to generate good feedback would be something like: "I have read the code in the DSR module, and run the examples, and I have reviewed the RFC. It seems to me that sections X, Y, and Z of the RFC are not aligned with the ns-3 model, and I also found some comments in the code that state that something is not supported yet. Can you give me some feedback about which of these features might be the most useful to prioritize?"

Please note that all first-time posters to the ns-developers list are moderated to filter out inappropriate posts, so don't be alarmed if your email does not immediately post to the list; it will within 24 hours.

## How to apply

Contributors apply directly to Google; for more information on how to apply, please look at the [Google program site](https://summerofcode.withgoogle.com/).

While contributors are encouraged to discuss their technical plans with potential mentors on the ns-developers list, they are under no obligation to share their application details on the list.

The application format is not fixed. However, we warmly suggest to follow this [Application Template](https://www.nsnam.org/wiki/GSOC2026ApplicationTemplate), as it will make it easier to evaluate your proposals.

## Contributor benefits

- GSoC is an excellent opportunity to gain experience working on an open source project.
- Working with the ns-3 project will allow you to improve your networking knowledge, C++ skills and to be in contact with a highly skilled team of developers and user group.
- This is a great opportunity to contribute to our open source community.

## A piece of advice

Based on the ns-3 team's experiences in the previous Google Summer of Code programs, the most important factor in the success of an application and project is communication. That process begins in the application phase. Without joining the [mailing list](https://groups.google.com/g/ns-developers) or the [Zulip chat](https://ns-3.zulipchat.com) and initiating a discussion of your ideas, it is unlikely that your application will be complete or rich enough to be competitive. Please feel free to discuss your proposed technical approach, plan, and other factors on the mailing list or in the GSoC thread on Zulip while developing your application. In addition to helping you develop the necessary details, focus, and priorities to write a good application, this will also demonstrate your commitment and willingness to dedicate time to the effort. During the program, every contributor is expected to communicate regularly with their mentor, announce weekly updates of their projects and participate on the [development mailing list](http://mailman.isi.edu/mailman/listinfo/ns-developers) and discuss their work over chat.

# Contributor guidelines

These guidelines are for contributors working on ns-3 summer of code projects.

## Goals

This is a program for you to develop and merge code to ns-3. Your mentors will help guide you through the many steps required to position yourself for a successful final review and merge. While writing code is the main activity, it must be supported by good documentation, good examples, tests, and good communications with the rest of the project.

## Guidelines for accepted contributors

Here is a brief checklist of things you should try to familiarize yourself with.

**Contributing.**[Documentation about contributing to ns-3 in general](https://www.nsnam.org/docs/contributing/html/index.html).**Coding style.**Do you know how to format your code properly? Do you know how to run the auto-formatting program check-style-clang-format.py? Have you added Doxygen properly? Please read[here](https://www.nsnam.org/docs/contributing/html/coding-style.html).**Zulip chat room.**[Zulip chat](https://ns-3.zulipchat.com)is where most of the day-to-day project discussion now occurs. We will ask contributors to hang out there during their working hours.**ns-3-users forum.**Please plan to read[this list](https://groups.google.com/g/ns-3-users)daily during your project. Please also try, from time to time, to answer questions that you feel comfortable answering. Soon you will have more expertise than many of the people posting questions to this list, and you can start to help share the load of answering questions for new users.**ns-developers mailing list.**Please plan to read[this list](https://groups.google.com/g/ns-developers)daily during your project. This will be the list where you communicate with the developers to get your code reviewed and merged.**wiki.**Please read through the[wiki](https://www.nsnam.org/wiki). Contributions and edits are welcome, to fix stale information or to create new topics.**Test framework.**Do you know how the test framework works? Can you write your own test code? Please read[this documentation](https://www.nsnam.org/docs/release/3.37/manual/html/tests.html).**gdb and valgrind.**Can you run your code through gdb and valgrind? Can you run your tests through that?**AI tools.**AI tools are neither suggested nor discouraged. However, their eventual use should be discussed with the mentors and acknowledged. In any case, the developer must take full responsibility for the correctness of the code.

## Planning

Some advice:

- Refine your plan of what you want to accomplish. The plan should start out slow with some low-risk, easy to accomplish milestones, and work towards harder milestones. It is really important to think and revisit these three issues:
**Scope.**What use cases should your code support, and what is specifically out of scope, when you are done with your project?**Usability.**How do you expect users to use your code? What kind of API would users find the most natural and easiest to work with? Is it extensible by future developers?**Testing.**How can you test that your code works as expected? What tests should your code pass when it is done?

- Decompose your project into small mergeable chunks. A good workflow would be to code something new, test it, document it, post for review, and iterate. If you don't accomplish all of your technical goals because you run out of time, make sure that what you have done is mergeable (i.e. it is better to accomplish 50% of your goals, with documentation and testing completed, than 80% or 100% of your goals that does not have good documentation and testing. The latter will not be merged.)
- Commit early, commit often. This will make it easier for your mentors to track your progress.
