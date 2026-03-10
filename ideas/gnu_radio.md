# GNU Radio — Project Ideas

**Source:** https://wiki.gnuradio.org/index.php/GSoCIdeas
**Scraped:** 2026-03-10T16:58:40.242632

---

# GSoCIdeas

[Jump to navigation](https://wiki.gnuradio.org#mw-head)

[Jump to search](https://wiki.gnuradio.org#searchInput)

Note- also check out [Grant Ideas](https://wiki.gnuradio.org/index.php?title=Grant_Ideas) for additional ideas that are more suited towards grant money than GSoC.

This is the list of project ideas for the summer of code 2026 within GNU Radio.

Remember that these are **ideas** and are merely meant as an inspiration for you to write your own proposal.

## Bringing Your Own Project Idea

Students who do not find a fit among these projects are encouraged to engage with us and suggest new ones. The [GNU Radio discussion mailing list](https://wiki.gnuradio.org/index.php?title=MailingLists) is the best place to contact all of us. Please do not contact us off-list for the sake of discussing the summer of code, unless you're contacting a mentor listed here to get feedback on a proposal.

Reviewing the [Google GSoC FAQ](https://developers.google.com/open-source/gsoc/faq) page for a broader understanding of project, mentor, and student responsibilities is recommended.

If you need a USRP or other radio hardware to complete the project, we will be able to arrange something.

Please add ideas to this list (you may cannibalize old ideas, of course!).

Guidelines for good projects (when suggesting projects, please consider these):

- Clearly defined scope, with a main target that can be done in 3 months
- Clear benefits for the GNU Radio project
- Not specific to a certain hardware. No specific embedded devices, either, please.
- Both OOTs and in-tree improvements are welcome





## Graphical interoperability between CyberEther and GNU Radio

The [CyberEther](https://github.com/luigifcruz/CyberEther) project comes with some neat graphical sinks that would be great to have access to in GNU Radio. This project entails creating a new CyberEther GUI workflow much like the [gr-bokehgui](https://github.com/gnuradio/gr-bokehgui) project, such that users can create flowgraphs with CyberEther sinks. This would allow the user to visualize GNU Radio data streams in one of the high-performance CyberEther plots (lineplot, waterfall, spectrogram, etc).

**Prerequisites**

- Knowledge of C++ and some Python
- Familiarity with graphical APIs (OpenGL, Vulkan, Metal)
- Basic Qt understanding

**Outcome**

- OOT module with CyberEther sinks
- Support for both GNU Radio main branch and 3.10?

**Project length**

Long (350 hours)

**Difficulty**

Medium

**Mentor(s)**

Luigi Cruz, Håkon Vågsether



## GNU Radio 4 signal processing server for MaiaSDR

The [MaiaSDR](https://maia-sdr.org/) project presents a modern web UI that would be great if it can be used with GNU Radio 4. This project entails creating a new signal processing server with GNU Radio 4 that provides the pre-processing and API to serve data to the MaiaSDR web frontend. The result may be very similar to what [gr-fosphor](https://github.com/osmocom/gr-fosphor) provides today with a spectrum plot, a history plot, and a waterfall plot. Depending of the target scope, additional features may be added.

**Prerequisites**

- Knowledge of C++ and Rust
- Basic knowledge of server and client interaction
- Basic Qt understanding

**Outcome**

- A full server to provide data to the MaiaSDR wasm frontend
- Updated controls to stream from multiple hardware sources as well as a file source.
- Updated reasonable controls

**Project length**

Small (90 hours) - Medium (175 hours)

**Difficulty**

Easy - Medium

**Mentor(s)**

Johannes Sterz Demel, Daniel Estévez

## Hardware in the loop CI

Current GNU Radio CI tests are software only, but real live usage usually involves hardware, and real over the air operations. It would be useful to have tests that run over actual hardware, with radio transmissions. The CorteXlab platform would host these, to have an isolated radio environment free of interference.

The idea is to define a set of relevant scenarios to test, as well as metrics for pass/fail criterion. And to implement them as flowgraphs that can run in CorteXlab. A final step would be to build the pipeline to automate these tests, triggered as GitHub actions.

**Prerequisites**

- Knowledge of DSP, and some Python/C++

**Outcome**

- Test scenarios definition, tests flowgraphs, automated CI pipeling

**Project length**

175 hours

**Difficulty**

Medium

**Mentor(s)**

Cyrille Morin, ?

## BokehGUI in GNU Radio 4.

gr-bokehgui is an OOT module (created by a previous GSoC project) allowing remote and browser-based monitoring of running flowgraphs.

The idea is to make a similar module for GNU Radio 4.0, either with the Bokeh library, or another one that could provide this remote plotting and interaction capability.

**Prerequisites**

- Knowledge of C++ and Python
- Some knowledge of DSP

**Outcome**

- OOT module with remote, browser-based plotting and widgets for interaction.

**Project length**

350 hours

**Difficulty**

Medium

**Mentor(s)**

Cyrille Morin, ?

## Old Ideas

Feel free to browse [old ideas](https://wiki.gnuradio.org/index.php?title=OldGSoCIdeas) from previous years for inspiration.
