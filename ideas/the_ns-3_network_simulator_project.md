# The ns-3 Network Simulator Project — Project Ideas

**Source:** https://www.nsnam.org/wiki/GSOC2026Projects
**Scraped:** 2026-02-22T23:28:47.552705

---

# GSOC2026Projects

[Jump to navigation](https://www.nsnam.org#mw-head)

[Jump to search](https://www.nsnam.org#searchInput)

[Main Page](/ideas/the-ns-3-network-simulator-project/main_page) - [Roadmap](/ideas/the-ns-3-network-simulator-project/roadmap) - [Summer Projects](/ideas/the-ns-3-network-simulator-project/summer_projects) - [Project Ideas](/ideas/the-ns-3-network-simulator-project/project_ideas) - [Developer FAQ](/ideas/the-ns-3-network-simulator-project/developer_faq) - [Tools](/ideas/the-ns-3-network-simulator-project/tools) - [Related Projects](/ideas/the-ns-3-network-simulator-project/related_projects)

[HOWTOs](/ideas/the-ns-3-network-simulator-project/howtos) - [Installation](/ideas/the-ns-3-network-simulator-project/installation) - [Troubleshooting](/ideas/the-ns-3-network-simulator-project/troubleshooting) - [User FAQ](/ideas/the-ns-3-network-simulator-project/user_faq) - [Samples](/ideas/the-ns-3-network-simulator-project/category-samples) - [Models](/ideas/the-ns-3-network-simulator-project/category-models) - [Education](/ideas/the-ns-3-network-simulator-project/education) - [Contributed Code](/ideas/the-ns-3-network-simulator-project/contributed_code) - [Papers](/ideas/the-ns-3-network-simulator-project/papers)

This page contains 2026 Google Summer of Code project ideas for ns-3.

[GSoC Frequently Asked Questions](https://developers.google.com/open-source/gsoc/faq)[ns-3's 2026 GSoC Contributor guide](/ideas/the-ns-3-network-simulator-project/gsoc2026contributorguide)[GSoC contributor/student guide (not ns-3 specific)](https://developers.google.com/open-source/gsoc/resources/guide)[2026 GSoC Contributor application template](/ideas/the-ns-3-network-simulator-project/gsoc2025applicationtemplate)[ns-3's GSoC Mentor guide](/ideas/the-ns-3-network-simulator-project/gsocmentorguide)[GSoC Mentor guide (not ns-3 specific)](https://archive.flossmanuals.net/gsocmentoring/index.html)[GSoC Contributor Selection Process](/ideas/the-ns-3-network-simulator-project/gsocselectionprocess)*Get in contact with the ns-3 team*:[ns-developers mailing list](https://groups.google.com/g/ns-developers)|*chat*[https://ns-3.zulipchat.com/](https://ns-3.zulipchat.com/)

### About the ns-3 project

ns-3 is a discrete-event network simulator, with a particular emphasis on network research and education.

Users of ns-3 can construct simulations of computer networks using models of traffic generators, protocols such as TCP/IP, and devices and channels such as WiFi, and analyze or visualize the results. Simulation plays a vital role in the research and education process, because of the ability for simulations to obtain reproducible results (particularly for wireless protocol design), scale to large networks, and study systems that have not yet been implemented. A particular emphasis in ns-3 is the high degree of realism in the models (including frameworks for real application and kernel code) and integration of the tool with virtual machine environments and testbeds; we view that researchers need to move more effortlessly between simulation, testbeds, and live experiments, and ns-3 is designed to facilitate that.

ns-3 has participated in past GSoCs during 2008-10, 2012-15, and 2017-25. We seek contributors interested in the intersection of wireless and computer networking, performance analysis, and open source software.

### Org admins

Google Summer of Code organizational admins for ns-3 are [Tommaso Pecorella](mailto:tpecorella@mac.com) and [Mohit P. Tahiliani](mailto:tahiliani.nitk@gmail.com); contact them with any questions. They also hang out on [Zulip](https://ns-3.zulipchat.com).

### Mentors

Mentors will be paired with contributors based on the projects that are selected. Mentors from companies are welcome, if the employer will permit the mentor sufficient time to perform the mentoring. Prospective mentors should notify Mohit P. Tahiliani or Tommaso Pecorella of interest. Mentors familiar with ns-3 development practices will be preferred, to improve the chances of code merge. We are going to be seeking two-person or multiple-person mentoring teams for projects, to help with the mentoring workload and bring more expertise.

The current list of prospective mentors can be found among the ideas listed below.

### How to apply

For students or contributors interested in applying to ns-3 for GSoC, please go through the following list to get started:

- Read the official
[GSoC contributor guide](https://developers.google.com/open-source/gsoc/resources/guide). - Read
[ns-3's 2026 GSoC contributor guide](/ideas/the-ns-3-network-simulator-project/gsoc2026contributorguide) - Look through our
[#Project Ideas](https://www.nsnam.org#Project_Ideas)below to see if you find a project that interests you. - Review the
[tutorial and contributing guide](/ideas/the-ns-3-network-simulator-project/documentation-development-tree)thoroughly, if you have not already done so. - Once it is posted, look through the
[GSoC application template](/ideas/the-ns-3-network-simulator-project/gsoc2024applicationtemplate)to start preparing your proposal. We will wait to see whether we are actually part of GSoC before updating the above link for 2026, but it will be similar to last year's application. - Next, proceed to get in touch with the developers on the mailing list or Zulip chat room and refine your proposal.
- In parallel, make sure you prepare a patch as per the patch requirement guidelines. Your application to ns-3 will not be considered if you do not fulfill this requirement.

Below is a list of [#Project Ideas](https://www.nsnam.org#Project_Ideas) proposed by the ns-3 team for Google Summer of Code 2026. Please note that these ideas are not limited to GSoC; anyone is welcome to work on them. Please email the [ns-developers list](https://groups.google.com/g/ns-developers) if you have a different idea that you'd like to work on, to see if a mentor may be interested. Applicants are encouraged to look over this list, pick one that especially interests them, think about it, and discuss potential approaches on the [ns-developers list](https://groups.google.com/g/ns-developers). Previous experience with the Google Summer of Code programs suggests that the more you discuss and refine your proposal on the mailing list beforehand, the stronger the proposal it will develop into, and the higher your chances of being accepted into the program.

Each project idea within a particular priority has been tagged with the following properties:


Required Experience:Languages, concepts, or packages with which applicants must be familiar.Bonus Experience:Other experience or familiarity which would be greatly helpful to applicants for this project.Interests:Areas of particular relevance to this project, and an indicator of where successful contributors might apply their experiences coming out of this project.Difficulty:easy, medium or difficultRecommended reading:pointers to documentation, papers, specific bugs, etc.Note that all of the projects require some experience and comfort with C++. Project ideas for which C++ is noted as a required experience will require more and deeper familiarity with the language. A similar notion applies to computer networking, BSD sockets, etc: Familiarity is strongly preferred, but is not required except where explicitly noted due to the topic being more advanced in that regard. A few projects are more Python-centric.


### Patch requirement guidelines

In past years, we have asked applicants to submit a patch related to an open issue or a suggested coding exercise. We are undecided at this time whether we will ask for this in 2026; check back later.

### Mentors: how to participate

The ns-3 project is open to the proposal of new project ideas by developers interested in being a GSoC mentor. For mentors who're adding project ideas to the list below, please ensure that:

- The projects are sized such that there can be a code merge by the end of the coding period. The scope of the project should be such that it is very difficult to *not* have a code merge by the end of the summer.
- The proposed projects are not too open-ended. That is, if the deliverables or a clear path to the same are not well understood, it is better kept outside GSOC.
- There should be a clear merge path to one of the main project code repositories (ns-3-dev, ns-3-dce, bake) by the end of the summer, either because the patches directly apply to these repositories, or because they apply to an ns-3 module that is in the process of being merged with ns-3-dev.

## Project Ideas

**Note to contributors:** These ideas are not listed in any priority order.
The projects can be grouped depending on their scope and/or their size. Below they are organized according to their scope. Please check each idea for details about its foreseen difficulty level.

### Internet models enhancements

[#Flent Application API in ns-3](https://www.nsnam.org#Flent_Application_API_in_ns-3)(small size project, 90h)[#Ping and TraverouteV4 enhancements](https://www.nsnam.org#Ping_and_TraverouteV4_enhancements)(small size project, 90h)[#Internet routing refactory](https://www.nsnam.org#Internet_routing_refactory)(small size project, 90h)[#AODVv2 Protocol enhancements](https://www.nsnam.org#AODVv2_Protocol_enhancements)(medium size project, 175h)[#Linux-like CAKE queue discipline for ns-3](https://www.nsnam.org#Linux-like_CAKE_queue_discipline_for_ns-3)(large size project, 350h)[#Switched Ethernet](https://www.nsnam.org#Switched_Ethernet)(large size project, 350h)

### IoT models enhancements

[#6LoWPAN mesh-under routing enhancements](https://www.nsnam.org#6LoWPAN_mesh-under_routing_enhancements)(medium size project, 175h)[#6LoWPAN neighbor discovery protocol](https://www.nsnam.org#6LoWPAN_neighbor_discovery_protocol)(medium size project, 175h)[#Mesh Link Establishment (MLE) protocol](https://www.nsnam.org#Mesh_Link_Establishment_(MLE)_protocol)(large size project, 350h)

### 5G NR models enhancements

The general idea is to improve the usability of the 5G NR module by adding new examples that help users start building scenario scripts. Also, an interesting improvement could be integration with other modules, like those for AI or visualizations. Here are some project ideas. Depending on the contributor's interest and skills we can adjust these projects' definitions.

[#OLLA Link Adaptation and Spec-Compliant TBS Calculation for 5G-LENA](https://www.nsnam.org#OLLA_Link_Adaptation_and_Spec-Compliant_TBS_Calculation_for_5G-LENA)(medium size project, 175h)[#Enabling 5G NR examples visualization](https://www.nsnam.org#Enabling_5G_NR_examples_visualization)(medium size project, 175h)[#Energy Consumption Modeling and Power-Aware Extensions for 5G-LENA](https://www.nsnam.org#Energy_Consumption_Modeling_and_Power-Aware_Extensions_for_5G-LENA)(medium size project, 250h)[#5G NR module integration with ns-3-ai](https://www.nsnam.org#5G_NR_module_integration_with_ns-3-ai)(large size project, 250h)

## Small sized projects (90 hours)

### Flent Application API in ns-3

Mentors: [Mohit P. Tahiliani](mailto:tahiliani.nitk@gmail.com)

Flexible Network Tester (Flent) is a network benchmarking tool. It is written in Python and wraps well-known network benchmarking tools (such as netperf and iperf) into aggregate, repeatable tests, such as a number of tests for Bufferbloat. A basic structure for Flent Application API in ns-3 has been developed. It is a wrapper around existing ns-3 applications. This project has four main goals: (1) update this implementation to match the current ns-3-dev, (2) integrate a JSON library properly (for Flent-style result handling) (3) validate correctness of Flent results produced by ns-3, and (4) Add more Flent-style test examples useful for ns-3 users. The goal of this project is to merge the Flent Application API into ns-3 mainline, not the app store.

*Required Experience:*Familiarity with Flent and C++ programming.*Bonus Experience:*Familiarity with applications supported in ns-3.*Interests:*Bufferbloat, TCP, AQM algorithms and ECN.*Difficulty:*Medium.*Recommended Reading:*- Flexible Network Tester [
[Paper](https://flent.org/flent-the-flexible-network-tester.pdf)] [[Tool](https://flent.org/)] [Existing Applications in ns-3](/ideas/the-ns-3-network-simulator-project/doxygen-d9-dc9-group__applications)[Prior work on Flent application API in ns-3](https://gitlab.com/tomhenderson/ns-3-dev/-/commits/flent?ref_type=heads)

- Flexible Network Tester [

### Internet routing refactory

Mentors: [Tommaso Pecorella](mailto:tommaso.pecorella@unifi.it), [TBD].

Traditionally IP routing tables are organized in tuples {Dst, DstMask, GatewayAddr}, e.g., {10.42.66.0, 255.255.255.0, 169.254.10.1}, plus other flags and data, like the interface to be used. In ns-3 this is accomplished by storing three separate objects, two Ipv[4,6]Address, and one Ipv[4Mask,6Prefix].

While this is quite simple to implement, this has some notable drawbacks, e.g., the Dst address must be a network address (Dst & ~DstMask == 0), it is not efficient (the mask or prefix could be represented by a simple integer), and more. In order to improve code readability and consistency between IPv4 and IPv6, !2645 introduces two new classes: Ipv[4,6]NetworkAddress.

The goal is to refactor the existing routing classes, along with Ipv[4,6]RotingTable classes, so that they use the new classes. The candidate should provide a clear and convincing plan to pursue the above mentioned goal, all while keeping backward compatibility. The APIs of the existing classes must be kept as they are (at most the can be deprecated), and new APIs should be introduced only where strictly necessary. Another very important requirement will be to break down the work in multiple sub-tasks, so that the merge process can be gradual.

It is not required that the candidate will update the code for all the routing schemes, but the choice of which routing algorithms will be considered during the project must be clear and motivated.

*Required Experience:*Fundamentals of IPv6 addressing and routing, C++ programming.*Interests:*IPv4 and IPv6 routing*Difficulty:*Easy.*Recommended reading:*

Possible tasks to fulfill the patch requirement:

- Use !2645 to modify all or in part the `Rip` protocol.

### Ping and TraverouteV4 enhancements

Mentors: [Tommaso Pecorella](mailto:tommaso.pecorella@unifi.it), [TBD].

The Ping and TraverouteV4 ns-3 application have some small limitations.

In particular 2 of them are annoying. 1. Neither Ping nor TracerouteV4 reacts to ICMP errors or informative messages. 2. As the name implies, TracerouteV4 is IPv4-only and can't be used on IPv6.

The goal is to remove the above mentioned limitations, all or in part. A proposal should clearly outline the plan and improvements to the existing code (e.g., the list of the ICMP messages that will be considered), and a clear breakdown of the work. For the TracerouteV4 refactoring to use IPv6 as well, the proposal must consider the Ping implementation as a guideline.

*Required Experience:*Fundamentals of IPv4, IPv6, ICMP, and ICMPv6. C++ programming.*Interests:*IPv4 and IPv6.*Difficulty:*Easy.*Recommended reading:*

Possible tasks to fulfill the patch requirement:

- MR to have Ping react to one ICMP message.

## Medium sized projects (175 hours)

### 6LoWPAN mesh-under routing enhancements

Mentors: [Tommaso Pecorella](mailto:tommaso.pecorella@unifi.it), [TBD].

The 6LoWPAN module offers a simple option to implement a multi-hop topology by using a contolled flooding. However, the implemented controlled flooding is very simple, and is not efficient in complex networks. This is mainly due to the lack of congestion control, or rather its naive implementation. Better approaches are possible, e.g., by leveraging some concepts from RFC 7731, by using SNR as a guidance, or by measuring the local network activity.

The candidate should outline the proposed approach, what parts of code are going to be affected, and how they can be enhanced.

*Required Experience:*Fundamentals of IPv6 addressing, C++ programming.*Bonus Experience:*Familiarity with mesh routing and 6LoWPAN ns-3*Interests:*IPv6 mesh routing*Difficulty:*Easy.*Recommended reading:*[Mesh-under in ns-3 6LoWPAN](/ideas/the-ns-3-network-simulator-project/docs-models-html-sixlowpan)[RFC 7731](https://datatracker.ietf.org/doc/html/rfc7731)[Meshtastic controlled flooding](https://meshtastic.org/docs/overview/mesh-algo/)[Routing by controlled flooding in communication networks](https://ieeexplore.ieee.org/document/91339)(if the document can not be accessed, PM the mentors)


Possible tasks to fulfill the patch requirement:

- The current code is hardwired, i.e., the mesh-under routing scheme is embedded into the SixLowPanNetDevice. Propose a patch to decouple it, using a SixLowPanMeshUnderRouting class to determine the "next hop". The behavior of the actual protocol should be unchanged.

### 6LoWPAN neighbor discovery protocol

Mentors: [Tommaso Pecorella](mailto:tommaso.pecorella@unifi.it), [Adnan Rashid](mailto:adnan.rashid@poliba.it).

The 6LoWPAN-ND (RFCs 4944, 6775, and 8505) is a replacement for IPv6 DAD and NDP for 6LoWPAN networks, and it is important to ensure address uniquness across a network that can potentially use different MAC/PHY layers.

There is a model for 6LoWPAN-ND, but it still not merged in the main ns-3 branch. The goal is to help merging the code (if it's not already merged) and add some features that are not yet considered in the model.

The candidate should outline in the proposal the features that are planned to be added, and a code mockup (or a complete class diagram) for said features.

*Required Experience:*Fundamentals of IPv6 addressing, C++ programming.*Bonus Experience:*Familiarity with 6LoWPAN and 6LoWPAN-ND*Interests:*IPv6 and IoT networks*Difficulty:*Easy.*Recommended reading:*

### OLLA Link Adaptation and Spec-Compliant TBS Calculation for 5G-LENA

Mentors: [Sandra Lagen](mailto:slagen@cttc.es), [Tom Henderson](mailto:tomh@tomh.org), [Biljana Bojovic](mailto:bbojovic@cttc.es), [Gabriel Ferreira](mailto:gcarvalho@cttc.es), [Katerina Koutlia](mailto:kkoutlia@cttc.es)

This project would focus on improving the realism and correctness of the CTTC 5G-LENA (NR module) by implementing Outer Loop Link Adaptation (OLLA) in the scheduling/link adaptation workflow, and by improving the Transport Block Size (TBS) calculation to be aligned with the 5G NR specification. OLLA is commonly used to track a target BLER by updating an SINR (or CQI) offset based on HARQ ACK/NACK feedback, leading to more stable and realistic link adaptation behavior. In addition, the project would include a performance evaluation comparing the new OLLA-enabled behavior against the current baseline and across multiple existing NR schedulers. The evaluation should consider throughput, latency, achieved BLER, convergence behavior, and fairness.

For starters, we would suggest adding the CTTC 5G-LENA (nr module) to ns-3 (as a module in the contrib/ directory), building and running the NR examples, and becoming familiar with the current scheduler, HARQ feedback flow, CQI/MCS selection, and TBS computation. Documentation is available here: [https://5g-lena.cttc.es/](https://5g-lena.cttc.es/). There is an overview tutorial video available here: [https://acmse.net/2021/tutorials-offered/#tut-work03](https://acmse.net/2021/tutorials-offered/#tut-work03). That is the background information.

- Required Experience: C++ programming, understanding of 5G NR MAC concepts (scheduling, CQI/MCS, HARQ), wireless networking fundamentals
- Interests: 5G NR simulations, scheduling, link adaptation, performance evaluation
- Difficulty: Medium
- Project size: Medium
- Patch requirement: See the
[description](/ideas/the-ns-3-network-simulator-project/gsoc2024patchrequirement). You can also consider some of the[nr good to start issues](https://gitlab.com/cttc-lena/nr/-/issues/?label_name%5B%5D=good%20first%20issue). Or, you can start writing some APIs for the selected project proposal. Also, if you have some previous MRs to ns-3 or the nr module, you can contact us to check whether it is enough for the patch requirement.

### Enabling 5G NR examples visualization

Mentors: [Amir Ashtari Gargari](mailto:aashtari@cttc.es), [Gabriel Ferreira](mailto:gcarvalho@cttc.es), [Biljana Bojovic](mailto:bbojovic@cttc.es) and [Katerina Koutlia](mailto:kkoutlia@cttc.es)

The main idea of this project is to allow easier visualization of 5G NR examples by integrating the NR module with some ns-3 visualization tools like NetAnim, or by implementing a kind of web-based visualization, e.g., through Jupyter notebook. The new feature should allow the visualization of already existing traces, visualization of topology, or even some new relevant simulation aspects could be considered. The idea is that users better understand how the metrics collection works, and how changing parameters can affect simulation results. In this project, we are open to other ideas on how to implement visualizations.

For starters, we would suggest adding the CTTC 5G-LENA (nr module) to ns-3, in the typical way (as a module in the contrib/ directory), then building and running the examples. After getting used to C++, then proceed to use the Python bindings, as described by the documentation: [https://www.nsnam.org/docs/manual/html/python.html#using-the-bindings-from-the-ns-3-source](/ideas/the-ns-3-network-simulator-project/docs-manual-html-python).
Documentation is available here: [https://5g-lena.cttc.es/](https://5g-lena.cttc.es/). There is an overview tutorial video available here: [https://acmse.net/2021/tutorials-offered/#tut-work03](https://acmse.net/2021/tutorials-offered/#tut-work03). That is the background information. For more specific guidelines, please view this [Google document](https://docs.google.com/document/d/1cQLIF1cdft1yj3vyWrjrxN2xDJMx8PuWaa9NP_nKf64/edit?usp=sharing).

- Required Experience: C++ and Python programming, understanding of 5G NR, LTE, and wireless networks
- Interests: 5G NR simulations
- Difficulty: Medium.
- Patch requirement: See the
[description](/ideas/the-ns-3-network-simulator-project/gsoc2024patchrequirement). You can also consider some of the[nr good to start issues](https://gitlab.com/cttc-lena/nr/-/issues/?label_name%5B%5D=good%20first%20issue). Or, you can start writing some APIs for the selected project proposal. Also, if you have some previous MRs to ns-3 or the nr module, you can contact us to check whether it is enough for the patch requirement.

### AODVv2 Protocol enhancements

Mentors: [Tommaso Pecorella](mailto:tommaso.pecorella@unifi.it), [TBD].

ns-3 contains models for proactive (DSDV and OLSR) and reactive (AODV and DSR) ad hoc routing protocols. AODVv2 is currently an IETF draft, and its implementation in ns-3 is ongoing. This project aims at enhancing the AODVv2 model for ns-3.

In particular the project should address the following points:

- Alignment with the latest drafts,
- Model finalization and testing (in particular for the IPv6 part),
- AODVv2 examples and documentation,
- "External" network routing support.

Collaboration with the draft authors is also highly suggested.

*Required Experience:*Fundamentals of IPv6 addressing, C++ programming.*Bonus Experience:*Familiarity with AODV implementations in ns-3 and AODVv2*Interests:*Ad hoc routing*Difficulty:*Medium.*Recommended reading:*

Possible tasks to fulfill the patch requirement:

[Issue #368](https://gitlab.com/nsnam/ns-3-dev/-/issues/368)- aodv: aodv parameters can be set to "impossible" values

## Large projects (350 hours)

### Mesh Link Establishment (MLE) protocol

Mentors: [Tommaso Pecorella](mailto:tommaso.pecorella@unifi.it), [Alberto Gallegos Ramonet](mailto:alramonet@is.tokushima-u.ac.jp).

The Mesh Link Establishment (MLE) is a proposed IETF protocol for establishing and configuring secure radio links in IoT networks. It was originally proposed for IEEE 802.15.4, and the IETF draft seems to be not progressing. However, MLE is being used in Thread, and it can be useful to implement it.

The goal of the project is to study the differences between the IETF version of MLE and the one being used in Thread, and propose an implementation that complies with either, or both.

*Required Experience:*Fundamentals of IPv4 and IPv6 sockets, C++ programming.*Interests:*Sockets and API interface implementation.*Difficulty:*Hard.*Recommended reading:*

Possible tasks to fulfill the patch requirement:

- TBD, contact the mentors if interested.

### Energy Consumption Modeling and Power-Aware Extensions for 5G-LENA

Mentors: [Katerina Koutlia](mailto:kkoutlia@cttc.es), [Biljana Bojovic](mailto:bbojovic@cttc.es), [Marco Miozzo](mailto:mmiozzo@cttc.es) and [Amir Ashtari Gargari](mailto:aashtari@cttc.es)

This project would add energy consumption modeling to the CTTC 5G-LENA (NR module). While 5G-LENA provides a detailed and validated simulation of the 5G NR protocol stack behavior, it currently lacks energy models for UEs and/or gNBs, limiting research on energy efficiency, green networking, 6G sustainability, and potentially AI-driven power-aware control.
The project would first evaluate reuse of the ns-3 Energy Framework (e.g., EnergySource, DeviceEnergyModel) by defining a clean interface between 5G-LENA and the energy module. If existing models are insufficient, the project would design and implement a 5G-specific device energy model (e.g., NrDeviceEnergyModel) and connect it to relevant 5G-LENA state/procedure events.
For starters, we would suggest adding the CTTC 5G-LENA (nr module) to ns-3 (as a module in the contrib/ directory), building and running the NR examples, and studying the Energy Framework integration patterns. Documentation is available here: [https://5g-lena.cttc.es/](https://5g-lena.cttc.es/). Tutorial video: [https://acmse.net/2021/tutorials-offered/#tut-work03](https://acmse.net/2021/tutorials-offered/#tut-work03).

Scope (expected deliverables):

- Energy consumption accounting for UEs and/or gNBs
- Per-state (and if feasible per-procedure) modeling, e.g.
- gNB: idle/active/sleep, TX/RX, processing; dependence on bandwidth/PRBs, TX power, MIMO layers/streams/RF chains, load
- UE: TX/RX, measurements, CSI-RS/SRS activity, beamforming-related processing, handover

- Tracing, example(s), and documentation

Optional (time permitting): a simple energy-aware scheduling extension to explore QoS trade-offs (e.g., energy-per-bit or energy-aware MIMO under GBR)

- Required Experience: C++ programming, wireless networking fundamentals (energy/state-machine modeling is a plus)
- Interests: 5G NR simulations, energy efficiency, green networking, 6G sustainability
- Difficulty: Medium
- Project size: Medium
- Patch requirement: See the
[description](/ideas/the-ns-3-network-simulator-project/gsoc2024patchrequirement). You can also consider some of the[nr good to start issues](https://gitlab.com/cttc-lena/nr/-/issues/?label_name%5B%5D=good%20first%20issue). Or, you can start writing some APIs for the selected project proposal. Also, if you have some previous MRs to ns-3 or the nr module, you can contact us to check whether it is enough for the patch requirement.

### 5G NR module integration with ns-3-ai

Mentors: [Katerina Koutlia](mailto:kkoutlia@cttc.es), [Gabriel Ferreira](mailto:gcarvalho@cttc.es), [Amir Ashtari Gargari](mailto:aashtari@cttc.es) and [Biljana Bojovic](mailto:bbojovic@cttc.es)

The objective of this project is to integrate the ns-3 5G NR module with [ns-3-ai](https://apps.nsnam.org/app/ns3-ai/). In GSoC 2024 we had a project in which 5G NR was integrated with [ns-3 gym](/ideas/the-ns-3-network-simulator-project/gsoc2024rlusability5g). While ns-3 gym is a popular ns-3 module for AI, it is limited to the application of reinforcement learning techniques in networking research. On the other hand, ns-3-ai module provides a more general solution that enables the data interaction between ns-3 and other Python-based AI frameworks, like [Tensorflow C++ APIs](https://www.tensorflow.org/api_docs/cc) and [PyTorch C++ APIs](https://pytorch.org/cppdocs/), which opens the door to use different machine learning-based techniques in 5G NR models. The correct functioning of the integration should be tested, and documented, and a fully working example using ns-3-ai should be provided. The contributor can propose a use-case scenario for matching learning. One option is to use it for MAC scheduling, but it could be used for other 5G related research problems, and the contributor is encouraged to propose the use case of his/her interest.

For starters, we would suggest adding the CTTC 5G-LENA (nr module) to ns-3, in the typical way (as a module in the contrib/ directory), and building and running the examples. Documentation is available from here: [https://5g-lena.cttc.es/](https://5g-lena.cttc.es/). There is an overview tutorial video available here: [https://acmse.net/2021/tutorials-offered/#tut-work03](https://acmse.net/2021/tutorials-offered/#tut-work03). That is the background information.
For more specific guidelines, please view this [Google document](https://docs.google.com/document/d/1cQLIF1cdft1yj3vyWrjrxN2xDJMx8PuWaa9NP_nKf64/edit?usp=sharing).

- Required Experience: C++ programming, understanding of 5G NR, LTE, and wireless networks
- Interests: 5G NR simulations
- Difficulty: Medium.
- Patch requirement: See the
[description](/ideas/the-ns-3-network-simulator-project/gsoc2024patchrequirement). You can also consider some of the[nr good to start issues](https://gitlab.com/cttc-lena/nr/-/issues/?label_name%5B%5D=good%20first%20issue). Or, you can start writing some APIs for the selected project proposal. Also, if you have some previous MRs to ns-3 or the nr module, you can contact us to check whether it is enough for the patch requirement.

### Linux-like CAKE queue discipline for ns-3

Mentors: [Mohit P. Tahiliani](mailto:tahiliani.nitk@gmail.com)

Common Applications Kept Enhanced (CAKE) is the most recent queue discipline added in Linux 4.19. It is a comprehensive queue management framework targeted for home Internet gateways, and integrates the following four components: bandwidth shaping, a new Active Queue Management (AQM) algorithm called COBALT (CoDel BLUE Alternate), handling Differentiated Services (DiffServ) and TCP ACK filtering. The main tasks in this project include: implementation, testing and documentation of individual components of CAKE in ns-3, followed by the integration of these components to form CAKE queue discipline in ns-3.

*Required Experience:*Familiarity with queue disciplines, TCP and C++ programming.*Bonus Experience:*Familiarity with CAKE framework in Linux 4.19*Interests:*Active Queue Management, Packet scheduling and TCP.*Difficulty:*Medium to Hard*Recommended reading:*

### Switched Ethernet

Mentors: [Tommaso Pecorella](mailto:tommaso.pecorella@unifi.it), TBD.

The current ns-3 models for wired connections are fine for simple networks, but the lack of a switched Ethernet model is a limitation in some cases.

The goal of the idea is to create, test, and document a Switched Ethernet model, able to simulate (at least) 1, 10, and 40 GbE links and model for a switch.

The model of the NetDevice and Channel shall take into account the link delays and errors, similarly to what is done by the point-to-point model. Futhermore, it should be able to set the link speed and if it is full-duplex or half-duplex. Additional support for flow control is a bonus, but not strictly required. Link speed auto-negotiation is not considered to be interesting.

The model for the switch should be modular (i.e., allowing the development of different switch types), and include auto-learning of I/O ports based on the MAC address, i.e., have a MAC/port table, and a basic store-and-forward operation. Features like advanced I/O buffer handling and ARP/NDP spoofing detection are not a priority and shall be left for future implementations.

The model should consider the future implementaion of algorithms like VLANs (IEEE 802.1Q, 802.1ad), and the Spanning Tree Protocol (IEEE 802.1D, 802.1w, and 802.1s). Their implementaion is not required, but the model design should allow their development.

*Required Experience:*Fundamentals of Ethernet sitched networking, C++ programming.*Interests:*Ethernet networks and switched data networks.*Difficulty:*Medium.*Recommended reading:*

Possible tasks to fulfill the patch requirement:

- TBD, contact the mentors if interested.
