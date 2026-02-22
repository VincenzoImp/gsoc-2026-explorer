# #7438

**Parent:** Neovim — Project Ideas
**Source:** https://github.com/neovim/neovim/issues/7438
**Scraped:** 2026-02-22T23:28:47.616779

---

## dynamic --headless, nvim_ui_builtin()

**Labels:** ui, tui, ui-extensibility, remote

I would like to request a vimscript function or api function that should negate the effect of the `--headless` command line switch. Lets call it `nvim_launch_builtin_tui()` for now. I imagine something like this:
```vim
if My_condition()
  call nvim_launch_builtin_tui()
  " now it looks as if we did start nvim without --headless
else
  " this text will go directly to stdout
  echo "running headless"
endif'
```
and then one would do `nvim --headless -S above-file.vim`. Depending on the user function `My_condition` one would effectively end up in a "normal" TUI nvim instance or in a headless nvim.

If I can express the logic of the `My_condition()` vimscript function in the `my_condition` shell command/function I can currently do something similar with this shell script:
```sh
if my_condition; then
  # this now *is* a nvim without --headless
  nvim
else
  # this text will go directly to stdout
  nvim --headless --cmd 'echo "running headless"'
fi
```


