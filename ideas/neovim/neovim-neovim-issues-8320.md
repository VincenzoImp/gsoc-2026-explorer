# GSOC project

**Parent:** Neovim — Project Ideas
**Source:** https://github.com/neovim/neovim/issues/8320
**Scraped:** 2026-02-22T23:28:47.616658

---

## Plan for extending the UI protocol and externalizing window layout and control

**Labels:** ui-extensibility, gsoc

Hi, I am excited to be working with Neovim for the following 3 months as a [GSoC student](https://summerofcode.withgoogle.com/projects/#5530001420582912) for the project mentioned in the title with @bfredl as my mentor. Here is a plan that we decided on for the same:

## First Evaluation (Jun 11)

- Split the windows internally into separate grids. Neovim still manages window layout and all window commands (`:wincmd ...`).
- Add API for the external UI to get/set window grid sizes. This will allow windows with different font size, even if the overall layout remains fixed.
- Implementation of the client side of this API in the `screen.lua` module of the test suite, and preferably also in a GUI such as the `python-gui`.


## Second Evaluation (Jul 09)

- Finalize the API described in the first step with documentation and examples.
Design the API for embedders to take control of window commands, and start work on the implementation.
- Externalize cursorline highlighting (ideally, as first example of a general abstraction for highlighting overlays).
- Externalize relativenumber (optional).


## Final Evaluation (Aug 06)

- Complete the implementation of an API that give embedders full control of window layout and interpreting window commands. The embedders can subscribe to and receive events for individual windows.
- Complete the working prototype of this API in a GUI.


Any suggestions, improvements and/or comments are welcome and encouraged. _Let's have a great summer of code!_

