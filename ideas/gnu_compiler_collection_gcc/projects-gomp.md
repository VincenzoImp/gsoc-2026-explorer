# https://gcc.gnu.org/projects/gomp/

**Parent:** GNU Compiler Collection (GCC) — Project Ideas
**Source:** https://gcc.gnu.org/projects/gomp/
**Scraped:** 2026-02-22T23:28:47.608791

---

The GOMP project consists of implementation of OpenMP and OpenACC to
permit annotating the source code to permit running it concurrently with
thread parallelization and on offloading devices (accelerators

such
as GPUs), including the associated run-time library and API routines. Both
OpenMP and OpenACC are supported with GCC's C, C++ and Fortran compilers.

[Usage](https://gcc.gnu.org#usage)[Documentation](https://gcc.gnu.org#documentation)[History and Project Goal](https://gcc.gnu.org#history_and_goal)[Contributing](https://gcc.gnu.org#contributing)[Reporting Bugs](https://gcc.gnu.org#bugs)[OpenMP Implementation Status](https://gcc.gnu.org#implementation-status):[2.5](https://gcc.gnu.org#omp2.5)·[3.0](https://gcc.gnu.org#omp3.0)·[3.1](https://gcc.gnu.org#omp3.1)·[4.0](https://gcc.gnu.org#omp4.0)·[4.5](https://gcc.gnu.org#omp4.5)·[5.0](https://gcc.gnu.org#omp5.0)·[5.1](https://gcc.gnu.org#omp5.1)·[5.2](https://gcc.gnu.org#omp5.2)·[6.0](https://gcc.gnu.org#omp6.0)·[TR 14](https://gcc.gnu.org#omp6.1)[OpenMP Releases and Status](https://gcc.gnu.org#omp-status)

- To enable
, use[OpenMP](https://www.openmp.org).`-fopenmp`

can be used to enable only the SIMD vectorization and loop-transformation constructs without creating multiple threads, offloading code or adding a library dependency.`-fopenmp-simd`

- To enable
, use[OpenACC](https://www.openacc.org).`-fopenacc`

- If either is enabled, offloading is automatically generated for all
offload-device types for which the compiler has been configured. Use
to disable or specify the offload-devices to be used. Use`-foffload=`

to pass device-specific compiler and linker flags.`-foffload-options=`


Diagnostics

- The
flag provides details about optimizations at compile time.`-fopt-info`

- Environment variables can be used to influence run-time behavior and output
more data, useful for debugging or performance tuning. See the
[GNU libgomp](https://gcc.gnu.org/onlinedocs/libgomp/)manual for details.

[GNU libgomp](https://gcc.gnu.org/onlinedocs/libgomp/)manual for API routines, environment variables and implementation details.[OpenMP specification](https://www.openmp.org/specifications/), including OpenMP API examples documents, reference cards and additional definitions specification.[OpenACC specification](https://www.openacc.org/specification).- Related GCC wiki pages:
[openmp](https://gcc.gnu.org/wiki/openmp),[OpenACC](https://gcc.gnu.org/wiki/OpenACC),[Offloading](https://gcc.gnu.org/wiki/Offloading).

The GOMP project has developed an implementation of
[OpenMP](https://www.openmp.org)
for the C, C++, and [Fortran](https://gcc.gnu.org/fortran/)
compilers in the [GNU
Compiler Collection](https://gcc.gnu.org/) and is further improving it.
GOMP simplifies parallel programming for a broad variety of systems.
This effort operates in an open environment to attract developers and
ensure applicability across multiple architectures and applications.

Traditionally, programmers have used architecture-specific methods to effectively program tightly-parallelized computers — high band-width clusters, SMP machines, or multi-core processors. Parallel programming has thus been a time-consuming and arcane task.

OpenMP offers a simple way of exploiting parallelism without interfering with algorithm design. An OpenMP program compiles and operates correctly in both parallel and serial execution environments. Using OpenMP's directive-based parallelism also simplifies converting existing serial code to efficient parallel code.

OpenMP additionally permits to offload computations to accelerators such as GPUs, making use of their highly parallel computation support. If no accelerator is available, as fallback, the computation is done on the host.

To remain relevant, free software development tools must support emerging technologies. By implementing OpenMP, GOMP provides a simple tool for creating software targeted at parallel architectures. OpenMP's platform-neutral syntax meshes well with the portability goals of GCC and other GNU projects.

GOMP includes a support library (libgomp) and extensions to target language parsers. A long-term goal is the generation of efficient and small code for OpenMP applications.

When support for OpenACC was added, the project name GOMP

was reinterpreted as GNU Offloading and Multi-Processing

instead
of denoting GNU OpenMP

.

We encourage everyone to
[contribute changes](https://gcc.gnu.org/contribute.html)
and help test GOMP. GOMP has been merged into mainline GCC.

Please add openmp

or openacc

to the keywords field when
filing a [bug report](https://gcc.gnu.org/bugs/).

Implementation status in libgomp manual:
[Mainline (GCC 16)](https://gcc.gnu.org/onlinedocs/libgomp/OpenMP-Implementation-Status.html),
[GCC 15](https://gcc.gnu.org/onlinedocs/gcc-15.1.0/libgomp/OpenMP-Implementation-Status.html),
[GCC 14](https://gcc.gnu.org/onlinedocs/gcc-14.2.0/libgomp/OpenMP-Implementation-Status.html),
[GCC 13](https://gcc.gnu.org/onlinedocs/gcc-13.3.0/libgomp/OpenMP-Implementation-Status.html),
[GCC 12](https://gcc.gnu.org/onlinedocs/gcc-12.4.0/libgomp/OpenMP-Implementation-Status.html).

Disclaimer: A feature might be only fully supported in a later GCC version than listed, depending on resolved corner cases and optimizations.

- Supported since GCC 4.2

- Supported since GCC 4.4

- Supported since GCC 4.7

**C/C++:**Supported since GCC 4.9**Fortran:**Supported since GCC 4.9.1

**C/C++:**Supported since GCC 6**Fortran:**Partial support since GCC 7, full support since GCC 11

| Feature | GCC Version | Comments |
|---|---|---|
`in_reduction` clause on task constructs |
|

`depend`

clauses`mutexinoutset`

`depend`

clause`depobj`

construct and depend objects `depend`

clause on `taskwait`

`teams`

construct outside an enclosing target region`if`

, `nontemporal`

and `order(concurrent)`

in `simd`

construct`defaultmap`

extensions`hint`

clause on the `atomic`

construct`atomic`

and `flush`

construct`omp_pause_resource`

and `omp_pause_resource_all`

runtime routines`nonmonotonic`

as default loop schedule modifier for worksharing-loop constructs`atomic`

constructs in `simd`

`task_reduction`

clause with `taskgroup`

`task`

modifier to `reduction`

clause`reduction`

and `in_reduction`

clauses on `taskloop`

and `taskloop simd`

constructs`taskloop`

construct cancelable by `cancel`

construct`requires`

directive`atomic_default_mem_order`

)(

`dynamic_allocators`

)complete but no non-host devices provides

`unified_address`

or
`unified_shared_memory`

complete but no non-host devices provides

`unified_shared_memory`

complete; see also

`conditional`

modifier to `lastprivate`

clause`scan`

directive and `in_scan`

modifier for the `reduction clause`

`order(concurrent)`

clause`loop`

construct`declare variant`

directive`use_device_addr`

clause on `target data`

`declare target`

directive`allocate`

clause`OMP_TARGET_OFFLOAD`

env variableFortran (partial,

`detach`

clause to `task`

construct`omp_fulfill_event`

runtime routine`declare target`

directive`omp_get_supported_active_levels`

routine`in_reduction`

clause on `target`

constructs`nowait`

only stub`affinity`

clause to `task`

construct`close`

`omp_get_device_num`

runtime routine`ancestor`

modifier on `device`

clauseReverse offload supported

(full)

`metadirective`

directive`allocate`

directivealso static variables; C++ unsupported; see also

`target update`

construct`to`

, `from`

and `map`

clauses`declare mapper`

directive| Feature | GCC Version | Comments |
|---|---|---|
| OpenMP directive as C++ attribute specifiers |
|

`nothing`

directive`error`

directive`masked`

construct`scope`

directive`strict`

modifier in the `grainsize`

and `num_tasks`

clauses of the `taskloop`

construct`align`

clause in `allocate`

directive`align`

modifier in `allocate`

clause`thread_limit`

clause to `target`

construct`has_device_addr`

clause to `target construct`

`atomic`

directive`seq_cst`

clause on a `flush`

construct`private`

and `firstprivate`

argument to `default`

clause in C and C++`omp_set_num_teams`

, `omp_set_teams_thread_limit`

, `omp_get_max_teams`

, `omp_get_teams_thread_limit`

runtime routines`omp_calloc`

, `omp_realloc`

, `omp_aligned_alloc`

, and `omp_aligned_calloc`

runtime routines`omp_alloctrait_key_t`

enum: `omp_atv_serialized`

added, `omp_atv_default`

changed`omp_display_env`

runtime routine`OMP_PLACES`

syntax extensions`OMP_NUM_TEAMS`

and `OMP_TEAMS_THREAD_LIMIT`

environment variables`unconstrained`

and `reproducible`

modifiers on `order`

clause`assume`

and `assumes`

directives`inoutset`

argument to the `depend`

clause`omp_target_is_accessible`

runtime routine`omp_target_memcpy_async`

and `omp_target_memcpy_rect_async`

runtime routines`omp_get_mapped_ptr`

runtime routine`omp_all_memory`

reserved locator`nowait`

clause in `taskwait`

directive`begin/end declare target`

syntax in C/C++`target_device`

selector set in context selectors`declare variant`

directive: support elision of preprocessed code and interpret enclosed function definitions as variant functions`declare variant`

: new clauses `adjust_args`

and `append_args`

`dispatch`

construct`target update`

motion clauses and map clauses`interop`

directive`omp_interop_t`

object support in runtime routines`present`

argument to `defaultmap`

clause`ompt_scope_endpoint_t`

enum: `ompt_scope_beginend`

`USE`

,
`IMPORT`

, and `IMPLICIT`

as invalid`#pragma`

form`indirect`

clause in `declare target`

`device_type(nohost)`

/`device_type(host)`

for variables`present`

modifier to the `map`

, `to`

and `from`

clauses`declare target`

and OpenMP context`metadirective`

`declare variant`

`ompt_sync_region_t`

enum additions`ompt_state_t`

enum: `ompt_state_wait_barrier_implementation`

and `ompt_state_wait_barrier_teams`

`ompt_callback_target_data_op_emi_t`

, `ompt_callback_target_emi_t`

, `ompt_callback_target_map_emi_t`

and `ompt_callback_target_submit_emi_t`

`ompt_callback_error_t`

type| Feature | GCC Version | Comments |
|---|---|---|
`omp_in_explicit_task` routine and implicit-task-var ICV |
|

`omp`

/`ompx`

/`omx`

sentinels and `omp_`

/`ompx_`

namespaces`ompx`

/`omx`

sentinels `end`

directive can be on directive`destroy`

clause with `depobj`

`destroy`

clause on `depobj`

`linear`

clause syntax changes and `step`

modifier`map`

modifiers without comma`declare mapper`

with iterator and `present`

modifiers`enter`

clause as alias for `to`

on declare target directive`to`

clause on declare target directive`allocators`

directive for Fortran`allocate`

directive for Fortran allocatables/pointers`end`

directive with `dispatch`

`memspace`

and `traits`

modifiers for `uses_allocators`

`uses_allocators`

`otherwise`

clause as alias for `default`

on metadirectives`default`

clause on metadirectives`declare target`

`order(concurrent)`

`allocate`

and `firstprivate`

clauses on `scope`

`ompt_callback_work`

`map`

clause in `target enter/exit data`

`doacross`

clause as alias for `depend`

with `source`

/`sink`

modifier`depend`

with `source`

/`sink`

modifier`omp_cur_iteration`

keyword`omp_initial_device`

and `omp_invalid_device`

enum/PARAMETER`OMP_TARGET_OFFLOAD=mandatory`

`all`

as `defaultmap`

`init`

clause of the `interop`

construct`mapper`

as map-type modifier in `declare mapper`

[(1)](https://gcc.gnu.org#impl-omp52-ompx) The
`ompx`

sentinel as C/C++ pragma and C++ attributes are warned for
with `-Wunknown-pragmas`

(implied by `-Wall`

) and
`-Wattributes`

(enabled by default), respectively; for Fortran
free-source code, there is a warning enabled by default and, for fixed-source
code, the `omx`

sentinel is warned for with `-Wsurprising`

(enabled by `-Wall`

). Unknown clauses are always rejected with an
error.

| Feature | GCC Version | Comments |
|---|---|---|
| Features deprecated in versions 5.2, 5.1 and 5.0 were removed | N/A | Backward compatibility |
| Full support for C 23 was added |
|

`-std=c2x`

,
since GCC 14 `-std=c23`

)`-std=c++2b`

,
since GCC 14 `-std=c++23`

)`-std=f2023`

)`_ALL`

suffix to the device-scope environment variables`num_threads`

now accepts a list`OMP_NUM_THREADS`

,
`OMP_THREAD_LIMIT`

and `OMP_TEAMS_THREAD_LIMIT`

`OMP_PLACES`

`OMP_DEFAULT_DEVICE`

and new
`OMP_AVAILABLE_DEVICES`

environment vars`uid`

trait for target devices and for
`OMP_AVAILABLE_DEVICES`

and `OMP_DEFAULT_DEVICE`

`OMP_THREADS_RESERVE`

environment variable`decl`

attribute was added to the C++ attribute syntax`do concurrent`

`adjust_args`

clause was extended to specify the argument by
position and supports variadic arguments`interop`

operation of `append_args`

,
allowing all modifiers of the `init`

clause`depobj`

with repeatable clauses
and the `init`

clause`depend`

clause of
the argument version of the `depend`

construct`looprange`

clause`private`

not supported`taskgraph`

construct including `saved`

modifier
and `replayable`

clause`default`

clause on the target directive and accepting
variable categories`use_device_ptr`

and `use_device_addr`

`reduction`

clause`init_complete`

clause to the `scan`

directive`ref`

modifier to the `map`

clause`storage`

map-type modifier; context-dependent
`alloc`

and `release`

are aliases`self`

modifier to `map`

and `self`

as `defaultmap`

argument`delete`

as delete-modifier not as map type`automap`

modifier to the `enter`

clause of `declare_target`

`groupprivate`

directive`local`

clause to `declare_target`

directive`part_size`

allocator trait for `interleaved`

allocator partitions`pin_device`

, `preferred_device`

and `target_access`

allocator traits`access`

allocator trait changes`partitioner`

value to `partition`

allocator trait`uses_allocators`

`need_device_addr`

modifier to `adjust_args`

clause`interop`

clause to `dispatch`

`declare_target`

`message`

and `severity`

clauses to
`parallel`

directive`self_maps`

clause to `requires`

directive`no_openmp_constructs`

assumptions clause`ordered`

regarding loop-transforming directives`apply`

clause to loop-transforming constructs`fuse`

loop-transformation construct`interchange`

loop-transformation construct`reverse`

loop-transformation construct`split`

loop-transformation construct`stripe`

loop-transformation construct`tile`

permitting association of grid and inter-tile loops`strict`

modifier keyword to `num_threads`

`safesync`

clause to the `parallel`

construct`omp_curr_progress_width`

identifier`omp_get_max_progress_width`

runtime routine`order(concurrent)`

and, hence,
the `loop`

construct`atomic`

permitted in a construct with
`order(concurrent)`

`order(concurrent)`

`workdistribute`

directive for Fortran`DO CONCURRENT`

as associated loop
in a `loop`

construct`task_iteration`

directive inside `taskloop`

`threadset`

clause in task-generating constructs`priority`

clause to `target`

,
`target_enter_data`

, `target_data`

,
`target_exit_data`

and `target_update`

`device_type`

clause to the `target`

directive`target_data`

as composite construct`nowait`

clause with reverse-offload `target`

directives`init`

clause`nowait`

and `nogroup`

may be non constant`memscope`

clause to `atomic`

and `flush`

`transparent`

clause for multi-generational
task-dependence graphs`cancel`

construct now completes tasks
with unfulfilled events`omp_fulfill_event`

routine was restricted
regarding fulfillment of event variables`omp_is_free_agent`

and
`omp_ancestor_is_free_agent`

routines`omp_get_device_from_uid`

and
`omp_get_uid_from_device`

routines`omp_get_device_num_teams`

,
`omp_set_device_num_teams`

,
`omp_get_device_teams_thread_limit`

, and
`omp_set_device_teams_thread_limit`

routines`omp_target_memset`

and
`omp_target_memset_async`

routines`omp_get_memspace_num_resources`

routine`omp_get_memspace_pagesize`

routine`omp_get_submemspace`

routine`omp_init_mempartitioner`

,
`omp_destroy_mempartitioner`

,
`omp_init_mempartition`

,
`omp_destroy_mempartition`

,
`omp_mempartition_set_part`

,
`omp_mempartition_get_user_data`

routines`target_data_op`

, `target`

,
`target_map`

and `target_submit`

callbacks
and as values that `set_callback`

must return`ompt_target_data_transfer`

and
`ompt_target_data_transfer_async`

values in
`ompt_target_data_op_t`

enum`ompt_target_data_transfer_to_device`

,
`ompt_target_data_transfer_from_device`

,
`ompt_target_data_transfer_to_device_async`

and
`ompt_target_data_transfer_from_device_async`

of
the `target_data_op`

OMPT type were deprecated`ompt_get_buffer_limits`

OMPT routine| Feature | GCC Version | Comments |
|---|---|---|
| Deprecation of omitting the optional white space to separate adjacent keywords in the directive-name in Fortran (fixed and free source form) | No | |
Deprecation of the combiner expression in the
`declare_reduction` argument |
No | |
Deprecation of the Fortran include file `omp_lib.h` |
No |

| Feature | GCC Version | Comments |
|---|---|---|
| Multi-word directives now use underscore by default | No | |
Relaxed Fortran restrictions to the `aligned` clause |
No | |
| Mapping lambda captures | No | |
New `omp_pause_stop_tool` constant for
`omp_pause_resource` |
No | |
| In Fortran (fixed and free source form), spaces between directive names are mandatory | No | |
Update of the map-type decay for mapping and
`declare_mapper` |
No |

Technical Report (TR) 14 is the first preview for OpenMP 6.1.

| Feature | GCC Version | Comments |
|---|---|---|
The `depth` clause to `fuse` directive |
No | |
The `attach` modifier to the `map` clause |
No | |
The `dyn_groupprivate` clause and the
`omp_get_dyn_groupprivate_ptr` , `omp_get_dyn_groupprivate_size` ,
and `omp_get_dyn_groupprivate_size` routines |
No | |
`begin declare_variant` directive in Fortran |
No | |
`grid` and `tile` modifier to the `size` clause |
No | |
New `flatten` loop-transforming directive |
No | |
`scaled` modifier to `simdlen` clause |
No | |
New `omp_default_device` identifier as conforming device number |
|

`omp_target_is_accessible`

routine returns zero| Feature | GCC Version | Comments |
|---|---|---|
| Deprecation of conditional-update-capture structured block without a capture statement | No |

**November 13, 2025**OpenMP Technical Report 14 (first preview for the OpenMP API Version 6.1) has been released [

[PDF](https://www.openmp.org/wp-content/uploads/openmp-TR14.pdf),[specifications site](https://www.openmp.org/specifications/)].**November 14, 2024**[OpenMP Version 6.0](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-6-0.pdf)has been released.**August 1, 2024**[OpenMP Technical Report 13 (third preview for the OpenMP API Version 6.0)](https://www.openmp.org/wp-content/uploads/openmp-TR13.pdf)has been released.**November 9, 2023**[OpenMP Technical Report 12 (second preview for the OpenMP API Version 6.0)](https://www.openmp.org/wp-content/uploads/openmp-TR12.pdf)has been released.**November 9, 2022**[OpenMP Technical Report 11 (first preview for the OpenMP API Version 6.0)](https://www.openmp.org/wp-content/uploads/openmp-TR11.pdf)has been released.**November 9, 2021**[OpenMP Version 5.2](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf)has been released.**July 15, 2021**[OpenMP Technical Report 10: Version 5.2 Public Comment Draft](https://www.openmp.org/wp-content/uploads/openmp-TR10.pdf)has been released.**November 13, 2020**[OpenMP Version 5.1](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-1.pdf)has been released.**August 20, 2020**[OpenMP Technical Report 9: Version 5.1 Public Comment Draft](https://www.openmp.org/wp-content/uploads/openmp-TR9.pdf)has been released.**May 7, 2020**[GCC 10 has been released](https://gcc.gnu.org/gcc-10/). It adds a number of newly implemented OpenMP 5.0 features on top of the GCC 9 release such as`conditional`

`lastprivate`

clause,`scan`

and`loop`

directives,`order(concurrent)`

and`use_device_addr`

clauses support,`if`

clause on`simd`

construct or partial support for the`declare variant`

directive, getting closer to full support of the OpenMP 5.0 standard.**May 3, 2019**[GCC 9 has been released](https://gcc.gnu.org/gcc-9/)and version 5.0 of the OpenMP specification is now partially supported in the C and C++ compilers. For details which features of OpenMP 5.0 are and which are not supported in the GCC 9 release see[this mail](https://gcc.gnu.org/legacy-ml/gcc-patches/2018-11/msg00628.html).**November 8, 2018**The

[OpenMP v5.0](https://www.openmp.org/specifications/)specification has been released.**May 2, 2017**[GCC 7 has been released](https://gcc.gnu.org/gcc-7/)and version 4.5 of the OpenMP specification is now partially supported in the Fortran compiler; the largest missing item is structure element mapping.**April 27, 2016**[GCC 6 has been released](https://gcc.gnu.org/gcc-6/)and version 4.5 of the OpenMP specification is now supported in the C and C++ compilers.**November 14, 2015**The final

[OpenMP v4.5](https://www.openmp.org/wp-content/uploads/openmp-4.5.pdf)specification has been released.**October 13, 2015**The

`gomp-4_1-branch`

has been merged into mainline, so GCC 6 and later will feature OpenMP v4.5 support for C and C++.**June 30, 2014**Fortran OpenMP v4.0 support has been backported to

`gcc-4_9-branch`

and will be available in the upcoming GCC 4.9.1 release.**June 18, 2014**The last major part of Fortran OpenMP v4.0 support has been committed into mainline.

**October 11, 2013**The

`gomp-4_0-branch`

has been merged into mainline, so GCC 4.9 and later will feature OpenMP v4.0 support for C and C++.**July 23, 2013**The final OpenMP v4.0 specification has been released.

**August 2, 2011**The

`gomp-3_1-branch`

has been merged into mainline, so GCC 4.7 and later will feature OpenMP v3.1 support.**July 9, 2011**The final OpenMP v3.1 specification has been released.

**February 6, 2011**A draft of the OpenMP v3.1 specification has been released for public review. The

`gomp-3_1-branch`

branch has been created and work began on implementing v3.1 support.**June 6, 2008**The

`gomp-3_0-branch`

has been merged into mainline, so GCC 4.4 and later will feature OpenMP v3.0 support.**May 12, 2008**The final OpenMP v3.0 specification has been released.

**October 22, 2007**Draft of the OpenMP v3.0 specification has been released for public review, the

`gomp-3_0-branch`

branch has been created and work began on implementing v3.0 support.**March 9, 2006**The branch has been merged into mainline, so starting with GCC 4.2 the compiler supports the OpenMP v2.5 specification.

**November 18, 2005**The branch is ready to be merged into mainline. All three front ends are functional and there should not be many corners of the standard left to implement. There are 5 main modules to merge into mainline: (1) runtime library, (2) code generation, (3) C front end, (4) C++ front end, and, (5) Fortran front end.

**October 20, 2005**The runtime library is functionally complete. The syntax parsers for C, C++ and Fortran are complete, though there are still dusty corners with respect to semantic translation to be resolved. Adventurous users who don't mind the compiler crashing on every other source file are encouraged to begin filing bugs.


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
Last modified 2026-01-20.
