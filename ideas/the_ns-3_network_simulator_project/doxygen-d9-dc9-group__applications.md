# Existing Applications in ns-3

**Parent:** The ns-3 Network Simulator Project — Project Ideas
**Source:** https://www.nsnam.org/doxygen/d9/dc9/group__applications.html
**Scraped:** 2026-02-22T23:28:47.555167

---

Loading...

Searching...

No Matches

Applications

This section documents the API of the ns-3 applications module.
[More...](https://www.nsnam.org#details)

Collaboration diagram for Applications:

| |
|

| |
| class |
|

This section documents the API of the ns-3 applications module.

Class [ns3::Application](https://www.nsnam.org/de/d96/classns3_1_1_application.html) can be used as a base class for [ns3](https://www.nsnam.org/d7/d2e/namespacens3.html) applications.

For a generic functional description, please refer to the ns-3 manual.

Applications are associated with individual nodes. Each node holds a list of references (smart pointers) to its applications.

Conceptually, an application has zero or more [ns3::Socket](https://www.nsnam.org/d8/db5/classns3_1_1_socket.html) objects associated with it, that are created using the [Socket](https://www.nsnam.org/d8/db5/classns3_1_1_socket.html) creation API of the Kernel capability. The [Socket](https://www.nsnam.org/d8/db5/classns3_1_1_socket.html) object API is modeled after the well-known BSD sockets interface, although it is somewhat simplified for use with [ns3](https://www.nsnam.org/d7/d2e/namespacens3.html). Further, any socket call that would normally "block" in normal sockets will return immediately in [ns3](https://www.nsnam.org/d7/d2e/namespacens3.html). A set of "upcalls" are defined that will be called when the previous blocking call would normally exit. THis is documented in more detail [Socket](https://www.nsnam.org/d8/db5/classns3_1_1_socket.html) class in [socket.h](https://www.nsnam.org/da/ddd/socket_8h.html).

The main purpose of the base class application public API is to provide a uniform way to start and stop applications.
