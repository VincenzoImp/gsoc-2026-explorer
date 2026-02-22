# https://gcc.gnu.org/git.html

**Parent:** GNU Compiler Collection (GCC) — Project Ideas
**Source:** https://gcc.gnu.org/git.html
**Scraped:** 2026-02-22T23:28:47.608878

---

Our Git source repository is available read-only to the public at large. That way you can pick up any version (including releases) of GCC that is in our repository.

In addition, you can
[browse our
Git history online](https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git).

(Our [web pages are managed via Git in a
separate repository](https://gcc.gnu.org/about.html#git).)

Assuming you have
[Git](https://git-scm.com/) installed, you can
check out the GCC sources using the following command:


`git clone https://gcc.gnu.org/git/gcc.git SomeLocalDir`


If there is another local repository accessible you can avoid
re-downloading everything by using `--reference`

, e.g.

`git clone --reference original-gcc --dissociate https://gcc.gnu.org/git/gcc.git new-gcc`


But if you own this other copy, you probably want to use
separate [worktrees](https://gcc.gnu.org#worktrees) instead of multiple clones.

Our source tree contains a number of files that are generated
from other source files by build tools such as Bison, Autoconf, and
Gperf. Bison is now required when using Git to access our sources,
but all other generated files are included in the source tree so that
GCC can be built without these build tools. The Git checkout and
update operations do not insure that the timestamps of generated files
are later than those of the files they are generated from. The script
`contrib/gcc_update`

updates the timestamps for all these
generated files. See the comments in that script for instructions on
running it.

GCC's build system (in particular Make) uses file timestamps to
determine if a generated file needs to be updated by running a particular
build tool. Because of this, GCC's build system may believe that
a generated file needs regenerating even though its source has not
changed, and require a particular build tool to rebuild that generated
file. If the appropriate build tool is installed on your system, then
this will not be a problem. If you do not intend to make changes to
the source, you can avoid installing these build tools by running
`contrib/gcc_update`

.

There has been some discussion of removing these generated files from GCC's Git source tree (there is no discussion of removing them from the released source tarballs). If that happens then building GCC from the Git source tree would require installing the above mentioned build tools. Installing these build tools is not particularly difficult, but can be time consuming especially if you only occasionally install GCC on a particular system.

The build tools that GCC uses are all available from the GNU
Project (see [https://www.gnu.org](https://www.gnu.org)),
are often already available on many systems, and can often be found
already built for some systems. A partial list of these build tools
is: Autoconf, Bison, Xgettext, Automake, and Gperf.

`git pull`

It is not uncommon to get Git conflict messages for some generated files when updating your local sources from the Git repository. Typically such conflicts occur with autoconf generated files. Such an error is of the form:

error: Your local changes to the following files would be overwritten by merge: gcc/configure Please commit your changes or stash them before you merge. Aborting

As long as you haven't been making modifications to the generated files
or the generator files, it is safe to revert the local differences
using `git checkout`

on the affected files, then run
`git pull`

again.

If you have changes you want to keep that result in such an error,
there are a few options. You can keep those changes on a local branch
rather than on a branch tracking upstream sources. If you wish to
keep those changes uncommitted, do `git stash`

before `git pull`

and `git stash pop`

after `git pull`

. If you commit them directly to your
local upstream-tracking branch, you may prefer to use ```
git pull
--rebase
```

instead of plain `git pull`

.

A branch called *branchname* can be checked out with the
following command:


`git checkout`

branchname

(The release branch of the GCC *SERIES* release series
is named `releases/gcc-`

.)*SERIES*

Similarly a tag called *tagname* can be checked out with the
following command:


`git checkout`

tagname

(The Git tag for GCC *X*.*Y*.*Z* is of the form
`releases/gcc-`

. Under the
release numbering scheme used for GCC 5 and later release
series, *X*.*Y*.*Z**Y* is always nonzero and *Z* is always zero for
a release, with other version numbers being used for development
versions.)

The following are some representative examples:

- releases/gcc-10 (a branch)
- releases/gcc-9 (a branch)
- releases/gcc-9.3.0 (a tag)
- releases/gcc-4.9 (a branch)
- releases/gcc-4.9.0 (a tag)

To get a list of available branches, after checking out any branch, use the command:


`git branch -a`


Similarly, to list tags:


`git tag -l`


To view logs for a branch only up to the point at which it was
created, use the command `git log origin/`

; for example:
*branchname*
^origin/*parentbranchname*


`git log origin/releases/gcc-9 ^origin/master`


Git allows you to share the git object repository between multiple working directories, each tracking a different branch. For instance, to create a worktree for a release branch, do

To create a worktree for a new project branch based on master, dogit worktree add ../gcc-9 releases/gcc-9

git worktree add -bproject../project master

By default, a `git clone`

operation will only fetch the
main development, release branches and their associated tags from the
server. This will be sufficient for most users, but a number of
additional branches can also be fetched if necessary.

The following areas exist on the server:

*refs/heads/master*- The active development version of the compiler.*refs/heads/releases/**- Release branches.*refs/heads/devel/**- topic-specific development branches - see[Active Development Branches](https://gcc.gnu.org#devbranches). Branches and tags in this space may be moved to refs/dead once active development is completed or abandoned.*refs/tags/**- tags for all of the above branches.*refs/vendors/*/{heads,tags}/**- vendor-specific branches and tags. These are owned and maintained by the respective vendor, but made available publicly. Non-fast-forward pushes are permitted on these branches.*refs/users/*/{heads,tags}/**- personal developer branches and tags. These are owned and maintained by the individual developer. Non-fast-forward pushes are permitted on these branches.*refs/dead/heads/**- completed or abandoned development branches.*refs/meta/config*- local configuration data for the commit hooks on the server.*refs/deleted/*/{heads,tags}/**- old branches and tags from the SVN repository that were deleted before the conversion to git.*refs/git-svn-old/**- various branches and tags from the git-svn pre-conversion git mirror.*refs/git-old/**- various branches and tags from the git-svn pre-conversion git mirror that were local to that git repository.

You can download any of the additional branches by adding a suitable fetch specification to your local copy of the git repository. For example, if your remote is called 'origin' (the default with git clone) you can add the 'dead' development branches by running:

git config --add remote.origin.fetch "+refs/dead/heads/*:refs/remotes/origin/dead/*" git config --add remote.origin.fetch "+refs/dead/tags/*:refs/tags/dead/*" git fetch origin

which will place the dead branches in `remotes/origin/dead`

and the tags in `tags/dead`

.

You can use `git ls-remote`

to get a complete list of
refs that the server holds.

Active development branches have names starting `devel/`

in Git.

- ira-select
- This branch is for work on a new algorithm of calculations of
pseudo register classes. The new algorithm is based on choosing an
insn alternative first and then calculation of pseudo reg class
costs knowing the alternative. The branch is maintained by Vladimir
Makarov
[vmakarov@redhat.com](mailto:vmakarov@redhat.com). [devel/omp/gcc-15](https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;a=shortlog;h=refs/heads/devel/omp/gcc-15)- This branch is for collaborative development of
[OpenACC](https://gcc.gnu.org/wiki/OpenACC)and[OpenMP](https://gcc.gnu.org/wiki/openmp)support and related functionality, such as[offloading](https://gcc.gnu.org/wiki/Offloading)support (OMP: offloading and multi processing). The branch is based on releases/gcc-15. Please send patch emails with a short-hand`[og15]`

tag in the subject line. This branch uses`ChangeLog.omp`

files that are occasionally updated automatically from the commit messages, so please ensure that your commit messages include a valid ChangeLog section. (Stale branches also exist for the prior GCC releases 9 to 14.) - unified-autovect
- This branch is for work on improving effectiveness and generality of GCC's
autovectorization by performing target-aware reordering instruction selection
using unified representation. This branch is maintained by Sameera Deshpande
<
[sameera.deshpande@imgtec.com](mailto:sameera.deshpande@imgtec.com)>.

- power-ieee128
- This branch is for community development of IEEE quad precision floating point for Power ("ieee128"), replacing the "double double" aka "ibm128" implementation we had for long double. The current focus is on Fortran support.

No active branches

- c++-contracts
- This is the sandbox for renewed work on
*contracts for C++*, that didn't make it into C++20. Most of the implementation was contributed by Lock3 Software. It is currently maintained by[Jason Merrill](mailto:jason@gcc.gnu.org). - gccgo
- This branch is for the Go front end to GCC. For more information
about the Go programming language,
see
[go.dev](https://go.dev/). The branch is maintained by Ian Lance Taylor. Patches should be marked with the tag [gccgo] in the Subject line. - modula-2
- This branch is for the
[GNU Modula-2](http://www.nongnu.org/gm2/homepage.html)front end to GCC prior to its integration with the mainline. The branch will be regularly rebased against the mainline. It is maintained by[Gaius Mulley](mailto:gaiusmod2@gmail.com). Patches should be prefixed with`[modula-2]`

in the subject line. - m2link
- This is a short term branch for the
[GNU Modula-2](http://www.nongnu.org/gm2/homepage.html)front end to GCC prior to its integration with the mainline. It contains the new scaffold and driver development. The contents of this branch will be folded back onto the`modula-2`

branch once a significant number of regression tests pass. It is maintained by[Gaius Mulley](mailto:gaiusmod2@gmail.com). Patches should be prefixed with`[m2link]`

in the subject line. - coarray_native
- This branch is for implementation of a shared memory
implementation of Fortran coarrays. It is maintained by
[Nicolas König](mailto:koenigni@gcc.gnu.org). [devel/rust/master](https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;a=shortlog;h=refs/heads/devel/rust/master)-
This branch is for development of
[Rust programming language support in GCC](https://gcc.gnu.org/wiki/RustFrontEnd). - fortran_unsigned
- This branch is for implementation of unsigned integers for Fortran,
an upcoming F202y feature. It is maintained by
[Thomas König](mailto:tkoenig@gcc.gnu.org).

These branches are maintained by organizations distributing GCC.
No changes should be made to those branches without the explicit
permission of the distributing organization. Such branches are
located in the Git repository
under `refs/vendors/`

, which is not
fetched by default; the *vendor*/heads/`heads/`

is omitted from the names
given below.

- apple/local-200502-branch
- This branch is for various improvements in use at Apple and to coordinate work with others. This branch is maintained by the folks at Apple. Previous branch was apple-ppc-branch.
- ARM/embedded-
*x_y*-branch - These branches provide bug-fixes, minor enhancements and stability
fixes for GCC
*x.y*branches when used with ARM's embedded cores, such as the Cortex-R and Cortex-M processors. Most patches will be limited ARM specific or common back-ports from trunk, unlike the current release branches. Very occasionally these branches will hold patches that are waiting for trunk acceptance. Patches for these branches should be marked with the tag`[arm-embedded]`

in the subject line. This family of branches is maintained by personnel from ARM. - google/integration
- This branch contains some minimal patches that are likely not
useful anywhere outside of Google's build environment. These are
typically configuration patches. The branch is maintained by
Diego Novillo
[dnovillo@google.com](mailto:dnovillo@google.com). - google/main
- This branch contains Google local patches that are staged to be
contributed to trunk. Some of these patches are either in the
process of being reviewed, or have not yet been proposed. The
intent of this branch is to serve as a staging platform to allow
collaboration with external developers. Patches in this branch are
only expected to remain here until they are reviewed and accepted in
trunk. This branch is maintained by
Diego Novillo
[dnovillo@google.com](mailto:dnovillo@google.com). - google/gcc-
*x_y* - Google compilers based on GCC
*x.y*releases. This family of branches is maintained by Diego Novillo[dnovillo@google.com](mailto:dnovillo@google.com). - google/gcc-
*x_y[_z]*-mobile - Google compilers based on GCC
*x.y.z*releases. These are used to build Android and ChromeOS. This family of branches is maintained by Ahmad Sharif[asharif@google.com](mailto:asharif@google.com), Han Shen[shenhan@google.com](mailto:shenhan@google.com), and Jing Yu[jingyu@google.com](mailto:jingyu@google.com). - google/gcc-
*x_y[_z]*-mobile-vtable-security - google/gcc-
*x_y[_z]*-mobile-vtable-verification - Google compilers based on GCC
*x.y.z*releases. These are used to build Android and ChromeOS. These branches are for work on function pointer and vtable security. They are maintained by Caroline Tice[cmtice@google.com](mailto:cmtice@google.com). - ibm/gcc-
*x*-branch - Branches that track the GCC branches and are used to create the IBM Advance Toolchain releases. This family of branches is maintained by personnel from IBM.
- linaro/gcc-
*x_y*-branch - Linaro compilers based on GCC
*x.y*releases. These branches only accept backports of patches which have been accepted to trunk. This family of branches is maintained by personnel from Linaro. - redhat/gcc-3_2-branch
- Red Hat GNU/Linux compilers based on GCC 3.2.x.
- redhat/gcc-3_4-branch
- Red Hat GNU/Linux compilers based on GCC 3.4.x.
- redhat/gcc-4_0-branch
- Red Hat GNU/Linux compilers based on GCC 4.0.x.
- redhat/gcc-4_1-branch
- Red Hat GNU/Linux compilers based on GCC 4.1.x.
- redhat/gcc-4_3-branch
- Red Hat GNU/Linux compilers based on GCC 4.3.x.
- suse/gcc-4_1-branch
- SUSE GNU/Linux compilers based on GCC 4.1.x.
- suse/gcc-4_2-branch
- SUSE GNU/Linux compilers based on GCC 4.2.x.
- ubuntu/gcc-4_2-branch
- This branch follows the gcc-4_2-branch, except for gcc/java, boehm-gc, libffi, libjava and zlib, which are backported from the trunk (and from gcc-4_3-branch, once created). The branch is used as the base for the Debian and Ubuntu gcc-4.2 source package.

These branches have been merged to GCC mainline, and are thus
inactive. Inactive branches are under `refs/dead/heads/`

in Git (except for ones under `refs/vendors/`

).

[aarch64/sve-acle-branch](https://gcc.gnu.org/git/?p=gcc-old.git;a=shortlog;h=refs/heads/aarch64/sve-acle-branch)- This
[Git-only branch](https://gcc.gnu.org/wiki/GitMirror)was used for collaborative development of the AArch64 SVE ACLE implementation. The branch is based off and merged with trunk. Please send patches to gcc-patches with an`[SVE ACLE]`

tag in the subject line. There's no need to use ChangeLogs; the ChangeLogs will instead be written when the work is ready to be merged into trunk. The branch is maintained by Richard Sandiford. - ARM/aarch64-branch
- This branch added support for the AArch64 architecture and tracked trunk until the port was merged into mainline.
- alias-improvements
- c-4_5-branch
- cfg-branch
- This branch was created to develop and test infrastructure for easier writing of new RTL based optimizations. The branch was based on GCC pre-3.3 and has been partially merged into the mainline for GCC 3.4. It is now closed, and work continues on the rtlopt-branch.
- cond-optab
- cp-parser-branch
- cp-parser-branch-2
- csl-*-branch
- csl/coldfire-4_1
- cxx0x-branch
- This branch was for the development of C++0x features, and all features developed on this branch have been merged to mainline. Future C++0x features will be developed against mainline. This branch was deleted at revision 152320.
[cxx0x-lambdas-branch](https://gcc.gnu.org/projects/cxx0x.html#lambdas)- This branch was for the development of lambda functions, a coming feature in C++0x. It was merged into the trunk at revision 152318.
- dataflow-branch
- This branch has been merged into mainline on June 6, 2007
as svn revision 125624. It used to contain a replacement of back-end
dataflow with df.c based dataflow. The branch was maintained
by Daniel Berlin <
[dberlin@dberlin.org](mailto:dberlin@dberlin.org)> and Kenneth Zadeck <[zadeck@naturalbridge.com](mailto:zadeck@naturalbridge.com)> - dfa-branch
- dfp-branch
- edge-vector-branch
- fixed-point
- function-specific-branch
- This branch is for development of adding function specific options to
GCC. See the GCC
[wiki](https://gcc.gnu.org/wiki/FunctionSpecificOpt)for a more detailed project description. Patches should be marked with the tag`[function-specific]`

in the subject line. The branch has been merged into GCC 4.4. - gcc-3_4-basic-improvements-branch
- gcc-3_4-e500-branch
- This branch was for stabilization of the powerpc-*spe architecture, and for adding support for the 8548 chip (e500 v2). This branch was maintained by Aldy Hernandez. All the e500 support was merged to mainline.
- gcj-abi-2-dev-branch
- gcj-eclipse-branch
[gimple-tuples-branch](https://gcc.gnu.org/wiki/tuples/)- gomp-20050608-branch
- gomp-3_0-branch
- java-gui-20050128-branch
- This was a temporary branch for development of java GUI libraries (AWT and Swing) in the libjava directory. It has been merged into mainline.
- killloop-branch
- The missing optimizations and optimization improvements necessary for removing the old loop optimizer were developed on this branch. Most of these changes were merged in 4.2.
[lno-branch](https://gcc.gnu.org/projects/tree-ssa/lno.html)- A sub-branch of tree-ssa that aims at implementing a loop nest optimizer at the tree level. Was largely merged into mainline, and is currently unmaintained. This work now continues on the autovect-branch.
[mem-ref2](https://gcc.gnu.org/wiki/MemRef)- mips-3_4-rewrite-branch
- named-addr-spaces-branch
- This branch was the development branch to add named address space support
for architectures that have multiple address spaces. The CELL/spu architecture
adds an
`__ea`

keyword to describe extended memory in the host chip address space instead of the local CELL/spu address space. The branch was created by Ben Elliston, modified by Michael Meissner and eventually maintained by[Ulrich Weigand](mailto:Ulrich.Weigand@de.ibm.com). All changes from this branch were merged into mainline. - microblaze
- This branch contained support for updating the Xilinx MicroBlaze
architecture to GCC 4.1.2.
It was created by Michael Eager
<
[eager@eagercon.com](mailto:eager@eagercon.com)>. All changes have been merged into mainline. - pch-branch
[tree-ssa-20020619-branch](https://gcc.gnu.org/projects/tree-ssa/)[var-tracking-assignments*-branch](https://gcc.gnu.org/wiki/Var_Tracking_Assignments)- predcom
- This branch aimed to implement predictive commoning optimization and to introduce the changes to the representation of Fortran arrays, alias analysis and dependency analysis to make it useful for the common applications (e.g., mgrid). The branch was merged in 4.3.
- split
- For development of stack splitting, as described
on
[the GCC wiki](https://gcc.gnu.org/wiki/SplitStacks). This branch was maintained by Ian Lance Taylor. All changes were merged into mainline. - tr29124
- This branch is for development of TR29124 Special math Functions,
for the C++ runtime library
See
. It is maintained by Ed Smith-Rowland <[3dw4rd@verizon.net](mailto:3dw4rd@verizon.net)>. - tree-cleanup-branch
- This branch contained improvements and reorganization to the tree optimizers that were not ready in time for GCC 4.0. The goal was to cleanup the tree optimizers and improve the sequencing of the passes. It has now been merged into mainline for the 4.1 release.

These branches are inactive and contain work that might not been merged.

- arc-20081210-branch
- The goal of this branch is to make the port to the ARCompact architecture available. This branch is maintained by Joern Rennecke during spring 2009, and is expected to be unmaintained thereafter.
- ARM/hard_vfp_4_4_branch
- This branch contains support for the hard-VFP variant of the AAPCS calling standard and tracked gcc-4.4 development. This branch was maintained by Richard Earnshaw.
- addressing-modes
- This branch aimed to clean up the way base and index registers are handled by target headers. In particular, the strict and non-strict meaning of these registers are unified and a common API is presented to implementations of the target macros. Obsolete target macros will also be removed. The branch was maintained by Paolo Bonzini. It is no longer maintained.
- alias-export
- This branch contains the alias export and data dependency export patch.
It is used to experiment with the propagation process. This branch is maintained
by Andrey Belevantsev
[abel@ispras.ru](mailto:abel@ispras.ru). - annotalysis
- This branch contains the implementation of thread safety annotations
and analysis (
[https://gcc.gnu.org/wiki/ThreadSafetyAnnotation](https://gcc.gnu.org/wiki/ThreadSafetyAnnotation)). The branch was maintained by[Delesley Hutchins](mailto:delesley@google.com). - apple-ppc-branch
- This branch was for various improvements in use at Apple and to coordinate work with others. This branch was maintained by the folks at Apple. It has been superseded by apple-local-200502-branch.
[ast-optimizer-branch](https://gcc.gnu.org/projects/ast-optimizer.html)- The purpose of this branch was to improve GCC's tree based optimizations. The patches of this branch have been moved to the tree-ssa-20020619-branch.
- autovect-branch
- This branch is the successor to the lno-branch. The purpose of this
branch is tree-level
[autovectorization](https://gcc.gnu.org/projects/tree-ssa/vectorization.html)work, and related work that the autovectorizer could use or benefit from (like data-dependence analysis,[loop nest optimizations](https://gcc.gnu.org/projects/tree-ssa/lno.html)). - avx512
- The goal of this branch is to implement Intel AVX-512 and SHA
Programming Reference.
The branch is maintained by Yukhin Kirill <
[kirill.yukhin@intel.com](mailto:kirill.yukhin@intel.com)>. Patches should be marked with the tag`[AVX512]`

in the subject line. - avx-512vlbwdq
- The goal of this branch is to implement the Intel AVX-512{VL,BW,DQ}
Programming Reference.
The branch is maintained by Yukhin Kirill <
[kirill.yukhin@intel.com](mailto:kirill.yukhin@intel.com)>. Patches should be marked with the tag`[AVX512]`

in the subject line. - avx2
- The goal of this branch is to implement AVX Programming Reference
(June, 2011). The branch is maintained by
H.J. Lu <
[hjl.tools@gmail.com](mailto:hjl.tools@gmail.com)> and Yukhin Kirill <[kirill.yukhin@intel.com](mailto:kirill.yukhin@intel.com)>. Patches should be marked with the tag`[AVX2]`

in the subject line. - bje-unsw-branch
- This branch was dedicated to some research work by Ben Elliston at the University of New South Wales (UNSW) on transformation phase ordering. It will never merge with mainline, although a selection of patches may be submitted over time. Deleted by revision 152653.
- boehms-gc
- The goal of this branch was to test Boehm's GC feasibility as the
garbage collector for GCC proper. This was a part of Google Summer
of Code project, described in detail
at
[https://gcc.gnu.org/wiki/Garbage_collection_tuning](https://gcc.gnu.org/wiki/Garbage_collection_tuning). The branch was maintained by[Laurynas Biveinis](mailto:laurynas.biveinis@gmail.com). - cell-4_3-branch
- The goal of this branch is to add fixes and additional features required for the Cell/B.E. processor (both PPE and SPE) to GCC 4.3.x. This branch is maintained by Ulrich Weigand.
- cell-4_4-branch
- The goal of this branch is to back-port from mainline fixes and additional features required for the Cell/B.E. SPE processor to GCC 4.4.x. This branch is maintained by Ulrich Weigand. The branch is merged from gcc-4_4-branch.
[cfo-branch](https://gcc.gnu.org/projects/cfo.html)- The goal of this branch was to add a new extension for improving the code size optimization of GCC with code factoring methods (code motion and merging algorithms). It is no longer maintained.
- cilkplus
- This branch was for the development of Cilk Plus language extension support on GCC and G++ compilers. It was maintained by Balaji V. Iyer.
- compile-server-branch
- This branch was aimed at improving compile speed by caching work
done between compilations. The work saved is mainly related to header
file processing. This branch was maintained by Mike Stump and Per Bothner.
Patches were marked with the tag
`[cs]`

in the subject line. [condate-branch](https://gcc.gnu.org/wiki/Condate)- The purpose of this branch is to develop a language for checking control flow graph properties. The code of this branch has not been merged in trunk.
- cxx-conversion
- This branch hosts mini-projects that rewrite parts of the existing
GCC code into C++. Each conversion project will be proposed for
trunk integration independently. The branch is maintained by
[Diego Novillo](mailto:dnovillo@google.com). Patches sent to this branch and discussions related to it should be marked with the tag`[cxx-conversion]`

in the subject line. For details on working with this branch, see the[C++ conversion](https://gcc.gnu.org/wiki/cxx-conversion)page. [cxx-mem-model](https://gcc.gnu.org/wiki/Atomic/GCCMM)- This branch is for the implementation of the C++ memory model.
Patches for this branch should be marked
`[cxx-mem-model]`

in the subject line. The branch is maintained by Aldy Hernandez. [cxx-reflection-branch](https://gcc.gnu.org/projects/cxx-reflection/)- Part of the work on providing support for compile time reflection
in C++ was done in this branch. This branch was maintained by Gabriel
Dos Reis
<
[gdr@integrable-solutions.net](mailto:gdr@integrable-solutions.net)>. It is no longer maintained. [cxx0x-concepts-branch](https://gcc.gnu.org/projects/cxx0x.html#concepts)- This branch contains the beginnings of a re-implementation of Concepts, a likely future feature of C++, using some of the code from the prototype implementation on conceptgcc-branch. It is not currently maintained.
- cygwin-improvements
- This branch is intended as a development and proving grounds for
fixes and enhancements specifically to the Cygwin port of the compiler,
although some of these may touch slightly on MinGW targets as well. It
is maintained by Dave Korn <
[dave.korn.cygwin@gmail.com](mailto:dave.korn.cygwin@gmail.com)> and open to contributions from any interested party; please tag patches with "[cygwin-improvements]" in the title line and post them to the GCC Patches list with a Cc: to that address. [debuglocus](https://gcc.gnu.org/wiki/AndrewMacLeod/debuglocus)- This branch is an experiment to see whether improved debug information
can be maintained throughout the compiler by associating a user decl with an
expression, statement, or insn. The name comes from attempting to utilize
the ever present source location (locus) field to carry the debug info.
Further information can be found on the
[debuglocus](https://gcc.gnu.org/wiki/AndrewMacLeod/debuglocus)wiki page . - dwarf4
- This branch is for support of DWARF-4 features. DWARF-4 is currently under development, so changes on this branch will remain experimental until Version 4 is officially finalized.
- faster-compiler-branch
- This was a temporary branch for compiler speedups for GCC 3.4.
See
[this thread](https://gcc.gnu.org/ml/gcc/2002-08/msg00498.html)for discussion of possible work still to be done in this area. The branch is unmaintained at present. - fortran-caf
- This branch contained experimental changes to the Fortran front end for
implementing the library calls for coarray communication. It was
maintained by Tobias Burnus
<
[burnus@gcc.gnu.org](mailto:burnus@gcc.gnu.org)>. - fortran-dev
- This branch was for disruptive changes to the Fortran front end,
especially for OOP development and
the
[array descriptor update](https://gcc.gnu.org/wiki/ArrayDescriptorUpdate). It was maintained by Jerry DeLisle <[jvdelisle@gcc.gnu.org](mailto:jvdelisle@gcc.gnu.org)>. - fortran-exp
- This branch contained experimental changes to the Fortran front end, initially
for array constructor refactoring using splay-tree and other areas of
optimization. It was maintained by Jerry DeLisle
<
[jvdelisle@gcc.gnu.org](mailto:jvdelisle@gcc.gnu.org)>. - gcc-3_3-e500-branch
- This branch was for backporting the PowerPC/E500 back end to GCC 3.3.
See
[this message](https://gcc.gnu.org/ml/gcc/2003-04/msg00733.html)for details. - gcc-4_4-plugins
- This branch is for backporting the plugin functionality into a 4.4-based release. There will be no new code or functionality added to this branch. It is maintained by Diego Novillo. Only patches backported from mainline are accepted. They should be marked with the tag [4_4-plugins] in the Subject line.
- gcc-in-cxx
- This branch was for converting GCC to be written in C++. The branch was maintained by Ian Lance Taylor.
- gcjx-branch
- This branch was used for development of gcjx, a rewrite of the front end for the Java programming language. It has been superseded by gcj-eclipse-branch.
- gc-improv
- This branch is for the development of garbage collector
improvements. It is the successor to the boehm-gc branch, but
without integration with Boehm's GC. The branch is maintained
by
[Laurynas Biveinis](mailto:laurynas.biveinis@gmail.com). Patches for this branch should be marked with the tag`[gc-improv]`

in the subject line. - gimple-front-end
- This branch implements a front end for GIMPLE. It is maintained
by
[Diego Novillo](mailto:dnovillo@google.com). Patches should be prefixed with`[gimplefe]`

in the subject line. See the[GIMPLE Front End](https://gcc.gnu.org/wiki/GimpleFrontEnd)page for details. [graphite-branch](https://gcc.gnu.org/wiki/Graphite)- The purpose of this branch is to develop an infrastructure for loop transforms using the polyhedral model.
- gomp-01-branch
- gomp-branch
- These two branches were initial attempts to implement
OpenMP support in GCC. They were never properly maintained and
have now been superseded by
`gomp-20050608-branch`

. - gomp-4_0-branch
- This branch was based on gcc-6-branch, and was used to update
the
[OpenMP support](https://gcc.gnu.org/wiki/openmp)to version 4.0, including development of[offloading support](https://gcc.gnu.org/wiki/Offloading)in GCC as well as support for[OpenACC](https://gcc.gnu.org/wiki/OpenACC). These features got merged into trunk. The branch was then used for on-going development of OpenACC support and related functionality, which subsequently moved to openacc-gcc-7-branch and then openacc-gcc-8-branch (both now also inactive, see below). [gupc](https://gcc.gnu.org/projects/gupc.html)- This branch implements support for UPC (Unified Parallel C).
UPC extends the C programming language to provide support for
high-performance, parallel systems with access to a single
potentially large, global shared address space.
Further information can be found on the
[GNU UPC](https://github.com/Intrepid/GUPC)page. - openacc-gcc-7-branch
- openacc-gcc-8-branch
- openacc-gcc-9-branch
- These branches were used for development of
[OpenACC support](https://gcc.gnu.org/wiki/OpenACC)and related functionality, based on gcc-7-branch, gcc-8-branch, and gcc-9-branch respectively. [devel/omp/gcc-9](https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;a=shortlog;h=refs/heads/devel/omp/gcc-9)[devel/omp/gcc-10](https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;a=shortlog;h=refs/heads/devel/omp/gcc-10)[devel/omp/gcc-11](https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;a=shortlog;h=refs/heads/devel/omp/gcc-11)[devel/omp/gcc-12](https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;a=shortlog;h=refs/heads/devel/omp/gcc-12)[devel/omp/gcc-13](https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;a=shortlog;h=refs/heads/devel/omp/gcc-13)[devel/omp/gcc-14](https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;a=shortlog;h=refs/heads/devel/omp/gcc-14)- These branches were used for collaborative development of
[OpenACC](https://gcc.gnu.org/wiki/OpenACC)and[OpenMP](https://gcc.gnu.org/wiki/openmp)support and related functionality as the successors to openacc-gcc-9-branch after the move to Git. The branches were based on releases/gcc-9, releases/gcc-10, etc. Development has now moved to the devel/omp/gcc-15 branch. - hammer-3_3-branch
- The goal of this branch was to have a stable compiler based on GCC 3.3
with improved performance for AMD's 64-bit Hammer CPUs. The branch was
maintained by Jan Hubicka <
[jh@suse.cz](mailto:jh@suse.cz)> and Andreas Jaeger <[aj@suse.de](mailto:aj@suse.de)>. Patches added on this branch might not be appropriate for the GCC 3.3 branch due to our policies concerning release branches. All patches were added to mainline GCC (for 3.4). - ia64-fp-model-branch
- This branch was a development branch with the goal of
implementing the improvements and features discussed at the
[ia64 floating point](https://gcc.gnu.org/wiki/ia64_floating_point)page on the[GCC wiki](https://gcc.gnu.org/wiki/). It was maintained by Zack Weinberg <[zack@codesourcery.com](mailto:zack@codesourcery.com)>. It is no longer maintained. - ia64-improvements
- The goal of this branch was to improve the performance of binaries
generated with GCC on the Itanium processor. Details can be found at the
[IA-64 improvements](https://gcc.gnu.org/projects/ia64.html)page. This branch was maintained by Robert Kidd <[rkidd@crhc.uiuc.edu](mailto:rkidd@crhc.uiuc.edu)> and Diego Novillo. It is no longer maintained. - ibm/power7-tmp
- This branch was used to stage patches for Power7 (PowerPC ISA 2.06)
from the development branch to the mainline. The branch was maintained by
Michael Meissner,
[meissner@linux.vnet.ibm.com](mailto:meissner@linux.vnet.ibm.com). - improved-aliasing-branch
- This branch contains improvements to the tree-based aliasing
infrastructure. The branch was maintained by Daniel Berlin <
[dberlin@dberlin.org](mailto:dberlin@dberlin.org)> and Diego Novillo <[dnovillo@redhat.com](mailto:dnovillo@redhat.com)>. It is no longer maintained. - ix86/avx
- The goal of this branch is to implement Intel AVX (Intel Advanced
Vector Extensions). The branch is maintained by
H.J. Lu <
[hjl.tools@gmail.com](mailto:hjl.tools@gmail.com)>. Patches should be marked with the tag`[AVX]`

in the subject line. - insn-select
- This branch aimed to implement in early instruction selection
and register class selection pass, which runs before register allocation
and subsumes the current
`regclass`

pass. In particular the goal is to chose an alternative per instruction, usable as a base during register allocation, which ideally is not changed during reload if registers could be allocated. This will not be possible in all cases, especially when addresses generated during spilling will be invalid on the target machine. But we should be able to do away with fake register classes representing strict unions of other register classes. The branch was maintained by Michael Matz. It is no longer maintained. - ix86/gcc-4_5-branch
- The goal of this branch is to backport support from trunk for
newer ix86 processors from AMD and Intel. It will track
4.5 branch with periodic merge from 4.5 branch. The current
maintainers are Sebastian Pop
<
[sebpop@gmail.com](mailto:sebpop@gmail.com)> and H.J. Lu <[hjl.tools@gmail.com](mailto:hjl.tools@gmail.com)>. - ix86/gcc-4_4-branch
- The goal of this branch is to add support for newer ix86 processors such
as AMD's Shanghai and Intel's Atom to GCC 4.4.x. The current maintainers
are Dwarakanath Rajagopal <
[dwarak.rajagopal@amd.com](mailto:dwarak.rajagopal@amd.com)> and H.J. Lu <[hjl.tools@gmail.com](mailto:hjl.tools@gmail.com)>. - ix86/gcc-4_3-branch
- The goal of this branch is to add support for newer ix86 processors such
as AMD's Barcelona and Intel's Westmere to GCC 4.3.x. The current maintainers
are Dwarakanath Rajagopal <
[dwarak.rajagopal@amd.com](mailto:dwarak.rajagopal@amd.com)> and H.J. Lu <[hjl.tools@gmail.com](mailto:hjl.tools@gmail.com)>. - ix86/gcc-4_2-branch
- The goal of this branch is to add support for newer ix86 processors such
as AMD's Barcelona and Intel's Core 2 to GCC 4.2.x. The current maintainers
are Dwarakanath Rajagopal <
[dwarak.rajagopal@amd.com](mailto:dwarak.rajagopal@amd.com)> and H.J. Lu <[hjl.tools@gmail.com](mailto:hjl.tools@gmail.com)>. - ix86/gcc-4_1-branch
- The goal of this branch is to add support for newer ix86 processors such
as AMD's Barcelona and Intel's Core 2 to GCC 4.1.x. The current maintainers
are Dwarakanath Rajagopal <
[dwarak.rajagopal@amd.com](mailto:dwarak.rajagopal@amd.com)> and H.J. Lu <[hjl.tools@gmail.com](mailto:hjl.tools@gmail.com)>. - java-gui-branch
- This was a temporary branch for development of java GUI libraries (AWT and Swing) in the libjava directory. It has been superseded by java-gui-20050128-branch
- libada-gnattools-branch
- This is the spiritual successor to the libada branch. This branch
exists to solve
[bug 5911](https://gcc.gnu.org/PR5911)and others, by breaking out the Ada runtime into a libada directory and the Ada tools into a gnattools directory. Work was devoted to cleaning up the configure and make machinery, and separating it as much as possible from the GCC build machinery. Nathanael Nerode <[neroden@gcc.gnu.org](mailto:neroden@gcc.gnu.org)> maintained this branch. It is no longer maintained. - libobjc-branch
- The branch is aimed to clean up libobjc and make it run on Darwin.
Patches should be marked with the tag
`[libobjc-branch]`

in the subject line. Patches can be approved by Andrew Pinski <[pinskia@gcc.gnu.org](mailto:pinskia@gcc.gnu.org)> or Nicola Pero <[n.pero@mi.flashnet.it](mailto:n.pero@mi.flashnet.it)>. - libstdcxx_so_7-branch
- This was a branch for experimental work on the C++ Runtime Library
(libstdc++-v3) beyond the current version 6 library ABI. Paolo Carlini
<
[pcarlini@suse.de](mailto:pcarlini@suse.de)> and Benjamin Kosnik <[bkoz@redhat.com](mailto:bkoz@redhat.com)> were maintaining this branch. It is no longer maintained. - libstdcxx_so_7-2-branch
- This branch carries all the C++ Runtime Library (libstdc++-v3) patches
that break its abi. It will be merged into the trunk as soon as the decision
to move to abi version 7 will have been taken. It is maintained by
[François Dumont](mailto:frs.dumont@gmail.com)and the official libstdc++-v3 maintainers Paolo Carlini, Benjamin Kosnik and Jonathan Wakely. Patches will be marked with the tag`[so_7-2]`

in the subject line. - lra
- This branch contains the Local Register Allocator (LRA). LRA is
focused to replace GCC reload pass. The branch is maintained by
Vladimir Makarov
<
[vmakarov@redhat.com](mailto:vmakarov@redhat.com)> and will be merged with mainline from time to time. Patches will be marked with the tag`[lra]`

in the subject line. [lto](https://gcc.gnu.org/wiki/LinkTimeOptimization)- This branch implemented link-time optimization.
- lto-pressure
- This branch is for work on adding analysis to inlining (for LTO in
particular) so that it can avoid inlining things that cause excessive
increases in register pressure. The branch is maintained by Aaron Sawdey
<
[acsawdey@linux.vnet.ibm.com](mailto:acsawdey@linux.vnet.ibm.com)>. - lto-streamer
- This was a sub-branch of the lto branch. It was intended for unstable work related to the conversion from DWARF encoding to GIMPLE streamer. It is no longer maintained.
[lw-ipo](https://gcc.gnu.org/wiki/LightweightIpo)- This branch aims to implement lightweight IPO. Patches
and discussion on this branch should be marked with the tag
`[lipo]`

in the subject line. The branch is maintained by[David Li](mailto:davidxl@google.com). - incremental-compiler
- This branch contains change to turn GCC into an incremental
compiler. The branch is maintained by Tom
Tromey
[tromey@redhat.com](mailto:tromey@redhat.com). Patches for this branch should be marked with the tag`[incremental]`

in the subject line. - melt-branch
- This branch is for
a
[Middle End Lisp Translator](https://gcc.gnu.org/wiki/MiddleEndLispTranslator)branch, including both the plugin Lisp-like facility and static analyzers developed with it. This branch is maintained by Basile Starynkevitch[basile@starynkevitch.net](mailto:basile@starynkevitch.net). Use the`[MELT]`

tag for patches. - mem-ref
- This branch is for lowering the GIMPLE IL for memory accesses to
a flat representation. See the GCC
[wiki](https://gcc.gnu.org/wiki/MemRef)for a more detailed project description. The branch is maintained by Richard Biener. Patches should be marked with the tag`[mem-ref]`

in the subject line. - mem-ssa
- This branch contains the implementation of Memory SSA, a new
mechanism for representing memory operations in SSA form (
[https://gcc.gnu.org/ml/gcc/2006-02/msg00620.html](https://gcc.gnu.org/ml/gcc/2006-02/msg00620.html)). The branch was maintained by Diego Novillo. It is no longer maintained. - milepost-branch
- This branch is for GCC developments done in the Milepost project.
The branch is maintained by Mircea Namolaru
[namolaru@il.ibm.com](mailto:namolaru@il.ibm.com). Patches should be marked with the tag`[mpost]`

in the subject line. [miro-branch](https://gcc.gnu.org/wiki/MIRO)- The purpose of this branch is to develop an improved Mudflap with referent objects. The code of this branch has not been merged in trunk.
- mpx
- The goal of this branch is to support Intel MPX technology.
The branch is maintained by
Ilya Enkovich <
[ilya.enkovich@intel.com](mailto:ilya.enkovich@intel.com)> Patches should be marked with the tag`[MPX]`

in the subject line. - named-addr-4_3-branch
- The goal of this branch was to backport the changes from the named-addr-spaces-branch to a GCC 4.3 tree. This branch was maintained by Michael Meissner. This branch was merged from gcc-4_3-branch.
- new-regalloc-branch
- Daniel Berlin and Michael Matz were working on an implementation of a graph-coloring register allocator on this branch. It is known to bootstrap under x86-linux-gnu and ppc-linux-gnu. It is no longer maintained.
- no-undefined-overflow
- This branch is for tracking overflow behavior on expressions
rather than on types.
Patches should be marked with the tag
`[no-undefined-overflow]`

in the subject line. The branch is maintained by Richard Biener. - objc-improvements-branch
- This branch was originally used to merge Objective-C bug fixes and
enhancements from Apple Computer into the FSF tree; this has now been
completed. A later purpose of the branch was to implement the
Objective-C++ language in the FSF GCC source tree. The message thread
starting
[here](https://gcc.gnu.org/ml/gcc/2003-07/msg00535.html)describes this at more length. This branch was being maintained by Zem Laski <[zlaski@apple.com](mailto:zlaski@apple.com)>. It is no longer maintained. - opt-diary
- This branch contains the implementation of Optimization Diary, a collection of useful log information generated by the optimizers. This branch was maintained by Devang Patel. It is no longer maintained.
- plugin
- This branch contains work for a plugin infrastructure in GCC
to enable additional checking work. This branch is maintained
by Eric Christopher
[echristo@gmail.com](mailto:echristo@gmail.com)and will be merged with mainline from time to time. Patches will be marked with the tag`[plugin]`

in the subject line. [plugins](https://gcc.gnu.org/wiki/plugins)- This branch adds plugin functionality to GCC. See the
[plugins wiki page](https://gcc.gnu.org/wiki/plugins)for details. - pointer_plus
- This branch is for the development of POINTER_PLUS_EXPR. Which
is to be used instead of casting between an integer type and a pointer
type before doing pointer addition. This branch is being maintained
by Andrew Pinski. Patches for this branch should be marked with
the tag
`[PTR-PLUS]`

in the subject line, and CC'ed to[Andrew Pinski](mailto:pinskia@gmail.com). - pph
- This branch implements
[Pre-Parsed Headers for C++](https://gcc.gnu.org/wiki/pph). It is maintained by[Diego Novillo](mailto:dnovillo@google.com)and[Lawrence Crowl](mailto:crowl@google.com). Patches should be prefixed with`[pph]`

in the subject line. - pth-icm
- This is a sub-branch of the
`pph`

branch. It implements[Pre-Tokenized Headers for C++](https://gcc.gnu.org/wiki/pph#Pre-Tokenized_Headers_.28PTH.29). Additionally, it contains instrumentation code in the C++ parser that was used in an incremental compiler model (icm) to study the effects of an incremental compiler cache for a compiler server. The branch is maintained by[Diego Novillo](mailto:dnovillo@google.com)and[Lawrence Crowl](mailto:crowl@google.com). Patches should be prefixed with`[pph]`

in the subject line. - ra-improvements
- This branch aims to implement several improvements to the
current register allocator. Examples include implementing a
lower-triangular conflict matrix and register coalescing.
It is hoped that these improvements will not only help the
current allocator, but will be useful to the other register
allocation projects such as RABLE and YARA. This branch will
be merged with the dataflow-branch from time to time.
The patches for this branch should be marked with the tag
`[ra-improvements]`

in the subject line. The branch is maintained by[Peter Bergner](mailto:bergner@vnet.ibm.com). - redhat/gcc-3_3-branch
- This branch used to hold Red Hat GNU/Linux compilers based on GCC 3.3.x.
- reload-branch
- This branch contains a version of reload in which the tracking of reload register lifetimes and the inheritance code has been rewritten in an attempt to make it more maintainable. It is no longer maintained.
- rtl-fud-branch
- This branch is for the development of factored use-def chains
as an SSA form for RTL. Patches should be marked with the tag
`[rtl-fud]`

in the subject line. The branch is maintained by Steven Bosscher and Kenneth Zadeck. [rtlopt-branch](https://gcc.gnu.org/projects/cfg.html)- This branch was the successor to the cfg-branch, with the exception that it was based on GCC pre-3.4. The purpose of the branch was to develop and test infrastructure for CFG based code improving transformations on RTL.
- scalar-storage-order
- This branch hosts the experimental support to specify a reverse
storage order (byte/word order, aka endianness) for scalar components
of aggregate types. The branch is maintained by
[Eric Botcazou](mailto:ebotcazou@adacore.com)and will be merged with mainline from time to time. Patches will be marked with the tag`[sso]`

in the subject line. - sel-sched-branch
- This branch contains the implementation of the selective scheduling
approach. The goal of the branch is to provide more aggressive scheduler
implementation with support for instruction cloning, register renaming,
and forward substitution. The branch is maintained by Andrey
Belevantsev <
[abel@ispras.ru](mailto:abel@ispras.ru)> and Maxim Kuvyrkov <[mkuvyrkov@ispras.ru](mailto:mkuvyrkov@ispras.ru)> and will be regularly merged with mainline. Patches will be marked with the tag`[sel-sched]`

in the subject line. - spu-4_5-branch
- The goal of this branch was to do development for the Cell/B.E. processor, in particular to support partitioning functions into multiple sections. This branch was created by Michael Meissner and is now maintained by Ulrich Weigand. The branch is merged from mainline.
- stack
- This branch contains a new stack alignment framework to
automatically align stack for local variables with alignment requirement.
The branch is maintained by
H.J. Lu <
[hjl.tools@gmail.com](mailto:hjl.tools@gmail.com)>. Patches should be marked with the tag`[stack]`

in the subject line. - struct-reorg-branch
- This branch is for the development of structure reorganization optimizations, including field reordering, structure splitting for trees. These optimizations are profile information driven. This is a subbranch of tree-profiling. This branch is being maintained by Caroline Tice, Dale Johannesen, Kenneth Zadeck, Stuart Hastings, Mostafa Hagog.
[sched-treegion-branch](https://gcc.gnu.org/projects/sched-treegion.html)- This branch was for the development of a treegion-based instruction scheduler. The branch was maintained by Chad Rosier. It is no longer maintained.
- ssaupdate-branch
- This branch served to clean up and improve utilities for the SSA form updating, as well as for related changes of the SSA form representation. Most of the changes in this branch were never merged. Part of them were incorporated in Diego Novillo's SSA updating improvement patch.
[stree-branch](https://gcc.gnu.org/projects/strees/index.html)- This branch was for improving compilation speed and reducing memory
use by representing declarations as small flat data structures whenever
possible, lazily expanding them into full trees when necessary. This
branch was being maintained by Matt Austern, Robert Bowdidge, Geoff
Keating, and Mike Stump. Patches were marked with the tag
`[stree]`

in the subject line. - structure-aliasing-branch
- This branch contains improvements to the tree optimizers ability to do pointer-to-structure aliasing analysis and optimization. This involves some significant rework of the way our memory information is represented in the tree-ssa form. The branch was maintained by Daniel Berlin. It is no longer maintained.
[st/cli-be](https://gcc.gnu.org/projects/cli.html)- The goal of the branch is to develop a back end producing CLI binaries,
compliant with ECMA-335 specification.
This branch was originally maintained by Roberto Costa
<
[robsettantasei@gmail.com](mailto:robsettantasei@gmail.com)>. Since May 2007, the current maintainers are Andrea Ornstein <[andrea.ornstein@st.com](mailto:andrea.ornstein@st.com)> and Erven Rohou <[erven.rohou@st.com](mailto:erven.rohou@st.com)>. - thread-annotations
- This branch contained the implementation of thread safety annotations
and analysis (
[https://gcc.gnu.org/wiki/ThreadSafetyAnnotation](https://gcc.gnu.org/wiki/ThreadSafetyAnnotation)). It was superseded by the[annotalysis branch.](https://gcc.gnu.org#annotalysis) [transactional-memory](https://gcc.gnu.org/wiki/TransactionalMemory)- This branch is for the development of transactional memory support
for GCC. Patches for this branch should be marked
`[trans-mem]`

in the subject line. The branch is maintained by Richard Henderson. [tree-profiling-branch](https://gcc.gnu.org/projects/tree-profiling.html)- This branch was for the development of profiling heuristics and profile based optimizations for trees, such as profile driven inline heuristics. Another goal of this branch was to demonstrate that maintaining the CFG and profile information over expanding from GIMPLE trees to RTL is feasible and can bring considerable performance improvements. It is no longer maintained.
- tree-ssa-cfg-branch
- This branch has been merged into the tree-ssa-20020619-branch.
- ubsan
- This branch contains the Undefined Behavior Sanitizer (ubsan). Ubsan is
an undefined behavior detector for the C family of languages. The branch is
maintained by Marek Polacek
<
[polacek@redhat.com](mailto:polacek@redhat.com)> and will be merged with mainline from time to time. Patches will be marked with the tag`[ubsan]`

in the subject line. - var-mappings-branch
- This branch is for improving debug information based on tracking
multiple variables per computed value. The branch is maintained by
Richard Biener and Michael Matz. Patches should be marked with the
tag
`[varmap]`

in the subject line. - var-template
- This branch is for implementation work on
*variable template for C++*. It was originally created by Gabriel Dos Reis. It is maintained by[Jason Merrill](mailto:jason@gcc.gnu.org). - vect256
- This branch is for extending vectorizer to 256bit. The branch is
maintained by Richard Biener and H.J. Lu. Patches should be marked
with the tag
`[vect256]`

in the subject line. - yara-branch
- This branch contains Yet Another Register Allocator (YARA).
The branch was maintained by Vladimir Makarov <
[vmakarov@redhat.com](mailto:vmakarov@redhat.com)>. It is no longer maintained; some of the work was used as a basis for the work on the ira branch. - x32
- This branch was to implement
[x32 psABI](https://sites.google.com/site/x32abi/). The branch is maintained by H.J. Lu. Patches should be marked with the tag`[x32]`

in the subject line.

For questions related to the use of GCC,
please consult these web pages and the
[GCC manuals](https://gcc.gnu.org/onlinedocs/). If that fails,
the [gcc-help@gcc.gnu.org](mailto:gcc-help@gcc.gnu.org)
mailing list might help.
Comments on these web pages and the development of GCC are welcome on our
developer list at [gcc@gcc.gnu.org](mailto:gcc@gcc.gnu.org).
All of [our lists](https://gcc.gnu.org/lists.html)
have public archives.

Copyright (C)
[Free Software Foundation, Inc.](https://www.fsf.org)
Verbatim copying and distribution of this entire article is
permitted in any medium, provided this notice is preserved.

These pages are
[maintained by the GCC team](https://gcc.gnu.org/about.html).
Last modified 2025-08-31.
