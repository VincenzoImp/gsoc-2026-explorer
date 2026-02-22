# Open Robotics — Project Ideas

**Source:** https://github.com/osrf/osrf_wiki/wiki/GSoC-2026
**Scraped:** 2026-02-22T23:28:47.604610

---

# Overview
This document describes a list of potential ideas created for the [2026 Google Summer of Code](https://summerofcode.withgoogle.com/). However, the ideas are open to everyone with interest on collaborating, and OSRF is open to new ideas. Feel free to use our application template below to indicate your interest in some of the projects. If you would like to suggest new projects please email [gsoc@openrobotics.org](mailto:gsoc@openrobotics.org).

The following list shows a set of ideas that can extend the functionality of some of the open source projects led by OSRF.

ROS (Robot Operating System) provides libraries and tools to help software developers create robot applications. It provides hardware abstraction, device drivers, libraries, visualizers, message-passing, package management, and more.

Gazebo is a multi-robot simulator for indoor and outdoor environments. It is capable of simulating a population of robots, sensors and objects in a three-dimensional world. It generates both realistic sensor feedback and interactions between physically plausible objects.

Open-RMF is a free, open source, modular software system that enables robotic system interoperability. Open-RMF coordinates multiple fleets of indoor and outdoor robots with typical robotic use cases and integrates them with elevators/lifts, doors and other infrastructure.

Infrastructure is the computing infrastructure that supports the above projects, such as by providing continuous integration services and building binary packages.

The link between all projects is their open source nature and its relationship with robotics. Browse through the list and do not hesitate to contact us if you wish to participate in any of the projects. Share with us your thoughts and ideas on any future improvement or project you may have.

# Template

### Title
Prerequisites: 

Necessary programming skills: 

Potential mentors: [Mentor and Info](https://github.com/fujitatomoya)

Expected size: *expected number of hours*

Expected outcome: *one sentence description of outcome*

Detailed description: *paragraph description*

## ROS 2

## Gazebo

### Vendor Agnostic SONAR implementation
Prerequisites: Linux, Git, familiarity with ROS 2 and Gazebo, basic understanding of sonar and simulation pipelines.
Necessary programming skills: C++ (Gazebo / ROS 2 integration), Rust (or willingness to learn), CMake, ABI basics (FFI), CUDA GPGPU compute fundamentals.

Difficulty level: Medium to hard

Mentors: [Woen-Sug Choi](https://scholar.google.com/citations?user=9rpkxUwAAAAJ&hl=en), [Arjo Chakravarty](https://github.com/arjo129)

Expected size: 175 hours to 350 hours

Expected outcome: A source-buildable, distribution package providing a Gazebo sonar plugin with GPU acceleration that is vendor-agnostic (no CUDA dependency), using wgpu as the compute backend.

Detailed description:
This project develops a vendor-agnostic GPU-accelerated SONAR simulation plugin for Gazebo by migrating the current CUDA-centric approach to a wgpu-based compute pipeline. Current existing physics-based underwater sonar plugin rely on CUDA for speed, which limits users to NVIDIA GPUs and complicates deployment in mixed hardware environments (AMD/Intel/Apple Silicon GPUs, and future-proofed stacks). Recent advances in cross-platform GPU APIs and the Rust wgpu ecosystem make it feasible to run high-throughput compute workloads across Vulkan / DirectX / Metal backends via a unified abstraction to utilize GPGPU capabilities. This project uses that foundation to implement sonar image synthesis on the GPU without vendor lock-in, while keeping Gazebo/ROS 2 integration clean and upstream-friendly.

### QA of Reset of core systems

Prerequisites: Linux, Git, familiarity with ROS 2 and Gazebo, basic understanding of sonar and simulation pipelines.

Necessary programming skills: C++ (Gazebo / ROS 2 integration), CMake, ABI basics (FFI), CUDA GPGPU compute fundamentals.

Expected size: 175 hours 

Difficulty: Easy

Expected outcome: A comprehensive test suite and audit of all system resets in gazebo

Detailed description: Gazebo ships with a lot of core plugins out of the box. Initially these were implemented with Configure, PreUpdate, Update, and PostUpdate hooks for each time step. However, as reinforcement learning took off, reset was added as a core behavior. Many of these plugins may behave weirdly upon reset as we have not audited their behaviours. The goal is to have a test suite that covers all the core plugins and their reset behaviour so that we can catch oddities and regressions.



## ROS Control

### Mission Control for ros2_control

The ros2_control framework focuses on direct management of hardware and their controllers to enable real-time capabilities with ROS.
Although those interfaces are easy to use, they provide only "manual" control over the system's state.
Therefore, very often in more complex systems our users have to implement an external, state-machine like component that serves as an orchestrator for ros2_control.
The main purpose of such a component is to serve as conductor of ros2_control by taking care of scenarios and making sure that at the appropriate moment the right controllers and hardware are in expected states.

This functionality should replace some high-level components currently used, e.g., MoveIt2-"SimpleControllerManager".

The main functionalities for the components and goals of the project are:

* Defining a scenario in form of a multi-robot and multi-tool configuration and its behavior that serves as a benchmark.
* Extending controller_manager with status publisher, providing all needed data to a mission-control component.
* Adding status topics to all standard controllers.
* Defining format of a YAML file where users can configure controller presets.
* Implementing the mission-control module/script that sets the controller_manager, i.e., the ros2_control framework, in a specific configuration/state.
## Open-RMF

### UI/UX improvements to the [Crossflow Diagram Editor](https://open-rmf.github.io/crossflow/?diagram=3VhLb%2BM2EP4rhtCjGZMUKYm%2BF2gPPbVAD4uFwcfQVleWvHokGwT57x1K8isbO%2FJigwY9xSKHo%2Fk%2BznwzylP0S2M3sNXRMtq07a5ZLha1frhb5%2B2mM10Dta3KFsr2zlbbRbWDktRbv7B11TS%2BqB4WNfhmsQHtmsVW5%2BXC5Xpd6%2B3d4PXun6Yqo3l0D3WT469lRO%2FYHcWVFra7QrfQRMun53nUtLpucbvZFXmL29UubETfGKXhb%2Fu4A9wtKwe4abq8cFDjwrYr8LmEb%2BFsMCam8x635hHG7fN1tMTFeeRydKwfV%2B3RMgpv7bbXvGvnDt6f%2BvU2DxhaqLd5icEHHy9cB5e4%2Bk8VLA%2Bu%2B8fgOgSHyD69CBaf9g%2BfD3hGV7h3CwWvMfAaAT3%2Bnu2j8z37DXzt8M5zXexDHWKMPg%2FxHF5yPDouDPuXtwNh0Ng637VDPvxd1V9CIs3ajW5nfQDNrNvhI8w4KbutgXqWl7uunRV5085niLfN0QyaYLPFPZff567TRfE4nwWih435TJduhlc42rXVGvBHfYdQen8r%2BKYxB0MGfnp6EdUfx5cwHs%2FM4wxBo4sZ%2BggrmFOngQiZDDZ7E1xAC7xAzJP1Hk4NDR7BcEY3SZYEXu910QWKPqHfeTj5GVm8EFD%2FjhfR0BfBkEPEe5Ow8mY4BG3OosET4SBGgymJaQNlKOG%2BLA%2FlT8ZyJ%2BDytqrJPQvbG91s0EUMID1VRolEaMdErLkCby3LWEohcXGaAZd9OmP5YzXh0ZDew4XkDl0sV6ux7Fa9QqxWQTrGZO0lYx7tqiYfWEK9iJacy3n0iH9lSHAowLbaFHjA66IBTD%2Fdotjhm%2FQWmp22wVVI2y3opqsB3%2FoUPeSuRQQ8SMcG8vUGi0RSTN7vwzpowWloR4G4GF7ynvElUnGnvCOJ9pII4RwxKfOEm0xYTy3IWB%2BjHSXlRaC9bgYe%2B0BfjSrI9O%2FhfaNCVLt30%2BobCUiNSlNnE%2BJTxC4kZySzxmE%2BC6aN4ZiW%2FC0C9jclJxAQpPot%2FD%2FcTW7EHseUUUk5kWAsEVQLkjkniHE80zR1ACY9Yh870wXsYgL20cMZ%2BB%2FvdzeC5TQzaczxorMsRrBCEk2VIqBibTDTBcv8Wxcdy5sy%2FeZEn96RbwSfMdCSakawtikRFijRoCyRVolMSSGd60et8%2BZ%2B4arZlDQ%2FTGe3DQ23XmqsPGWJIrFIUb58IomhJg0algiwzAsfSul8tLgoYPFEATte0xm8k8nlFgzY6RjHDk9iVFsilPVEKZNgYibeSC54qk%2Fu5hKGfWpOxPBzIIR279anbdipNPZOWmIUQ0nheDUm0SmRLpEyppkAGocMqLq6D%2BrVtj3s%2FoZTWeh2ZVcUCF%2FXOHvckMq9%2FbmPra6%2FQP1r2WMaEeu6rh5sUTWIdH4EesTJKZIxGjvwGichNNwTXHUtDojDl0k%2FK5643ls%2Fn9Shy3SW%2BYxox1GEHNeouMgR94JR62LmetU40DOxPV8lbGqNfEjCLPdpJmIgArTC4LkkigOQJAWBZGEyMHNK2MR2fpWwyzPbh6QIG1dKneckSzKOjQ31SUFCCWZYYuMYsCDtKUUT8%2BEqRVMnh%2Fcg7KBcU%2FgajP%2BEr0PbiZbo1ENrN3%2F1%2B6hhRx32kCr85CDMCky1QKHOVEJSXDUGa5X2nz0HHifq9v%2BUR3aRR1T6VHPriEs8apxC4co0%2FrKGqVQqpTw%2FatZ0Dq7yOHWK%2F5AF7IwzPMDG5oUEZF6RjIMjaazxG5gnKfa1swKeNsleJWzq0PEhCUs0%2Fj%2BEUk2okwYrNcuIiWlCqM2YMSaW8lzxJo4MVwmb%2BqH8HoT1c%2FNQe98xNqraNOJonAonHCaNZBpBYEvVMlYkTaj0MmacUfaziZv63fXfEMeuE4cfJM%2FP%2FwI%3D)

Prerequisites: [React](https://react.dev/), [React Flow](https://reactflow.dev/)

Necessary programming skills: TypeScript and a little Rust

Potential mentors: [mxgrey](https://github.com/mxgrey)

Expected size: 175 to 350 hours

Difficulty: Medium

Expected outcome: Improved user experience for the [crossflow](https://github.com/open-rmf/crossflow) diagram editor

Detailed description: [Crossflow](https://github.com/open-rmf/crossflow) is a general-purpose high-performance reactive programming library written in Rust on top of the [Bevy Game Engine](https://bevy.org/). One way to use crossflow is to manually draw a diagram that describes a workflow, and then send that diagram to a crossflow application to be executed. We provide the [crossflow diagram editor](https://open-rmf.github.io/crossflow/) as a basic open source out-of-the-box diagram editor tailored to creating workflows that can be executed by the crossflow library. Participants for this project would add features to the diagram editor to improve its user-friendliness. Some features to consider may include:
* Real-time validation of the diagram (e.g. make sure all connections are compatible)
* Make it easier/faster to add new operations to the diagram
* Real-time tracing of workflow execution, illustrated on the diagram (e.g. highlighting active nodes)
* Interactive debugging
  * Pause / resume
  * Toggle breakpoints
  * Step in / Step out
  * Hot start a workflow from a saved state
* Manage multiple workflow sessions from the same window

### Continuous integration testing of the reservation node.

Prerequisites: Basic understanding of ROS2, colcon and python.

Necessary programming skills: C++, Python

Potential mentors: [arjo129](https://github.com/arjo129)

Expected size: 90 hours

Expected outcome: Provide an integrated test suite for open-rmf's reservation node.

Detailed description: Open-RMF's reservation system makes sure that robots dont end up occupying each others spaces. In its current form it is a very simple greedy queue based allocator. This component, however is incredibly brittle and any change to the protocol or heuristics requires extensive testing. Currently, we have [some hacky scripts](https://github.com/arjo129/stress_test_rmf_chope) which we need to watch for testing edge cases. It would be good to be able to run these in CI or automatically.

### Improved throughput for Traffic Dependency Calculation

Necessary programming skills: Rust

Potential mentors: [arjo129](https://github.com/arjo129)

Expected size: 90 hours

Expected outcome: Implement a faster collision detection mechanism in our traffic dependency code

Detailed Description: Traffic Dependency calculations are critical for executing MAPF plans. The current prototype uses an older algorithm that runs in $O(N^4)$. Recent works are able to reduce this bound using
KD-Trees. The goal would be to implement one of these faster algorithms within the traffic dependency calculator.

## ROS Infrastructure

# Application template for students

 * If you would like to suggest new projects you are free to e-mail your ideas to us at: gsoc@osrfoundation.org. _We recommend you stick to one of the projects listed above unless you have already recruited a mentor._
 * If you have specific questions to discuss about a project, send an email to gsoc@osrfoundation.org. You may also ask your question in the `gsoc-q-and-a` channel [on our Discord server](https://discord.com/servers/open-robotics-1077825543698927656).
 * If you meet the general requirements and are interested in working on one of the OSRF projects during Google Summer of Code, **you can apply by submitting your application through the [Google GSoC web site](https://summerofcode.withgoogle.com) once participant** applications open on March 25th, 2025. 

# Completing Your GSoC Application

## Proposal Title

Your proposal title should match one of the projects listed above.

## Proposal Summary

For your proposal summary introduce yourself and briefly discuss your plan for addressing the project you have selected. 

## What to Include in Your Proposal PDF File 

Your proposal PDF file should include the bulk of your application. Please include the information outlined in the subsequent four sections below. 

### Contact Information

 * Your name
 * A phone number
 * An email address where we can reach you for daily communication
 * **Your Github profile or personal website**


### Education and Coursework

Please provide information about your university, degree type, and your expected graduation year. Please list relevant technical courses you have taken.  In particular, we are interested in your background in:

 * Robotics
 * Software engineering
 * Computer graphics
 * Physics simulation

### Experience

Please list any experience you’ve had in software development, including relevant class projects, internships, undergraduate or graduate research, and/or **contributions to open source projects**.
For each example, please include a brief description of the overall project along with the specific contributions you made and when you made them.

In addition to the above information, we are interested in concrete examples of your work, which may include:

 * 📢 Open source contributions: **Our mentors are looking for students who have mastered the fundamentals of open source contribution.** If you have contributed to any of our open source projects, or any other open source projects, please include a link to those contributions prominently in your application.  
 * Sample code: please send an example of code you have written that you are proud of; be prepared to answer questions about it. A link to a Github repository works the best!
 * Publications: if you have participated in undergraduate or graduate research, please include a link to a copy of any relevant publications.
 * Specialized skills: if you have experience/skills in particular areas that you believe would be useful to one of our projects, please let us know.
 * Personal website: if you have a website that discusses your research or other projects, please include a link.
 * References: names and contact information for people you have worked with who can recommend you.

### Statement of Intent

In a paragraph or two, describe your interests and background.  Please tell us which of the project ideas you are interested in and why you’d like to work on it.  If you have a proposal for a project not included on our list, please describe the idea clearly and provide a motivation for the work and a timeline for how you plan to accomplish it.

## ⚠️ A Note on Generative AI ⚠️

**We strongly discourage students from using generative AI tools to generate their application.** Students working with OSRF project mentors over the summer must possess strong communication skills. Our mentors use GSoC applications to evaluate each student's written communication skills. Our mentors may choose to reject students they suspect have used generative AI tools as part of their application. Moreover, as per the [OSRA's interim policy on generative AI tools,](https://discourse.ros.org/t/interim-policy-on-the-use-of-generative-ai-in-osrf-projects/39731) contributors are not permitted to use generative AI tools for code contributions.
