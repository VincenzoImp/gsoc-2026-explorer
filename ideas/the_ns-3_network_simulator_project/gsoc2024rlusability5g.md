# ns-3 gym

**Parent:** The ns-3 Network Simulator Project — Project Ideas
**Source:** https://www.nsnam.org/wiki/GSOC2024RLUsability5G
**Scraped:** 2026-02-22T23:28:47.555601

---

# GSOC2024RLUsability5G

[Jump to navigation](https://www.nsnam.org#mw-head)

[Jump to search](https://www.nsnam.org#searchInput)

[Main Page](https://www.nsnam.org/wiki/Main_Page) - [Roadmap](https://www.nsnam.org/wiki/Roadmap) - [Summer Projects](https://www.nsnam.org/wiki/Summer_Projects) - [Project Ideas](https://www.nsnam.org/wiki/Project_Ideas) - [Developer FAQ](https://www.nsnam.org/wiki/Developer_FAQ) - [Tools](https://www.nsnam.org/wiki/Tools) - [Related Projects](https://www.nsnam.org/wiki/Related_Projects)

[HOWTOs](https://www.nsnam.org/wiki/HOWTOs) - [Installation](https://www.nsnam.org/wiki/Installation) - [Troubleshooting](https://www.nsnam.org/wiki/Troubleshooting) - [User FAQ](https://www.nsnam.org/wiki/User_FAQ) - [Samples](https://www.nsnam.org/wiki/Category:Samples) - [Models](https://www.nsnam.org/wiki/Category:Models) - [Education](https://www.nsnam.org/wiki/Education) - [Contributed Code](https://www.nsnam.org/wiki/Contributed_Code) - [Papers](https://www.nsnam.org/wiki/Papers)

Back to [ GSoC 2024 projects](https://www.nsnam.org/wiki/Summer_Projects#Google_Summer_of_Code_2024)

## Project Overview

**Project Name:**Enhancement of RL Approach Accessibility in NR**Student:**Hyerin Kim**Mentors:**Katerina Koutlia, Amir Ashtari, Biljana Bojovic, Gabriel Ferreira**Google page:**[https://summerofcode.withgoogle.com/programs/2024/projects/vPuZgTe1](https://summerofcode.withgoogle.com/programs/2024/projects/vPuZgTe1)**Project Goals:**In this project, I will design a new RL based MAC scheduler of NR and implement it in 5g-lena integrating with ns3-gym. Additionally, I will enhance the usability of 5G-lena in terms of RL approach by providing an example using the designed RL based scheduler.**Repository:**[https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/tree/gsoc24-nr-usability?ref_type=heads](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/tree/gsoc24-nr-usability?ref_type=heads)(fork nr GitLab)**MR:**[cttc-lena/nr!166](https://gitlab.com/cttc-lena/nr/-/merge_requests/166)**About Me:**I am currently pursuing a Master's degree in Computer Science and Engineering at Seoul National University, South Korea. My research at the Mobile Computing & Communications Laboratory focuses on resource allocation methods in NR V2X Sidelink. As an undergraduate, I conducted research on improving spatial reuse in dense Wi-Fi environments and implemented a Reinforcement Learning (RL)-based modified OBSS/PD algorithm using ns3 gym. I believe that participating in GSoC 2024 presents an excellent opportunity for me to contribute to enhancing the usability of 5G and RL experiences on ns-3, while also deepening my understanding of 5G technology, mechanisms, and system architecture.

## Milestones

The planned milestones are outlined below

### Phase1. Design example (3 weeks)

- Familiar with 5g-lena
*(2 weeks)* - Design Scenario (e.g., UEs deployment, UEs speed, cell configuration, …)
*(1 week)*

- - Define Assumption (e.g., delay, TDMA/OFDMA, …)


### Phase2. Design RL based Scheduler (6 +1 weeks)

- Design scheduler
*(2 weeks)*

- - input/output
- - goal of optimization


- Design RL process
*(1 week)*

- - Define suitable RL techniques considering optimization objective of the scheduler and computational complexity


- Implementation of RL based scheduler in 5g lena
*(3 +1 weeks)*

- - Create the test
- - Create documentation
- - Create MR to 5g lena
**(Milestone 1)**


### Phase3. RL Integration (4 weeks)

- Design RL framework
*(1 week)*

- - Define RL technique


- Develop gym scripts
*(3 weeks)*

- - Develop gym python scripts
- - Develop ns3 gym interface in RL 5g lena example
- - Validate RL process of the example
- - Create MR to 5g lena
**(Milestone 2)**


### Phase4. Evaluation (3 +1 weeks)

- Evaluate the result of example compared with other schedulers

- - Write simulation campaign scripts
- - Execute scripts
- - Plotting python scripts


- Address review comment of the MR 1 and 2
- Update MR 1 and 2 with necessary modification
- Create brief description of the work and the results for 5g lena blog
**(Milestone 3)**

## Weekly Report

### Week 1 [May 27 - Jun. 02]

Familiarity with 5g-lena (1)

- Studied cttc-nr-demo example with cttc-nr-demo tutorial

- ৹ quasi-ideal assumption
- ৹ RAN Lifecycle (i.e. downlink packet flow from gNB to UE)
- ৹ How to configure the scenario, EPC, physical layer, and traffic(application)
- ৹
*(DOUBT)*What do I consider when I configure bands, carrier component, BWP?


### Week 2 [Jun. 03 - Jun. 09]

Familiar with 5g-lena (2)

- Organized the concepts of Band, CC, and BWP to address the issue from the previous week

- Studied schedulers in 5g-lena

- ৹ Studied MAC Layer section related to schedulers in NR module documentation
- ৹ Studied cttc-nr-simple-qos-sched example


### Week 3 [Jun. 10 - Jun. 16]

Design Scenario

- Analyzed the QoS Scheduler in 5g-lena

- ৹ Page:
[QoS Scheduler Simulation Results Analysis](https://mye280c37.github.io/posts/gsoc2024-02/) - ৹ Reference: Koutlia, Katerina, Sandra Lagén, and Biljana Bojovic. "Enabling QoS Provisioning Support for Delay-Critical Traffic and Multi-Flow Handling in ns-3 5G-LENA." Proceedings of the 2023 Workshop on ns-3. 2023.

- ৹ Page:

- Created an initial example code

- ৹ Created the example based on the example named 'cttc-nr-simple-qos-sched'
- ৹ Altered the default UE count to 3, assigning each UE a single QoS flow represented by 5QI indices 1, 80, and 87, which denote GBR, non-GBR, and Delay Critical GBR resource types, respectively
- ৹ Commit:
[Add new example cttc-nr-initial-my-sched](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/commit/80523b0b9baf3199554e1d0b72a4682ef560b62e)


### Week 4 [Jun. 17 - Jun. 23]

Design Scheduler (1)

- Modified the initial example

- ৹ Added a new parameter `numTrafficProfile`
- ‣ Specified the flow profile based on the number of traffic types. Possible values are 2 and 3
- ‣ If the `numTrafficProfile` is 2, two types of traffic (5QI 80, 87), same as ‘cttc-nr-multi-flow-qos-sched’, is installed in 3 UEs. Two UE have 5QI 80 traffic and the other has 5QI 87 traffic
- ‣ If the `numTrafficProfile` is 3, three types of traffic (5QI 1, 80, 87), as defined initially, is installed in 3 UEs repectively.


- ৹ Commit:
[Add a parameter for the number of traffic types](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/commit/7eafd7d5cd173a1d3e25603c53065e50966945cb)

- ৹ Added a new parameter `numTrafficProfile`

- Evaluated the QoS scheduler in various scenarios

- ৹ Evaluated the results when non-GBR and DC GBR are installed in different UEs to verify the simulation results analysis from the previous week
- ৹ As a result of this evaluation, I observed that all non-GBR traffic experienced more severe delays compared to DC GBR traffic
- ৹ From my analysis of the simulation results in the QoS scheduler paper, non-GBR traffic benefits when the UE with non-GBR traffic also has DC GBR traffic in a multi-flow configuration.
- ৹ Page:
[QoS Scheduler Evaluation](https://mye280c37.github.io/posts/gsoc2024-03/)


- Designed a new scheduler

- ৹ Made the assumption that all UEs have a single flow for simplicity (extend it further to multi-flow after achieving the first goal)
- ৹ Decided the goals of the scheduler
- ‣ Option 1: Minimize the total delay of the gNB
- ‣ Option 2: The scheduler schedules UEs to meet their PDB requirements (primary goal). Among DC-GBR and other types of traffic, DC-GBR traffic has higher priority in scheduling (secondary goal)




### Week 5 [Jun. 24 - Jun. 30]

Design Scheduler (2)

- The scheduler is designed to be user-friendly and easy to reuse

- ৹ To facilitate ease of reuse, the scheduler's design should be simple and easily understandable
- ৹ For simplicity, the goal of the scheduler is to minimize the total delay of the gNB while considering the priority of each attached UE
- ‣ As analyzed before, one of the issues in the QoS scheduler is the unfairness of delay between DC-GBR and other types of traffic
- ‣ To address this issue, the designed scheduler focuses on minimizing the total delay


- ৹ Page:
[Scheduler Design](https://mye280c37.github.io/posts/gsoc2024-04/) - ৹
**TBD:**the reward function


### Week 6 [Jul. 01 - Jul. 07]

Design RL Process

- Decided how to implement the designed RL-based scheduler in 5g-lena and ns3-gym

- ৹ Visualized the sequence UML diagram of the scheduling process among `NrMacSchedulerTdma`, `NrMacSchedulerTdmaQos`, and `NrMacSchedulerUeInfoQos`
- ৹ Based on the communication logic between 5g-lena and ns3-gym, designed the sequence UML diagram and the class UML diagram for the RL process
- ‣ The existing TDMA and OFDMA scheduler classes assign resources to UEs, calling their methods per UE
- ‣ However, the RL-based scheduler should transfer data, including data about all UEs
- ‣ Thus, `NrMacSchedulerTdmaAI` and `NrMacSchedulerOfdmaAI` will inherit from `NrMacSchedulerTdma` and `NrMacSchedulerOfdma`, respectively, and override `AssignDLRBG()` and `AssignULRBG()`. They will then perform the RL process by calling the `Notify()` method of the `OpenGymEnv` in the ns3-gym module, transferring the data about all UEs


- ৹ Diagram: AI Scheduler Diagram (
[Google Docs](https://docs.google.com/document/d/1n6u4pbRRItiNC5UgIYZiVjhuwZZl4bwsOz3BELxme4Q/edit?usp=sharing),[draw.io](https://drive.google.com/file/d/1NZMoSk6l0MX3IGXuHlEmaVupeOneHciU/view?usp=sharing))


### Week 7 [Jul. 08 - Jul. 14]

Implementation of RL-based scheduler in 5g lena (1)

- Created a
[MR](https://gitlab.com/cttc-lena/nr/-/merge_requests/166)to share the development progress - Developed the skeleton of the RL-based scheduler on the 5g-lena side

- ৹ Created the class skeleton
- ‣
*(THOUGHT)*The functions used for scheduling resources to UEs and the functions used for communicating with ns3-gym are the same in both TDMA and OFDMA schedulers. How about separating these functions into a class such as `NrMacSchedulerAIAlgorithm`?

- ‣

- ৹ Developed the logic for calling the ns3-gym environment in the `AssignDLRBG` function of the `NrMacSchedulerOfdmaAI` class
- ৹ Managed a week's work as a
[milestone](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/milestones/2#tab-issues). The issues pertaining to this milestone are as follows:

- ৹ Created the class skeleton

- Modified the UML diagram to reflect the characteristics of a constant function in a class and that of the variable `ueVector`

- ৹ In the AssignDLRBG function, the vector used for getting observations is assigned to a local variable named `ueVector`. Due to the characteristics of a constant function, `ueVector` can only be passed to other constant functions through input. Therefore, by defining a function named `CallNotifyFn()` that takes `ueVector` as an input, the function first transfers the information, including the observation, to `OpenGymEnv` in ns3-gym. It then calls the `Notify` function of `OpenGymEnv` to transfer this information to the Python gym through `OpenGymInterface`.
- ৹
*(DISCUSSION)*When getting observations of all UEs, the function `GetUeObservation()` in `NrMacSchedulerUeInfoAI` is called for each UE. This can be implemented in either `NrMacSchedulerOfdmaAI`/`NrMacSchedulerTdmaAI` or `OpenGymEnv`. In the former case, the clarity of the classes is maintained, but the sequence diagram becomes more complex. In the latter case, the sequence diagram can remain simple. Which approach is better?


### Week 8 [Jul. 15 - Jul. 21]

Implementation of RL-based scheduler in 5g lena (2)

- Developed the RL-based scheduler on the 5g-lena side

- ৹ Developed a class for UE information, including the data needed for RL-based scheduling
- ৹ Developed classes for RL-based resource allocation in OFDMA and TDMA
- ৹ Modified functions for assigning RBGs in OFDMA and TDMA scheduler classes to implement the RL-based scheduler


- Managed a week's work as a
[milestone](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/milestones/3#tab-issues). The issues pertaining to this milestone are as follows:

- Created draft documentation corresponding to the developed code

*(DISCUSSION)*: Our developed classes call an RL model for each available symbol. How about adding functions to call the RL model for each slot, including information about available symbols in a slot as an observation?

### Week 9 [Jul. 22 - Jul. 28]

Implementation of RL-based scheduler in 5g lena (3) : Code Refactoring based on the comments in [MR](https://gitlab.com/cttc-lena/nr/-/merge_requests/166)
(Managed a week's work as a [milestone](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/milestones/5#tab-issues).)

- Remove duplicate functions

- ৹ Remove functions that are duplicated with the classes related to QoS
- ৹ Issue:
[Remove duplicate functions](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/issues/8)


- Improve the clarity and detail of structures

- ৹ Change the structure of observation
- ‣ Create the LcObservation structure which represents the observation of a active flow
- ‣ The observation of a UE becomes a vector of LcObservation
- ‣ The observation of a scheduler becomes a vector of LcObservation


- ৹ Add the details of the comparison weights function to call the functions of the QoS when AI is not activated
- ৹ Issue:
[Improve the clarity and detail of structures](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/issues/9)

- ৹ Change the structure of observation

- Improve the Doxygen documentation

- ৹ Expand the doxygen of the classes related with the RL-based scheduler
- ৹ Expand the descriptions about the RL-based scheduler in nr-module.rst
- ৹ Fix the documentation in the 'cttc-nr-rl-based-sched' example
- ৹ Issue:
[Improve the Doxygen documentation](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/issues/10)


- Fix CI/CD errors

- ৹ Fix check-style-clang-format errors
- ৹ Fix clang-tidy errors
- ৹ Issue:
[Fix CI/CD errors](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/issues/11)


### Week 10 [Jul. 29 - Aug. 04]

Implementation of RL-based scheduler in 5g lena (4): Familiarity with the test code

- Discussed the test code for the RL-based scheduler

- ৹ Decided to create unit test code for the function `CallNotifyDl`
- ‣ The test will check the first call of the function `CallNotifyDl`


- ৹ If the test succeeds, it satisfies the following conditions:
- ‣ The observations transferred by the scheduler correspond to the QoS profiles of all UEs and the initial configuration
- ‣ The transferred reward should be zero, indicating no reward on the first call
- ‣ The function for updating weights from the scheduler is called successfully



- ৹ Decided to create unit test code for the function `CallNotifyDl`

- Studied the reference test code

- ৹ By referring to “nr-test-notching.cc”, I can create a simplified SapProvider for testing, set up LC and parameters, and then call the functions that need to be tested (e.g., `CreateMac`, `CreateScheduler`, and the functions in the scheduler)
- ৹ Alternatively, by referring to “nr-test-sched.cc”, I can use a system test, trace a specific observation time, and compare it with the UE’s observation


### Week 11 [Aug. 05 - Aug. 11]

Implementation of RL-based scheduler in 5g lena (5): Create the test and refactor the code

- Refactored the code while creating the test code

- ৹ Removed redundant code
- ৹ Clarified the logic for setting the function that calls the gym class
- ‣ The conversion error occurred while using `std::bind` because the `this` pointer was continually being recognized as an input while passing the weight update function of the `NrMacSchedulerUeInfoAi` class as a function argument
- ‣ This happened because the function was not declared as `const`


- ৹ Clarified the definition of structures sent to the AI model
- ৹ Fixed minor details in the definitions of functions and parameters
- ৹ Progressed according to the
[milestone](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/milestones/4#tab-issues), and the issue related to refactoring is as follows:


- Created the unit test code according to the design discussed last week

- ৹ Issue:
[Create the test code](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/issues/14)

- ৹ Issue:

### Week 12 [Aug. 12 - Aug. 18]

Develop the ns3-gym interface in the RL 5G-LENA example

- To implement RL models using the AI scheduler, we need to define a custom gym environment by inheriting from the `OpenGymEnv` class in the ns3-gym module and then apply this in the example
- The following steps were taken to achieve this:

- ৹ Defined a custom gym environment inheriting from the `OpenGymEnv` class in the ns3-gym module
- ‣ Defined OpenGymSpace and OpenGymDataContainer to align with the observation structure and weight of the scheduler
- ‣ Defined the Notify function, which will be set as a callback for the scheduler
- ‣ Defined a variable to implement the weights update function of the scheduler, which is passed as an input to the Notify function
- ‣ Overrode the functions to ensure the proper execution of the preceding tasks


- ৹ Modified the "cttc-nr-rl-based-sched" example to apply the custom gym environment
- ৹ Modified CMakeLists.txt to build the files needed for implementing RL models and the example

- ৹ Defined a custom gym environment inheriting from the `OpenGymEnv` class in the ns3-gym module

- The details can be found in the
[milestone](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/milestones/6#tab-issues), including the following issues:

*(CHALLENGE)*Modified CMake so that the necessary files are built only if the user has the ns-3 gym module when running the python gym script example. While there are no errors in clang-tidy, build, or execution, an error occurs in the CMake format pipeline

### Week 13 [Aug. 19 - Aug. 25]

Develop a python gym script for a simple test

- Developed a simple example using only the ns-3 gym environment without implementing a specific RL Model

- ৹ Developed a simple python example that includes the arguments required to implement "Ns3Env," as well as the parameters corresponding to the "cttc-nr-rl-based-sched" example
- ৹ Executed a basic loop that samples an action for each received data point from the custom C++-based Gym environment, which consists of observation, reward, game-over status, and extra information
- ৹ Commit:
[Add a simple test implementation](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/commit/30c1361d87868d1c1d969e29523eb2ac6b554036)


- Added the parameters from python gym environment in the "cttc-nr-rl-based-sched" example

- ৹ To execute the "cttc-nr-rl-based-sched" example through the python gym script, the example must include the parameters "openGymPort" and "simSeed," which are passed by the python-based "Ns3Env"
- ৹ Commit:
[Apply the parameters used in the gym env](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/commit/332346480afcdf689e4c687a6f0bd8fabbf261e5,)


### Week 14 [Aug. 26 - Sep. 01]

Develop a python gym script for Proximal Policy Optimization (PPO) model

- Develop a python gym script for PPO model that aligns with the observations and actions of the AI scheduler

- ৹ Developed a PPO class containing the Actor-Critic component
- ৹ Using the Actor-Critic class, the PPO model selects actions and evaluates the selected actions
- ৹ Developed a Memory class that stores states, actions, and log probabilities for future updates during each action selection iteration
- ৹ The stored memory is periodically updated
- ৹ Defined arguments using 'argparse' to allow users to adjust parameters for a simple test
- ৹ Commit:
[Add draft script for PPO model](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/commit/7e2fc471a47c516676c0326f6e4d2774719787a6)


### Week 15 [Sep. 02 - Sep. 08]

Address comments in [MR](https://gitlab.com/cttc-lena/nr/-/merge_requests/166)

- Updated Doxygen documentation

- ৹ Fixed minor doxygen details in the scheduler class
- ৹ Enhanced documentation details in the .rst file


- Resolved comments on the scheduler's unit test

- ৹ Added documentation
- ৹ Removed notching-related code


### Week 16 [Sep. 09 - Sep. 15]

Address comments in [MR](https://gitlab.com/cttc-lena/nr/-/merge_requests/166)

- Revised the UE configuration in the example to align with the multi-flow qos example
- Resolved comments on the python gym scripts

- ৹ Changed the structure of the Memory class in test-ppo.py to use a dequeue
- ৹ Added descriptions for each function and class
- ৹ Added a simple debug print function
- ৹ Fixed minor issues related to variables


- Resolved other comments:

- ৹ Removed empty destructor
- ৹ Removed mask-related code
- ৹ Added descriptions to the MyGymEnv class
- ৹ Added an installation guide for the rl-based example


### Week 17 [Sep. 16 - Sep. 22]

Conduct Simulation Campaigns and Refine Models (1)

- Evaluated the AI scheduler against other schedulers: QoS, RR, PF

- ৹ Ran tests with various simulation parameters: TDMA/OFDMA, RR LC/QoS LC Assignment
- ৹ Tested with different reward functions


- Fixed and reordered state based on (RNTI, LC ID) order to prevent state shape changes when the number of active flows changes during the simulation

- ৹ Commit:
[Fix state shape bug caused by active flows](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/commit/a3d3f842a01675337cc981676fb2d6969de34f2a) - ৹ Commit:
[Support fixed format state representation](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/commit/8ea00773e73f71a89d6072f0e0de290c067bd988)

- ৹ Commit:

- Adjusted the action range to continuous values

- ৹ Commit:
[Adjust to a continuous action range](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/commit/74262f1042bbcdcce89ec0ae03a251e3a8e9cdcc)

- ৹ Commit:

### Week 18 [Sep. 23 - Sep. 29]

Conduct Simulation Campaigns and Refine Models (2)

- Evaluated the schedulers (AI, QoS, PF, and RR) in a scenario where a single gNB with a single cell is deployed with 2 UEs, each having a single flow:

- ৹ One UE has a non-GBR flow, and the other UE has a Delay-Critical (DC)-GBR flow
- ৹ OFDMA was configured with QoS LC assignment
- ৹ You can view the simulation results here:
[Simulation Campaigns](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/wikis/Simulation-Campaigns)


- Enabled CUDA support when users set the 'enableCuda' parameter to 1, provided that CUDA is available on the system, to accommodate the potential increase in the number of flows

- ৹ Commit:
[Enable torch processes on cuda](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/commit/d8cb48b5c71748e52d7b32d3f0fa7f17ef5fc32a)

- ৹ Commit:

- Adjusted the action range for active flows to avoid zero, ensuring it is distinguishable from the default action value of zero for non-active flows

- ৹ Commit:
[Adjust the action range to avoid zero](https://gitlab.com/mye280c37/5g-lena-integrated-with-ns-3-gym/-/commit/4331d17333de1ce1b415895d6a1e8ce589ccb427)

- ৹ Commit:

- Resolved the documentation-related threads in the
[MR](https://gitlab.com/cttc-lena/nr/-/merge_requests/166)

### Week 19 [Sep. 30 - Oct. 06]

Address comments in [MR](https://gitlab.com/cttc-lena/nr/-/merge_requests/166) and squash commits

- Relocated and renamed ns3-gym environment files to improve user accessibility when constructing their own examples using the ns3-gym environment

- ৹ Renamed files to 'nr-mac-scheduler-ai-ns3-gym-env.*' and class name to 'NrMacSchedulerAiNs3GymEnv'
- ৹ Moved files to 'model/' directory


- Add Doxygen to the ns3-gym environment per each functions to enhance users' understanding and enable more effective utilization of the class
- Squashed commits for merge
