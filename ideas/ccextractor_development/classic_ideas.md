# Classic Projects page

**Parent:** CCExtractor Development — Project Ideas
**Source:** https://ccextractor.org/docs/classic_ideas/
**Scraped:** 2026-02-22T23:28:47.611977

---

Google Summer of Code (GSoC) 2026 ideas page - classics

This page contains ideas that we find interesting, and we would love to do but maybe there are too niche or complicated and no one ever picks them up :-)

Thanks for visiting this page!
These projects have the same importance as those in the main page. We just moved them to their own page to help keep things tidy.

DTMB is the standard for Chinese TV, also implemented by countries such as Cuba. What kind of student is ideal for this task? One with lots of analytic skills and patience. If you are one of those, don't disregard this task just because you don't speak (or maybe, even care) about Chinese. The experience on dealing with this will be extremely valuable in the future.We will use part of the organization funds to buy standard documents you might need, a capture device, and in general, anything required to make your life easier.

Captions are used by people all over the world on a regular basis. Most of us are familiar with regular horizontal captions at the bottom of the screen, but did you know that in Japan a common position for captions is vertically on the right or left side of the screen? Come learn more about what Japanese audiences need out of captions as well as how captioning standard likes IMSC and WebVTT support these features.

Japanese (or be good with foreign languages), Rust

Come up with a system that tunes the linux kernel to maximize network throughput for a number of workloads, such as web server or BitTorrent. We will provide access to a server with a huge pipe (10 Gbit/s, SSD, lots of cores) and your task is to build a tool that maximizes the throughput (and prove it!)

BitTorrent protocol is not secure. Its encryption mechanism is outdated and weak. Even for obfuscation, it is ineffective. Nowadays, even an entry-level gateway has the capability to detect and block BitTorrent traffic at little to no risk. The BitTorrent community would benefit from a new standard encryption mechanism that allows strong encryption, forward secrecy and resistance to censorship.

BitTorrent is of course the world's most used peer to peer protocol. It's great, but it was designed before the cloud was ubiquitous and it doesn't make use of the places where you have the most storage or the most bandwidth. Can we design something for the next decade?

Depends

Peer-to-peer, cloud

Unknown

175 hours

rTorrent

We use jesec/rtorrent. It provides a more modern base with Bazel/CMake and C++ 17 (instead of autotools and C++ 0x). Plus, your works are guaranteed to be incorporated if they match expectations.

Note - we want to have a unified rtorrent that gets the best from jesec's and novik's work. See the first project in this section.

Each of the two most important rTorrent frontends have their own backend version. We need to create a version that works with both ruTorrent and Flood.

rTorrent currently uses an antique XMLRPC interface, which is limited in capability, not scalable, hard to use, insecure and low-performance. Community needs a modern RPC interface with full bidirectional, stream processing, incremental data loading and high concurrency capabilities, which allows real-time events for RPC users, reduced serialization/transfer overheads, potentially better security (with authentication and/or TLS), etc.

C++

RPC, Event Loop

Medium/Hard

350 hours

asynchronous name resolution

UDP tracker name resolution is not asynchronous at the moment, which causes blocking in the main thread and can block (timeout) other ongoing/incoming connections/transfers. c-ares or libwebsockets implementation is preferred, as c-ares is already used by curl, which rTorrent depends on, while libwebsockets may be used by a future WebSockets RPC interface.

C, C++

Threading, Event Loop

Medium

350 hours

improve scalability

rTorrent has a well-defined threading behaviour, which makes it stable and light on resources. There are 3 permanent threads only: main, disk and scgi. However, in the age of Gigabit/10G connections, 3 threads are often not sufficient. Implement a new threading model with better scalability.

C++

Threading

Hard

350 hours

scheduling/queuing

In some cases, users might want to download a series of torrents one-by-one without having to manually start the next when the previous is completed. Implement a scheduler along with a queue to allow users to limit the number of maximum simultaneous downloads. Enqueue if the user adds a download or decrease the limit. Dequeue when a download is completed or the user increases the limit. Keep the queue state across reboots.
