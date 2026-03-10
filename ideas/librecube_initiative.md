# LibreCube Initiative — Project Ideas

**Source:** https://librecube.org/google-summer-of-code/
**Scraped:** 2026-03-10T16:58:40.236891

---

LibreCube is applying for the [Google Summer of Code](https://summerofcode.withgoogle.com) (GSoC) program this year!

GSoC is a vital opportunity for attracting new members to the LibreCube community and the open source world in general. We heavily rely on contributors to extend our open source ecosystem for semi-autonomous exploration systems and technology. Listed below are the project ideas for this year. Please email directly to the mentors (with [gsoc@librecube.org](mailto:gsoc@librecube.org) in copy), with a short text about yourself (your skills and interests) and what of the project(s) you find interesting to work on. You may want to structure your project application according to [this template](/ideas/librecube-initiative/google-summer-of-code-proposal). Also, have a look at a [previous application](https://github.com/ShayanMajumder/GSoC-2021-Proposal).

**Please note:**

- As always, we aim for a
**diverse audience**and encourage applications from women and under-represented groups! - The idea of GSoC is to engage people in open-source development.
- Most projects require at least a basic knowledge of Python language. Basic experience with Git is also needed.
- We do not restrict the use of AI tooling for code generation. However, you must disclose that you used AI and you must have
**understood**the generated code! If you submit a merge request that you cannot explain how it works, you will not be considered further for this program.

#### 1. SpaceCAN Tester

**Description**: [SpaceCAN](https://librecube.gitlab.io/standards/spacecan/) is the robust onboard communication bus for CubeSats and other autonomous vehicles, developed by the LibreCube community. Currently we have a reference implementation in Python and an embedded version in MicroPython. A SpaceCAN network is composed of a controller node and several attached responder nodes. To help during the development of responder nodes, we developed the [SpaceCAN Tester](https://gitlab.com/librecube/elements/LC3301) application.The task here is to improve this application with several features, to improve the user experience and to extend its capabilities. The list of features to add can be found [here](https://gitlab.com/librecube/elements/LC3301/-/issues). In addition, a responder node shall be created with [rust-spacecan](https://gitlab.com/librecube/prototypes/rust-spacecan) using STM32 microcontrollers.

**Skills**: Python, Web Framework (NiceGUI)

**Proposed Mentors**: Peter ([peter@librecube.org](mailto:peter.mader@librecube.org)), Artur ([artur@librecube.org](mailto:artur@librecube.org))

**Project Size**: 350 hours

**Difficulty**: medium

#### 2. ZED PLUTO Language Plugin

**Description**: [PLUTO](https://ecss.nl/standard/ecss-e-st-70-32c-test-and-operations-procedure-language/) is a domain specific language for writing procedures to be used for test and operation of space system. PLUTO procedures are both human-readable and can be parsed by machines (for example, we have developed a [PLUTO to Python parser](https://gitlab.com/librecube/lib/python-pluto-parser) to demonstrate it). The goal here is to create a [language support plugin](https://zed.dev/docs/extensions/languages?highlight=markdown) for the [ZED editor](https://zed.dev/) to support syntax highlighting and code formatting. This will greatly assist in writing PLUTO procedures. Previously we had developed a [plugin](https://gitlab.com/librecube/tools/vscodium-pluto-syntax) for VS Code, which can serve as a guideline.

**Skills**: Python, PLUTO

**Proposed Mentors**: Sai

**Project Size**: 90 hours

**Difficulty**: easy

#### 3. Blockly PLUTO Procedure Editor

**Description**: In a previous GSoC project, we developed a [blockly-based application](https://developers.google.com/blockly) to support the creation of [PLUTO](https://ecss.nl/standard/ecss-e-st-70-32c-test-and-operations-procedure-language/) procedures using block programming. A demo of the application can be found [here](https://lc6401-5e3d9b.gitlab.io/). PLUTO is predominantly used in European space missions. This application is targeted for students and engineers of space mission automation. It provides them an easy-to-use tool to create valid PLUTO procedures. The task here is to improve the editor in a number of ways. Most importantly, the activity and value references, which are currently defined as free text in the blocks input fields, should be instead come from a database and be presented as pull-down menu. The database should be an [XTCE](https://www.omg.org/xtce/) file. Further improvements concern the implementation of other missing functionalities, which are listed [here](https://gitlab.com/librecube/elements/LC6401/-/issues).

**Skills**: JavaScript, Blockly, Docker

**Proposed Mentors**: Artur ([artur@librecube.org](mailto:artur@librecube.org))

**Project Size**: 350 hours

**Difficulty**: medium/hard

#### 4. CCSDS GNU Radio Receiver & Decoder

**Description**: LibreCube is developing an [UHF CubeSat communications board](https://gitlab.com/librecube/prototypes/proto-LC2302). This project will complement this activity by creating a lab-style ground station, utilizing SDR and GNU Radio flowgraphs (and an optional small OOT module) to receive, demodulate, and decode CCSDS packets. Data can come from real SDR and from provided baseband IQ recording. The work will take inspiration from the existing CCSDS GNU Radio decoder (gr-cc_sdr, gr-satellites, gr-ccsds). Deliverables include working flowgraphs, packet/frame decoding, examples and clear documentation with sample datasets.

**Skills**: C++, GNU Radio, Signal Processing

**Proposed Mentors**: Tamara ([tamara@librecube.org](mailto:tamara@librecube.org)), Shayan ([shayan@librecube.org](mailto:shayan@librecube.org))

**Project Size**: 350 hours

**Difficulty**: hard

#### 5. GNU Radio LoRa Receiver with Optional TinyGS / LoRaWAN Integration

**Description**: This project focuses on creating an SDR-based ground station receiver using GNU Radio capable of receiving and demodulating LoRa satellite signals with standard SDR hardware. The receiver will allow conventional SDR ground stations to decode LoRa packets and optionally forward them to networks such as [TinyGS](https://tinygs.com) or [LoRaWAN](https://lora-alliance.org/about-lorawan/) infrastructure. The work will build on existing GNU Radio LoRa implementations and produce reusable flowgraphs, optional modules, and clear documentation.

**Skills**: C++, GNU Radio, Signal Processing

**Proposed Mentors**: Shayan ([shayan@librecube.org](mailto:shayan@librecube.org))

**Project Size**: 350 hours

**Difficulty**: hard
