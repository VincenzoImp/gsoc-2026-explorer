# GNU Compiler Collection (GCC) — Project Ideas

**Source:** https://gcc.gnu.org/wiki/SummerOfCode
**Scraped:** 2026-02-22T23:28:47.608468

---

# Google Summer Of Code

GCC has applied to be a GSoC mentoring organization in 2026. If successful, the primary org-admin is going to be [Martin Jambor](mailto:mjambor@suse.cz). However, it is always better to contact the whole community by emailing [mailing list](/ideas/gnu-compiler-collection-gcc/mailman-listinfo-gcc) [gcc@gcc.gnu.org](mailto:gcc@gcc.gnu.org) if you have any questions or requests - please put "GSoC" somewhere to the subject. If you are interested in gcc-rust topics, you can also reach out to the gcc-rust community via [Zulip](https://gcc-rust.zulipchat.com/).

If you would like to be a GSoC contributor with GCC, first make sure you read the [Before you apply](https://gcc.gnu.org/wiki/SummerOfCode#Before_you_apply) and [Application](https://gcc.gnu.org/wiki/SummerOfCode#Application) sections on this page and then pick a project, possibly from the list below. After you made your selection or have a project idea of your own, please discuss it as soon as possible (way before the application) via the [gcc@gcc.gnu.org mailing list](/ideas/gnu-compiler-collection-gcc/mailman-listinfo-gcc) (put "GSoC" somewhere to the subject too) and feel free to raise it on [IRC](https://gcc.gnu.org/wiki/GCConIRC). Again, gcc-rust projects should be discussed via their [Zulip](https://gcc-rust.zulipchat.com/).

Contents


## Selected Project Ideas

When discussing GSoC project ideas in the community, we have found out we are especially interested in the following few. One of their main advantages, apart from their particular relevance and usefulness this year, is that we are confident we can find mentors for them. We will however also consider other projects and we will be happy to discuss your own ideas with you. Nevertheless, please do consider applying for the following:

**Rust Front-End**. GCC's front-end for Rust is in development please see:[https://github.com/Rust-GCC/gccrs](https://github.com/Rust-GCC/gccrs). A number of projects are available, you can choose one of the following. Required skills include C/C++ and finding a way through a large code-base, some knowledge of Rust would of course also be highly beneficial. Note that proposals written entirely using generative AI will be automatically rejected. We would love to read your proposals regardless of your level in English, and as long as the content comes from you directly. Finally, it is extremely important to interact with our community on our[Zulip chat](https://gcc-rust.zulipchat.com/), IRC (#gccrust on oftc.net), mailing list ([gcc-rust@gcc.gnu.org](mailto:gcc-rust@gcc.gnu.org)) or[GitHub](https://github.com/rust-GCC/gccrs/)repository. Code and non-code contributions matter tremendously when selecting candidates.*Add infrastructure required to compile the "alloc" crate*- The rust frontend is slowly progressing toward the complete compilation of the "core" crate. The next step before compiling the standard library is the allocation library.
- The rust frontend may not be able to process some bits within the alloc crate.
- The allocation library requires some special intrinsinc mechanisms to handle pointer types.

- This projects involves finding what is not processed correctly within the alloc crate and fixing it as well as adding the mechanisms required to handle the Box type. It may requires mocking or modifying the core library to sidestep some current issues with it.
- We usually don't require rust experience for our GSOC projects but this one will be a lots harder if you have never written any rust code as it will require some understanding of the intricacies within the core and alloc crates.
- This is a large project.

- The rust frontend is slowly progressing toward the complete compilation of the "core" crate. The next step before compiling the standard library is the allocation library.
*Add infrastructure to handle the "Drop" trait*- The rust language heavily relies on RAII and allows custom behaviors when a data structure goes out of scope or as said more commonly is "dropped". This behavior is handled by the "Drop" trait and is not yet handled by the compiler.
- Some drop rules such as the "drop check eyepatch" with the "may_dangle" attribute are a bit tricky to get right . During the project the implementer will have to familiarize themselves with those rules to ensure drop behavior correctness.
- This can be both a medium-sized or large project.


**Extend the static analysis pass**GCC has gained an experimental[static analysis pass](https://gcc.gnu.org/wiki/StaticAnalyzer)which performs some rudimentary checking of malloc/free and the stdio FILE stream API. There is plenty of scope for extending this pass in ways that may interest a contributor, such asAdd format-string support to

`-fanalyzer`. We currently have two different implementations of warnings for format strings (e.g.`printf`) in GCC;`gcc/c-family/c-format.cc`implements`-Wformat`in the C/C++ frontends, doing type-checking on format strings against their arguments, and`gcc/gimple-ssa-sprintf.cc`implements parts of`-Wformat_overflow=`,`-Wformat_truncation=`, and`-Wrestrict`in the middle-end). Now that the analyzer has`-Wanalyzer-out-of-bounds`, it might be good to refactor and generalize this format-string parsing to share more code, and so that the analyzer can reuse it, and do similar range analysis (but with the analyzer's more precise path-sensitive interprocedural approach; see[https://gcc.gnu.org/bugzilla/show_bug.cgi?id=107017](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=107017))- Add a checker for some API or project of interest to the contributor (e.g. the Linux kernel, a POSIX API that we're not yet checking, or something else), either as a plugin, or as part of the analyzer core for e.g. POSIX.
Extending the analyzer's support for C++. See

[https://gcc.gnu.org/bugzilla/showdependencytree.cgi?id=97110](https://gcc.gnu.org/bugzilla/showdependencytree.cgi?id=97110).Extend the plugin to add checking for usage of the CPython API (e.g. reference-counting); see

[https://gcc.gnu.org/bugzilla/show_bug.cgi?id=107646](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=107646)

This project would be mentored by David Malcolm. Required skills include C/C++ and finding a way through a large code-base. Applicants should familiarize themselves with GCC's GIMPLE representation, and the

[internals of the static analyzer](/ideas/gnu-compiler-collection-gcc/onlinedocs-gccint-static-analyzer). The size of the project depends on its agreed scope, i.e. it**can be both a 175-hour (medium-sized) or a 350 hour (large) project**but it is probably easier to define a large one. Difficulty also depends on scope but is**likely to be hard**.**Ada - Compile-time data-race detection and global variable analysis**. Ada 2022 specifies a series of levels of checking for data races and global variable usage. We propose to implement the Global variable analysis specified in the Ada 2022 RM section 6.1.2, which checks that any use of global variables within a subprogram correspond to the usages specified by the "Global" aspect for the subprogram. We also propose to implement the compile-time parallel conflict checking specified in section 9.10.1 as "All_Parallel_Conflict_Checks" which verifies that a parallel construct only reads or updates global variables that are "synchronized" objects.- The expected outcome is that the compiler will recognize the Global aspect for subprograms, and detect uses of global variables that exceed the specification for a given subprogram. The compiler will recognize the Conflict_Check_Policy pragma, and will detect uses of non-synchronized global variables by parallel constructs.
This could be a

**medium or large**project (175 or 350 hours), depending on the applicant's familiarity with the GCC Ada front end (GNAT).**Medium difficulty**project, as this is only enforcing compile-time restrictions and has no effect on the generated code.- Expected Mentors: Tucker Taft and Richard Wai
- Skills required: Basic understanding of compiler front-end syntax and static semantic processing, experience with writing significant programs in Ada. Ideally, some familiarity with the GCC Ada front end (GNAT).

**Fortran – DO CONCURRENT**– see[GFortranStandards](https://gcc.gnu.org/wiki/GFortranStandards)for language links (Fortran standard and what's new documents for 2018 and 202x). Project would be (mainly) mentored by Tobias Burnus. Required skills include C/C++; some knowledge of Fortran helps, but is not needed.**Difficulty medium, size: 175 hours (medium)**- "DO CONCURRENT" is a special way to write loops such that each iteration is independent of another (except for reductions), permitting to run it concurrently.
- Goal is to execute the loops actually in parallel, namely:
- Handling do-concurrent loops in the generic OpenMP code, possibly starting without MASK support and only for those annotated by '!$omp loop'
- Extending it for MASK support / or optimizing the loop count for it.
- Handling parallelization without '!$omp loop' using the command line flag -fdo-concurrent= (like: no parallelization, OpenMP loop, etc.), "parallel" (pthread parallelization similar to (based on?) -ftree-parallelize-loops=n).

For some experiments and results, see also

[https://arxiv.org/pdf/2110.10151.pdf](https://arxiv.org/pdf/2110.10151.pdf)or experiments by other compiler vendors (search the internet)*As of Jan 2026, local/local_init for Fortran loops has some corner case issues, cf.*[PR101602](https://gcc.gnu.org/PR101602#c6); this should not affect the OpenMP implementation (unless it has the same deficits) but should eventually be fixed.

**Fortran – 2018/202x**– Several Fortran 2018 and all Fortran 202x features are unimplemented. See[GFortranStandards](https://gcc.gnu.org/wiki/GFortranStandards)for language links (Fortran standard and what's new documents for 2018 and 202x).- Project would be (mainly) mentored by Tobias Burnus - but also by those on GCC' Fortran mailing list. Required skills include C/C++; some knowledge of Fortran helps, but is not needed.
The size and difficulty of the project depends on its agreed scope, i.e. it

**can be both a 175-hour (medium-sized) or a 350 hour (large) project**,**can be both medium difficulty or hard**.Effort depends on which new feature(s) are implemented; requires some research about what's missing and about the effort. If interested, please ask via the fortran@ mailing list,

[https://gcc.gnu.org/lists.html](/ideas/gnu-compiler-collection-gcc/lists)- The "what's new in 202x" document would be a starting point.

**libgomp Optimizations for Scheduler Guided OpenMP Execution in Cloud VMs**

- While HPC deployments traditionally avoid oversubscription, there is continued interest in optimizing OpenMP execution under oversubscribed conditions. OpenMP execution in cloud VMs is commonplace, and oversubscription is a popular cost-cutting practice in cloud deployments.
This project aims to implement a solution that was recently proposed in the

*GCC (GNU Toolchain)*devroom at FOSDEM 2026:[https://fosdem.org/2026/schedule/event/3QDZQ8-scheduler-guided-openmp-execution-in-cloud-vms/](https://fosdem.org/2026/schedule/event/3QDZQ8-scheduler-guided-openmp-execution-in-cloud-vms/).

OpenMP performance inside an oversubscribed cloud VM heavily depends on barrier synchronization within the guest and on task-scheduling decisions made by the host OS. The proposed solution leverages para-virtualized task-scheduling insights to optimize the following OpenMP runtime decisions:- Degree of Parallelism (DoP) per parallel region.
- Barrier synchronization mechanism per barrier.

Implementation of a new environment variable,

`GOMP_DYNAMIC_POLICY`, which, when set to`pvsched`, adapts the DoP of each new parallel region inside the guest based on runtime conditions on the host.Addition of support for a new value,

`pvsched`, to libgomp’s implementation of the OpenMP ICV`OMP_WAIT_POLICY`, enabling the use of a para-virtualized scheduling guided barrier synchronization mechanism.- Comprehensive testsuite coverage for the newly added features.


Project Difficulty: medium

Expected Time Commitment: 350 hrs (large)

Prerequisite: A basic understanding OpenMP, Operating Systems, and Virtualization

Required skills: C Programming, Git

Mentors: Himadri CS, Tobias Burnus, Thomas Schwinge

- While HPC deployments traditionally avoid oversubscription, there is continued interest in optimizing OpenMP execution under oversubscribed conditions. OpenMP execution in cloud VMs is commonplace, and oversubscription is a popular cost-cutting practice in cloud deployments.
**Enhance OpenMP support.**OpenMP supports thread-based paralleliaztion and GPU offloading for C, C++, and Fortran.- There are several projects possible / project would be (mainly) mentored by Tobias Burnus.
In particular, adding support for some more OpenMP 6.x features. See

[https://gcc.gnu.org/projects/gomp/](/ideas/gnu-compiler-collection-gcc/projects-gomp)for general information, links and, in particular, the current status. Some random picks and notes:- Changes to related to environment variables like OMP_DEFAULT_DEVICE, OMP_AVAILABLE_DEVICES, OMP_NUM_THREADS, OMP_PLACES is a runtime-library only work in C (simpler in scope and probably had to be combined with some other smaller feature)
- Atomic changes require some parser changes (mostly Fortran, some also C/C++) - this is compiler front-end work in C-ish C++ but using the existing parser infrastructure, testcases would be in the respective language. Also smaller-in-scope feature that should to be combined with some other smaller tasks
- New loop transformation features: some front-end support, mostly early middle end code (C-ish C++). 'unroll'/'tile' are handled, 'fuse, interchange, reverse, split, stripe, flatten' are to be implemented - tricky part is to handle the corner cases. If not enough time has been burnt on this the new 'apply' clause and some other increase the required effort.
- There are plenty of other features, some tiny, some huge and the list above is a random pick. - Besides OpenMP 6.x, there is some other work useful (quality of implementation related, performance, some missing gaps, known bugs); suggestions welcome, but picking 6.x features suggested.


**Enhance OpenACC support.**[OpenACC](https://gcc.gnu.org/wiki/OpenACC)is parallel programming model for heterogeneous HPC hardware. GCC currently supports most but not all of OpenACC 2.6. The project idea here is to fill some of the gaps, for example, implement:*OpenACC*(albeit for 'init' a draft patch already exists)`init`,`shutdown`,`set`directivesThese complement the corresponding

`acc_init`etc. runtime API routines, which are already implemented.

Make the

*OpenACC*actually do something`cache`directive- It's currently only parsed, but we're not actually using it for optimization purposes: prefetch data, move data to low-latency memory.

*OpenACC*`bind`clause*OpenACC*`device_type`clause- Newer features, added after 2.6.

To work on these items, it's definitely very helpful to have available a GNU/Linux system with an AMD or Nvidia GPU supported by GCC

[Offloading](https://gcc.gnu.org/wiki/Offloading), but it's not strictly necessary. Mentors: Thomas Schwinge, Tobias Burnus. The size and difficulty of the project depends on the agreed number of items to be implemented, i.e. it**can be both a 175-hour (medium-sized) or a 350 hour (large) project**,**can be both medium difficulty or hard**.


Notes on*OpenACC*:`init`,`shutdown`,`set`directives

Certain functionality in OpenACC exists both in a directive variant and a runtime API routine variant. For example, OpenACC 2.6 has 2.16.3. "Wait Directive" (directive variant) and 3.2.11. "acc_wait" etc. (runtime API routine variants). In GCC, the front ends map the directive variant to`gcc/omp-builtins.def:BUILT_IN_GOACC_WAIT`(see`git grep --cached BUILT_IN_GOACC_WAIT\\\|c_finish_oacc_wait -- gcc/`). This eventually gets translated to a regular function call to`libgomp/oacc-async.c:GOACC_wait`, which uses the same building blocks as do`acc_wait`etc., which are also implemented in`libgomp/oacc-async.c`. (libgomp is the GCC runtime library for[OpenMP](https://gcc.gnu.org/wiki/OpenMP)originally, but then also OpenACC, implementing both the user-level OpenACC "Runtime Library Routines" and the compiler-used`GOACC_[...]`etc. routines.) Similar for`#pragma acc enter data create(var)`vs.`acc_create`, and others. Some users like to use one of directive vs. runtime API routine variants over the other; generally some prefer using the directive variants instead of C/C++`#include <openacc.h>`or Fortran`use openacc`module. Corresponding to the`acc_init`,`acc_shutdown`,`acc_set_device_num`/`acc_set_device_type`runtime API routine variants implemented in GCC, in OpenACC 2.5, "New`init`,`shutdown`,`set`directives were added", which are not yet implemented in GCC. Implementation of those is assumed to be very much similar as the OpenACC`wait`directive is via`BUILT_IN_GOACC_WAIT`, for example, so would enhance the GCC code along these lines, plus proper testsuite coverage.[Lower prio]

**Fortran – run-time argument checking.**– In particular older Fortran code, which does not use modules, but also code which uses implicit-size or explicit-size arrays is prone to argument mismatches. The goal of this item is to add an optional run-time test which works by storing the argument-type/size data before the call in a global variable – and check against it in the callee. (A pointer to the called function is stored alongside to permit calls from uninstrumented code to instrumented code.) This project would/could be mentored by Tobias Burnus. Required skills include C/C++; some knowledge of Fortran helps, but is not needed.**Difficulty medium, size: 175 hours (medium)**.[Lower prio]

**Fortran – improved argument compile-time checking**– The compiler does check for the arguments in the same file – but it could do better in some cases, i.e. checking better the interface data or updating the expected input better from the use. This project would/could be mentored by Tobias Burnus. Required skills include C/C++; some knowledge of Fortran helps, but is not needed.**Difficulty medium, size: 175 hours (medium)**.

**The expected outcome** of all projects listed above is a series of patch submissions which pass review and are included in the main GCC repository, the GCC-Rust project repository (for Rust-related projects) and/or binutils (e.g. the demangler code is shared between GCC and binutils).

Unless a project above was explicitly marked with a different difficulty, consider it to be hard. Generally speaking, GCC is a production compiler and working on one of those is always hard, especially if you are new. On the other hand, the community of GCC developers is very helpful and goes out of its way to assist newcomers with various difficulties they inevitably encounter.

If the list above was not exhaustive enough for you, you can have a look also at [Other Project Ideas](https://gcc.gnu.org/wiki/SummerOfCode#Other_Project_Ideas) section below.



## Before you apply

Applicants for a GCC Google Summer of Code project need to have experience coding in C/C++. Furthermore, if you want to work on the actual compiler you must have at least rudimentary theoretical background in the area of compilers and compiler optimizations - at the very least you need to understand the term *intermediate representation* (IR), sometimes also called *intermediate language* (IL). It also helps if you know what *static single assignment* ([SSA](https://en.wikipedia.org/wiki/Static_single-assignment_form)) form is and why it is useful. This may not be strictly necessary if your project aims to improve a different tool or library that is part of GCC, such as the demangler but even in these cases you need to know about the required algorithms.

Before you apply and even before you even reach out to us make sure that you can check out the GCC source code from its Git repository, build GCC from it and run the testsuite (this is something that would need doing very many times in the course of any project working on GCC) and look around the project a bit.

The following links should help you:

How to checkout our sources using Git is described at

[https://gcc.gnu.org/git.html](/ideas/gnu-compiler-collection-gcc/git).Steps linked from

[https://gcc.gnu.org/install/](/ideas/gnu-compiler-collection-gcc/install)show you how to configure, build and test GCC (look for`--disable-bootstrap`, among other things). The[Installing GCC](https://gcc.gnu.org/wiki/InstallingGCC)page shows an easy way to obtain the libraries required to build GCC which people often find most problematic and other advice related to building and installing GCC for the first time.Read through David Malcolm's guide

[GCC for New Contributors](https://gcc-newbies-guide.readthedocs.io/en/latest/). David has also presented a[talk about this topic at FOSDEM'24](https://fosdem.org/2024/schedule/event/fosdem-2024-2569-gcc-for-new-contributors/), you can watch the recording. You can also check out[Getting Started](https://gcc.gnu.org/wiki/GettingStarted)wiki page.Wiki page

[DebuggingGCC](https://gcc.gnu.org/wiki/DebuggingGCC)and the manual page about[Developer options](/ideas/gnu-compiler-collection-gcc/onlinedocs-gcc-developer-options)are of particular interest. Read through those, compile a simple but non-trivial program with

-O3 -S -fdump-tree-all -fdump-ipa-all -fdump-rtl-all

and look through the generated files. Look at the the source code, especially in the

`gcc`subdirectory and try to set a breakpoint somewhere and hit it. Then look around in gdb.

- If you plan to work on the Ada front-end, we recommend studying the following:
- Documentation of the GCC Ada front end (GNAT) which is included within the Ada source code for critical packages.
- The Ada 2022 Reference Manual.
- The textbook "Programming in Ada 2022" (John Barnes).
- A compiler textbook with good coverage of compiler front end structure, such as Appel's "Modern Compiler Implementation".

If you intend to work in the area of

*Link Time Optimization*(LTO), the following two videos may help you understand the required concepts:If your selected project involves

*Offloading*, you almost certainly want to familiarize yourself with the concept which is described[on its own wiki page](https://gcc.gnu.org/wiki/Offloading). You probably want to look at it also if you plan to work in the are of*OpenACC*or (to a lesser extent)*OpenMP*.If your selected project is in the area of the

*static analyzer*, some notes specifically about the analyzer's internals and debugging it can be seen here:

If you have done all of the above, or at least most of it, and still find it all a little bit intimidating, do not despair. If you are facing any specific technical problem or if you have difficulties figuring out where to start looking for particular things, that is something the mentors and the community at large are willing to help you with. First, the mailing list you keep reading about here has an [archive](/ideas/gnu-compiler-collection-gcc/pipermail-gcc), it is always a good idea to check if some other GSoC applicant has not asked your question recently. If not, send an email describing your situation to the [mailing list](/ideas/gnu-compiler-collection-gcc/mailman-listinfo-gcc) yourself. We will appreciate if in your email you will make it clear that you have read this section and briefly list the steps above you have managed to carry out successfully.


## Legal requirements

Any non-trivial contributions to GCC are accepted only if their author either formally assign their copyright for them to the Free Software Foundation or if the author certifies the "Developer Certificate of Origin" (DCO) by adding the Signed-off-by: tag to their submission. Both processes are described in the official page on [Contributing to GCC](/ideas/gnu-compiler-collection-gcc/contribute). Accepted GSoC contributors will be expected to choose one and follow it.


## Use of AI

With the exception of test cases, you may not include any non-trivial (more than de-minimus) amount of code generated by a Large Language Model (an "AI" such as ChatGPT, Gemini, and Copilot) in code that you submit as a participant of GCC GSoC.

Applications which look like that they have been generated by a Large Language Model will be quickly disregarded too, they will never give us the confidence that the applicant can finish the project. GCC contributors are used to working with non-native English speakers, in fact English is a foreign language for many of us, so do not be afraid of that.


## Application

First, you need to select a project. If you have been following GCC development, you might have an idea of your own, otherwise look at the suggested projects above and try to pick one there. In the course of selecting a project or when researching it in order to write your application, do not hesitate to ask questions or request more details from the community by email to the [gcc@gcc.gnu.org](mailto:gcc@gcc.gnu.org) [mailing list](/ideas/gnu-compiler-collection-gcc/mailman-listinfo-gcc) with the string "GSoC" in the email subject or on our #gcc [IRC](https://gcc.gnu.org/wiki/GCConIRC) channel at irc.oftc.net. Please note that the mailing list does not accept HTML messages, you must set your email client to plain text. If you are interested in gcc-rust topics, you can also reach out to the community via [Zulip](https://gcc-rust.zulipchat.com/).

When you have a draft of your proposal ready, send it to the [gcc@gcc.gnu.org](mailto:gcc@gcc.gnu.org) [mailing list](/ideas/gnu-compiler-collection-gcc/mailman-listinfo-gcc) as a request for comments. First, it should help you come up with a much better final proposal. Second, when evaluating applicants, we look closely at how they responded to feedback and how they incorporated it in their application document. We are unlikely to accept an application from someone who has not interacted with the community before at all. Please remember to put the string "GSoC" in the email subject of all messages about GSoC or a GSoC project proposal.


### Formal application document

GCC does not have any application form or a mandatory application format to follow, but we strongly suggest you include the following in the formal application document that you submit to GSoC:

- Describe the project and clearly define its goals.
- If you chose a project that is not among the "selected project ideas," describe why it is a worthwhile effort.
- Provide an expected time-line. We understand it is likely to change, that is not the point. Instead we want to know that you have a reasonable idea about project milestones. Moreover, org-admins will pay close attention to your plan for the first and second week of the coding period. If you intend to do general research how to "do stuff" only then, it likely means that you do not understand the actual technical issues and that you should do some of the research before applying. On the other hand, researching specific topics is probably fine, some semi-independent researching throughout the project is actually expected.
- Briefly introduce yourself and your skills and/or accomplishments. We would like to be sure you have the knowledge and skills to complete the project - but we will evaluate this also from how you have interacted with us in the preparation phase.


### Further tips and guidelines

- Be honest and realistic. We prefer a smaller project with clearly defined goals to a far-reaching but vague proposal (that is likely never going to be finished by the contributor).
- Applicants that have already submitted good patches give a much better impression to reviewers and potential mentors.
Starting with some small patch for the area you are interested in before the proposal submittal period can help (ask for guidance and a simple enough project): It helps you to get the code known and to decide whether you really want to do the project, it shows how the development procedure is, and helps potential mentors to judge the proposal based on actual work. Besides: Also small fixes are good and getting people known by email (or IRC) exchange is nice by itself

And let's stress again that you need to present your project on the

[gcc@gcc.gnu.org](mailto:gcc@gcc.gnu.org)[mailing list](/ideas/gnu-compiler-collection-gcc/mailman-listinfo-gcc)because there is likely going to be a feedback that you should incorporate. Put "GSoC" somewhere into the email subject.



## Other Project Ideas

Note that some of the ideas found below might be fully or partially obsolete. This is another reason why it is always a good idea to discuss the project of interest on the [mailing list](/ideas/gnu-compiler-collection-gcc/mailman-listinfo-gcc) and/or via [IRC](https://gcc.gnu.org/wiki/GCConIRC) before submitting a GSoC proposal.


### Link-time and interprocedural optimization improvements

Link-time optimization (LTO) is powerful infrastructure in GCC and there are many areas how to make it better, for example:

- Implement tree level section anchors to improve code generation at ARM/PPC.


### Language front-ends and run-time libraries

[Fortran](https://gcc.gnu.org/wiki/GFortran)front end (please discuss ideas on the[Fortran mailing list](mailto:fortran@gcc.gnu.org)):Extend

[OOP](https://gcc.gnu.org/wiki/OOP)support (possible mentors: Janus Weil, Tobias Burnus) by improving partially-implemented features, such as:- Associate construct

[coarray](http://users.physik.fu-berlin.de/~tburnus/coarray/README.txt)support for SMP and distributed memory systems (possible mentor: Tobias Burnus)[Coarrays](https://gcc.gnu.org/wiki/Coarray)are a PGAS extension, which is part of Fortran 2008.- There has been some work on this by Thomas/Nicolas König in GIT branch devel/gfortran-caf; unclear status.
**Fortran – shared-memory coarrays***NOTE: Partial implementation available in devel/coarray_native branch, if interested, ask about remaining tasks in this area*–[Coarrays](https://gcc.gnu.org/wiki/Coarray)are a means of parallelizing code; conceptually, all memory is local memory, except for coarrays which are on multiple processes ("images") and remote can be directly accessed. (Internally: one-sided communication.) GCC/gfortran supports "single" (compiles but does not do any actual parallelization) and "lib" (requires a communication library). The goal of this task is to add a shared-memory implementation – such that parallel coarray programs runs out of the box without additional external libraries. This project would be mentored by Tobias Burnus. This project consists of work mostly on a run-time library written in C but also on the compiler itself written in C/C++. Hence, required skills include C/C++, knowledge about POSIX Threads; some knowledge of Fortran helps, but is not needed.Possible task: Improving the multi-image support, which uses

[OpenCoarray](https://gcc.gnu.org/wiki/OpenCoarray)[communication library](https://gcc.gnu.org/wiki/CoarrayLib)- Implement Fortran 2018 additions (TS18508) additions

- Run-time argument checking: Uninitialized variables, correctness of arguments
- Improve handling of allocatable characters
- Improve parameterized derived types (possible sponsor: Paul Thomas)
- Better IEEE support
Other

[Unimplemented Fortran 2003](https://gcc.gnu.org/wiki/Fortran2003Status),[Fortran 2008 features](https://gcc.gnu.org/wiki/Fortran2008Status),[TS 29113 features](https://gcc.gnu.org/wiki/TS29113Status)- IO optimization. Currently formatted scalar IO is quite slow and uses lots of stack space.

OpenMP runtime improvements:

[openmp](https://gcc.gnu.org/wiki/openmp)Enhance the

[GimpleFrontEnd](https://gcc.gnu.org/wiki/GimpleFrontEnd)with CFG and SSA annotation reconstruction to make writing and extracting unit-tests easier.


### New optimization passes

- Implement code motion of stores towards entry (and use this to improve code for int to float conversion on rs6000-based targets)
Loop optimizations and automatic parallelization based on

[Graphite](https://gcc.gnu.org/wiki/Graphite)- Implement a basic-block local scheduling pass to improve SSA name coalescing opportunities at RTL expansion time
Implement a (prototype) addressing mode selection (AMS) pass as a replacement of auto-inc-dec. For more details see

[PR 56590](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=56590).


### Other projects and project ideas

Make cp-demangle non-recursive. C++ mangled names use a recursive grammar, and naturally led to a recursive demangler in libibiberty (used for

`__cxa_demangle`and other entry points). Very long symbols and malformed inputs can cause deep recursion (even unbounded in the malformed case). Stack overflow is unpredictable and has terrible failure modes, which has led to imposing arbitrary recursion limits in the demangler. The demangler should be converted to use a bespoke heap-allocated data stack for the recursive state, and the implicit recursion removed. Resource allocation failure can be indicated via the existing failure code. The demangler is implemented in C, the project entails turning implicit recursion into an explicit ne driven by a LIFO worklist - clear understanding of what that means and good command of C is required. You will also learn about C++ mangled names.**175 hour (medium-sized)**project.Type Sanitizer. Both LLVM and GCC compilers do share a common sanitizer library called libsanitizer. The library has recently received support of typed-based sanitization (

[TySan](https://gcc.gnu.org/wiki/TySan)). Goal of the task would be to investigate and prototype usage of type-based aliasing rules information provided by GCC in order to detect violations of strict aliasing rules.Replace

[libiberty](/ideas/gnu-compiler-collection-gcc/onlinedocs-libiberty)with[gnulib](http://www.gnu.org/software/gnulib/). See[http://gcc.gnu.org/ml/gcc-patches/2012-08/msg00362.html](/ideas/gnu-compiler-collection-gcc/ml-gcc-patches-2012-08-msg00362)Initial work was done in GSoC 2016 ([replacelibibertywithgnulib](https://gcc.gnu.org/wiki/replacelibibertywithgnulib)).Finish the

[implementation of a stable introspection plugin API](/ideas/gnu-compiler-collection-gcc/ml-gcc-2012-09-msg00074)(with the possibility of extending it to cover non-introspection cases)- Modify any GCC optimization decisions externally through plugins (see MILEPOST GCC, for example). -- G. Fursin, 2014.
- Systematize learning of optimal optimization decisions for multiple benchmarks, data sets and architectures (see c-mind.org/repo, for example). -- G. Fursin, 2014.
- Extend GCC plugin framework to enable code instrumentation (insert calls to external function after individual instructions) for dynamic code analysis. We need it to extend our TM/TLS models. -- G. Fursin, 2014.
- Fix -ftrapv so that it works.
- Improve the regression testing system, for example to detect places where the generated code changed (useful for refactoring).
Promote C++ operator new to

`alloca`when pointer does not escape and user allows non-conformance to C++ standard- Improve loop unrolling heuristics and enable loop unrolling with default optimization
- Analyze and improve inlining, loop unrolling, reassociation and predictive commoning heuristics for PowerPC architecture
- Use TARGET_EXPAND_TO_RTL_HOOK for pipelined divide on PowerPC
- Support AIX XCOFF file format for LTO (David Edelsohn)
Implement something similar to Clang's

*-ftime-trace*feature which generates performance reports that show where the compiler spends compile time. For more information, please check the following[blog post](https://aras-p.info/blog/2019/01/16/time-trace-timeline-flame-chart-profiler-for-Clang/). There's also an existing[bugzilla entry for this](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=92396)(if this becomes a GSoC project, the assignee will of course change). Required skills include C/C++ and finding a way through a large code-base.

There are several pages with general ideas for GCC, many of which we linked below for easy access. These ideas usually are not just one project but a group of distinct projects.

- This category of projects deals with a range of changes, from simple to challenging. These projects are of great interest to us, because they address some long-standing architectural issues that we want to fix.

Other project ideas can be found in the

[bug database](http://gcc.gnu.org/bugzilla/), look for old bugs which are still open.

**Or invent your own project.** We're always open to good ideas. But note that we are probably not too interested in projects to add new extensions to the C or C++ languages. We've found over time that these tend to introduce more problems than they solve.

Thanks, and we look forward to your submissions!


### Improving GCC Developer Documentation

**The rules of the GSoC program do not allow projects to consist of documentation improvements only.** Nevertheless, note that writing documentation may be an important part of your project or even an essential one if you introduce user-visible changes and plan your work accordingly.



## Accepted GCC Projects


### 2025

|
|
|
Fortran - 2018/202x |
Yuao Ma |
Tobias Burnus |
Implementing Parallel Features on the GCC Ada Frontend |
Ethan Luis McDonough |
Tucker Taft, Richard Wai |
Rewrite Rust lints to operate on frontend's HIR |
Ryutaro Okada |
Arthur Cohen, Pierre-Emmanuel Patry |
gccrs: Improving match expressions & pattern matching |
Zhi Heng |
Arthur Cohen, Pierre-Emmanuel Patry |
Implementation of a simple in-memory file system for running offloading tests on NVIDIA GPUs |
Arijit Kumar Das |
Thomas Schwinge, Tobias Burnus |
Tooling for running BPF GCC tests on a live kernel |
Piyush Raj |
Jose E. Marchesi, David Faust, Thomas Schwinge |


### 2024

|
|
|
gccrs - Inline Assembly Support |
jjasmine |
Arthur Cohen, Pierre-Emmanuel Patry |
Fortran – DO CONCURRENT |
Anuj Mohite |
Tobias Burnus, Thomas Schwinge |
Offloading to a separate process on the same host |
Georgii Burunsuzian |
Thomas Schwinge, Tobias Burnus |
Borrow-checking IR location support |
Kushal Pal |
Arthur Cohen, Pierre-Emmanuel Patry |
Rustc Testsuite Adapter for GCCRS |
Muhammad Mahad |
Thomas Schwinge, Arthur Cohen, Pierre-Emmanuel Patry |
Improve nothrow detection in GCC |
Pranil Dey |
Martin Jambor, Jan Hubicka |
Structured Dumping of GENERIC Trees |
Thor Preimesberger |
Richard Biener |


### 2023

|
|
|
Improving user errors & Error Code Support for GCC Rust Frontend |
Muhammad Mahad |
Philip Herron and Arthur Cohen |
Unicode Support for GCC Rust Frontend |
Raiki Tamura |
Philip Herron and Arthur Cohen |
Extending gcc -fanalyzer C++ support for self-analysis |
Benjamin Priour |
David Malcolm |
GCC static analyzer plugin for CPython extension modules |
Eric Feng |
David Malcolm |
Bypass assembler when generating LTO object files |
Rishi Raj |
Martin Jambor and Jan Hubicka |
|
Ken Matsui |
Patrick Palka |


### 2022

|
|
|
Faisal Abbas |
Philip Herron |
|
|
Immad Mir |
David Malcolm |
Improving Rust debugging experience by enhancing the HIR dump |
Andrew Naguib |
Arthur Cohen and Philip Herron |
Bypass assembler when generating LTO object files |
Nitin Kumar |
Jan Hubička and Martin Jambor |
Tim Lange |
David Malcolm |
|
Accelerating Fortran DOCONCURRENT |
Wileam Phan |
Tobias Burnus and Thomas Schwinge |


### 2021

|
|
|
Ankur Saini |
David Malcolm |
|
Arthur Cohen |
Philip Herron |
|
Wenzhang Yang |
Philip Herron |
|
Make Cp-demangler non recursive |
Vishnu Madhav |
Nathan Sidwell and Martin Jambor |


### 2020

|
|
|
Giuliano Belinassi |
Richard Biener |
|
John Ravi |
Martin Liška and Nathan Sidwell |
|
Implementation of OMPD in GCC and libgomp |
Tony Sim |
Jakub Jelínek and Martin Jambor |


### 2019

|
|
|
|
ThePhD |
Thomas Rodgers, Jonathan Wakely and Ville Voutilainen |
Tejas Joshi |
Martin Jambor and Jan Hubička |
|
Shubham Narlawar |
Martin Liška and Andi Kleen |
|
Khurai Kim |
Jakub Jelínek |
|
|
akshatg |
Paul E. |
|
Giuliano Belinassi |
Richard Biener |


### 2018

|
|
|
Hrishikesh Kulkarni |
Martin Liška and Jan Hubička |


### 2016

|
|
|
Ayush Goel |
Manuel Lopez-Ibanez |
|
Prasad Ghangal |
Richard Biener |
|
erikvarga |
Oleg Endo |


### 2015

|
|
|
|
Fan You |
Tim Shen |
Erik Krisztian Varga |
Oleg Endo |


### 2014

|
|
|
Coarray support in GNU GFortran |
Alessandro Fanfarillo |
Tobias Burnus |
Concepts Separate Checking |
Braden Obrzut |
Andrew Sutton |
Integration of ISL code generator into Graphite |
Roman Gareev |
Tobias Grosser |
Generating folding patterns from meta description |
Prathamesh Kulkarni |
Richard Biener |
GCC Go escape analysis |
Ray Li |
Ian Lance Taylor |


### 2013

|
|
|
Fotis Koutoulakis |
Thomas Schwinge |
|
Martin Liška |
Jan Hubicka |
|
Tim Shen |
Stephen M. Webb |


### 2012

|
|
|
Dimitrios Apostolou |
Andrey Belevantsev |
|
Morgen Matvey |
Benjamin De Kosnik |
|
|
Sandeep Soni |
Diego Novillo |
Sergey Lega |
Benjamin De Kosnik |


### 2011

|
|
|
|
Daniel Carrera |
Tobias Burnus |
|
Dimitrios Apostolou |
Steven Bosscher |
|
Ismail KURU |
Richard Henderson |
Ketaki |
Diego Novillo |
|
Philip Herron |
Ian Lance Taylor |
|
Piervit |
Basile Starynkevitch |
|
Sho Nakatani (中谷 翔) |
Jakub Jelínek |


### 2010

The source code for finished projects can be found at [Google's code hosting site](http://code.google.com/p/google-summer-of-code-2010-gcc/downloads/list) and their respective SVN branches.

|
|
|
Yi-Hong Lu |
H. J. Lu |
|
Sandeep Soni |
Diego Novillo |
|
Artjoms Sinkarovs |
Richard Günther |
|
Philip Herron |
Ian Taylor |
|
|
Vladimir Kargov |
Sebastian Pop |
Ankur Deshwal |
David Edelsohn |
|
|
Sebastian Pop |
|
Andreas Simbuerger |
Tobias Grosser |
|
Tobias Burnus |
||
|
Daniel Kraft |
Tobias Burnus |


### 2009

The source code for finished projects can be found at [Google's code hosting site](https://code.google.com/archive/p/google-summer-of-code-2009-gcc/downloads).

|
|
|
Li Feng |
Tobias Grosser |
|
Enable generic function cloning and program instrumentation in GCC to be able to create static binaries adaptable to varying program and system behavior or different architectures at run-time |
Liang Peng |
Grigori Fursin |
gfortran: |
Tobias Burnus |
|
Traditional Loop Transformations |
pranav garg |
Sebastian Pop |
Make the OpenCL Platform Layer API and Runtime API for the Cell Processor and CPUs |
phil prattszeliga |
Paolo Bonzini |
Provide fine-grain optimization selection and tuning abilities in GCC to be able to tune default optimization heuristic of the compiler or fine optimizations for a given program on a given architecture entirely automatically using statistical and machine learning techniques from the MILEPOST project. |
Yuanjie Huang |
Grigori Fursin |


### 2008

The source code for finished projects can be found at [Google's code hosting site](https://code.google.com/archive/p/google-summer-of-code-2008-gcc/downloads).

|
|
|
Steven Bosscher |
||
Improving Dead Store Elimination |
Jakub Staszak |
|
Extend Fortran 2003 support for gfortran |
Daniel Kraft |
François-Xavier Coudert |
C++0x lambda functions for GCC |
John Freeman |
|
Tobias Grosser |
||
Finish work on propagation aliasing and array dependence information from Tree-SSA to RTL. |
Alexander Monakov |
Diego Novillo |
Tobias Burnus |


### 2007

The source code for finished projects can be found at [Google's code hosting site](https://code.google.com/archive/p/google-summer-of-code-2007-gcc/downloads).

|
|
|
Propagating array data dependence information from Tree-SSA to RTL |
Alexander Monakov |
Daniel Berlin |
Manuel López-Ibáñez |
Diego Novillo |
|
Speeding up GCC for fun and profit |
James Webber |
Eric Marshall Christopher |
Steven Bosscher |
||
Open Mutliprogramming Interprocedural Analasis and Optimalizations |
Jakub Staszak |
Daniel Berlin |
Integrating OpenJDK's javac bytecode compiler into gcj |
Dalibor Topic |
Mark J. Wielaard |
New static scheduling heuristic for GCC |
Dmitry Zhurikhin |
Vladimir Makarov |
GCC support for Windows-compatible Structured Exception Handling (SEH) on the i386 platform |
Michele Cicciotti |
Ian Lance Taylor |


### 2006

|
|
|
Code parallelization using polyhedral model |
Plesco Alexandru |
Daniel Berlin |
Paul Biggar |
Daniel Berlin |
|
Laurynas Biveinis |
Daniel Berlin |
|
java.lang.management in Classpath |
Andrew John Hughes |
Mark Wielaard |
Lock free C++ containers |
Phillip Jordan |
Benjamin Kosnik |
Manuel López-Ibáñez |
Ian Lance Taylor |
