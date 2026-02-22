# QEMU — Project Ideas

**Source:** https://wiki.qemu.org/Google_Summer_of_Code_2026
**Scraped:** 2026-02-22T23:28:47.605772

---

# Google Summer of Code 2026

# Introduction

QEMU is participating in [Google Summer of Code 2026](https://summerofcode.withgoogle.com/). This page contains our ideas list and information for applicants and mentors. Google Summer of Code is an open source internship program offering paid remote work.

**Status: Prospective interns can research project ideas and discuss them with mentors. Applications will be open March 16-31.**

# Project Ideas

### Fast Snapshot Load

**Summary:** Instantly launch VMs from snapshots by loading RAM on demand

Extend the ["migrate_incoming" QMP command](https://gitlab.com/qemu-project/qemu/-/blob/master/migration/migration.c?ref_type=heads#L1748) to avoid loading all
RAM pages from the snapshot file before starting the VM. The ["postcopy" live migration mode](https://gitlab.com/qemu-project/qemu/-/blob/master/migration/postcopy-ram.c?ref_type=heads#L1275) does something similar by trapping accesses to pages that have not been migrated yet using the Linux
userfaultfd(2) syscall. Combine userfaultfd(2) with the ["mapped-ram" feature](https://gitlab.com/qemu-project/qemu/-/blob/master/docs/devel/migration/mapped-ram.rst), which
makes it possible to find a RAM page in the snapshot file, to do the same
thing for snapshot loading.

You will implement this feature and compare the snapshot loading time against eager loading. For more details, see [ToDo/LiveMigration#Fast_load_snapshot](https://wiki.qemu.org/ToDo/LiveMigration#Fast_load_snapshot).

**Details:**

- Difficulty: advanced
- Project size: 350 hours
- Required skills: fluent in the C programming language
- Mentors: Peter Xu <peterx@redhat.com> (peterx on #qemu IRC)

### USB Device Redirection for qemu-rdp

**Summary:** Implement MS-RDPEUSB protocol (client & server) in IronRDP with libusb backend and qemu-rdp integration.

The goal of this project is to add USB device redirection support to IronRDP, the Rust implementation of the Remote Desktop Protocol. This enables client-attached USB devices (webcams, scanners, security keys, etc.) to be transparently accessed by applications running on the remote server.

MS-RDPEUSB is a Dynamic Virtual Channel (DVC) extension that provides low-level USB packet redirection. Unlike high-level device redirection (like file system or audio), USB redirection transfers raw USB packets, allowing any USB device to work remotely without device-specific driver support on the client.

The implementation will include:

**Client-side implementation**: Capture local USB devices using libusb (via rusb crate), enumerate device descriptors, and relay USB packets to the server over the RDPEUSB virtual channel. Teach rdw-rdp to do USB redirection.

**Server-side implementation**: Receive USB packets from clients, create virtual USB device representations, and forward I/O requests. This enables IronRDP-based RDP servers to receive USB devices from connecting clients. Teach qemu-rdp to handle USB redirection with QEMU.

**Links:**

[MS-RDPEUSB Specification](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rdpeusb/a1004d0e-99e9-4968-894b-0b924ef2f125)[MS-RDPEUSB Protocol Overview](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rdpeusb/4d28161d-a4c7-4951-873a-a7d969a4cd00)[IronRDP Repository](https://github.com/Devolutions/IronRDP)[IronRDP Architecture](https://github.com/Devolutions/IronRDP/blob/master/ARCHITECTURE.md)[qemu-rdp Project](https://gitlab.com/marcandre.lureau/qemu-display)[rdw-rdp Project](https://gitlab.gnome.org/malureau/rdw)[rusb - Rust libusb bindings](https://crates.io/crates/rusb)

**Details:**

- Difficulty: advanced
- Project size: 350 hours
- Required skills: Rust
- Mentor: Marc-André Lureau <marcandre.lureau@redhat.com>

### vhost-user memory isolation

**Summary:** Add a new mode for vhost-user devices that does not expose guest RAM as shared memory.

The [vhost-user protocol](https://gitlab.com/qemu-project/qemu/-/blob/master/docs/interop/vhost-user.rst) enables VIRTIO devices to be implemented as separate processes outside of QEMU. vhost-user achieves good performance by directly accessing guest RAM through shared memory, but exposing guest RAM is not always desirable for security reasons.

You will add a memory isolation mode where QEMU intercepts I/O requests, copies data buffers between guest RAM and a vhost-user isolated memory area, and then forwards the notifications between the guest and the vhost-user device. This will be done without changes to the vhost-user protocol so that existing software remains compatible.

**Internship tasks:**

- Add a bool "memory-isolation" qdev property to QEMU's vhost-user devices.
- Modify hw/virtio/vhost-user.c to intercept and forward the vhost-user callfd and kickfd eventfds when memory isolation is enabled.
- Manage an area of memory where I/O requests will be copied.
- Integrate the existing
[Shadow Virtqueue (SVQ)](https://kvm-forum.qemu.org/2023/vDPA_sw_lm_-_KVM2023_6Ix6R5i.pdf)code into hw/virtio/vhost-user.c so that vhost-user devices see the SVQ instead of the guest's virtqueue. - Extend tests/qtest/vhost-user-test.c to run with memory-isolation=on, proving that the feature works.

**Links:**

**Details:**

- Difficulty: intermediate
- Project size: 350 hours
- Required skills: fluency in the C programming language
- Mentors: Stefan Hajnoczi <stefanha@redhat.com>, Tyler Fanelli <tfanelli@redhat.com>, Hanna Czenczek <hreitz@redhat.com>

### virtio-rtc vhost-user device

**Summary:** Implement virtio-rtc device as a vhost-user-device

The virtio-rtc device provides access to real-time clocks, such as UTC or TAI, or physical time elapsed since a given epoch. The driver can read the time using simple or more accurate methods and may optionally set an alarm.

To research this project idea, focus on the virtio-rtc device as described in
the [VIRTIO specification](https://github.com/oasis-tcs/virtio-spec/tree/virtio-1.4/device-types/rtc), as well as studying the existing [Linux virtio-rtc driver](https://lore.kernel.org/all/20250509160734.1772-1-quic_philber@quicinc.com/). Also, it may help to look at the [QEMU implementation of the rtc clock](https://gitlab.com/qemu-project/qemu/-/tree/master/hw/rtc). In parallel, an existing [vhost-user-device implementation](https://github.com/rust-vmm/vhost-device) can be used as a reference to design and write the new device.

The device will be implemented in Rust and must conform to the VIRTIO specification. The project also includes debugging interoperability issues, identifying possible mismatches between the driver and the specification, and submitting the final implementation to the vhost-device project.

High-level tasks:

- Design and implement the virtio-rtc device as a vhost-user-device in Rust. Existing vhost-user-devices may help to get inspiration. This step also requires adding the glue code in QEMU to support this device.
- Build and test the virtio-rtc driver.
- Test, debug, and submit the new device to the vhost-device project.

**Details:**

- Difficulty: intermediate
- Project size: 175 or 350 hours depending on intern
- Required skills: Rust and C
- Mentors: Matias Ezequiel Vara Larsen <mvaralar@redhat.com>, Francesco Valla <francesco@valla.it> and Stefano Garzarella <sgarzare@redhat.com>

### Support X86 Process Context Identifiers (PCID) in COCONUT-SVSM

[COCONUT-SVSM](https://github.com/coconut-svsm/svsm/) is a Secure Virtual machine Service Module that runs at a
privileged level within a Confidential Virtual Machine (CVM) to provide trusted
services, such as a virtual TPM, to the guest operating system, independent of
the host hypervisor.

The goal of the project is to enhance the COCONUT-SVSM kernel to make use of
the PCID feature on X86 (see [AMD64 APM 2 PCIDs, Section 5.5.1](https://docs.amd.com/v/u/en-US/24593_3.43)) to reduce the number of runtime [TLB misses](https://en.wikipedia.org/wiki/Translation_lookaside_buffer). The work consists of several steps:

- Implement generic CPUID feature enumeration support by building a code generator which automatically creates a Rust crate from the data provided by the
[X86-CPUID project](https://x86-cpuid.org/). Use that generated crate in COCONUT-SVSM for detecting the PCID feature and clean up all the open coded CPUID checks. - Design and implement a PCID assignment strategy for tasks and threads in the COCONUT kernel.
- Apply the PCIDs in the COCONUT page-tables and adapt the TLB flushing code to take PCIDs into account.

**Details:**

- Difficulty: Intermediate
- Project size: 350 hours
- Required skills: Rust
- Mentors: Joerg Roedel <joerg.roedel@amd.com>, Luigi Leonardi <leonardi@redhat.com>

### Observability Support for COCONUT-SVSM

**Summary:** Implement Support for COCONUT-SVSM Observability within the TEE

[COCONUT-SVSM](https://github.com/coconut-svsm/svsm/) is a Secure Virtual machine Service Module that runs at a
privileged level within a Confidential Virtual Machine (CVM) to provide trusted
services, such as a virtual TPM, to the guest operating system, independent of
the host hypervisor.

The goal of the project is to implement [basic support for observability of COCONUT-SVSM](https://coconut-svsm.github.io/svsm/developer/DEVELOPMENT-PLAN/#observability) from the guest OS. When finished the guest OS has a way to fetch runtime metrics and data from the COCONUT-SVSM running within the same TEE. Runtime data includes the log buffer, memory usage, and possible future extensions.

The project consists of several parts:

- Implement a handler for the pre-defined SVSM observability protocol within COCONUT-SVSM following the
[other protocols](https://docs.amd.com/v/u/en-US/58019)COCONUT-SVSM already implements. - Implement a Linux device driver which uses this protocol to get observability data from COCONUT-SVSM and make it accessible to Linux user-mode via a device file.
- Implement a Linux user-space utility to fetch and save the observability data using the device driver.

**Details:**

- Difficulty: Intermediate
- Project size: 350 hours
- Required skills: Rust and C
- Mentors: Stefano Garzarella <sgarzare@redhat.com>, Gerd Hoffmann <kraxel@redhat.com>, Joerg Roedel <joerg.roedel@amd.com>

### SCSI TAPE device emulation

**Summary:** Development of an emulated SCSI TAPE device

QEMU provides functionality to emulate [SCSI](https://en.wikipedia.org/wiki/SCSI) hard discs and SCSI CD-ROM drives,
but lacks an emulated [SCSI TAPE drive](https://en.wikipedia.org/wiki/Tape_drive). The goal of this project is to develop
an emulation for a SCSI TAPE drive which is backed by a file in the
host filesystem, similar to an ISO file which is used to emulate a CD-ROM drive.

This will involve writing code to emulate a SCSI TAPE drive and storing the data in a file, adding test coverage, and documenting how to use the new feature. Finally, it should be possible to backup files from the current emulated OS to tape via standard tools, e.g. tar and mt on Linux.

Starters for researching this project idea:

- Linux
[scsi_debug](https://sg.danny.cz/sg/p/sdebug.html)has tape emulation code in the Linux kernel. - Check existing
[QEMU SCSI emulation code](https://gitlab.com/qemu-project/qemu/-/blob/master/hw/scsi/scsi-bus.c?ref_type=heads#L1280)to determine what is missing for SCSI TAPE support. - Check whether tape file storage fits into
[QEMU's block layer API](https://gitlab.com/qemu-project/qemu/-/blob/master/include/block/block-io.h?ref_type=heads). - Decide how the emulated tape data should be stored on disc. Libraries exist for handling TAPE data, e.g. the
[tape library](https://simh.trailing-edge.com/docs/simh_magtape.pdf)from the[SIMH project](https://github.com/simh/simtools). - On Linux the
[mt program](https://linux.die.net/man/1/mt)allows control of magnetic tape drives and can be used to test the driver.

**Details:**

- Difficulty: Intermediate
- Project size: 350 hours
- Required skills: C (required), SCSI protocol (optional)
- Mentors: Helge Deller <deller@gmx.de>

# Application Process

## AI Policy


- Do not use AI to generate your proposal
- Exception: You may use AI to adjust grammar. This can be useful if you are not a native speaker.
- Do not use AI to generate code
- Exceptions: You can still use AI to understand the codebase, get answers to technical questions, or debug issues. Just don't generate your code using AI.

### 1. Discuss the project idea with the mentor(s)

Read the project ideas list and choose one you are interested in. Read the links in the project idea description and start thinking about how you would approach this. Ask yourself:

- Do I have the necessary technical skills to complete this project?
- Will I be able to work independently without the physical presence of my mentor?

If you answer no to these questions, choose another project idea and/or organization that fits your skills.

Once you have identified a suitable project idea, email the mentor(s) your questions about the idea and explain your understanding of the project idea to them to verify that you are on the right track.

### 2. Submit your proposal

Upload your proposal PDF file to the [Google Summer of Code website](https://summerofcode.withgoogle.com/) and notify your mentor(s) so they can give you feedback.

You can make changes and upload the PDF again until the application deadline. Your proposal must include the following:

- Project idea (title)
- Your name and email address
- Outline of your solution
- Do some background research by looking at source code, browsing relevant specifications, etc in order to decide how to tackle the project. Discuss any questions with your mentor. This section will explain how your solution will work.

- Project schedule
- Create a week-by-week schedule of the coding period. Breaking down the project into tasks and estimate how many weeks they will take. The schedule can be adjusted during the summer so don't worry about getting everything right ahead of time.

- Relevant experience (programming language knowledge, hobby projects, etc)
- Are you available to work with no other commitments (jobs, university, vacation, etc) for the duration of your project? If not, please give details about the working hours and dates.

### 3. Contribution task

Once you have submitted your proposal PDF, your mentor might ask you to complete a contribution task. The task will be a real bug or small feature that should not take more than 1 or 2 days to complete. This will allow you to demonstrate your skills in a realistic setting.

## Key Dates

From the [timeline](https://developers.google.com/open-source/gsoc/timeline):

- February 19 18:00 UTC - Organizations and project ideas announced
- March 16-31 18:00 UTC - Application period
- April 15 - Contribution task deadline
- April 30 18:00 UTC - Accepted applicants announced
- May 25 - August 24 - Standard coding period (an extended timeline is possible depending on your project)

# Find Us

- IRC (GSoC specific):
[#qemu-gsoc on irc.oftc.net](https://webchat.oftc.net/?channels=qemu-gsoc)

- IRC (development):
- QEMU:
[#qemu on irc.oftc.net](https://webchat.oftc.net/?channels=qemu) - KVM: #kvm on chat.freenode.net

- QEMU:

- Mailing lists:
- QEMU:
[qemu-devel](http://lists.nongnu.org/mailman/listinfo/qemu-devel) - KVM:
[linux-kvm](http://www.linux-kvm.org/page/Lists,_IRC)

- QEMU:

For general questions about QEMU in GSoC, please contact the following people:

[Stefan Hajnoczi](https://wiki.qemu.org/User:Stefanha)<stefanha@gmail.com> (stefanha on IRC)

# How to get familiar with our software

See what people are developing and talking about on the mailing lists:

Grab the source code or browse it:

Build QEMU and run it: [QEMU on Linux Hosts](http://wiki.qemu-project.org/Hosts/Linux)

# Links

# How to add a project idea

Mentors may add a project idea by following these steps:

- Create a new wiki page under "Internships/ProjectIdeas/YourIdea" based on the
[#Project idea template](https://wiki.qemu.org#Project_idea_template). - Link to your new wiki page using the following syntax: {{:Internships/ProjectIdeas/YourIdea}}

## Project idea template

=== TITLE === '''Summary:''' One sentence describing the project Detailed description of the project (5 sentences). Expected outcomes. '''Details:''' * Difficulty: beginner, intermediate, or advanced * Project size: 90 hours, 175 hours, or 350 hours * Required skills: C/Rust/Python * Mentors: Email address and IRC nick
