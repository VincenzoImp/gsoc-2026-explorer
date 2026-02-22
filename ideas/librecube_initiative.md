# LibreCube Initiative — Project Ideas

**Source:** https://librecube.org/google-summer-of-code/
**Scraped:** 2026-02-22T23:28:47.621369

---

LibreCube is applying for the [Google Summer of Code](https://summerofcode.withgoogle.com) (GSoC) program this year!

GSoC is a vital opportunity for attracting new members to the LibreCube community and the open source world in general. We heavily rely on contributors to extend our open source ecosystem for semi-autonomous exploration systems and technology. Listed below are the project ideas for this year. Please send us an email ([info@librecube.org](mailto:info@librecube.org)) with a short text about yourself (your skills and interests) and what of the project(s) you find interesting to work on. You may want to structure your project application according to [this template](/ideas/librecube-initiative/google-summer-of-code-proposal).

**Notes:**

- As always, we aim for a
**diverse participation**and encourage applications from women and under-represented groups! - Most projects require at least a basic knowledge of Python language. Basic experience with Git is also needed.
- We do not restrict the use of AI tooling for code generation. However, we strongly encourage to build the code step by step, and will expect you to explain what you are coding.

#### 1. SpaceCAN Tester

**Description**: [SpaceCAN](https://librecube.gitlab.io/standards/spacecan/) is the robust onboard communication bus for CubeSats and other autonomous vehicles, developed by the LibreCube community. Currently we have a reference implementation in Python and an embedded version in MicroPython. A SpaceCAN network is composed of a controller node and several attached responder nodes. To help during the development of responder nodes, we developed the [SpaceCAN Tester](https://gitlab.com/librecube/elements/LC3301) application.The task here is to improve this application with several features, to improve the user experience and to extend its capabilities. The list of features to add can be found [here](https://gitlab.com/librecube/elements/LC3301/-/issues).

**Skills**: Python, Web Framework (NiceGUI)

**Proposed Mentors**: Peter, Shayan

**Project Size**: 350 hours

**Difficulty**: medium

#### 2. ZED PLUTO Language Plugin

**Description**: [PLUTO](https://ecss.nl/standard/ecss-e-st-70-32c-test-and-operations-procedure-language/) is a domain specific language for writing procedures to be used for test and operation of space system. PLUTO procedures are both human-readable and can be parsed by machines (for example, we have developed a [PLUTO to Python parser](https://gitlab.com/librecube/prototypes/python-pluto-parser) to demonstrate it). The goal here is to create a language support plugin for the [ZED editor](https://zed.dev/) to support syntax highlighting and code formatting. This will greatly assist in writing PLUTO procedures. Previously we had developed a [plugin](https://gitlab.com/librecube/tools/vscodium-pluto-syntax) for VS Code, which can serve as a guideline.

**Skills**: Python, PLUTO

**Proposed Mentors**: Sai, Artur

**Project Size**: 90 hours

**Difficulty**: easy

#### 3. Blockly PLUTO Procedure Editor

**Description**: In a previous GSoC project, we developed a [blockly-based application](https://developers.google.com/blockly) to support the creation of [PLUTO](https://ecss.nl/standard/ecss-e-st-70-32c-test-and-operations-procedure-language/) procedures using block programming. A demo of the application can be found [here](https://lc6401-5e3d9b.gitlab.io/#). PLUTO is predominantly used in European space missions. This application is targeted for students and engineers of space mission automation. It provides them an easy-to-use tool to create valid PLUTO procedures. The task here is to improve the editor in a number of ways. Some improvements pertain to the improvement of user experience. The bulk of improvements however concern the implementation of missing functionalities, which are listed [here](https://gitlab.com/librecube/elements/LC6401/-/issues).

**Skills**: JavaScript, Blockly, Docker

**Proposed Mentors**: Artur, Sai

**Project Size**: 350 hours

**Difficulty**: medium/hard

#### 4. CC1120 GNU Radio Receiver & Decoder

**Description**: LibreCube is developing an [UHF CubeSat communications board](https://gitlab.com/librecube/prototypes/proto-LC2302). This project will complement this activity by creating GNU Radio flowgraphs (and an optional small OOT module) to receive, demodulate, and decode TI CC1120 packets from provided baseband IQ recording, no hardware setup needed. The work will take inspiration from the existing CC1101 GNU Radio decoder (gr-cc_sdr, gr-satellites) and adapt it for CC1120 packet formats. Deliverables include working flowgraphs, packet/frame decoding, examples and clear documentation with sample datasets.

**Skills**: C++, GNU Radio, Signal Processing

**Proposed Mentors**: Tamara, Shayan

**Project Size**: 350 hours

**Difficulty**: hard
