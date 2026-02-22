# tracking issue

**Parent:** Neovim — Project Ideas
**Source:** https://github.com/neovim/neovim/issues/9421
**Scraped:** 2026-02-22T23:28:47.616717

---

## UI extension work (tracking issue)

**Labels:** ui, ui-extensibility

Tracking/discussion issue for planned UI enhancements. NB: being mentioned on the list below is not a guarantee for being done at any specific time scale, nor is the order necessarily indicative of readiness/priority (except perhaps for the smaller follow-up items for multigrid, which I hope to get done pretty soon). Feel free to add stuff.

- [x] multigrid (#8455 **merged**)
  - [x] improve size handling: non-screen functions should use requested size, not grid allocated size.
  - [x] `:term` sizing issues (fix `terminal_resize`)
  - [x] mouse support (#9429)
  - [ ] messages on dedicated grid (when not `ext_messages`)
- [x] floating windows (#6619)
  - [x] for `!ext_popupmenu`: pum as float (#9530)
  - [x] for `ext_popupmenu`: add tests for grid anchoring 
  - [x] `nvim_win_close` to close window by id.
  - [x] Ex-commands for floats (#9663)
      - [ ] #9920
  - [x] `pumblend` but for floats (because why not)
- [x] `ext_messages` (#7466)
- [ ] `ext_windows`: UI control of layout and wincmds (#8707)
- [x]  use `ext_popupmenu` events for wildmenu to support info and pum (#9607) 
- [ ] `ext_statusline` (I have some ideas/pre-WIP code...)
- [ ] external columns (number, signs) by transmitting `wline_T` info (no work done)
- [ ] "tabgrid" (#7541 but with multigrid)
- [x] transmit UI highlight definitions for `ext_popupmenu` using `hl-Pmenu`, etc. (#10504)
    - [x] ensure that we always use concrete rgb colors for `default_colors_set`
    - [ ] allow subscribing non-default groups
- [x] UI control of `ext_popupmenu` #9445 
    - [ ] For `ext_cmdline` maybe `nvim_call_function('setcmdpos')` already works (check + add docs/test)

