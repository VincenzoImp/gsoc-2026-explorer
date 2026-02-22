# JdeRobot — Project Ideas

**Source:** https://jderobot.github.io/activities/gsoc/2026#ideas-list
**Scraped:** 2026-02-22T23:28:47.557419

---

# GSoC 2026

Robotics applications are typically distributed, made up of a collection of concurrent asynchronous components which communicate using some middleware (ROS messages, DDS…). Building robotics applications is a complex task. Integrating existing nodes or libraries that provide already solved functionality, and using several tools may increase the software robustness and shorten the development time. JdeRobot provides several tools, libraries and reusable nodes. They have been written in C++, Python or JavaScript. They are ROS-friendly and full compatible with ROS2-Humble (and Gazebo Harmonic).

Our community mainly works on three development areas:

-
Education in Robotics.

[RoboticsAcademy](/ideas/jderobot/roboticsacademy)is our main project. It is a ROS-based framework to learn robotics and computer vision with drones, autonomous cars…. It is a collection of Python programmed exercises and challenges for engineering students. -
Robot Programming Tools. For instance,

[BT-Studio](https://github.com/JdeRobot/bt-studio), for robot programming with Behavior Trees;[VisualCircuit](/ideas/jderobot/visualcircuit)for robot programming with connected blocks, as in electronic circuits, in a visual way. -
Machine Learning in Robotics. For instance, the

[BehaviorMetrics tool](/ideas/jderobot/behaviormetrics)for assessment of neural networks in end-to-end autonomous driving. Another example is[PerceptionMetrics tool](https://github.com/JdeRobot/PerceptionMetrics)for unified evaluation of 2D and 3D perception models.

# Ideas list

This open source organization welcomes contributors in these topics:

## Project #1: PerceptionMetrics: GUI extension and support for standard datasets and models

**Brief explanation**: [PerceptionMetrics](/ideas/jderobot/perceptionmetrics) is a toolkit for evaluating perception models across frameworks and datasets. Past GSoC projects ([Vinay Sharma, 2017](https://github.com/TheRoboticsClub/2017-colab-vinay_sharma), [Jeevan Kumar, 2019](https://theroboticsclub.github.io/colab-gsoc2019-Jeevan_Kumar/)) contributed to its first stable release, published in *Sensors* ([Paniego et al., 2022](https://doi.org/10.3390/s22124575)). Recently, the tool has been revamped to support LiDAR, image segmentation, and object detection ([Sakhineti Praveena, 2025](https://github.com/TheRoboticsClub/gsoc2025-Sakhineti_Praveena)).

Moving beyond our current focus on off-road navigation, this project aims to scale *PerceptionMetrics* for industry-standard benchmarks. The main goals are:

- Exploring core segmentation/detection datasets in the industry for image and LiDAR (e.g., SemanticKITTI, Cityscapes), prioritizing, and adding support for them.
- Extending the GUI to support image and LiDAR segmentation visualization (currently limited to object detection).
- Generating comprehensive tutorials and documentation for different use cases, models, and data formats.
- Improving the robustness of the project through an improved test suite.

**Skills required/preferred**: Python, PyTorch, Deep Learning, Streamlit**Difficulty rating**: Medium**Expected results**: Support for new datasets, GUI extension for image and LiDAR segmentation, and comprehensive technical documentation.**Expected size**: Long (~350h)**Mentors**: David Pascual Hernández (d.pascualhe AT gmail.com), Sakhineti Praveena (sakhinetipraveena AT gmail.com)

## Project #2: Robotics Academy: extend C++ support for more exercises

**Brief explanation**: [Robotics-Academy](/ideas/jderobot/roboticsacademy-2) is a framework for learning robotics and computer vision. It consists of a collection of robot programming exercises. The students have to code in Python the behavior of a given (either simulated or real) robot to fit some task related to robotics or computer vision. It uses standard middleware and libraries such as ROS 2 or OpenCV.

Nowadays, Robotics Academy offers the student up to 26 exercises. All of them come ready to use in the RoboticsAcademy docker image (RADI). The only requirement for the students its to download the docker image, all the dependencies are installed inside the RADI.

Currently, exercises can be solved using Python with our Hardware Abstraction Layer (HAL) or directly using ROS 2 interfaces (topics and services). Right now there are 2 exercises that also support C++: follow line and vacuum cleaner. The goal of this project would be to expand the selection of exercises that support the C++ language.

**Skills required/preferred**: Python, C++, ROS2**Difficulty rating**: Medium**Expected results**: Extend C++ support for more exercises providing a simplified API and direct ROS**Expected size**: 90h**Mentors**: Javier Izquierdo Hernández (javizqh AT pm.me), Nikhil Gupta

## Project #3: Robotics Academy: New power tower inspection using deep learning

**Brief explanation**: The goal of this project is to develop a new deep learning based challenge in [RoboticsAcademy](/ideas/jderobot/roboticsacademy) for power tower inspection. In addition to the existing [classical power inspection](/ideas/jderobot/roboticsacademy-exercises-drones-power_tower_inspection) exercise, this project will introduce a new challenge where defect detection and classification are performed using a deep learning model trained and provided by the student, instead of relying on traditional image processing techniques. The expected work for this project includes:

- Create new exercise, following the example of previous deep learning based exercises such as
[end-to-end visual control](/ideas/jderobot/roboticsacademy-exercises-autonomouscars-end_to_end_visual_control). - Extend or create simulated power tower environments and record and label datasets for students to train their models on.
- Build comprehensive documentation, upload datasets to accessible repositories, and provide Jupyter Notebooks or similar materials to guide students.
- Extend the
*Simple API*used by deep learning exercises to define a structured way of setting results such as classification logits, bounding boxes for detection, and confidence scores.

**Skills required/preferred**: Python, PyTorch, Deep Learning, ROS2, Gazebo**Difficulty rating**: Medium**Expected results**: New deep learning based power tower inspection exercise with comprehensive docs and learning materials.**Expected size**: Medium (~175h)**Mentors**: David Pascual Hernández (d.pascualhe AT gmail.com), Md. Shariar Kabir (skabircp08 AT gmail.com), Luis Roberto Morales (lrmoralesiglesias AT gmail.com)

## Project #4: RoboticsAcademy: drone-cat-mouse chase exercise, two controlled robots at the same time

**Brief explanation**: The goal of this project is to recover the drone-cat-mouse chase challenge in the new [RoboticsAcademy](/ideas/jderobot/roboticsacademy) architecture. This exercise requires the support for two robotics applications connected to the corresponding drones, one connected to the mouse-drone (which may fly autonomously following a 3D position pattern) and the second connected to the cat-drone. The RoboticsAcademy user has to program the cat-drone so it successfully chases the drone-mouse. This challenge should work in Gazebo Harmonic and use Aerostack2 middleware for drones, as all current available drone exercises at RoboticsAcademy. Additional exercises involving two concurrent agents in the same robotic world may also be designed using this plumbing.

**Skills required/preferred**: Python, Gazebo, Linux processes**Difficulty rating**: Medium**Expected results**: A new drone-cat-mouse chase exercise, new internal architecture supporting two simultanous agents in RoboticsAcademy challenges and comprehensive technical documentation.**Expected size**: Long (~350h)**Mentors**: José María Cañas (josemaria.plaza AT gmail.com) and Prajyot (prajyotj04 AT gmail.com)

## Project #5: Robotics Academy: using the Open3DEngine as robotics simulator

**Brief explanation**: Open 3D Engine (O3DE) is an Apache 2.0-licensed multi-platform 3D engine that enables developers and content creators to build AAA games, cinema-quality 3D worlds, and high-fidelity simulations. It supports also simulation of most common robot sensors and actuators. The idea of this project is to integrate Open3DEngine into the RoboticsAcademy framework, with at least one exercise using it instead of Gazebo.

**Skills required/preferred**: C++ programming, ROS**Difficulty rating**: Medium**Expected results**: A new robotics exercise in RoboticsAcademy using the Open3DEngine**Expected size**: 175h**Repository Link**-[Open 3D Engine](https://github.com/o3de/o3de),[RoboticsAcademy](https://github.com/JdeRobot/RoboticsAcademy),[RoboticsInfrastructure](https://github.com/JdeRobot/RoboticsInfrastructure)**Mentors**: José M. Cañas (josemaria.plaza AT gmail.com) and Pedro Arias (pedro.ariasp AT upm.es)

## Project #6: VisualCircuit: Improving Functionality & Expanding the Block Library

**Brief explanation**: VisualCircuit allows users to program robotic intelligence using a visual language similar to electronic circuits, simplifying the creation of code for robotics applications such as Deep Learning, ROS, and more.

Over the past few years, we have focused on making VisualCircuit more robust by resolving Nested Blocks (multi-level blocks) with the Block Composition feature, developing a working prototype for dockerized execution of robotics applications directly from the browser, migrating the old POSIX IPC implementation to a cross-platform compatible Python Shared Memory implementation, and more.

For GSoC 2026, this project aims to improve and expand the VisualCircuit block library, enabling contributors to publish reusable blocks in a structured and validated manner. Each block will include metadata, execution logic, and visual assets, while automated CI pipelines will validate contributions. Alongside this infrastructure, the project will focus on developing high-quality reusable blocks and complete end-to-end robotics applications using VisualCircuit. The VisualCircuit frontend will integrate the block library as a built-in marketplace, allowing users to browse, install, and reuse blocks with minimal effort, while ensuring offline usability and seamless execution identical to native blocks.
You can read further about the tool on the [website](/ideas/jderobot/visualcircuit).

**Skills required/preferred**: ROS2, Gazebo, Python, TypeScript**Difficulty rating**: Medium**Expected results**: Expanding Block library for VisualCircuit, improving automated testing using GitHub Actions and creating real world robotics applications developed with latest functionalities of VC and resolving other major issues.**Expected size**: 175h**Mentors**: Toshan Luktuke (toshan1603 AT gmail.com) and Pankaj Borade (borade.pankaj825 AT gmail.com).

## Project #7: Robotics Academy: Exploring optimization strategies for RoboticsBackend container

**Brief explanation**: Our [Robotics Academy](/ideas/jderobot/roboticsacademy-2) platform relies on a containerized environment that encapsulates robotics middleware, simulators, libraries, and the application management stack: the **RoboticsBackend**. This approach significantly lowers the technical entry barrier for students, allowing them to start learning robotics without dealing with complex environment setup. However, the large number of coexisting dependencies causes the container image to grow substantially in size, negatively affecting maintainability and increasing download times for first time users.

This project has a twofold objective. First, it aims to identify bottlenecks in the current container build and propose concrete strategies to reduce image size and build time. Potential approaches include layer optimization, dependency pruning, replacing heavy libraries such as OMPL when viable, and providing minimal installation variants for components like Aerostack2. Second, the project will explore alternative container technologies, such as Podman, as a replacement for Docker in the build pipeline. Podman offers a daemonless and rootless execution model while maintaining compatibility with existing container workflows, potentially improving security, portability, and maintainability.

**Skills required/preferred**: Docker, Linux fundamentals, familiarity with common robotic software stack**Difficulty rating**: Medium**Expected results**: An optimized RoboticsBackend and a feasibility study of migration to Podman**Expected size**: 175h**Mentors**: Nikhil Gupta and Miguel Fernández

## Project #8: Robotics Academy: palletizing with an industrial robot exercise

**Brief explanation**: A few years ago we developed some exercises on industrial robots using MoveIt1 and ROS1-Noetic. A Work-In-Progress from the JdeRobot Industrial Robotics Working Group is the support in RoboticsAcademy to MoveIt2 and ROS2. Currently two exercises are available: (a) the Pick and Place application and (b) the MachineVision application (from GSoC-2025). The main goal of this project is to create a palletizing exercise with an industrial robot (UR5) over the base of the current exercises at RoboticsAcademy using ROS2, MoveIt2 and the easy API for the programming of industrial robots (similar to other solutions such as RAPID from ABB) already available.

**Skills required/preferred**: C++ programming, Python, ROS, MoveIt**Difficulty rating**: Medium**Expected results**: A new robotics exercise in RoboticsAcademy using an industrial robot for palletizing application**Expected size**: 350h**Repository Link**-[RoboticsAcademy](https://github.com/JdeRobot/RoboticsAcademy),[RoboticsInfrastructure](https://github.com/JdeRobot/RoboticsInfrastructure)**Mentors**: José M. Cañas (josemaria.plaza AT gmail.com) and Shu Xiao (shuxiao19980101 AT gmail.com)

# Application Instructions for GSoC 2026

If you are interested in applying for GSoC with our organization, we highly encourage you to start contributing and engaging with the relevant repositories early on. This helps you become familiar with the codebase and development workflow while allowing mentors to get to know you and your technical skills.

## Getting Started

First, explore the specific project(s) you are interested in:

Check[RoboticsAcademy](/ideas/jderobot/roboticsacademy):[this GitHub Discussion thread](https://github.com/JdeRobot/RoboticsAcademy/discussions/3381)for initial setup and guidance.Check[PerceptionMetrics](/ideas/jderobot/perceptionmetrics):[this GitHub Discussion thread](https://github.com/JdeRobot/PerceptionMetrics/discussions/124)for initial setup and guidance.Read the[VisualCircuit](/ideas/jderobot/visualcircuit):[official documentation](https://jderobot.github.io/VisualCircuit/docs/), explore the[repository](https://github.com/JdeRobot/VisualCircuit), and reach out to the mentors.

## Communication & Proposals

Once you have a feel for the workflow and have identified your preferred project(s), we recommend reaching out to the project mentors directly. If you decide to apply, **sharing your proposal via Google Docs** with the mentors is highly recommended. This allows us to provide feedback and suggestions before the final submission deadline, significantly improving your chances of success.

## Technical Demo Challenge

As part of your application, you must provide a short screen recording (1–2 minutes) demonstrating your proficiency with our ecosystem. This verifies that your development environment is functional and that you can successfully use our core tools.

Please choose the task that **most closely aligns with the project(s) you are applying for**:

**RoboticsAcademy:**Record a working solution for at least one challenge (e.g., Follow Line, Drone Cat and Mouse).**⚠️ IMPORTANT:**To protect your work, you**must blur or hide your code**in the recording. Focus the video on the robot’s behavior and the simulation results.**PerceptionMetrics:**Walk through at least one tutorial notebook in our repository and demonstrate interaction with our GUI.**VisualCircuit:**Demonstrate a simple, functional circuit built using the tool.

### Submission & Sharing

Upload your video to YouTube (set to **Unlisted** or **Public**) or Google Drive (ensure permissions are set to **“Anyone with the link can view”**). You will need to provide this link in the application form.

### Showcase Your Work!

We love seeing our community grow. We encourage you to share your progress on social media! Tag us **@jderobot** on X and LinkedIn—we’d love to see what you’ve built.

## Application Form

After you have engaged with the codebase, contacted your mentors, and completed your technical demo, you are ready to apply! Filling out the application form is a **mandatory** step in our process. You can find the form [here](https://forms.gle/fwtDfbMngSppqDad7).

# Previous GSoC students

[Ashish Ramesh](https://github.com/TheRoboticsClub/gsoc2025-Ashish_Ramesh)(GSoC 2025) Robotics-Academy: support for solutions directly using ROS2 topics[Abdallah Ibrahim Ismail](https://github.com/TheRoboticsClub/gsoc2025-Abdallah_Ibrahim_Ismail)(GSoC 2025) Robotics-Academy: CI & Testing[Md. Shariar Kabir](https://github.com/TheRoboticsClub/gsoc2025-Md_Shariar_Kabir)(GSoC 2025) Robotics-Academy: new exercise on End-to-End Visual Control of an Autonomous Vehicle using DeepLearning[Nikhil Gupta](https://github.com/TheRoboticsClub/gsoc2025-Nikhil_Gupta)(GSoC 2025) Robotics Academy: improvement of Gazebo scenarios and robot models[Shu Xiao](https://github.com/TheRoboticsClub/gsoc2025-Shu_Xiao)(GSoC 2025) Robotics Academy: improvement of industrial robotics exercises with MoveIt2 and ROS2[Javier Izquierdo](https://github.com/TheRoboticsClub/gsoc2025-Javier_Izquierdo)(GSoC 2025) BT-Studio: a tool for programming robots with Behavior Trees[Sakhineti Praveena](https://github.com/TheRoboticsClub/gsoc2025-Sakhineti_Praveena)(GSoC 2025) Extend DetectionMetrics: GUI, CI Workflow, and Object Detection[Prajyot Jadhav](https://github.com/TheRoboticsClub/gsoc2024-Prajyot_Jadhav)(GSoC-2024) Robotics-Academy: migration to Gazebo Fortress[Mihir Gore](https://github.com/TheRoboticsClub/gsoc2024-Mihir_Gore)(GSoC-2024) Robotics-Academy: improve Deep Learning based exercises[Pankaj Borade](https://github.com/TheRoboticsClub/gsoc2024-Pankaj_Borade)(GSoC-2024) VisualCircuit: block library[Óscar Martínez](https://github.com/TheRoboticsClub/gsoc2024-Oscar_Martinez)(GSoC-2024) BT-Studio: a tool for programming robots with Behavior Trees[Zebin Huang](https://github.com/TheRoboticsClub/gsoc2024-ZebinHuang)(GSoC-2024) End-to-end autonomous vehicle driving based on text-based instructions: research project regarding Autonomous Driving + LLMs[Pawan Wadhwani](https://github.com/TheRoboticsClub/gsoc2023-Pawan_Wadhwani)(GSoC-2023) Robotics Academy: migration to ROS2 Humble[Meiqi Zhao](https://github.com/TheRoboticsClub/gsoc2023-Meiqi_Zhao)(GSoC 2023) Obstacle Avoidance for Autonomous Driving in CARLA Using Segmentation Deep Learning Models[Siddheshsingh Tanwar](https://github.com/TheRoboticsClub/gsoc2023-Siddheshsingh_Tanwar)(GSoC 2023) Dockerization of Visual Circuit[Prakhar Bansal](https://github.com/TheRoboticsClub/gsoc2023-Prakhar_Bansal)(GSoC 2023) RoboticsAcademy: Cross-Platform Desktop Application using ElectronJS[Apoorv Garg](https://theroboticsclub.github.io/gsoc2022-Apoorv_Garg/)(GSoC-2022) Improvement of Web Templates of Robotics Academy exercises[Toshan Luktuke](https://theroboticsclub.github.io/gsoc2022-Toshan_Luktuke/)(GSoC-2022) Improvement of VisualCircuit web service[Nikhil Paliwal](https://theroboticsclub.github.io/gsoc2022-Nikhil_Paliwal/)(GSoC-2022) Optimization of Deep Learning models for autonomous driving[Akshay Narisetti](https://theroboticsclub.github.io/gsoc2022-Akshay_Narisetti/)(GSoC-2022) Robotics Academy: improvement of autonomous driving exercises[Prakarsh Kaushik](https://theroboticsclub.github.io/gsoc2022-Prakarsh_Kaushik/)(GSoC-2022) Robotics Academy: consolidation of drone based exercises[Bhavesh Misra](https://theroboticsclub.github.io/gsoc2022-Bhavesh_Misra/)(GSoC-2022) Robotics Academy: improve Deep Learning based Human Detection exercise[Suhas Gopal](https://theroboticsclub.github.io/gsoc2021-Suhas_Gopal/)(GSoC-2021) Shifting VisualCircuit to a web server[Utkarsh Mishra](https://theroboticsclub.github.io/gsoc2021-Utkarsh_Mishra/)(GSoC-2021) Autonomous Driving drone with Gazebo using Deep Learning techniques[Siddharth Saha](https://theroboticsclub.github.io/gsoc2021-Siddharth_Saha/)(GSoC-2021) Robotics Academy: multirobot version of the Amazon warehouse exercise in ROS2[Shashwat Dalakoti](https://theroboticsclub.github.io/gsoc2021-Shashwat_Dalakoti/)(GSoC-2021) Robotics-Academy: exercise using Deep Learning for Visual Detection[Arkajyoti Basak](https://theroboticsclub.github.io/gsoc2021-Arkajyoti_Basak/)(GSoC-2021) Robotics Academy: new drone based exercises[Chandan Kumar](https://theroboticsclub.github.io/gsoc2021-Chandan_Kumar/)(GSoC-2021) Robotics Academy: Migrating industrial robot manipulation exercises to web server[Muhammad Taha](https://theroboticsclub.github.io/colab-gsoc2020-Muhammad_Taha/)(GSoC-2020) VisualCircuit tool, digital electronics language for robot behaviors.[Sakshay Mahna](https://theroboticsclub.github.io/colab-gsoc2020-Sakshay_Mahna/)(GSoC-2020) Robotics-Academy exercises on Evolutionary Robotics.[Shreyas Gokhale](https://theroboticsclub.github.io/colab-gsoc2020-Shreyas_Gokhale/)(GSoC-2020) Multi-Robot exercises for Robotics Academy In ROS2.[Yijia Wu](https://theroboticsclub.github.io/colab-gsoc2020-Yijia_Wu/)(GSoC-2020) Vision-based Industrial Robot Manipulation with MoveIt.[Diego Charrez](https://theroboticsclub.github.io/colab-gsoc2020-Diego_Charrez/logbook/)(GSoC-2020) Reinforcement Learning for Autonomous Driving with Gazebo and OpenAI gym.[Nikhil Khedekar](https://theroboticsclub.github.io/colab-gsoc2019-Nikhil_Khedekar/)(GSoC-2019) Migration to ROS of drones exercises on JdeRobot Academy[Shyngyskhan Abilkassov](https://theroboticsclub.github.io/colab-gsoc2019-Shyngyskhan_Abilkassov)(GSoC-2019) Amazon warehouse exercise on JdeRobot Academy[Jeevan Kumar](https://theroboticsclub.github.io/colab-gsoc2019-Jeevan_Kumar/)(GSoC-2019) Improving DetectionSuite DeepLearning tool[Baidyanath Kundu](https://theroboticsclub.github.io/colab-gsoc2019-Baidyanath_Kundu/)(GSoC-2019) A parameterized automata Library for VisualStates tool[Srinivasan Vijayraghavan](https://theroboticsclub.github.io/colab-gsoc2019-Srinivasan_Vijayraghavan/)(GSoC-2019) Running Python code on the web browser[Pankhuri Vanjani](https://theroboticsclub.github.io/colab-gsoc2019-Pankhuri_Vanjani/)(GSoC-2019) Migration of JdeRobot tools to ROS 2[Pushkal Katara](https://wiki.jderobot.org/Club-PushkalKatara)(GSoC-2018) VisualStates tool[Arsalan Akhter](https://wiki.jderobot.org/Club-aakhter)(GSoC-2018) Robotics-Academy[Hanqing Xie](https://wiki.jderobot.org/Club-hanqingxie)(GSoC-2018) Robotics-Academy[Sergio Paniego](https://wiki.jderobot.org/Club-spaniego)(GSoC-2018) PyOnArduino tool[Jianxiong Cai](https://wiki.jderobot.org/Club-jianxiong)(GSoC-2018) Creating realistic 3D map from online SLAM result[Vinay Sharma](https://wiki.jderobot.org/Club-VinaySharma)(GSoC-2018) DeepLearning, DetectionSuite tool[Nigel Fernandez](https://wiki.jderobot.org/Ni9elf-colab)GSoC-2017[Okan Asik](https://wiki.jderobot.org/Okanasik-colab)GSoC-2017, VisualStates tool[S.Mehdi Mohaimanian](https://wiki.jderobot.org/index.php?title=Deep_Reinforcement_Learning_in_Robotic&redirect=no)GSoC-2017[Raúl Pérula](https://wiki.jderobot.org/Raulperula-colab)GSoC-2017, Scratch2JdeRobot tool[Lihang Li](https://wiki.jderobot.org/Hustcalm-colab): GSoC-2015, Visual SLAM, RGBD, 3D Reconstruction[Andrei Militaru](https://wiki.jderobot.org/Militaru92-colab)GSoC-2015, interoperation of ROS and JdeRobot[Satyaki Chakraborty](https://wiki.jderobot.org/Chakraborty-colab)GSoC-2015, Interconnection with Android Wear
