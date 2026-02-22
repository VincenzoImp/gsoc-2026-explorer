# Project Ideas

**Parent:** The ns-3 Network Simulator Project — Project Ideas
**Source:** https://www.nsnam.org/wiki/Project_Ideas
**Scraped:** 2026-02-22T23:28:47.553188

---

# Project Ideas

[Jump to navigation](https://www.nsnam.org#mw-head)

[Jump to search](https://www.nsnam.org#searchInput)

[Main Page](https://www.nsnam.org/wiki/Main_Page) - [Roadmap](https://www.nsnam.org/wiki/Roadmap) - [Summer Projects](https://www.nsnam.org/wiki/Summer_Projects) - [Project Ideas] - [Developer FAQ](https://www.nsnam.org/wiki/Developer_FAQ) - [Tools](https://www.nsnam.org/wiki/Tools) - [Related Projects](https://www.nsnam.org/wiki/Related_Projects)

[HOWTOs](https://www.nsnam.org/wiki/HOWTOs) - [Installation](https://www.nsnam.org/wiki/Installation) - [Troubleshooting](https://www.nsnam.org/wiki/Troubleshooting) - [User FAQ](https://www.nsnam.org/wiki/User_FAQ) - [Samples](https://www.nsnam.org/wiki/Category:Samples) - [Models](https://www.nsnam.org/wiki/Category:Models) - [Education](https://www.nsnam.org/wiki/Education) - [Contributed Code](https://www.nsnam.org/wiki/Contributed_Code) - [Papers](https://www.nsnam.org/wiki/Papers)

**Note:** If you are here looking for **Google Summer of Code project ideas**, visit [ this page](https://www.nsnam.org/wiki/Summer_Projects#Google_Summer_of_Code_2026).

One way to get involved with ns-3 is to work with a mentor on a suggested project. These are typically project suggestions that would be valued contributions but the proposer does not have enough time to do it himself or herself, but is willing to mentor someone else to do it.

Another possibility for students is to get involved in the [Google Summer of Code](http://code.google.com/soc/) program. This program is administered by Google and acceptance is competitive.

How does a mentored project work? You contact the mentor and describe your interests and availability to work on the module. You and the mentor will work out a plan to regularly review and discuss the development of your module, following the [guidelines for developing new models for ns-3](https://www.nsnam.org/docs/manual/html/new-modules.html). You will set up a public repository somewhere such as [a site listed here](http://mercurial.selenic.com/wiki/MercurialHosting) or your own mercurial server.

Not all projects are mentored, nor do they all need to be. Please suggest new project ideas on this page and whether you would mentor them.

# Introductory projects

This project category is for smaller, simpler projects for new developers to get started. If you would like to work on one of these, please coordinate with the named mentor.

## tcp-echo example and relative tutorial section

**Mentor**: [Natale](mailto:natale.patriciello@gmail.com)

References:

From the bug report: Pretty much every introduction to BSD sockets ever written uses a TCP echo client server pair to start with. It then moves to a UDP echo client server pair to illustrate datagrams.

We wrote the udp-echo.cc example when there was no TCP in the system. Now that we have some TCPs, it would be useful to make a tcp-echo.cc and associated applications. In our documentation, it would be very useful go through the same kind of tutorial as everyone else in the world, with a tcp echo walkthrough followed by a udp echo walkthrough.

The code is already there, and it is perfect to be read and to be adapted to latest ns-3 by an interested student.

## Sockets should support the setting of QoS

**Mentor**: [Tommaso Pecorella](mailto:tommaso.pecorella@unifi.it)

References:

[http://groups.google.com/group/ns-3-users/browse_thread/thread/5be010835c4b5b71](http://groups.google.com/group/ns-3-users/browse_thread/thread/5be010835c4b5b71)[https://www.nsnam.org/bugzilla/show_bug.cgi?id=1361](https://www.nsnam.org/bugzilla/show_bug.cgi?id=1361)

## Reducing header dependencies

**Mentor**: [Tom Henderson](mailto:tomh@tomh.org)

Bug [1832](https://www.nsnam.org/bugzilla/show_bug.cgi?id=1832) describes some software maintenance that could be performed on ns-3, to reduce unnecessary header dependencies. Patches are welcome for even a small part of the overall solution.

I would suggest to adapt deheader and place it in utils/deheader.py. Running utils/deheader.py should list all the unnecessary includes, and let the maintainers decide whether they want to go clean these up.

Daniel Camara performed this work already, but the work was not finished and merged. Bug 1832 has the details.

References:

## Fixing Doxygen errors and warnings

**Mentor**: [Tom Henderson](mailto:tomh@tomh.org), [Vedran Miletic](mailto:rivanvx@gmail.com), or [Peter Barnes](mailto:pdbarnes@llnl.gov)

Bug [938](https://www.nsnam.org/bugzilla/show_bug.cgi?id=938) describes an overall effort to eliminate Doxygen warnings (primarily, for missing Doxygen) from our modules. Any patches that contribute to the overall goal would be welcome. Contact one of the mentors if interested.

# Projects needing completion

Some projects were started in the past and never brought to completion.

## PyViz open issues

As of ns-3.29, PyViz has been ported to GTK+3 but several open issues remain. There are open tracker issues on each of these.

- The 'show_last_packets.py' plugin needs an update away from use of Python Kiwi library (
[https://www.nsnam.org/bugzilla/show_bug.cgi?id=2972](https://www.nsnam.org/bugzilla/show_bug.cgi?id=2972)) - Use of ipython needs to be tested (
[https://www.nsnam.org/bugzilla/show_bug.cgi?id=2971](https://www.nsnam.org/bugzilla/show_bug.cgi?id=2971)) - Flow labels for vertical flows are not rendered correctly (
[https://www.nsnam.org/bugzilla/show_bug.cgi?id=2970](https://www.nsnam.org/bugzilla/show_bug.cgi?id=2970)) - GooCanvas API inconsistency for bounds resizing (
[https://www.nsnam.org/bugzilla/show_bug.cgi?id=2969](https://www.nsnam.org/bugzilla/show_bug.cgi?id=2969))

## Wifi rate control example

ns-3 supports many different wifi rate controls, but there isn't a good example program that allows users to clearly contrast the performance of different ones. The example program 'examples/wireless/multirate.cc' does this a little bit, but it focuses on sampling the throughput.

The suggested project is to work with improving multirate.cc so that users can clearly see the difference between selecting the different rate control algorithms, perhaps by running for longer amount of time and finding a way to plot the rate chosen by the control algorithm as a function of time.

## Perfect ARP

[Bug 187](https://www.nsnam.org/bugzilla/show_bug.cgi?id=187) has a patch that needs further review, updating to ns-3-dev, and finishing off. The enhancement is described as follows:

We need an implementation of ARP which avoids the generation of ARP request/reply packets and assumes a 'perfect' ARP table is always available and up-to-date.

## IPv6 Routing

**Mentor**: [Tom Henderson](mailto:tomh@tomh.org), [Tommaso Pecorella](mailto:tommaso.pecorella@unifi.it),

There is little support for global (i.e. god) routing routing for IPv6. This was started in a 2011 ns-3 summer of code project. IPv6 can use Dynamic routing (RIPng is included in ns-3.20), but more protocols are welcome.

However, global routing is still needed. Moreover, all the ad-hoc routing protocols are currently IPv4-only.

## Refactor AODV Hello

[Bug 1188](https://www.nsnam.org/bugzilla/show_bug.cgi?id=1188) describes a problem with the current AODV implementation that Hellos are sent even without any active routes.

We would like for someone to align our implementation with the AODV RFC (or with working implementations) in this regard.

**Mentor**: [Daniel Lertpratchya](mailto:nikkipui@gmail.com)

# Mentored projects

This section lists project ideas for which there is interest by an ns-3 developer or maintainer to serve as a mentor in the development of a new feature for ns-3.

Please do not apply for mentoring help on a class project unless you have approval from the instructor to receive mentoring.

## Make NetAnim modular

**Mentor**: [Tommaso Pecorella](mailto:tommaso.pecorella@unifi.it)

Edited from the bug description ([https://www.nsnam.org/bugzilla/show_bug.cgi?id=2968](https://www.nsnam.org/bugzilla/show_bug.cgi?id=2968)):

NetAnim ns-3 interface is "hardwired" on the modules it can understand. As a result, if you try to enable only a specific module *and* NetAnim, NetAnim will build unnecessarily a lot of other stuff.

In light of modularizing ns-3, it would be helpful to have NetAnim probe for the available modules and build itself accordingly. NetAnim should be slimmed down to its bare minimum, and each module should (optionally) include its own code to support NetAnim.

Adding new types support to NetAnim could be way easier in this way, leaving the burden to write the proper code to the specific modules developers.



## Decouple traffic generation from sockets

**Mentor**: [Tom Henderson](mailto:tomh@tomh.org)

All ns-3 simulations are IP based but there is no template for how to do this for non-IP-based stacks. One issue that should be addressed in the long term is that applications that generate traffic are strongly coupled to the sockets interface. It would be nice to decouple the traffic generation aspects of these applications from the sockets-related code.

*summary*: Proposed decoupling to generalize applications*ns-developers post*:[http://mailman.isi.edu/pipermail/ns-developers/2007-July/003136.html](http://mailman.isi.edu/pipermail/ns-developers/2007-July/003136.html)*code location*:[http://code.nsnam.org/laprisee/ns-3-mp/](http://code.nsnam.org/laprisee/ns-3-mp/)*status*: Was under discussion in the summer.




## SCTP (Stream Control Transmission Protocol)

**Mentor**: [Tommaso Pecorella](mailto:tommaso.pecorella@unifi.it)

[SCTP](http://en.wikipedia.org/wiki/Stream_Control_Transmission_Protocol) is a message-based L4 protocol with features similar to both TCP and UDP. It was originally developed as a reliable protocol to transport PSTN control streams, and it's currently used to carry 3G and 4G signaling over IP networks. The use of SCTP, however, is not limited to signaling transport, as its features makes it very interesting for a lot of other applications where UDP or TCP fails.
Currently there is no SCTP implementation for ns-3. An SCTP implementation would have to comply with the IPv4 and IPv6 layers and have programming APIs toward the application layer similar to the ones defined in the available SCTP implementations for Linux.

- Required Experience: C++
- Bonus Experience: L4 protocols understanding
- Interests: L4 protocols modeling and simulation
- Difficulty: medium
- Recommended reading:

# Feature requests

The following projects have been suggested in the past. If you are working on them, please let us know on the developers or users list so that we can coordinate activities. If you want to add a project, please describe it below.

## TCP congestion window validation

Linux uses TCP congestion window validation (CWV) but ns-3 lacks this option. This draft provides details:
[https://tools.ietf.org/html/rfc7661](https://tools.ietf.org/html/rfc7661)

## Path MTU discovery

When a L4 packet is passed to the IPv4 or IPv6 stacks, the MTU (i.e., the size of the outgoing IP packets) is usually set to the local interface MTU. Or so it is the popular belief. Using the local interface MTU might lead to IP-level fragmentation, more overhead, and poor network performance.+

As a consequence, multiple techniques to discover the end-to-end MTU (called Path MTU) are available. The current PMTU discovery ns-3 capability status is listed below.

### Path MTU discovery for IPv4 stacks

**Status:** Being worked on by Vedran Miletic

There is no [path MTU discovery](http://en.wikipedia.org/wiki/Path_MTU_discovery) implemented for IPv4. This makes guessing the end-to-end MTU imperative for ns-3 simulations. We would welcome a contribution that introduced path MTU discovery to ns-3.

Vedran expressed interest in working on PMTU discovery.

### Path MTU discovery for IPv6 stacks

[path MTU discovery](http://en.wikipedia.org/wiki/Path_MTU_discovery) is implemented in ns-3's IPv6 stack.

### Packetization Layer Path MTU Discovery

[RFC 4821](http://tools.ietf.org/html/rfc4821) describes a method to detect PMTU at packetization (i.e., L4) level. This is another good candidate to be implemented.

### L4 compliance with PMTU

Even if IPv6 is able to detect PMTU, and IPv4 could be, currently there is no API to probe for a specific PMTU from L4 (e.g., UDP, TCP, etc.). Moreover, TCP is blind with respect to PMTU. I.e., its MSS (Maximum Segment Size) is fixed.

In order to reproduce real TCP performance it is of paramount importance to:

- Define an API to be used by L4 protocols, for PMTU probing.
- Update TCP to react to PMTU changes (dynamic MSS).
- Update TCP to not decrement its Congestion Window upon losses due to PMTU discovery (especially important for IPv6).

## DSR RFC compliance

**Note:** As of June 2015, Gaurangi Saxena is working on this (see: [http://mailman.isi.edu/pipermail/ns-developers/2015-June/012842.html](http://mailman.isi.edu/pipermail/ns-developers/2015-June/012842.html)).

The ns-3 DSR implementation is not following strictly the [RFC 4728](http://datatracker.ietf.org/doc/rfc4728/). The topic has been briefly discussed in [bug# 1895](https://www.nsnam.org/bugzilla/show_bug.cgi?id=1895).

It would be nice to have a switch to change from the current behaviour to the "RFC-strict" behaviour. As a byproduct, DSR could be updated to support IPv6. Although not explicitly stated by the rFC, DSR can be used for IPv6 as well.
