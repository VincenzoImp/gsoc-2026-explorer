# Issue tracker

**Parent:** Ste||ar group — Project Ideas
**Source:** https://github.com/STEllAR-GROUP/hpx/issues
**Scraped:** 2026-02-22T23:28:47.614141

---

## #6931: Two correctness bugs in  chunk_size.hpp : swapped next_or_subrange args and mismatched  add_ready_future_idx  parameter order

While reviewing:

    libs/core/algorithms/include/hpx/parallel/util/detail/chunk_size.hpp

I found two silent correctness bugs affecting bulk iteration shape handling.


Bug 1 — Swapped arguments in next_or_subrange (variable chunk path)
===============================================================================

Location:
    get_bulk_iteration_shape_variable (around line 320)

Signature:
    constexpr auto next_or_subrange(IterOrR const& target,
        std::size_t offset, std::size_t size)

Current code:

    std::size_t chunk = (std::min)(chunk_size, count);
    shape.emplace_back(it_or_r, chunk);
    chunk = (std::min)(count, chunk);
    count -= chunk;
    it_or_r = next_or_subrange(it_or_r, count, chunk);  // BUG

Issue:
At this point `count` has already been decremented and represents the
remaining elements, not the advance distance.

The iterator should advance by `chunk`, but instead advances by the
remaining `count`, leading to incorrect range progression.

Correct form:

    it_or_r = next_or_subrange(it_or_r, chunk, count);

This matches the correct usage in the other overload (line ~214).

Impact:
- Any algorithm using the variable-chunk-size path (std::true_type)
- Multi-chunk scenarios silently process incorrect ranges
- No compile-time warning


Proposed Fix:
- Swap the two arguments at line ~320
- Add a unit test ensuring multi-chunk iteration visits all elements exactly once



Bug 2 — Parameter order mismatch in add_ready_future_idx
===============================================================================

Location:
    Overloads for add_ready_future_idx (lines ~366–380)

Correct overload (future<void>):

    void add_ready_future_idx(std::vector<hpx::future<void>>& workitems,
        F&& f, FwdIter first, std::size_t base_idx, std::size_t count)

Incorrect overload (shared_future<void>):

    void add_ready_future_idx(
        std::vector<hpx::shared_future<void>>& workitems,
        F&& f, std::size_t base_idx, FwdIter first, std::size_t count)
           // base_idx and first swapped

Problem:
Call sites pass arguments in the order:

    (first, base_idx, count)

This matches the future<void> overload, but in the shared_future<void>
case the parameters are reversed, potentially binding:

    first → base_idx
    base_idx → first

This leads to undefined behavior passed silently into the kernel.

Corrected version:

    void add_ready_future_idx(
        std::vector<hpx::shared_future<void>>& workitems,
        F&& f, FwdIter first, std::size_t base_idx, std::size_t count)
    {
        HPX_FORWARD(F, f)(first, count, base_idx);
        workitems.push_back(hpx::make_ready_future());
    }

Impact:
- Silent UB when shared_future<void> workitems are used
- Incorrect base_idx propagation in indexed iteration shapes


Proposed Fix:
- Reorder parameters of the shared_future<void> overload
- Add test covering shared_future<void> path via
  get_bulk_iteration_shape_idx
- Optionally document required parameter order to pr

*[truncated]*

---

## #6922: fork_join_executor silently truncates ranges > 2^32

**Labels:** type: defect, category: executors

Summary
-------

fork_join_executor currently truncates iteration ranges to 32-bit
indices. When size > UINT32_MAX (~4.29B), indices wrap silently,
causing incorrect results with no warning or exception.

This affects both static and dynamic scheduling paths.


Root Cause
----------

1) Static scheduling:
   In fork_join_executor.hpp, partition boundaries are cast to
   std::uint32_t:

       auto const part_begin = static_cast<std::uint32_t>(...);
       auto const part_end   = static_cast<std::uint32_t>(...);

   If size > UINT32_MAX, part_begin/part_end wrap.

2) Dynamic scheduling:
   contiguous_index_queue is hardcoded to 32-bit indices via:

       static_assert(sizeof(T) <= 4, ...);

   It packs two 32-bit indices into a 64-bit atomic, so 64-bit
   ranges are fundamentally unsupported.


Impact
------

- Silent incorrect results for large ranges
- Affects for_each, transform, reduce, etc.
- Particularly problematic for HPC workloads


Proposed Fix
------------

Immediate (correctness):

1) For loop_schedule::static_:
   Replace std::uint32_t with std::size_t in partition calculations.

2) For loop_schedule::dynamic:
   Add runtime guard:

       if (size > std::numeric_limits<std::uint32_t>::max())
           throw std::overflow_error(
               "fork_join_executor: dynamic scheduling "
               "not supported for ranges > 2^32");

Long-term:
- Either implement a 64-bit index queue (128-bit CAS), or
- Provide a lock-based fallback for 64-bit indices.

---

## #6908: Implement missing C++23 range algorithms: fold, chunk_by, slide, stride, cartesian_product

**Labels:** category: algorithms

Proposal: Implement Missing C++23 Range Algorithms and Views
===============================================================================

Overview
-------------------------------------------------------------------------------

I would like to work on implementing several C++23 range algorithms that are
currently missing in HPX.

This will help move HPX closer to full C++23 standard compliance and provide
users with additional modern tools for working with ranges.


Planned Additions
===============================================================================

1) Fold Algorithms (P2322R6)
-------------------------------------------------------------------------------

ranges::fold_left family:
    - fold_left
    - fold_left_with_iter
    - fold_left_first
    - fold_left_first_with_iter

ranges::fold_right family:
    - fold_right
    - fold_right_last


2) Range Adaptors / Views
-------------------------------------------------------------------------------

- views::chunk_by        (P2443R1)
- views::slide           (P2442R1)
- views::stride          (P1899R3)
- views::cartesian_product (P2374R4)
- views::repeat          (P2474R2)


Implementation Plan
===============================================================================

- Implement fold algorithms as Customization Point Objects (CPOs)
  using hpx::tag_invoke, following the pattern used in reduce.

- Place implementations under:
    hpx/parallel/container_algorithms   (for fold algorithms)
    hpx/parallel/util                   (for views)

- Ensure support for:
    - sequenced execution policy
    - parallel execution policy
    - parallel unsequenced execution policy

- Add unit tests for each algorithm/view covering:
    - Basic correctness
    - Sequential execution
    - Parallel execution
    - Edge cases (e.g., empty ranges)

---

## #6906: Add missing subtraction unit tests for gid_type

**Labels:** category: tests

## Add missing subtraction unit tests for `gid_type`

The file `libs/full/naming_base/tests/unit/gid_type.cpp` contains a TODO comment (line 17) indicating that subtraction tests for the `gid_type` class are still missing.

While the test suite currently covers many operations, there is no unit test coverage for the subtraction operator.

---

### Existing test coverage

The current tests include:

- Constructor and retrieval tests  
- Assignment tests  
- Equality / inequality tests  
- Comparison operators (`<`, `<=`, `>`, `>=`)  
- Increment operators (pre and post)  
- Addition operator (`operator+`)  
- Logical shift operations  
- Boolean conversion  

However:

- ❌ Subtraction operator (`operator-`) — **not tested**

---

###  Motivation

The `gid_type` class defines `operator-` (see `gid_type.hpp`, line 42), but its behavior is currently not validated by unit tests. Adding coverage would help ensure correctness and prevent regressions.

---

### Proposed additions

Add comprehensive subtraction tests covering:

- Basic subtraction operations  
- Boundary cases (e.g., borrowing across 64-bit boundaries)  
- Edge cases:
  - Subtracting a value from itself  
  - Subtracting large values  
- Verification that subtraction does not mutate operands  

Tests should follow the structure and conventions used in the existing `gid_type.cpp` test file.

---

###  Additional context

This would improve test completeness and operator coverage for `gid_type`.

---

## #6905: Split fast path ignores receiver’s scheduler leading to mismatched completion thread

**Labels:** type: defect, category: senders/receivers

**Problem**
When split replays a cached result on the fast path (`predecessor_done == true`), it calls `set_value` inline on the thread that calls `add_continuation()`. This ignores the receiver’s completion scheduler returned by `get_completion_scheduler<set_value_t>`(get_env(receiver)).

There is a TODO in [split.hpp#L349](https://github.com/STEllAR-GROUP/hpx/blob/ca5f46db81fab10ebbeb0fa15640b1f60e2ec482/libs/core/execution/include/hpx/execution/algorithms/split.hpp#L349) around the fast-path that mentions preserving the scheduler, but the current implementation does not propagate it.

**Observed behavior from a demo file**
```
shlokjain@Shloks-MacBook-Pro-2 hpx %  /Users/shlokjain/hpx/split_fastpath_scheduler_violation_demo
=== split fast-path scheduler mismatch (HPX split only) ===

Predecessor completed on thread 0x1eecea0c0 with value=42

UI scheduler thread id : 0x16d3cb000
Main thread id          : 0x1eecea0c0

Connecting split sender from MAIN thread to a receiver that expects the UI scheduler...

set_value called with value=42
  expected scheduler(UI) thread id: 0x16d3cb000
  actual completion thread id     : 0x1eecea0c0
  match? NO

Demo finished.
```

**Reproduce**
[Minimal standalone demo](https://gist.github.com/shlokjain2031/cd8fd6298be71c2a9fc8d5f2e09f8daf)

---

## #6904: reduce lock contention in local_priority_queue_scheduler via randomized victim selection

**Labels:** category: scheduler

Motivation
===============================================================================

Currently, the local_priority_queue_scheduler (the default scheduler in HPX)
iterates through the list of potential victim threads starting from index 0
for every steal attempt.

This deterministic access pattern can lead to a "thundering herd" problem,
where multiple idle threads simultaneously attempt to steal from the same
few victims (typically neighboring threads). As a result:

- High contention occurs on a small subset of queues.
- Cache-line bouncing increases.
- Overall throughput may decrease under high contention.

To mitigate this behavior, we introduce a lightweight mechanism that
breaks the deterministic lock-step victim selection.


Proposed Change
===============================================================================

Instead of always starting the victim search from index 0 of victim_threads_,
we introduce a per-thread atomic offset:

    victim_offset_[thread_id]

On each steal attempt, the thread performs:

    std::size_t offset =
        victim_offset_[thread_id].data_.fetch_add(1, std::memory_order_relaxed);

The starting victim index is then calculated as:

    std::size_t start = (index + offset) % victim_count;

This creates a round-robin style rotation of victim selection.


Behavioral Impact
===============================================================================

- Distributes steal attempts more evenly across victims.
- Reduces contention on neighboring queues.
- Prevents deterministic synchronization of steal attempts.
- Maintains minimal runtime overhead.
- Preserves existing stealing logic and semantics.


Implementation Details
===============================================================================

1. Added the following member to local_priority_queue_scheduler:

    std::vector<
        util::cache_line_data<std::atomic<std::size_t>>
    > victim_offset_;

2. Initialized victim_offset_ in the scheduler constructor.

3. Updated the following functions to use the rotating offset:

    - attempt_stealing()
    - attempt_stealing_pending()

Each function now:
    - Performs a relaxed fetch_add(1) on victim_offset_[thread_id]
    - Computes a rotated starting index
    - Iterates through victims starting from that offset


Design Rationale
===============================================================================

This approach was use as a lightweight alternative to full randomization or more complex heuristics.

It avoids:
- Costly RNG calls
- Additional synchronization
- Complex scheduling heuristics

---

## #6895: Add exception handling in AGAS namespace server iterate methods

**Labels:** category: AGAS, type: feature request

There are TODO comments indicating missing exception handling in the AGAS base namespace servers:

1. `libs/full/agas_base/src/server/component_namespace_server.cpp` (line 281)
2. `libs/full/agas_base/src/server/symbol_namespace_server.cpp` (line 279)

// TODO: catch exceptions
void component_namespace::iterate_types(
    iterate_types_function_type const& f)
{
    // ... implementation without try-catch
}

Suggested Fix
Wrap the iteration logic in appropriate try-catch blocks to handle potential exceptions gracefully, following HPX's error handling patterns

---

## #6881: Asynchronous channel communicator construction

**Labels:** type: defect, category: components, category: init

## Expected Behavior

The code passes ,`hpx::collectives::create_channel_communicator` on each locality is constructed.

```c++
#include <hpx/hpx_main.hpp> // IWYU pragma: keep

#include <cstddef>  // for size_t, ptrdiff_t
#include <iostream> // for cout
#include <vector>   // for vector

#include <hpx/actions/base_action.hpp>              // for HPX_REGISTER_ACTION_2
#include <hpx/actions_base/plain_action.hpp>        // for HPX_PLAIN_ACTION
#include <hpx/async_distributed/async.hpp>          // for async
#include <hpx/collectives/argument_types.hpp>       // for that_site_arg, num_sites_arg
#include <hpx/collectives/channel_communicator.hpp> // for channel_communicator, get, set
#include <hpx/hpx_finalize.hpp>            // for terminate
#include <hpx/iostream.hpp>                // for cout, ostream
#include <hpx/naming_base/id_type.hpp>     // for id_type
#include <hpx/runtime.hpp>                 // for find_all_localities, get_os_thread_count
#include <hpx/serialization/serialize.hpp> // for operator>>, operator<<

void hpx_channel_communicator_test() {
    using hpx::collectives::num_sites_arg, hpx::collectives::that_site_arg;
    constexpr auto channel_communicator_name = "test/";
    const std::uint32_t n_localities = hpx::get_initial_num_localities();
    auto comm = hpx::collectives::create_channel_communicator(hpx::launch::sync,
                    channel_communicator_name, num_sites_arg(n_localities));
}

HPX_PLAIN_ACTION(hpx_channel_communicator_test, HPXChannelCommunicatorTestAction)

int main() {
    const std::vector<hpx::id_type> localities = hpx::find_all_localities();
    std::cout << localities.size() << " localities are used.\n";
    std::vector<hpx::future<void>> futures;
    futures.reserve(localities.size());
    for (const auto& locality : localities) {
        futures.push_back(hpx::async<HPXChannelCommunicatorTestAction>(locality));
    }
    hpx::wait_all(futures);
    std::cout<<"Done\n";
    return 0;
}
```

## Actual Behavior

Often hangs. The issue occurred when updating from HPX 1.10 to 1.11 

## Steps to Reproduce the Problem

Run `./my_app`

Sometimes multiple runs are required to catch the issue.

Observation: the hanging seems not to occur when (by luck) the construction happens on the localities in order Loc0, Loc1, Loc2.

Changing
```c++
auto comm = hpx::collectives::create_channel_communicator(hpx::launch::sync,
                    channel_communicator_name, num_sites_arg(n_localities));
```
to 
```c++
auto comm = hpx::collectives::create_channel_communicator(channel_communicator_name, num_sites_arg(n_localities)).get()`
 ```
solves the issue, but if this is the intended way, it does not quite follow from the documentation.

## Specifications

  - HPX Version: 1.11.0
  - Platform (compiler, OS, Architecture): g++13.2.0, Ubuntu 24.04.1 LTS, x86_64
  - Platform2 : macOS 15.6.1, clang-1700.0.13.5, arm64-apple-darwin24.6.0.

---

## #6878: Parallel uninitialized_relocate does not preserve sequenced semantics for overlapping ranges

**Labels:** type: defect, category: algorithms

The parallel overloads of `hpx::experimental::uninitialized_relocate` and uninitialized_relocate_backward do not preserve the same ordering semantics as the sequenced implementation when the source and destination ranges overlap.

While overlapping ranges are only well-defined when the caller selects the correct direction (analogous to `std::copy` vs `std::copy_backward),` the parallel implementations may reorder relocations due to chunk-based parallelization. This can lead to observable differences in object lifetime and final memory layout compared to `hpx::execution::seq.`

**Expected behavior:**
For a given algorithm (`uninitialized_relocate` or `uninitialized_relocate_backward`), parallel execution should preserve the same behavior as the sequenced implementation, even for overlapping contiguous ranges.

**Actual behavior:**
When using `hpx::execution::par`, overlapping contiguous ranges may be relocated in a different order than the sequenced algorithm, resulting in differences in object state and lifetime.

---

## #6867: v1.11.0 fails to build on F44

**Labels:** type: defect

From https://bugzilla.redhat.com/show_bug.cgi?id=2434647:
```
template argument deduction/substitution failed:
                • error: type/value mismatch at argument 1 in template parameter list for ‘template<class _Tp, class ... _Types> constexpr _Tp&& std::get(tuple<_Elements ...>&&)’
```

See [build.log.zip](https://github.com/user-attachments/files/24984206/build.log.zip)

---

## #6793: Performance in recursive fork-join is very bad

**Labels:** category: executors

I maintain a set of benchmarks to compare the performance of executors. https://github.com/tzcnt/runtime-benchmarks currently it mostly tracks fork-join performance. I have recently added HPX to this benchmark suite in PR https://github.com/tzcnt/runtime-benchmarks/pull/4.

I was shocked to discover that HPX on average is 900x slower than the fastest runtime. See the summary table on the repo README, or the full dataset chart here: https://fleetcode.com/runtime-benchmarks/ Note that I have only run this on one machine so far (with 128GB ram) - because on a different machine, it would take literally hours to complete the benchmark run, or run out of memory... whereas the competing runtimes can complete a benchmark run in a few minutes.

You can read the PR description above for a complete description of all the things that I tried, but the summary is that I wasn't able to achieve reasonable performance despite spending many hours trying different approaches.

I also discovered that the `abp-priority-lifo` scheduler is broken and doesn't actually use the correct scheduling policy. I had to manually edit [this line](https://github.com/STEllAR-GROUP/hpx/blob/f23dba500a506bea052bde15755c223d8d2ba7c0/libs/core/threadmanager/src/threadmanager.cpp#L437) to reference `hpx::threads::policies::lockfree_abp_lifo` instead, after which I was able to I verify that the correct scheduler was being used.

I expected that this would solve the problem as the memory blowup that I observed is usually what happens when runtimes use strictly FIFO scheduling, which can result in e.g. for Skynet, 10^8 = 100,000,000 active tasks maximum, rather than 10*8 = 80 active tasks maximum when using LIFO scheduling for the local task queue. I thought that the `lockfree_abp_lifo` policy would prevent this problem, but it didn't make any impact.

I see this issue https://github.com/STEllAR-GROUP/hpx/issues/3348 and this PR https://github.com/STEllAR-GROUP/hpx/pull/4744 but I'm not sure if this would resolve this problem.

I'd also like to note that 3 of the benchmarks I'm running have nearly equivalent implementations in your examples, so I'd expect that it would be possible to make these run in a performant manner.
https://github.com/STEllAR-GROUP/hpx/blob/master/examples/quickstart/fibonacci_one.cpp
https://github.com/STEllAR-GROUP/hpx/blob/master/tests/performance/local/skynet.cpp
https://github.com/STEllAR-GROUP/hpx/tree/master/examples/nqueen

I'd like to give you an opportunity to present your library in the best light, so I'm open to any feedback on how I can optimize my implementation / build flags to make HPX perform better.

---

## #6765: v1.10.0: tests fail on ppc64le & s390x

**Labels:** type: defect, platform: s390x

In an attempt to fix https://bugzilla.redhat.com/show_bug.cgi?id=2381020:
```diff
diff --git a/hpx.spec b/hpx.spec
index 94548c3..cadca25 100644
--- a/hpx.spec
+++ b/hpx.spec
@@ -215,7 +216,7 @@ rm %{buildroot}/%{_datadir}/%{name}/LICENSE_1_0.txt
 . /etc/profile.d/modules.sh
 for mpi in '' openmpi mpich ; do
   test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
-  make -C %{__cmake_builddir}/ tests.examples
+  %ctest --tests-regex tests.examples
   test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
 done
```

I realized we actually never ran the tests during the rpm build after enabling the test we get:
Pass: buildArch (hpx-1.10.0-7.fc44.src.rpm, x86_64)
Pass: buildArch (hpx-1.10.0-7.fc44.src.rpm, aarch64)
Fail: buildArch (hpx-1.10.0-7.fc44.src.rpm, ppc64le)
Fail: buildArch (hpx-1.10.0-7.fc44.src.rpm, s390x)
(see https://koji.fedoraproject.org/koji/taskinfo?taskID=135996561)

In the ppc64le build log it has:
```
98% tests passed, 2 tests failed out of 120
Total Test time (real) =  63.65 sec
The following tests FAILED:
        1088 - tests.examples.1d_stencil.1d_stencil_4_parallel (Failed)
        1091 - tests.examples.1d_stencil.1d_stencil_7 (Failed)
Errors while running CTest
```
with
``` 38/120 Test #1091: tests.examples.1d_stencil.1d_stencil_7 ......................................................***Failed    0.14 sec
pure virtual method called
terminate called without an active exception
Base command is "/builddir/build/BUILD/hpx-1.10.0-build/hpx-1.10.0/ppc64le-redhat-linux-gnu-serial/bin/1d_stencil_7 --hpx:threads=4"
Executing command: /builddir/build/BUILD/hpx-1.10.0-build/hpx-1.10.0/ppc64le-redhat-linux-gnu-serial/bin/1d_stencil_7 --hpx:threads=4
Process 0 failed with an unexpected error code of 255 (expected 0) <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
```
and
```
35/120 Test #1088: tests.examples.1d_stencil.1d_stencil_4_parallel .............................................***Failed    0.12 sec
...
{what}: Segmentation fault
Base command is "/builddir/build/BUILD/hpx-1.10.0-build/hpx-1.10.0/ppc64le-redhat-linux-gnu-serial/bin/1d_stencil_4_parallel --hpx:threads=4"
Executing command: /builddir/build/BUILD/hpx-1.10.0-build/hpx-1.10.0/ppc64le-redhat-linux-gnu-serial/bin/1d_stencil_4_parallel --hpx:threads=4
Process 0 failed with an unexpected error code of 255 (expected 0) <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
```

Build log:  [build_ppc64le.txt.zip](https://github.com/user-attachments/files/21756047/build_ppc64le.txt.zip)

s390x is much worse:
```
11% tests passed, 107 tests failed out of 120
Total Test time (real) = 4511.38 sec
```

Build log:  [build_s390x.txt.zip](https://github.com/user-attachments/files/21756080/build_s390x.txt.zip)

---

## #6745: Forward `stdexec::bulk` in HPX to support full S/R NVIDIA's integration implementation

`stdexec::bulk` and `stdexec::bulk_t` are not forwarded in `libs/core/execution_base/include/hpx/execution_base/stdexec_forward.hpp`

---

## #6743: flecsi: New hangs with HPX 1.11.0

**Labels:** type: defect, project: FLeCSI

We're observing new, consistent hangs in FleCSI in the `data-index` unit test when switching from HPX 1.10.0 to 1.11.0. 

Our Spack environment:

```yaml
spack:
  specs:
  - flecsi
  view:
    default:
      exclude:
      - gcc-runtime
      root: .spack-env/view
  packages:
    boost:
      require:
      - +debug
      - cxxstd=17 +program_options
      prefer:
      - '@1.88.0'
    c:
      prefer:
      - gcc
    cxx:
      prefer:
      - gcc
    flecsi:
      require:
      - spec: backend=hpx build_type=Debug caliper_detail=low +flog +graphviz %gcc
        when: '@2.4:'
    fortran:
      prefer:
      - gcc
    hpx:
      require:
      - build_type=Debug
      prefer:
      - '@1.11.0'
    kokkos:
      require:
      - +serial~openmp~cuda~rocm
      prefer:
      - '@4.6.01'
    mpi:
      require:
      - mpich
    cmake:
      prefer:
      - '@3.31.6'
    graphviz:
      prefer:
      - '@12.1.0'
      require:
      - +poppler+pangocairo %gcc
    py-sphinx:
      prefer:
      - '@8.2.0'
    hdf5:
      prefer:
      - '@1.14.6'
    metis:
      require:
      - '@5.1.0'
    parmetis:
      require:
      - '@4.0.3'
    mpich:
      prefer:
      - '@4.3.0'
      require:
      - +hydra +slurm +fortran device=ch4 netmod=ucx %c,cxx,fortran=gcc
    ucx:
      prefer:
      - '@1.18.0'
      require:
      - +cma+dc+rc+rdmacm+thread_multiple+ud+verbs+debug %c,cxx=gcc
```

Concretized:

```console
$ spack spec
 -   flecsi@2.4.develop~cuda~doc+flog~format+graphviz~hdf5~ipo~rocm+shared backend=hpx build_system=cmake build_type=Debug caliper_detail=low commit=77f5313b54f6782ec2a57002ce1a9f4f35641da8 generator=make arch=linux-rhel8-broadwell %c,cxx=gcc@13.2.0
[+]      ^boost@1.88.0+atomic~charconv+chrono~clanglibcpp~cobalt~container~context~contract~coroutine+date_time+debug+exception~fiber+filesystem+graph~graph_parallel+icu+iostreams~json+locale+log+math~mpi~mqtt5+multithreaded~nowide~numpy~pic+program_options~python+random+regex+serialization+shared+signals~singlethreaded+stacktrace+system~taggedlayout+test+thread+timer~type_erasure~url~versionedlayout+wave build_system=generic cxxstd=17 patches:=a440f96 visibility=hidden arch=linux-rhel8-broadwell %c,cxx=gcc@13.2.0
[+]          ^bzip2@1.0.8~debug~pic+shared build_system=generic arch=linux-rhel8-broadwell %c=gcc@13.2.0
[e]              ^diffutils@3.6 build_system=autotools arch=linux-rhel8-broadwell
[+]          ^icu4c@76.1 build_system=autotools cxxstd=17 arch=linux-rhel8-broadwell %c,cxx=gcc@13.2.0
[+]          ^xz@5.6.3~pic build_system=autotools libs:=shared,static arch=linux-rhel8-broadwell %c=gcc@13.2.0
[+]          ^zlib-ng@2.2.4+compat+new_strategies+opt+pic+shared build_system=autotools arch=linux-rhel8-broadwell %c,cxx=gcc@13.2.0
[+]          ^zstd@1.5.7+programs build_system=makefile compression:=none libs:=shared,static arch=linux-rhel8-broadwell %c,cxx=gcc@13.2.0
[+]      ^caliper@2.12.1+adiak~cuda~fortran+gotcha~ipo+kokkos+libdw~libpfm+libunwind+mpi+papi~python~rocm+sample

*[truncated]*

---

## #6742: Preparing V1.11.1

**Labels:** type: cleanup

Here is a list of PRs that should be retargeted for V1.11.1"

- [ ] https://github.com/STEllAR-GROUP/hpx/pull/6731
- [ ] https://github.com/STEllAR-GROUP/hpx/pull/6737
- [ ] https://github.com/STEllAR-GROUP/hpx/pull/6738
- [ ] https://github.com/STEllAR-GROUP/hpx/pull/6748
- [ ] https://github.com/STEllAR-GROUP/hpx/pull/6749
- [ ] https://github.com/STEllAR-GROUP/hpx/pull/6766

---

## #6740: HPX headers in device builds

**Labels:** type: defect, platform: CUDA, platform: HIP, platform: ROCm

GPU kernels cannot appear in translation units that make any non-trivial use of HPX, because many HPX declarations are removed by the preprocessor when compiling for the device.  Obviously many HPX features cannot be used on a GPU, but the implicit `__host__` everywhere should generally be sufficient to enforce that without having simple name lookup fail in any class that uses HPX in one member function and launches a kernel in another.

(We've discussed this in the past; sorry if I just failed to find an existing formal issue for it.)

---

## #6733: Annotated subroutines don't show up in OTF2 traces when executed by IO_pool_executor

**Labels:** category: APEX

Description of issue:
Using APEX (develop branch) with HPX (version 1.10.0, build_type=RelWithDebInfo), generated OTF2 trace does not capture subroutine/function executed by "io_pool_executor".

Relevant software used to build HPX:
1. GCC, ver. 13.3.0
2. hwloc, ver. 2.10.0
3. OpenMPI, ver. 5.0.5
4. Boost, ver. 1.86.0
5. jemalloc, ver. 5.3.0
6. OTF2, ver. 3.1
7. PAPI, ver. 7.1.0

HPX configuration options:
CMAKE_BUILD_TYPE=RelWithDebInfo
CMAKE_POLICY_VERSION_MINIMUM=3.5
CMAKE_CXX_COMPILER=g++
HPX_WITH_PAPI=TRUE
HPX_WITH_FETCH_APEX=TRUE
HPX_WITH_APEX=TRUE
HPX_WITH_APEX_TAG=develop
HPX_WITH_PARCELPORT_ACTION_COUNTERS=TRUE
HPX_WITH_THREAD_IDLE_RATES=TRUE
HPX_WITH_MALLOC=jemalloc
HPX_WITH_HWLOC=TRUE
HPX_WITH_NETWORKING=TRUE
HPX_WITH_PARCELPORT_TCP=FALSE
HPX_WITH_PARCELPORT_MPI=TRUE
HPX_WITH_TESTS=FALSE
HPX_WITH_EXAMPLES=TRUE
HPX_WITH_MAX_CPU_COUNT=256
HPX_WITH_FETCH_ASIO=TRUE
HPX_WITH_CUDA=TRUE
APEX_WITH_CUDA=TRUE
APEX_WITH_OTF2=TRUE
OTF2_ROOT=...

Compilation & execution of example program:
1. mkdir build && cd build && cmake ..
2. cmake --build .
3. export  APEX_OTF2=1
4. execution can be done on any number of locality and expected os_threads.

Comments:
The relevant line in the source code is line 38 and 39. Provided source code is missing "internal_print" annotation. Commenting line 39 and uncommenting line 38 should provide a trace with "internal_print" shown.

Source code:
[IO_MWE.tar.gz](https://github.com/user-attachments/files/21034729/IO_MWE.tar.gz)

Vampir results:
1. Not using IO_pool_executor
![Image](https://github.com/user-attachments/assets/c0735402-9f79-416d-a2c9-8a51201b6ed2)

2. with IO_pool_executor
![Image](https://github.com/user-attachments/assets/5f17a358-70a4-48e2-a177-6cccb74fe4e7)

---

## #6718: Bad user experience with algorithms interface

**Labels:** type: defect, category: algorithms

Passing an incorrect argument to a parallel algorithm results in a wall of template spew that's worse than your typical C++ template output. The use of `tag_invoke` in the algorithm's interface erases all the actual type and concept information of the viable calls. For example, making a mistake when calling `for_each` results in a huge wall of tag-invoke related information, including the `for_each` tag, but the `for_each.hpp` file in which the implementation and relevant information is doesn't even appear in the trace.

Making `tag_invoke` an implementation detail rather than the interface would have the additional benefit that each algorithm requirements are based on the algorithm itself, and not on any particular customization. This was a crucial design choice in `std::ranges`, where concept and constraints are still checked even when calling a customized implementation.

---

## #6717: Extensible execution policy design

**Labels:** type: feature request, category: executors

The execution policy design does not allow for easily defining new policies. In particular, the rebinding mechanism is too rigid. Additionally, numerous traits need to be specialized for new policies to interact correctly with the runtime.

Integration with other frameworks often requires the introduction of new execution policies which fulfill the requirements of both HPX and the other framework in question. This is the case for hpxMp, HPX/Kokkos, HPX/CCCL integration, and possibly others.

The rebinding mechanism is rigid as it requires a specific template template parameter as the most derived class, forcing the user facing type interface. If the executor and executor parameters can be handled orthogonally, this would allow for a simpler design, where the policy itself doesn't need to be aware of it. Additionally, it could be beneficial to disable inheritance altogether and instead allow for customization of a special member or base in case a particular policy has to keep additional state and/or provide additional interfaces.

It may be possible to reduce the number of required `is_*_policy` trait specializations by making the default implementation inspect some state or struct associated with the policy tag.

---

## #6715: Compiler / linker warnings when building HPX 1.11.0-rc1

**Labels:** type: compatibility issue

I am testing the build of the Conda packages of the upcoming version of HPX. All packages build fine, which is great. I collected the compiler and linker warnings which you may want to check. Most of them are easy to fix it seems.

---

## #6706: Fixing CI issues

**Labels:** type: defect, category: tests

Failing tests:
- [x] [tests.examples.modules.collectives.channel_pingpong](https://cdash.rostam.cct.lsu.edu/test/18189652)
- [ ] [tests.unit.modules.algorithms.algorithms.move](https://cdash.rostam.cct.lsu.edu/test/18188913)
- [ ] [tests.unit.modules.compute_local.numa_allocator](https://cdash.rostam.cct.lsu.edu/test/18184657)
- [ ] [tests.unit.modules.algorithms.algorithms.sort](https://cdash.rostam.cct.lsu.edu/test/18201561)

Other issues
- [x] Fix 50+ emitted build warnings
- [ ] Investigate CTest/CDash integration with [address sanitizer](https://cmake.org/cmake/help/latest/command/ctest_memcheck.html) and [code coverage](https://cmake.org/cmake/help/latest/command/ctest_coverage.html).

---

## #6647: Incorrect reduce implementation

**Labels:** type: defect, category: algorithms, project: GSoC

https://github.com/STEllAR-GROUP/hpx/blob/0005b929c69fd199c11dfd691f4d1b62d90735af/libs/core/algorithms/include/hpx/parallel/algorithms/reduce.hpp#L421

This line in `reduce` implementation attempts to convert `*first`  to `T`, but there is no requirement for that operation. See https://eel.is/c++draft/reduce#5

As a somewhat artificial example, it's possible to implement `minmax` on top of `reduce`:

```
struct minmax
{
    std::pair<int, int> operator()(
        std::pair<int, int> lhs, std::pair<int, int> rhs) const
    {
        return {
            lhs.first < rhs.first ? lhs.first : rhs.first,
            lhs.second < rhs.second ? rhs.second : lhs.second,
        };
    }
    std::pair<int, int> operator()(std::pair<int, int> lhs, int rhs) const
    {
        return (*this)(lhs, std::pair<int, int>{rhs, rhs});
    }
    std::pair<int, int> operator()(int lhs, std::pair<int, int> rhs) const
    {
        return (*this)(std::pair<int, int>{lhs, lhs}, rhs);
    }
    std::pair<int, int> operator()(int lhs, int rhs) const
    {
        return (*this)(std::pair<int, int>{lhs, lhs}, std::pair<int, int>{rhs, rhs});
    }
};

auto [min, max] = hpx::reduce(hpx::execution::par,
    c.begin(), c.end(), std::pair<int, int>{INT_MAX, INT_MIN}, minmax{});
```

---

## #6624: Remove type alias sender completions

**Labels:** type: enhancement, type: compatibility issue, category: senders/receivers

In Hagenberg, as part of voting P3164, WG21 voted to eliminate the option of a nested type alias for `completion_sigantures`, in favor of keeping only the member function `get_completion_signatures`.

---

## #6618: Enable intel compiler cause hpx program return some errors.

**Labels:** type: defect, category: CI

Before i call $ source /opt/intel/oneapi/setvars.sh, every hpx program works fine, but when i use intel compiler for other works and run again the hpx program with a little modification for example change a variable value, it return some errors. Maybe there is something wrong when i build hpx from source ?

```
-- Configuring done (0.6s)
-- Generating done (0.0s)
-- Build files have been written to: /home/asus/cppproject/hpx_example/build
[1/2] : && /opt/rh/gcc-toolset-14/root/usr/bin/c++  -pthread -Wl,-z,defs -fvisibility=hidden -Wl,--dependency-file,CMakeFiles/hpx_example.dir/link.d CMakeFiles/hpx_example.dir/main.cc.o -o hpx_example  -Wl,-rpath,/home/asus/hpx_install/lib64  /home/asus/hpx_install/lib64/libhpx_iostreams.so.1.10.0  /home/asus/hpx_install/lib64/libhpx_wrap.a  -Wl,-wrap=main  /home/asus/hpx_install/lib64/libhpx_init.a  /home/asus/hpx_install/lib64/libhpx.so.1.10.0  /home/asus/hpx_install/lib64/libhpx_core.so  /usr/lib64/libtcmalloc_minimal.so  /usr/lib64/libhwloc.so  -ldl  -lrt && :
FAILED: hpx_example 
: && /opt/rh/gcc-toolset-14/root/usr/bin/c++  -pthread -Wl,-z,defs -fvisibility=hidden -Wl,--dependency-file,CMakeFiles/hpx_example.dir/link.d CMakeFiles/hpx_example.dir/main.cc.o -o hpx_example  -Wl,-rpath,/home/asus/hpx_install/lib64  /home/asus/hpx_install/lib64/libhpx_iostreams.so.1.10.0  /home/asus/hpx_install/lib64/libhpx_wrap.a  -Wl,-wrap=main  /home/asus/hpx_install/lib64/libhpx_init.a  /home/asus/hpx_install/lib64/libhpx.so.1.10.0  /home/asus/hpx_install/lib64/libhpx_core.so  /usr/lib64/libtcmalloc_minimal.so  /usr/lib64/libhwloc.so  -ldl  -lrt && :
/opt/rh/gcc-toolset-14/root/usr/libexec/gcc/x86_64-redhat-linux/14/ld: CMakeFiles/hpx_example.dir/main.cc.o: in function `tbb::detail::d1::execution_slot(tbb::detail::d1::execution_data const&)':
main.cc:(.text._ZN3tbb6detail2d114execution_slotERKNS1_14execution_dataE[_ZN3tbb6detail2d114execution_slotERKNS1_14execution_dataE]+0x14): undefined reference to `tbb::detail::r1::execution_slot(tbb::detail::d1::execution_data const*)'
/opt/rh/gcc-toolset-14/root/usr/libexec/gcc/x86_64-redhat-linux/14/ld: CMakeFiles/hpx_example.dir/main.cc.o: in function `tbb::detail::d1::current_thread_index()':
main.cc:(.text._ZN3tbb6detail2d120current_thread_indexEv[_ZN3tbb6detail2d120current_thread_indexEv]+0xe): undefined reference to `tbb::detail::r1::execution_slot(tbb::detail::d1::execution_data const*)'
collect2: error: ld returned 1 exit status
ninja: build stopped: subcommand failed.
[asus@localhost hpx_example]$ 

```

---

## #6602: Align our parallel range implementation with P3179

**Labels:** type: enhancement, type: compatibility issue, category: algorithms, project: GSoC

For details, see: wg21.link/p3179

---

## #6601: Implement P2079 for HPX (System execution context)

**Labels:** type: compatibility issue, project: GSoC, category: senders/receivers

See: wg21.link/p2079

---

## #6574: Using the parcelport TCP causes the memory usage to continuously increase, and I'm not sure if it is a memory leak

**Labels:** type: defect, category: parcel transport

Recently, I’ve been validating the feasibility of using HPX as the foundational framework for our team's signal processing algorithm development. However, during testing, I noticed what seems to be a memory leak issue with HPX.

So, I wrote a separate test program using the TCP parcelport to test data interaction across multiple nodes and discovered what looked like a memory leak. But I’m not entirely sure, so I’m seeking your help here.

I used two nodes, running on two different hosts (Ubuntu 22.04 LTS), and the test code is as follows:
```C++
static vector<std::byte> getData(const size_t sz) 
{
    vector<std::byte> data(sz, (std::byte)(0xFF));
    
    return data;
}

HPX_PLAIN_ACTION(getData, GetDataAction);

int hpx_main(int argc, char* argv[])
{
    hpx::error_code ec = hpx::make_success_code();
    std::vector<hpx::id_type> localities = hpx::find_all_localities(ec);
    if (hpx::error::success != ec.value()) 
    {
        printf("find_all_localities executed failed, %s\n", ec.get_message().c_str());
        return -1;
    }

    if (localities.size() < 2) 
    {
        printf("this program requires at least 2 localities\n");
        return -2;
    }

    printf("num of localities: %ld\n", localities.size());
    for (const auto& loc : localities) 
    {
        hpx::naming::gid_type gid = loc.get_gid();
        std::string address = hpx::get_locality_name(loc).get();
        std::uint32_t localityId = hpx::naming::get_locality_id_from_gid(gid);

        printf("locality id: %d\n", localityId);
        printf("locality name: %s, id: %08X\n", address.c_str(), localityId);
    }

    size_t dataSize = 960256;
    while (true) 
    {
        hpx::this_thread::sleep_for(1400us);

        auto dataNode0 = hpx::sync<GetDataAction>(localities[0], dataSize);
        auto dataNode1 = hpx::sync<GetDataAction>(localities[1], dataSize);

        printf("node0, data size: %ld, node1, data size: %ld\n", dataNode0.size(), dataNode1.size());
    }
    
    return hpx::finalize();
}
```

Node 0 is the root node. I observed the memory usage on both Node 0 and Node 1. Both hosts have 8GB of physical memory.

When the test program started, the memory usage on both nodes was about 0.4%. But after 1 hour, the memory usage on Node 0 increased to 0.7%, while the memory usage on Node 1 remained at 0.4%. 

After about 24 hours, the memory usage on Node 0 reached 1.9%, while the memory usage on Node 1 remained at 0.4%. This looks like a memory leak.

Later, I modified the test code to run a single process on one host, and there was no increase in memory usage.

However, my test code is extremely simple, so it’s unlikely that the issue is due to my code. Could you help analyze this problem?

---

## #6540: Race conditions related to thread_local variables

**Labels:** type: race condition, type: defect, category: general

In various places within HPX, `thread_local` variables are accessed without locking or synchronization, using a pattern such as:

```C++
T& get_var(){
  thread_local T important_var{};
  return important_var;
}
```

```C++
// Multiple threads may concurrently run this code:
void run()
{
  {
    auto& var = get_var();
    do_A(var);
  }

  // Do things, yield, suspend, wait for future, calculate 42, etc...

  {
    auto& var2 = get_var();
    do_B(var2);
  }
}
```

This can be thread-safe, as long as we don't context switch (ie `suspend` the current hpx-thread) while holding a reference to the `thread_local` variable, because each instance of the `thread_local` variable will be accessed by only one thread at a time (the currently executing thread).

_(suspending the hpx-thread will send it back to the thread-queue, where it may be picked up by a different OS-worker-thread, so holding a pointer or reference to the thread_local variable can cause trouble, as it will still refer to the previous thread)_

However, a malfunctioning example led us to the realization that compiler optimizations transformed the previous code to something equivalent to:

```C++
void run()
{
  auto& var_ref = get_var() // Cache address of thread_local

  {
    do_A(var_ref);
  }

  // Do things, yield, suspend, wait for hpx::future, calculate 42, etc...

  {
   do_B(var_ref);
  }
}
```

This transformation, in combination with the hpx-thread migrating to different worker-threads, led to unexpected race conditions on the thread_local variable. 

While this was spotted in `thread_local_caching_allocator`, we still seek a general solution to address this usage pattern. As also mentioned in [this related stack-overflow question](https://stackoverflow.com/questions/25673787/making-thread-local-variables-fully-volatile), taking a volatile ptr to the `thread_local` does not help.

I will update this issue as more is done to address it.

---

## #6538: Running Hpx Program Using srun/mpiexec Error

Earlier, I discussed with @JiakunYan about the issue of an HPX-based application crashing when using parcelport LCI, and we debugged it. Currently, the crash issue has been resolved.
Please refer to this link:
https://github.com/STEllAR-GROUP/hpx/discussions/6526

Available PMI with Slurm:
```Bash
srun --mpi=list
MPI plugin types are...
        none
        cray_shasta
        pmi2
        pmix
specific pmix plugin versions available: pmix_v3
```

Here is my test code:
```C++
#include <iostream>
#include "Xlog.h"
#include "Iface.h"
// #include "hpx.hpp"
#include "hpx/hpx_start.hpp"
#include "hpx/version.hpp"
#include "hpx/init.hpp"
#include "hpx/runtime.hpp"
#include "hpx/include/actions.hpp"
#include "hpx/include/lcos.hpp"
#include "hpx/include/async.hpp"
#include "TestHpx.h"

using namespace std;

int hpx_main(int argc, char* argv[])
{
    TRACE("hpx_main function");

    hpx::error_code ec = hpx::make_success_code();
    std::vector<hpx::id_type> localities = hpx::find_all_localities(ec);
    if (hpx::error::success != ec.value()) 
    {
        ERROR("find_all_localities executed failed, %s", ec.get_message().c_str());
        return -1;
    }
    
    if (localities.size() < 2) 
    {
        ERROR("this program requires at least two localities");
        return -2;
    }

    INFO("num of localities: %ld", localities.size());

    for (const auto& loc : localities) 
    {
        hpx::naming::gid_type gid = loc.get_gid();
        std::string address = hpx::get_locality_name(loc).get();
        std::uint32_t localityId = hpx::naming::get_locality_id_from_gid(gid);

        DEBUG("locality id: %d", localityId);
        DEBUG("locality name: %s, id: %08X", address.c_str(), localityId);
    }

    getchar();
    
    return hpx::finalize();
}

int main(int argc, char **argv) 
{
    auto ret = xlogInitFile("conf/LogConf.yaml");
    if (false == ret) 
    {
        cerr << "logger init failed." << endl;
        return -1;
    }

    INFO("hpx demostration running...");

    auto hpxMajor = hpx::major_version();
    auto hpxMinor = hpx::minor_version();
    auto hpxPatch = hpx::subminor_version();
    INFO("hpx version: %d-%d-%d", hpxMajor, hpxMinor, hpxPatch);

    auto hpxCfg = vector<string>();
    hpxCfg.push_back("hpx.handle_signals=0");
    hpxCfg.push_back("hpx.max_idle_loop_count=1000");
    hpxCfg.push_back("hpx.max_idle_backoff_time=1000");
    
    hpx::init_params initArgs;
    initArgs.cfg = std::move(hpxCfg);    

    ret = hpx::start(argc, argv, initArgs);
    if (false == ret) 
    {
        ERROR("hpx runtime init failed");
        return -3;
    }

    getchar();

    WARN("hpx demostration exiting...");

    return hpx::stop();
}
```

When I start my HPX program with different command parameters, I encounter various issues such as errors, crashes, and the program not entering the hpx_main function, depending on the command u

*[truncated]*

---

## #6535: Fix S/R versions of the parallel algorithms

PR #6494 adds unit test cases and fixes for the S/R versions of a subset of HPX's parallel algorithms. This issue serves to track the remaining algorithms that have not yet been adapted to work with S/R and/or do not yet have unit test cases for their S/R versions:

- [ ] `copy_if`
- [ ] `exclusive_scan`
- [ ] `for_loop` (see PR #6529)
- [ ] `for_loop_n` (see PR #6529)
- [ ] `for_loop_strided` (see PR #6529)
- [ ] `for_loop_n_strided` (see PR #6529)
- [ ] `inclusive_scan`
- [ ] `make_heap`
- [ ] `merge`
- [ ] `inplace_merge`
- [ ] `nth_element`
- [ ] `partial_sort`
- [ ] `partial_sort_copy`
- [ ] `stable_partition`
- [ ] `partition`
- [ ] `partition_copy`
- [ ] `reduce_by_key`
- [ ] `remove_copy`
- [ ] `remove_copy_if`
- [ ] `search_n`
- [ ] `set_difference`
- [ ] `set_intersection`
- [ ] `set_symmetric_difference`
- [ ] `set_union`
- [ ] `shift_left`
- [ ] `shift_right`
- [ ] `sort`
- [ ] `sort_by_key`
- [ ] `stable_sort`
- [ ] `transform_exclusive_scan`
- [ ] `transform_inclusive_scan`
- [ ] `uninitialized_copy`
- [ ] `uninitialized_copy_n`
- [ ] `uninitialized_default_construct`
- [ ] `uninitialized_default_construct_n`
- [ ] `uninitialized_fill`
- [ ] `unititialized_fill_n`
- [ ] `uninitialized_move`
- [ ] `uninitialized_move_n`
- [ ] `uninitialized_relocate`
- [ ] `uninitialized_relocate_backward`
- [ ] `uninitialized_relocate_n`
- [ ] `uninitialized_value_construct`
- [ ] `uninitialized_value_construct_n`
- [ ] `unique_copy`

Note: During the work on PR #6494, S/R unit tests were added for some algorithms without also fixing their S/R versions. To avoid cluttering the tests, these temporarily non-functional unit test cases were removed. However, if they are needed for future work, you they can be restored by reverting commit [a20f1b4](https://github.com/STEllAR-GROUP/hpx/pull/6494/commits/a20f1b4da8e49de5d4380dd23a5c928525106768).  See [this spreadsheet](https://docs.google.com/spreadsheets/d/1zbz88UZn912nLiBMbRaMTQTU2lT0vZRigui4jrcbIRA/edit?usp=sharing) from the PR for a list of algorithms for which unit test cases were originally added.

---

## #6534: Addressing remaining Stdexec issues

Remaining issues

1. HPX senders should replace tag-invocable tags with member functions, following the changes introduced in P2300R8.
2. Some Stdexec algorithms use `std` synchronization primitives, which clash with HPX's (e.g. `stdexec::run_loop`, `this_thread::sync_wait` use `std::mutex` and `std::condition_variable`. This causes some tests to deadlock. Thanks to @zhekemist for identifying this! The following commit fixed a bug caused by this interaction: https://github.com/STEllAR-GROUP/hpx/pull/6431/commits/d06c9ad13aca0ed38e77e08fa2664290389fbc4e.
3. The tests `algorithm_transform_mpi` and `mpi_ring_async_executor` have been disabled due to issue # 2 highlighted above. Other tests may be failing too, but it was noticed that there are MPI tests that fail but do `return 0` so they are not marked as failing. This should be corrected too.
4. Code and build system need testing on Windows and macOS beyond CI.

Due to these issues, Stdexec won't be enabled by default. To activate there needs to be an explicit definition: `HPX_WITH_STDEXEC=ON`

---

## #6528: Wrong version recommendation of shpinx when building documentation

**Labels:** category: documentation, type: enhancement, type: compatibility issue

The page suggests to use:
pip install --user "sphinx<5" sphinx-book-theme breathe sphinxcontrib-bibtex sphinx-copybutton

## Actual Behavior
There are version conflicts with sphinx<5 (4.5.0, recommended on the page).
## Solution
I succeded in building HPX with these steps:
Install docutils<0.18
and pip install --user "sphinx<6" sphinx-book-theme breathe sphinxcontrib-bibtex sphinx-copybutton

... Please describe your environment

  - HPX Version: HPX v1.10.0
  - Python version:  Python 3.10.12
  - Platform (compiler, OS): WSL (Ubuntu)

---

## #6504: `FindTBB.cmake` cannot find correct TBB library.

**Labels:** category: CMake, type: defect

## Expected Behavior

After enabling `HPX_WITH_EXAMPLES_TBB` option at configuration time, the test `tbb_homogeneous_timed_task_spawn` specified in `tests/performance/local/CMakeLists.txt` should be built and be tested when invoking `CTest`.

## Actual Behavior

The test `tbb_homogeneous_timed_task_spawn` is not invoked during `CTest`

## Steps to Reproduce the Problem

1. `mkdir -p <hpx_source_dir>/build && cd <hpx_source_dir>/build`
2. `cmake -DHPX_WITH_EXAMPLES_TBB=ON ..`
    In this step the following warning message appears:
    ```
    -- Nice threadlevel is disabled.
    -- Stack traces are enabled.
    CMake Warning (dev) at /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:438 (message):
      The package name passed to `find_package_handle_standard_args` (TBBmalloc)
      does not match the name of the calling package (TBB).  This can lead to
      problems in calling code that expects `find_package` result variables
      (e.g., `_FOUND`) to follow a certain pattern.
    Call Stack (most recent call first):
      cmake/FindTBB.cmake:44 (find_package_handle_standard_args)
      CMakeLists.txt:1365 (find_package)
    This warning is for project developers.  Use -Wno-dev to suppress it.
    
    -- Could NOT find TBBmalloc (missing: Tbb_LIBRARY) 
    -- Compiling with the native toolset
    -- Performing Test HPX_WITH_CXX11_ATOMIC - Success
    ```
3. `cmake --build .`
4. `ctest | grep tbb_homogeneous_timed_task_spawn`
    Nothing to output from stdout.

## Specifications

  - HPX Version: current master (5898e7ea)
  - Platform (compiler, OS): Archlinux, with the following packages installed from Arch offical repo:
    ```
    pacman -Qs | grep -E '(/gcc )|(/onetbb )|(/cmake )' 
    local/cmake 3.29.5-2
    local/gcc 14.1.1+r58+gfc9fb69ad62-1
    local/onetbb 2021.12.0-2
    ```
  - The contents of file `/usr/lib/pkgconfig/tbb.pc` from package `onetbb` is:
    ```
    # Copyright (c) 2021-2023 Intel Corporation
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    prefix=/usr
    libdir=${prefix}/lib
    includedir=${prefix}/include
    
    Name: oneAPI Threading Building Blocks (oneTBB)
    Description: C++ library for parallel programming on multi-core processors.
    URL: https://github.com/oneapi-src/oneTBB
    Version: 2021.12.0
    Libs: -L${libdir}  -ltbb
    Cflags: -I${includedir}
    ```

---

## #6502: The test executable numa_allocator_test fails with an assertion

## Steps to Reproduce the Problem

```
$ /usr/ports/devel/hpx/work/.build/bin/numa_allocator_test
<DEB> 0000000000 -------------- 0x0x2ff06015f00 cpu ---               SPQUEUE start_thread         local_thread 0 
<DEB> 0000000023 -------------- 0x0x2ff06016d00 cpu ---               SPQUEUE start_thread         local_thread 2 
<DEB> 0000000037 -------------- 0x0x2ff06016600 cpu ---               SPQUEUE start_thread         local_thread 1 
<DEB> 0000000120 -------------- 0x0x2ff06017400 cpu ---               SPQUEUE start_thread         local_thread 3 
<DEB> 0000000521 -------------- 0x0x2ff06015f00 cpu ---               SPQUEUE thread holder        local_thread 0 domain 0 index 0 local_id 0 owner_mask f 
<DEB> 0000000782 -------------- 0x0x2ff06015f00 cpu ---               QH_THRD construct            D 00 Q 000 Rollover counter 00 01 
<DEB> 0000000810 -------------- 0x0x2ff06015f00 cpu ---               _TQ_MC_ set_holder           D 00 Q 000 
<DEB> 0000000839 -------------- 0x0x2ff06015f00 cpu ---               _TQ_MC_ set_holder           D 00 Q 000 
<DEB> 0000000853 -------------- 0x0x2ff06015f00 cpu ---               _TQ_MC_ set_holder           D 00 Q 000 
<DEB> 0000000865 -------------- 0x0x2ff06015f00 cpu ---               _TQ_MC_ set_holder           D 00 Q 000 
<DEB> 0000001100 -------------- 0x0x2ff06016600 cpu ---               SPQUEUE thread holder        local_thread 1 domain 0 index 1 local_id 1 owner_mask 7 
<DEB> 0000001405 -------------- 0x0x2ff06016600 cpu ---               QH_THRD construct            D 00 Q 001 Rollover counter 01 01 
<DEB> 0000001427 -------------- 0x0x2ff06016600 cpu ---               _TQ_MC_ set_holder           D 00 Q 001 
<DEB> 0000001452 -------------- 0x0x2ff06016600 cpu ---               _TQ_MC_ set_holder           D 00 Q 001 
<DEB> 0000001474 -------------- 0x0x2ff06016600 cpu ---               _TQ_MC_ set_holder           D 00 Q 001 
<DEB> 0000001487 -------------- 0x0x2ff06016600 cpu ---               _TQ_MC_ set_holder           D 00 Q 000 
<DEB> 0000001721 -------------- 0x0x2ff06016d00 cpu ---               SPQUEUE thread holder        local_thread 2 domain 0 index 2 local_id 2 owner_mask 7 
<DEB> 0000002003 -------------- 0x0x2ff06016d00 cpu ---               QH_THRD construct            D 00 Q 002 Rollover counter 02 01 
<DEB> 0000002028 -------------- 0x0x2ff06016d00 cpu ---               _TQ_MC_ set_holder           D 00 Q 002 
<DEB> 0000002061 -------------- 0x0x2ff06016d00 cpu ---               _TQ_MC_ set_holder           D 00 Q 002 
<DEB> 0000002085 -------------- 0x0x2ff06016d00 cpu ---               _TQ_MC_ set_holder           D 00 Q 002 
<DEB> 0000002107 -------------- 0x0x2ff06016d00 cpu ---               _TQ_MC_ set_holder           D 00 Q 000 
<DEB> 0000002378 -------------- 0x0x2ff06017400 cpu ---               SPQUEUE thread holder        local_thread 3 domain 0 index 3 local_id 3 owner_mask 7 
<DEB> 0000002753 -------------- 0x0x2ff06017400 cpu ---  

*[truncated]*

---

## #6430: HPX distributed barrier runs into assertion error

**Labels:** type: defect, category: actions, category: init

## Expected Behavior

The `hpx::distributed::barrier::synchronize()` runs successfully.

## Actual Behavior

It gets into an assertion error
```
{file}: /home/jiakuny/workspace/hpx-master/libs/full/collectives/src/barrier.cpp
{line}: 210
{function}: static void hpx::distributed::barrier::synchronize()
{what}: Assertion 'b[0].node_ && b[1].node_' failed: HPX(assertion_failure)
```


## Steps to Reproduce the Problem

A simple example code to reproduce this error. (Ran it with 2 localities)
```
void run_test();
HPX_PLAIN_ACTION(run_test, run_test_action)

void run_test() {
    fprintf(stderr, "%d: run_test\n", hpx::get_locality_id());
    hpx::distributed::barrier::synchronize();
}

///////////////////////////////////////////////////////////////////////////////
int hpx_main(hpx::program_options::variables_map& b_arg)
{
    std::vector<hpx::future<void>> futs;
    for (auto l : hpx::find_all_localities()) {
        futs.emplace_back(hpx::async<run_test_action>(l));
    }
    hpx::wait_all(futs);

    hpx::finalize();
    return 0;
}

int main(int argc, char* argv[])
{
    namespace po = hpx::program_options;
    po::options_description description("HPX test barrier");

    hpx::init_params init_args;
    init_args.desc_cmdline = description;

    return hpx::init(argc, argv, init_args);
}
```

## Specifications

  - HPX Version: The current master branch
  - Platform (compiler, OS): ubuntu 20.04, GCC 9.4

---

## #6399: Warning: type attributes ignored after type is already defined

**Labels:** type: defect, compiler: gcc

## Expected Behavior

No warning should appear. 

## Actual Behavior

```
In file included from /usr/local/hpx-corot/include/hpx/parcelset_base/policies/message_handler.hpp:14,
                 from /usr/local/hpx-corot/include/hpx/parcelset_base/parcel_interface.hpp:24,
                 from /usr/local/hpx-corot/include/hpx/agas_base/primary_namespace.hpp:17,
                 from /usr/local/hpx-corot/include/hpx/async_colocated/async_colocated.hpp:13,
                 from /usr/local/hpx-corot/include/hpx/distribution_policies/colocating_distribution_policy.hpp:17,
                 from /usr/local/hpx-corot/include/hpx/parallel/segmented_algorithms/detail/dispatch.hpp:16,
                 from /usr/local/hpx-corot/include/hpx/parallel/segmented_algorithms/adjacent_difference.hpp:17,
                 from /usr/local/hpx-corot/include/hpx/parallel/segmented_algorithm.hpp:12,
                 from /usr/local/hpx-corot/include/hpx/algorithm.hpp:10,
                 from /usr/local/hpx-corot/include/hpx/hpx.hpp:10,
                 from __code__.cpp:2:
/usr/local/hpx-corot/include/hpx/parcelset_base/parcelset_base_fwd.hpp:17:22: warning: type attributes ignored after type is already defined [-Wattributes]
   17 |     class HPX_EXPORT locality;
      | 

```

## Specifications

... Please describe your environment

  - HPX Version:  HPX 1.8.1
  - Platform (compiler, OS): gcc

---

## #6385: gasnet parcelport and parcelport test failures

## Expected Behavior

gasnet builds and all parcelport tests should work

## Actual Behavior

all parcelports tests fail

## Steps to Reproduce the Problem

  1. parcelports fail in the CI system when gasnet is tested

## Specifications

  - HPX Version: the development branch
  - Platform (compiler, OS): gcc and clang from CI testing

---

## #6333: Current thread_id changing after suspending in direct execution

**Labels:** type: defect

## Background

@hkaiser I came across this issue while investigating the current hangs in `cancelable_action` test.

In that test, the current thread_id is firstly obtained using `hpx::this_thread::get_id()` (through a `reset_id` helper object).
Then, we have a workloop that occasionally suspends, waiting to be interrupted (`hpx::thread::interrupt(id_)`).

https://github.com/STEllAR-GROUP/hpx/blob/bc993dd15b9252908e0b30b9ed5efd830cf99909/examples/cancelable_action/cancelable_action/server/cancelable_action.hpp#L81-L94

## Issue

I found that calling `hpx::this_thread::get_id()` before and after `hpx::this_thread::suspend()` would often return a different id.
I believe this is due to the way yielding is handled when utilizing direct execution:

https://github.com/STEllAR-GROUP/hpx/blob/bc993dd15b9252908e0b30b9ed5efd830cf99909/libs/core/coroutines/include/hpx/coroutines/detail/coroutine_stackful_self_direct.hpp#L34-L39

`coroutine_stackful_self_direct` falls back to `next_self_` (its calling context) for yielding, which will fail to correctly restore the state after yielding:

https://github.com/STEllAR-GROUP/hpx/blob/bc993dd15b9252908e0b30b9ed5efd830cf99909/libs/core/coroutines/include/hpx/coroutines/detail/coroutine_stackful_self.hpp#L32-L42

If I understand correctly, `reset_self_on_exit` will cause the [static variable `local_self_`](https://github.com/STEllAR-GROUP/hpx/blob/bc993dd15b9252908e0b30b9ed5efd830cf99909/libs/core/coroutines/src/detail/coroutine_self.cpp#L14) to refer to the "simple" (`coroutine_stackful_self`) coroutine after yielding (and not to the direct coroutine where it used to before the yield, see the use of `reset_self_on_exit` on [`coroutine_impl::invoke_directly()`](https://github.com/STEllAR-GROUP/hpx/blob/bc993dd15b9252908e0b30b9ed5efd830cf99909/libs/core/coroutines/src/detail/coroutine_impl.cpp#L119-L129)).

The solution is probably simple, but I just barely got to understanding how these coroutines work, so I just hope I got things right fttb.

---

## #6331: 6 tests fail, 4 tests time out

**Labels:** type: defect, platform: FreeBSD

## Actual Behavior

See the log [here](https://people.freebsd.org/~yuri/hpx-1.9.1-test.log).

## Specifications

  - HPX Version: 1.9.1
  - Platform (compiler, OS): clang-16, FreeBSD 13.2

---

## #6323: Fix 32bit Windows build

**Labels:** type: defect, platform: Windows, compiler: msvc

See https://github.com/microsoft/vcpkg/pull/33106#issuecomment-1677125807 for details

---

## #6240: HPX does not compile with G++ version prior to 9.3.

**Labels:** type: compatibility issue, compiler: gcc

## Expected Behavior

Compile successfully for any compilers supporting c++17.

## Actual Behavior

G++ 8.5 gave me an error `error: expected unqualified-id before '[' token`


## Steps to Reproduce the Problem

Just compile it with G++ 8.5.

## Specifications

  - HPX Version: the master branch `ad3ac76e159692355d4715f8b275c0a062b859af`
  - Platform (compiler, OS): G++ 8.5. This should apply to any version prior to g++9.3.

## Comment

This is not a fault of HPX, but G++, but this ticket can at least serve as an explanation for future users encountering this error. This is caused by a bug in G++ prior to 9.3. G++ doesn't parse correctly the `[[maybe_unused]]` attribute for the constructor's first argument. However, HPX uses it in `libs/core/executors/include/hpx/executors/service_executors.hpp` line 49.

```
explicit service_executor([[maybe_unused]] hpx::util::io_service_pool* pool) noexcept
```

Reference: https://gcc.gnu.org/bugzilla/show_bug.cgi?id=81429.

---

## #6232: Par performance of hpx::reverse

**Labels:** type: defect, category: algorithms

## Expected Behavior

hpx::reverse() performs worse with par execution policy compared to seq execution policy.
Mentioned in : https://devblogs.microsoft.com/cppblog/using-c17-parallel-algorithms-for-better-performance/

![ReverseAlgorithm](https://user-images.githubusercontent.com/69986621/236041182-da815e0d-c50f-4e94-8478-c307443cca8a.png)
![ReverseAlgorithm](https://user-images.githubusercontent.com/69986621/236041565-ff8e7c71-80da-4a6b-91b2-b6e16089b049.png)


Median execution time for 100'000'000 elements
Par : 9787040.0
Seq : 6424720.0

The performance difference is as mentioned in the microsoft blog

perf-stat output:

Par
 Performance counter stats for './par':

          6,856.13 msec task-clock                #    3.624 CPUs utilized          
             1,734      context-switches          #  252.912 /sec                   
                25      cpu-migrations            #    3.646 /sec                   
         1,051,732      page-faults               #  153.400 K/sec                  
    27,791,403,155      cycles                    #    4.054 GHz                      (83.55%)
        68,433,024      stalled-cycles-frontend   #    0.25% frontend cycles idle     (83.52%)
       524,413,414      stalled-cycles-backend    #    1.89% backend cycles idle      (83.16%)
    21,075,188,028      instructions              #    0.76  insn per cycle         
                                                  #    0.02  stalled cycles per insn  (83.47%)
     3,606,953,700      branches                  #  526.092 M/sec                    (83.21%)
         3,547,443      branch-misses             #    0.10% of all branches          (83.12%)

       1.891962963 seconds time elapsed

       5.695293000 seconds user
       1.143055000 seconds sys


 Performance counter stats for './par':

       426,032,401      cache-references                                            
        51,362,077      cache-misses              #   12.056 % of all cache refs    
    24,980,933,230      cycles                                                      
    18,996,816,372      instructions              #    0.76  insn per cycle         
     3,239,373,302      branches                                                    
         1,051,732      faults                                                      
                29      migrations                                                  

       1.605927855 seconds time elapsed

       5.177040000 seconds user
       0.884079000 seconds sys








Seq:
 Performance counter stats for './seq':

          2,531.75 msec task-clock                #    1.589 CPUs utilized          
               401      context-switches          #  158.388 /sec                   
                28      cpu-migrations            #   11.060 /sec                   
         1,051,725      page-faults               #  415.414 K/sec                  
     9,805,342,29

*[truncated]*

---

## #6190: --hpx:queuing=shared fails for distributed runs

**Labels:** type: defect, category: parcel transport, category: scheduler

From IRC:
```
[16:37]	beojan: I've noticed that if I use the `--hpx:queuing=shared` option to enable a shared queue across hardware threads, my program crashes when I run it through mpirun with -n >= 2.
[16:38]	beojan: I originally noticed this with my Gaudi port, but it also happens with my toy demo: https://github.com/beojan/HPXDemo
[16:39]	beojan: Here's the error:
[16:39]	beojan: {os-thread}: locality#1/worker-thread#1
[16:39]	beojan: {thread-description}: <unknown>
[16:39]	beojan: {state}: not running
[16:39]	beojan: {auxinfo}: 
[16:39]	beojan: {file}: /home/beojan/Development/src/hpx/src/hpx-1.8.1/libs/core/schedulers/include/hpx/schedulers/thread_queue_mc.hpp
[16:39]	beojan: {line}: 247
[16:39]	beojan: {function}: thread_queue_mc::create_thread
[16:39]	beojan: {what}: staged tasks must have 'pending' as their initial state: HPX(bad_parameter)
```

---

## #6177: Performance drop

**Labels:** type: defect

## Expected Behavior
No performance drop

## Actual Behavior
Performance drop of 25% with the changes of 
https://github.com/STEllAR-GROUP/hpx/commit/6f16e770c9f6ae809e9fbf15384ab11e40c390e6

## Steps to Reproduce the Problem
Use of `restricted_thread_pool_executor` and `executor_guided_chunk_size` as in my old examples in https://github.com/STEllAR-GROUP/hpx/pull/5117.

## Specifications
  - Ubuntu clang version 14.0.0-1ubuntu1

---

## #6128: CMake configures wrong for Clang

**Labels:** category: CMake, type: defect

## Expected Behavior

on docker image stevenrbrandt/clangmi

git clone https://github.com/STEllAR-GROUP/parallelnumericalintegration.git
mkdir parallelnumericalintegration/build
cd parallelnumericalintegration/build
cmake -DCMAKE_CXX_COMPILER=$(which clang++) ..

fails with

[ 10%] Building CXX object src/CMakeFiles/taylor_par_hpx.dir/taylor_par_hpx.cpp.o
[ 20%] Linking CXX executable taylor_par_hpx
/usr/bin/ld: /usr/local/lib64/libhpx_wrap.a(hpx_wrap.cpp.o): undefined reference to symbol '_ZNKSt3__114error_category10equivalentEiRKNS_15error_conditionE'
/usr/bin/ld: /usr/lib64/libc++.so.1: error adding symbols: DSO missing from command line
clang-14: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [src/CMakeFiles/taylor_par_hpx.dir/build.make:103: src/taylor_par_hpx] Error 1
make[1]: *** [CMakeFiles/Makefile2:862: src/CMakeFiles/taylor_par_hpx.dir/all] Error 2
make: *** [Makefile:146: all] Error 2

You can fix the problem by configuring as follows:

cmake -DCMAKE_CXX_COMPILER=$(which clang++) -DCMAKE_CXX_FLAGS=-stdlib=libc++ ..

## Specifications

... Please describe your environment
Docker image: stevenrbrandt/clangmi

  - HPX Version: 1.8.1
  - Platform (compiler, OS):
$ uname -a
Linux 49a6c2f51cac 5.10.102.1-microsoft-standard-WSL2 #1 SMP Wed Mar 2 00:30:59 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux

---

## #6097: Parcelport fails to initialize when multiple jobs run on the same cluster

**Labels:** type: defect, category: parcel transport

## Expected Behavior

Expected is that multiple independent jobs (e.g. SLURM job array) can run concurrently on the same cluster (on disjoint sets of nodes, not co-scheduled).

## Actual Behavior

Only one (or none) of the jobs is able to run while all others crash at initialization with the following errors:
```
the bootstrap parcelport (tcp) has failed to initialize on locality 0:
<unknown>: HPX(network_error),
bailing out
terminate called without an active exception
srun: error: queue1-dy-m5a2xlarge-1: task 0: Exited with exit code 255
the bootstrap parcelport (tcp) has failed to initialize on locality 4294967295:
<unknown>: HPX(network_error),
bailing out
terminate called without an active exception
the bootstrap parcelport (tcp) has failed to initialize on locality 4294967295:
<unknown>: HPX(network_error),
bailing out
```
## Steps to Reproduce the Problem

Schedule multiple jobs on a SLURM cluster without dependences and only using a subset of the nodes (so allowing the SLURM scheduler to start multiple instances on separate partitions).

Tried to use MPI parcelport and disable TCP to no avail (error changes, but still fails to initialize).

## Specifications

  - HPX Version: 1.7.1 and 1.8.1 tried
  - Platform (compiler, OS): Ubuntu / GCC

---

## #6028: `hpx` namespaces without corresponding `std`

**Labels:** category: documentation, type: feature request

The following list contains names that are currently in the `hpx` namespace, but are not present in the `std` namespace:

- [ ] `hpx::any_nonser`
- [ ] `hpx::unique_any_nonser`
- [ ] `hpx::make_any_nonser`
- [ ] `hpx::make_unique_any_nonser`
- [ ] `hpx::channel`
- [x] `hpx::function_ref` (see: http://wg21.link/p0792) DOCUMENTED
- [x] `hpx::scoped_annotation`
- [x] `hpx::annotated_function`
- [x] ~`hpx::apply`~ `hpx:post`
- [x] `hpx::sync`
- [x] `hpx::dataflow`
- [x] `hpx::make_future`
- [x] `hpx::make_shared_future`
- [x] `hpx::make_ready_future` (see: http://wg21.link/p0159) DOCUMENTED
- [x] `hpx::make_ready_future_alloc`
- [x] `hpx::make_ready_future_at`
- [x] `hpx::make_ready_future_after`
- [x] `hpx::make_exceptional_future` (see: http://wg21.link/p0159) DOCUMENTED
- [x] `hpx::when_all` (see: http://wg21.link/p0159) DOCUMENTED
- [x] `hpx::when_any` (see: http://wg21.link/p0159) DOCUMENTED
- [x] `hpx::when_some`
- [x] `hpx::when_each`
- [x] `hpx::wait_all`
- [x] `hpx::wait_any`
- [x] `hpx::wait_some`
- [x] `hpx::wait_each`
- [x] all names in the `init.hpp` header file
- [x] `hpx::no_mutex` DOCUMENTED
- [x] `hpx::spinlock` DOCUMENTED
- [x] `hpx::unlock_guard`
- [x] `hpx::unwrap`
- [x] `hpx::unwrap_n`
- [x] `hpx::unwrap_all`
- [x] `hpx::unwrapping`
- [x] `hpx::unwrapping_n`
- [x] `hpx::unwrapping_all`
- [ ] all names in the `version.hpp` header file

This is not an implication that all the above names should change namespace. The list's purpose is to make the differences between `hpx` and `std` known.

---

## #6014: Support C++20 modules

**Labels:** type: enhancement, type: compatibility issue, category: modules

Level 0:
- [ ] core/config_registry
- [ ] core/preprocessor

Level 1:
- [ ] core/config

Level 2:
- [ ] core/assertion
- [ ] core/cache
- [ ] core/concepts
- [ ] core/debugging
- [ ] core filesystem
- [ ] core/hardware
- [ ] core/itt_notify
- [ ] core/string_util

Level 3:
- [ ] core/allocator_support
- [ ] core/timing
- [ ] core/type_support

Level 4:
- [ ] core/format
- [ ] core/tag_invoke
- [ ] core/thread_support

Level 5:
- [ ] core/logging
- [ ] core/properties

Level 6:
- [ ] core/errors

Level 7:
- [ ] core/serialization

Level 8:
- [ ] core/datastructures
- [ ] core/hashing
- [ ] core/memory
- [ ] core/checkpoint_base

Level 9:
- [ ] core/functional
- [ ] core/iterator_support

Level 10:
- [ ] core/asio
- [ ] core/lock_registration
- [ ] core/plugin
- [ ] core/program_options
- [ ] core/util
- [ ] core/statistics

Level 11:
- [ ] core/batch_environments
- [ ] core/concurrency
- [ ] core/execution_base
- [ ] core/prefix
- [ ] core/testing

Level 12:
- [ ] core/ini
- [ ] core/static_reinit
- [ ] core/topology
- [ ] core/version

Level 13:
- [ ] core/affinity
- [ ] core/coroutines

Level 14:
- [ ] core/async_base
- [ ] core/runtime_configuration
- [ ] core/threading_base

Level 15:
- [ ] core/command_line_handling_local
- [ ] core/io_service
- [ ] core/schedulers
- [ ] core/synchronization

Level 16:
- [ ] core/futures
- [ ] core/thread_pools
- [ ] full/command_line_handling

Level 17:
- [ ] core/lcos_local
- [ ] core/pack_traversal
- [ ] core/resource_partitioner
- [ ] core/threading
- [ ] full/naming_base

Level 18:
- [ ] core/async_combinators

Level 19:
- [ ] core/execution

Level 20:
- [ ] core/executors

Level 21:
- [ ] core/async_local
- [ ] core/timed_execution

Level 22:
- [ ] core/algorithms
- [ ] core/resiliency
- [ ] core/thread_pool_util

Level 23:
- [ ] core/threadmanager

Level 24:
- [ ] core/runtime_local

Level 25:
- [ ] core/compute_local
- [ ] core/init_runtime_local
- [ ] full/parcelset_base

Level 26:
- [ ] core/include_local
- [ ] full/components_base
- [ ] full/plugin_factories

Level 27:
- [ ] full/actions_base
- [ ] full/naming

Level 28:
- [ ] full/actions
- [ ] full/components

Level 29:
- [ ] full/executors_distributed
- [ ] full/parcelset

Level 30:
- [ ] full/async_distributed
- [ ] full/parcelport_tcp

Level 31:
- [ ] full/agas_base
- [ ] full/resiliency_distributed

Level 32:
- [ ] full/agas
- [ ] full/async_colocated

Level 33:
- [ ] full/runtime_components

Level 34:
- [ ] full/lcos_distributed
- [ ] full/performance_counters

Level 35:
- [ ] full/distribution_policies

Level 36:
- [ ] full/runtime_distributed
- [ ] full/segmented_algorithms

Level 37:
- [ ] full/checkpoint
- [ ] full/collectives
- [ ] full/compute

Level 38:
- [ ] full/include
- [ ] full/init_runtime

---

## #5997: Coroutines do work with Apple Clang but not with gcc

**Labels:** compiler: gcc

## Expected Behavior

The [code](https://github.com/ModernCPPBook/Examples/blob/main/hpx/taylor_hpx_future_coroutine.cpp) should compile with both clang and gcc. 

## Actual Behavior

However, using gcc results in this error

```
/home/diehlpk/git/book/Examples/hpx/taylor_hpx_future_coroutine.cpp: In function ‘hpx::future<double> run(size_t, size_t, double)’:
/home/diehlpk/git/book/Examples/hpx/taylor_hpx_future_coroutine.cpp:38:77: error: use of deleted function ‘hpx::future<double>::future(const hpx::future<double>&)’
   38 |   for (size_t i = 0; i < futures2.size(); i++) result += co_await futures2[i];
      |                                                                             ^
In file included from /home/diehlpk/Compile/hpx-1.8.0/libs/core/runtime_local/include/hpx/runtime_local/runtime_local.hpp:12,
                 from /home/diehlpk/Compile/hpx-1.8.0/libs/core/init_runtime_local/include/hpx/init_runtime_local/init_runtime_local.hpp:20,
                 from /home/diehlpk/Compile/hpx-1.8.0/libs/full/init_runtime/include/hpx/hpx_init_params.hpp:13,
                 from /home/diehlpk/Compile/hpx-1.8.0/libs/full/init_runtime/include/hpx/hpx_init.hpp:16,
                 from /home/diehlpk/Compile/hpx-1.8.0/wrap/include/hpx/wrap_main.hpp:11,
                 from /home/diehlpk/Compile/hpx-1.8.0/wrap/include/hpx/hpx_main.hpp:9,
                 from /home/diehlpk/git/book/Examples/hpx/taylor_hpx_future_coroutine.cpp:3:
/home/diehlpk/Compile/hpx-1.8.0/libs/core/futures/include/hpx/futures/future.hpp:830:11: note: ‘hpx::future<double>::future(const hpx::future<double>&)’ is implicitly declared as deleted because ‘hpx::future<double>’ declares a move constructor or move assignment operator
  830 |     class future : public lcos::detail::future_base<future<R>, R>
      |           ^~~~~~
make[2]: *** [hpx/CMakeFiles/taylor_hpx_future_coroutine.dir/build.make:76: hpx/CMakeFiles/taylor_hpx_future_coroutine.dir/taylor_hpx_future_coroutine.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:1136: hpx/CMakeFiles/taylor_hpx_future_coroutine.dir/all] Error 2
```



## Steps to Reproduce the Problem

... Please be as specific as possible while describing how to reproduce your problem.

  1. Compile HPX with clang 12 and gcc 12
  1. Compile the example code with both of them

## Specifications

... Please describe your environment

  - HPX Version: 1.8.0
  - Platform (compiler, OS): Mac OS X with Apple Clang and Fedora Linux with gcc 12

---

## #5978: Registering Nested Component Actions

## Expected Behavior

I'm attempting to convert an established MPI code to HPX by writing an HPX version of the program's swappable communication submodule. I've been following along with the local to remote example in the documentation. I'm preserving most of the structure from the distributed memory verson of that example and trying to nest it in a class of the type being used for the communication submodule.

## Actual Behavior

When running the example below as is, mimicking the local to remote example with an extra layer of indirection to the components, I get an error about the `get_data_action` that I registered using `HPX_DEFINE_COMPONENT_DIRECT_ACTION()` not naming a type:

````
error: ‘get_data_action’ in ‘struct CommHPX::partition_server’ does not name a type
  763 | typedef CommHPX::partition_server::get_data_action get_data_action;
      |                                    ^~~~~~~~~~~~~~~
````

Trying to make `CommHPX` inherit `hpx::components::component_base<>` in the same manner as the `partition_server` component and adding a matching call to `HPX_REGISTER_COMPONENT()` as shown below throws a long list of errors regarding multiple definitions. I think I'm either fundamentally misunderstanding nested components or trying to leverage a code structure that HPX doesn't support.
````
typedef hpx::components::component<CommHPX> comm_hpx_type;
HPX_REGISTER_COMPONENT(comm_hpx_type, CommHPX)
````

## Steps to Reproduce the Problem

This is a stripped down version of the class structure of the communication module, as well as the macros I'm using to register the components and actions in global scope.

comm_hpx.h
````
class CommHPX {
    struct partition_data {}

    struct partition_server : hpx::components::component_base<partition_server> {
        partition_data get_data() const;
    }

    struct partition : hpx::components::client_base<partition, partition_server> {}
}

HPX_DEFINE_COMPONENT_DIRECT_ACTION(CommHPX::partition_server, get_data, get_data_action)

typedef hpx::components::component<CommHPX::partition_server> partition_server_type;
HPX_REGISTER_COMPONENT(partition_server_type, partition_server)

typedef CommHPX::partition_server::get_data_action get_data_action;
HPX_REGISTER_ACTION(get_data_action)
````



comm_hpx.cpp

````
hpx::future<CommHPX::partition_data> CommHPX::partition::get_data() const {
  get_data_action act;
  //return hpx::async(act, get_id(), t);
  return hpx::async(act, get_id());
}
````

## Specifications

  - HPX Version: 1.8
  - Platform (compiler, OS): CMake/3.21.1, GCC/8.3.0, Arch

---
