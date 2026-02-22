# Developer FAQ

**Parent:** The ns-3 Network Simulator Project — Project Ideas
**Source:** https://www.nsnam.org/wiki/Developer_FAQ
**Scraped:** 2026-02-22T23:28:47.553319

---

# Developer FAQ

[Jump to navigation](https://www.nsnam.org#mw-head)

[Jump to search](https://www.nsnam.org#searchInput)

[Main Page](https://www.nsnam.org/wiki/Main_Page) - [Roadmap](https://www.nsnam.org/wiki/Roadmap) - [Summer Projects](https://www.nsnam.org/wiki/Summer_Projects) - [Project Ideas](https://www.nsnam.org/wiki/Project_Ideas) - [Developer FAQ] - [Tools](https://www.nsnam.org/wiki/Tools) - [Related Projects](https://www.nsnam.org/wiki/Related_Projects)

[HOWTOs](https://www.nsnam.org/wiki/HOWTOs) - [Installation](https://www.nsnam.org/wiki/Installation) - [Troubleshooting](https://www.nsnam.org/wiki/Troubleshooting) - [User FAQ](https://www.nsnam.org/wiki/User_FAQ) - [Samples](https://www.nsnam.org/wiki/Category:Samples) - [Models](https://www.nsnam.org/wiki/Category:Models) - [Education](https://www.nsnam.org/wiki/Education) - [Contributed Code](https://www.nsnam.org/wiki/Contributed_Code) - [Papers](https://www.nsnam.org/wiki/Papers)

This FAQ is for developers who have accounts on the server code.nsnam.org, and for maintainers.

**Warning to readers:** This info is really out of date and should be cleaned up/cleaned out. In the meantime, please review the Sphinx documentation maintained here, especially the contributing guide: [https://www.nsnam.org/documentation/development-tree/](https://www.nsnam.org/documentation/development-tree/)

## New accounts on code.nsnam.org

**Node:** code.nsnam.org is now legacy Mercurial server-- current users should use Gitlab.com.

In general, we are restricting new accounts on code.nsnam.org to maintainers who need commit access to the main repositories. Going forward, we encourage other developers who want to host or stage code to use hosted services such as [https://github.com](https://github.com) (git) or [https://bitbucket.org](https://bitbucket.org) (mercurial).

## Mercurial repository layout for code.nsnam.org

These instructions pertain to users of code.nsnam.org who wish to host private repositories such as [http://code.nsnam.org/tomh/ns-3-simple-wireless](http://code.nsnam.org/tomh/ns-3-simple-wireless).

- In your home dir on code.nsnam.org, you will find a new directory named "
`repositories/username`

". e.g.:`/home/tomh/repositories/tomh`

. If you create a repository in this directory, it will appear automatically on[http://code.nsnam.org](http://code.nsnam.org) - You can ssh and rsync to your personal account and manage these repositories
- You can push to these repositories with the command such as:
`hg push`

[ssh://tomh@code.nsnam.org/repositories/tomh/ns-3-simple-wireless](ssh://tomh@code.nsnam.org/repositories/tomh/ns-3-simple-wireless) - You can pull with the usual commands:
`hg clone`

[http://code.nsnam.org/tomh/ns-3-simple-wireless](http://code.nsnam.org/tomh/ns-3-simple-wireless) - If you want to have shared non-mainline repositories (e.g. the 'laa' or 'dcf' users), we can create a user by that name and add multiple public keys to that account.
- The push command for the main tree is still:
`hg push`

[ssh://code@code.nsnam.org/repos/ns-3-dev](ssh://code@code.nsnam.org/repos/ns-3-dev) **New developers on code.nsnam.org, please read this:**When creating a new repository, do not "hg clone" it into your repositories directory on code.nsnam.org (which will generate a big ns-commits mail message); instead, just copy (cp -r) or rsync it to your local "/home/username/repositories/username" directory. Recommended steps:`cp -rp /home/code/repos/ns-3-dev /path/to/my/repositories/ns-3-feature-name`

- edit the .hgrc file in your new
`ns-3-feature-name`

repository - check that the
`Description`

and`Contact`

fields for this new repository are correct by browsing[http://code.nsnam.org](http://code.nsnam.org)


## General mercurial tips

**How to undo a commit**: Let's suppose you are working on a private repository and you check something in, but some other files were inadvertently checked in, and you want to revert and start over. There are two ways to do this:`hg revert`

: This can be used to revert the repository to a previous revision number. For example, to revert to changeset number #1000, type`hg revert -r 1000 --all`

. This does**not**remove your checkin from the repository history. For example, if your mistaken checkin was number 1001, and you revert back to 1000 and then commit, you will be at changeset number 1002 now even though the code matches what was in there at changeset 1000.`hg rollback`

: This can be used to completely wipe clean the last transaction only (commit, import, push, pull). Use with care-- cannot be undone.

**How to restore repository to the tip**: Sometimes you want to just clean the repository of your local changes, to restore back to the last tip of the repository. This can be done globally or file-by-file.- Globally:
`hg update -C`

(will restore _all_ tracked files to the last committed version; will leave untracked files untouched) - Per-file:
`hg revert filename`

(replace 'filename' with the path to the file of interest).

- Globally:
**How to rename a file**:`hg rename old-file-name new-file-name`

This is preferable to adding the new file name and removing the old file name, because it preserves revision history. Don't forget to commit after a rename once you are done.**How to merge a branch**: If you have forked a branch repository, have worked on it, and are ready to merge it back to ns-3-dev, here are the steps to take (Also, read[this chapter](http://hgbook.red-bean.com/hgbookch3.html)to better understand how the mercurial source tree is structured when merging is occurring):*cd into your branch*`hg pull`

[http://code.nsnam.org/ns-3-dev](http://code.nsnam.org/ns-3-dev)`hg merge`

*resolve all of the merge issues, if any, and confirm that it builds and validates*`hg ci -m"merge your-branch-name with tip"`

`hg push`

[ssh://code@code.nsnam.org/repos/ns-3-dev](ssh://code@code.nsnam.org/repos/ns-3-dev)

**How to create patches for circulation**:`hg export tip`

Suppose you don't have write access to the main repositories, but have some patches you'd like to circulate. This command outputs out all the diffs for the latest changeset you committed into your local repository. Simply redirect this output to a file, and you can circulate your patch for consideration. This is for when you have committed changesets. If you would like to export uncommitted changes as a patch, use:`hg diff`

This gets the diffs of all the uncommitted changes versus what is checked into the repository. Redirect to a file for circulation among developers, or for inclusion with a bug report, etc.**Save a push URL so that you don't need to enter it each time**: If you are tired of having to specify the same ssh URL each time when you go to push, you can specify a default push location in the branch's local hgrc.*cd into your branch*`vi .hg/hgrc`

*add the following line to the [paths] section*`default-push =`

[ssh://username@code.nsnam.org/repositories/username/ns-3-reponame](ssh://username@code.nsnam.org/repositories/username/ns-3-reponame)`hg push`

should now "just work" without the URL

**How to fix two-headed repositories**: Note, please never check in code by forcing it (with hg push -f option). This will cause the repository to have multiple heads. If the repository ends up with two heads, this can fix it:`hg merge`

`hg commit -m"merge two heads"`

`hg push ...`


**Don't use named branches**: that is, never do "`hg branch`

" nor "`hg push --new-branch`

"

## The WAF build system

**Note:** Waf was removed in favor of CMake in release 3.36.

See also the [Waf User FAQ](http://www.nsnam.org/wiki/index.php/User_FAQ#WAF_.28new_build_process.29).

### Obtaining WAF

A snapshot of WAF is distributed with ns-3 releases and mercurial branches. This snapshopt has been tested to work correctly with ns-3, although the *trunk* version from the main WAF repository usually works equally well.

### Documentation resources

There is a [WAF book](http://freehackers.org/~tnagy/wafbook/index.html). Some useful tips can be found in the [WAF Wiki](http://code.google.com/p/waf/w/list). Finally, there is a plethora of examples distributed in WAF itself, in the 'demos' directory.

### How to add new ns-3 modules

Ns-3 is organized as a set of *modules*. Each module is built as a set of object files, has a name, may depend on other modules, and installs a specific set of *public header files*.

Starting with version 3.11, ns-3 went to a modular directory structure. The following chapter in the ns-3 Manual shows how to add a module in the new directory structure:

If you are using a version of ns-3 earlier than 3.11, then follow the instructions in this FAQ.

To add a new ns-3 module to the WAF build system, begin by creating a directory under the `src/`

subtree, with the source files inside. We will use *p2p* module as example here. Each module needs to define a `wscript`

file. For instance let us see what `src/devices/point-to-point/wscript`

contains:

## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*- def build(bld): module = bld.create_ns3_module('point-to-point', ['node']) module.source = [ 'point-to-point-net-device.cc', 'point-to-point-channel.cc', 'point-to-point-topology.cc', ] headers = bld.create_obj('ns3header') headers.module = 'point-to-point' headers.source = [ 'point-to-point-net-device.h', 'point-to-point-channel.h', 'point-to-point-topology.h', ]

A wscript file is basically a special python module. The main entry point to this module is the `build(bld)`

python function.

In the code above, the *module* variable represents a ns-3 module; internally it is a WAF 'objects' build object that will be linked to be come part of the ns3 library. It is created by calling a special method bld.create_ns3_module, whose first parameter is the name of the module, and the second parameter is a list of other modules that this module depends on. Additionally, module.sources has to be set to the list of source files (excluding header files) that constitute the module. Warning: beware that the name of the module must match the name of the directory where it is built. In this case, the module is in 'src/devices/point-to-point', so the module name must be 'point-to-point'.

There is usually also a *headers* object. It is used to declare public header files. These files are copied to the build directory, and can be included from any module or program with `#include "ns3/header-name.h"`

.

A final step, after the wscript file is created, is to register it. Open the file `src/wscript`

and add the new module to the `all_modules`

list variable:

all_modules = ( 'core', 'common', 'simulator', 'node', 'internet-node', 'devices/point-to-point', # <---- example here 'applications', )

### Adding programs

Use the special method bld.create_ns3_program(name, [...dependencies...]). Example:

obj = bld.create_ns3_program('main-simple', ['node', 'internet-node', 'applications']) obj.source = 'main-simple.cc'

## Generating new python bindings

See the [ns-3 python documentation](https://www.nsnam.org/docs/manual/html/python.html).

## Release Process

## Mercurial

- Adrian Tam's
[mercurial cheatsheet](http://mercurial.selenic.com/wiki/QuickReferenceCardsAndCheatSheets) [Mercurial for subversion users](http://wiki.pylonshq.com/display/pylonscookbook/Mercurial+for+Subversion+Users)

### Your .hgrc file

Each mercurial checkin is made by a user. If there is no .hgrc configuration file in the user's home directory, mercurial will default to using the accountname@hostname. This leads to commit lines like the following:

changeset: 7:e53ac3c458e9 user: tomh@powerbook.local

To avoid this, and have it print something nicer, like

changeset: 7:e53ac3c458e9 user: Tom Henderson <tomh@tomh.org>

you need to add an .hgrc file to your home directory, such as follows:

[ui] username = Tom Henderson <tomh@tomh.org>

or, for each checkin, you will need to specify the user string manually, such as:

hg commit -u"Tom Henderson <tomh@tomh.org>" -m"commit message"

If you want to commit a change on behalf of another user, such as attributing a bug fix to the original author, you can use the above -u command to override what is in your .hgrc file

### Avoid named branches

Mercurial has a feature called a [named branch](http://mercurial.selenic.com/wiki/NamedBranches). These are not the same as git branches; they are permanent symbolic names in the repository, and do not want them propagating to the main repository. Here is a discussion on this feature: [http://mercurial.808500.n3.nabble.com/Closed-branch-push-behavior-td3562689.html](http://mercurial.808500.n3.nabble.com/Closed-branch-push-behavior-td3562689.html)

The workflow that we recommend for working on new features is to clone new repositories instead of using named branches.

Also, no one but the release manager should create a mercurial tag and check it into ns-3-dev.

Some named branches were inadvertently merged to ns-3-dev around May 2013. If you have a private repository that is tracking ns-3-dev, you may get this error message:

abort: push creates new remote branches: coverity, ptl,...

To get past this, one must use the --new-branch option such as:

hg push --new-branch[ssh://code.nsnam.org/repositories/tomh/ns-3-lr-wpan]

## Coding style

Of course, you need to follow the ns-3 coding style: [http://www.nsnam.org/developers/contributing-code/coding-style/](http://www.nsnam.org/developers/contributing-code/coding-style/)

### If you use emacs

All ns-3 files include this:

/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */

The "gnu" indentation style mostly conforms to the ns3 coding guidelines, but has a few quirks. One of these is that code after "namespace ns3 {" is indented, while the ns3 coding style says it should not. One workaround is typing the following command for every open buffer:

C-c C-o innamespace <ret> 0 <ret>

Fixing this issue permanently would require using a different modeline, as discussed [in this thread](http://www.nabble.com/emacs-indentation-innamespace-td22802271.html).

### If you use VIM

If you use VIM you should add the following lines to your ~/.vimrc:

set ts=2 set sw=2 set sta set et set ai set si set cin

And the following lines to realize white space errors (trailing white spaces):

let c_no_bracket_error=1 let c_no_curly_error=1 let c_comment_strings=1 let c_gnu=1

## Submitting patches for consideration

The best way to submit a patch for consideration is to request a patch review:

- download
[http://codereview.appspot.com/static/upload.py](http://codereview.appspot.com/static/upload.py) - record the changes you want to request a review for in a mercurial repository: "hg commit ..."
- within the mercurial repository, run upload.py to submit a review with
[http://codereview.appspot.com/](http://codereview.appspot.com/). Make sure you specify ns-3-reviews@googlegroups.com as a CC. - paste your review request on
[http://www.nsnam.org/wiki/index.php/Reviews](http://www.nsnam.org/wiki/index.php/Reviews) - announce your review request on ns-developers

When you send a tree without a detailed summary of your changes, it would help if you could send a list of the changesets you want to merge. To generate it, first merge with ns-3-dev and then, from your modified directory, run "hg outgoing -p [http://code.nsnam.org/ns-3-dev](http://code.nsnam.org/ns-3-dev)"

Also, avoid spurious coding style and whitespace changes when preparing such a patch, as it distracts from the readability of your proposed technical changes.

If you already pulled changes from ns-3-dev into your private repository after you started doing your private modifications, there is an issue to be considered. upload.py does not let you specify a range of revisions, nor a set of changesets. So if you just run upload.py in your private repository, also the changesets pulled from ns-3-dev will be published on codereview, which is of course not desirable.

A possible workaround is to pull your changes into a temporary repository which is an up-to-date clone of ns-3-dev. The following code should do the trick. This code assumes that your private repository is in path DEV_BRANCH_WITH_NEW_FEATURE, and that it is in sync with ns-3-dev.

hg clone http://code.nsnam.org/ns-3-dev ns-3-tmp cd ns-3-tmp export REVNO=`hg tip -q | sed 's/:.*$//'` hg pull DEV_BRANCH_WITH_NEW_FEATURE hg merge hg commit -m "merged new feature" upload.py --rev=$REVNO --cc=ns-3-reviews@googlegroups.com

## Checking in code

This is mainly for maintainers who want to commit their code, or patches from others, to `ns-3-dev`

or other mainline repositories.

### General guidelines

Subscribe to ns-bugs mailing list, if you haven't already, so that you get the bug tracker notifications.

Please maintain a valid .hgrc in your home directory so that the proper username can be added to your commits. Here is an example of a minimal one that provides a username for commit messages:

[ui] username = John Doe <john.doe@example.com>

Please always update your code to the tip of ns-3-dev before checking in. Never force a push (which creates another head on the repository); actually, creating multiple heads is now disabled on the server and the push will fail. If someone else pushed something before you got a chance to perform your push, you will need to pull those changes, resolve any possible conflicts, merge, and then push. Also don't push with "--new-branch" ([the use of named branches is not allowed](http://mailman.isi.edu/pipermail/ns-developers/2013-May/011169.html)).

Before checking in code, it is good practice to pull from ns-3-dev and deal with any merge issues in advance:

cd ns-3-dev hg pull -u

Once you think you have code to commit (or after you have done a bunch of small commits), it is good practice to run the test suite:

./test.py

Depending on the intrusiveness and nature of your patch, you may want to go further with your testing, including testing debug, optimized, and static versions, generating new python bindings, and running test.py with the -g option for valgrind.

When you are ready to push upstream, it is good practice to review the outgoing changesets. This can be done with the following command:

hg outgoing -v

If this looks good, the command to check in code is:

hg push[ssh://code@code.nsnam.org/repos/ns-3-dev]

If it fails because you forgot to do an update before this step, you will need to:

hg pull hg update hg commit -m "branch merge" ./test.py (make sure you didn't break anything) hg push[ssh://code@code.nsnam.org/repos/ns-3-dev]

If your commit closes a bug in the bugzilla database, please label the commit with the bug number, note the resultant hexidecimal changelog ID, and mark the bug as RESOLVED FIXED and list the changelog ID in the tracker entry. e.g.:

hg commit -m "bug 1365: unused variable declaration of a private data member"

### merging vs. rebasing

Mercurial does not have a native [rebase feature](https://git-scm.com/docs/git-rebase) like git (or if it does, we do not use it). As a result, you can be working on some code for commit to ns-3-dev, get it all ready to push, and find that the tip of `ns-3-dev`

has evolved since you forked. So you cannot push immediately; you would create two heads (which is forbidden). What to do?

- (preferred): Manually rebase on the latest ns-3-dev. That is, export your changeset or changesets to patch files, checkout a fresh ns-3-dev, and try to import (or patch and merge) your changesets. This tends to keep the mainline tree history very linear, which helps future maintainers. This can be very simple if you are trying to push just one changeset. Let's assume that you committed one patch and have one outgoing changeset (
`hg outgoing -v`

shows one changeset). You can try:`hg export tip > my-changeset.patch`

(this extracts your changeset with commit string intact)`hg rollback`

(this undoes the last commit`hg pull -u`

(this syncs your ns-3-dev to code.nsnam.org)`hg import my-changeset.patch`

(this reapplies your patch on top of the tip)`hg outgoing -v`

(everything look OK still?)`hg push`

(should work now)[ssh://code@code.nsnam.org/repos/ns-3-dev](ssh://code@code.nsnam.org/repos/ns-3-dev)

- (alternative): Merge and resolve. That is, perform a 'hg pull -u' onto your local copy (with outgoing changesets), and one of two things will happen.
*simply merge heads.*If the new changesets are orthogonal to yours, update will succeed, and you'll have to do a`hg commit -m"merge heads"`

commit to merge the two heads into one. Then, you can try to`hg push`

again.*resolve conflicts and merge.*If the update fails, you will have to work through the merge conflicts and commit the changes, merging also the two heads. This can be messy.


### When to commit

When is it OK to commit code (from a bugzilla patch, or from a code review)?

- If you are the maintainer of an existing module, you can commit changes when you want, as long as you coordinate with the release manager (if it is close to a release or code freeze date).
- If you are not the maintainer (e.g. your patch touches other modules too), please obtain +1 from the maintainer if the change is not trivial. You may have to remind him or her about it; if you do not get a response, email the release manager.
- If you would like to add a new module, or to commit to a module that does not have a maintainer, it usually should have some review by core maintainers. Email the release manager for help.
- When in doubt, email the release manager.

### Checking in patches from other users

If you as a maintainer check in a patch authored by someone else, it is good practice to credit them in the commit message using the --user or -u option to hg; e.g.:

hg commit -m"...commit message..." -u"Another User <another.user@example.com>"

You can sometimes find the appropriate user string by searching the hg log for their previous commits; e.g.

hg log | grep <username>

Reference: [http://www.gnu.org/prep/maintain/html_node/Recording-Contributors.html](http://www.gnu.org/prep/maintain/html_node/Recording-Contributors.html)

If the author of the patch is a first-time author, please ask in private email beforehand whether he or she is comfortable with the commit string (name and email address) that you choose. The reason is that people may want a specific email address (e.g. a non-work address, or a work address) to exist in the commit string.

### Checking that you don't introduce regressions or leaks

Before you do a checkin that is somewhat intrusive, you should run the ns-3 tests. Make sure that you have valgrind installed, and change into the top level directory and type

./test.py -g

If you do this, you will see a bunch of passing tests and then, if something goes wrong:

FAIL: TestSuite test-tcp-large-transfer

Sometimes you will commit something that will fail on another regression buildslave (e.g. clang raises a warning that gcc does not). If you have access to both clang and gcc, it is good to check beforehand; if not, don't worry, another maintainer will try to clean it.

### Updating python bindings

Python bindings are kept loosely synchronized with ns-3-dev. Additions to the public API do not require a bindings rescan immediately; they should not break the build. Changes to the public API, however, will typically break the bindings compilation.

We tend to prefer to keep the bindings update in a separate changeset, to make the C++ changes more readable in the codebase. That is, if you introduce a C++ API change in one changeset, commit it first, and then do the Python rescan and commit any changed bindings as a separate commit.

At the moment (Oct. 2016), the bindings scanning process is limited to gcc-4 machines (there is an open bug on moving this over to CastXML). If this is a problem for you (i.e. your commit breaks the bindings but you don't have an easy facility to regenerate them), coordinate with Tom or Tommaso about the rescanning.

### Commit message formatting

Going forward, we prefer to follow the conventions adapted from [http://chris.beams.io/posts/git-commit/](http://chris.beams.io/posts/git-commit/)

- Separate subject from body with a blank line
- Limit the subject line to 60 characters
- Capitalize the subject line
- Do not end the subject line with a period
- Use the imperative mood in the subject line
- Wrap the body at 72 characters
- Use the body to explain what and why vs. how

For the subject line, if the module name and bug number can be succinctly included, they may preface the subject string. The module name is lowercase as per the directory name, followed by a colon. If the commit closes a bug, it may parenthetically mention that bug, and use the '#' character. If it purely affects documentation or logging in a module, it can have '(documentation)' added. Documentation, logging, and doxygen-only commits outside of a module may be identified with 'documentation:' tag, and the build system with 'waf:' Examples:

sixlowpan: (fixes #2272) Allow NetDevice to send packets larger than MTU

sixlowpan: (documentation) Complete doxygen on input/output parameters

documentation: Update RELEASE_NOTES and CHANGES.html

waf: Update Waf to 1.8.12

If the subject doesn't fit neatly into one of these categories, use your judgement within the 60 character limit.

Here is an example with both subject and body:

Summarize changes in around 60 characters or less More detailed explanatory text, if necessary. Wrap it to about 72 characters or so. In some contexts, the first line is treated as the subject of the commit and the rest of the text as the body. The blank line separating the summary from the body is critical (unless you omit the body entirely); various tools like `log`, `shortlog` and `rebase` can get confused if you run the two together. Explain the problem that this commit is solving. Focus on why you are making this change as opposed to how (the code explains that). Are there side effects or other unintuitive consequences of this change? Here's the place to explain them. Further paragraphs come after blank lines. - Bullet points are okay, too - Typically a hyphen or asterisk is used for the bullet, preceded by a single space, with blank lines in between, but conventions vary here If you use an issue tracker, put references to them at the bottom, like this: Resolves: #123 See also: #456, #789

### Logging your changes in the release notes

The project maintains two files for tracking changes to the codebase. As you check in changes to the code that fix bugs, add features, or change the existing behavior of the simulator, you should also update these files.

*CHANGES.html*: Used to log changes to the build system, new API, changes to existing API, and changed behavior.*RELEASE_NOTES*: Summarize new user-visible features and bugs fixed.

These files may both be updated, or maybe only one is updated for a given changeset. For instance, if you change the API on a class, you might add a simple bullet "Changed API for class X to improve ability to do Y" to RELEASE_NOTES, but add more detail about exactly which signatures changed in the CHANGES.html file. If the change is trivial (e.g. adding missing Doxygen), there is no need to edit these files.

Please update these files when you make changes to ns-3-dev rather than relying on the release manager later documenting them.

### Fixing a bug from the Bugzilla tracker

Q. What I should do when a bug will be fixed (send a mail to the mailing list, write some comment to bugzilla, other ) ?

A. The typical thing to do is:

- check in the bug fix to ns-3-dev with a commit message that indicates the bug number, such as "bug 903: TapBridge doesn't close cleanly". If the patch was created by a user, you can use their name and email in the mercurial commit userstring.

- remember what the changeset number is; Mercurial provides both a local sequential integer, and a global hexadecimal value; e.g.

changeset: 1763:4624d5aba98f

- mark the bug as "Resolved, Fixed" in Bugzilla, with a comment such as "fixed in changset 4624d5aba98f", or "fixed in changeset 1763:4624d5aba98f". Bugzilla will notify the ns-bugs mailing list of the fix, and the ns-commits list will be notified of the checkin.

## Using gcov and lcov code coverage tools

Here is a brief howto for using the [lcov](http://ltp.sourceforge.net/coverage/lcov.php) front-end to gcc's code coverage tool [gcov](http://gcc.gnu.org/onlinedocs/gcc/Gcov.html)

A custom version of lcov and its associated tools (geninfo, genhtml) is stored in the directory utils/lcov/, and this is the version that waf uses to run lcov. As of ns-3.13, the version of lcov in ns-3 is lcov-1.9, with geninfo patched to deal with [this branching bug](http://old.nabble.com/-Ltp-coverage--lcov-hangs-td28514226.html).

**Note (Oct. 10, 2017):**Please see[https://www.nsnam.org/bugzilla/show_bug.cgi?id=2799](https://www.nsnam.org/bugzilla/show_bug.cgi?id=2799)about recent problems with running lcov-report through Waf; you may be better to run lcov directly on the coverage files, as described in the bug report.

You probably also need to have a version of lcovrc file installed somewhere (either at /etc/lcovrc or ~/.lcovrc). The easiest way to do this is to install lcov from your package manager; e.g.

sudo apt-get install lcov

or install it from source. But just be aware that waf will use the version that is maintained in the utils/lcov/ directory.

Then, for instance, to see the coverage of the ns-3 test suite, type:

./waf configure --enable-gcov --enable-examples --enable-tests ./test.py ./waf --lcov-report

You will find a file "index.html" in the directory build/debug-gcov/lcov-report/ that you can look at with your browser.

Note that if you want to test coverage of another program, you will want to zero the counters for lcov. You can't presently do this from within waf but you can run this command from your top-level ns-3 directory:

utils/lcov/lcov --directory build --zerocounters

and it should report:

Deleting all .da files in build and subdirectories Done.

## The preferred way to create a private repository

Let's say that developer "alice" wants to create a new repository "ns-3-dev-new-feature" that will exist on the code server as alice/ns-3-dev-new-feature. Suppose she wants to fork from the tip of ns-3-dev.

cd /home/alice/repositories/alice cp -r /home/code/repos/ns-3-dev ns-3-dev-new-feature cd ns-3-dev-new-feature/.hg

At this point, edit the "hgrc" file to provide contact/description information:

[paths] default =[http://code.nsnam.org/alice/ns-3-dev-new-feature][web] description = alice's new feature contact = <alice@example.com>

Next, check that your repository shows up properly on the [web page](http://code.nsnam.org/?sort=lastchange).

At this point, you are done with the code server, and you can perform "hg clone [http://code.nsnam.org/alice/ns-3-dev-new-feature](http://code.nsnam.org/alice/ns-3-dev-new-feature)" on your local machine.

**Note:** A common minor problem is if you do an "hg clone" into the new directory instead of a "cp -r", there will be a huge ns-commits mail message generated. This is why "cp -r" is preferred way to do this.

## Testing code on nsnam.org hosts

Some times a compilation error can only reproduced in certain architectures. nsnam.org has some machines that can be accessed remotely for testing purposes, if you have an appropriate account. Contact Tom Henderson if you need an account.

### Full Suite

Note that this takes several hours to run. It puts a specified branch through its paces on several machines/architectures. You can specify a branch to test and a notification email address where you will receive a report about how the branch performed in the tests (SUCCESS or FAILURE).

$ ssh ns-regression.ee.washington.edu $ sudo -u nsnam bash $ cd /usr/local/bin/ $ ./ns-3-run-tests.sh -h usage: ./ns-3-run-tests.sh options This script runs the ns-3 branch through the ns-regression testbed. OPTIONS: -h Help: show this message -n ns-3 branch Default: ns-3-dev -m mailto address. Where to send the mail. If unspecified, program output will just scroll onto stdout. $ ./ns-3-run-tests.sh -n mathieu/ns-3-simu -m someone@wherever.com

### Ubuntu x86_64

ssh ns-regression.ee.washington.edu

### Mac OS X PowerPC

ssh ns-regression.ee.washington.edu sudo -u nsnam bash <enter your password> ssh darwin-ppc

## Adding a buildslave to our BuildBot

The ns-3 project uses BuildBot to test the ns-3-dev build daily. The buildmaster resides on a server at the University of Washington. Currently, we use several buildslaves running Fedora Core 10 with different versions of gcc as well as a Mac OS X PPC machine. For a quick snapshot of the current buildslaves in use, please see the buildbot [waterfall](http://ns-regression.ee.washington.edu:8010/waterfall).

If you would like to see another buildslave, for example mingw or cygwin, and you have a machine to donate daily cycles, please complete the following steps:

- Install buildbot using a package manager or installing from source:
[download](http://buildbot.net/trac/wiki/DownloadInstall) - When creating the buildslave, you will need to provide a slavename and password. Note that you will have to send us this name and password. You also need the hostname and port of our buildmaster: ns-regression.ee.washington.edu:9989
- Follow the buildbot manual to setup a buildslave:
[creating a buildslave](http://buildbot.net/buildbot/docs/0.8.1/Creating-a-buildslave.html) - Send John Abraham <john.abraham@gatech.edu> an email with your buildslave name and password, and we will update the buildmaster configuration to accept connections from your buildslave.

To change the buildmaster master script, edit master.cfg and then 'make reconfig' in the /home/buildmaster/master directory.

To restart buildbot on ns-regression:

su buildmaster cd /home/buildmaster /usr/bin/buildbot start master
