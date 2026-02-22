# ArduPilot — Project Ideas

**Source:** https://ardupilot.org/dev/docs/gsoc-ideas-list.html
**Scraped:** 2026-02-22T23:28:47.606306

---

# List of Suggested Projects for GSoC 2026[Â¶](https://ardupilot.org#list-of-suggested-projects-for-gsoc-2026)

This is a list of projects suggested by ArduPilot developers for [GSoC 2026](https://summerofcode.withgoogle.com/). These are only suggestions so if you have your own ideas then please discuss them on the [ArduPilot Discord Chat](https://ardupilot.org/discord) or on the [discuss server here](https://discuss.ardupilot.org/c/google-summer-of-code)

Fleet Management Webtool

SITL Model Generation from Flight Data

Multi-Drone Mesh Networking (MAVLink-aware)

ArduHumanoid (ArduPilot controlling a simple humanoid)

AI-Assisted Log Diagnosis & Root-Cause Detection

Real-Time Companion-Computer Health Monitoring & Failsafe


See lower down on this page for more details on each project

## Timeline[Â¶](https://ardupilot.org#timeline)

The timeline for [GSoC 2026 is here](https://developers.google.com/open-source/gsoc/timeline)

## How to improve your chances of being accepted[Â¶](https://ardupilot.org#how-to-improve-your-chances-of-being-accepted)

When making the difficult decision about which students to accept, we look for:

Clear and detailed application explaining how you think the project could be done

Relevant prior experience

Experience contributing to ArduPilot or other open source projects

Understanding of Git and/or GitHub


### Fleet Management WebTool[Â¶](https://ardupilot.org#fleet-management-webtool)

Skills required: Javascript, Python

Mentors: Ryan Friedman, Randy Mackay

Expected Size: 175h

Level of Difficulty: Medium

Expected Outcome: Webtool to ease the management of a fleet of ArduPilot vehicles


The goal of this project is create a fleet management web tool that helps companies and individuals manage the data collected by multiple ArduPilot vehicles

Should extend the capabilities of the existing

[LogFinder Webtool](https://firmware.ardupilot.org/Tools/WebTools/LogFinder/)Accept onboard logs, tlogs, photos and videos uploaded by the GCS or from the vehicleâs companion computer (possibly running BlueOS or APSync)

Allow users to search and download data based on vehicle ID, recording date, location

Support both table views and map views of the uploaded data


Funding will be provided for hardware and cloud server as required.

### SITL Model Generation from Flight Data[Â¶](https://ardupilot.org#sitl-model-generation-from-flight-data)

Skills required: Python, C++ (ArduPilot/SITL), system identification

Mentors: Nathaniel Mailhot

Expected Size: 350h

Level of Difficulty: Hard

Expected Outcome: A toolchain that auto-builds or tunes SITL airframe models from real flight logs


The goal of this project is to take ArduPilot logs and estimate the key dynamics/sensor parameters needed for SITL, then output an updated model + params that better match the real vehicle.

### Multi-Drone Mesh Networking (MAVLink-aware)[Â¶](https://ardupilot.org#multi-drone-mesh-networking-mavlink-aware)

Skills required: Networking, C/C++, Linux, MAVLink

Mentors: Nathaniel Mailhot

Expected Size: 350h

Level of Difficulty: Hard

Expected Outcome: A practical mesh networking layer for multi-vehicle comms (telemetry + coordination)


The goal of this project is to enable resilient multi-hop links between multiple ArduPilot vehicles, so telemetry and commands can route through the swarm when direct links drop.

### ArduHumanoid (ArduPilot controlling a simple humanoid)[Â¶](https://ardupilot.org#arduhumanoid-ardupilot-controlling-a-simple-humanoid)

Skills required: C++, control, servo systems, simulation (Gazebo/Ignition)

Mentors: Nathaniel Mailhot

Expected Size: 175h

Level of Difficulty: Medium

Expected Outcome: A minimal humanoid âvehicle typeâ running on ArduPilot with SITL support


The goal of this project is to prove ArduPilot can command a small humanoid-style jointed frame (think âservo robotâ), with a basic control interface and a simple simulated model.

### AI-Assisted Log Diagnosis & Root-Cause Detection[Â¶](https://ardupilot.org#ai-assisted-log-diagnosis-root-cause-detection)

Skills required: Python, ML (classification + retrieval), ArduPilot logs/parameters

Mentors: Nathaniel Mailhot

Expected Size: 350h

Level of Difficulty: Hard

Expected Outcome: A model/service that flags likely root causes from logs and suggests fixes with confidence


The goal of this project is to automatically diagnose common failures and misconfigurations by learning from labeled log segments, known issue patterns, and parameter states. It should output a probable root cause, suggested fixes, and a confidence score (with links to the relevant evidence in the log).

### Real-Time Companion-Computer Health Monitoring & Failsafe[Â¶](https://ardupilot.org#real-time-companion-computer-health-monitoring-failsafe)

Skills required: C/C++ or Python, MAVLink, Linux companion computers

Mentors: Jaime Machuca

Expected Size: 175h

Level of Difficulty: Medium

Expected Outcome: A standard MAVLink-based health reporting + failsafe mechanism for companion computers


The goal of this project is to define and implement a consistent âcompanion healthâ report (CPU/GPU load, heartbeat, critical services, watchdog) and connect it to configurable failsafes so ArduPilot can respond predictably when the companion degrades or dies.

### Projects Completed in past years[Â¶](https://ardupilot.org#projects-completed-in-past-years)

In 2025, students completed the following projects:

In 2024, students completed the following projects:

In 2023, students completed the following projects:

In 2022, students worked on these projects:

In 2019, students successfully completed these projects:

AirSim Simulator Support for ArduPilot SITL

Development of Autonomous Autorotations for Traditional Helicopters

Further Development of Rover Sailboat Support

Integration of ArduPilot and VIO tracking camera for GPS-less localization and navigation

MAVProxy GUI and module development


In 2018, students successfully completed these projects:

RedTail integration with ArduPilot

Live video improvements for APSync


In 2017, 3 students successfully completed these projects:

Smart Return-To-Launch which involves storing the vehicleâs current location and maintaining the shortest possible safe path back home

Rework ArduRover architecture to allow more configurations and rover type (

[see details here](https://github.com/khancyr/GSOC-2017))Add âsensor headâ operation of ArduPilot, split between two CPUs


You can find their proposals and works on the

[Google GSoC 2017 archive page]
