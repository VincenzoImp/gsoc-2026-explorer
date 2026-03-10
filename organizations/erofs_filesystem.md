# EROFS filesystem

> Modern image-based kernel filesystem for everyone

**Technologies:** c, android, linux kernel, Containerd, gVisor
**Topics:** operating system, containers, android, filesystems, agent sandbox
**Website:** https://erofs.docs.kernel.org
**Ideas:** https://erofs.docs.kernel.org/en/latest/roadmap.html
**GSoC Page:** https://summerofcode.withgoogle.com/programs/2026/organizations/erofs-filesystem

## Description

EROFS is a modern, high-performance block-based immutable Linux filesystem with highly-optimized on-disk format and runtime implementation. Since it's landed upstream, it has been widely deployed to billions of devices, and addresses various target scenarios. Nowadays, almost all Linux mainstream distributions support EROFS.

EROFS has become an Android recommended filesystem (https://source.android.com/docs/core/architecture/kernel/erofs) for Android system partitions and has already been adopted by the majority of Android vendors. It has also become popular in the Linux container world. For example, Composefs (https://github.com/containers/composefs) uses the EROFS format for its metadata tree. Containerd 2.1+ also officially includes a built-in EROFS support to boost container launch performance. gVisor now supports EROFS as well.

