# GSoCGoogle Summer of Code

**Parent:** AFLplusplus — Project Ideas
**Source:** https://github.com/AFLplusplus/LibAFL/issues?q=state%3Aopen%20label%3A%22GSoC%22
**Scraped:** 2026-02-22T23:28:47.605554

---

## #3733: Expose `no_link_main` and `interceptors` as configurable features in `libafl_libfuzzer_runtime`

**Labels:** enhancement

Note this issue was created with the help of an LLM, and I've extensively reviewed it for correctness and accuracy.

**Is your feature request related to a problem? Please describe.**

LibAFL's `libFuzzer.a` cannot be linked into shared objects with GNU `ld` because `FuzzerInterceptors.cpp` introduces a `.preinit_array` section. The ELF specification states that `.preinit_array` is only processed in executable files and must not appear in shared objects ([ELF gABI, Dynamic Section](https://refspecs.linuxbase.org/elf/gabi4+/ch5.dynamic.html)). GNU `ld` enforces this at link time:

```
.preinit_array section is not allowed in DSO
```

This affects projects like [Ruzzy](https://github.com/trailofbits/ruzzy) (Ruby fuzzing) and [Atheris](https://github.com/google/atheris) (Python fuzzing) that merge `libFuzzer.a` with clang's sanitizer archives into shared objects (e.g. `asan_with_fuzzer.so`) which are `LD_PRELOAD`ed at runtime. This is a somewhat hacky solution, but it works.

LLVM/clang's libfuzzer avoids this by shipping the interceptors in a separate archive:

| Archive | `main` | Interceptors |
|---|---|---|
| `libclang_rt.fuzzer.a` | yes | no |
| `libclang_rt.fuzzer_no_main.a` | no | no |
| `libclang_rt.fuzzer_interceptors.a` | no | yes |

The `libafl_targets` crate already has the internal feature flags to control both — `libfuzzer_no_link_main` (guarding `main` via `#ifndef FUZZER_NO_LINK_MAIN` in `libfuzzer.c`) and `libfuzzer_interceptors` (gating `FuzzerInterceptors.cpp` compilation in `build.rs`) — but `libafl_libfuzzer_runtime` hardcodes them and doesn't expose them to consumers.

**Describe the solution you'd like**

Add crate-level features to `libafl_libfuzzer_runtime/Cargo.toml`:

```toml
[features]
default = ["interceptors"]
interceptors = ["libafl_targets/libfuzzer_interceptors"]
no_link_main = ["libafl_targets/libfuzzer_no_link_main"]
```

And remove `"libfuzzer_interceptors"` from the hardcoded `libafl_targets` dependency features list.

This is a backwards-compatible change — default behavior is preserved. Consumers can then configure the build via `build.sh`:

```bash
# Equivalent to libclang_rt.fuzzer_no_main.a (no main, no interceptors)
bash build.sh --cargo-args "--no-default-features --features no_link_main"

# No interceptors, with main (current weak symbol)
bash build.sh --cargo-args "--no-default-features"

# Default (current behavior, interceptors + main)
bash build.sh
```

**Describe alternatives you've considered**

- Using `lld` instead of GNU `ld`. lld permits `.preinit_array` in shared objects, but it adds a build dependency and the section is silently ignored at runtime anyway (the dynamic linker only processes `.preinit_array` for the main executable).
- Patching the cloned source with `sed -i '/"libfuzzer_interceptors",/d' Cargo.toml` before running `build.sh`. This works but is fragile and requires modifying LibAFL source.
- Stripping the `.preinit_array` section from `libFuzzer.a` with `objcopy --remove-section`

*[truncated]*

---

## #3731: Redundant Borrowing and Double Mapping in MappedCrossoverInsertMutator::mutate

### Description

The `MappedCrossoverInsertMutator::mutate` function performs redundant operations when accessing and mapping the corpus input:

1. The testcase is borrowed twice using `get_from_all(id)?.borrow_mut()`.
2. The input is loaded and mapped twice:
   - First to compute `other_size`
   - Second to retrieve the mapped input for mutation
3. Additional unnecessary `unwrap()` checks increase branching complexity.

This results in:
- Redundant function calls
- Extra borrow operations
- Unnecessary memory allocations
- Reduced readability

### Expected Behavior

The mapped input and its size should be retrieved in a single borrow scope and used directly for mutation without re-loading or re-mapping.

---

## #3729: Panic when using AFL++ with cmplog on some sizes

**Labels:** bug

AFL++'s cmplog passes can add integer comparisons with any byte size, not just power-of-2s.
When LibAFL encounters such a size, it panics: https://github.com/AFLplusplus/LibAFL/blob/c59e61e9f426e0036a3f15065ee98f4a99bbbb7c/crates/libafl_targets/src/cmps/mod.rs#L610-L634

AFL++'s GCC and clang plugin is not perfectly in sync how they choose the cmplog shape.
E.g. a 24-bit comparison is treated as a 32-bit in the clang plugin: https://github.com/AFLplusplus/AFLplusplus/blob/2c1f988ae6735f79af447dcbf8bd3011ec45a07e/instrumentation/cmplog-instructions-pass.cc#L416-L417
The GCC plugin on the other hand reports it as 24-bit via the `hookN` variant: 
https://github.com/AFLplusplus/AFLplusplus/blob/stable/instrumentation/afl-gcc-cmplog-pass.so.cc#L170-L173

I suggest treating 24-bit values as 32-bit, 40/48/56-bit values as 64-bit.
Larger values are not implemented currently, there is a TODO for that already in the code, that's another problem.

---

## #3724: Improvement on Intel-PT-based fuzzing capabilities

I noticed that LibAFL has been integrating the Intel-PT-based fuzzing capabilities using the [ptcov](https://crates.io/crates/ptcov) crate. I have also implemented a full-featured Intel-PT decoder [iptr](https://github.com/Evian-Zhang/iptr) using pure Rust with more idiomatic APIs in both low-level and bitmap-level APIs. 

Evaluated on the famous [`libxdc_experiments`](https://github.com/nyx-fuzz/libxdc_experiments) benchmark, it turns out that iptr has comparable performance with libxdc, the fastest Intel PT decoder written in C, with each target completed in 5-10 seconds. However, ptcov cannot run most of the targets (possible due to the approach that I build up `PtImage` since libxdc dumps memory in page level instead of image level, leading to some instructions split into two pages), while some targets cannot complete in even 18 hours... I guess the reason for the low performance is that ptcov does not use TNT cache to accelerate the bitmap update.

I also managed to integrate iptr into LibAFL, creating a fuzzer with the same functionality with [`intel_pt_command_executor`](https://github.com/AFLplusplus/LibAFL/tree/main/fuzzers/binary_only/intel_pt_command_executor). Due to the fact that the target program is very small, the performance improvement is not as large as what we see in `libxdc_experiments`. Anyway, it can still discover the vulnerabilities as ptcov does, proving the full functionalities.

I wonder whether the LibAFL team is willing to accept iptr as an alternative Intel PT decoder. I can think of four feasible approaches:

1. iptr as an alternative with independent sub-crate like [`libafl_intelpt`](https://github.com/AFLplusplus/LibAFL/tree/main/crates/libafl_intelpt)
2. iptr and ptcov being two configurable backend features in [`libafl_intelpt`](https://github.com/AFLplusplus/LibAFL/tree/main/crates/libafl_intelpt)

   However, I found that the logics and APIs are highly coupled with ptcov in both [`libafl_intelpt`](https://github.com/AFLplusplus/LibAFL/tree/main/crates/libafl_intelpt) and the [Intel PT executor hook](https://github.com/AFLplusplus/LibAFL/blob/main/crates/libafl/src/executors/hooks/intel_pt.rs), with some ptcov-related structs exposed in public APIs.

   If we want to use features to select these two backends, some refactor works still need to be done.
3. Rewrite ptcov using iptr
4. Directly use iptr to replace ptcov.

I'm willing to assist in any of the above approaches. Which approach do you prefer? :)

cc @Marcondiro @domenukk

---

## #3715: libafl pointers getting corrupted when a harness function overflows (mac m4)

**Labels:** bug

**IMPORTANT**
1. You have verified that the issue to be present in the current `main` branch

Thank you for making LibAFL better!

**Describe the bug**

I have used Libafl at main branch with commit `a2eb6ecf822e2a30839f1b698ae3640556f9507d`

cargo 1.91.1 (ea2d97820 2025-10-10)
rustup 1.28.2 (e4f3ad6f8 2025-04-28)

The target function `processVulnerableImageFromFile:` has a stack buffer overflow. When it overflows, it writes past its stack frame and corrupts memory that belongs to:
                                                                                  
```
  ┌─────────────────────────────┐  High addresses
  │  LibAFL's executor state    │  ← gets corrupted
  │  (fuzzer, state, mgr ptrs)  │
  ├─────────────────────────────┤
  │  Frida helper data          │  ← gets corrupted
  ├─────────────────────────────┤
  │  harness function      │
  ├─────────────────────────────┤
  │  processVulnerableImageFromFile  │
  │  [BUFFER OVERFLOW HAPPENS]  │  ← overflow writes upward
  │  local buffer               │
  └─────────────────────────────┘  Low addresses
```
attaching debugger revealed this:

```
(lldb) process attach --pid 24973
Process 24973 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x1111111111111111)
    frame #0: 0x0000000100a93d40 libafl_fuzzer`libafl::executors::hooks::unix::unix_signal_handler::inproc_crash_handler::hcff683bd75bb190a + 3952
libafl_fuzzer`libafl::executors::hooks::unix::unix_signal_handler::inproc_crash_handler::hcff683bd75bb190a:
->  0x100a93d40 <+3952>: ldp    q0, q1, [x23]
    0x100a93d44 <+3956>: ldp    q2, q3, [x23, #0x20]
    0x100a93d48 <+3960>: stp    q2, q3, [x0, #0x20]
    0x100a93d4c <+3964>: stp    q0, q1, [x0]
Target 0: (libafl_fuzzer) stopped.
Executable binary set to "/Users/vinay/research_libafl_mac_patch/libafl_fuzzer/target/release/libafl_fuzzer".
Architecture set to: arm64-apple-macosx-.
(lldb) bt
warning: could not execute support code to read Objective-C class data in the process. This may reduce the quality of type information available.

* thread #1, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x1111111111111111)
  * frame #0: 0x0000000100a93d40 libafl_fuzzer`libafl::executors::hooks::unix::unix_signal_handler::inproc_crash_handler::hcff683bd75bb190a + 3952
    frame #1: 0x0000000100c003f4 libafl_fuzzer`libafl::executors::hooks::unix::unix_signal_handler::_$LT$impl$u20$exceptional..unix_signals..SignalHandler$u20$for$u20$libafl..executors..hooks..inprocess..InProcessExecutorHandlerData$GT$::handle::hfe2882b0a0512d66 + 100
    frame #2: 0x0000000100b05b98 libafl_fuzzer`exceptional::unix_signals::handle_signal::h7138974ceaf314e5 + 132
    frame #3: 0x0000000100da0150 libafl_fuzzer`gum_exceptor_backend_on_signal + 448
    frame #4: 0x000000019456d6a4 libsystem_platform.dylib`_sigtramp + 56
    frame #5: 0x000000019443ca94 libsystem_c.dylib`__abort + 164
    frame #6: 0x000000019442d818 libsystem_c.dylib`__st

*[truncated]*

---

## #3709: Is FridaHelperObserver really necessary for Frida executor?

FridaHelperObserver doesn't support Inputs w/o target_bytes(). So it isn't possible to combine Nautilus with Frida executor.

---

## #3706: GSoC 2026

**Labels:** GSoC

Welcome to our Google Summer of Code idea list for 2026!

Our projects are technical, demanding, and meant for students who genuinely want to learn by doing. We value careful thinking, solid fundamentals, and the ability to work independently more than flashy output. Quality matters here. If we’re not confident a collaboration will work well, we prefer not to take a student at all.

Before applying, take time to understand the project space. Read existing documentation and code, experiment locally, and ask precise, well-researched questions. Early pull requests, small but thoughtful, are strongly encouraged and are the best way to demonstrate seriousness and technical fit.

We do not accept AI-generated, low-effort proposals or submissions. If you use tools, you are still fully responsible for understanding and defending every line of what you submit.

If this sounds like the kind of environment you want to grow in, join the fuzzing Discord, introduce yourself, and start engaging early. The strongest applications usually come from students who do exactly that.

Below you find a list of potential projects, but you can come up with your own!

---

## #3705: Proposal: Port TinyInst backend to macOS (Apple Silicon) + add example integration

**Labels:** enhancement

**Is your feature request related to a problem? Please describe.**
Currently, libAFL provides integration with TinyInst only on Windows platforms.
However, there is no available TinyInst backend or example for macOS environments, especially for Apple Silicon (arm64).

This limits the usability of libAFL for users and researchers who want to perform efficient instrumentation-based fuzzing on modern macOS hardware.

**Describe the solution you'd like**
I would like to propose adding support for TinyInst on macOS (Apple Silicon) within libAFL by:
	•	Porting the TinyInst backend to macOS (arm64)
	•	Integrating it properly into the existing libAFL instrumentation framework
	•	Adding a minimal working example demonstrating TinyInst-based fuzzing on macOS

This would enable high-performance fuzzing workflows on Apple Silicon systems and expand libAFL’s cross-platform instrumentation capabilities.

**Describe alternatives you've considered**
Other existing macOS instrumentation options (e.g., Frida mode) are available, but TinyInst support would provide an additional lightweight backend, especially for Apple Silicon-focused fuzzing.

**Additional context**
I have already tested an initial TinyInst + libAFL setup on Apple Silicon and observed promising performance improvements.

I am planning to work on the macOS port and submit a PR including both the backend integration and a minimal working example.

Before starting the full implementation, I wanted to ask whether this contribution would be welcomed upstream and if there are any preferred design constraints or ongoing related efforts.

---

## #3699: Rust v1.93 causes clippy:non_ascii_literal in the CI.

**Labels:** bug

**IMPORTANT**
1. You have verified that the issue to be present in the current `main` branch

Thank you for making LibAFL better!

**Describe the bug**
There was a recent release on the rust release (v1.93) that is causing the CI to trigger a failure for clippy:non_ascii_literal for libafl_frida.

Getting no error for v1.92.

**To Reproduce**
Steps to reproduce the behavior:
1. rustup install 1.93.0
2. rustup override set 1.93.0
3. cd LibAFL
4. cargo --version  
// You should be seeing 1.93.0
5. cargo clippy --package libafl_frida --all-targets

**Expected behavior**
You should be seeing the following error:

<img width="568" height="398" alt="Image" src="https://github.com/user-attachments/assets/4c446f34-16be-4c04-a9a1-0e7548d87d6f" />

**Screen output/Screenshots**
```
error: this lint expectation is unfulfilled
   --> crates/libafl_frida/src/asan/errors.rs:172:18
    |
172 |         #[expect(clippy::non_ascii_literal)]
    |                  ^^^^^^^^^^^^^^^^^^^^^^^^^
    |
    = note: `-D unfulfilled-lint-expectations` implied by `-D warnings`
    = help: to override `-D warnings` add `#[allow(unfulfilled_lint_expectations)]`

error: this lint expectation is unfulfilled
   --> crates/libafl_frida/src/asan/errors.rs:207:26
    |
207 |                 #[expect(clippy::non_ascii_literal)]
    |                          ^^^^^^^^^^^^^^^^^^^^^^^^^

error: this lint expectation is unfulfilled
   --> crates/libafl_frida/src/asan/errors.rs:256:26
    |
256 |                 #[expect(clippy::non_ascii_literal)]
    |                          ^^^^^^^^^^^^^^^^^^^^^^^^^

error: this lint expectation is unfulfilled
   --> crates/libafl_frida/src/asan/errors.rs:306:26
    |
306 |                 #[expect(clippy::non_ascii_literal)]
    |                          ^^^^^^^^^^^^^^^^^^^^^^^^^

error: this lint expectation is unfulfilled
   --> crates/libafl_frida/src/asan/errors.rs:339:30
    |
339 |                     #[expect(clippy::non_ascii_literal)]
    |                              ^^^^^^^^^^^^^^^^^^^^^^^^^

error: this lint expectation is unfulfilled
   --> crates/libafl_frida/src/asan/errors.rs:376:30
    |
376 |                     #[expect(clippy::non_ascii_literal)]
    |                              ^^^^^^^^^^^^^^^^^^^^^^^^^

error: this lint expectation is unfulfilled
   --> crates/libafl_frida/src/asan/errors.rs:403:26
    |
403 |                 #[expect(clippy::non_ascii_literal)]
    |                          ^^^^^^^^^^^^^^^^^^^^^^^^^

error: this lint expectation is unfulfilled
   --> crates/libafl_frida/src/asan/errors.rs:424:26
    |
424 |                 #[expect(clippy::non_ascii_literal)]
    |                          ^^^^^^^^^^^^^^^^^^^^^^^^^

error: this lint expectation is unfulfilled
   --> crates/libafl_frida/src/asan/errors.rs:441:26
    |
441 |                 #[expect(clippy::non_ascii_literal)]
    |                          ^^^^^^^^^^^^^^^^^^^^^^^^^

error: this lint expectation is unfulfilled
   --> crates/libafl_frida/src/

*[truncated]*

---

## #3697: `tuple_list_ex` does not build with `--no-default-features --all-targets`

**Labels:** bug

On c88849bb833c9e6ed8ece0a04b983e6be1500b24,
```
cd crates/tuple_list_ex
cargo check --no-default-features --all-targets

error[E0412]: cannot find type `OwnedMutSlice` in this scope
    --> crates/tuple_list_ex/src/lib.rs:1130:39
     |
1130 |         type OwnedMutSliceAlias<'a> = OwnedMutSlice<'a, u8>;
     |                                       ^^^^^^^^^^^^^ not found in this scope
```

**Expected behavior**
It compiles

---

## #3694: Multiple qemu usermode tests disabled until a bug is fixed

**Labels:** bug

#3650 disables tests for `qemu_coverage` and `qemu_tmin` because of a bug in the restarting manager.
they should be enabled again once the bug is fixed.

---

## #3688: README: Python bindings instructions missing correct working directory for maturin

The Python bindings README instructs users to run maturin develop but does not specify the directory where this command must be executed.

Also there is an install cmd first before creating the virtual environment.

---

## #3664: Add module-level documentation for restarting and multi-machine event managers

**Labels:** enhancement

**Is your feature request related to a problem? Please describe.**

While going through the event manager implementations, I found it hard
to understand the intent and correct usage of `restarting.rs` and
`multi_machine.rs` because they don’t have any module level documentation or
a simple introduction.

Most other event managers such as tcp,event_hooks,llmp include a 
short comment at the top explaining what they do and when to 
use them, but these two don’t, which makes it difficult
for new contributors to quickly grasp their purpose.

**Describe the solution you'd like**

Add short module level rustdoc comments to `restarting.rs` and
`multi_machine.rs` which explain what each event manager does and
when it should be used.

For example, a one–two lines introduction at the top of each file
(similar to the other event managers) describing the purpose of the
restarting event manager and how the multi-machine setup works at a high
level. This would make them much easier to understand and consistent with
the rest of the codebase.


**Describe alternatives you've considered**

Reading through the source code and related examples is possible, but without
some small documentation explaining a bit about these event managers,
it will require a significant amount of time and prior architectural
knowledge to figure it out. Adding these short and conceptual docs
seems like the simplest and most effective improvement.

---

## #3649: Undefined Symbols for Crate libafl-libfuzzer (with nix)

**Labels:** bug

# Preface / IMPORTANT

> 1. You have verified that the issue to be present in the current `main` branch

Yes, I can confirm the issue on the current `main` branch.
I've provided a fully reproducible environment and a PoC at my repository: [fuzz-ciborium-poc](https://github.com/nausicaea/fuzz-ciborium-poc).

> Thank you for making LibAFL better!

Thank YOU for creating LibAFL in the first place! <3
Note that the error may be on my side. If I can provide more information, please let me know.

# Describe the Bug

Any attempts to build the fuzzing target (see my PoC above) fail with "Undefined symbols" errors. The following symbols are undefined:

* _LLVMFuzzerCustomCrossOver
* _LLVMFuzzerCustomMutator
* _libafl_main

Additional context clues see below.

# To Reproduce

1. Download the code from the linked repository: [fuzz-ciborium-poc](https://github.com/nausicaea/fuzz-ciborium-poc)
2. Install the [nix](https://nixos.org/download/#nix-install-macos) package manager
3. Navigate to the repository code and run `nix develop` to instantiate the development environment
4. Either build or run the fuzzing target with 
    `cargo fuzz build --fuzz-dir=. parse_cbor` or `cargo fuzz run --fuzz-dir=. parse_cbor`

# Expected behavior

I expect the build process to succeed.

# Additional context

## System Information

I am running an Apple MacBook Air M1 from 2020.

```
$ sw_vers
ProductName:            macOS
ProductVersion:         15.7.3
BuildVersion:           24G419
```

## Nix Version

```
$ nix --version
nix (Nix) 2.31.2
```

## Build Output

```
$ cargo fuzz build --fuzz-dir=. parse_cbor
   Compiling proc-macro2 v1.0.104
   Compiling quote v1.0.42
   Compiling unicode-ident v1.0.22
   Compiling libc v0.2.179
   Compiling serde_core v1.0.228
   Compiling shlex v1.3.0
   Compiling find-msvc-tools v0.1.6
   Compiling equivalent v1.0.2
   Compiling hashbrown v0.16.1
   Compiling rustversion v1.0.22
   Compiling winnow v0.7.14
   Compiling zerocopy v0.8.31
   Compiling indexmap v2.12.1
   Compiling toml_writer v1.0.6+spec-1.1.0
   Compiling toml_parser v1.0.6+spec-1.1.0
   Compiling cfg-if v1.0.4
   Compiling serde v1.0.228
   Compiling arbitrary v1.4.2
   Compiling syn v2.0.113
   Compiling ciborium-io v0.2.2
   Compiling serde_spanned v1.0.4
   Compiling toml_datetime v0.7.5+spec-1.1.0
   Compiling jobserver v0.1.34
   Compiling toml v0.9.10+spec-1.1.0
   Compiling cc v1.2.51
   Compiling libfuzzer-sys v0.4.10
   Compiling libafl_libfuzzer v0.16.0 (https://github.com/AFLplusplus/LibAFL.git#541f2ab6)
   Compiling zerocopy-derive v0.8.31
   Compiling serde_derive v1.0.228
   Compiling half v2.7.1
   Compiling ciborium-ll v0.2.2
   Compiling ciborium v0.2.2
   Compiling fuzz v0.0.0 (/Users/user/fuzz-ciborium)
error: linking with `cc` failed: exit status: 1
  |
  = note:  "cc" "/Users/user/fuzz-ciborium/target/aarch64-apple-darwin/release/deps/rustc0F986c/symbols.o" "-Wl,-rpath,<sysroot>/lib/rustlib/aarch64-apple-darwin/lib" "-lrustc-nightly_rt.asan" "<2 object 

*[truncated]*

---

## #3465: Fast snapshots randomly fail upon restoration in QEMU system mode

**Labels:** bug

**Describe the bug**

When using fast snapshots (syx snapshots) in QEMU system mode to restore OS execution context (GNU/Linux), the snapshot restoration frequently fails and corrupts the OS memory. The issue occurs randomly in most snapshot attempts, making reliable state restoration difficult.

**To Reproduce**

Steps to reproduce the behavior:

1. Set up LibAFL fuzzing with QEMU in system mode
2. Configure fast snapshots
3. Repeatedly create and restore snapshots during fuzzing
4. Observe that in most cases, the restored OS state is corrupted

**Expected behavior**

Fast snapshots should consistently restore the OS execution context without memory corruption. The `restore_fast_snapshot()` function should reliably return the system to a valid state.

**Additional context**

- Through experimentation, I found that calling `check_fast_snapshot()` after `restore_fast_snapshot()` can verify snapshot integrity
- The workaround involves creating a loop that repeatedly takes and restores snapshots until `check_fast_snapshot()` reports no inconsistencies
- Currently, accessing the `nb_page_inconsistencies` field from `QemuSnapshotCheckResult` is not possible as the field is private
- A potential fix would involve making this field accessible (either public or via a getter method) to enable snapshot validation

QEMU launch parameters:

```shell
-cpu max \
-icount auto \
-m 8G \
-L /usr/share/seabios/ \
-L /usr/share/qemu/ \
-L /usr/lib/ipxe/qemu/ \
-uuid aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee \
-drive if=ide,media=disk,id=main_drive,file=./image.qcow2,format=qcow2 \
-netdev user,id=mgmt,net=10.0.2.0/24,restrict=on \
-device e1000,netdev=mgmt,id=mgmt-dev \
-netdev user,id=outside,net=10.0.3.0/24,restrict=on,hostfwd=tcp::8443-:443 \
-device e1000,netdev=outside,id=outside-dev \
-S \
-serial telnet::30007,server=on,wait=off \
-serial mon:telnet::5444,server=on,wait=off \
-nodefaults \
-vga none \
-nographic
```

Device list:

```text
timer, slirp, slirp, cpu_common, cpu, kvm-tpr-opt, apic, 0000:00:00.0/I440FX, PCIHost, PCIBUS, fw_cfg, dma, dma, mc146818rtc, 0000:00:01.1/ide, i2c_bus, 0000:00:01.3/piix4_pm, 0000:00:01.0/PIIX3, i8259, i8259, ioapic, hpet, i8254, pcspk, serial, serial, fdc, ps2kbd, ps2mouse, pckbd, vmmouse, port92, smbus-eeprom, smbus-eeprom, smbus-eeprom, smbus-eeprom, smbus-eeprom, smbus-eeprom, smbus-eeprom, smbus-eeprom, 0000:00:02.0/e1000, 0000:00:03.0/e1000, acpi_build
```

---

## #3462: Allow exiting the current execution in QEMU syscall hooks

**Labels:** enhancement

QEMU syscall hooks currently have two options: run the syscall, or skip it and provide a return value. I think it would be valuable to add a third: abort the current execution (probably with a given `ExitKind`). My particular use-case is that I want to hook the `exit` and `exit_group` system calls.

Here's my attempt at an `exit` syscall handler:
```rust
#[allow(clippy::too_many_arguments)]
fn syscall_exit_hook<ET, I, S>(
    qemu: Qemu,
    _emulator_modules: &mut EmulatorModules<ET, I, S>,
    _s: Option<&mut S>,
    code: i32,
    arg0: u64,
    _arg1: u64,
    _arg2: u64,
    _arg3: u64,
    _arg4: u64,
    _arg5: u64,
    _arg6: u64,
    _arg7: u64,
) -> SyscallHookResult {
    let code = i64::from(code);
    if code != x86_64::SYS_exit && code != x86_64::SYS_exit_group {
        return SyscallHookResult::Run;
    }

    let cpu = qemu.current_cpu().expect("No current CPU in syscall hook?");
    let rip = cpu.read_reg(Regs::Rip).unwrap();
    debug!("Exiting with: {:#x} at {:#x}", arg0, rip);
    // TODO: What to put here?
    // cpu.trigger_breakpoint();
    // unsafe { qemu.target_signal(Signal::SigAbort) };
    SyscallHookResult::Skip(arg0)
}
```
The problem is that I don't know what to put after the TODO. If I don't put anything, my target enters a loop until it times out. If I put `trigger_breakpoint`, the target just hangs (I think). If I raise a signal, then the `EventManager` has to restart the process. Ideally, I'd just return to the harness with an OK exit from QEMU.

---

## #3460: IfElseRuntime incorrect behaviour

**Labels:** bug

**Describe the bug**
`FridaRuntime`s used in `IfElseRuntime` do not work correctly. This breaks ASAN in the `frida_libpng` example fuzzer for example.

**To Reproduce**
Either simply run the `frida_libpng` example fuzzer and observe that ASAN is not working correctly, or:

1. Create a fuzzer with `asan` in the `runtimes` for `FridaInstrumentationHelper` 
2. Verify that ASAN is enabled and working
3. Replace `asan` with `IfElseRuntime::new(move || Ok(true), tuple_list!(asan), tuple_list!())`
4. Observe that ASAN is no longer working

**Expected behavior**
`IfElseRuntime::new(move || Ok(true), tuple_list!(asan), tuple_list!())` should behave identically to `asan`.

---

## #3450: Incorrect Asan errors handling (frida, windows)

**Labels:** bug

Currently, if Frida Asan detects an error, the handling of is not working correctly.
Without continue-on-error, it panics after reporting the error. However, as this is done from inside the hooks, different parts (such as allocator) are under mutex and then the processing gets suck as we try to gracefully clean the allocatoed memory.
With continue-on-error and if iterations are used, when we get to the end of the executor's `run_target`, we abort. However, Fuzzer-respawner refuses to start a new instance

I haven't touched the project for a while, so I'm not sure if these changes are relatively new.
Unfortunately, I'm not familiar enough with the respawner logic. If we can make it work this would be a working workaround.

---

## #3404: `InMemoryOnDiskCorpus::with_meta_format_and_prefix` does not actually add a prefix to files

It looks like the `prefix` field of `InMemoryOnDiskCorpus` can be set using `with_meta_format_and_prefix`, but it is actually never used to compose the name of the corpus files [as the documentation states][1]. The same holds for `OnDiskCorpus::with_prefix`, which offloads that functionality to this struct.

https://github.com/AFLplusplus/LibAFL/blob/fb5772e425fef60cfa7529488c98542254b1e543/crates/libafl/src/corpus/inmemory_ondisk.rs#L55-L65

It looks like the `prefix` field was added as part of https://github.com/AFLplusplus/LibAFL/pull/981 but never completely implemented.

[1]: https://docs.rs/libafl/latest/libafl/corpus/inmemory_ondisk/struct.InMemoryOnDiskCorpus.html#method.with_meta_format_and_prefix

---

## #3401: `ExitKind::Ok` exposing the result of `libfuzzer_test_one_input`

**Labels:** enhancement

Currently, `libfuzzer_test_one_input` returns an i32 that is discarded when turning into `ExitKind::Ok`, whereas the value could potentially signal interestingness from the harness leveraged by domain-specific fuzzers. I suppose `ExitKind` is part of the public API so it wouldn't be possible to change it after this point, but perhaps an `ExitKind::Value(i32)` would come in handy?

---

## #3391: libafl_ar and libafl_cc automatic configurations mechanism doesn't support response files.

**Labels:** bug

**Describe the bug**
Modern toolchain components support 'response files', `@`-prefixed arguments which are names of files including additional command line arguments.

The logic which replaces e.g. `xxx.o` with `xxx.coverage.o` in libafl_cc and libafl_ar, when using multiple configurations, does not know about response files, and so projects which use them in their build systems produce incorrect compilation results.

We should refactor the libafl_cc crate to fully support response files.

---

## #3388: Libafl-Libfuzzer does not build with CARGO_TARGET_DIR

When trying to build libafl-libfuzzer with a custom `CARGO_TARGET_DIR`, the following call fails:
https://github.com/AFLplusplus/LibAFL/blob/90cb9a2919faf386e0678870e52784070cdac4b6/crates/libafl_libfuzzer/build.rs#L163

Likely we'll have to calculate paths differntly in this case.

---

## #3362: make the fuzzer to have multiple executors

**Labels:** enhancement

**Is your feature request related to a problem? Please describe.**
I'm currently fuzzing the Linux kernel in a Syzkaller-like setup, where an executor agent (similar to syz-executor) runs inside a QEMU VM. This agent executes seeds on behalf of the LibAFL executor and communicates with it via a TCP connection. In my design, the LibAFL executor is a lightweight wrapper around the QEMU VM harness, responsible for dispatching commands and seeds to the executor agent inside the VM.

**Describe the solution you'd like**
I would like LibAFL to support multiple executors within a single fuzzer instance. In this setup, the fuzzer could:

1. Assign seeds to idle executors within the same fuzzer instance.
2. Asynchronously monitor all executors for completed tasks.
3. Evaluate the execution results as they are returned.

This would allow me to run multiple executor agents inside a single VM, significantly reducing the memory usage of running multiple VMs while maintaining the ability to fuzz concurrently.

**Describe alternatives you've considered**
- **Multiple fuzzer instances**: I considered running multiple fuzzer instances, each with its own VM. However, this approach is inefficient in my use case due to the high memory overhead of running multiple VMs.
- **Custom executor management**: I could implement custom logic outside of LibAFL to manage multiple executor agents within a single VM. However, this would require significant effort and would duplicate functionality that could be integrated into LibAFL itself.

**Additional context**
In my use case, the host-side LibAFL executor is a lightweight wrapper of my custom harness that communicates with the VM-side executor agent via TCP to dispatch commands and seeds. Supporting multiple executors within a single fuzzer instance would allow me to leverage this design more effectively, enabling concurrent fuzzing without the need for multiple VMs.

---

## #3343: Nautilus Grammar Macro

**Labels:** enhancement

**Is your feature request related to a problem? Please describe.**
When writing Nautilus grammar, I've found it's annoying to use a separate file or just have to embed it in my Rust code in a way that doesn't benefit from Rust's typing system.

**Describe the solution you'd like**
I want there to be some sort of macro that makes it easy to make a Nautilus grammar, is checked at compile time, and just allows for more synergy in my code.

**Describe alternatives you've considered**
I've looked around for a macro that does something similar but I haven't found anything. The only alternatives are ones I don't really like working with, e.g. `NautilusContext::from_file` or hand rolling a vector in my code using `NautilusContext::with_rules`

**Additional context**
I made a [small macro crate](https://github.com/AshrafIbrahim03/nautilus-macro) that solves the exact problem I describe. I don't have a lot of experience making macros, but this seemed like a nice place to start. I would appreciate some feedback if this seems like a good feature.

The macro makes a Vec<[(&str,&[u8])]> which is what's needed by `NautilusContext::with_rules`. Using this macro with `NautilusContext::with_rules` allows for compile time checked Nautilus grammar definitions.

I figured making a PoC before directly submitting a PR would be better.

---

## #3335: `libafl_qemu` can not build ASAN for mips target

**Labels:** bug

**IMPORTANT**
1. You have verified that the issue to be present in the current `main` branch

Thank you for making LibAFL better!

**Describe the bug**
In the `just/envs/.env.mips` file, missing relevant fields for building asan. 
If we manully create them and try compile again, we will get an error because the latest Rust version does not support cross-compilation for MIPS.

**To Reproduce**
Steps to reproduce the behavior:
1. Just using `ARCH=mips just build` try to build the qemu_launcher
2. run `rustup target list | grep mips` and we can not find any mips support ....

**Expected behavior**
1. I will try to see if it's possible to compile a prebuilt version using rust cross....

**Additional context**
Add any other context about the problem here.

---

## #3312: Add a dedicated mechanism for disabling a test case

**Labels:** enhancement

**Is your feature request related to a problem? Please describe.**
Let's say we wanna disable a testcase (because we are not interested in it anymore). The only way using the current API is to remove it and then add it as disabled. However, as it is indirect, it has potentially problematic consequences. For example, a new id will be given to the test case (which can cause the `parent_id` chain to break), or might delete some information (like in `OnDiskCorpus`)

**Describe the solution you'd like**
A dedicated API for disabling a test case.

**Describe alternatives you've considered**
Using `remove` and then `add_disabled`.
Also, `set_disabled` on the test case is not enough. It is not connected with the scheduler or the corpus, which may break the semantics (e.g., having a corpus with all disabled test cases is not considered empty).

---

## #3291: doc: List of papers

**Labels:** enhancement

It would be nice if the documentation had a list of papers *about* LibAFL including:

https://download.vusec.net/papers/libaflgo_eurosp25.pdf
https://hal.science/hal-04500872/
https://dl.acm.org/doi/abs/10.1145/3605157.3605176

And a list of papers *using* LibAFL, e.g.:

https://ieeexplore.ieee.org/abstract/document/10190370
https://dl.acm.org/doi/abs/10.1145/3597926.3604927

---

## #3288: crash in grimoire's generalization stage is not added to objective corpus

**Labels:** bug

i'll fix it

This may be present in other stages where inputs are modified and `Executor::run_target` is used. Not the case in tracing since input is unmodified but maybe in colorization?

---

## #3273: Replace bincode with postcard (or vice versa)

We have two serializer libraries that do pretty much the same (fast no-std-ready serialization): [bincode](https://crates.io/crates/bincode) and [postcard](https://crates.io/crates/postcard).
Most things in LibAFL use postcard right now, except for concolic.

We should remove bincode - unless it's more performant, then we should move everything to it and remove postcard.

---

## #3218: Split up LibAFL-bolts into reusable libraries

We have a bunch of cool libs hidden inside libafl-bolts.
Let's break them apart for people to use individual components outside of libafl more easily.

In general, I propose the following libs (renamed according to crates.io name availability), with descriptions:

`shmem`: Shared Memory support for Windows, Linux, MacOS, *nix
`signal-handler`: exception handling library for raw &unsafe exception/crash handling
`fast-rands`: Non-cryptographically secure (but fast) RNGs
`anymap`: Map to store and retrieve types, SerDe compatible
`build_id2`: Updated and maintained build id library
`core_affinity2`: Updated and maintained core_affinity library with larger OS support
`llmp`: Low-level message passing: A lockfree IPC library for many-to-one - one-to-many messages
`minibsod`: Write stack traces on crashes
`ownedref`:  Wrappers that abstracts references (or pointers) and owned data accesses, that deserialize to owned values
`tuple_list_ex`: Additional methods for compiletime tuple_lists
`libafl-simd`: SIMD acceleration
`libafl-bolts`: all the rest

---

## #3208: Publish `libafl_nyx` on crates.io

**Labels:** enhancement

I've been working on developing a library that builds upon `libafl_nyx`. I've noticed that it isn't published on crates.io at all; this makes it difficult to work with when I'm pulling other libraries in that build upon `libafl` but reference the crates.io version, not the git version. The current fix (changing dependencies all to git) would constitute traversing dependencies I'm pulling in and patching their sources, which isn't the most ideal solution.

Can `libafl_nyx` be published on crates.io, or are there technical hurdles preventing such? I realize it has a lot of moving parts in its build system and packer to make everything work right; I just wanted to make sure there wasn't an easy publish that could happen before I go ahead with switching all my dependencies to the libAFL git repo.

---

## #3168: Seeding rand does not make the fuzzing campaign deterministic

**Labels:** bug

(Submitted upon email request for preserving anonymity; I cannot give follow-up details on this issue)

Seeding the rand used in the state does not make the fuzzing campaign deterministic even when a single fuzzer is used with 100% stability. As such, there is a non-determinism source which is affecting runs that is unaccounted for in "standard" fuzzers.

We should identify the source of this non-determinism so that users seeking to do replayable fuzzer campaigns may do so reliably.

---

## #3152: libfuzzer_libpng examples are broken on MacOS

**Labels:** bug, macos

I'm running current MacOS (Apple Silicon, Xcode command-line tools installed), current Rust, current LibAFL.

Logs for `just fuzzer > out.log 2>&1`:

[libfuzzer_libpng.log](https://github.com/user-attachments/files/19709602/out.log)

[libfuzzer_libpng_centralized.log](https://github.com/user-attachments/files/19710015/libfuzzer_libpng_centralized.log)

---

## #3103: [librasan]: link libqasan statically with baremetal application

#### Description 
I am experimenting on writing a fuzzer for a cross compiled application on aarch64.
For now, if I understand correctly, `libqasan` can only get linked dynamically with `LD_LIBRARY_PATH` and override function symbols (`malloc`, `free` etc). 
I am not sure  `libqasan.so` can be linked with a baremetal application, though

#### Questions
1. Is there a way to link `libqasan.so` to a baremetal app?
2. If not, would statically linking `libqasan.a` (`.renamed`) archive file, be a possible solution?
3. I already have experimented with linking `libqasan.a` (`libqasan.renamed` actually), and the final question is, what header file should be imported to the baremetal target in order to build it with `malloc`, `free` etc defined in `libqasan`? As I can see, the old implementation `qasan` has a `libqasan.h` file for importing it to the target. How can I override `malloc` with a potential static link with `libqasan`?

#### Examples
For example building the `fuzzers/full_system/qemu_baremetal` example with `libqasan.a`.
**NOTE: it is not a working example, I just put it here to show a simple use case**
```bash
    arm-none-eabi-gcc -ggdb -ffreestanding -nostartfiles -lgcc \
        -T example/mps2_m3.ld \
        -mcpu=cortex-m3 \
        -D "TARGET_{{ uppercase(flavor) }}" \
        -I {{BUILD_DIR / "include"}} \
        example/main.c \
        libqasan.a \
        example/startup.c \
        -o {{TARGET_DIR}}/example.elf
```

---

## #3100: Full system qemu baremetal for riscv

# Description
I am trying to fuzz the riscv32 baremetal program in qemu full system emulation mode in LibAFL. Currently, I have made following changes to the given Arm example accordingly to match with riscv.
- Changed the `Cargo.toml` file to install qemu riscv32 version.
- Changed the `Justfile` to modify the gcc toolchain for riscv32 and to modify the qemu machine to `sifive_e`
- Then I made changes to the linker file according to `sifive_e` machine.

I was able to successfully build the environment (`just build`). However, when running the fuzzer(`just run`), I am getting following error. 
```afluser@860c6ff8fa77:/workspaces/wolfboot-fuzzer/LibAFL/fuzzers/full_system/qemu_riscv32$ just run
mkdir -p "/workspaces/wolfboot-fuzzer/LibAFL/fuzzers/full_system/qemu_riscv32/target"
qemu-img create -f qcow2 /workspaces/wolfboot-fuzzer/LibAFL/fuzzers/full_system/qemu_riscv32/target/dummy.qcow2 32M
Formatting '/workspaces/wolfboot-fuzzer/LibAFL/fuzzers/full_system/qemu_riscv32/target/dummy.qcow2', fmt=qcow2 cluster_size=65536 extended_l2=off compression_type=zlib size=33554432 lazy_refcounts=off refcount_bits=16
riscv32-unknown-elf-gcc -ggdb -ffreestanding -nostartfiles -lgcc -T example/sifive_e.ld -D "TARGET_BREAKPOINT" -I /workspaces/wolfboot-fuzzer/LibAFL/fuzzers/full_system/qemu_riscv32/target/release/include example/main.c example/startup.c -o /workspaces/wolfboot-fuzzer/LibAFL/fuzzers/full_system/qemu_riscv32/target/example.elf
cargo build --profile release --no-default-features --features std,breakpoint --target-dir /workspaces/wolfboot-fuzzer/LibAFL/fuzzers/full_system/qemu_riscv32/target
    Finished `release` profile [optimized + debuginfo] target(s) in 0.11s
/workspaces/wolfboot-fuzzer/LibAFL/fuzzers/full_system/qemu_riscv32/target/release/qemu_baremetal -icount shift=auto,align=off,sleep=off -machine sifive_e -monitor null -kernel /workspaces/wolfboot-fuzzer/LibAFL/fuzzers/full_system/qemu_riscv32/target/example.elf -drive if=none,format=qcow2,file=/workspaces/wolfboot-fuzzer/LibAFL/fuzzers/full_system/qemu_riscv32/target/dummy.qcow2 -serial null -nographic -snapshot -S
FUZZ_INPUT @ 0x80000000
main address = 0x20010306
Breakpoint address = 0x20010200
Devices = ["timer", "cpu_common", "cpu", "riscv_sifive_plic", "riscv_mtimer", "sifive_soc.gpio", "riscv.sifive.uart", "riscv.sifive.uart"]
[Objective   #1]  (GLOBAL) run time: 0h-0m-3s, clients: 1, corpus: 0, objectives: 1, executions: 0, exec/sec: 0.000
                  (CLIENT) corpus: 0, objectives: 1, executions: 0, exec/sec: 0.000
We imported 0 inputs from disk.

thread 'main' panicked at src/fuzzer_breakpoint.rs:217:14:
called `Result::unwrap()` on an `Err` value: Empty("No entries in corpus. This often implies the target is not properly instrumented.", ErrorBacktrace)
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
[Objective   #1]  (GLOBAL) run time: 0h-0m-6s, clients: 1, corpus: 0, objectives: 2, executions: 0, exec/sec: 0.000
                  (CLIENT) co

*[truncated]*

---

## #3042: [libafl-targets] Value profile guidance for strcmp/memcmp interceptor and friends

**Labels:** enhancement

Currently in libfuzzer, the hooks for strncmp, [`__sanitizer_weak_hook_strncmp`](https://github.com/llvm/llvm-project/blob/74df2032d467618a9aab085120539e306f21bcc0/compiler-rt/lib/fuzzer/FuzzerTracePC.cpp#L628-L639) calls into:

```c
fuzzer::TPC.AddValueForMemcmp(caller_pc, s1, s2, n, /*StopAtZero*/true);
```

and then `AddValueForMemcmp` in turn does [these two calls](https://github.com/llvm/llvm-project/blob/74df2032d467618a9aab085120539e306f21bcc0/compiler-rt/lib/fuzzer/FuzzerTracePC.cpp#L376-L377):

```c
  ValueProfileMap.AddValue(Idx);
  TORCW.Insert(Idx ^ Hash, Word(B1, Len), Word(B2, Len));
```

`TORCW` is the comparison logging mechanism but notice it also has `ValueProfileMap` guidance here.

(same code in [AFL++ here](https://github.com/AFLplusplus/AFLplusplus/blob/f590973387ee04d6c7ef016d5111313f9f4945b8/custom_mutators/libfuzzer/FuzzerTracePC.cpp#L432-L434))

---

In comparison, the hook for strncmp in `libafl-targets` does: https://github.com/AFLplusplus/LibAFL/blob/89342b22c2011f455566d1b5516177b9857dd3f2/libafl_targets/src/sancov_cmp.rs#L92

which in turn only adds the value to the cmplog map:

https://github.com/AFLplusplus/LibAFL/blob/89342b22c2011f455566d1b5516177b9857dd3f2/libafl_targets/src/cmplog.h#L190-L191


---

This prevents libafl-libfuzzer from being able to solve things like this little harness (full harness attached [harness.cpp.txt](https://github.com/user-attachments/files/19095581/harness.cpp.txt)):

```c
extern "C" int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size) {
    if (Size == 0) return 0;
    char* encoded = (char*) malloc(Size * 3);
    if (encoded == NULL) return 0;

    int b64_length = b64_encode((unsigned char*) Data, Size, (unsigned char*) encoded);
    // "Hello " in base64 so it's not visible to cmplog
    if (strncmp(encoded, "SGVsbG8g", 8) == 0) {
        // "World" in base64 so it's not visible to cmplog
        if (b64_length > 8 && strncmp(encoded + b64_length - 8, "V29ybGQ=", 8) == 0) {
            abort();
        }
    }

    free(encoded);
    return 0;
}
```

libfuzzer with value profiles can solve this rather easily because it breaks the strncmp into a brute-force of the base64 output:

```
$ time ./libfuzzer -use_value_profile=1
INFO: Running with entropic power schedule (0xFF, 100).
INFO: Seed: 3161432840
INFO: Loaded 1 modules   (16 inline 8-bit counters): 16 [0x55a96f6e0fe1, 0x55a96f6e0ff1),
INFO: Loaded 1 PC tables (16 PCs): 16 [0x55a96f6e0ff8,0x55a96f6e10f8),
INFO: -max_len is not provided; libFuzzer will not generate inputs larger than 4096 bytes
INFO: A corpus is not provided, starting from an empty corpus
#2      INITED cov: 7 ft: 24 corp: 1/1b exec/s: 0 rss: 26Mb
...
0x48,0x65,0x6c,0x6c,0x6f,0x20,0x57,0x6f,0x72,0x6c,0x64,
Hello World
artifact_prefix='./'; Test unit written to ./crash-0a4d55a8d778e5022fab701977c5d840bbc486d0
Base64: SGVsbG8gV29ybGQ=

real    0m20.850s
user    0m20.556s
sys     0m0.068s
...
```

but using libafl's libfuzzer shim for the same thing:
```
$

*[truncated]*

---

## #3010: Crash in libafl_maps_next when iterating over qemu.mapping

**Labels:** bug, qemu

**Describe the bug**
My fuzzer crash every time a `for map in qemu.mappings() {` is done (in Snapshot helper, QemuMappingsViewer or when I do it in my code) . Same when I run the `qemu_coverage` example on latest LibAFL commit  (it does `let mappings = QemuMappingsViewer::new(&qemu);`).

**To Reproduce**
Steps to reproduce the behavior:
1. Maybe this is related to my setup which affect the mapping ? But it is not that exotic: `Linux pct 6.1.0-30-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.124-1 (2025-01-12) x86_64 GNU/Linux`
2. Do `just run` on qemu_coverage example:

```
Thread 3.1 "qemu_coverage" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffff7aeb900 (LWP 81365)]
libafl_maps_next (pageflags_maps_node=0x55555600bc60, proc_maps_root=<optimized out>, ret=0x7fffffffae40) at ../linux-user/syscall.c:13826
13826           ret->offset = (target_ulong)e->offset;
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
────────────────────────────────────────────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]────────────────────────────────────────────────────────────────────────
 RAX  0x0
*RBX  0x7fffffffae40 ◂— 0xffffffffff600000
 RCX  0x0
*RDX  0x555555fe9298 (guest_base) ◂— 0x0
 RDI  0x0
 RSI  0x0
*R8   0x7ffff7d5cc60 (main_arena) ◂— 0x0
*R9   0x555556118ec0 ◂— 0x55500344e038
*R10  0xa0cb078db41b86e7
*R11  0x1d0
*R12  0xffffffffff600000
*R13  0xffffffffff601000
*R14  0x55555600bc60 —▸ 0x555556022880 —▸ 0x555556022611 ◂— 0x8000005555560225
*R15  0xffffffffff600fff
*RBP  0x4
*RSP  0x7fffffffada0 —▸ 0x555556111d10 —▸ 0x5555561199a0 ◂— 0x1
*RIP  0x555555763426 (libafl_maps_next+326) ◂— mov rcx, qword ptr [rax + 0x48]
─────────────────────────────────────────────────────────────────────────────────[ DISASM / x86-64 / set emulate on ]─────────────────────────────────────────────────────────────────────────────────
 ► 0x555555763426 <libafl_maps_next+326>    mov    rcx, qword ptr [rax + 0x48]
   0x55555576342a <libafl_maps_next+330>    mov    qword ptr [rbx + 0x10], rcx
   0x55555576342e <libafl_maps_next+334>    mov    rcx, qword ptr [rax + 0x50]
   0x555555763432 <libafl_maps_next+338>    mov    qword ptr [rbx + 0x18], rcx
   0x555555763436 <libafl_maps_next+342>    mov    dword ptr [rbx + 0x20], ebp
   0x555555763439 <libafl_maps_next+345>    movzx  eax, byte ptr [rax + 0x33]
   0x55555576343d <libafl_maps_next+349>    mov    dword ptr [rbx + 0x24], eax
   0x555555763440 <libafl_maps_next+352>    mov    rdi, r14
   0x555555763443 <libafl_maps_next+355>    xor    esi, esi
   0x555555763445 <libafl_maps_next+357>    mov    rdx, 0xffffffffffffffff
   0x55555576344c <libafl_maps_next+364>    add    rsp, 8
──────────────────────────────────────────────────────────────────────────────────────────[ SOURCE (CODE) ]───────────────────────────────────────────────────────────────────────────────────────────
In file: /home/celian/Downloads/experimentation/last_LibAFl/LibAFL/fuzzers/binary_only/qemu_coverage/target/re

*[truncated]*

---

## #2944: Crossover mutators currently don't work with nested MappingMutators

**Labels:** enhancement

One may want to use two (or more) nested `MappingMutator`s, one to map from a complex input type to a primitive that can be mutated by built-in mutators such as `havoc_mutations`, and one to map from a composite input type (such as a list of the complex input type, which would e.g. be a list of network packets) to the complex input type.

This limitation is because one can only pass a single mapper to the mutator which extracts the data to be injected from the corpus. In the future, this mapping should be done in `MappingMutator` as well (maybe an alternate crossover version). However, for crossover the dependency between the different stages of `MappingMutator`s is the reverse to the mapping of the current input. This makes it somewhat tricky.

I have at some point toyed around with an implementation which would create a new `CrossoverMutator` trait, which has a default `Mutator` implementation and just maps the current input and the crossover input and passes those two to the default impl for the actual mutation. With this approach, for the crossover mapping, one needs to create closures at each level of mapping, each owning the next-lower crossover mapper. I've not managed to get past lifetime limitations because the default impl needs to receive both a mut reference to state (because certain mutators need a source of randomness), and a reference to the input, which depends on state as well, so the borrow checker complained.

I may give it another go at some point, for now I just wanted to document this limitation. If anyone wants to work on this though, please do!

---

## #2922: undefined symbols for fuzzer binary_only/frida_libpng

**Labels:** bug, macos

When compiling fuzzers/binary_only/frida_libpng I get `undefined symbols`, see below.

```
$ sw_vers 
ProductName:		macOS
ProductVersion:		15.3
BuildVersion:		24D60

$ rustc --version
rustc 1.84.0 (9fc6b4312 2025-01-07) (Homebrew)

$ cd fuzzers/binary_only/frida_libpng

$ cargo run
....
          Undefined symbols for architecture arm64:
            "__frida_g_get_current_dir", referenced from:
                frida_gum::process::Process::current_dir::h7ab5639f21cbba14 in libfrida_gum-65f16446e27b8f25.rlib[5](https://github.com/AFLplusplus/LibAFL/frida_gum-65f16446e27b8f25.frida_gum.a96db2485db9796c-cgu.2.rcgu.o)
            "__frida_g_get_home_dir", referenced from:
                frida_gum::process::Process::home_dir::h058beb1f826552f2 in libfrida_gum-65f16446e27b8f25.rlib[5](https://github.com/AFLplusplus/LibAFL/frida_gum-65f16446e27b8f25.frida_gum.a96db2485db9796c-cgu.2.rcgu.o)
            "__frida_g_get_tmp_dir", referenced from:
                frida_gum::process::Process::tmp_dir::h611516336a6bc0c9 in libfrida_gum-65f16446e27b8f25.rlib[5](https://github.com/AFLplusplus/LibAFL/frida_gum-65f16446e27b8f25.frida_gum.a96db2485db9796c-cgu.2.rcgu.o)
            "_gum_linux_parse_ucontext", referenced from:
                frida_gum::backtracer::Backtracer::accurate_with_signal_context::h79e9b1780c65ca38 in libfrida_gum-65f16446e27b8f25.rlib[6](https://github.com/AFLplusplus/LibAFL/frida_gum-65f16446e27b8f25.frida_gum.a96db2485db9796c-cgu.3.rcgu.o)
                frida_gum::backtracer::Backtracer::fuzzy_with_signal_context::h17b4e5c9b22bb179 in libfrida_gum-65f16446e27b8f25.rlib[6](https://github.com/AFLplusplus/LibAFL/frida_gum-65f16446e27b8f25.frida_gum.a96db2485db9796c-cgu.3.rcgu.o)
          ld: symbol(s) not found for architecture arm64
          clang: error: linker command failed with exit code 1 (use -v to see invocation)

error: could not compile `frida_fuzzer` (bin "frida_fuzzer") due to 1 previous error

```

---

## #2880: Rewrite InProcessExecutors

- We should use builder pattern instead of current constructors that has 90% same code
- Redesign crash, timeout hooks.

---

## #2877: OnDiskCorpus actually only evicts the input from memory, not the entire Testcase

**Labels:** bug

From the docs of `OnDiskCorpus`:
https://github.com/AFLplusplus/LibAFL/blob/2842f95e2aa4e0c665df3c99f1e46a5f4db52fbd/libafl/src/corpus/ondisk.rs#L1-L6

`OnDiskCorpus` uses `CachedOnDiskCorpus` under the hood:
https://github.com/AFLplusplus/LibAFL/blob/2842f95e2aa4e0c665df3c99f1e46a5f4db52fbd/libafl/src/corpus/cached.rs#L1

However, both these docs are wrong: `CachedOnDiskCorpus` only ever evicts the actual input from memory, the rest of the Testcase is kept in memory, including all metadata.

We should either implement what the docs say (not sure about the performance implications though), or at least fix the docs.

(Disclaimer: I'm only about 95% sure.)

---

## #2809: `ShMem` should probably require stored values to be `Sync`

**Labels:** bug

`ShMem` can be used to create data-races if you use it to store non-`Sync` types such as `Cell`. For example, the assertion at the end of the following program fails:
```rust
use std::cell::Cell;

use libafl_bolts::os::{fork, ForkResult};
use libafl_bolts::shmem::{ShMem, ShMemProvider as _};

fn do_stuff(shmem: &impl ShMem) {
    let p = shmem.as_ptr_of::<Cell<usize>>().unwrap();
    for i in 0..128 {
        let val = unsafe { (*p).get() };
        println!("val = {val}");
        unsafe { (*p).set(val + 1) };
    }
}

fn main() {
    let mut shmem_provider = libafl_bolts::shmem::MmapShMemProvider::default();
    let shmem = shmem_provider.new_on_shmem(Cell::new(0usize)).unwrap();
    shmem_provider.pre_fork().unwrap();
    match unsafe { fork() }.unwrap() {
        ForkResult::Parent(handle) => {
            shmem_provider.post_fork(false).unwrap();
            do_stuff(&shmem);
            handle.status();
        }
        ForkResult::Child => {
            shmem_provider.post_fork(true).unwrap();
            do_stuff(&shmem);
            std::process::abort();
        }
    }
    let p = shmem.as_ptr_of::<Cell<usize>>().unwrap();
    assert_eq!(256, unsafe { (*p).get() });
}
```
Of course, you can *also* create data-races just by using `as_mut_ptr`... But fixing that would require a whole different design, whereas it would be pretty easy to add a `Sync` bound to `ShMemProvider::new_on_shmem`, `ShMem::as_ptr_of`, etc..

---

## #2808: `ShMem` is easy to misuse

**Labels:** enhancement

Consider the following program:
```rust
use libafl_bolts::shmem::{ShMem as _, ShMemProvider as _};

fn main() {
    let mut prov = libafl_bolts::shmem::MmapShMemProvider::default();
    let shmem = prov.new_on_shmem([0x01u8; 256]).unwrap();
    let v_ptr = shmem.as_ptr_of::<Vec<u8>>().unwrap();
    let v = unsafe { (*v_ptr).clone() };
    println!("{}", v[5]);
}
```
This results in an assertion failure in `std` (though it could easily also result in a segfault, depending on your machine):
```
cargo -q run -r

memory allocation of 72340172838076673 bytes failed
zsh: abort (core dumped)  cargo -q run -r
```
The problem is that the type passed to `ShMem::as_ptr_of` is different from that passed to `ShMemProvider::new_on_shmem`. In this trivial example, this is easy to see, but one can certainly imagine a larger program where the construction- and use-sites are further away and drift out of sync.

You might say that this isn't that big of a deal, because it requires dereferencing a raw pointer, which is `unsafe`. In particular, doing so requires you to ensure that there is a valid value of the pointer's type at that address. I would argue that this interface is unnecessarily flexible, and makes it too easy to do the wrong thing without realizing it.

One easy enhancement would be to add a typed wrapper around `ShMem`:
```rust
pub trait ShMemProvider {
    fn new_on_shmem<T: Sized + 'static>(&mut self, value: T) -> Result<TypedShMem<Self::ShMem, T>, Error>;
}

pub struct TypedShMem<S: ShMem, T: Sized + 'static> {
    inner: S,
    phantom: PhantomData<T>
}

impl<S: ShMem, T: Sized + 'static> TypedShMem<S, T> {
    pub fn into_inner(self) -> S {  self.inner  }
    pub fn as_ptr(&self) -> *const T {  self.inner.as_ptr_of::<T>().unwrap() }
    pub fn as_mut_ptr(&mut self) -> *mut T { self.inner.as_mut_ptr_of::<T>().unwrap()  }
}
```
(I would advocate against `impl DerefMut<Target = T> for TypedShMem<S, T>` due to #2807.) This retains all of the flexibility of the current approach, while making it easier for the type system to nudge users in the right direction.

This is just a suggestion, feel free to close if you disagree with my reasoning!

---

## #2807: `ShMem` should not give out references, pt. 2

**Labels:** bug

You can recreate #1748 with [the `impl DerefMut<Target = [u8]>` for `MmapShMem`](https://docs.rs/libafl_bolts/0.14.1/libafl_bolts/shmem/unix_shmem/struct.MmapShMem.html#impl-DerefMut-for-MmapShMem).
```rust
// cargo init
// cargo add --no-default-features --features=std --git https://github.com/AFLplusplus/LibAFL libafl_bolts
// cargo run

use std::ops::{DerefMut as _};
use libafl_bolts::shmem::{ShMemProvider as _};

pub fn main() {
    let mut prov = libafl_bolts::shmem::MmapShMemProvider::default();
    let mut shmem1 = unsafe { prov.new_on_shmem::<u8>(0).unwrap_unchecked() };
    let mut shmem2 = unsafe { prov.clone_ref(&shmem1).unwrap_unchecked() };
    let r1 = &mut shmem1.deref_mut()[0];
    let r2 = &mut shmem2.deref_mut()[0];
    go(r1, r2);
}

pub fn go(r1: &mut u8, r2: &mut u8) {
    mut_r1(r1);
    mut_r2(r2);
    if *r1 == 1 {
        println!("r1 = {r1}");
    }
}

pub fn mut_r1(r1: &mut u8) {
    *r1 = 1;
}

pub fn mut_r2(r2: &mut u8) {
    *r2 = 32;
}
```
Prints
```
r1 = 32
```

---

## #2798: Trying to write an HTTP fuzzer

**Labels:** question

Wasnt't sure if there was a forum to post questions, so I figured I'd ask here. As the title says, I'm trying to write an HTTP fuzzer for practice, but right now I'm kind of stuck at how to link things together. I'm writing an HTTPFeedback that holds a set of HTTP codes, and the idea is that in its `is_interesting` function, it will see if the HTTP status code is in its set, and return a value based on that. The only problem is, how do I communicate the returned HTTP status code to the feedback? Would I do that through the ExitKind or state or something else?

Thanks if you're able to help out, and if this isn't the right place to ask, I'd be more than happy to repost my question somewhere else.

---

## #2786: Unify and Fix Pseudo-Coverage in Example Fuzzers

**Labels:** bug

`static_mut_refs` are going to break soon. This needs fixing. See discussion [here](https://github.com/AFLplusplus/LibAFL/pull/2784#discussion_r1893727318) and [here](https://github.com/AFLplusplus/LibAFL/pull/2770#discussion_r1885707774).

Additionally, handling of the pseudo-coverage is different between example fuzzers. The names, the extraction of necessary data from the static array, and the way the data is passed to the observers should be unified.

---

## #2765: Document more clearly that EmulatorHooks.post_exec get called at the end of the harness

**Labels:** enhancement, qemu

**Is your feature request related to a problem? Please describe.**
I just wasted multiple days trying to figure out why my fuzzer, that I based on [qemu_baremetal/low_level](https://github.com/AFLplusplus/LibAFL/blob/main/fuzzers/full_system/qemu_baremetal/src/fuzzer_breakpoint.rs), reported incorrect values for a memory location that I read from my custom module in the `post_exec` step.

This was due to the fact that the snapshot had already been restored and the memory reset to its original value
https://github.com/AFLplusplus/LibAFL/blob/be21fae4909018c2a7dfdc496d70c33a237f6a54/fuzzers/full_system/qemu_baremetal/src/fuzzer_low_level.rs#L192


**Describe the solution you'd like**
Maybe change the post_exec name to post_harness? Also to differentiate against observers?

**Describe alternatives you've considered**
Update the comment to state that the hooks run after the harness

**Additional context**

What would be the correct way to read a chunk of memory after this line has returned?
https://github.com/AFLplusplus/LibAFL/blob/be21fae4909018c2a7dfdc496d70c33a237f6a54/fuzzers/full_system/qemu_baremetal/src/fuzzer_low_level.rs#L160

I can't do it in an observer, because observers need to be serializable, so I can't add a `Qemu` struct to it.
I'm currently storing the return value of `emulator.qemu().run()` in a local var, reading the memory and then match of the stored value but that feels very hacky.

---

## #2758: Derive Named

**Labels:** enhancement

A lot of structs within LibAFL implement `Named`. And all of those are done manually, leading to a lot of code duplication. Would it make sense to create a derive macro that implements it based on the struct name?

Is there a reason this doesn't exist already?

---

## #2746: libafl-qemu: multiple consecutive `load_snapshot` calls cause segmentation fault

**Labels:** bug, qemu

Like @langston-barrett in #2628, I'm trying to fuzz an EDKII image while using snapshots. I'm running into an issue where restoring a snapshot twice in a row, without starting/restarting QEMU in between those restorations, will reliably cause a segmentation fault once QEMU restarts. (Also like Langston, I can't share the compiled artifacts used here, but I strongly suspect the issue is independent of them, and should be replicable with another systemmode target.) Consider this example:
```rs
// cargo init
// cargo add --no-default-features --features=systemmode --git https://github.com/AFLplusplus/LibAFL libafl_qemu
// cargo run

use std::error;

const QEMU_FLAGS: &[&str] = &[
    "-machine",
    "q35",
    "-kernel",
    "./impl/bzImage",
    "-append",
    "'rootwait root=/dev/vda console=tty1 console=ttyS0 keep_bootcon'",
    "-drive",
    "file=./impl/rootfs.ext2,if=virtio,format=raw,readonly=on",
    "-global",
    "driver=cfi.pflash01,property=secure,value=on",
    "-drive",
    "if=pflash,format=raw,unit=1,file=./impl/OVMF_VARS.fd",
    "-drive",
    "if=pflash,format=raw,unit=0,readonly=on,file=./impl/OVMF_CODE.fd",
    "-smp",
    "2",
    "-m",
    "4G",
    "-bios",
    "./impl/OVMF.fd",
    "-snapshot",
    "-S",
    "-nodefaults",
];

const SNAPSHOT_NAME: &'static str = "snapshot";
const SYNC: bool = true;

fn main() -> Result<(), Box<dyn error::Error>> {
    let mut args = vec!["qemu".to_owned()];
    args.extend(QEMU_FLAGS.iter().map(|s| (*s).to_owned()));
    let qemu = libafl_qemu::Qemu::init(args.as_slice())?;

    let entry = 0x7FFA3C01;

    println!("Saving snapshot...");
    qemu.save_snapshot(SNAPSHOT_NAME, SYNC);

    println!("Loading snapshot...");
    qemu.load_snapshot(SNAPSHOT_NAME, SYNC);

    // println!("Loading snapshot again...");
    // qemu.load_snapshot(SNAPSHOT_NAME, SYNC);

    println!("Running to {entry:#x}...");
    qemu.entry_break(entry);
    println!("...finished.");

    Ok(())
}
```

Without the second `load_snapshot`, I see this run to completion. With the second `load_snapshot`, I get a segmentation fault when QEMU restarts:
```
rom: file kvmvapic.bin        : error Failed to open file “kvmvapic.bin”: No such file or directory
rom: file linuxboot_dma.bin   : error Failed to open file “linuxboot_dma.bin”: No such file or directory
Saving snapshot...
Loading snapshot...
Loading snapshot again...
Running to 0x7ffa3c01...
Segmentation fault (core dumped)
```

Here's a backtrace:
```
Saving snapshot...
Loading snapshot...
Loading snapshot again...
Running to 0x7ffa3c01...

Thread 1 "scratch" received signal SIGSEGV, Segmentation fault.
0x00005555571c68c0 in ?? ()
(gdb) bt
#0  0x00005555571c68c0 in ?? ()
#1  0x0000555555a6e604 in vm_state_notify (running=running@entry=true, state=state@entry=RUN_STATE_RUNNING) at ../system/runstate.c:399
#2  0x0000555555a64fca in vm_prepare_start (step_pending=step_pending@entry=false) at

*[truncated]*

---

## #2720: Count Executions With Same Observer Value

**Labels:** enhancement

**Is your feature request related to a problem? Please describe.**
I have a target that is unstable, i.e. for the same input I don't always get the same observation.

**Describe the solution you'd like**
I would like to have a way to count how often a certain `Observer` observes the same value to get a frequency distribution and figure out how bad things are. This could be implemented in three levels:
1. A pure count of how often each observed value is measured — this would only really be useful with a single corpus entry and a `NopMutator`, but maybe a good start.
2. A count of how often each value is measured, along with an example input that triggers this execution
3. A count of how often each value is measured, along with a list of all inputs that triggered this execution — this would be really inefficient, but maybe useful for debugging.

**Describe alternatives you've considered**
Right now, in a very hacky way, I just hash the observer value in the executor and append that hash to a file. It also gets put in some metadata in the corpus, so I can correlate them after the fact. This is wildly inefficient. And I'm using the single corpus entry/`NopMutator` strategy.

I've also attempted to implement this as a feedback that updates a count field in some metadata entry on each `is_interesting` call, but I could not get those updated metadata values to be written to disk. It's also a bit hacky, because in `is_interesting`, I only have the input, and not the testcase, so I have to manually extract that from state -> corpus -> testcase. If this were to work, it would basically provide solution 2. But I'm not sure it's possible, I don't know the internals well enough.

Lastly, one could write a feedback that keeps an internal representation of input-outcome values (e.g. `HashMap` with the `Observer` value as the key and a tuple of `(count, example_input)` as the value, to get solution level 2. These values could then be written to disk at a certain interval, similar to `OnDiskTomlMonitor`.

**Additional context**
I'm just curious if anyone has an opinion on how this could be done in a pretty way.

---
