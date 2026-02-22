# Neovim — Project Ideas

**Source:** https://github.com/neovim/neovim/wiki/Google-Summer-of-Code
**Scraped:** 2026-02-22T23:28:47.615798

---

# Introduction

Neovim is a text editor based on Vim. One of the main [project goals](https://neovim.io/charter/) is to encourage hacking and collaboration.

- Project proposals for [Google Summer of Code](https://summerofcode.withgoogle.com/) are tracked as [discussions](/ideas/neovim/neovim-neovim-discussions).
- These projects may require familiarity with C, Lua, and Vimscript.
- Documentation for Neovim developers is here: https://neovim.io/doc/user/dev.html

The Neovim source has roots going back to 1987 which means libraries such as [libuv](https://github.com/libuv/libuv) were not around at that time. The codebase can be made easier to maintain and understand by using these libraries. Project ideas that heavily involve "internals" will in general be more difficult than project ideas that add new features. However working with older/complex parts of the code base can also provide valuable learning feedback for writing simpler and more maintainable code.

# Getting started

Proposals (and the final "work submission") are tracked as [discussions with the "gsoc" label](/ideas/neovim/neovim-neovim-discussions). We are happy to hear other ideas you may have, just [create a new discussion](/ideas/neovim/neovim-neovim-discussions-new) and mention that it's for GSoC. Because communication is a big part of open source development you are expected to get in touch with us before sending your proposal, see [Where to ask questions](#where-to-ask-questions).

To get familiar with the project, 

- read [CONTRIBUTING.md](/ideas/neovim/neovim-neovim-blob-master-contributing)
- try a small coding task (choose from [complexity:low](/ideas/neovim/neovim-neovim-issues) issues)
    - working on concrete tasks in the existing codebase, even if the tasks are unrelated to your proposal, gives us a valuable signal about your work style and communication. This is a key component of a successful proposal.

To get familiar with GSoC, read their materials. Especially:

- https://google.github.io/gsocguides/student/
- https://summerofcode.withgoogle.com/rules

Note: this year we will likely accept 1-2 students. We expect to get more strong proposals than available slots, so we will need to turn some good proposals down.

## AI-assisted work

AI-assisted work is fine, but:

- We cannot spend our time reviewing your AI output; it is *your* responsibility to review the AI output before asking *humans* to review it.
- You are expected to distill the AI output into its essentials, reducing verbosity and removing "slop" such as irrelevant markdown files, misplaced or redundant tests, etc.
- You are expected to ensure that the AI solution makes sense in the context of the Neovim codebase, and that it follows documented conventions and patterns.

**We will close AI-assisted PRs that are overly verbose or include AI-generated slop.**

## Tips

- Anywhere a Vim concept (such as "textlock") is mentioned, you can find what it means by using the `:help` command in Nvim (`:help textlock`).
- Ask questions and post your partial work frequently (every 1-2 days, if possible). It's OK if work is messy; just mark the pull request (PR) as "Draft".
- Take advantage of the continuous integration (CI) systems which automatically run against your pull requests. When you send work to a PR, the full test-suite runs on the PR while you continue to work locally.
- Only a text editor, `cmake`, and a compiler are needed to develop Neovim. LSP is very helpful also.
- See `:help dev-tools` and [CONTRIBUTING.md](/ideas/neovim/neovim-neovim-blob-master-contributing) for documentation on building, debugging, and development tips.

## Where to ask questions

Ask questions here:

- https://github.com/neovim/neovim/discussions
- https://matrix.to/#/#neovim:matrix.org

Do *not* ask general GSoC questions on [the issue tracker](/ideas/neovim/neovim-neovim-issues-2); use [discussions](/ideas/neovim/neovim-neovim-discussions-2) for that. **Do not ask "where do I start?"** on the issue tracker. *Do* comment on related issues to ask specific technical questions about an issue. If your question is not specific to an issue, open a [discussion](/ideas/neovim/neovim-neovim-discussions-2).

# Making a proposal

The application period for GSOC is March 16-31 ([Timeline](https://developers.google.com/open-source/gsoc/timeline)). Send your proposal through the [GSOC page](https://summerofcode.withgoogle.com/programs/2026/organizations/neovim). We encourage students to send a first draft early in this period, this allows us to give feedback and and ask for more information if need.

- ["Writing a proposal" guidelines](https://google.github.io/gsocguides/student/writing-a-proposal)
- [Proposal evaluation criteria](http://intermine.org/internships/guidance/grading-criteria-2019/)

## Tips for a successful application

A **successful proposal** will have the following:

- Start by describing the problem briefly.
- The rest of the proposal should give confidence that it can actually be done. 
    - Concrete description of the technical approach, and implementation (code), increases confidence that the proposal is feasible in the timeline and the contributor is capable of delivering it.
- Minimal verbosity/buzzwords. Vague descriptions lower confidence.
- Appendix that links to:
    1. Draft PR (or code pasted into the proposal) that shows how your idea is feasible, in code.
    2. Neovim PR(s) that you worked on. This is the main way to demonstrate your approach to understanding the codebase and executing real work. Working on concrete tasks in the existing codebase, even if the tasks are unrelated to your proposal, gives us an important signal about your work style and communication. This is a key component of a successful proposal.

Below are some suggested issues. These are starting points. If you have a great idea, propose it!

# GSoC Ideas 2026

## Proposals are [tracked as discussions](/ideas/neovim/neovim-neovim-discussions-2)

Proposals are tracked as [discussions](/ideas/neovim/neovim-neovim-discussions-2) which implement features [tracked as issues](/ideas/neovim/neovim-neovim-labels-gsoc).

1. Choose an [existing issue](/ideas/neovim/neovim-neovim-labels-gsoc), or [create a new issue](/ideas/neovim/neovim-neovim-issues-new) to outline a feature/project proposal.
    - Your proposal and work will not be discussed on the issue itself. Use discussions for that.
2. Create a [discussion](/ideas/neovim/neovim-neovim-discussions-2) to ask questions, talk about your idea(s), and (later) discuss your progress.

Below are some suggested issues. These are starting points. Your proposal should start with (1) a "Problem" section that describes the problem being solved, followed by (2) your proposed solution to the problem, including implementation details and constraints.

## Multibuffer: many buffers stitched together as one virtual buffer

- Size: 350 hours
- Difficulty: Hard
- Desirable Skills:
    - C
    - Lua
- Code license: Apache 2.0
- Mentor: TBD
- Tracking issue: https://github.com/neovim/neovim/issues/30463

**Description:**

todo

**Expected Result:**

todo

## Run Neovim in a web browser

- Size: 350 hours
- Difficulty: Hard
- Desirable Skills:
    - C
    - javascript/wasm
- Code license: Apache 2.0
- Mentor: TBD
- Tracking issue: https://github.com/neovim/neovim/issues/35567

**Description:**

todo

**Expected Result:**

- Build system has a task which compiles Nvim to javascript or webassembly and runs fully in-browser
- The task runs in CI and produces a usable artifact.

## Restore `:terminal` buffers after restart

- Size: 175 hours
- Difficulty: Medium
- Desirable Skills:
    - Lua
    - C (minimal)
- Code license: Apache 2.0
- Mentor: Justin M. Keyes ([@justinmk](http://github.com/justinmk))
- Tracking issue: https://github.com/neovim/neovim/issues/28297

**Description:**

Currently, the contents of `:terminal` buffers isn't preserved after Nvim restarts. Or when a `:terminal` buffer is closed, its contents can't be reloaded.

**Expected Result:**

- `:terminal` buffer contents can be saved to the filesystem.
- User has a way to view saved terminal buffers and reload them.
- Visiting a "mark" in a terminal buffer reloads the terminal buffer if it's not loaded.
- `:terminal` buffers optionally are included in Nvim "session" files and restored when the session is reloaded.

## Visual-first editing

- Size: 350 hours
- Difficulty: Medium-Hard
- Desirable Skills:
    - C and Lua
    - Familiar with event-loop programming model
- Code license: Apache 2.0
- Mentor: Justin M. Keyes ([@justinmk](http://github.com/justinmk))
- Tracking issue: https://github.com/neovim/neovim/issues/16296

**Description:**

Vim tradtionally has a "verb-object" editing model, whereas editors like kakoune and helix have "object-verb". The existing visual-mode in Nvim could be enhanced to support this in Nvim.

**Expected Result:**

Visual-mode in Nvim becomes more intuitive and useful:

- it can be repeated with dot (.)
- introduce a modifier similar to `v`, except normal-mode commands work in this mode, after the "selection" is chosen.

## GUI Features

- Size: 175 hours
- Difficulty: Medium-Hard
- Desirable Skills:
    - C and related tools
    - Familiar with event-loop programming model
- Code license: Apache 2.0
- Mentor: Justin M. Keyes ([@justinmk](http://github.com/justinmk)), [@bfredl](http://github.com/bfredl)

**Description:**

Nvim GUIs are implemented as processes communicating with Nvim. Originally the UI protocol exposed most functionality as a single, terminal-like screen grid. Work has been done to allow UIs (including embeddings in GUI editors, like VSCode) to render the screen layout themselves, based on semantic updates from Nvim. Some screen elements like the cmdline, popupmenu and message area has been externalized. As a result of a 2018 [GSOC project](/ideas/neovim/neovim-neovim-issues-8320), windows can be drawn on separate grids.

**Expected Result:**

Further improvements to the GUI protocol.

Some UIs want to render the buffer contents themselves. A solution would be a UI protocol mode, where the rendered grid is not used, rather all decorations, such as syntax highlighting, conceals, virtual text are transmitted for the current viewport. Such an UI would be able to render text without the restrictions of the builtin monospace grid. Then the UI should be able to inform nvim about usage of virtual columns and wrapping, so that vim commands such as `gj` are consistent with how text is presented to the user.

Another path is to improve the core Nvim grid model. We could allow the width and height of cells be different for each row. This would allow for heading text with different font size, and pictures rendered inside windows.

Putting forward your own ideas of UI improvements is encouraged. Read the [docs](https://github.com/neovim/neovim/blob/master/runtime/doc/ui.txt) for the implemented extensions as well as the [tracking issue](/ideas/neovim/neovim-neovim-issues-9421) for ongoing/planned work, as a starting point.




## IDE "Vim mode"

- Size: 175 hours
- Difficulty: Medium
- Desirable Skills:
    - Familiar with RPC
- Code license: Apache 2.0
- Mentor: Justin M. Keyes ([@justinmk](http://github.com/justinmk))

**Description:**

Implement "Vim mode" in an editor/IDE (such as IntelliJ) by embedding a `nvim` instance.

**Expected Result:**

Full Nvim editing should be available in the editor/IDE, while also allowing the user to use the native editor/IDE features.

Examples:

- [VSCode integration](https://github.com/asvetliakov/vscode-neovim)
- [Sublime Text integration](https://github.com/lunixbochs/actualvim)


# GSoC Ideas 2025

## ✅ (DONE) AI primitives

- Size: 350 hours
- Difficulty: Medium
- Desirable Skills:
    - Lua
- Code license: Apache 2.0
- Mentor: Justin M. Keyes ([@justinmk](http://github.com/justinmk))
- Tracking issue: https://github.com/neovim/neovim/issues/32084

**Description:**

Although Nvim doesn't plan to include AI features by default, it should provide basic features that make it easy to build AI plugins (chat, completion, etc.)

**Expected Result:**

Identify and implement Nvim features that make it easy for users to build high-quality AI "chat" and "completion" plugins. For example:

- ✅ Support `textDocument/inlineCompletion` from the LSP 3.18 spec.
- ✅ Add a way to mark a buffer or window as "busy" or "in progress", that works with the default statusline (and custom statuslines).
- ✅ Add a "progress meter" interface to the Nvim standard library.
- ✅ Improvements to the "prompt buffer" concept
    - multiline input
    - paste into the prompt
    - a builtin "filetype" with standard highlighting
    - standard headers with distinctive highlighting
    - standard mappings
- ...?

## ✅ ([DONE](https://github.com/neovim/neovim/pull/33953)) ":restart" command

- Size: 175 hours
- Difficulty: Medium
- Desirable Skills:
    - C
    - Lua
- Code license: Apache 2.0
- Mentor: Justin M. Keyes ([@justinmk](http://github.com/justinmk))
- Tracking issue: https://github.com/neovim/neovim/issues/32484

**Description:**

Developing/troubleshooting plugins has friction because "restarting" Nvim requires quitting, then manually starting again, in some fashion.

**Expected Result:**

Implement a `:restart` command which allows Nvim to restart itself. This will involve some knowledge of inter-process communication / RPC.

## "Remote SSH" features

- Size: 350 hours
- Difficulty: Medium
- Desirable Skills:
    - Lua
- Code license: Apache 2.0
- Mentor: Justin M. Keyes ([@justinmk](http://github.com/justinmk))
- Tracking issue: https://github.com/neovim/neovim/issues/21635

**Description:**

Working with remote systems could be more "ergonomic". VSCode's "remote ssh" plugin demonstrates how ergonomics can greatly improve usability.

**Expected Result:**

Introduce a command or some sort of interface that Allows the user to:

1. input a ssh URI (hostname + port)
     - or select from a list of hosts discovered from your local `~/.ssh/config`
2. nvim connects to the remote ssh endpoint using your local `~/.ssh` credentials
    - or prompts for password as needed
3. nvim starts a new local UI that attaches to a remote `nvim` server running on the remote machine.
4. if necessary, nvim auto-installs itself on the remote machine.
    - it also installs your plugins, on the remote!
5. the local nvim UI controls the remote nvim server, and you can use it to work on the remote machine very much like a local nvim.




---

# GSoC Ideas 2019

## ✅ (DONE) "Multiprocessing" feature

**Description:**

p2p architecture for data sharing between multiple Nvim instances. Similar to Python's [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) module, the idea is to to offload Nvim tasks (VimL and/or Lua) to child Nvim processes.

Here's a picture of the potential workflow:

1. parent calls `invoke_async(Foo)`
2. parent spawns new child `nvim` process
3. parent sends command name `Foo` + state to child
4. parent does other, unrelated work
5. child completes its `Foo` work
6. child sends notification (method name + state) to parent

**Difficulty:** Hard

**Code license:** Apache 2.0

**Mentor:** Justin M Keyes ([@justinmk](http://github.com/justinmk))

## ✅ ([DONE](https://github.com/neovim/neovim/pull/10071)) TUI (Terminal UI) remote attachment

**Description:**

The built-in UI is called the TUI. It looks like Vim, but internally it is decoupled from the UI and "screen" layout subsystem. It was designed to be able to connect to other (remote) instances of Nvim, but this hasn't been implemented yet. [#7438](/ideas/neovim/neovim-neovim-issues-7438)

Nvim is both a server and a client. Nvim (client) can connect to any other Nvim (server). And Nvim [GUIs](/ideas/neovim/related-projects) can show the screen of a remote Nvim server.

But the built-in Nvim TUI cannot show the screen of a remote Nvim server. That's the goal of this project.

- It is not "live share". It's just showing the remote UI in a client TUI.
- Networking question are out of scope. It is assumed the client has an SSH tunnel or named pipe to connect to.

The Nvim API model is:

- `:help api`: general API functions
- `:help ui`: UI events
- Any client can call any API function.
- If a client calls `nvim_ui_attach`, then it is a "UI client". This simply means that Nvim will send UI events as msgpack-rpc notifications on the channel.

That's how _every_ Nvim UI works. And that's how the TUI client (this project proposal) will work.

Python "demo UI" may be helpful: https://github.com/neovim/python-gui

The simplest UI is the "fake UI" implemented in `test/functional/ui/screen.lua` from the Nvim test suite. It creates a text UI from real Nvim UI events. This allows us to write Lua tests that check the state of the UI, by simply writing the text UI in the test. In the Neoivm repo, "git grep 'screen:expect'" shows all of the places where this is used.

The `example_spec.lua` test shows a simple example. You can try it by running this shell command:

    TEST_FILE=test/functional/example_spec.lua make functionaltest

Overview of the `screen.lua` "fake UI" implementation:

- `Screen._wait()` / `Screen:sleep()` runs the event loop to consume UI events
- `Screen:_redraw()` dispatches UI events to the appropriate handlers
- For example `Screen:_handle_grid_line()` consumes a line event, and updates some tables (self._grids and self._attr_table).
    - And those tables are literally the contents of the fake UI that `Screen:expect()` tests against.

Use cases:

- Connect to any Nvim. Unlike tmux, Nvim UI client can connect to any other running Nvim, including GUIs.
- Potential for using `libnvim` as the RPC core of any Nvim API client, to eliminate the need for clients to implement their own msgpack-RPC handling.

**Expected Result:**

Implement a TUI "remote UI" client. Modify the TUI subsystem so that it can display a remote Nvim instance.
The C codebase already has msgpack support, an event-loop, and the ability to connect to sockets/named pipes/etc.

- Extend `tui/tui.c` to:
  1. connect to a channel
  2. get UI events from the channel
  3. unpack the events and call the appropriate handlers
- Extend `tui/input.c` to:
  1. send user input to the channel (i.e. call the nvim_input() API function)

Example:

    nvim --servername foo

will connect to the Nvim server at address `foo`. The `nvim` client instance sends input to the remote Nvim server, and reflects the UI of the remote Nvim server. So the `nvim` client acts like any other external (G)UI.


**Difficulty:** Medium

**Code license:** Apache 2.0

**Mentor:** Justin M Keyes ([@justinmk](http://github.com/justinmk)), Björn Linse ([@bfredl](http://github.com/bfredl))

---
# GSoC Ideas 2018

## ✅ ([DONE](https://github.com/neovim/neovim/pull/8707)) UI protocol improvements

**Description:**

Nvim GUI:s are implemented as processes communicating with Nvim over a protocol. Currently this protocol exposes most functionality as a terminal-like screen grid. A long term goal is enabling richer UIs (including embeddings in GUI editors, like VSCode) by refactoring the protocol towards semantic updates and letting the GUI actually draw buffer contents and other screen elements. Currently this has been implemented for a few specific elements, like the completion popup menu and the command line.

**Expected Result:**

The UI protocol has gained new capabilities. This could involve substantial changes such as the GUI receiving redraw updates for each window separately, so that the GUI could be responsible for managing the overall layout of windows and statuslines.

Alternatively, improvements could be done within the current global screen grid, such as the ability to display grid-aligned images in signs, buffers and statuslines. It could also involve adding semantic information to the grid, so that GUI:s can identify screen elements reliably rather than guessing it from highlights.

- Code license: Apache 2.0

**Difficulty:**

Medium to Hard

**Student:** ([@UtkarshMe](https://github.com/UtkarshMe))

**Mentor:** Björn Linse ([@bfredl](http://github.com/bfredl))

## Java client

**Desirable Skills:**

- Familiar with Vim/Nvim and Vim script (VimL)
- Moderate/High experience in Java
- Familiar with event-loop programming model

**Description:**

Implement a Nvim [API client](https://github.com/neovim/neovim/wiki/Related-projects#api-clients) using Java. 

Implement a client, written in Java, which allows Java applications to control Nvim using the Nvim RPC API.  If you are familiar with AWS or any other SaaS, note that a Nvim API client is just like a SDK for a REST web service, except that Nvim uses msgpack, not HTTP/JSON.

The Nvmi RPC API is documented at [:help api](https://neovim.io/doc/user/api.html) and [:help rpc](https://neovim.io/doc/user/msgpack_rpc.html).

To correctly implement the client one needs to understand the [msgpack-rpc](https://github.com/msgpack-rpc/msgpack-rpc/blob/master/spec.md) protocol. Some sort of event-loop mechanism will be needed to handle notifications.

For reference, you can find clients in other languages at the [related projects](https://github.com/neovim/neovim/wiki/Related-projects#api-clients) wiki page.

The ultimate goal is to have a library that can be used to create plugins for [IntelliJ](https://www.jetbrains.com/help/idea/plugin-development-guidelines.html) and [Eclipse](https://help.eclipse.org/mars/index.jsp?topic=%2Forg.eclipse.platform.doc.isv%2Fguide%2Ffirstplugin.htm).  **Minimizing third-party dependencies** may help there.

**Expected Result:**

- Java library that can be used to build Neovim extensions (UIs and other applications).
  - Method signatures generated from `nvim --api-info`.
  - Since `nvim` is already required (for `--api-info`), the Java code-generation script could be written in Lua (which is built-in to `nvim`).
- Passes the test suite used by the Nvim [python-client](https://github.com/neovim/python-client).
  - Using the [python-client tests](https://github.com/neovim/python-client/tree/master/test) as a guide, create equivalent tests using a Java testing framework.
  - Test suite should be runnable from the command-line (should not require an IDE) via maven/gradle (or some other industry-standard build-tool).
- Builds (and passes tests) on Linux (Travis CI) and Windows (AppVeyor)
- End-user deliverable should be compatible Java 6 (this is negotiable)
- Source-code can be latest version of Java (no backwards-compatibility requirement)
- Code license: Apache 2.0

**Difficulty:**

Medium

**Mentor:** Justin M Keyes ([@justinmk](http://github.com/justinmk))

## ✅ ([DONE](https://github.com/neovim/nvim.net)) C# client

**Description:**

Implement a Nvim [API client](https://github.com/neovim/neovim/wiki/Related-projects#api-clients) using C#. 

Implement a client, written in C#, which allows C# applications to control Nvim using the Nvim RPC API.  If you are familiar with AWS or any other SaaS, note that a Nvim API client is just like a SDK for a REST web service, except that Nvim uses msgpack, not HTTP/JSON.

The Nvmi RPC API is documented at [:help api](https://neovim.io/doc/user/api.html) and [:help rpc](https://neovim.io/doc/user/msgpack_rpc.html).

To correctly implement the client one needs to understand the [msgpack-rpc](https://github.com/msgpack-rpc/msgpack-rpc/blob/master/spec.md) protocol. Some sort of event-loop mechanism will be needed to handle notifications ([hint1](https://blogs.msdn.microsoft.com/pfxteam/2012/01/20/await-synchronizationcontext-and-console-apps/), [hint2](https://blogs.msdn.microsoft.com/pfxteam/2012/02/02/await-synchronizationcontext-and-console-apps-part-3/)).

For reference, you can find clients in other languages at the [related projects](https://github.com/neovim/neovim/wiki/Related-projects#api-clients) wiki page.

The ultimate goal is to have a library that can be used to create plugins for Visual Studio.  **Minimizing third-party dependencies** may help there.

**Expected Result:**

- C# library that can be used to create C#-based Neovim extensions (UIs and other applications).
  - Method signatures generated from `nvim --api-info`.
  - Since `nvim` is already required (for `--api-info`), the C# code-generation build script could be written in Lua (which is built-in to `nvim`).
- Passes the test suite used by the Nvim [python-client](https://github.com/neovim/python-client).
  - Using the [python-client tests](https://github.com/neovim/python-client/tree/master/test) as a guide, create equivalent tests using a C# testing framework.
  - Test suite should be runnable from the command-line (should not require an IDE) via MSBuild or some other industry-standard build-tool.
- Builds (and passes tests) on Linux (Travis CI) and Windows (AppVeyor)
- Builds against **.NET Standard 2.0**
- Deliverable should be easy to install as a NuGet (or other) package.
- Source-code can be latest version of C# (no backwards-compatibility requirement)
- Code license: Apache 2.0

**Difficulty:**

Medium

**Student:** ([@b-r-o-c-k](https://github.com/b-r-o-c-k))

**Mentor:** Justin M Keyes ([@justinmk](http://github.com/justinmk))
