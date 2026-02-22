# the issue tracker

**Parent:** Neovim — Project Ideas
**Source:** https://github.com/neovim/neovim/issues
**Scraped:** 2026-02-22T23:28:47.616301

---

## #38021: Bracketed paste under tmux is contaminated with extended keys

### Problem

Bracketed paste into neovim under tmux contains misrepresented ctrl-j (ASCII LF) values. This happens no matter if `set -s extended-keys on` or `off` (as neovim requests extended-keys and tmux honors it regardless), and the representation changes depending on if I use `set -s extended-keys-format xterm` or `csi-u` (`[27;5;106~` and `[106;5u` respectively).

This has been reported more than once on the tmux side (et al: https://github.com/tmux/tmux/issues/4663), yet all closed seemingly without resolution.

I have not been able to reproduce it outside of tmux.

### Steps to reproduce

Use tmux inside of:
* Alacritty
* Wezterm
* Kitty

Do not use:
* Microsoft Terminal (doesn't seem to implement any form of extended keys yet?)

### Expected behavior

Bracketed pastes with newlines having newlines instead of ctrl-j representations.

### Nvim version (nvim -v)

0.11.6

### Vim (not Nvim) behaves the same?

vim has different bracketed paste behavior

### Operating system/version

Any/all

### Terminal name/version

Multiple

### $TERM environment variable

Multiple

### Installation

appimage

---

## #38014: Hang if PTY process exits after spawning detached child that keeps writing output

**Labels:** job-control, channels-rpc, bug-regression

### Problem

Hang if PTY process exits after spawning detached child that keeps writing output.
Regression from #37325.

### Steps to reproduce

1. Compile the following C program into an executable `./a.out`:
```c
#include <stdio.h>
#include <unistd.h>

int main() {
  if (fork() == 0) {
    setsid();
    for (;;) {
      printf("foobar\n");
    }
  } else {
    usleep(1000);
  }
  return 0;
}
```
2. Run `nvim --clean`
3. Run `:call jobstart(['./a.out'], {'term': v:true}`
4. Nvim hangs and doesn't respond to any input

Theoretically this can happen with `'pty': v:true` as well, but when I test this it only happens with `'term': v:true`.

### Expected behavior

No hang. There are three possible solutions:
1. Restore the remaining data size limit, but use a larger limit on Linux. See #38011.
2. Allow interrupting the loop in `flush_stream()` with Ctrl-C.
3. Don't drain PTY master after the direct child exits. Instead, keep the terminal channel open until EOF on PTY master (i.e. all children have exited).

It seems that some terminal emulators (e.g. kitty) do wait for all processes in the PTY to exit (e.g. after `:detach` in Nvim, kitty doesn't exit until the server is also stopped), while some other terminal emulators don't. This is also mentioned in tui_spec.lua:

https://github.com/neovim/neovim/blob/94c21c22dcf6b1afdb25a250c08bd858d481429b/test/functional/terminal/tui_spec.lua#L205-L209

Making Nvim's builtin terminal do this can be a bit hard and can potentially break plugins, as it's not clear how this should interact with `on_exit` and `jobwait()` etc..

### Nvim version (nvim -v)

v0.12.0-dev-2379+g524164ae05

### Vim (not Nvim) behaves the same?

Yes, Vim 9.0.38 also hangs with `:call term_start(['./a.out'])`

### Operating system/version

Arch Linux

### Terminal name/version

kitty 0.45.0

### $TERM environment variable

xterm-kitty

### Installation

Arch User Respository (AUR)

---

## #38008: ui2: statusline is covered when `laststatus=3`

**Labels:** bug-regression, has:bisected, ui2

### Problem

https://github.com/neovim/neovim/issues/36420 no longer happens.

### Steps to reproduce

- `nvim --clean`
- `:lua require('vim._core.ui2').enable {}`
- `:set laststatus=3`
- `:hi`
- `g<`

Issue bisected to [16495e686371d45f02eafff5aa3216ca15d5f735](https://github.com/neovim/neovim/commit/16495e686371d45f02eafff5aa3216ca15d5f735) (#37905)

---

## #37994: ui2: messages.lua:310: Invalid 'end_col': out of range

**Labels:** ui2

## Problem

Describe the problem (concisely).

## Steps to reproduce

cd `/path/to/neovim`
```
nvim --clean --cmd "lua require('vim._core.ui2').enable({})" src/nvim/main.c +'map <space> <Cmd>Inspect<CR>'
```
Then type `<space><space>`:
```
Error in "msg_show" UI event handler (ns=nvim.ui2):                                                 
Lua: runtime/lua/vim/_core/ui2/messages.lua:310: Invalid 'end_col': out of range
```

## Expected behavior
No error.

## System info

- Nvim version (nvim -v): `v0.12.0-dev-2377 gd79a9dcd42` neovim/neovim@d79a9dcd42
- Vim (not Nvim) behaves the same?: ?
- Operating system/version: Linux 6.18.9-zen1-2-zen
- Terminal name/version: kitty
- $TERM environment variable: `xterm-kitty`
- Installation: ?

---

## #37989: buffer-updates: on_bytes args of nvim_buf_attach are different when using `o` and `A<Enter>`

**Labels:** events, editor-state

### Problem

Hey there I'm sorry if i am doing this wrong. 

I stole the title from #25966, because it's the same issue but #25966 is closed and wasn't reopend after someone commented that the issue still persists.


Using `o`, the args passed to `on_bytes` of `nvim_buf_attach` is different from when using `A<Enter>`


### Steps to reproduce


blatently stolen from the before issue #25966 by [lucario387](https://github.com/lucario387):

reproduce the bug using 
```lua
-- test.lua
vim.api.nvim_create_autocmd("BufEnter", {
  callback = function(args)
    vim.api.nvim_buf_attach(args.buf, true, {
      on_bytes = function(_, _, _, start_row, start_col, byte_offset, old_end_row, _, _, new_end_row, new_col, _)
        --print(start_row, old_end_row, new_end_row)
        print(start_row, start_col, byte_offset, old_end_row, new_end_row, new_col)
      end
    })
  end
})
```

- `nvim --clean -u test.lua test.foo` and do `o`. We get `1 0 1 0 1 0`
- `nvim --clean -u test.lua test.foo` and do `A<Enter>`. We get `0 0 0 0 1 0`


I also found additional stuff but am not so clear on how to document it. This is one case:
- `nvim --clean -u test.lua test.foo` and do `i`, `1234`, `ESC`, `V`, `d` an then `p`. We get `1 0 1 0 1 0`. Shuldn't this also be `0 0 0 ? ? 4`. Because we insert a newline, and on the new line 4 characters so new_col should be 4

another case should be when you `V` then `y` for lines and then `V` the last 6 lines and `p`.


For me this issues came up when I did stuff on the last line of the buffer.



### Expected behavior

`o` and `A<Enter>` should both produce `0 0 0 0 1 0`.




### Nvim version (nvim -v)

NVIM v0.11.6     Build type: Release    LuaJIT 2.1.1741730670

### Vim (not Nvim) behaves the same?

unsure

### Operating system/version

arch linux 6.18.4-arch1-1 x86_64 GNU/Linux

### Terminal name/version

st 0.9.2 (suckless)

### $TERM environment variable

st-256color

### Installation

system package manager (archlinux)  and from github release page

---

## #37982: PTY output may still be dropped after process exit on Linux

**Labels:** job-control, terminal, channels-rpc, platform:linux

### Problem

On Linux, the following check in `flush_stream()` isn't sufficient to ensure that all PTY output is received:

https://github.com/neovim/neovim/blob/94c21c22dcf6b1afdb25a250c08bd858d481429b/src/nvim/event/proc.c#L394-L404

It seems that even if `poll()` doesn't return any events after process exit, PTY master can still have more output. This problem is present both with and without #37401.

### Steps to reproduce

Since #37918 this started happening occasionally on Linux CI jobs other than ASAN/TSAN. Example test failure:
```
FAILED   test/functional/terminal/tui_spec.lua @ 2552: TUI no assert failure on deadly signal #21896
test/functional/terminal/tui_spec.lua:2554: Row 1 did not match.
Expected:
  |*Nvim: Caught deadly signal 'SIGTERM'              |
  |*                                                  |
  |*[Process exited 1]^                                |
  |                                                  |
  |                                                  |
  |                                                  |
  |{5:-- TERMINAL --}                                    |
Actual:
  |*                                                  |
  |*[Process exited 1]^                                |
  |*                                                  |
  |                                                  |
  |                                                  |
  |                                                  |
  |{5:-- TERMINAL --}                                    |
```
There are also several other test that may fail due to this.

### Expected behavior

Full PTY output should be received by the terminal buffer.

It seems that the proper way to detect PTY master EOF on Linux is to call `read()` and check if `errno` is `EIO`.

However, then there is another problem that if there is another program running in the PTY, EOF only happens on PTY master when that process exits as well.

It seems that some terminal emulators (e.g. kitty) do wait for all processes in the PTY to exit (e.g. after `:detach` in Nvim, kitty doesn't exit until the server is also stopped), while some other terminal emulators don't. This is also mentioned in tui_spec.lua:

https://github.com/neovim/neovim/blob/94c21c22dcf6b1afdb25a250c08bd858d481429b/test/functional/terminal/tui_spec.lua#L205-L209

Making Nvim's builtin terminal do this can be a bit hard and can potentially break plugins, as it's not clear how this should interact with `on_exit` and `jobwait()` etc..

### Nvim version (nvim -v)

v0.12.0-dev-2374+g94c21c22dc

### Vim (not Nvim) behaves the same?

Cannot verify as issue is hard to reproduce locally

### Operating system/version

GitHub Actions Ubuntu 24.04

### Terminal name/version

N/A

### $TERM environment variable

N/A

### Installation

N/A

---

## #37944: :detach, :restart are broken on Windows

**Labels:** platform:windows, channels-rpc, lifecycle, remote

### Problem

We have `chan.detach` internal feature which allows the TUI channel to close without triggering the server to self-close: https://github.com/neovim/neovim/blob/6e1745e96e3d74ee7958904b81a3f8ebfe404184/src/nvim/channel.h#L34-L36

However, this is not working on Windows:

https://github.com/neovim/neovim/blob/6bb6b479332727852052baa6c1ea0801e776895e/test/functional/terminal/tui_spec.lua#L119-L126

This also [affects `:restart`](https://github.com/neovim/neovim/pull/35223#issuecomment-3920230868).

### Expected behavior

make it so

---

## #37936: lsp: push and pull diagnostics override each other

**Labels:** bug-regression, lsp, has:bisected

### Problem

Pull diagnostics (from `textDocument/diagnostic`) and push diagnostics (from `textDocument/publishDiagnostics`) use the same namespace, which is a problem when using language servers that publish two different sets of diagnostics on push vs pull, like rust-analyzer (see https://github.com/rust-lang/rust-analyzer/issues/18709#issuecomment-2551394047).

A `git bisect` pointed to https://github.com/neovim/neovim/pull/37221 as the first offending commit.

### Steps to reproduce

- `cargo new --lib repro && cd repro`
- create this `repro.lua`:

```lua
vim.lsp.config("rust_analyzer", {
  cmd = { "rust-analyzer" },
  root_markers = { "Cargo.toml", ".git" },
})

vim.lsp.enable("rust_analyzer")
```
- `printf 'fn foo() {}\n' > ./src/lib.rs`
- `nvim -u repro.lua ./src/lib.rs`
- ‼️ the diagnostic is shown, then immediately removed:

https://github.com/user-attachments/assets/3a4bc8ab-05c1-4df9-8351-aa144620420e


### Expected behavior

The diagnostic is not removed.

### Nvim version (nvim -v)

NVIM v0.12.0-nightly+29a46a1

### Vim (not Nvim) behaves the same?

N/A

### Operating system/version

macOS 10.15

### Terminal name/version

N/A

### $TERM environment variable

N/A

### Installation

Nix flake

---

## #37931: ui2: paste spinner "..." displays as multiline message

**Labels:** clipboard, has:plan, messages, ui2

### Problem

When pasting a big string, the internal paste handler prints a "spinner" or "throbber" that cycles through `.`, `..`, `...` to indicate activity.

With ui2 enabled, the throbber items are shown as a multiline message:

<img width="132" height="101" alt="Image" src="https://github.com/user-attachments/assets/6c9ce9b3-6cdb-41c8-a8c2-a4a2a254fdaa" />

### Steps to reproduce

1. enable ui2: 
   ```lua
   vim.o.cmdheight = 0
   require('vim._core.ui2').enable({msg={target='cmd'}})
   ```
1. copy a big string into OS clipboard, e.g. any CI build log.
1. paste it into a new buffer using OS paste (bracketed paste)

### Expected behavior

These messages are ephemeral and shouldn't be stacked. When the paste is done they shouldn't be shown at all.

---

## #37922: vim.system():wait() may return `nil`

**Labels:** job-control, event-loop, lua

### Problem

`vim.system():wait()` may return `nil` if `timeout` is exceeded during the sigkill : https://github.com/neovim/neovim/blob/73c4472d4a0addec9e52a0e379b3cb0651baf690/runtime/lua/vim/_core/system.lua#L144-L147

Example seen during CI test which makes a `git` call. Presumably the sigkill didn't finish fast enough (or there is a deeper event-loop or `vim.wait` bug?):

```
ERROR    test/functional/plugin/health_spec.lua @ 35: :checkhealth detects invalid 
...
- ❌ ERROR Failed to run healthcheck for "vim.health" plugin. Exception:
  ...ner/work/neovim/neovim/runtime/lua/vim/health/health.lua:543: attempt to index local 'result' (a nil value)

stack traceback:
	test/testutil.lua:140: in function 'matches'
	test/functional/plugin/health_spec.lua:40: in function <test/functional/plugin/health_spec.lua:35>
```

### Expected behavior

Should we change the return type to indicate this, or return a dummy `result` with e.g. `result.code = -1` ?

cc @lewis6991

---

## #37892: linematch degrades inline:char diff precision

**Labels:** diff

## Problem

`linematch` degrades `inline:char` (and `inline:word`) precision by splitting multi-line diff blocks into separate per-line hunks before the inline diff runs. This prevents the inline diff from cross-matching text across lines within the same hunk.

This interaction was noted in the commit message of PR #33086 (_“This doesn’t interact with linematch perfectly currently”_), but no issue exists to track it. It’s also surfacing in practice as a compatibility issue — see [this comment on #22696](https://github.com/neovim/neovim/issues/22696#issuecomment-2796819324), where a user resorts to `set diffopt-=linematch:40` to work around linematch-related problems in `nvimdiff`.

## Steps to reproduce

Create two files that differ by a line change + a line addition, with no unchanged separator between them:

**left.txt:**
```
Shared 1
The term being defined with role="term", using [`aria-labelledby`](https://github.com/path/to/aria-labelledby).
$
```

**right.txt:**
```
Shared 1
The term being defined with role="term".
CRThe contents; the [`aria-braillelabel`](https://github.com/neovim/neovim/url1), [`aria-label`](https://github.com/neovim/neovim/url2), and [`aria-labelledby`](https://github.com/path/to/aria-labelledby). properties are prohibited.
$
```

Then diff them with and without `linematch`.

## Expected behavior

With `inline:char` enabled, the inline diff should highlight only `, using` as the changed text on the left side — regardless of whether `linematch` is enabled.

The text `[\`aria-labelledby\`](https://github.com/path/to/aria-labelledby)` appears on both the left (line 2) and right (line 3). The inline diff should match these across lines, showing only the true difference.

## Actual behavior

- **Without `linematch`**: All three changed lines (L2, R2, R3) form one diff block. `inline:char` cross-matches `aria-labelledby` across L2 and R3, correctly highlighting only `, using` (7 chars) as `DiffText`.

- **With `linematch`**: The hunk is split so that the inline diff cannot cross-match across lines. The result is 42 chars of `DiffText` instead of 7.

## Minimal reproduction script

```lua
-- Save as /tmp/repro.lua, run: nvim --headless -u NONE -c "luafile /tmp/repro.lua"
vim.o.columns = 200
vim.o.lines = 30

local shared = {}
for i = 1, 10 do shared[i] = "Shared line " .. i end

local left = vim.list_extend(vim.list_extend({}, shared), {
  'The term being defined with role="term", using [`aria-labelledby`](https://github.com/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-labelledby).',
  "$",
})
local right = vim.list_extend(vim.list_extend({}, shared), {
  'The term being defined with role="term".',
  'CRThe contents; the [`aria-braillelabel`](https://github.com/neovim/neovim/url1), [`aria-label`](https://github.com/neovim/neovim/url2), and [`aria-labelledby`](https://github.com/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-labelledby). properties are prohibited.',
  "$",
})

local function test(label, diffopt_val)
  vim.cmd("silent! only | enew")
  vim.o.diffopt = diffopt_val
  local rb = vim.api.nvim_create_buf(false, true)
  vim.cmd("noautocmd buffer " .. rb)
  vim.api.nvim_buf_set_lines(rb, 0, -1, false, right)
  

*[truncated]*

---

## #37887: lsp: unexpected LSP behavior on Nvim exit when `exit_timeout=false`

**Labels:** documentation, lsp

## Problem

`client.exit_timeout = false` signals for Nvim to wait forever for a language server to exit (and never force exit the server). However, during Nvim exit, Nvim will ignore this option and force stop the language server anyway. This is intentional behavior as to prevent Nvim from seeming to "freeze" when it is actually the language server's fault (https://github.com/neovim/neovim/issues/36752#issuecomment-3596017419). As of #37597, this inconsistency only occurs when `exit_timeout` is `false`; when it is a number, it now behaves as expected in all situations.

See #36752 for previous.

## Possible Solutions

After thinking this over, I have come up with three possibly solutions.

### Fully respect `exit_timeout = false`

Nvim will wait to exit until all language servers have exited, waiting as long as needed. Since #37597 has been merged, Nvim will display an informative message if the server takes an abnormal time to exit. This will avoid the "Nvim seems frozen" effect, which was why this wasn't done to begin with.

This is my preferred fix.

Pros:
- Fully consistent with `exit_timeout = false` in all other contexts, making this the most intuitive option.
- Fully avoids force stopping a language server, which can lead to file corruption (https://github.com/neovim/neovim/pull/36783#issuecomment-3603340968).
- Problems with bugged language servers are visible instead of being masked by Nvim.
- Consistent behavior with what happens when `exit_timeout` is a number. In fact, `false` and `math.huge` become fully identical.

Cons:
- User needs to hit `^C` to close Nvim if a language server hangs forever.

### Fork off all non-stopped language servers on exit

Nvim will daemonize any language servers that fail to exit, allowing them to take as long as they need to exit without preventing Nvim itself from exiting.

Pros:
- While it is an exception to the `exit_timeout` behavior, `exit_timeout = false` will still never force stop a language server (no file corruption).
- Does not delay Nvim's shutdown.

Cons:
- Frozen language servers will never be stopped and will potentially pile up. This would be a bug in the LSP and not in Nvim, but it's not ideal behavior.
- `exit_timeout = false` behaves differently to `exit_timeout = math.huge`

### Keep the current behavior, but make it official

Keep the behavior as is, but explicitly document it as an exception to the `exit_timeout` rules.

Pros:
- Nvim exit is kept as simple as possible: no messages, no daemonized processes, etc.

Cons:
- Force stopping a language server can lead to file corruption, and defaulting to this behavior on Nvim exit is bad.
- `exit_timeout = false` behaves differently to `exit_timeout = math.huge`.
- Does the exact opposite of what `exit_timeout = false` represents.

---

cc @justinmk @mfussenegger @zeertzjq @phanen

### Nvim version (nvim -v)

NVIM v0.12.0-dev-2313+g7d8653575f

---

## #37885: Wasm/Emscripten build fails: luv cannot find LibUV

**Labels:** build

### Problem

When attempting to build Neovim for WebAssembly using Emscripten, the dependency build fails during luv configuration with:

<img width="931" height="141" alt="Image" src="https://github.com/user-attachments/assets/503942b7-f5d3-488d-8d5e-98c76c9e577b" />

This occurs even though LibUV builds successfully earlier in the process.

### Expected behavior

When trying to run make deps with Emscripten, LibUV is built first and installed to .deps/usr/lib/libuv.a as a WebAssembly compiled library. However, when luv begins its configuration, it searches for LibUV in standard system paths like /usr/lib and /usr/local/lib. These system paths compiled for the host system, not WebAssembly libraries. The build system is cross compiling, so these native libraries are incompatible and should not be used, but CMake doesn't know that, so it simply fails when it cannot find a suitable LibUV in the system paths.

Without explicit LIBUV_INCLUDE_DIR and LIBUV_LIBRARY paths being passed to luv's CMake configuration, the FindLibuv.cmake module cannot locate the cross compiled library. This is why native builds work fine, but WebAssembly builds fail. So, what I am proposed is to modify `cmake.deps/cmake/BuildLuv.cmake` to pass LibUV paths in this case. 

If the proposed approach and explanation are correct, I could submit a PR.

---

## #37876: `:nohlsearch` doesn't call dictwatcher for `v:hlsearch`

**Labels:** vimscript

### Problem

Executing `:nohlsearch` changes the value of `v:hlsearch` to zero, but the dictwatcher for `v:` is not called.

### Steps to reproduce

1. Create the following 'init.vim':

    ```vim
    function! WatchHLSearch(d,k,z)
      let g:n_hlsearch = g:n_hlsearch + 1
    endfunction
    call dictwatcheradd(v:, 'hlsearch', 'WatchHLSearch')

    let g:n_hlsearch = 0
    call setline(1, 'aa aaa aaaa')
    ```

2. `nvim --clean -u init.vim`
3. Type `/a<CR>` to start searching. Executing `:echo g:n_hlsearch v:hlsearch` shows `0 1`.
4. Execute `:nohlsearch`. Output of `:echo g:n_hlsearch v:hlsearch` is now `0 0`. Meaning `v:hlsearch` has changed but dict watcher was not called.
5. To be sure that dict watcher works, execute `:let v:hlsearch = 1 - v:hlsearch`. Output of `:echo g:n_hlsearch v:hlsearch` is now `1 1`.

### Expected behavior

Dictwatcher for `v:hlsearch` is called after `:nohlsearch` since it does change the value of the `v:hlsearch`.

I am aware of #21469, but this issue might be the result of `:nohlsearch` bypassing the regular "set variable" rules, so might still be relevant.

### Nvim version (nvim -v)

NVIM v0.12.0-dev-2306+gf8d59cfab9

### Vim (not Nvim) behaves the same?

No, doesn't have this functionality

### Operating system/version

EndeavourOS Linux x86_64, 6.18.9-arch1-2

### Terminal name/version

Ghostty 1.2.3-arch2

### $TERM environment variable

xterm-ghostty

### Installation

Appimage

---

## #37874: treesitter/extmarks: Unable to unset (NONE) guibg on nested highlight group

**Labels:** highlight, treesitter

### Problem

Via legacy syntax highlighting I am able to unset `guibg` from a nested group and have its background color removed again.

Given this sample bash script (`foobar.sh`):

```bash
﻿#!/usr/bin/env bash
foo="bar"
echo "Hello $foo"
```

I can run the following commands after starting `NVIM_APPNAME=stock nvim foobar.sh` (no plugins):

```
:set termguicolors
:hi Normal guibg='NONE'
:hi shDerefSimple guibg='#ffccff'
:hi shDoubleQuote guifg='#000000' guibg='#ffccff'
:hi shDerefSimple guibg='NONE'
```

And the overall result as well as the output of `:Inspect` on `foo` shows:

<img width="230" height="187" alt="Image" src="https://github.com/user-attachments/assets/088b7c05-d132-45f0-8821-7a179a97ea23" />

**The background color of `$foo` was removed**, we can clearly see that `shDerefSimple` is nested inside of `shDoubleQuote`, but the `NONE` of `shDerefSimple` takes precedence.

The same is not true when using `nvim` with `nvim-treesitter`, which defines own namespaces using extmarks.

### Steps to reproduce

```
nvim foobar.sh # with nvim-treesitter installed
:set termguicolors
:hi Normal guibg='NONE'
:hi @punctuation.special.bash guibg='#ffccff'
:hi @variable.bash guibg='#ffccff'
:hi @string.bash guifg='#000000' guibg='#ffccff'
:hi @punctuation.special.bash guibg='NONE'
:hi @variable.bash guibg='NONE'
```

Now the overall result as well as the output of `:Inspect` on `foo` shows:

<img width="506" height="197" alt="Image" src="https://github.com/user-attachments/assets/611e0c42-30f3-4c62-a660-0da87fc43296" />

**The variable `$foo` still has a background color, which is wrong.**

### Expected behavior

I would expect extmarks highlighting to behave in the same way as legacy highlighting.

### Nvim version (nvim -v)

NVIM v0.11.5 Build type: Release LuaJIT 2.1.1765228720

### Vim (not Nvim) behaves the same?

extmarks is a NeoVim feature

### Operating system/version

macOS 15.7.3

### Terminal name/version

wezterm 20240203-110809-5046fc22

### $TERM environment variable

screen-256color

### Installation

Homebrew

---

## #37867: marktree.c:378: unintersect_node: Assertion `seen' failed (Debug build)

**Labels:** has:repro, has:backtrace, bug-crash, marks

### Problem

Already reported as https://github.com/neovim/neovim/issues/27196 but the issue is locked.

nvim aborts with an assertion failure in marktree.c.

I used AFL++ to fuzz nvim and find several repros (or several variations of the same repro).

### Steps to reproduce

Save this as seen-repro.lua:

```
local namespace_id = vim.api.nvim_create_namespace('extmark-fuzz')

local lines = {}
for _ = 1, 301 do
    table.insert(lines, string.rep('o', 48))
end
vim.api.nvim_buf_set_lines(0, 48, 48, false, lines)

vim.api.nvim_buf_set_extmark(0, namespace_id, 190, 48, {
    right_gravity = false,
})

vim.api.nvim_buf_set_extmark(0, namespace_id, 48, 48, {})

vim.api.nvim_buf_set_extmark(0, namespace_id, 190, 48, {
    right_gravity = false,
})

vim.api.nvim_buf_set_extmark(0, namespace_id, 166, 48, {
    right_gravity = false,
    end_row = 166,
    end_col = 48,
})

vim.api.nvim_buf_set_extmark(0, namespace_id, 48, 48, {
    end_row = 48,
    end_col = 48,
})

vim.api.nvim_buf_set_extmark(0, namespace_id, 48, 48, {
    end_row = 48,
    end_col = 48,
})

vim.api.nvim_buf_set_extmark(0, namespace_id, 48, 48, {
    end_row = 255,
    end_col = 48,
})

vim.api.nvim_buf_set_extmark(0, namespace_id, 131, 48, {
    right_gravity = false,
    end_row = 48,
    end_col = 48,
})

vim.api.nvim_buf_set_extmark(0, namespace_id, 131, 48, {
    right_gravity = false,
    end_row = 48,
    end_col = 48,
})

vim.api.nvim_buf_set_extmark(0, namespace_id, 48, 48, {
    end_row = 131,
    end_col = 48,
})

vim.api.nvim_buf_set_extmark(0, namespace_id, 48, 48, {
    right_gravity = false,
    end_row = 216,
    end_col = 48,
})

vim.api.nvim_buf_set_extmark(0, namespace_id, 172, 48, {
    right_gravity = false,
    end_row = 51,
    end_col = 48,
})

vim.api.nvim_buf_set_extmark(0, namespace_id, 131, 48, {
    right_gravity = false,
    end_row = 131,
    end_col = 48,
})

vim.api.nvim_buf_set_extmark(0, namespace_id, 156, 48, {
    right_gravity = false,
    end_row = 131,
    end_col = 48,
})

vim.api.nvim_buf_set_extmark(0, namespace_id, 135, 48, {
    right_gravity = false,
    end_row = 166,
    end_col = 48,
})

vim.api.nvim_buf_set_extmark(0, namespace_id, 172, 48, {
    right_gravity = false,
    end_row = 250,
    end_col = 48,
})

vim.api.nvim_buf_set_extmark(0, namespace_id, 48, 48, {
    right_gravity = false,
    end_row = 143,
    end_col = 48,
})

vim.api.nvim_buf_set_lines(0, 48, 187, false, {})

vim.cmd.qall({ bang = true })
```

Execute with:

```
./build/bin/nvim -u NONE -i NONE -n --headless --cmd "source seen-repro.lua"
```

It works fine with `-S seen-repro.lua` also, I've just been using --cmd because it runs earlier in startup, as I understand it.

Any attempt I've made to simplify by removing an individual `nvim_buf_set_extmark` call has resulted in no repro.

Also, every version of the repro that I've collected follows the same pattern: Add lines to the file, add several extmarks with different parameters, in some cases delete an single extmar

*[truncated]*

---

## #37862: `:nospecial cmd [args...]` invokes cmd with literal args

**Labels:** needs:discussion, cmdline-mode, editor

## Problem

No way to invoke a command with a "raw", literal arg, without dealing with command-specific escaping. 

Some things like `fnameescape()` exist to deal with this, but that only works if the command expects a filename. And it depends on escaping rules, which can be fragile.

## Expected behavior

    :nospecial cmd arg

invokes `:cmd` with literal raw `arg`, including all whitespace.

    :2nospecial cmd arg1 arg2

invokes `:cmd` with literal `arg1` and `arg2`, split at the first whitespace. Does not support "escaping" whitespace, thus `:2nospecial cmd arg1\ arg2` passes `arg1\` literally as arg1.

## use cases

- internal calls to `:help <token>` https://github.com/neovim/neovim/blob/cadddbff6959a23337d417b000177326abc5a862/src/nvim/normal.c#L3325
- session restore https://github.com/neovim/neovim/blob/cadddbff6959a23337d417b000177326abc5a862/src/nvim/ex_session.c#L288

---

## #37850: `vim._with` `emsg_silent=true` can silent all error in cmdline

**Labels:** lua

## Problem

Describe the problem (concisely).

## Steps to reproduce

`nvim --clean -u repro.lua`, then `:echoerr 123`, nothing is shown.
```lua
local api, fn = vim.api, vim.fn
-- api.nvim_create_autocmd("CursorMovedC", {
api.nvim_create_autocmd("CmdlineChanged", {
	callback = function(args)
		if args.match ~= ":" then
			return
		end
		-- vim.cmd([[silent! ]])
		vim._with({ emsg_silent = true }, function()
			-- return api.nvim_parse_cmd(fn.getcmdline(), {})
		end)
	end,
})
```

## Expected behavior
`:echoerr 123` shouldn't be silent.

## System info

- Nvim version (nvim -v): `v0.12.0-dev-2284 g9c5ade9212` neovim/neovim@9c5ade9212
- Vim (not Nvim) behaves the same?: ?
- Operating system/version: Linux 6.18.9-zen1-2-zen
- Terminal name/version: kitty
- $TERM environment variable: `xterm-kitty`
- Installation: ?

---

## #37848: inccommand: `:substitute` preview does not respect `matchadd()` priority

**Labels:** compatibility, inccommand

### Problem

When using `matchadd()` with low priority (e.g., -1), / search correctly displays the search highlight on top of the matchadd highlight. However, `:substitute` preview ignores match priority, and the matchadd highlight appears on top of the substitute preview instead.

This creates inconsistent behaviour between two search mechanisms that should handle priority uniformly.

_(I would expect that both have the same behaviour when interacting with matchadd highlighting)_

### Steps to reproduce

```sh
nvim --clean
```

Run these commands:

```lua
:highlight TestHL guibg=Red ctermbg=Red
:call matchadd('TestHL', 'foo', -1)
```

Insert sample text:

```
foo bar foo bar
foo barz fooz bar
```

**Test 1 - Search (works correctly):**
```lua
/foo
```
Result: Search highlight appears on top of red background ✅ 

<img width="1436" height="750" alt="Image" src="https://github.com/user-attachments/assets/64882d27-24dc-46b4-b66e-544562d5c16b" />

**Test 2 - Substitute ():**
```lua
:%s/foo/foo test/gc
```
Result: Red background overlaps substitute preview highlight ❌

<img width="1437" height="749" alt="Image" src="https://github.com/user-attachments/assets/93271ae1-75fa-45b9-92e9-631ceb5c8e1f" />

### Expected behavior

Both `/` search and `:%s` substitute preview should respect `matchadd()` priority consistently. With priority -1, the `matchadd` highlight should appear behind other highlights in both cases.

### Nvim version (nvim -v)

0.11.2

### Vim (not Nvim) behaves the same?

N/A

### Operating system/version

macOS 26.1

### Terminal name/version

Ghostty 1.2.3 (commit 6d2dd585a)

### $TERM environment variable

tmux-256color

### Installation

homebrew

---

## #37832: vim.lsp.util.apply_text_edits forces given buffer to be listed (buflisted=true)

**Labels:** lsp

I have a question about this line of code in the function `apply_text_edit`:

https://github.com/neovim/neovim/blob/8a0cbf04d6a60f91c69c707789b18986a6921f8f/runtime/lua/vim/lsp/util.lua#L315

I am aware this code is mentioned in this issue:
https://github.com/neovim/neovim/issues/25272

I was wondering why does this function change the current buffer to a listed one.
Is this critically needed?
It seems to be a bug to me.

Even trying to load the buffer (just above) seems strange.
Why would you make edits to a buffer that is not even loaded.

But I don't know much about the inner workings of vim/neovim so I may be wrong.

## Why I'm asking

I was experiencing very strange crashes in one of my custom plugins.

It was caused by me handling the BufDelete event, which I thought `only me™` could possibly trigger.

But it turns out, the BufDelete was also emitted by a [nvim-cmp] completion confirmation.
Because it calls `apply_text_edit` during this procedure.
And it will also remember the buflisted value before the call, and then reapply the old buflisted value after the call.

https://github.com/hrsh7th/nvim-cmp/blob/da88697d7f45d16852c6b2769dc52387d1ddc45f/lua/cmp/utils/api.lua#L74-L79

This will cause neovim (I think) to emit a BufDelete event.
(because the buffer becomes unlisted?)

The problem is, the buffer is not deleted, it is still there.
So it might even be a bug in neovim, I don't know.

<details>
<summary>I have a snippet to reproduce the issue if it helps:</summary>

If you just change the buffer from listed to unlisted (even though the buffer is not destroyed, the event is still fired):

`nvim -u <filename> --noplugins`
```lua
-- Setup textEdit payload for demonstration
local textEdit = {
	newText = "",
	range = {
		["end"] = { character = 0, line = 1 },
		start = { character = 0, line = 1 },
	},
}

-- Create an unlisted, scratch buffer (the problem only happens in an unlisted buffer, scratch or not)
local the_buffer = vim.api.nvim_create_buf(false, true)

-- Setup a listener to see the problem occur
vim.api.nvim_create_autocmd("BufDelete", {
	group = vim.api.nvim_create_augroup("ReproGroup", { clear = true }),
	callback = function()
		vim.api.nvim_buf_set_lines(the_buffer, -1, -1, false, { "A BufDelete event was triggered!!" })
	end,
})

-- Just a quick setup with some guidance (no impact on the issue)
vim.cmd.buffer(the_buffer)

local function append(lines) vim.api.nvim_buf_set_lines(0, -1, -1, false, lines) end
local function buflisted() return vim.bo[the_buffer].buflisted and "✅ listed" or "❌ unlisted" end

--- This is cmp.utils.api.apply_text_edits with added debug statements
local function apply_text_edits(text_edits, bufnr, position_encoding)
	-- preserve 'buflisted' state because vim.lsp.util.apply_text_edits forces it to true
	local prev_buflisted = vim.bo[bufnr].buflisted                         append({ "Memorize buflisted                    "..buflisted() })
	vim.lsp.util.apply_text_edits(text_edits, bufnr, position_encoding) 

*[truncated]*

---

## #37814: LSP:  `nil` index in `lsp/_changetracking.lua`

**Labels:** lsp

### Problem

[Kulala](https://github.com/mistweaverco/kulala.nvim) is a Neovim plugin that bundles an in-process LSP. When using its LSP, in combination with a regular LSP, file edits may throw an error: 
```
Lua callback: /usr/share/nvim/runtime/lua/vim/lsp/_changetracking.lua:308: attempt to index local 'buf_state' (a nil value)
stack traceback:
	/usr/share/nvim/runtime/lua/vim/lsp/_changetracking.lua:308: in function 'send_changes_for_group'
	/usr/share/nvim/runtime/lua/vim/lsp/_changetracking.lua:351: in function 'send_changes'
	/usr/share/nvim/runtime/lua/vim/lsp.lua:927: in function </usr/share/nvim/runtime/lua/vim/lsp.lua:921>
```
If I then try to save the file, I get another error:
```
Error in BufWritePost Autocommands for "<buffer=1>":
Lua callback: /usr/share/nvim/runtime/lua/vim/lsp/_changetracking.lua:175: attempt to index local 'buf_state' (a nil value)
stack traceback:
	/usr/share/nvim/runtime/lua/vim/lsp/_changetracking.lua:175: in function '_get_and_set_name'
	/usr/share/nvim/runtime/lua/vim/lsp.lua:838: in function 'text_document_did_save_handler'
	/usr/share/nvim/runtime/lua/vim/lsp.lua:916: in function </usr/share/nvim/runtime/lua/vim/lsp.lua:915>
```
Related: https://github.com/neovim/neovim/pull/37454

### Steps to reproduce using "nvim --clean -u minimal_init.lua"

Not quite as minimal™ because it requires Kulala. I could only observe this behavior with its LSP.

- Config
```lua
vim.pack.add({
	"https://github.com/mistweaverco/kulala.nvim",
})
require("kulala").setup()

---@type vim.lsp.Config
vim.lsp.config("jsonls", {
	cmd = { "vscode-json-language-server", "--stdio" },
	filetypes = { "json", "jsonc" },
})

vim.lsp.enable("jsonls")
```
- Sample file:
```json
{"vimscript":"let SessionLoad = 1\nlet s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1\nlet v:this_session=expand(\"<sfile>:p\")\nsilent only\nsilent tabonly\ncd ~/.local/share/nvim/possession\nif expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''\n  let s:wipebuf = bufnr('%')\nendif\nlet s:shortmess_save = &shortmess\nset shortmess+=aoO\nbadd +1 minimal.lua\nargglobal\n%argdel\n$argadd minimal.lua\nedit minimal.lua\nargglobal\nsetlocal foldmethod=expr\nsetlocal foldexpr=v:lua.vim.treesitter.foldexpr()\nsetlocal foldmarker={{{,}}}\nsetlocal foldignore=#\nsetlocal foldlevel=99\nsetlocal foldminlines=1\nsetlocal foldnestmax=20\nsetlocal foldenable\nlet s:l = 1 - ((0 * winheight(0) + 20) / 41)\nif s:l < 1 | let s:l = 1 | endif\nkeepjumps exe s:l\nnormal! zt\nkeepjumps 1\nnormal! 0\ntabnext 1\nif exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'\n  silent exe 'bwipe ' . s:wipebuf\nendif\nunlet! s:wipebuf\nset winheight=1 winwidth=20\nlet &shortmess = s:shortmess_save\nlet s:sx = expand(\"<sfile>:p:r\").\"x.vim\"\nif filereadable(s:sx)\n  exe \"source \" . fnameescape(s:sx)\nendif\nlet &g:so = s:so_save | let &g:siso = s:siso_save\nset hlsearch\ndoautoall Se

*[truncated]*

---

## #37800: terminal: wrong cursor position in prompt after closing window

**Labels:** terminal

### Problem

When the shell's prompt spans multiple lines (e.g., default config from [starship](https://starship.rs/)), closing a window may cause the cursor to be drawn on the wrong position.

### Steps to reproduce

1. `:term`
2. `:vert new`
3. Repeat step 2 until prompt wraps into multiple lines:
Start:

<img width="597" height="116" alt="Image" src="https://github.com/user-attachments/assets/d16ad41b-10c6-477d-bb95-c1dd6b888b62" />

Expected:

<img width="502" height="140" alt="Image" src="https://github.com/user-attachments/assets/b3109a5a-d5a4-432a-a103-18c923c29355" />

4.  Switch to terminal window
5. `:new|quit|starti`
6. Insert any text, it will not show on the correct line:
<img width="551" height="129" alt="Image" src="https://github.com/user-attachments/assets/c6557453-e87a-4503-acda-2c8b05df1fb1" />

### Expected behavior

Cursor should be drawn on the correct line

### Nvim version (nvim -v)

v0.12.0-dev-2246+g57fc77ed29

### Vim (not Nvim) behaves the same?

N/A

### Operating system/version

Linux 6.18

### Terminal name/version

foot 1.25.0

### $TERM environment variable

xterm-256color

### Installation

AUR

---

## #37789: Image API proposal

**Labels:** api

### Problem

# Image API proposal

A previous attempt (#31399) to implement image support was halted due to disagreements over the API design (#34093). So I have made my own proposal for an image API and any feedback would be much appreciated.

## Motivation

Image support has been a requested feature in Neovim (see #30889) and there has even been a previous attempt (#31399) at implementing this feature. There are existing plugins that provide image support, such as
[image.nvim](https://github.com/3rd/image.nvim), [snacks.nvim](https://github.com/folke/snacks.nvim), and this proposal would build on these and add this as a core feature -- similar to `vim.lsp` and `lsp_config`. I would develop this as part of a [Google Summer of Code](https://summerofcode.withgoogle.com/) project.

## High level overview

This would be aimed at plugin developers as an easy and first class way off adding images to their plugins.

Initially the API would support only the kitty graphics protocol [^1] and would serve as a thin abstraction layer implemented in lua. Relative / inline placement only would be supported since I believe this is easier to implement
and more useful. It would use Unicode placeholders as this would allow for use of the protocol when running tmux and would simplify the inserting of images within a block of text. Placeholders would be inserted in the correct row and column, shifting any following text to the right.

To use the API one would first load an image, which transfers the image to the terminal. Then create a placement which generates the required text to be inserted. To show an image one specifies an image id and a placement id, which creates a virtual placement and inserts the generated text in the correct position in the buffer.

[^1]: Previous implementations were [criticised](https://github.com/neovim/neovim/issues/34093#issuecomment-2893087110) for being too complex for a first implementation since they attempted to
integrate multiple different providers. Kitty is the most complete image protocol and so I have chosen it as the first to be implemented. More providers can always be added later.

### Expected behavior

## API

The API suggested below is a rather direct conversion of the kitty API.

`image_id: int` \
`placement_id: int` \
Image and placement ids would be non overlapping allowing the program to distinguish between them even though internally they are just ints.

`load_image(bytes) -> image_id` \
`load_image(file_path) -> image_id` \
Transfers an image to the terminal; raises an error if the image is not of a supported type (RGB/RGBA/PNG).

`create_placement(line, col, width, height) -> placement_id` \
Generates the required unicode placeholders for an image of the specified width and height.

`draw_image(image_id, placement_id)` \
Creates a virtual placement and inserts the generated unicode placeholders into the buffer.

`delete_placement(placement_id)` \
Deletes a single placement of an image, leaving all others intact.

*[truncated]*

---

## #37780: Whitespace in the middle of the line can be removed when exiting into Normal mode

**Labels:** bug-vim, editor

### Problem

Whitespace in the middle of the line (i.e. not leading and not trailing) can be removed when exiting from Insert into Normal mode (even if temporary with `<C-o>`).

This behavior can be reproduced in as far as Neovim 0.5.1, **but** it is not present in Vim 9.1.2132.

### Steps to reproduce

1. Create the following 'init-remove-whitespace.vim' file:

    ```vim
    set nocompatible
    inoremap <M-t> <Cmd>call setline('.', 'v  v')<CR><Cmd>call setpos('.', [0, line('.'), 2, 0])<CR>
    ```

2. `nvim --clean -u init-remove-whitespace.vim`
3. Start Insert mode with `i` and press `<M-t>`. It inserts `v  v` with cursor after first `v`.
4. Exit into Normal mode with `<Esc>`. The line stays the same `v  v`, which is expected.
5. Start Insert mode on an empty line with `cc` (or `o`, or `O`) and press `<M-t>`. It still inserts `v  v`  with cursor after first `v`.
6. Exit into Normal mode with `<Esc>` (or `<C-o>`). Line becomes `vv`.


### Expected behavior

Whitespace in the middle of the line doesn't change after exiting into Normal mode.

### Nvim version (nvim -v)

NVIM v0.12.0-dev-2224+gc90593ed5f, can be reproduced as far as 0.5.1

### Vim (not Nvim) behaves the same?

No, not in 9.1.2132

### Operating system/version

EndeavourOS Linux x86_64, 6.18.7-arch1-1

### Terminal name/version

Ghostty 1.2.3-arch2

### $TERM environment variable

xterm-ghostty

### Installation

Appimage

---

## #37719: Some Nvim API functions return Buffer, Window, Tabpage objects, but doc only say they return `integer`

**Labels:** documentation, api

### Problem

Nvim API defines 3 special types `Buffer`, `Window` and `Tabpage`. Even though they seem like subtype/subclass of integers, they are still not integers in some API clients. It seems to me that Nvim has some API functions that return Buffer, Window, Tabpage, but the document only say they return integer.

### Steps to reproduce

#### Test 1

Make sure to have Nvim with `has("python3")` return 1

1. nvim --clean
1. `:h nvim_win_get_buf`. You can see that the document says this function return window id as `integer`
1. py buf=vim.request("nvim_win_get_buf", 1000)
1. py = type(buf) # <class 'pynvim.api.buffer.Buffer'>
1. py = isinstance(buf, int) # False, so it is not even a subclass of integer

#### Test 2
```ruby
require 'msgpack/rpc'
require 'msgpack/rpc/transport/unix'

nvim = MessagePack::RPC::Client.new(MessagePack::RPC::UNIXTransport.new, ENV['NVIM'])
puts nvim.call(:nvim_win_get_buf, 1000)
```
Copy to a Nvim buffer and save it, then run the above file with `:term ruby %`, you can see it returns an error
```
/var/lib/gems/3.2.0/gems/msgpack-rpc-0.7.0/lib/msgpack/rpc/future.rb:59:in `get': request timed out (MessagePack::RPC::TimeoutError)
        from /var/lib/gems/3.2.0/gems/msgpack-rpc-0.7.0/lib/msgpack/rpc/session.rb:54:in `call'
        from test.rb:5:in `<main>'
```
But if I change the last line of the above Ruby file to
```ruby
puts nvim.call(:nvim_eval, 'nvim_win_get_buf(1000)')
```
Then run it again and it works (it prints number `1`)

So I guess the error with the above Ruby script is because Nvim API returns type `Buffer` for the first Ruby script instead of just normal `integer`

### Expected behavior

Nvim must correct document of return type of functions that return Buffer, Window or Tabpage objects



### Nvim version (nvim -v)

NVIM v0.12.0-dev-ddd1bf7

### Vim (not Nvim) behaves the same?

NA

### Operating system/version

Kubuntu 24.04.1

### Terminal name/version

NA

### $TERM environment variable

NA

### Installation

source

---

## #37703: float: allow to set cursor shape from the window behind in some cases

**Labels:** api, floatwin

### Problem

This is a follow-up of #37624 (https://github.com/neovim/neovim/pull/37624#issuecomment-3846784011).

Sometimes we have created non-focusable decoration windows on top of the current non-float window and rather don't want to obscure the cursor. 

An example is a list of (possibly long) names inside a narrow, vertical window (like the nvim-tree view shown below).

<img width="858" height="325" alt="image" src="https://github.com/user-attachments/assets/75d7019c-4eed-4c09-b2ba-a88c03df19d1" />

### Expected behavior

Allow a single float window to set cursor shape from the window behind, apparently by a new win_config option.

---

## #37698: vim.fs: trim redundant trailing slashes with basename(), dirname()

**Labels:** needs:decision, documentation, lua, filesystem

### Problem

https://github.com/neovim/neovim/blob/ddd1bf757fab3615301053acab5cc85508340844/runtime/lua/vim/fs.lua#L114

```lua
:= vim.fs.basename("/name/")
""
```

### Expected behavior

```lua
:= vim.fs.basename("/name/")
:= vim.fs.basename("/name//////////")
"name"
```

The same behavior as `basename` in the shell or `path.basename` in [Node.Js #pathbasenamepath-suffix](https://nodejs.org/api/path.html#pathbasenamepath-suffix).

---

## #37696: LSP: `Client:supports_method("callHierarchy/[incom|outgo]ingCalls")` should have same result as "textDocument/prepareCallHierarchy"

**Labels:** lsp

### Problem

The LSP spec says that "callHierarchy/incomingCalls" and "callHierarchy/outgoingCalls" don't have their own capabilities; instead, servers with the "textDocument/prepareCallHierarchy" capability support them.

Thus, `Client:supports_method("callHierarchy/[incom|outgo]ingCalls")` in practice always returns true since no server would advertise capabilities under those names.

Calling something like `vim.lsp.buf_request_sync("callHierarchy/incomingCalls)` will thus always send requests to all servers even if they explicitly do not support it by not advertising "textDocument/prepareCallHierarchy".

### Steps to reproduce using "nvim --clean -u minimal_init.lua"

```lua
---@type vim.lsp.Config
return {
	cmd = { 'stylua', '--lsp' },
	filetypes = { 'lua' },
}
```

### Expected behavior

The result of `Client:supports_method("callHierarchy/[incom|outgo]ingCalls")` should have the same result as if called with "textDocument/prepareCallHierarchy"

### Nvim version (nvim -v)

NVIM v0.12.0-dev-2186+gddd1bf757f

### Language server name/version

any that doesn't support prepareCallHierarchy, like stylua

### Operating system/version

macOS 26

### Log file

_No response_

---

## #37691: `textDocument/documentLink` improvements

**Labels:** lsp

https://github.com/neovim/neovim/pull/37644 adds basic support for [`textDocument/documentLink`](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_documentLink), but the implementation could be improved.

### Ideas

- Add support for [`documentLink/resolve`](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#documentLink_resolve) for fetching `target` information instead of filtering out such results.
- Use extmarks to track the links (refer to the discussion in https://github.com/neovim/neovim/pull/37644#discussion_r2752757668 and https://github.com/neovim/neovim/pull/37644#issuecomment-3839890814)

---

## #37687: When building the RPM package it fails in the test suite because of too long and complicated pathnames

**Labels:** test, bug-vim

### Problem

When building [RPM package with the nightly build for openSUSE](https://build.opensuse.org/package/show/home:mcepl/neovim-nightly), it passes the build and most of the test suite, but it fails with this error:

```
[  209s] Failures: 
[  209s]        From test_mksession.vim:
[  209s]        Found errors in Test_mksession_rtp():
[  209s]        Caught exception in Test_mksession_rtp(): Vim(let):E33: No previous substitute regular expression @ command line..script /home/abuild/rpmbuild/BUILD/neovim-0.12.0_git.1770107487.d594407735-build/neovim-0.12.0~git.1770107487.d594407735/test/old/testdir/runtest.vim[659]..function RunTheTest[61]..Test_mksession_rtp[17]..<lambda>1, line 1
[  209s]        Found errors in Test_mkview_no_file_name():
[  209s]        Caught exception in Test_mkview_no_file_name(): Vim(help):E856: Filename too long @ command line..script /home/abuild/rpmbuild/BUILD/neovim-0.12.0_git.1770107487.d594407735-build/neovim-0.12.0~git.1770107487.d594407735/test/old/testdir/runtest.vim[659]..function RunTheTest[61]..Test_mkview_no_file_name, line 8
[  209s]        From test_packadd.vim:
[  209s]        Found errors in Test_packadd():
[  209s]        command line..script /home/abuild/rpmbuild/BUILD/neovim-0.12.0_git.1770107487.d594407735-build/neovim-0.12.0~git.1770107487.d594407735/test/old/testdir/runtest.vim[659]..function RunTheTest[61]..Test_packadd line 14: Pattern '^nosuchdir,/home/abuild/rpmbuild/BUILD/neovim-0.12.0_git.1770107487.d594407735-build/neovim-0.12.0~git.1770107487.d594407735/test/old/testdir/Xdir/pack/mine/opt/mytest,' does not match 'nosuchdir,/home/abuild/rpmbuild/BUILD/neovim-0.12.0_git.1770107487.d594407735-build/neovim-0.12.0~git.1770107487.d594407735/test/old/testdir/Xdir/pack/mine/opt/mytest,/home/abuild/rpmbuild/BUILD/neovim-0.12.0_git.1770107487.d594407735-build/neovim-0.12.0~git.1770107487.d594407735/test/old/testdir/Xdir/pack/mine/opt/mytest/after,/home/abuild/rpmbuild/BUILD/neovim-0.12.0_git.1770107487.d594407735-build/neovim-0.12.0~git.1770107487.d594407735/test/old/testdir/Xdir/pack/mine/opt/mytest/after'
[  209s]        Caught exception in Test_packadd(): Vim(call):E33: No previous substitute regular expression @ command line..script /home/abuild/rpmbuild/BUILD/neovim-0.12.0_git.1770107487.d594407735-build/neovim-0.12.0~git.1770107487.d594407735/test/old/testdir/runtest.vim[659]..function RunTheTest[61]..Test_packadd, line 14
```

[Complete build log](https://github.com/user-attachments/files/25047090/_log.txt) with all packages used and all steps taken to reproduce.

Exact steps taken could be (hopefully) read from [the SPEC file](https://build.opensuse.org/projects/home:mcepl/packages/neovim-nightly/files/neovim.spec).

### Steps to reproduce

See above

### Expected behavior

The test suite should pass even in the build environment with complicated and long pathnames.

### Nvim version (nvim -v)

0.12.0~git.1770107487.d594407735 (the last part is the commit)

### Vim (not Nvim) behaves the s

*[truncated]*

---

## #37674: Semantic Diff using Gumtree Algorithm and Treesitter (Discussion)

**Labels:** treesitter

### Problem

When I moved from JetBrains IDEs (tried Rider for game dev) back to Neovim, one thing I actually miss is how they handled diffs. If you move a function, it showed "hey this moved" instead of treating it like you deleted and rewrote it

**Current Behavior (line diff)**:
```diff
- function calculate(x, y) { return x + y; } // looks deleted

+ function calculate(x, y) {return x + y; } // looks like new code
```

### Expected behavior

**What I am proposing**:
```lua
M | calculate()     ⤷ moved to L200
```
This would make code reviews and refactoring way cleaner.

## Why not just make a plugin?
I know this was discussed way back in https://github.com/neovim/neovim/issues/15064. @lewis6991 suggested trying it as plugin first, and someone else mentioned using `diffexpr` to call external tools
So I tried the plugin route:
I have a built a *proof of concept* Lua plugin that implements the GumTree algorithm with treesitter. It works(not perfectly right now), it detects moves and updates well in practice. But it hits some fundamental walls:
- `vim.diff()` is purely line-based, no way to tell it "these are the same even though they moved"
- Had to use `extmarks` with virtual text, to show the "Moved to L...", which imo is a good way to represent **move**, but currently it can not integrate with `:diffthis`
- Can't use the existing diff utilities, have to reparse tree-sitter ASTs even though they are already in memory for syntax highlighting

The `diffexpr` approach could work but has downsides:
- Need to shell out to external tools
- Loses the benefit of tree-sitter already being in memory
- Still can't properly integrate moves/updates into Neovim's diff UI
- Users would need to install separate tools

After working on diffopt(`inline:word`) improvements in https://github.com/neovim/neovim/pull/37085, I got familiar with this part of the codebase and I feel this actually needs core support to work properly. The tree-sitter integration is already there, just needs the diff engine to understand semantic operations.

## The Pitch
This would:
- Reuse tree-sitter parses that already happen for syntax highlighting
- Only run when you actually diff (zero background cost)
- Be opt-in via `diffopt+=semantic` or `diffopt+=algorithm:gumtree` or similar
- Fall back to regular line diff if tree-sitter isn't available or cost is too high
So it's not trying to make Neovim heavy like Rider or something, just one feature that makes diff smarter
**Bonus:** This would benefit plugins like gitsigns. With proper API (`vim.diff(...., {semantic = true})`), git integration plugins could show moved/renamed code in git history and blame views.

## What I have built
Working proof of concept plugin that does(Gumtree Algorithm):
- Top-down matching (exact subtree hash matching)
- Bottom-up matching (matches from children to parents)
- Simple recovery algorithm from [GumTree ICSE '24 paper](https://hal.science/hal-04855170v1/file/GumTree_simple__fine_grained__accurate_and_s

*[truncated]*

---

## #37664: `operatorfunc` operators can't distinguish between regions ending or not in a newline (builtin operators can)

**Labels:** needs:vim-patch, editor

### Problem

Given a buffer with the following content

```
a(
  b
)
```

with the cursor located above `b`, doing `vkol` to get the following visual selection

<img width="112" height="131" alt="Image" src="https://github.com/user-attachments/assets/ba367bf8-f307-4150-859a-398e279700a5" />

and then doing `y` will result in the register `"` containing the trailing newline of the visual selection (i.e. `=vim.fn.getreg('"')` output will be `\n  b\n`).

However, given the same buffer and the same visual selection, using the following `operatorfunc` operator

```lua
---@param type 'line'|'char'|'block'
_G.my_yank = function(type)
	local mode = type == "line" and "V" or type == "char" and "v" or vim.keycode("<c-v>")
	local yanked = vim.fn.getregion(vim.fn.getpos("'["), vim.fn.getpos("']"), { type = mode })
	local end_mark = vim.api.nvim_buf_get_mark(0, "]")
	-- __PRINT_VAR_START
	print([==[┆_G.my_yank┆ ╎end_mark╎ ┊1┊:]==], vim.inspect(end_mark)) -- __PRINT_VAR_END
	-- __PRINT_VAR_START
	print([==[┆_G.my_yank┆ ╎yanked╎ ┊1┊:]==], vim.inspect(yanked)) -- __PRINT_VAR_END
end
vim.keymap.set({ "x", "n" }, "<F4>", function(a)
	vim.o.operatorfunc = "v:lua._G.my_yank"
	return "g@"
end, { expr = true })
```

and typing `<F4>` will result in `┆_G.my_yank┆ ╎yanked╎ ┊1┊: { "", "  b" }` being printed. Note the lack of a trailing empty string representing the trailing newline.

The same happens for the `operatorfunc` operator when the newline is not selected at all. With the cursor above `b`, doing `k` to get the following visual selection

<img width="93" height="118" alt="Image" src="https://github.com/user-attachments/assets/df6adb9c-0698-4d29-bf00-84de0124de19" />

also results in `┆_G.my_yank┆ ╎yanked╎ ┊1┊: { "", "  b" }` being printed.

So, no matter if the newline if visually selected or not, the `operatorfunc` operator sees the same values for the `[` and `]` marks.

This happens because builtin operators (like `y`) get to operate on the range defined by `oap`

https://github.com/neovim/neovim/blob/a8a097d178414e30ed758d332a74e649e43f105c/src/nvim/register.c#L1065-L1071

before its end is adjusted with `decl`

https://github.com/neovim/neovim/blob/a8a097d178414e30ed758d332a74e649e43f105c/src/nvim/register.c#L1158-L1161

On the other hand, `operatorfunc` operators get the value adjusted by `decl` before they can even see it

https://github.com/neovim/neovim/blob/a8a097d178414e30ed758d332a74e649e43f105c/src/nvim/ops.c#L3160-L3163

I also found that, with the first visual selection mentioned, doing `y` results in `vim.api.nvim_buf_get_mark(0, ']')` returning `{2,2}` while `vim.api.nvim_buf_get_mark(0, '>')` returns `{2,3}`

### Steps to reproduce

1. `nvim --clean -u minimal.lua`

where `minimal.lua` contains

```lua
---@param type 'line'|'char'|'block'
_G.my_yank = function(type)
  local mode = type == "line" and "V" or type == "char" and "v" or vim.keycode "<c-v>"
  local yanked = vim.fn.getregion(vim.fn.getpos "'[", vim.fn.getpos "']", { type = mode })
  lo

*[truncated]*

---

## #37653: ui2: spoof cmdline_block events when cmdline is entered during expanded cmdline?

**Labels:** ui2

## Problem

## Steps to reproduce
```
nvim --clean --cmd "lua require('vim._extui').enable{}" --cmd "cnoremap <c-cr> <cmd>lua vim.api.nvim_feedkeys('\r:', 'nt', false)<cr>"
```

## Expected behavior
`<c-cr>` should show message then enter cmdline mode again. (maybe for similar reason `gQ`/exmode don't work well with extui) 

## System info

- Nvim version (nvim -v): `v0.12.0-dev-2160 g1355640d6a-dirty` neovim/neovim@1355640d6a
- Vim (not Nvim) behaves the same?: ?
- Operating system/version: Linux 6.18.7-zen1-1-zen
- Terminal name/version: kitty
- $TERM environment variable: `xterm-kitty`
- Installation: ?

---

## #37638: failed to get cwd of window-ID in other tabpage

**Labels:** window

### Problem

can not using `getcwd(win-id)` to get cwd of the windows, if the winid is not in current tabpage.

### Steps to reproduce

nvim -u NONE
echo win_getid()  -- 1000
tabnew
echo getcwd(1000) -- shows E5002: Cannot find window number.

### Expected behavior

echo getcwd(win-id) should return the cwd of windows.

### Nvim version (nvim -v)

0.11.4

### Vim (not Nvim) behaves the same?

same as vim, in vim 9.1.954

`echo getcwd(1000)` return empty string, and does not show error `Cannot find windows number`

### Operating system/version

win 11

### Terminal name/version

wezterm

### $TERM environment variable

NONE

### Installation

scoop install neovim

---

## #37629: Add French support to :Tutor

**Labels:** localization

### Problem

I am adding French language support to the Neovim `Tutor` command. As a native speaker, I consider this a valuable addition. I’ve already begun work but want to confirm if this is something the project needs or wants.

I have limited experience contributing to open source and may make errors. Let me know if I make any mistakes.

### Expected behavior

A French user could learn Neovim basics in his native language using `:Tutor`

---

## #37625: Wrong information after -V1 and :verbose

**Labels:** build, lua, messages

### Problem

```
$ cd /usr/local/sbin
$ nvim -V1

:verbose set termguicolors?

Last set from /usr/local/sbin/vim/_defaults.lua (run Nvim with -V1 for more details)
              ^^^^^^^^^^^^^^^

$ nvim -V1 -v
NVIM v0.11.5
Build type: Release
LuaJIT 2.1.1731601260
Compilation: /usr/bin/x86_64-pc-linux-gnu-gcc -O2 -pipe   -Wall -Wextra -pedantic -Wno-unused-parameter -Wstrict-prototypes -std=gnu99 -Wshadow -Wconversion -Wvla -Wdouble-promotion -Wmissing-noreturn -Wmissing-format-attribute -Wmissing-prototypes -fsigned-char -fstack-protector-strong -Wno-conversion -fno-common -Wno-unused-result -Wimplicit-fallthrough -fdiagnostics-color=always  -DUNIT_TESTING -D_GNU_SOURCE -DINCLUDE_GENERATED_DECLARATIONS -DUTF8PROC_STATIC -I/usr/include/luajit-2.1 -I/usr/include -I/var/data/large/tmp/portage/app-editors/neovim-0.11.5/work/neovim-0.11.5_build/src/nvim/auto -I/var/data/large/tmp/portage/app-editors/neovim-0.11.5/work/neovim-0.11.5_build/include -I/var/data/large/tmp/portage/app-editors/neovim-0.11.5/work/neovim-0.11.5_build/cmake.config -I/var/data/large/tmp/portage/app-editors/neovim-0.11.5/work/neovim-0.11.5/src

$ uname -sr
Linux 6.12.58-gentoo
$ uname -sr
FreeBSD 14.2-STABLE

```

### Steps to reproduce

see description

### Expected behavior

`/usr/share/vim/...` resp. `/usr/local/share/vim/...`

### Nvim version (nvim -v)

v0.11.5

### Vim (not Nvim) behaves the same?

Didn't try

### Operating system/version

Linux 6.12.58-gentoo / FreeBSD 14.2-STABLE

### Terminal name/version

alacritty

### $TERM environment variable

tmux-256color

### Installation

emerge / make install

---

## #37607: SIGABRT when using :sleep in b:term_title watcher

**Labels:** terminal, has:backtrace, bug-crash, event-loop

### Problem

```
=================================================================
==1452659==ERROR: AddressSanitizer: ABRT on unknown address 0x03e800162a73 (pc 0x7f7eb5d8f90c bp 0x7ffd87e09440 sp 0x7ffd87e09400 T0)
    #0 0x7f7eb5d8f90c in __pthread_kill_implementation /usr/src/debug/glibc/glibc/nptl/pthread_kill.c:44:76
    #1 0x7f7eb5d3539f in raise /usr/src/debug/glibc/glibc/signal/../sysdeps/posix/raise.c:26:13
    #2 0x7f7eb5d1c579 in abort /usr/src/debug/glibc/glibc/stdlib/abort.c:77:3
    #3 0x56281f2121f0 in loop_uv_run **/src/nvim/event/loop.c:44:5
    #4 0x56281f212034 in loop_poll_events **/src/nvim/event/loop.c:80:26
    #5 0x56281f2d62a9 in do_sleep **/src/nvim/ex_docmd.c:6407:3
    #6 0x56281f2f15b1 in ex_sleep **/src/nvim/ex_docmd.c:6394:3
    #7 0x56281f2b092f in execute_cmd0 **/src/nvim/ex_docmd.c:1762:7
    #8 0x56281f293705 in do_one_cmd **/src/nvim/ex_docmd.c:2392:7
    #9 0x56281f288cc6 in do_cmdline **/src/nvim/ex_docmd.c:679:20
    #10 0x56281f28cd48 in do_cmdline_cmd **/src/nvim/ex_docmd.c:377:10
    #11 0x56281f0d1a54 in execute_common **/src/nvim/eval/funcs.c:1322:5
    #12 0x56281f0fb6ea in f_execute **/src/nvim/eval/funcs.c:1359:3
    #13 0x56281f0cf261 in call_internal_func **/src/nvim/eval/funcs.c:282:3
    #14 0x56281f1a03ae in call_func **/src/nvim/eval/userfunc.c:1788:15
    #15 0x56281f19d58b in get_func_tv **/src/nvim/eval/userfunc.c:580:11
    #16 0x56281f041870 in eval_func **/src/nvim/eval.c:1725:13
    #17 0x56281f039cb7 in eval7 **/src/nvim/eval.c:2717:15
    #18 0x56281f035d88 in eval6 **/src/nvim/eval.c:2514:7
    #19 0x56281f035057 in eval5 **/src/nvim/eval.c:2358:7
    #20 0x56281f033c82 in eval4 **/src/nvim/eval.c:2146:7
    #21 0x56281f032def in eval3 **/src/nvim/eval.c:2055:7
    #22 0x56281effd96f in eval2 **/src/nvim/eval.c:1977:7
    #23 0x56281efe89a1 in eval1 **/src/nvim/eval.c:1881:7
    #24 0x56281f1a817d in call_user_func **/src/nvim/eval/userfunc.c:1263:5
    #25 0x56281f1b1fd0 in call_user_func_check **/src/nvim/eval/userfunc.c:1424:5
    #26 0x56281f1a010d in call_func **/src/nvim/eval/userfunc.c:1779:17
    #27 0x56281f01011c in callback_call **/src/nvim/eval.c:4903:13
    #28 0x56281f16776b in tv_dict_watcher_notify **/src/nvim/eval/typval.c:1988:3
    #29 0x56281ecc1663 in dict_set_var **/src/nvim/api/private/helpers.c:253:7
    #30 0x56281feadf79 in buf_set_term_title **/src/nvim/terminal.c:1441:3
    #31 0x56281fec3b44 in term_settermprop **/src/nvim/terminal.c:1471:7
    #32 0x562820151c63 in settermprop **/src/nvim/vterm/screen.c:437:12
    #33 0x5628201650e8 in vterm_state_set_termprop **/src/nvim/vterm/state.c:2376:10
    #34 0x562820199902 in settermprop_string **/src/nvim/vterm/state.c:548:10
    #35 0x56282018aab2 in on_osc **/src/nvim/vterm/state.c:1953:5
    #36 0x5628201348b0 in string_fragment **/src/nvim/vterm/parser.c:89:7
    #37 0x562820131ec2 in vterm_input_write **/src/nvim/vterm/parser.c:323:9
    #38 0x56281feb231f in terminal_receive **/src/nvim/terminal.c:1281:5

*[truncated]*

---

## #37586: Make `:packadd!` not result into 'runtimepath' re-caching when using Lua's `require()`

**Labels:** performance, packages

### Problem

Executing `:packadd!` with 'pack/*/opt' plugins intentionally updates 'runtimepath' value. However, it does so in a way that later prompts for reparsing and recaching of 'runtimepath' value ([here](https://github.com/neovim/neovim/blob/c28113dd9d09b661061d25c147e39efadc6e700b/src/nvim/runtime.c#L656), I believe). Since `:packadd!` already knows how to insert entries into 'runtimepath' value, it might be reasonable for it to also more directly update the parsed/cached value.

---

The current behavior has visible performance downsides when using with `vim.pack.add`. Here is how to reproduce them:

1. Create a separate config directory (like '~/.config/nvim-packadd-bench').
2. Inside of it, add the 'setup-plugins.lua' file that sets up many similar plugins to later be `:packadd!`ed:

    <details><summary>Contents of 'setup-plugins.lua'</summary>

    ```lua
    local create_plugin = function(name, path)
      local cmd = name:sub(1, 1):upper() .. name:sub(2)

      -- 'lua/' module
      local lua_lines = {
        string.format('local run = function() _G.value = "%s" end', cmd),
        string.format('local config = function() _G.%s = { "%s" } end', name, cmd),
        'return { config = config, run = run }',
      }

      vim.fn.mkdir(vim.fs.joinpath(path, 'lua'), 'p')
      vim.fn.writefile(lua_lines, vim.fs.joinpath(path, 'lua', name .. '.lua'))

      -- 'plugin/' script
      local plugin_lines = {
        -- Define one user command
        string.format('vim.api.nvim_create_user_command("%s", function() require("%s").run() end, {})', cmd, name),
        -- Define one `<Plug>` keymap
        string.format('vim.keymap.set("n", "<Plug>(%s)", function() require("%s").run() end)', cmd, name),
      }

      vim.fn.mkdir(vim.fs.joinpath(path, 'plugin'), 'p')
      vim.fn.writefile(plugin_lines, vim.fs.joinpath(path, 'plugin', name .. '.lua'))
    end

    local pack_path = vim.fs.joinpath(vim.fn.stdpath('config'), 'pack', 'demo', 'opt')
    vim.fn.mkdir(pack_path, 'p')

    local n_plugins = 10
    for i = 1, n_plugins do
      local name = string.format('plugin%02d', i)
      local path = vim.fs.joinpath(pack_path, name)
      create_plugin(name, path)
    end
    ```

    </details>

3. Run `NVIM_APPNAME=nvim-packadd-bench nvim -l setup-plugins.lua`.
4. Create an 'init.lua' file for "grouped `:packadd`" config:

    ```lua
    for i = 1, 10 do
      vim.cmd('packadd! plugin' .. string.format('%02d', i))
    end

    for i = 1, 10 do
      require('plugin' .. string.format('%02d', i)).config()
    end
    ```
5. Run `NVIM_APPNAME=nvim-packadd-bench nvim --startuptime startup-grouped`.
6. Replace content of 'init.lua' with "separate `:packadd`" config:

    ```lua
    for i = 1, 10 do
      vim.cmd('packadd! plugin' .. string.format('%02d', i))
      require('plugin' .. string.format('%02d', i)).config()
    end
    ```
7. Run `NVIM_APPNAME=nvim-packadd-bench nvim --startuptime startup-separate`.
8. Observe difference in `require` t

*[truncated]*

---

## #37548: Diagnostic virtual_lines persists after diagnostic is fixed/removed

**Labels:** has:plan, diagnostic

### Problem

When using the example from `:h diagnostic-on-jump-example` to show virtual lines when jumping to diagnostics, the diagnostic and virtual lines persist even after the diagnostic has been fixed or removed.

![Image](https://github.com/user-attachments/assets/9eae7d41-320d-40a7-b98a-78e99c2e145c)

As shown in the gif above, the virtual lines persist on the line where the diagnostic was even though trying to jump to it shows 'No more valid diagnostics to move to'.

### Related

This issue was discovered while working on PR #37516.

### Steps to reproduce

`nvim --clean -u minimal.lua` with the following minimal config using any language server (tested with lua_ls, basedpyright and rust-analyzer):

```lua
vim.lsp.config.basedpyright = {
  cmd = { "basedpyright-langserver", "--stdio" },
  filetypes = { "python" },
}

vim.lsp.enable({ "basedpyright" })

local virt_lines_ns = vim.api.nvim_create_namespace "on_diagnostic_jump"

--- @param diagnostic? vim.Diagnostic
--- @param bufnr integer
local function on_jump(diagnostic, bufnr)
  if not diagnostic then return end

  vim.diagnostic.show(
    virt_lines_ns,
    bufnr,
    { diagnostic },
    { virtual_lines = { current_line = true }, virtual_text = false }
  )
end

vim.diagnostic.config({ jump = { on_jump = on_jump } })
```
Create an error and jump to it with `[d` or `]d`. Then fix/remove the error and move to the line where the diagnostic was.

### Expected behavior

The virtual lines should clear once the diagnostic has been fixed/removed.

### Nvim version (nvim -v)

v0.12.0-dev-2032+gdddc359213

### Vim (not Nvim) behaves the same?

No, Vim 9.1

### Operating system/version

Fedora Linux 43

### Terminal name/version

Ghostty 1.3.0-dev+0000000

### $TERM environment variable

xterm-ghostty

### Installation

Build from repo

---

## #37535: terminal/vterm: character is missing from the display when a single output exceeds 32,768 characters in length

**Labels:** platform:windows, terminal

### Problem

In Neovim's terminal mode, when a single output exceeds 32,768 characters in length, one character is missing from the display.

### Steps to reproduce

```vim
:terminal
```

```bash
# Prepare test text
for i in {1..10000}; do printf "0123456789"; done >> 100000.txt
```

```bash
# Observe the display at the end of the last line
head -c $((32768 + 1)) 100000.txt
```

```bash
# Observe the display at the end of the last line
head -c $((32768 * 2 + 1)) 100000.txt
```

```bash
# Observe the display at the end of the last line
head -c $((32768 * 3 + 1)) 100000.txt
```


### Expected behavior

No character is missing from the display.

### Nvim version (nvim -v)

0.11.5

### Vim (not Nvim) behaves the same?

no. vim 9.1.2081

### Operating system/version

Win10 with msys2 bash shell

### Terminal name/version

libvterm/vterm in neovim

### $TERM environment variable

xterm-256-color

### Installation

official release

---

## #37525: support east-asian sentences as textoject

**Labels:** encoding, needs:vim-patch, normal-mode

### Problem

I implement a neovim plugin to help with japanese learning (a simpler https://rikaitan.github.io/ for neovim).
One thing I want to do is tokenize (split into different words since there are no space between the words, with something like https://github.com/WorksApplications/sudachi.rs/) japanese sentences  along the way. Thus I need to retreive the current sentence.
While this seemed like an ideal usecase for treesitter, I have failed to find a grammar for prose or a lua api for that (I ma have missed something), one can use the textobject "as" though in japanese/asian it's a bit tricker since the final dot `.` is not but `。` (same problem with `！ / ？`), which is ignored by neovim.

For instance, with the cursor on first character, pressing `)` moves cursor to next line instead of stopping after `。`:
```
このマークは、国くにのルールを守まもっているおもちゃにつけます。 3歳さいまでの子こどものおもちゃは、このマークがついていないと、売うることができません
```

I have started patching src/nvim/textobject.c to support `。`. I think it makes sense to support this natively but before I invest more time in a proper patch I wonder:
- why this isn't already the case considering the big japanese vim community already ?
- can this be considered a breaking change ? I doubt plugins rely on east-asian dots being ignored to select text. Even then, I would venture it's worth breaking
- what about prose text-objects as tree-sitter-grammar since text-ojects can depend upon languages etc. More as a roadmap though, in a first step modifying src/nvim/textobject.c looks good enough

related:
https://github.com/neovim/neovim/issues/8544
https://github.com/neovim/neovim/issues/22740
https://www.reddit.com/r/neovim/comments/1qim6dt/is_there_a_sentence_text_object_that_doesnt_stop/

### Expected behavior

pressing `)` should take into account the ` ` final dot and use it to differentiate between  sentences .

---

## #37512: treesitter: flicker when scroll in file contain many injection regions

**Labels:** needs:response, treesitter

## Problem

## Steps to reproduce

Flicker on scroll
```sh
yes | head -n 100 | sed 's/.*/vim.cmd[[noremap <silent> <buffer> <CR> <C-\\\\><C-N>:call <SID>CR()<CR>]]/' > repro.lua
VIMRUNTIME=runtime build/bin/nvim --clean repro.lua
```
Related: https://github.com/neovim/neovim/issues/32660

https://github.com/user-attachments/assets/0f89d205-772b-4492-a37d-d1b5e1375ca1

## Expected behavior
No flicker on scroll.

## System info

- Nvim version (nvim -v): `v0.12.0-dev-2086 gc39d18ee93` neovim/neovim@c39d18ee93
- Vim (not Nvim) behaves the same?: ?
- Operating system/version: Linux 6.18.5-zen1-1-zen
- Terminal name/version: kitty
- $TERM environment variable: `xterm-kitty`
- Installation: ?

---

## #37447: extmarks: terminal highlight is hidden when insert extmark with `virt_text_pos=inline`

**Labels:** terminal, display, marks

## Problem

## Steps to reproduce

```lua
local api = vim.api
vim.cmd.terminal([[printf "\033[32mGREEN\033[0m\n"]])
-- this is ok
-- api.nvim_buf_set_lines(0, 0, -1, false, { 'GREEN' })
-- vim.cmd.match('Added /.*/')
vim.defer_fn(function()
  local ns = api.nvim_create_namespace('highlight')
  api.nvim_buf_set_extmark(0, ns, 0, 0, {
    virt_text_pos = 'inline',
    virt_text = { { 'abc', 'Error' } },
  })
end, 100)
```

<img width="644" height="168" alt="Image" src="https://github.com/user-attachments/assets/2714a262-4a3f-49f3-819d-bdd28c7f0a8a" />

## Expected behavior
"GREEN" should be all green after "abc" is inserted at begin of line.

## System info

- Nvim version (nvim -v): `v0.12.0-dev-2049 gdde914f926` neovim/neovim@dde914f926
- Vim (not Nvim) behaves the same?: ?
- Operating system/version: Linux 6.18.4-zen1-1-zen
- Terminal name/version: kitty
- $TERM environment variable: `xterm-kitty`
- Installation: ?

---

## #37423: `:trust /path/to/file` to trust non-current buffer

**Labels:** security, editor-state, editor

## Problem

When `vim.secure.read()` prompts about an untrusted file (e.g., `.nvim.lua` via `exrc`, or `.lazy.lua` via lazy.nvim), the user must:

1. Choose `(v)iew` to open the file
2. Ensure they are in the correct buffer
3. Run `:trust`

The `:trust` command trusts the **current buffer**, not the file that triggered the prompt. This creates UX friction because:

- Users may accidentally trust the wrong file if they switch buffers
- The workflow is unnecessarily cumbersome

## Current Behavior

```
exrc: Found untrusted code. To enable it, choose (v)iew then run `:trust`:
/path/to/.nvim.lua
(i)gnore, (v)iew, (d)eny:
```

After choosing `(v)iew`:
- The file opens in a split
- User must manually verify they're in the correct buffer
- `:trust` only works on the current buffer

If the user runs `:trust` in the wrong buffer (e.g., the original file they were editing), they trust the wrong file.

## Expected Behavior

Option A: `:trust` should trust the file that triggered the prompt, regardless of current buffer.

Option B: Allow `:trust /path/to/file` syntax for `allow` action, so users can explicitly specify which file to trust.

Currently, `vim.secure.trust({action="allow", path=...})` throws an error:
```lua
assert(not path, '"path" is not valid when action is "allow"')
```

## Security Considerations

In [Discussion #27627](https://github.com/neovim/neovim/discussions/27627), it was mentioned that trusting non-current files is not allowed for security reasons (e.g., a malicious process may change content while typing the command).

I'd like to offer some thoughts on this:

1. **Hash-based trust already provides protection**: The trust database stores SHA256 hashes. If a file is modified after trusting, the hash won't match on next load, and Neovim will prompt again.

2. **Allowing path specification could be equally safe**: The hash would still be computed at the moment of trust, providing the same protection as the current buffer-based approach.

3. **Current UX risk**: Users may accidentally trust the wrong file by running `:trust` in the wrong buffer, which could be a greater practical risk.

4. **API consistency**: `vim.secure.trust({action="deny", path=...})` allows specifying a path. Allowing the same for `allow` would make the API more consistent.

## Steps to Reproduce

1. Enable `exrc` or use lazy.nvim with `local_spec = true`
2. Create a `.nvim.lua` or `.lazy.lua` file in a project directory
3. Open Neovim in that directory
4. When prompted, choose `(v)iew`
5. Switch to a different buffer (e.g., `:b#`)
6. Run `:trust`
7. **Result**: The wrong file is trusted

## Proposed Solution

Modify `vim/secure.lua` to:

1. Remove the restriction on `path` parameter for `allow` action
2. Or, store the "pending trust" file path when the prompt is shown, and have `:trust` (without arguments) trust that file

```lua
-- Current:
if action == 'allow' then
    assert(not path, '"path" is not valid when action is "allow"')
end

-- Proposed:
-- Remove th

*[truncated]*

---

## #37388: difftool: closing the quickfix window resets the current quickfix list

**Labels:** plugin, complexity:low, diff

### Problem

My first instinct when using this tool on my small laptop display is to find a
file i want to look at in the quickfix window, hit enter on it to diff it and close the qf
window so I have more display real estate to view the diff windows vertically.  That use
pattern is not currently supported. What happens is:

When closing the quickfix window opened by the plugin, the autocmds created by the plugin
are deleted and an empty list is added to the quickfix history (`:h :chistory`). Despite
the original quickfix list generated still technically being available (via `:colder`),
this effectively ends the usefulness of that list because the `BufWinEnter` autocmd was
what triggered the file diffing when navigating the list.  After that it just becomes an
ordinary quickfix list, i.e. `:cnext` just shows the file.

This is intentional.  However does it need to be?  Perhaps it is for the sake of cleanup?

If you drop the `WinClosed` autocmd that is on the quickfix window (it was calling the
`cleanup_layout` function and also closing the left diff window) and remove all code
referencing `layout.qf_win` inside `cleanup_layout`, then that quickfix list remains functional
when closing and reopening the qf window--at least until one of the diff windows is closed
(which also does the cleanup).  Maybe there is a use case where this would cause a problem?

### Expected behavior

Closing the quickfix window has no effect on the functioning of the difftool.

---

## #37382: user docs HTML: lua-guide.txt

**Labels:** documentation

`gen_help_html.lua` problem at: https://neovim.io/doc/user/lua-guide.html

Context:

All the "See Also:" hyperlink tags point to the same location; pointing to the "See Also:" in the "Using Lua" section.
```
TODO
```

---

## #37371: `%!` does not work with `nushell`

**Labels:** environment

### Problem

Nushell does not support file piping with the `<` and `>` syntax,
The error from `vim` as its more verbose:
```nu
Error: nu::parser::operator_incompatible_types

  × Types 'bool' and 'string' are not compatible for the '>' operator.
   ╭─[source:1:1]
 1 │ (echo) < /tmp/voDJjHe/2 > /tmp/voDJjHe/3
   · ───────────┬─────────── ┬ ───────┬──────
   ·            │            │        ╰── string
   ·            │            ╰── does not operate between 'bool' and 'string'
   ·            ╰── bool
   ╰────


shell returned 1

E485: Can't read file /tmp/voDJjHe/3
```

From `neovim`
```nu
shell returned 1                                                                                                        
                                                                                                                        
E485: Can't read file /tmp/nvim.road/LpnbeO/1  
```

### Steps to reproduce

use nushell
start neovim with any file 
then try `:%!echo`

### Nvim version (nvim -v)

NVIM v0.11.5 Build type: MinSizeRel LuaJIT 2.1.1723681758

### Vim (not Nvim) behaves the same?

yes, vim 9.1.2072

### Operating system/version

linux

---

## #37317: `BufModifiedSet` does not get triggered when 'modified' is manually set.

**Labels:** needs:decision, events, options

### Problem

The event 'BufModifiedSet' does not trigger any autocommands when a buffer's `modified` option is manually set, be that through `:se`, `:let &modified`, or `vim.bo.modified`. It only fires in the scenarios that set `modified` described under `:h 'modified'`.

I guess this isn't necessarily unreasonable behaviour depending on how you look at it, however the manual would make you think that it should trigger regardless of how  the value was changed (also, I wonder, is the idea that it fires when the value actually changes, or when the option is set in general even if it the same value?).

`:h BufModifiedSet`:
> After the `'modified'` value of a buffer has been changed.

This seems not related to https://github.com/neovim/neovim/issues/32817, as getting the buffer to redraw does not cause the autocommand to do a delayed trigger.

### Steps to reproduce

1. Launch nvim with `nvim --clean`
2. `lua vim.api.nvim_create_autocmd("BufModifiedSet", { callback = function() print(os.date()) end })`
3. Manually change the value of the buffer's 'modified' option, e.g. `:set modified`
4. The autocommand will not trigger.

### Expected behavior

The autocommand should trigger regardless of how 'modified' was changed (or perhaps the manual should clarify that explicitly setting it won't cause an event?)

### Nvim version (nvim -v)

0.11.5

### Vim (not Nvim) behaves the same?

n/a

### Operating system/version

NixOS 26.05 (Yarara) x86_64

### Terminal name/version

Kitty 0.44.0

### $TERM environment variable

xterm-kitty

### Installation

nixpkgs-unstable (commit 418468ac9527e799809c900eda37cbff999199b6; issue is reproducible in both neovim and neovim-unwrapped packages)

---

## #37308: :terminal has inconsistent 'modified' behaviour

**Labels:** terminal, options

### Problem

Per the neovim-manual:

`:h terminal-emulator`:
> Terminal buffers behave like normal buffers, except:
> - With 'modifiable', lines can be edited but not deleted.
> - 'scrollback' controls how many lines are kept.
> - Output is followed ("tailed") if cursor is on the last line.
> - 'modified' is the default. You can set 'nomodified' to avoid a warning when
>   closing the terminal buffer.
> - 'bufhidden' defaults to "hide".

However, the buffer is treated as modified by certain parts of neovim, but as not modified by others. Running `:setlocal modified? ` in the terminal-buffer right after opening it will show `nomodified`; similarly `nvim_get_option_value()` and `vim.fn.getbufinfo()` will report the flag as being set to false. . Additionally, trying to change the value of `modified` seems to have no effect, whether done through `:set(local)` or   `nvim_set_option_value()` and it will remain on `nomodified` (and as far as I can tell, this isn't a visual issue and the value actually doesn't change internally). Despite this, calling `getbufinfo` with `bufmodified = 1` will still return a result that includes any terminal buffers (eventhough their `changed` entry is set to 0). Furthermore,  using `:bd` on the terminal buffer will trigger a warning (eventhough it shouldn't when `nomodified` is set, according to the manual), but `:q` will  not when the terminal-buffer is the only window.

Additionally, running `:setlocal bufhidden?` in a terminal buffer right after opening it shows it to be empty, even though it should be set to `hide` according to the manual. It is possible to manually change this value without issue and neovim seems to treat it properly.

As far as I can tell, there are no issues with the other options listed in `:h terminal-emulator` nor in `:h terminal-config`.

### Steps to reproduce

1. Start with `nvim --clean`
2. Open a terminal buffer with `:term`.
3. `:setlocal bufhidden` will result in an empty value.
4. `:setlocal modified?` will result in `nomodified`.
5. `:setlocal modified | setlocal modified?` will results in `nomodified`
6. `:echo getbufinfo({'bufmodified': 1})` will include the terminal buffer in its results.
7. `:bd` will trigger a warning and not close the buffer.
8. `:q` will close the terminal's buffer-window.

### Expected behavior

- When opening a terminal window, the default value of `modified` should be `modified`, not `nomodified`, and for `bufhidden` it should be `hide`, not empty.
- Setting the value of `modified` in a terminal-buffer should have an effect and alter its value, but doesn`t.
- Neovim should consistently treat the `modified` value of a terminal buffer. E.g. closing a terminal buffer should not emit a warning when `modified` is set to `nomodified`, and `getbufinfo({'bufmodified': 1'})` should not include terminal buffers when their `modified` option is set to `nomodified`.

### Nvim version (nvim -v)

0.11.5

### Vim (not Nvim) behaves the same?

n/a

### Operating system/version

*[truncated]*

---

## #37293: Allow accessing utf8proc library from FFI in Windows

**Labels:** build, platform:windows, lua, core

### Problem

Currently, I cannot use FFI to call utf8proc functions on Windows, even though that works on Linux and MacOS builds of Nvim. This is my code
```lua
local ffi = require("ffi")

ffi.cdef [[
	typedef int utf8proc_ssize_t;

	typedef enum {
		UTF8PROC_COMPOSE = (1<<3),
		UTF8PROC_IGNORE = (1<<5)
	} utf8proc_option_t;

	typedef unsigned char utf8proc_uint8_t;

	utf8proc_ssize_t utf8proc_map(
		const utf8proc_uint8_t *str, utf8proc_ssize_t strlen, utf8proc_uint8_t **dstptr, utf8proc_option_t options
	);

	void free(void *ptr);
]]

local flags = ffi.C.UTF8PROC_COMPOSE + ffi.C.UTF8PROC_IGNORE

function utf8_normalize(str)
    local out = ffi.new("utf8proc_uint8_t*[1]")

    local rc = ffi.C.utf8proc_map(
        ffi.cast("const utf8proc_uint8_t*", str),
        #str, out, flags
    )

    if rc < 0 then
        return nil, rc
    end

    local res = ffi.string(out[0], rc)
    ffi.C.free(out[0])
    return res
end
```
When I call function `utf8_normalize()`, it will give error `cannot resolve symbol 'utf8proc_map': The specified procedure could not be found.`. I know that FFI usage of internal functions is not officially support, but given that there have been some works on it like #15999, I would expect this to work as well

### Expected behavior

FFI calls to utf8proc to work on Windows, like on MacOS and Linux

---
