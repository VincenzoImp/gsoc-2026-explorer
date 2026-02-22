# AFLplusplus — Project Ideas

**Source:** https://github.com/AFLplusplus/LibAFL/issues/3706
**Scraped:** 2026-02-22T23:28:47.605447

---

-
-
[Notifications](https://github.com/login?return_to=%2FAFLplusplus%2FLibAFL)You must be signed in to change notification settings -
[Fork 450](https://github.com/login?return_to=%2FAFLplusplus%2FLibAFL)

[GSoCGoogle Summer of Code](/ideas/aflplusplus/aflplusplus-libafl-issues)Google Summer of Code

## Description

Welcome to our Google Summer of Code idea list for 2026!

Our projects are technical, demanding, and meant for students who genuinely want to learn by doing. We value careful thinking, solid fundamentals, and the ability to work independently more than flashy output. Quality matters here. If we’re not confident a collaboration will work well, we prefer not to take a student at all.

Before applying, take time to understand the project space. Read existing documentation and code, experiment locally, and ask precise, well-researched questions. Early pull requests, small but thoughtful, are strongly encouraged and are the best way to demonstrate seriousness and technical fit.

We do not accept AI-generated, low-effort proposals or submissions. If you use tools, you are still fully responsible for understanding and defending every line of what you submit.

If this sounds like the kind of environment you want to grow in, join the fuzzing Discord, introduce yourself, and start engaging early. The strongest applications usually come from students who do exactly that.

Below you find a list of potential projects, but you can come up with your own!

## Activity

# Proposal 1: Improving LibAFL QEMU Bridging with AFL++

LibAFL QEMU is a library enabling binary-only fuzzing leveraging LibAFL and QEMU within the same process.

This approach reduces context-switching overhead and improves flexibility through a modular design.

We introduced a pull request ([#3114](https://github.com/AFLplusplus/LibAFL/pull/3114)) that adds full compatibility with AFL++, utilizing the forkserver protocol and re-implementing critical optimizations from [qemuafl](https://github.com/AFLplusplus/qemuafl), such as translation block caching.

### Project goals

The main goal of this project would be to turn this prototype into a full-fledged fuzzer capable of replacing `qemuafl`

.

The contributor will:

- Ensure the tool can be used interchangeably with
`qemuafl`

in AFL++ by creating various tests. - Design and implement benchmarks to properly compare the prototype against
`qemuafl`

performance-wise. - Identify possible bottlenecks that are not present in
`qemuafl`

, and propose solutions to resolve them.

### Required skills

- Proficiency with C and Rust.
- Strong OS knowledge (Linux, memory management, low-level programming).
- Experience with fuzzers like LibAFL, AFL++, or libfuzzer

### Preferred skills

- Familiarity with the QEMU codebase.
- Knowledge of AFL++ and LibAFL internals.
- Prior experience with performance and debugging tooling (perf, gdb, etc.).

### Difficulty Rating

The overall difficulty of this project is expected to be **medium**.

### Possible mentors

### Expected size of the project

The project is expected to take either 175 or 350 hours.

# Proposal 2: Add Ijon support to LibAFL

In AFL++, we [recently merged Ijon](https://github.com/AFLplusplus/AFLplusplus/pull/2540) support.

The feature is not supported in LibAFL yet.

### Project goals

We can probably do multiple things here

- P0: Add support for targets with Ijon support into the LibAFL forkserver
- P1: Implement Ijon into LibAFL properly (for InProcessExecutor).

For a proper Ijon implementation, we can add custom observers and feedback, to implement [the ideas of the paper](https://wcventure.github.io/FuzzingPaper/Paper/SP20_IJON.pdf).

The contributor will:

- Dig deep into the inner workings of the forkserver
- Understand the paper background
- Implement it all in LibAFL, including example fuzzers in ./fuzzers.

### Required skills

- Strong Rust skills
- Experience with fuzzers like LibAFL, AFL++, ...

### Preferred Skills

- A strong background in fuzzing research
- Prior knowledge of LibAFL internals.

# Proposal 3: Network Emulation for LibAFL_QEMU

Implement syscall emulation for filesystems and network in libafl_qemu.

### Description

The student must implement something similar to [preeny](https://github.com/zardus/preeny) and [FitM](https://github.com/fgsect/FitM) to hook the network API and an emulator filesystem that can be snapshot-restored always hooking the syscall in libafl_qemu user mode

### Expected Outcomes

A working network emulation layer for LibAFL_QEMU

### Required Skills

- Good understanding of Rust, C, and system programming
- Ideally: prior knowledge in emulators and fuzzing

### Difficulty Rating

The overall difficulty of this project is expected to be **medium**.

### Possible mentors

### Expected size of the project

The project is expected to take either 175 or 350 hours, depending on the details

# Proposal 4: Remote Worker Stage

Mutations and execution of a `Stage`

is always on the machine LibAFL runs at. For very slow targets, it may be beneficial to offload the actual executions to a stateless worker.

### Description

We could add a `RemoteWorkerLauncherStage`

that builds `n`

work packages, each including a next scheduled corpus entry, all metadata for this Testcase, the current feedback state, as well as additional random corpus entries for splicing.

The work package should then be posted to Redis or some other queue db (very much like celery, whatever a rust alternative is).

After the execution, the results should be collected in an extra stage

### Expected Outcome:

The implementation and a set of working examples, including:

LibAFL Workers / RemoteWorkerLauncherStage + RemoteWorkerCollectorStage

### Required Skills

- Rust
- Prior knowledge in distributed computing and/or fuzzing are a plus

### Difficulty Rating

easy to medium

### Possible mentors

### Expected size of the project

175 hours

# Proposal 5: Reimplement Frida-ASAN using the new librasan infrastructure

Currently we have two implementations of ASAN, one in frida-mode and one in librasan.

### Description

librasan is a new framework for building ASAN implementations, developed initially for various QEMU ASAN use cases. It is built to be modular and extensible.

Frida-ASAN is an implementation of ASAN for frida-mode.

There are numerous overlaps between these two implementations, and we would like to merge them, in as much as that is possible, by reimplementing Frida-ASAN in terms of librasan.

### Expected Outcome:

A new implementation of Frida-ASAN using librasan, with duplicate code and functionality removed, and a set of unit and integration tests which verify that the implementation is correct.

### Required Skills

- Rust
- C and systems programming
- Prior experience in frida usage (including Stalker) an advantage.
- Prior experience in allocator development an advantage.

### Difficulty Rating

medium

### Possible mentors

### Expected size of the project

175 or 350 hours

on Feb 3, 2026

early pull requests should demonstrate technical skills and ability to solve real problems, not documentation fixes or typo corrections or etc..

Early pull requests should not include AI-generated code, which we clearly stated in: [https://github.com/AFLplusplus/LibAFL/blob/main/CONTRIBUTING.md](/ideas/aflplusplus/aflplusplus-libafl-blob-main-contributing)

We want to see how well *you* understand the codebase and how well *you* can solve the problems with your code;

NOT how well you can ask *your chatbot* to solve the problem

## Metadata

## Metadata

### Assignees

### Labels

[GSoCGoogle Summer of Code](/ideas/aflplusplus/aflplusplus-libafl-issues)Google Summer of Code
