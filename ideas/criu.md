# CRIU — Project Ideas

**Source:** https://criu.org/Google_Summer_of_Code_Ideas
**Scraped:** 2026-03-10T16:58:40.253561

---

# Google Summer of Code Ideas

[Jump to navigation](https://criu.org#mw-head)

[Jump to search](https://criu.org#searchInput)

Google Summer of Code (GSoC) is a global program that offers post-secondary students an opportunity to be paid for contributing to an open source project over a three month period.

This page contains project ideas for upcoming Google Summer of Code.

## Contact[[edit](https://criu.org/index.php?title=Google_Summer_of_Code_Ideas&action=edit§ion=1)]

First, make sure to go through the [GSoC Students Recommendations](/ideas/criu/gsoc_students_recommendations). Once you build CRIU locally and C/R a simple process successfully, please contact the respective mentor for the idea you are interested in. For general questions feel free to send an email to the [mailing list](mailto:criu@lists.linux.dev) or write in [gitter](https://gitter.im/save-restore/criu).

## Project ideas[[edit](https://criu.org/index.php?title=Google_Summer_of_Code_Ideas&action=edit§ion=2)]

### Kubernetes Operator for Automated Checkpointing[[edit](https://criu.org/index.php?title=Google_Summer_of_Code_Ideas&action=edit§ion=3)]

**Summary:** Extend the Checkpoint/Restore Operator with support for automated policy-based checkpointing.

The [Checkpoint/Restore Operator](https://github.com/checkpoint-restore/checkpoint-restore-operator) for Kubernetes currently supports only policies and parameters that limit the number of checkpoints. This project aims to extend the current support with automated policy-based checkpointing, allowing users to define triggers for checkpoint creation, such as time-based schedules, resource thresholds (CPU, memory, I/O usage), Kubernetes events (node drain, pod eviction, preemption), and application-level signals or annotations.

**Links:**

[https://github.com/checkpoint-restore/checkpoint-restore-operator](https://github.com/checkpoint-restore/checkpoint-restore-operator)[https://kubernetes.io/docs/reference/node/kubelet-checkpoint-api](https://kubernetes.io/docs/reference/node/kubelet-checkpoint-api)

**Details:**

- Skill level: intermediate
- Language: Go
- Expected size: 350 hours
- Mentors: Viktória Spišaková <spisakova@ics.muni.cz>, Radostin Stoyanov <rstoyanov@fedoraproject.org>, Adrian Reber <areber@redhat.com>

### Forensic Checkpointing Framework for Kubernetes[[edit](https://criu.org/index.php?title=Google_Summer_of_Code_Ideas&action=edit§ion=4)]

Kubernetes provides a highly dynamic and ephemeral environment where workloads can start and disappear very quickly and are continuously being rescheduled across different nodes in the cluster. One of the key challenges with forensic investigations in Kubernetes is capturing and preserving the evidence during security incidents. This project aims to address this problem by developing a framework for efficiently capturing and preserving the state of all running applications in a container at a specific point in time, along with the associated container configurations and metadata. These artifacts would allow investigators to accurately reconstruct the events, create a timeline, and analyze security incidents without impacting the running cluster. This is an important step towards enabling forensic readiness for Kubernetes, where cluster administrators proactively ensure the environments are prepared to collect and preserve evidence before a security incident occurs.

**Links:**

[https://github.com/checkpoint-restore/checkpointctl](https://github.com/checkpoint-restore/checkpointctl)[Investigating Security Incidents with Forensic Snapshots in Kubernetes](https://fosdem.org/2026/events/attachments/F9RANH-forensic-snapshots-in-kubernetes/slides/267371/fosdem_2_4dh73ni.pdf)[Cloud Native Security Whitepaper](https://www.cncf.io/reports/cloud-native-security-whitepaper/)[Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)

**Details:**

- Skill level: intermediate
- Language: Go
- Expected size: 350 hours
- Mentors: Lorena Goldoni <lory.goldoni@gmail.com>, Radostin Stoyanov <rstoyanov@fedoraproject.org>, Adrian Reber <areber@redhat.com>

### Enabling Checkpoint/Restore of Rootless Containers[[edit](https://criu.org/index.php?title=Google_Summer_of_Code_Ideas&action=edit§ion=5)]

[Rootless containers](https://rootlesscontaine.rs/) are containers that can be created, run, and managed by unprivileged users. Container engines such as Podman natively support running containers in a rootless mode to improve security and usability. While checkpoint/restore functionality is already available for rootful containers and unprivileged checkpointing is possible with the `CAP_CHECKPOINT_RESTORE`

capability, container engines do not yet support native checkpointing of containers running in rootless mode. This project aims to explore and address the remaining challenges required to enable unprivileged checkpoint/restore for rootless containers.

**Links:**

[https://github.com/checkpoint-restore/criu/pull/1930](https://github.com/checkpoint-restore/criu/pull/1930)[https://github.com/torvalds/linux/commit/124ea650d3072b005457faed69909221c2905a1f](https://github.com/torvalds/linux/commit/124ea650d3072b005457faed69909221c2905a1f)[https://src.fedoraproject.org/rpms/criu/pull-request/10#request_diff](https://src.fedoraproject.org/rpms/criu/pull-request/10#request_diff)

**Details:**

- Skill level: intermediate
- Language: C, Go
- Expected size: 350 hours
- Mentors: Radostin Stoyanov <rstoyanov@fedoraproject.org>, Adrian Reber <areber@redhat.com>

### Checkpointing of POSIX message queues[[edit](https://criu.org/index.php?title=Google_Summer_of_Code_Ideas&action=edit§ion=6)]

**Summary:** Add support for checkpoint/restore of POSIX message queues

POSIX message queues are a widely used inter-process communication mechanism. Message queues are implemented as files on a virtual filesystem (mqueue), where a file descriptor (message queue descriptor) is used to perform operations such as sending or receiving messages. To support checkpoint/restore of POSIX message queues, we need a kernel interface (similar to [MSG_PEEK](https://github.com/checkpoint-restore/criu/commit/8ce9e947051e43430eb2ff06b96dddeba467b4fd)) that would enable the retrieval of messages from a queue without removing them. This project aims to implement such an interface that allows retrieving all messages and their priorities from a POSIX message queue.

**Links:**

[https://github.com/checkpoint-restore/criu/issues/2285](https://github.com/checkpoint-restore/criu/issues/2285)[https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/ipc/mqueue.c](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/ipc/mqueue.c)[https://www.man7.org/tlpi/download/TLPI-52-POSIX_Message_Queues.pdf](https://www.man7.org/tlpi/download/TLPI-52-POSIX_Message_Queues.pdf)

**Details:**

- Skill level: intermediate
- Language: C
- Expected size: 350 hours
- Mentors: Radostin Stoyanov <rstoyanov@fedoraproject.org>, Pavel Tikhomirov <ptikhomirov@virtuozzo.com>
- Suggested by: Pavel Tikhomirov <ptikhomirov@virtuozzo.com>

### Add support for SCM_CREDENTIALS / SCM_PIDFD and friends[[edit](https://criu.org/index.php?title=Google_Summer_of_Code_Ideas&action=edit§ion=7)]

**Summary:** Support for SCM_CREDENTIALS / SCM_PIDFD

SCM_CREDENTIALS and SCM_PIDFD are types of SCM (Socket-level Control Messages). They play a crucial role in systemd and many other user space applications. This project is about adding support for these SCMs to be properly saved and restored back with CRIU. There is an existing code in OpenVZ CRIU fork, see [1] and [2]. Goal would be first of all to properly port this code, cover with extensive tests and ensure that SCM_PIDFD / SO_PEERPIDFD are handled correctly. Also we expect to cover things like SO_PASSRIGHTS and SO_PASSPIDFD.

There is some extra source of complexity here pidfds can be "stale" (see PIDFD_STALE in Linux kernel) and we need to ensure that we properly cover those cases.

**Links:**

- [1] openvz-criu
[https://bitbucket.org/openvz/criu.ovz/history-node/918653a0a343194385592d7b50b5bd7a8fbe1cc1/criu/sk-unix.c?at=hci-dev](https://bitbucket.org/openvz/criu.ovz/history-node/918653a0a343194385592d7b50b5bd7a8fbe1cc1/criu/sk-unix.c?at=hci-dev) - [2] openvz-criu
[https://bitbucket.org/openvz/criu.ovz/history-node/918653a0a343194385592d7b50b5bd7a8fbe1cc1/criu/sk-queue.c?at=hci-dev](https://bitbucket.org/openvz/criu.ovz/history-node/918653a0a343194385592d7b50b5bd7a8fbe1cc1/criu/sk-queue.c?at=hci-dev) - [3] Linux kernel
[https://github.com/torvalds/linux/commit/5e2ff6704a275be009be8979af17c52361b79b89](https://github.com/torvalds/linux/commit/5e2ff6704a275be009be8979af17c52361b79b89) - [4] Linux kernel
[https://github.com/torvalds/linux/commit/c679d17d3f2d895b34e660673141ad250889831f](https://github.com/torvalds/linux/commit/c679d17d3f2d895b34e660673141ad250889831f)

**Details:**

- Skill level: intermediate / advanced
- Language: C
- Expected size: 350 hours
- Suggested by: Alexander Mikhalitsyn <alexander@mihalicyn.com>
- Mentors: Andrei Vagin <avagin@gmail.com>, Alexander Mikhalitsyn <alexander@mihalicyn.com>

### Integrate with Live Update Orchestrator (LUO)[[edit](https://criu.org/index.php?title=Google_Summer_of_Code_Ideas&action=edit§ion=8)]

**Summary:** Integrate with Live Update Orchestrator (LUO)

Live Update Orchestrator (LUO) is a framework for Linux kernel live updates (via kexec). Idea behind it is to provide kernel and user space API to save specific system resources across kexec reboot.

This research project explores how CRIU can be integrated with LUO. For example, if a user is running memcached on a node, the current approach would require a full CRIU dump, then saving the entire process memory to disk, then followed by restoring it after the kernel live update.

Instead, CRIU could be extended to leverage the LUO API. When instructed, it could preserve selected memory regions directly across the kexec reboot, avoiding a full disk dump and significantly accelerating the restore process after the kernel update.

**Links:**

- [1] LUO kernel documentation
[https://docs.kernel.org/core-api/liveupdate.html](https://docs.kernel.org/core-api/liveupdate.html) - [2] LUO memfd doc
[https://docs.kernel.org/mm/memfd_preservation.html](https://docs.kernel.org/mm/memfd_preservation.html)

**Details:**

- Skill level: intermediate / advanced
- Language: C
- Expected size: 350 hours
- Suggested by: Andrei Vagin <avagin@gmail.com>
- Mentors: Andrei Vagin <avagin@gmail.com>, Alexander Mikhalitsyn <alexander@mihalicyn.com>

### Optimize COW memory dumping[[edit](https://criu.org/index.php?title=Google_Summer_of_Code_Ideas&action=edit§ion=9)]

**Summary:** Optimize COW memory dumping

The Linux kernel memory management subsystem is highly optimized not only for performance, but also to minimize unnecessary memory consumption. A key example of this is how the kernel handles private VMAs when user space invokes the fork() system call.

Rather than duplicating the entire VMA tree along with all memory contents, the kernel creates optimized copies of inherited VMAs using the Copy-on-Write (COW) mechanism. When a process writes to a page within a COW-ed VMA, a write page fault occurs, and the kernel creates a private copy of that page before applying the modification. However, if the page is only read, no copying is performed.

This approach significantly improves fork() performance and can dramatically reduce memory usage in many workloads.

In CRIU, when dumping VMAs and their associated memory pages, this COW optimization is not currently taken into account during the dump phase. As a result, for COW-backed VMAs, CRIU may generate multiple copies of identical memory pages in the dump image.

During restore, however, CRIU explicitly handles this situation (see [1] and [2]) and attempts to reconstruct COW relationships inside the kernel. This step is critical: without it, a checkpoint/restore (C/R) cycle could lead to a substantial increase in memory consumption for the same process tree. For example, a workload that originally consumed 500 MiB could expand to 800 MiB after restore, which is clearly unacceptable.

This project aims to improve the dumping algorithm so that it avoids producing multiple unnecessary copies of identical pages belonging to COW-ed VMAs.

The project requires some understanding of Linux memory management internals and CRIU’s architecture. We strongly encourage GSoC contributors to study references [1] and [2] and experiment with the relevant code paths before applying. We are happy to answer questions and provide guidance along the way.

**Links:**

- [1] preparing COW VMAs
[https://github.com/checkpoint-restore/criu/blob/c180188db036f8ea4c08bfee28cbcdbdd52cdfc3/criu/mem.c#L878](https://github.com/checkpoint-restore/criu/blob/c180188db036f8ea4c08bfee28cbcdbdd52cdfc3/criu/mem.c#L878) - [2] private vma content restore cow case
[https://github.com/checkpoint-restore/criu/blob/c180188db036f8ea4c08bfee28cbcdbdd52cdfc3/criu/mem.c#L1219](https://github.com/checkpoint-restore/criu/blob/c180188db036f8ea4c08bfee28cbcdbdd52cdfc3/criu/mem.c#L1219)

**Details:**

- Skill level: intermediate / advanced
- Language: C
- Expected size: 350 hours
- Suggested by: Andrei Vagin <avagin@gmail.com>
- Mentors: Andrei Vagin <avagin@gmail.com>, Alexander Mikhalitsyn <alexander@mihalicyn.com>

## Suspended project ideas[[edit](https://criu.org/index.php?title=Google_Summer_of_Code_Ideas&action=edit§ion=10)]

Listed here are tasks that seem suitable for GSoC, but currently do not have anybody to mentor it.

### Optimize logging engine[[edit](https://criu.org/index.php?title=Google_Summer_of_Code_Ideas&action=edit§ion=11)]

**Summary:** CRIU puts a lots of logs when doing its job. Logging is done with simple fprintf function. They are typically useless, but *if* some operation fails -- the logs are the only way to find what was the reason for failure.

At the same time the printf family of functions is known to take some time to work -- they need to scan the format string for %-s and then convert the arguments into strings. If comparing criu dump with and without logs the time difference is notable (15%-20%), so speeding the logs up will help improve criu performance.

One of the solutions to the problem might be binary logging. The problem with binary logs is the amount of efforts to convert existing logs to binary form. Preferably, the switch to binary logging either keeps existing log() calls intact, either has some automatics to convert them.

The option to keep log() calls intact might be in pre-compilation pass of the sources. In this pass each `log(fmt, ...)`

call gets translated into a call to a binary log function that saves `fmt`

identifier copies all the args *as is* into the log file. The binary log decode utility, required in this case, should then find the fmt string by its ID in the log file and print the resulting message.

**Links:**

**Details:**

- Skill level: intermediate
- Language: C, though decoder/preprocessor can be in any language
- Expected size: 350 hours
- Suggested by: Andrei Vagin
- Mentors: Alexander Mikhalitsyn <alexander@mihalicyn.com>

### IOUring support[[edit](https://criu.org/index.php?title=Google_Summer_of_Code_Ideas&action=edit§ion=12)]

The io_uring Asynchronous I/O (AIO) framework is a new Linux I/O interface, first introduced in upstream Linux kernel version 5.1 (March 2019). It provides a low-latency and feature-rich interface for applications that require AIO functionality.

**Links:**

[https://blogs.oracle.com/linux/an-introduction-to-the-io_uring-asynchronous-io-framework](https://blogs.oracle.com/linux/an-introduction-to-the-io_uring-asynchronous-io-framework)[https://github.com/axboe/liburing](https://github.com/axboe/liburing)

**Details:**

- Skill level: expert (+linux kernel)
- Expected size: 350 hours

### Add support for SPFS[[edit](https://criu.org/index.php?title=Google_Summer_of_Code_Ideas&action=edit§ion=13)]

**Summary:** The SPFS is a special filesystem that allows checkpoint and restore of such things as NFS and FUSE

NFS support is already implemented in Virtuozzo CRIU, but it's very beneficial to port it to mainline CRIU. The importaint part of it is the need to implement the integration of Stub-Proxy File System (SPFS) with LXC/yet_another_containers_environment.

**Links**

[https://github.com/checkpoint-restore/criu/issues/60](https://github.com/checkpoint-restore/criu/issues/60)[https://github.com/checkpoint-restore/criu/issues/53](https://github.com/checkpoint-restore/criu/issues/53)[https://github.com/skinsbursky/spfs](https://github.com/skinsbursky/spfs)[https://patchwork.criu.org/series/137/](https://patchwork.criu.org/series/137/)

**Details:**

- Skill level: expert
- Language: C
- Mentor: Alexander Mikhalitsyn <alexander@mihalicyn.com>
- Suggested by: Alexander Mikhalitsyn <alexander@mihalicyn.com>



### Anonymise image files[[edit](https://criu.org/index.php?title=Google_Summer_of_Code_Ideas&action=edit§ion=14)]

**Summary:** Teach [CRIT](/ideas/criu/crit) to remove sensitive information from images

When reporting a BUG it may be not acceptable for the reporter to send us raw images, as they may contain sensitive data. Need to teach CRIT to "anonymise" images for publication.

List of data to shred:

- Memory contents. For the sake of investigation, all the memory contents can be just removed. Only the sizes of pages*.img files are enough.
- Paths to files. Here we should keep the paths relations to each other. The simplest way seem to be replacing file names with "random" (or sequential) strings, BUT (!) keeping an eye on making this mapping be 1:1. Note, that file paths may also sit in sk-unix.img.
- Registers.
- Process names. (But relations should be kept).
- Contents of streams, i.e. pipe/fifo data, sk-queue, tcp-stream, tty data.
- Ghost files.
- Tarballs with tmpfs-s.
- IP addresses in sk-inet-s, ip tool dumps and net*.img.

**Links:**

[Anonymize image files](/ideas/criu/anonymize_image_files)[https://github.com/checkpoint-restore/criu/issues/360](https://github.com/checkpoint-restore/criu/issues/360)[CRIT](/ideas/criu/crit),[Images](/ideas/criu/images)- External links to mailing lists or web sites

**Details:**

- Skill level: beginner
- Language: Python

### Add support for checkpoint/restore of CORK-ed UDP socket[[edit](https://criu.org/index.php?title=Google_Summer_of_Code_Ideas&action=edit§ion=15)]

**Summary:** Support C/R of corked UDP socket

There's UDP_CORK option for sockets. As man page says:

If this option is enabled, then all data output on this socket is accumulated into a single datagram that is transmitted when the option is disabled. This option should not be used in code intended to be portable.

Currently criu refuses to dump this case, so it's effectively a bug. Supporting
this will need extending the kernel API to allow criu read back the write queue
of the socket (see [how it's done](/ideas/criu/tcp_connection) for TCP sockets, for example). Then
the queue is written into the image and is restored into the socket (with the CORK
bit set too).

**Notes:**

We already had a couple (3) of tries for this problem:

- UDP_REPAIR approach didn't succeed:
[https://lore.kernel.org/netdev/721a2e32-c930-ad6b-5055-631b502ed11b@gmail.com/](https://lore.kernel.org/netdev/721a2e32-c930-ad6b-5055-631b502ed11b@gmail.com/),[https://lore.kernel.org/netdev/?q=udp_repair](https://lore.kernel.org/netdev/?q=udp_repair) - eBPF (CRIB) approach, socket queue iterator was not merged:
[https://lore.kernel.org/netdev/AM6PR03MB5848EDA002E3D7EACA7C6BDA99A52@AM6PR03MB5848.eurprd03.prod.outlook.com/](https://lore.kernel.org/netdev/AM6PR03MB5848EDA002E3D7EACA7C6BDA99A52@AM6PR03MB5848.eurprd03.prod.outlook.com/), and we have general objections to CRIB approach[https://lore.kernel.org/bpf/CAHk-=wjLWFa3i6+Tab67gnNumTYipj_HuheXr2RCq4zn0tCTzA@mail.gmail.com/](https://lore.kernel.org/bpf/CAHk-=wjLWFa3i6+Tab67gnNumTYipj_HuheXr2RCq4zn0tCTzA@mail.gmail.com/)

We still have one idea we didn't try, as UDP allows packets to be lost on the way on restore we can somehow mark the socket to drop all data before UNCORK. This way we don't really need to restore contents of UDP CORK-ed sockets send queue.

**Links:**

[https://github.com/checkpoint-restore/criu/issues/409](https://github.com/checkpoint-restore/criu/issues/409)[https://github.com/criupatchwork/criu/commit/a532312](https://github.com/criupatchwork/criu/commit/a532312)[Sockets](/ideas/criu/sockets),[TCP connection](/ideas/criu/tcp_connection)- [
[UDP cork explained](https://groups.google.com/forum/#!topic/comp.os.linux.networking/Uz8PYiTCZSg)]

**Details:**

- Skill level: intermediate (+linux kernel)
- Language: C
- Expected size: 350 hours
- Mentors: Alexander Mikhalitsyn <alexander@mihalicyn.com>, Pavel Tikhomirov <ptikhomirov@virtuozzo.com>, Andrei Vagin <avagin@gmail.com>
