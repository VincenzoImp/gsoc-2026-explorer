# Developer options

**Parent:** GNU Compiler Collection (GCC) — Project Ideas
**Source:** https://gcc.gnu.org/onlinedocs/gcc/Developer-Options.html
**Scraped:** 2026-02-22T23:28:47.609038

---

This section describes command-line options that are primarily of interest to GCC developers, including options to support compiler testing and investigation of compiler bugs and compile-time performance problems. This includes options that produce debug dumps at various points in the compilation; that print statistics such as memory use and execution time; and that print information about GCC’s configuration, such as where it searches for libraries. You should rarely need to use any of these options for ordinary compilation and linking tasks.

Many developer options that cause GCC to dump output to a file take an
optional ‘`= filename`’ suffix. You can specify ‘

If ‘`= filename`’ is omitted, a default dump file name is
constructed by concatenating the base dump file name, a pass number,
phase letter, and pass name. The base dump file name is the name of
output file produced by the compiler if explicitly specified and not
an executable; otherwise it is the source file name.
The pass number is determined by the order passes are registered with
the compiler’s pass manager.
This is generally the same as the order of execution, but passes
registered by plugins, target-specific passes, or passes that are
otherwise registered late are numbered higher than the pass named
‘

`-fcallgraph-info`

[¶](https://gcc.gnu.org#index-fcallgraph-info)`-fcallgraph-info=`

`MARKERS`Makes the compiler output callgraph information for the program, on a per-object-file basis. The information is generated in the common VCG format. It can be decorated with additional, per-node and/or per-edge information, if a list of comma-separated markers is additionally specified. When the

`su`

marker is specified, the callgraph is decorated with stack usage information; it is equivalent to`-fstack-usage`. When the`da`

marker is specified, the callgraph is decorated with information about dynamically allocated objects.When compiling with

`-flto`, no callgraph information is output along with the object file. At LTO link time,`-fcallgraph-info`may generate multiple callgraph information files next to intermediate LTO output files.`-d`

`letters`[¶](https://gcc.gnu.org#index-d-1)`--dump=`

`letters``--dump`

`letters``-fdump-rtl-`

`pass``-fdump-rtl-`

`pass`-`options``-fdump-rtl-`

`pass`-`options`=`filename`Says to make debugging dumps during compilation at times specified by

`letters`when using`-d`or by`pass`when using`-fdump-rtl`. This is used for debugging the RTL-based passes of the compiler.Some

`-d`switches have different meaning when`letters``-E`is used for preprocessing. See[Options Controlling the Preprocessor](https://gcc.gnu.org/Preprocessor-Options.html), for information about preprocessor-specific dump options.The ‘

`-`’ form allows greater control over the details of the dump. See`options``-fdump-tree`.Here are actual instances of command-line options following these patterns and their meanings:

`-fdump-rtl-alignments`

[¶](https://gcc.gnu.org#index-fdump-rtl-alignments)Dump after branch alignments have been computed.

`-fdump-rtl-asmcons`

[¶](https://gcc.gnu.org#index-fdump-rtl-asmcons)Dump after fixing rtl statements that have unsatisfied in/out constraints.

`-fdump-rtl-auto_inc_dec`

[¶](https://gcc.gnu.org#index-fdump-rtl-auto_005finc_005fdec)Dump after auto-inc-dec discovery. This pass is only run on architectures that have auto inc or auto dec instructions.

`-fdump-rtl-barriers`

[¶](https://gcc.gnu.org#index-fdump-rtl-barriers)Dump after cleaning up the barrier instructions.

`-fdump-rtl-bbpart`

[¶](https://gcc.gnu.org#index-fdump-rtl-bbpart)Dump after partitioning hot and cold basic blocks.

`-fdump-rtl-bbro`

[¶](https://gcc.gnu.org#index-fdump-rtl-bbro)Dump after block reordering.

`-fdump-rtl-btl1`

[¶](https://gcc.gnu.org#index-fdump-rtl-btl2)`-fdump-rtl-btl2`

`-fdump-rtl-btl1`and`-fdump-rtl-btl2`enable dumping after the two branch target load optimization passes.`-fdump-rtl-bypass`

[¶](https://gcc.gnu.org#index-fdump-rtl-bypass)Dump after jump bypassing and control flow optimizations.

`-fdump-rtl-combine`

[¶](https://gcc.gnu.org#index-fdump-rtl-combine)Dump after the RTL instruction combination pass.

`-fdump-rtl-compgotos`

[¶](https://gcc.gnu.org#index-fdump-rtl-compgotos)Dump after duplicating the computed gotos.

`-fdump-rtl-ce1`

[¶](https://gcc.gnu.org#index-fdump-rtl-ce1)`-fdump-rtl-ce2`

`-fdump-rtl-ce3`

`-fdump-rtl-ce1`,`-fdump-rtl-ce2`, and`-fdump-rtl-ce3`enable dumping after the three if conversion passes.`-fdump-rtl-cprop_hardreg`

[¶](https://gcc.gnu.org#index-fdump-rtl-cprop_005fhardreg)Dump after hard register copy propagation.

`-fdump-rtl-csa`

[¶](https://gcc.gnu.org#index-fdump-rtl-csa)Dump after combining stack adjustments.

`-fdump-rtl-cse1`

[¶](https://gcc.gnu.org#index-fdump-rtl-cse1)`-fdump-rtl-cse2`

`-fdump-rtl-cse1`and`-fdump-rtl-cse2`enable dumping after the two common subexpression elimination passes.`-fdump-rtl-dce`

[¶](https://gcc.gnu.org#index-fdump-rtl-dce)Dump after the standalone dead code elimination passes.

`-fdump-rtl-dbr`

[¶](https://gcc.gnu.org#index-fdump-rtl-dbr)Dump after delayed branch scheduling.

`-fdump-rtl-dce1`

[¶](https://gcc.gnu.org#index-fdump-rtl-dce1)`-fdump-rtl-dce2`

`-fdump-rtl-dce1`and`-fdump-rtl-dce2`enable dumping after the two dead store elimination passes.`-fdump-rtl-eh`

[¶](https://gcc.gnu.org#index-fdump-rtl-eh)Dump after finalization of EH handling code.

`-fdump-rtl-eh_ranges`

[¶](https://gcc.gnu.org#index-fdump-rtl-eh_005franges)Dump after conversion of EH handling range regions.

`-fdump-rtl-expand`

[¶](https://gcc.gnu.org#index-fdump-rtl-expand)Dump after RTL generation.

`-fdump-rtl-fwprop1`

[¶](https://gcc.gnu.org#index-fdump-rtl-fwprop1)`-fdump-rtl-fwprop2`

`-fdump-rtl-fwprop1`and`-fdump-rtl-fwprop2`enable dumping after the two forward propagation passes.`-fdump-rtl-gcse1`

[¶](https://gcc.gnu.org#index-fdump-rtl-gcse1)`-fdump-rtl-gcse2`

`-fdump-rtl-gcse1`and`-fdump-rtl-gcse2`enable dumping after global common subexpression elimination.`-fdump-rtl-init-regs`

[¶](https://gcc.gnu.org#index-fdump-rtl-init-regs)Dump after the initialization of the registers.

`-fdump-rtl-initvals`

[¶](https://gcc.gnu.org#index-fdump-rtl-initvals)Dump after the computation of the initial value sets.

`-fdump-rtl-into_cfglayout`

[¶](https://gcc.gnu.org#index-fdump-rtl-into_005fcfglayout)Dump after converting to cfglayout mode.

`-fdump-rtl-ira`

[¶](https://gcc.gnu.org#index-fdump-rtl-ira)Dump after iterated register allocation.

`-fdump-rtl-jump`

[¶](https://gcc.gnu.org#index-fdump-rtl-jump)Dump after the second jump optimization.

`-fdump-rtl-loop2`

[¶](https://gcc.gnu.org#index-fdump-rtl-loop2)`-fdump-rtl-loop2`enables dumping after the rtl loop optimization passes.`-fdump-rtl-mach`

[¶](https://gcc.gnu.org#index-fdump-rtl-mach)Dump after performing the machine dependent reorganization pass, if that pass exists.

`-fdump-rtl-mode_sw`

[¶](https://gcc.gnu.org#index-fdump-rtl-mode_005fsw)Dump after removing redundant mode switches.

`-fdump-rtl-rnreg`

[¶](https://gcc.gnu.org#index-fdump-rtl-rnreg)Dump after register renumbering.

`-fdump-rtl-outof_cfglayout`

[¶](https://gcc.gnu.org#index-fdump-rtl-outof_005fcfglayout)Dump after converting from cfglayout mode.

`-fdump-rtl-peephole2`

[¶](https://gcc.gnu.org#index-fdump-rtl-peephole2)Dump after the peephole pass.

`-fdump-rtl-postreload`

[¶](https://gcc.gnu.org#index-fdump-rtl-postreload)Dump after post-reload optimizations.

`-fdump-rtl-pro_and_epilogue`

[¶](https://gcc.gnu.org#index-fdump-rtl-pro_005fand_005fepilogue)Dump after generating the function prologues and epilogues.

`-fdump-rtl-sched1`

[¶](https://gcc.gnu.org#index-fdump-rtl-sched1)`-fdump-rtl-sched2`

`-fdump-rtl-sched1`and`-fdump-rtl-sched2`enable dumping after the basic block scheduling passes.`-fdump-rtl-ree`

[¶](https://gcc.gnu.org#index-fdump-rtl-ree)Dump after sign/zero extension elimination.

`-fdump-rtl-seqabstr`

[¶](https://gcc.gnu.org#index-fdump-rtl-seqabstr)Dump after common sequence discovery.

`-fdump-rtl-shorten`

[¶](https://gcc.gnu.org#index-fdump-rtl-shorten)Dump after shortening branches.

`-fdump-rtl-split1`

[¶](https://gcc.gnu.org#index-fdump-rtl-split1)`-fdump-rtl-split2`

`-fdump-rtl-split3`

`-fdump-rtl-split4`

`-fdump-rtl-split5`

These options enable dumping after five rounds of instruction splitting.

`-fdump-rtl-sms`

[¶](https://gcc.gnu.org#index-fdump-rtl-sms)Dump after modulo scheduling. This pass is only run on some architectures.

`-fdump-rtl-stack`

[¶](https://gcc.gnu.org#index-fdump-rtl-stack)Dump after conversion from GCC’s “flat register file” registers to the x87’s stack-like registers. This pass is only run on x86 variants.

`-fdump-rtl-subreg1`

[¶](https://gcc.gnu.org#index-fdump-rtl-subreg1)`-fdump-rtl-subreg2`

`-fdump-rtl-subreg1`and`-fdump-rtl-subreg2`enable dumping after the two subreg expansion passes.`-fdump-rtl-vartrack`

[¶](https://gcc.gnu.org#index-fdump-rtl-vartrack)Dump after variable tracking.

`-fdump-rtl-vregs`

[¶](https://gcc.gnu.org#index-fdump-rtl-vregs)Dump after converting virtual registers to hard registers.

`-fdump-rtl-web`

[¶](https://gcc.gnu.org#index-fdump-rtl-web)Dump after live range splitting.

`-fdump-rtl-regclass`

[¶](https://gcc.gnu.org#index-fdump-rtl-regclass)`-fdump-rtl-subregs_of_mode_init`

`-fdump-rtl-subregs_of_mode_finish`

`-fdump-rtl-dfinit`

`-fdump-rtl-dfinish`

These dumps are defined but always produce empty files.

`-da`

[¶](https://gcc.gnu.org#index-da)`--dump=a`

`-fdump-rtl-all`

Produce all the dumps listed above.

`-dA`

[¶](https://gcc.gnu.org#index-dA)`--dump=A`

Annotate the assembler output with miscellaneous debugging information.

`-dD`

[¶](https://gcc.gnu.org#index-dD-1)`--dump=D`

Dump all macro definitions, at the end of preprocessing, in addition to normal output.

`-dH`

[¶](https://gcc.gnu.org#index-dH)`--dump=H`

Produce a core dump whenever an error occurs.

`-dp`

[¶](https://gcc.gnu.org#index-dp)`--dump=p`

Annotate the assembler output with a comment indicating which pattern and alternative is used. The length and cost of each instruction are also printed.

`-dP`

[¶](https://gcc.gnu.org#index-dP)`--dump=P`

Dump the RTL in the assembler output as a comment before each instruction. Also turns on

`-dp`annotation.`-dx`

[¶](https://gcc.gnu.org#index-dx)`--dump=x`

Just generate RTL for a function instead of compiling it. Usually used with

`-fdump-rtl-expand`.

`-fdump-debug`

[¶](https://gcc.gnu.org#index-fdump-debug)Dump debugging information generated during the debug generation phase.

`-fdump-earlydebug`

[¶](https://gcc.gnu.org#index-fdump-earlydebug)Dump debugging information generated during the early debug generation phase.

`-fdump-noaddr`

[¶](https://gcc.gnu.org#index-fdump-noaddr)When doing debugging dumps, suppress address output. This makes it more feasible to use diff on debugging dumps for compiler invocations with different compiler binaries and/or different text / bss / data / heap / stack / dso start locations.

`-freport-bug`

[¶](https://gcc.gnu.org#index-freport-bug)Collect and dump debug information into a temporary file if an internal compiler error (ICE) occurs.

`-fdump-unnumbered`

[¶](https://gcc.gnu.org#index-fdump-unnumbered)When doing debugging dumps, suppress instruction numbers and address output. This makes it more feasible to use diff on debugging dumps for compiler invocations with different options, in particular with and without

`-g`.`-fdump-unnumbered-links`

[¶](https://gcc.gnu.org#index-fdump-unnumbered-links)When doing debugging dumps (see

`-d`option above), suppress instruction numbers for the links to the previous and next instructions in a sequence.`-fdump-internal-locations`

[¶](https://gcc.gnu.org#index-fdump-internal-locations)Dump detailed information about GCC’s internal representation of source code locations.

`-fdump-ipa-`

`switch`[¶](https://gcc.gnu.org#index-fdump-ipa)`-fdump-ipa-`

`switch`-`options`Control the dumping at various stages of inter-procedural analysis language tree to a file. The file name is generated by appending a switch specific suffix to the source file name, and the file is created in the same directory as the output file. The following dumps are possible:

- ‘
`all`’ Enables all inter-procedural analysis dumps.

- ‘
`cgraph`’ Dumps information about call-graph optimization, unused function removal, and inlining decisions.

- ‘
`inline`’ Dump after function inlining.

- ‘
`strubm`’ Dump after selecting

`strub`

modes, and recording the selections as function attributes.- ‘
`strub`’ Dump

`strub`

transformations: interface changes, function wrapping, and insertion of builtin calls for stack scrubbing and watermarking.

Additionally, the options

`-optimized`,`-missed`,`-note`, and`-all`can be provided, with the same meaning as for`-fopt-info`, defaulting to`-optimized`.For example,

`-fdump-ipa-inline-optimized-missed`will emit information on callsites that were inlined, along with callsites that were not inlined.By default, the dump will contain messages about successful optimizations (equivalent to

`-optimized`) together with low-level details about the analysis.- ‘
`-fdump-ipa-clones`

[¶](https://gcc.gnu.org#index-fdump-ipa-clones)-
Create a dump file containing information about creation of call graph node clones and removals of call graph nodes during inter-procedural optimizations and transformations. Its main intended use is that tools that create live-patches can determine the set of functions that need to be live-patched to completely replace a particular function (see

`-flive-patching`). The file name is generated by appending suffix`ipa-clones`

to the source file name, and the file is created in the same directory as the output file. Each entry in the file is on a separate line containing semicolon separated fields.In the case of call graph clone creation, the individual fields are:

- String
`Callgraph clone`

. - Name of the function being cloned as it is presented to the assembler.
- A number that uniquely represents the function being cloned in the call graph. Note that the number is unique only within a compilation unit or within whole-program analysis but is likely to be different in the two phases.
- The file name of the source file where the function is defined.
- The line on which the function definition is located.
- The column where the function definition is located.
- Name of the new function clone as it is presented to the assembler.
- A number that uniquely represents the new function clone in the call graph. Note that the number is unique only within a compilation unit or within whole-program analysis but is likely to be different in the two phases.
- The file name of the source file where the source code location of the new clone points to.
- The line to which the source code location of the new clone points to.
- The column to which the source code location of the new clone points to.
- A string that determines the reason for cloning.

In the case of call graph clone removal, the individual fields are:

- String
`Callgraph removal`

. - Name of the function being removed as it would be presented to the assembler.
- A number that uniquely represents the function being cloned in the call graph. Note that the number is unique only within a compilation unit or within whole-program analysis but is likely to be different in the two phases.
- The file name of the source file where the function is defined.
- The line on which the function definition is located.
- The column where the function definition is located.

- String
`-fdump-lang`

[¶](https://gcc.gnu.org#index-fdump-lang)Dump language-specific information. The file name is made by appending

`.lang`to the source file name.`-fdump-lang-all`

[¶](https://gcc.gnu.org#index-fdump-lang-all)`-fdump-lang-`

`switch``-fdump-lang-`

`switch`-`options``-fdump-lang-`

`switch`-`options`=`filename`Control the dumping of language-specific information. The

`options`and`filename`portions behave as described in the`-fdump-tree`option.`-fdump-tree-all`enables all language-specific dumps; other options vary with the language. For instance, see See[Options Controlling C++ Dialect](https://gcc.gnu.org/C_002b_002b-Dialect-Options.html)for the`-fdump-lang`flags supported by the C++ front-end.`-fdump-passes`

[¶](https://gcc.gnu.org#index-fdump-passes)Print on

`stderr`the list of optimization passes that are turned on and off by the current command-line options.`-fdump-statistics-`

`option`[¶](https://gcc.gnu.org#index-fdump-statistics)Enable and control dumping of pass statistics in a separate file. The file name is generated by appending a suffix ending in ‘

`.statistics`’ to the source file name, and the file is created in the same directory as the output file. If the ‘`-`’ form is used, ‘`option``-stats`’ causes counters to be summed over the whole compilation unit while ‘`-details`’ dumps every event as the passes generate them. The default with no option is to sum counters for each function compiled.`-fdump-tree-all`

[¶](https://gcc.gnu.org#index-fdump-tree-all)`-fdump-tree-`

`switch``-fdump-tree-`

`switch`-`options``-fdump-tree-`

`switch`-`options`=`filename`Control the dumping at various stages of processing the intermediate language tree to a file. If the ‘

`-`’ form is used,`options``options`is a list of ‘`-`’ separated options which control the details of the dump. Not all options are applicable to all dumps; those that are not meaningful are ignored. The following options are available- ‘
`address`’ Print the address of each node. Usually this is not meaningful as it changes according to the environment and source file. Its primary use is for tying up a dump file with a debug environment.

- ‘
`asmname`’ If

`DECL_ASSEMBLER_NAME`

has been set for a given decl, use that in the dump instead of`DECL_NAME`

. Its primary use is ease of use working backward from mangled names in the assembly file.- ‘
`slim`’ When dumping front-end intermediate representations, inhibit dumping of members of a scope or body of a function merely because that scope has been reached. Only dump such items when they are directly reachable by some other path.

When dumping pretty-printed trees, this option inhibits dumping the bodies of control structures.

When dumping RTL, print the RTL in slim (condensed) form instead of the default LISP-like representation.

- ‘
`raw`’ Print a raw representation of the tree. By default, trees are pretty-printed into a C-like representation.

- ‘
`details`’ Enable more detailed dumps (not honored by every dump option). Also include information from the optimization passes.

- ‘
`stats`’ Enable dumping various statistics about the pass (not honored by every dump option).

- ‘
`blocks`’ Enable showing basic block boundaries (disabled in raw dumps).

- ‘
`graph`’ For each of the other indicated dump files (

`-fdump-rtl-`), dump a representation of the control flow graph suitable for viewing with GraphViz to`pass`. Each function in the file is pretty-printed as a subgraph, so that GraphViz can render them all in a single plot.`file`.`passid`.`pass`.dotRTL is always dumped in slim form.

- ‘
`vops`’ Enable showing virtual operands for every statement.

- ‘
`lineno`’ Enable showing line numbers for statements.

- ‘
`uid`’ Enable showing the unique ID (

`DECL_UID`

) for each variable.- ‘
`verbose`’ Enable showing the tree dump for each statement.

- ‘
`eh`’ Enable showing the EH region number holding each statement.

- ‘
`scev`’ Enable showing scalar evolution analysis details.

- ‘
`optimized`’ Enable showing optimization information (only available in certain passes).

- ‘
`missed`’ Enable showing missed optimization information (only available in certain passes).

- ‘
`note`’ Enable other detailed optimization information (only available in certain passes).

- ‘
`folding`’ Enable dumping information about match-and-simplify (match.pd) patterns, when they are applied.

- ‘
`all`’ Turn on all options, except

`raw`,`slim`,`verbose`and`lineno`.- ‘
`optall`’ Turn on all optimization options, i.e.,

`optimized`,`missed`, and`note`.

To determine what tree dumps are available or find the dump for a pass of interest follow the steps below.

- Invoke GCC with
`-fdump-passes`and in the`stderr`output look for a code that corresponds to the pass you are interested in. For example, the codes`tree-evrp`

,`tree-vrp1`

, and`tree-vrp2`

correspond to the three Value Range Propagation passes. The number at the end distinguishes distinct invocations of the same pass. - To enable the creation of the dump file, append the pass code to
the
`-fdump-`option prefix and invoke GCC with it. For example, to enable the dump from the Early Value Range Propagation pass, invoke GCC with the`-fdump-tree-evrp`option. Optionally, you may specify the name of the dump file. If you don’t specify one, GCC creates as described below. - Find the pass dump in a file whose name is composed of three components
separated by a period: the name of the source file GCC was invoked to
compile, a numeric suffix indicating the pass number followed by the
letter ‘
`t`’ for tree passes (and the letter ‘`r`’ for RTL passes), and finally the pass code. For example, the Early VRP pass dump might be in a file named`myfile.c.038t.evrp`in the current working directory. Note that the numeric codes are not stable and may change from one version of GCC to another.

- ‘
`-fopt-info`

[¶](https://gcc.gnu.org#index-fopt-info)`-fopt-info-`

`options``-fopt-info-`

`options`=`filename`Controls optimization dumps from various optimization passes. If the ‘

`-`’ form is used,`options``options`is a list of ‘`-`’ separated option keywords to select the dump details and optimizations.The

`options`can be divided into three groups:- options describing what kinds of messages should be emitted,
- options describing the verbosity of the dump, and
- options describing which optimizations should be included.

The options from each group can be freely mixed as they are non-overlapping. However, in case of any conflicts, the later options override the earlier options on the command line.

The following options control which kinds of messages should be emitted:

- ‘
`optimized`’ Print information when an optimization is successfully applied. It is up to a pass to decide which information is relevant. For example, the vectorizer passes print the source location of loops which are successfully vectorized.

- ‘
`missed`’ Print information about missed optimizations. Individual passes control which information to include in the output.

- ‘
`note`’ Print verbose information about optimizations, such as certain transformations, more detailed messages about decisions etc.

- ‘
`all`’ Print detailed optimization information. This includes ‘

`optimized`’, ‘`missed`’, and ‘`note`’.

The following option controls the dump verbosity:

- ‘
`internals`’ By default, only “high-level” messages are emitted. This option enables additional, more detailed, messages, which are likely to only be of interest to GCC developers.


One or more of the following option keywords can be used to describe a group of optimizations:

- ‘
`ipa`’ Enable dumps from all interprocedural optimizations.

- ‘
`loop`’ Enable dumps from all loop optimizations.

- ‘
`inline`’ Enable dumps from all inlining optimizations.

- ‘
`omp`’ Enable dumps from all OMP (Offloading and Multi Processing) optimizations.

- ‘
`vec`’ Enable dumps from all vectorization optimizations.

- ‘
`optall`’ Enable dumps from all optimizations. This is a superset of the optimization groups listed above.


If

`options`is omitted, it defaults to ‘`optimized-optall`’, which means to dump messages about successful optimizations from all the passes, omitting messages that are treated as “internals”.If the

`filename`is provided, then the dumps from all the applicable optimizations are concatenated into the`filename`. Otherwise the dump is output onto`stderr`. Though multiple`-fopt-info`options are accepted, only one of them can include a`filename`. If other filenames are provided then all but the first such option are ignored.Note that the output

`filename`is overwritten in case of multiple translation units. If a combined output from multiple translation units is desired,`stderr`should be used instead.In the following example, the optimization info is output to

`stderr`:gcc -O3 -fopt-info

This example:

gcc -O3 -fopt-info-missed=missed.all

outputs missed optimization report from all the passes into

`missed.all`, and this one:gcc -O2 -ftree-vectorize -fopt-info-vec-missed

prints information about missed optimization opportunities from vectorization passes on

`stderr`. Note that`-fopt-info-vec-missed`is equivalent to`-fopt-info-missed-vec`. The order of the optimization group names and message types listed after`-fopt-info`does not matter.As another example,

gcc -O3 -fopt-info-inline-optimized-missed=inline.txt

outputs information about missed optimizations as well as optimized locations from all the inlining passes into

`inline.txt`.Finally, consider:

gcc -fopt-info-vec-missed=vec.miss -fopt-info-loop-optimized=loop.opt

Here the two output filenames

`vec.miss`and`loop.opt`are in conflict since only one output file is allowed. In this case, only the first option takes effect and the subsequent options are ignored. Thus only`vec.miss`is produced which contains dumps from the vectorizer about missed opportunities.`-fsave-optimization-record`

[¶](https://gcc.gnu.org#index-fsave-optimization-record)Write a SRCFILE.opt-record.json.gz file detailing what optimizations were performed, for those optimizations that support

`-fopt-info`.This option is experimental and the format of the data within the compressed JSON file is subject to change.

It is roughly equivalent to a machine-readable version of

`-fopt-info-all`, as a collection of messages with source file, line number and column number, with the following additional data for each message:- the execution count of the code being optimized, along with metadata about whether this was from actual profile data, or just an estimate, allowing consumers to prioritize messages by code hotness,
- the function name of the code being optimized, where applicable,
- the “inlining chain” for the code being optimized, so that when a function is inlined into several different places (which might themselves be inlined), the reader can distinguish between the copies,
- objects identifying those parts of the message that refer to expressions, statements or symbol-table nodes, which of these categories they are, and, when available, their source code location,
- the GCC pass that emitted the message, and
- the location in GCC’s own code from which the message was emitted

Additionally, some messages are logically nested within other messages, reflecting implementation details of the optimization passes.

`-fsched-verbose=`

`n`[¶](https://gcc.gnu.org#index-fsched-verbose)On targets that use instruction scheduling, this option controls the amount of debugging output the scheduler prints to the dump files.

For

`n`greater than zero,`-fsched-verbose`outputs the same information as`-fdump-rtl-sched1`and`-fdump-rtl-sched2`. For`n`greater than one, it also output basic block probabilities, detailed ready list information and unit/insn info. For`n`greater than two, it includes RTL at abort point, control-flow and regions info. And for`n`over four,`-fsched-verbose`also includes dependence info.`-fenable-`

`kind`-`pass`[¶](https://gcc.gnu.org#index-fdisable-)`-fdisable-`

`kind`-`pass`=`range-list`-
This is a set of options that are used to explicitly disable/enable optimization passes. These options are intended for use for debugging GCC. Compiler users should use regular options for enabling/disabling passes instead.

`-fdisable-ipa-`

`pass`Disable IPA pass

`pass`.`pass`is the pass name. If the same pass is statically invoked in the compiler multiple times, the pass name should be appended with a sequential number starting from 1.`-fdisable-rtl-`

`pass``-fdisable-rtl-`

`pass`=`range-list`Disable RTL pass

`pass`.`pass`is the pass name. If the same pass is statically invoked in the compiler multiple times, the pass name should be appended with a sequential number starting from 1.`range-list`is a comma-separated list of function ranges or assembler names. Each range is a number pair separated by a colon. The range is inclusive in both ends. If the range is trivial, the number pair can be simplified as a single number. If the function’s call graph node’s`uid`falls within one of the specified ranges, the`pass`is disabled for that function. The`uid`is shown in the function header of a dump file, and the pass names can be dumped by using option`-fdump-passes`.`-fdisable-tree-`

`pass``-fdisable-tree-`

`pass`=`range-list`Disable tree pass

`pass`. See`-fdisable-rtl`for the description of option arguments.`-fenable-ipa-`

`pass`Enable IPA pass

`pass`.`pass`is the pass name. If the same pass is statically invoked in the compiler multiple times, the pass name should be appended with a sequential number starting from 1.`-fenable-rtl-`

`pass``-fenable-rtl-`

`pass`=`range-list`Enable RTL pass

`pass`. See`-fdisable-rtl`for option argument description and examples.`-fenable-tree-`

`pass``-fenable-tree-`

`pass`=`range-list`Enable tree pass

`pass`. See`-fdisable-rtl`for the description of option arguments.

Here are some examples showing uses of these options.

# disable ccp1 for all functions -fdisable-tree-ccp1 # disable complete unroll for function whose cgraph node uid is 1 -fenable-tree-cunroll=1 # disable gcse2 for functions at the following ranges [1,1], # [300,400], and [400,1000] # disable gcse2 for functions foo and foo2 -fdisable-rtl-gcse2=foo,foo2 # disable early inlining -fdisable-tree-einline # disable ipa inlining -fdisable-ipa-inline # enable tree full unroll -fenable-tree-unroll

`-fchecking`

[¶](https://gcc.gnu.org#index-fchecking)`-fchecking=`

`n`Enable internal consistency checking. The default depends on the compiler configuration.

`-fchecking=2`enables further internal consistency checking that might affect code generation.`-frandom-seed=`

`string`[¶](https://gcc.gnu.org#index-frandom-seed)This option provides a seed that GCC uses in place of random numbers in generating certain symbol names that have to be different in every compiled file. It is also used to place unique stamps in coverage data files and the object files that produce them. You can use the

`-frandom-seed`option to produce reproducibly identical object files.The

`string`can either be a number (decimal, octal or hex) or an arbitrary string (in which case it’s converted to a number by computing CRC32).The

`string`should be different for every file you compile.`-save-temps`

[¶](https://gcc.gnu.org#index-save-temps)`--save-temps`

Store the usual “temporary” intermediate files permanently; name them as auxiliary output files, as specified described under

`-dumpbase`and`-dumpdir`.When used in combination with the

`-x`command-line option,`-save-temps`is sensible enough to avoid overwriting an input source file with the same extension as an intermediate file. The corresponding intermediate file may be obtained by renaming the source file before using`-save-temps`.`-save-temps=cwd`

[¶](https://gcc.gnu.org#index-save-temps_003dcwd)Equivalent to

`-save-temps -dumpdir ./`.`-save-temps=obj`

[¶](https://gcc.gnu.org#index-save-temps_003dobj)Equivalent to

`-save-temps -dumpdir`, where`outdir/``outdir/`is the directory of the output file specified after the`-o`option, including any directory separators. If the`-o`option is not used, the`-save-temps=obj`switch behaves like`-save-temps=cwd`.`-time[=`

`file`][¶](https://gcc.gnu.org#index-time)Report the CPU time taken by each subprocess in the compilation sequence. For C source files, this is the compiler proper and assembler (plus the linker if linking is done).

Without the specification of an output file, the output looks like this:

# cc1 0.12 0.01 # as 0.00 0.01

The first number on each line is the “user time”, that is time spent executing the program itself. The second number is “system time”, time spent executing operating system routines on behalf of the program. Both numbers are in seconds.

With the specification of an output file, the output is appended to the named file, and it looks like this:

0.12 0.01 cc1

`options`0.00 0.01 as`options`The “user time” and the “system time” are moved before the program name, and the options passed to the program are displayed, so that one can later tell what file was being compiled, and with which options.

`-fdump-final-insns[=`

`file`][¶](https://gcc.gnu.org#index-fdump-final-insns)Dump the final internal representation (RTL) to

`file`. If the optional argument is omitted (or if`file`is`.`

), the name of the dump file is determined by appending`.gkd`

to the dump base name, see`-dumpbase`.`-fcompare-debug[=`

`opts`][¶](https://gcc.gnu.org#index-fcompare-debug)If no error occurs during compilation, run the compiler a second time, adding

`opts`and`-fcompare-debug-second`to the arguments passed to the second compilation. Dump the final internal representation in both compilations, and print an error if they differ.If the equal sign is omitted, the default

`-gtoggle`is used.The environment variable

`GCC_COMPARE_DEBUG`

, if defined, non-empty and nonzero, implicitly enables`-fcompare-debug`. If`GCC_COMPARE_DEBUG`

is defined to a string starting with a dash, then it is used for`opts`, otherwise the default`-gtoggle`is used.`-fcompare-debug=`, with the equal sign but without`opts`, is equivalent to`-fno-compare-debug`, which disables the dumping of the final representation and the second compilation, preventing even`GCC_COMPARE_DEBUG`

from taking effect.To verify full coverage during

`-fcompare-debug`testing, set`GCC_COMPARE_DEBUG`

to say`-fcompare-debug-not-overridden`, which GCC rejects as an invalid option in any actual compilation (rather than preprocessing, assembly or linking). To get just a warning, setting`GCC_COMPARE_DEBUG`

to ‘`-w%n-fcompare-debug not overridden`’ will do.`-fcompare-debug-second`

[¶](https://gcc.gnu.org#index-fcompare-debug-second)This option is implicitly passed to the compiler for the second compilation requested by

`-fcompare-debug`, along with options to silence warnings, and omitting other options that would cause the compiler to produce output to files or to standard output as a side effect. Dump files and preserved temporary files are renamed so as to contain the`.gk`

additional extension during the second compilation, to avoid overwriting those generated by the first.When this option is passed to the compiler driver, it causes the

*first*compilation to be skipped, which makes it useful for little other than debugging the compiler proper.`-gtoggle`

[¶](https://gcc.gnu.org#index-gtoggle)Turn off generation of debug info, if leaving out this option generates it, or turn it on at level 2 otherwise. The position of this argument in the command line does not matter; it takes effect after all other options are processed, and it does so only once, no matter how many times it is given. This is mainly intended to be used with

`-fcompare-debug`.`-fvar-tracking-assignments-toggle`

[¶](https://gcc.gnu.org#index-fvar-tracking-assignments-toggle)Toggle

`-fvar-tracking-assignments`, in the same way that`-gtoggle`toggles`-g`.`-Q`

[¶](https://gcc.gnu.org#index-Q-1)When used on the command line prior to

`--help=`,`-Q`acts as a modifier to the help output. See[Options Controlling the Kind of Output](https://gcc.gnu.org/Overall-Options.html), for details about`--help=`.Otherwise, this option makes the compiler print out each function name as it is compiled, and print some statistics about each pass when it finishes.

`-ftime-report`

[¶](https://gcc.gnu.org#index-ftime-report)Makes the compiler print some statistics to stderr about the time consumed by each pass when it finishes.

If SARIF output of diagnostics was requested via

`-fdiagnostics-format=sarif-file`or`-fdiagnostics-format=sarif-stderr`then the`-ftime-report`information is instead emitted in JSON form as part of SARIF output. The precise format of this JSON data is subject to change, and the values may not exactly match those emitted to stderr due to being written out at a slightly different place within the compiler.`-ftime-report-details`

[¶](https://gcc.gnu.org#index-ftime-report-details)Record the time consumed by infrastructure parts separately for each pass.

`-fira-verbose=`

`n`[¶](https://gcc.gnu.org#index-fira-verbose)Control the verbosity of the dump file for the integrated register allocator. The default value is 5. If the value

`n`is greater or equal to 10, the dump output is sent to stderr using the same format as`n`minus 10.`-flto-report`

[¶](https://gcc.gnu.org#index-flto-report)Prints a report with internal details on the workings of the link-time optimizer. The contents of this report vary from version to version. It is meant to be useful to GCC developers when processing object files in LTO mode (via

`-flto`).Disabled by default.

`-flto-report-wpa`

[¶](https://gcc.gnu.org#index-flto-report-wpa)Like

`-flto-report`, but only print for the WPA phase of link-time optimization.`-fmem-report`

[¶](https://gcc.gnu.org#index-fmem-report)Makes the compiler print some statistics about permanent memory allocation when it finishes.

`-fmem-report-wpa`

[¶](https://gcc.gnu.org#index-fmem-report-wpa)Makes the compiler print some statistics about permanent memory allocation for the WPA phase only.

`-fpre-ipa-mem-report`

[¶](https://gcc.gnu.org#index-fpre-ipa-mem-report)`-fpost-ipa-mem-report`

Makes the compiler print some statistics about permanent memory allocation before or after interprocedural optimization.

`-fmultiflags`

[¶](https://gcc.gnu.org#index-fmultiflags)This option enables multilib-aware

`TFLAGS`

to be used to build target libraries with options different from those the compiler is configured to use by default, through the use of specs (see[Specifying Subprocesses and the Switches to Pass to Them](https://gcc.gnu.org/Spec-Files.html)) set up by compiler internals, by the target, or by builders at configure time.Like

`TFLAGS`

, this allows the target libraries to be built for portable baseline environments, while the compiler defaults to more demanding ones. That’s useful because users can easily override the defaults the compiler is configured to use to build their own programs, if the defaults are not ideal for their target environment, whereas rebuilding the runtime libraries is usually not as easy or desirable.Unlike

`TFLAGS`

, the use of specs enables different flags to be selected for different multilibs. The way to accomplish that is to build with ‘`make TFLAGS=-fmultiflags`’, after configuring ‘`--with-specs=%{fmultiflags:...}`’.This option is discarded by the driver once it’s done processing driver self spec.

It is also useful to check that

`TFLAGS`

are being used to build all target libraries, by configuring a non-bootstrap compiler ‘`--with-specs='%{!fmultiflags:%emissing TFLAGS}'`’ and building the compiler and target libraries.`-fprofile-report`

[¶](https://gcc.gnu.org#index-fprofile-report)Makes the compiler print some statistics about consistency of the (estimated) profile and effect of individual passes.

`-fstack-usage`

[¶](https://gcc.gnu.org#index-fstack-usage)Makes the compiler output stack usage information for the program, on a per-function basis. The filename for the dump is made by appending

`.su`to the`auxname`.`auxname`is generated from the name of the output file, if explicitly specified and it is not an executable, otherwise it is the basename of the source file. An entry is made up of three fields:- The name of the function.
- A number of bytes.
- One or more qualifiers:
`static`

,`dynamic`

,`bounded`

.

The qualifier

`static`

means that the function manipulates the stack statically: a fixed number of bytes are allocated for the frame on function entry and released on function exit; no stack adjustments are otherwise made in the function. The second field is this fixed number of bytes.The qualifier

`dynamic`

means that the function manipulates the stack dynamically: in addition to the static allocation described above, stack adjustments are made in the body of the function, for example to push/pop arguments around function calls. If the qualifier`bounded`

is also present, the amount of these adjustments is bounded at compile time and the second field is an upper bound of the total amount of stack used by the function. If it is not present, the amount of these adjustments is not bounded at compile time and the second field only represents the bounded part.`-fstats`

[¶](https://gcc.gnu.org#index-fstats)Emit statistics about front-end processing at the end of the compilation. This option is supported only by the C++ front end, and the information is generally only useful to the G++ development team.

`-fdbg-cnt-list`

[¶](https://gcc.gnu.org#index-fdbg-cnt-list)Print the name and the counter upper bound for all debug counters.

`-fdbg-cnt=`

`counter-value-list`[¶](https://gcc.gnu.org#index-fdbg-cnt)Set the internal debug counter lower and upper bound.

`counter-value-list`is a comma-separated list of`name`:`lower_bound1`-`upper_bound1`[:`lower_bound2`-`upper_bound2`...] tuples which sets the name of the counter and list of closed intervals. The`lower_bound`is optional and is zero initialized if not set. For example, with`-fdbg-cnt=dce:2-4:10-11,tail_call:10`,`dbg_cnt(dce)`

returns true only for second, third, fourth, tenth and eleventh invocation. For`dbg_cnt(tail_call)`

true is returned for first 10 invocations.`-print-file-name=`

`library`[¶](https://gcc.gnu.org#index-print-file-name)`--print-file-name=`

`library``--print-file-name`

`library`Print the full absolute name of the library file

`library`that would be used when linking—and don’t do anything else. With this option, GCC does not compile or link anything; it just prints the file name.`-print-multi-directory`

[¶](https://gcc.gnu.org#index-print-multi-directory)`--print-multi-directory`

Print the directory name corresponding to the multilib selected by any other switches present in the command line. This directory is supposed to exist in

`GCC_EXEC_PREFIX`

.`-print-multi-lib`

[¶](https://gcc.gnu.org#index-print-multi-lib)`--print-multi-lib`

Print the mapping from multilib directory names to compiler switches that enable them. The directory name is separated from the switches by ‘

`;`’, and each switch starts with an ‘`@`’ instead of the ‘`-`’, without spaces between multiple switches. This is supposed to ease shell processing.`-print-multi-os-directory`

[¶](https://gcc.gnu.org#index-print-multi-os-directory)`--print-multi-os-directory`

Print the path to OS libraries for the selected multilib, relative to some

`lib`subdirectory. If OS libraries are present in the`lib`subdirectory and no multilibs are used, this is usually just`.`, if OS libraries are present in`lib`sibling directories this prints e.g.`suffix``../lib64`,`../lib`or`../lib32`, or if OS libraries are present in`lib/`subdirectories it prints e.g.`subdir``amd64`,`sparcv9`or`ev6`.`-print-multiarch`

[¶](https://gcc.gnu.org#index-print-multiarch)`--print-multiarch`

Print the path to OS libraries for the selected multiarch, relative to some

`lib`subdirectory.`-print-prog-name=`

`program`[¶](https://gcc.gnu.org#index-print-prog-name)`--print-prog-name=`

`program``--print-prog-name`

`program`Like

`-print-file-name`, but searches for a program such as`cpp`

.`-print-libgcc-file-name`

[¶](https://gcc.gnu.org#index-print-libgcc-file-name)`--print-libgcc-file-name`

Same as

`-print-file-name=libgcc.a`.This is useful when you use

`-nostdlib`or`-nodefaultlibs`but you do want to link with`libgcc.a`. You can do:gcc -nostdlib

`files`… `gcc -print-libgcc-file-name``-print-search-dirs`

[¶](https://gcc.gnu.org#index-print-search-dirs)`--print-search-dirs`

Print the name of the configured installation directory and a list of program and library directories

`gcc`

searches—and don’t do anything else.This is useful when

`gcc`

prints the error message ‘`installation problem, cannot exec cpp0: No such file or directory`’. To resolve this you either need to put`cpp0`and the other compiler components where`gcc`

expects to find them, or you can set the environment variable`GCC_EXEC_PREFIX`

to the directory where you installed them. Don’t forget the trailing ‘`/`’. See[Environment Variables Affecting GCC](https://gcc.gnu.org/Environment-Variables.html).`-print-sysroot`

[¶](https://gcc.gnu.org#index-print-sysroot)`--print-sysroot`

Print the target sysroot directory that is used during compilation. This is the target sysroot specified either at configure time or using the

`--sysroot`option, possibly with an extra suffix that depends on compilation options. If no target sysroot is specified, the option prints nothing.`-print-sysroot-headers-suffix`

[¶](https://gcc.gnu.org#index-print-sysroot-headers-suffix)`--print-sysroot-headers-suffix`

Print the suffix added to the target sysroot when searching for headers, or give an error if the compiler is not configured with such a suffix—and don’t do anything else.

`-dumpmachine`

[¶](https://gcc.gnu.org#index-dumpmachine)Print the compiler’s target machine (for example, ‘

`i686-pc-linux-gnu`’)—and don’t do anything else.`-dumpversion`

[¶](https://gcc.gnu.org#index-dumpversion)Print the compiler version (for example,

`3.0`

,`6.3.0`

or`7`

)—and don’t do anything else. This is the compiler version used in filesystem paths and specs. Depending on how the compiler has been configured it can be just a single number (major version), two numbers separated by a dot (major and minor version) or three numbers separated by dots (major, minor and patchlevel version).`-dumpfullversion`

[¶](https://gcc.gnu.org#index-dumpfullversion)Print the full compiler version—and don’t do anything else. The output is always three numbers separated by dots, major, minor and patchlevel version.

`-dumpspecs`

[¶](https://gcc.gnu.org#index-dumpspecs)Print the compiler’s built-in specs—and don’t do anything else. (This is used when GCC itself is being built.) See

[Specifying Subprocesses and the Switches to Pass to Them](https://gcc.gnu.org/Spec-Files.html).`--param`

`name`=`value`[¶](https://gcc.gnu.org#index-param)`--param=`

`name`=`value`GCC by convention uses parameters that can be specified on the command line instead of hard-wired constants to represent arbitrary compiler limits or heuristics. Many parameters are related to optimization; for example, GCC does not inline functions that contain more than a certain number of instructions. The static analyzer similarly uses parameters to limit complexity, link-time optimization uses parameters to control partitioning, and so on. Other parameters control aspects of GCC that are completely internal, such as its memory allocation and garbage collection strategy. Still others control target-specific behavior.

The

`--param`option provides a uniform interface for specifying values for these compiler parameters. However, the names of specific parameters, and the meaning of the values, are tied to the internals of the compiler, and are subject to change without notice in future releases. You should not depend on parameter settings for correct compilation of your program. They are exposed via the command line for the convenience of developers in debugging compilation problems or, in some cases, to provide workarounds for compiler bugs.See

[Parameters](https://gcc.gnu.org/onlinedocs/gccint/Parameters.html#Parameters)in GNU Compiler Collection (GCC) Internals, for documentation of these internal parameters.
