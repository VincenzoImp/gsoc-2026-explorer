# International Catrobat Association — Project Ideas

**Source:** https://developer.catrobat.org/pages/development/google-summer-of-code/2026/
**Scraped:** 2026-02-22T23:28:47.613628

---

# Ideas Page for Google Summer of Code 2026

We are thrilled to share our carefully curated project ideas for this year’s Google Summer of Code.

## General Information

These ideas are just some topics we came up with, where currently nobody is working on. However, Catrobat is a project with a wide range of possibilities and we’re aware of our blindspots: So let’s live the spirit of Open Source and come up with improvements (e.g., new features, extensions, …) that are related to the project and in which you’re interested in. We do have many senior contributors who would be happy to mentor such a project. Don’t be shy and check out the last point on the list: Your idea!

For your submission, please follow [our instructions](https://docs.google.com/document/d/1vOGY2C80raXLV6RVRHXoqiAhcnBJFeZdU8wqMm-Rgo0/edit?usp=sharing) and submit a corresponding document via the [GSoC application site](https://summerofcode.withgoogle.com/).

## AI tools policy

You may use AI tools as much as you like (brainstorming, code generation, refactoring, tests, documentation, review). We believe this can significantly improve quality and learning when used thoughtfully. What matters is the outcome: correctness, maintainability, Clean Code and tests. You must be able to explain and justify your implementation and tests.

To apply for some of the project ideas, please complete the associated entry task, if any, and include the links to the requested demo artifacts in your application. Entry tasks have on purpose been formulated in a little bit more difficult way so that it’s not easy to simply feed the idea into an AI, and let the AI completely answer for you. However, we understand that the time to complete an entry task can be substantial, and we therefore ask you to write down the time you need to finish the entry task. In case your proposal will be accepted, this time to complete the entry task will be subtracted from the number of hours that will be agreed to be completed by you. For substantial proposals that we could not accept, there will be some other way of recompense for you, to be decided.

## General Knowledge Prerequisites for all Projects

- Usage of Git and GitHub
- Software testing (e.g., test doubles) and test-driven development
- Kotlin, Java, or Flutter for Android ideas (depending on target project)
- Swift for iOS ideas
- Also please check that you have the proper hardware for the development (e.g., an Android/iOS smartphone for testing some of the projects, Mac for iOS development etc)

## Idea Overview

[Multiplayer, IoT, and Home Assistant support via two MQTT bricks](https://developer.catrobat.org#multiplayer-iot-and-home-assistant-support-via-two-mqtt-bricks)[SeaSee’r: Underwater Mapping and Exploration using Spatially anchored Panoramas](https://developer.catrobat.org#seaseer-underwater-mapping-and-exploration-using-spatially-anchored-panoramas)[Pocket Paint Flutter: backwards compatibility to old Android app](https://developer.catrobat.org#pocket-paint-flutter-backwards-compatibility-to-old-android-app)[Pocket Paint Flutter: antialiasing and smoothing (advanced options)](https://developer.catrobat.org#pocket-paint-flutter-antialiasing-and-smoothing-advanced-options)[AI Mentor for PocketCode Students](https://developer.catrobat.org#ai-mentor-for-pocketcode-students)[Pin projects to the Android launcher (“Play as app” shortcuts)](https://developer.catrobat.org#pin-projects-to-the-android-launcher-play-as-app-shortcuts)[Skeleton-Based Procedural Animation System for Marine Organisms](https://developer.catrobat.org#skeleton-based-procedural-animation-system-for-marine-organisms)[Gemini-Powered Ecosystem Narration and Analysis Interface](https://developer.catrobat.org#gemini-powered-ecosystem-narration-and-analysis-interface)[AI-Driven Dynamic Procedural Map Generation System](https://developer.catrobat.org#ai-driven-dynamic-procedural-map-generation-system)[Upgradation of AR-Based Interactive and Procedural Marine Ecosystem Simulation](https://developer.catrobat.org#upgradation-of-ar-based-interactive-and-procedural-marine-ecosystem-simulation)[AR Based Human Interaction Enabled Application for Marine Life](https://developer.catrobat.org#ar-based-human-interaction-enabled-application-for-marine-life)[Extension of Sandbox Toolkit for simplifying the Development of Marine based AR Modules](https://developer.catrobat.org#extension-of-sandbox-toolkit-for-simplifying-the-development-of-marine-based-ar-modules)[Web-Based Sandbox Toolkit for Marine AR Modules](https://developer.catrobat.org#web-based-sandbox-toolkit-for-marine-ar-modules)[Blockchain-Based Ethical Governance for IoT Care Systems](https://developer.catrobat.org#blockchain-based-ethical-governance-for-iot-care-systems)[Gemini-API–Powered Intelligent Care Assistant](https://developer.catrobat.org#gemini-apipowered-intelligent-care-assistant)[AR Rocket Builder & Space Flight Sandbox](https://developer.catrobat.org#ar-rocket-builder--space-flight-sandbox)[AR Gravity & Planetary Physics Simulator](https://developer.catrobat.org#ar-gravity--planetary-physics-simulator)[AR Interactive Physics Playground](https://developer.catrobat.org#ar-interactive-physics-playground)[Sentiment Analysis of Cephalopods](https://developer.catrobat.org#sentiment-analysis-of-cephalopods)[Minimal Open-Source IoT Cloud Platform with Secure Device Access](https://developer.catrobat.org#minimal-open-source-iot-cloud-platform-with-secure-device-access)[Your own Project Ideas …](https://developer.catrobat.org#your-own-project-ideas-)

## Project Descriptions

### Multiplayer, IoT, and Home Assistant support via two MQTT bricks

90, 175 or 350 hours


Required Skills: Kotlin, Android-Development, Agile Development, Test Driven Development, Clean Code

Possible Mentors: Wolfgang Slany, Paul Spiesberger

Expected Outcome: Two new bricks for sending and receiving MQTT messages

Difficulty level: Advanced

Task link:[View task]

Implement MQTT support for the Catrobat language in Catroid (Pocket Code and its flavors) so Catrobat programs can publish/receive network messages for multiplayer games, IoT, and Home Assistant setups. Add two new Catrobat bricks (activated via app settings):

- Broadcast … via MQTT on channel …
- When you receive a message via MQTT on channel … store it in …

Broker/TLS/auth/client-id are configured globally in app settings, and connect/subscribe happen lazily to avoid boilerplate (wildcard channels should store channel+message as JSON). Provide example projects for two multiplayer architectures:

- one phone acting as a local hub (extending the existing Bluetooth multiplayer variables concept) and
- a dedicated hub over local Wi-Fi (e.g., Mosquitto) coordinating multiple players. Also provide a Home Assistant-oriented topic convention under catrobat/… enabling wall-tablet dashboards and home automations (Tuya/Smart Life and other Home Assistant-supported hardware).

Ensure reliability (reconnect/offline handling) and strong automated tests for core logic (especially topic-filter matching and message routing).

To apply for this project idea, please complete [this entry task](https://docs.google.com/document/d/1jw87hf8iq5DStlKOhT9yvQP7trsnzgZ6jYcH99BxBMs/edit?usp=sharing) and include the links to the requested demo artifact in your application.

### SeaSee’r: Underwater Mapping and Exploration using Spatially anchored Panoramas

350 Hours


Required Skills: Web Development (Full Stack), Web 3D Graphics, Real-Time Rendering, Python, Computer Vision, Git, REST APIs

Possible Mentors: Benedikt Kantz, Tobias Schreck, Wolfgang Slany

Expected Outcome: A navigatable underwater map based on real multimodal data from a remotely operated vehicle (ROV), including panorama (videos) and sonar dataDifficulty level: Advanced

Project size: Large

Task link:[View task]

Project Description

Modern underwater ROVs provide a magnitude of different data streams in both real-time and post-operation for scientific application. There is, however, a lack of systems integrating the domain-specific requirements for navigating and exploring these data, especially for frequent site visits to study the behavior of marine creatures.

The project therefore proposes the creation of an open-source system to ingest data from the ROV and display the panorama images spatially anchored based on the position and orientation of the vehicle at the specific time stamps. The resulting interface should also incorporate multimodal data, i.e. sonar data and possible further data streams like point clouds directly into the visual exploration system. Once this basic visualization system is set up, specific exploration tasks can be implemented, such as:

- Mission and path planning, with
- Search for prior exploration passes for detailed mission planning at specific sites,
- Point cloud stitching / Image registration to compare passes over the same regions,
- Site Re-Identification even in noisy environments through multimodal data use, and possible
- Registration of new images and feeds live (during missions) to improve the navigation accuracy.

The project serves as an exploratory foray into bringing advances in spatial exploration and mapping techniques below the sea, and requires an extensible and longevity-focused architecture to enable downstream additions of data modalities and different vehicle types. The specific mission planning aspects need to be flexible in their structure as well, to allow for a rapid evolution in supported planning tooling; as the scientific goals might shift over time – or new aspects of the marine life are discovered, requiring new paradigms.

### Pocket Paint Flutter: backwards compatibility to old Android app

350 Hours


Required Skills: Flutter, Dart, Android-Development, Agile Development

Possible Mentors: Abdulbaki Celebi, Mario Kaurin, Julia Herold, Thorsten Bandel

Expected Outcome: Compatibility of the Kotlin/Java version file formats in the new Flutter-based version

Difficulty level: Medium to advanced

The developer should have knowledge of Flutter. Develop and implement missing tools in Flutter that exist in our old Android app built with Android Native.

### Pocket Paint Flutter: antialiasing and smoothing (advanced options)

350 Hours


Required Skills: Flutter, Dart, Android-Development, Agile Development

Possible Mentors: Julia Herold, Thorsten Bandel, Abdulbaki Celebi, Mario Kaurin

Expected Outcome: Add antialiasing and smoothing as advanced options

Difficulty level: Medium to advanced

Task link:[View task]

The developer should have knowledge of Flutter. Develop and implement missing tools in Flutter that exist in our old Android app built with Android Native.

### AI Mentor for PocketCode Students

350 Hours


Required Skills: Kotlin, Python, JavaScript, Android AI and ML Tools, Android-Development, Agile Development, Test Driven Development, Clean Code

Possible Mentors: Paul Spiesberger, Wolfgang Slany

Expected Outcome: An integrated proof of concept AI mentor within PocketCode

Difficulty level: Advanced

AI is now capable of sophisticated programming and can automate many coding tasks. More importantly, it excels at explaining code to students, making learning more engaging and accessible. Our goal is to integrate our AI-powered mentor, developed during GSoC 2025, into PocketCode. This mentor understands a student’s programming context and provides real-time guidance to enhance learning and coding skills. We already have an existing [AI Tutor SDK](https://github.com/Catrobat/catrobat-ai-tutor) and are now ready to integrate it into PocketCode and its derivatives to test and improve students’ experiences with PocketCode + AI.

The AI mentor could:

- Explain programming concepts, ranging from variables and loops to software design patterns and testing strategies
- Suggest code from text prompts, help debug issues and propose project ideas
- Assist with code architecture, naming conventions and writing tests in the Catrobat language
- Explain and translate downloaded projects from other users

You won’t need to implement everything—just focus on the part that excites you most! The Catrobat team will provide the initial prompt and the necessary API access or local LLMs for support.

### Pin projects to the Android launcher (“Play as app” shortcuts)

90, 175 or 350 hours


Required Skills: Kotlin, Android-Development, Agile Development, Test Driven Development, Clean Code

Possible Mentors: Wolfgang Slany, Patrick Ratschiller, Paul Spiesberger

Expected Outcome: Pin to launcher option and functionality to execute projects directly from launcher.

Difficulty level: Advanced

Task link:[View task]

Add support in Catrobat/Catroid so users can pin a project to the Android home screen with an app-like icon (project thumbnail + title). Tapping the pinned icon must start the project immediately in Play mode (no IDE screens), and exiting Play must not return to the IDE but instead close the task back to the launcher. Implement this via a dedicated shortcut entry point (trampoline) and a stable project identifier, with graceful handling if the project was renamed or deleted. Deliver strong automated tests for intent parsing, task/back-stack behavior, and the exit contract across common Android versions.

To apply for this project idea, please complete [this entry task](https://docs.google.com/document/d/14BSMYM7JiwKSqJHJIXSPfNT_PcyK9orRc68WhBzh-3o/edit?usp=sharing) and include the links to the requested demo artifact in your application.

### Skeleton-Based Procedural Animation System for Marine Organisms

350 Hours


Required Skills: Python, C#, Procedural Animation, Skeletal Systems, Blender Scripting, 3D Geometry, Git Version Control, GitHub, Understanding and integration of ML models, Unity, Blender

Possible Mentors: Nikhil Ranjan Rajhans, Abha Kumari

Expected Outcome: A reusable skeleton-driven procedural animation framework for marine animals

Difficulty level: Advanced

Project size: Large

Task link:[View task]

Project Description

This project focuses on creating a skeleton-based procedural animation system for marine animals generated via AI or procedural 3D pipelines. Instead of keyframe animations, animal motion (swimming, turning, fleeing, idling) will be generated dynamically using rule-based skeletal deformation and motion constraints.

Animations will be driven by behavior states and environmental conditions, allowing seamless integration with AI behavior engines and ecosystem simulations. The system will be lightweight, reusable, and suitable for real-time educational applications.

### Gemini-Powered Ecosystem Narration and Analysis Interface

175 Hours


Required Skills: Python, C#, LLM Integration, Prompt Engineering, Explainable AI, Simulation Analysis, Git Version Control, Understanding and integration of ML models, Unity

Possible Mentors: Abha Kumari, Garima Jain, Kumari Deepika

Expected Outcome: An AI-powered narration and analysis layer for marine ecosystem simulations

Difficulty level: Average

Project size: Medium

Task link:[View task]

Project Description

This project integrates a Gemini-based natural language interface to enhance accessibility and explainability of marine ecosystem simulations. The AI will provide real-time narration, ecosystem summaries, causal explanations, and natural-language spawning of marine organisms and environmental events.

The LLM will act strictly as an interface and explanation layer, translating simulation states into human-readable insights and structured ecosystem modifications, while core logic remains deterministic and transparent.

### AI-Driven Dynamic Procedural Map Generation System

175 Hours


Required Skills: C#, Procedural Generation, AI Simulation Systems, Spatial Data Structures, Noise Functions, Environmental Modeling, Behavior Modeling, Git Version Control, Auth, DBMS, Understanding and integration of ML models, Unity, Blender

Possible Mentors: Kumari Deepika, Atharva Prashant Joshi

Expected Outcome: A dynamically evolving coral reef environment guided by AI-driven simulation models

Difficulty level: Advanced

Project size: Medium

Task link:[View task]

Project Description

This project extends the mARine AR application by combining procedural generation with AI-based environmental intelligence to create marine ecosystems that evolve realistically over time.

Instead of static procedural placement, the environment will be guided by AI models that simulate reef growth, ecological balance, and adaptive behavior. The system will use a seed-based deterministic generator enhanced by AI rules, ensuring synchronized AR experiences across devices while still allowing intelligent variation.

The system should generate:

- AI-guided terrain topology — Terrain shaped using noise functions enhanced by learned patterns from real reef structures
- Intelligent coral and flora placement — AI models determine clustering, competition, and growth patterns to mimic natural ecosystems
- AI-driven environmental motion — Coral sway, particle flow, and micro-movements based on simulated currents and environmental forces
- Ecosystem evolution over time — Coral growth, decay, and adaptation using rule-based AI or lightweight simulation learning

All generations must remain deterministic from a seed, with AI models acting as rule systems that produce identical synchronized environments across devices.

The final system should feel alive, it should be biologically plausible and continuously evolving.

### Upgradation of AR-Based Interactive and Procedural Marine Ecosystem Simulation

350 Hours


Required Skills: C#, Java, Unity, Vuforia SDK, AR Foundation, Firebase, Cloud, Git Version Control, GitHub, REST API, Auth, DBMS, Understanding and integration of ML models, CI/CD, Blender

Possible Mentors: Krishna Mohan Patel, Himanshu Kumar

Expected Outcome: A more realistic, scalable, and performance-optimized AR marine ecosystem platform

Difficulty level: Advanced

Project Size: Large

Task link:[View task]

Description

This project focuses on upgrading and strengthening the existing AR-based marine ecosystem simulation platform built during the previous GSoC cycle. The aim is to enhance both scientific realism and system scalability, enabling more accurate ecosystem interactions and smoother deployment across mid-range mobile devices.

The upgraded version will improve procedural generation of marine environments (reef, interaction, deep ocean), introduce more advanced ecosystem behaviors (predator-prey cycles, habitat-based movement, climate-driven changes), and implement performance-critical improvements like optimized LOD pipelines, shader efficiency, and streaming-based spawning.

Additionally, this project will expand infrastructure support using Firebase, cloud-ready services, enabling user authentication, progress storage, module sharing, and future backend integration. Optional integration of lightweight ML models can be explored for behavior prediction, adaptive learning, or intelligent content recommendation.

### AR Based Human Interaction Enabled Application for Marine Life

175 Hours


Required Skills: Python, YOLO, MediaPipe, Pose Detection Algorithms, Machine Learning, C#, Unity, Vuforia SDK, AR Foundation, Firebase, Cloud, Git Version Control, GitHub, REST API, Auth, DBMS, Understanding and integration of ML models, CI/CD, Blender

Possible Mentors: Udit Narayan, Nikhil Ranjan Rajhans

Expected Outcome: A complete gesture-driven AR marine learning experience

Difficulty level: Advanced

Project Size: Medium

Task link:[View task]

Description

This project is focused at extending the marine AR learning system by introducing a human-interaction enabled interface, allowing students to interact naturally with marine life using body gestures and pose-based controls.

Instead of relying only on buttons and UI controls, users will be able to perform interactions such as interfering with a creature’s movement using hand gestures, triggering behavior events (octopus camouflage/ink defense etc.), interacting with the ecosystem through human presence and activities through the device camera.

The expected goal is to achieve a complete gesture-driven AR marine learning experience that improves immersion, accessibility, and interaction realism.

### Extension of Sandbox Toolkit for simplifying the Development of Marine based AR Modules

350 Hours


Required Skills: Java, C#, Unity, Unity Editor tooling, Vuforia SDK, ScriptableObjects, AR Foundation, Firebase, Cloud, Git Version Control, GitHub, REST API, Auth, DBMS, Understanding and integration of ML models, CI/CD, Blender

Possible Mentors: Somya Barolia, Shivendra Verma

Expected Outcome: A reusable Unity-based Marine AR Module Builder

Difficulty level: Advanced

Project Size: Large

Task link:[View task]

Description

This project enhances our existing Marine AR Module Builder to make it significantly easier for educators and developers to create, package, and distribute marine AR modules without deep technical knowledge.

The extension will focus on improved editor tools for drag-drop environment creation, actor placement & configuration workflows, reusable behavior templates (movement, interactions, ecology rules), JSON/script-based module definition support, validation tools (missing assets, invalid scripts, performance warnings), alignment with marine curriculum and optional cloud syncing (module hosting+version control support).

The toolkit will be built as a modular Unity package so it can be reused beyond this project and integrated into other Catrobat AR education initiatives.

### Web-Based Sandbox Toolkit for Marine AR Modules

350 Hours


Required Skills: JavaScript, WebAR (WebXR), Three.js / A-Frame, HTML/CSS, Firebase, REST API, Git/GitHub, Basic Cloud & CI/CD, Blender

Possible Mentors: Somya Barolia, Shivendra Verma

Expected Outcome: A lightweight, reusable Web AR Sandbox Toolkit for marine education

Difficulty level: Advanced

Project Size: Large

Task link:[View task]

Description

This project extends an existing Web-based Marine AR Sandbox Toolkit to simplify the development and deployment of marine-focused Web AR learning modules. The aim is to enable educators and developers to create interactive marine AR experiences directly from a browser without requiring deep AR or 3D programming expertise.

The extension will introduce a dashboard-based module builder where users can visually assemble marine scenes, place 3D marine organisms, configure basic interactions, and publish Web AR modules that run on mobile browsers.

Scope of Work

- Browser-based dashboard for creating and managing marine AR modules
- Drag-and-drop placement of 3D marine assets in AR scenes
- Reusable behavior templates for basic movement and interactions
- JSON-based module definition and export/import support
- Validation checks for missing assets and basic performance limits
- Cloud-hosted module storage and versioning using Firebase

Expected Outcome

- A lightweight, reusable Web AR Sandbox Toolkit for marine education
- Simplified creation and sharing of marine AR modules via URLs
- A foundation for extending Web-based AR learning across marine science topics

### Blockchain-Based Ethical Governance for IoT Care Systems

350 Hours


Required Skills: Strong programming fundamentals, smart contract development, blockchain architecture understanding, API design and system integration, security and access-control conceptsPossible Mentors: Garima Jain, Supreeth Kumar MDesirable Skills: Privacy-by-design principles, cryptographic hashing, regulatory-aware system designExpected Outcome: A complete blockchain-based consent and governance framework for IoT care systems

Difficulty level: Advanced

Project Size: Large

Description

This project focuses on designing and implementing a blockchain-based governance and consent framework for ethical IoT-based care monitoring systems. The objective is to ensure trust, transparency, data ownership, and immutable consent management for sensitive care-related data generated by IoT devices used in assisted living environments.

Rather than storing health data on-chain, the blockchain will act as a trust and audit layer, recording consent decisions, access approvals, role assignments, and accountability events.

Problem Context

IoT-based care systems face critical challenges:

- Consent is often implicit, unclear, or changeable without traceability
- Care data access decisions are difficult to audit
- Families, caregivers, and supervisors rely on centralized systems with limited transparency
- Ethical compliance relies heavily on documentation rather than system-level enforcement

This project addresses these issues by embedding ethical governance directly into system architecture using blockchain.

Technical Scope

**A. Governance Model Design**

- Definition of care-related roles (patient, caregiver, supervisor, relative)
- Consent lifecycle modeling (grant, update, revoke)
- Human-in-the-loop approval workflows

**B. Blockchain Layer**

- Smart contracts for:
- Consent registration and revocation
- Role-based access authorization
- Event logging for care-related decisions

- Immutable audit trail for:
- Who approved what
- When access was granted or revoked
- Which role initiated the action


**C. Off-Chain / On-Chain Architecture**

- Sensitive IoT data stored off-chain
- Cryptographic hashes and metadata stored on-chain
- Blockchain used purely for verification, not data storage

**D. Integration Interface**

- APIs to connect IoT systems with the blockchain layer
- Verification endpoints for access checks
- Read-only audit views for compliance and evaluation

Expected Outcome

At the end of the project, the contributor will deliver:

- A complete blockchain-based consent and governance framework
- Deployed smart contracts implementing ethical access control
- API layer enabling IoT system integration
- Demonstrable immutable audit trail
- System architecture documentation and threat analysis

The result is a production-relevant governance layer, not a theoretical blockchain demo.

### Gemini-API–Powered Intelligent Care Assistant

350 Hours


Required Skills: Backend development, API integration, prompt engineering for structured systems, data processing and normalization, system-level reasoning

Desirable Skills: Human-centered AI design, ethical AI concepts, evaluation of AI outputs

Possible Mentors: Supreeth Kumar M, Atharva Prashant JoshiExpected Outcome: An AI-powered, ethically governed intelligent care assistant built on Gemini API

Difficulty level: Intermediate to Advanced

Project Size: Large

Description

This project aims to build an AI-powered intelligent care assistant using the Gemini API to support caregivers, supervisors, and families by converting raw IoT activity signals into context-aware insights, summaries, and alerts—while maintaining ethical, permission-based access. The focus is on responsible AI usage, ensuring that AI augments human decision-making rather than replacing it.

The assistant acts as an interpretation and explanation layer over existing IoT-based care systems, not as a surveillance or diagnostic system.

Problem Context

IoT care systems generate large volumes of low-level signals such as:

- Activity logs
- Time-based events
- Movement patterns
- Routine confirmations

These signals are difficult to interpret meaningfully and ethically in real time. Manual monitoring often leads to caregiver overload, missed anomalies, and increased anxiety among family members. This project introduces an AI interpretation layer that summarizes and contextualizes data while preserving human oversight.

Technical Scope

**A. Data Interpretation Layer**

- Structured ingestion of non-invasive IoT activity data
- Time-windowed summaries of daily routines
- Detection of deviations from normal patterns

**B. Gemini API Integration**

- Natural-language summaries of patient routines
- Context-aware explanations for alerts (why an alert was triggered)
- Ethical prompt design to avoid medical diagnosis or inference
- Role-aware output filtering (different outputs for caregivers, supervisors, and relatives)

**C. Human-in-the-Loop Controls**

- AI outputs require supervisor validation before escalation
- Confidence indicators and uncertainty explanations
- Manual override and feedback loop for continuous improvement

**D. Responsible AI Safeguards**

- Prompt constraints and system instructions
- No medical diagnosis generation
- Explainability-first responses
- Logging and review of AI outputs

**E. Application & System Integration**

- Integration with a secure care monitoring application featuring role-restricted dashboards
- Support for voice-assisted interactions to improve accessibility for elderly users
- Backend services handling ingestion, summarization, and alert generation
- Secure authentication and role-based access to AI-generated insights

Expected Outcome

By the end of the project, the contributor will deliver:

- An AI-powered intelligent care assistant service
- Gemini API–based summarization and explanation engine
- Ethical prompt and output governance framework
- Role-based AI response filtering
- Demonstration of AI-assisted, human-approved alerts
- Complete documentation and evaluation report

The outcome demonstrates applied, responsible AI in a real-world care context, not chatbot experimentation.

### AR Rocket Builder & Space Flight Sandbox

350 Hours


Required Skills: Augmented Reality (ARCore/ARKit), Physics Simulation, Rigid Body Dynamics, Vector Math, Orbital Mechanics Basics, Unity & Flutter 3D Integration, Firebase, Cloud Sync, Git Version Control, REST API, DBMS, CI/CD

Possible Mentors: Himanshu Kumar, Abhishek Kumar

Expected Outcome: An AR rocket construction and flight simulator where users build rockets in their real environment and launch them with physics-accurate behavior

Difficulty level: Advanced

Project size: Large

Task link:[View task]

Project Description

This project transforms the app into an augmented reality rocket engineering sandbox. Users build rockets on real-world surfaces using AR placement and modular components. The launch simulation applies thrust, drag, gravity, and fuel consumption in real time.

Rockets launch directly from the floor or table in the user’s environment. Failures such as imbalance, insufficient thrust, or structural instability are visualized physically, helping children understand engineering constraints.

Educational overlays explain forces, center of mass, and orbital velocity using visual arrows and motion trails. The system supports multiple gravity presets (Earth, Moon, Mars) and replay tools to analyze trajectories.

The architecture will allow reusable rocket parts, physics presets, and AR experiment modules for future aerospace learning features.

### AR Gravity & Planetary Physics Simulator

175 Hours


Required Skills: Augmented Reality Rendering, Newtonian Physics Simulation, N-Body Systems, Numerical Integration, Real-Time Optimization, 3D Visualization, Flutter, Unity Firebase, Cloud Systems, Git

Possible Mentors: Abhishek Kumar, Ashwani Kumar Moudgil

Expected Outcome: An AR gravity sandbox where users create planetary systems in their room and observe real-time orbital mechanics

Difficulty level: Advanced

Project size: Medium

Task link:[View task]

Project Description

This project creates a real-time AR gravity sandbox where celestial bodies appear inside the user’s physical environment. Users spawn planets, stars, or asteroids on tables or floors and observe how gravity shapes motion.

The simulation implements Newtonian gravitational models with optimized solvers for mobile performance. Users can walk around their planetary systems, view orbits from different angles, and physically scale the simulation.

Educational visualizations convert invisible forces into arrows, trails, and orbit predictions. Presets include solar systems, binary stars, asteroid collisions, and black hole experiments.

The system is designed as a reusable AR physics engine supporting scalable multi-body simulations for future educational modules.

### AR Interactive Physics Playground

350 Hours


Required Skills: AR Interaction Design, Physics Engines, Collision Systems, Real-Time Rendering, Mobile Optimization, Educational Game Design, Flutter, Unity, Firebase, Git, REST APIs

Possible Mentors: Shivendra Verma, Himanshu Kumar

Expected Outcome: A modular AR physics playground that lets children run real-world science experiments in their environment

Difficulty level: Advanced

Project size: Large

Task link:[View task]

Project Description

This project introduces an augmented reality science playground where children run interactive physics experiments in their surroundings. Objects can be placed on real surfaces and manipulated using gestures to test forces, motion, and collisions.

Mini-labs include pendulums, ramps, projectiles, levers, bouncing systems, and gravity experiments. Each experiment includes guided prompts and simplified explanations.

The playground acts as a reusable AR education framework where new experiments can be plugged in easily. It bridges abstract physics concepts with real-world spatial interaction.

### Sentiment Analysis of Cephalopods

350 Hours


Required Skills: Java, Python, Machine Learning, Deep Learning, Multi-Modal Modelling, Knowledge Distillation, Model Optimization Techniques, Computer Vision, Git Version Control, GitHub, REST API, Authentication

Possible Mentors: Aryavardhan Sharma, Krishna Mohan Patel, Himanshu Kumar

Expected Outcome: An open-source multi-modal pipeline for automated cephalopod behavioral sentiment analysis

Difficulty level: Advanced

Project Size: Large

Task link:[View task]

Description

Cephalopods exhibit complex cognition and emotional-like behavioral states (stress, comfort, aggression, curiosity). However, interpreting their state currently requires expert manual observation and lacks scalable tools.

This project aims to develop an open-source pipeline that uses multi-modal data (behavioral video, bioacoustic data) using computer vision and advanced machine learning algorithms to automatically infer and classify behavioral sentiment states along with recording them for further analysis.

The expected outcomes are to contain of:

- Dataset ingestion pipeline + preprocessing scripts
- Multi-modal model baseline (video + optional audio)
- Behavioral feature extractor (movement, postures, color/pattern changes)
- Sentiment label classification system (stress/calm/curious/aggressive/etc.)
- Training + evaluation scripts with metrics
- Documentation + reproducible experiments
- Deployment API, demo dashboard

The project will help researchers, aquaculture facilities, and education/science communities by providing reproducible tools for cephalopod behavioral analysis. The system will be designed with extensibility in mind, supporting future datasets, species, and deployment environments (edge devices compatibility as well).

### Minimal Open-Source IoT Cloud Platform with Secure Device Access

175 Hours


Required Skills: Python, REST API development, backend engineering fundamentals, HTTP and JSON, databases (SQLite, PostgreSQL, or time-series databases), basic web technologies (HTML, CSS, JavaScript), Git version control, GitHub

Expected Outcome: A lightweight, open-source IoT cloud platform with secure device authentication, telemetry ingestion, persistent storage, and a web-based visualization dashboard

Difficulty level: MediumPossible Mentors: Atharva Prashant Joshi, Shivendra VermaProject Size: Medium

Description

This project focuses on building a minimal and educational open-source IoT cloud platform that exposes the core principles of device-to-cloud communication in a clear and transparent way. Instead of relying on fully managed or proprietary IoT services, the platform emphasizes explicit implementation of authentication, access control, data ingestion, storage, and visualization.

Devices will be able to register with the platform and receive unique API keys used to authenticate all telemetry ingestion requests. Incoming data will be validated, securely associated with the correct device, and stored persistently in a structured time-series format. This ensures that only authorized devices can submit data while keeping the system simple and easy to reason about.

To make the system observable and useful, a lightweight web-based dashboard will be developed. The backend will expose REST APIs that return stored telemetry data as JSON, while the frontend will render this data as interactive time-series graphs using open-source JavaScript charting libraries. Backend processing will focus on correctness, validation, and basic aggregation, while the frontend handles visualization and interaction.

The platform is intentionally scoped as a learning-oriented reference implementation rather than a production-scale IoT cloud. Emphasis will be placed on clean architecture, readable and well-documented code, automated tests for authentication and ingestion logic, and reproducibility. The resulting system will serve as a strong foundation for future extensions such as MQTT-based ingestion, certificate-based device authentication, or more fine-grained access-control mechanisms.

### Your own Project Ideas …

90, 175 or 350 Hours


Required Skills: Kotlin, Java, Android-Development, iOS-Development, Agile Development

Requirement: self-organized work

Difficulty level: advanced

In the last years we found that you have many great ideas and knowledge! We’re aware that there are many ways how to improve performance, reduce memory usage, make our services more stable and of course the code easier to maintain. We’re sure you do have ideas how to achieve this, although we may have never heard of this approach before -> that’s the great thing about Open Source! And well, that’s also the experience we made at last year’s GSoC - and we liked it!

Also new features or extensions for iOS and Android are welcome to be introduced to us. Help us to spread coding and Open Source!
