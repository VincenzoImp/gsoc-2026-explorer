# User FAQ

**Parent:** The ns-3 Network Simulator Project — Project Ideas
**Source:** https://www.nsnam.org/wiki/User_FAQ
**Scraped:** 2026-02-22T23:28:47.553863

---

# User FAQ

[Jump to navigation](https://www.nsnam.org#mw-head)

[Jump to search](https://www.nsnam.org#searchInput)

[Main Page](https://www.nsnam.org/wiki/Main_Page) - [Roadmap](https://www.nsnam.org/wiki/Roadmap) - [Summer Projects](https://www.nsnam.org/wiki/Summer_Projects) - [Project Ideas](https://www.nsnam.org/wiki/Project_Ideas) - [Developer FAQ](https://www.nsnam.org/wiki/Developer_FAQ) - [Tools](https://www.nsnam.org/wiki/Tools) - [Related Projects](https://www.nsnam.org/wiki/Related_Projects)

[HOWTOs](https://www.nsnam.org/wiki/HOWTOs) - [Installation](https://www.nsnam.org/wiki/Installation) - [Troubleshooting](https://www.nsnam.org/wiki/Troubleshooting) - [User FAQ] - [Samples](https://www.nsnam.org/wiki/Category:Samples) - [Models](https://www.nsnam.org/wiki/Category:Models) - [Education](https://www.nsnam.org/wiki/Education) - [Contributed Code](https://www.nsnam.org/wiki/Contributed_Code) - [Papers](https://www.nsnam.org/wiki/Papers)

This wiki page is devoted to questions for **users** of the simulator. There is a similar [Developer_FAQ](https://www.nsnam.org/wiki/Developer_FAQ) page for ns-3 **software developers and maintainers**.

## What is the difference between ns-2 and ns-3?

[ns-2](http://www.isi.edu/nsnam/ns) is a popular discrete-event network simulator developed under several previous research grants and activities. It remains in active use and will continue to be maintained.

[ns-3](http://www.nsnam.org) is a new software development effort focused on improving upon the core architecture, software integration, models, and educational components of ns-2. The project commenced in July 2006 and the first release was made on June 30, 2008.

## Will ns-2 scripts run on ns-3?

No. ns-2 uses OTcl as its scripting environment. ns-3 uses C++ programs or python scripts to define simulations.

## I found a bug in ns-3. How do I report it?

Please consult [this page](http://www.nsnam.org/support/report-a-bug/). Also, please consider fixing the bug, not just reporting it :)

### Bug Priorities

Bugs may be assigned a priority ranging from one to five, and a severity ranging from Blocker to Enhancement. There is typically a correlation between priority and severity in our scheme, but it is possible to mix and match as described below.

The maintainers usually will adjust priorities/severities once the bug is filed, so do not worry too much about initially assigning something here (defaults are fine).

The highest priorities are assigned by the maintainers to identify critical path issues for upcoming releases. In every release cycle, the maintainers evaluate the list of bugs and promote certain of these bugs to P1 or P2. This places them directly on the critical path for a given release, and they must be fixed before that release can go forward.

- P1 -- The most severe bugs that will block the upcoming release of ns-3 if they are not fixed.
- P2 -- Very serious bugs that, for some reason, cannot be fixed in the upcoming release.

The severities which typically correspond to P1 and P2 bugs are:

- Blocker -- The most severe bugs that will block the upcoming release of ns-3 if they are not fixed.
- Critical -- Very serious bugs that, for some reason, cannot be fixed in the upcoming release.

The priorities P1 and P2, along with the corresponding severities, Blocker and Critical, are only set by ns-3 maintainers. P1 bugs should always be labeled as blockers, and P2 should always be critical, and vice versa.

In general, if a bug is an error in the implementation or could conceivably cause erroneous simulation results for unsuspecting users, it should be labeled at least P2. Users who are not maintainers should enter bugs at most at P3/Major level. These can be raised to P2 or P1 level by maintainers, once confirmed.

The remaining priorities which developers and users can assign are:

- P3 -- The submitter considers this a severe bug that impacts the usefulness of the system to him or her. No workaround is available.
- P4 -- The submitter considers this a serious bug, but can work around it in some way.
- P5 -- The default priority level chosen by Bugzilla, which represents an unassigned or very low priority, i.e. nice to have.

In addition to a priority, a bug submitter has the opportunity to add a severity:

- Major -- The submitter is saying that he or she is blocked and has no workaround.
- Normal -- The submitter considers this a serious bug, but can work around the problem in some way.
- Minor -- Does not affect the functionality of the product, but something is strange or unexpected.
- Trivial -- Does not affect the functionality of the product. A typo in documentation, for example.
- Enhancement -- There is no broken functionality, but a request for a product enhancement.

Typically one would expect Major severity to be associated with P3 bugs, Normal severity to be associated with P4 bugs, and Minor or Trivial Severity to be associated with P5 bugs. However, there is some flexibility. For example, a user can have a Major severity problem that prevents him or her from proceeding with a certain task, but that task is a low priority. In this case, you could file a P4 Major bug, indicating that the workaround is, well, to not work on it for a while. It is conceivable to have a P3 Trivial bug as well. This could be a piece of documentation that misleads users into very difficult situations, for example.

Enhancement severity can reasonably accompany any priority level. For example, a nice to have thing that would make your life slightly better could be seen as a P5 Enhancement. A piece of functionality missing in ns-3 that prevents you from doing your work could be easily seen to be a P3 Enhancement. Maintainers could eventually decide that a missing piece of functionality is so important that it needs to be a P1 Enhancement that blocks the next release unless it is added.

Users who are not maintainers should enter bugs at most at P3/Major level. These can be raised to P2 or P1 level by maintainers, once confirmed.

Use your judgment in entering these priorities and severities.

## Downloading ns-3

### Download a stable release

ns-3 makes unpackaged source releases only at this time. Downloading the latest stable release should be straightforward, from the [main project page](http://www.nsnam.org). Archived older releases are also linked there.

### Download the development tree

Some people may want to work with our development branch, which is ns-3-dev. We've introduced a framework to ease working with the development version. It is called ns-3-allinone. As of early January 2009, downloading of optional components to ns-3 has been delegated to a download script in this ns-3-allinone framework.

Using the development tree requires mercurial. Try the following steps:

hg clone[http://code.nsnam.org/ns-3-allinone]cd ns-3-allinone ./download.py

You should then have the following directory structure in ns-3-allinone/

build.py* dist.py* ns-3-dev/ pybindgen/ util.py constants.py download.py* nsc/ README

Users will want to then invoke build.py to start a coordinated build.

./build.py

If all goes well, one can cd into ns-3-dev and run the ns-3 tests:

cd ns-3-dev ./test.py

## Upgrading ns-3

ns-3 makes releases about three times per year. ns-3 is not integrated into the various package management systems (yum, apt-get, ports) and just makes source tarball releases (although some people have expressed interest in making and publishing packages in the future).

For now, if you are working with a previous release (e.g. ns-3.17) and wish to upgrade to the newer release (e.g. ns-3.18), you will need to patch your code using the Unix *patch* tool.

### Upgrading ns-3 by itself

As a new release is made, you can create a patch as follows. We'll use ns-3.17 to ns-3.18 as an example.

- download and extract ns-allinone-3.17 and ns-allinone-3.18
- copy the ns-3.17 and ns-3.18 directories to some temporary workspace
- assuming that ns-3.17/ and ns-3.18/ directories are side by side, you can issue the following command:

diff -Naur ns-3.17 ns-3.18 > ns-3.17-to-ns-3.18.patch

Now, if you have some code based on ns-3.17 that you wish to upgrade, you can apply the patch. It is **highly recommended** that you try this on a copy of your code in case the patch does not apply cleanly and you need to do manual edits.

For example, let's assume that your ns-3.17-based directory is called *ns-3.17-my-code*. You can try this:

- copy ns-3.17-my-code to a temporary workspace
- create or obtain the patch for upgrading
- cd into your copy of ns-3.17-my-code
- copy the patch file there
- issue the following command:

patch -p1 -i ns-3.17-to-3.18.patch

Patch also allows you to do a dry run before you apply changes, to see if it will go well. This command is:

patch -p1 -i ns-3.17-to-3.18.patch --dry-run

In some cases, if you have changed code around where the patch is trying to make changes, the merge will not be successful and you will be left with reject files that you will need to manually take care of. This [link](http://elinux.org/Handling_Patch_Rejects) describes in general how to handle that case.

### Upgrading ns-3 and Python bindings

If you want to use Python bindings (which use pybindgen) or NetAnim, you should probably upgrade those packages too. They are typically published in the *ns-allinone* tarball.

If you just upgrade ns-3 without upgrading pybindgen, you will not be able to use python bindings in your new code.

Here is one way you can attempt this upgrade (ns-3.17 to ns-3.18 is used for sake of example here):

- download the new ns-allinone-3.18.tar.bz2 and unpack it
- patch your code (as described above)
- copy the patched ns-3 directory into the new ns-allinone-3.18 directory. It should then be able to find the updated python bindings

### Available patches

Available patches are posted in the [patches](http://www.nsnam.org/release/patches) directory.

## Mercurial

### merging a separate repository with a main repository

Q. I want to incorporate some code from a mercurial branch (repository) that is off the main repository.

A. (from Mathieu Lacage)

You can create a local clone of the repository and pull into it from the main repository: you can push these yourself by creating a local clone of that repo and then pushing it back to the main repo. It will keep the original history; e.g.:

hg clone http://code.nsnam.org/mathieu/ns-3-ptr cd ns-3-ptr # merge from main ns-3 repository into this other repository hg pull http://code.nsnam.org/ns-3 hg merge

Pushing this new merged repository into another repository will then keep the original change history:

# push back-- must have privileges to push to the repository hg push ssh://code@code.nsnam.org/repos/ns-3

### working with subsets of repositories

Q. Is there a way with mercurial to pull/merge/push subsets of the repositories? For instance, suppose I wanted only to grab the samples directory from a repo and merge that alone.

A. (from Mathieu Lacage) You cannot cherry-pick individual changesets other than by exporting
them to patches first. The reason is that each Changeset contains a
single hash which is, among others, based on the hash of the 'parent'
changeset hash. So, if you 'reparent' a changeset, you change its hash
id because the id of the parent changes. If the hash id of a changeset
changes, it is a different changeset so, mercurial cannot really manage
these individual changesets. There is, however, the [transplant extension](http://www.selenic.com/mercurial/wiki/index.cgi/TransplantExtension) that lets you do just that.

So, the idea is that merging happens from one repo to another, and cannot be done on a sub-dir basis. The other alternatives are:

1) the latest mercurial has support for in-repo branches: you can maintain multiple branches within a single repository but each branch represents a branch for the whole repository.

2) the latest mercurial contains the [forest extension](http://www.selenic.com/mercurial/wiki/index.cgi/ForestExtension) which is a way
to make mercurial manage a 'forest' of repos: each repo is independent
but they also behave as a single big repo through the forest extension.

## WAF (build process)

See also the [WAF developers FAQ](http://www.nsnam.org/wiki/index.php/Developer_FAQ#The_WAF_build_system)

### How to build NS-3

First choose the debug level that you want. To select the debug level, you have to *configure* NS-3 first with the command:

./waf configure -d debuglevel

Where *debuglevel* is one of:

*debug*(the default): builds NS-3 with the most suited options for debugging. This includes disabling of all optimization, since it confuses the debugger and makes debugging very difficult. It also activates NS-3 internal assertions to catch all programming errors, as well as enabling support for debugging messages (NS_DEBUG and NS_DEBUG_UNCONDITIONAL). This mode should be used initially for development, until you are happy that the code runs correctly and does not contain any serious programming mistake.*optimized*: this compiles NS-3 with optimization, but disabled assertions and debugging messages. Use this when the program is correct and you just want to extrat results.

It is also possible to customize the C compilation flags through the CXXFLAGS environment variable. Example:

CXXFLAGS='-O3' ./waf configure -d optimized

See [here](http://code.google.com/p/waf/wiki/EnvironmentVariables) for a list of additional environment variables that can be used to control waf configure. After configuration, NS-3 can be built with the command:

./waf build

[ The waf command *build* can be omitted, since it is the default command. ]

**WARNING**: even though the -d option is accepted outside "waf configure", it is completely ignored unless applied together with the configure command.

### How to run NS-3 programs

First, the builtin NS-3 [unit tests](http://en.wikipedia.org/wiki/Unit_test) can be executed (from the top-level directory in the distribution) with the command:

./test.py

To run the remaining programs, there are three different ways to do it.

- The hard way: because NS-3 is built as a set of shared library (dll) files, it requires you to manually configure LD_LIBRARY_PATH, PATH, or DYLD_LIBRARY_PATH, depending on your platform, to make them point to each ns-3 module directory. Only then can you run the programs that were built as
`build/<debuglevel>/path/to/program`

. - Easy way #2: run
`./waf shell`

. You will then have a new nested shell from which programs can be run, e.g.`gdb ./build/debug/examples/simple-p2p`

. - Easy way #1:
`./waf --run programname`

, or`./waf --run "programname args"`

. To find out available program names, run`./waf --run non-existent-program-name`

.

### How to run NS-3 programs under another tool

For running ns-3 programs with gdb or valgrind, try the following:

- Use the "command-template" argument; e.g.
`waf --run csma-cd-one-subnet --command-template="gdb %s"`

`waf --run csma-cd-one-subnet --command-template="valgrind %s"`


- To run the unit tests (waf --check) under gdb:
`./waf --command-template="gdb %s" --run run-tests`



### How to configure cygwin

cygwin works reasonably-well by default: just make sure you grab the cygwin installer from [http://www.cygwin.com/setup.exe](http://www.cygwin.com/setup.exe)
cygwin includes support for mercurial, gcc, and, python so, nothing else should be needed.

### How to configure mingw

mingw requires more work than cygwin to setup. You need to grab:

- the core mingw system:
[http://downloads.sourceforge.net/mingw/MinGW-5.1.4.exe](http://downloads.sourceforge.net/mingw/MinGW-5.1.4.exe) - python:
[http://www.python.org/ftp/python/2.5.2/python-2.5.2.msi](http://www.python.org/ftp/python/2.5.2/python-2.5.2.msi)

Since msvc cannot build ns-3, you need to tell WAF to use your mingw g++ compiler instead: `waf configure --check-cxx-compiler=g++`

will do this

You might need additional packages, depending on your needs:

- the
[msys shell](http://downloads.sourceforge.net/mingw/MSYS-1.0.10.exe). Warning: you should not use the msys terminal, as it[does not play well with native windows binaries](http://www.nabble.com/Interactive-mode-in-MSYS-shell-tt9706332.html#a9706463), such as Python. Just put the path to the msys binaries in the system PATH environment variable (My Computer -> Properties -> Advanced), but _do NOT_ run the msys terminal. Instead, run a plain old Windows terminal; [mercurial](http://downloads.sourceforge.net/tortoisehg/TortoiseHg-0.4.1.exe). You will need this if you plan to use mercurial.

Note: under mingw, all regression tests are known to fail. The developers have not had the time yet to investigate the reasons for those failures.

### How to run programs with gdb

It's not very hard:

- First, setup your environment variables:
`./waf --shell`

- Then, run your program with gdb:
`gdb ./build/src/csma/examples/ns3-dev-csma-broadcast-debug`


## Python bindings

Questions about how to use Python with ns-3? See [ns-3 python wiki page](http://www.nsnam.org/wiki/index.php/NS-3_Python_Bindings)
