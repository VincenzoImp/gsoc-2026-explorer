# GSoC 2017 log

**Parent:** Haiku — Project Ideas
**Source:** https://www.haiku-os.org/blog/hyche
**Scraped:** 2026-02-22T23:28:47.590375

---

#### Blog-O-Sphere

[Haiku Activity & Contract Report, January 2026](https://www.haiku-os.org/blog/waddlesplash/2026-02-12-haiku_activity_contract_report_january_2026/)[The Gerrit code review iceberg, episode 5](https://www.haiku-os.org/blog/pulkomandy/2026-02-03-the_gerrit_pending_review_iceberg_5/)[Haiku Activity & Contract Report, December 2025](https://www.haiku-os.org/blog/waddlesplash/2026-01-12-haiku_activity_contract_report_december_2025/)[The Gerrit code review iceberg, episode 4](https://www.haiku-os.org/blog/pulkomandy/2025-12-31-the_gerrit_pending_review_iceberg_4/)[The Gerrit code review iceberg, episode 3](https://www.haiku-os.org/blog/pulkomandy/2025-12-19-the_gerrit_pending_review_iceberg_3/)[Haiku Activity & Contract Report, November 2025 (ft. Go)](https://www.haiku-os.org/blog/waddlesplash/2025-12-12-haiku_activity_contract_report_november_2025/)[The Gerrit code review iceberg, episode 2](https://www.haiku-os.org/blog/pulkomandy/2025-12-05-the_gerrit_pending_review_iceberg_2/)[The Gerrit code review iceberg](https://www.haiku-os.org/blog/pulkomandy/2025-11-24-the_gerrit_pending_review_iceberg/)[Haiku Activity & Contract Report, October 2025](https://www.haiku-os.org/blog/waddlesplash/2025-11-11-haiku_activity_contract_report_october_2025/)[Haiku Activity & Contract Report, September 2025](https://www.haiku-os.org/blog/waddlesplash/2025-10-13-haiku_activity_contract_report_september_2025/)

[[GSoC 2017 - BTRFS write supports] Third coding period - Final recap](https://www.haiku-os.org/blog/hyche/2017-08-25_gsoc_2017_-_btrfs_write_supports_third_coding_period_-_final_recap/)

## Hello everyone,

Google Summer of Code 2017 is coming to the end. This is my final report which covers third coding sprint, also read my introduction blog[1] for a brief of my project.

Creating and removing directories are now working. Basically, creating directories involve in inserting new inode (metadata of file) and making links between file name and inode. Because directories don’t hold any data so there isn’t any links between inode and file data, creating new files need to handle it.

[[GSoC 2017 - BTRFS write support] Week #9 #10 #11 (Second coding period)](https://www.haiku-os.org/blog/hyche/2017-08-04_gsoc_2017_-_btrfs_write_supports_week_9_10_11_second_coding_period/)

### Hi there!

It has been 4 weeks since my last blog post. This blog post recaps what I have done in the second coding period and what I am doing and will do in the following weeks. Link to my previous blog post[1].

In the previous weeks I have been doing the implmentation for extent allocator and journal. About the extent allocator, the allocating strategy for now is “first fit” which means it allocates a first extent that after the address and has size that equal or larger the size we need. The allocator also handle extents that not present in the current tree because of the Copy-On-Write mechanism, so that the new allocated extent will not delete the old extent. The allocator can now allocate and deallocate extent, but it still need more testing though, it is hard to tell that it works well if is not actually in used (for examples making directories, writing files, etc).

[[GSoC 2017 - BTRFS Write Supports] Week #6 #7 #8](https://www.haiku-os.org/blog/hyche/2017-07-07_gsoc_2017_-_btrfs_write_supports_week_6_7_8/)

### Hello again,

Sorry for late report, things are not going as I planned. In order to implement tree manipulation or copy-on-write function, I must first have a blocks/extents allocator that works well. Also, those things need to handle transactions as well.

In the previous weeks, I did some “edgy” works that are supported functions, add some on-disks structures, modify some parts of the source code, etc. Currently, I am implementing the extent allocator, it can now dump all the free extents and used extents for all roots, included backup roots. The goal is allocating continuous extents and preventing external fragmentation, but I’m stuck at it. My initial idea is using AVLTree that is existed in Haiku for tracking extents, and from that I can find a next necessary extent for allocating, but I’m not sure it is the right way. You can read all the works in my commit history[1].

[[GSoC 2017 - BTRFS Write Supports] Week #4 #5](https://www.haiku-os.org/blog/hyche/2017-06-14_gsoc_2017_-_btrfs_write_supports_week_4_5/)

### Hello everyone,

I spent last 2 weeks mainly for researching and forming an complete idea so that something will not be changed much in the future and some coding. These things are what I did in the previous 2 weeks:

I implemented a “cat” command in **btrfs_shell** for testing, since current **fs_shell** misses read file content command.

Refixed ticket #127883. This is the ticket I fixed as a proof to attend GSoC for Haiku, but it is hardcoded. I simply changed the block size to node size (the old block size is sector size), so that block_cache can cache the whole node instead of caching multiple blocks with old block size, and reverted back the old code. I misunderstood in the past that block is sector but that is not always (at least in BtrFS case). In BtrFS, metadata is in tree block (node) and file data is in extent (a continous run of sectors), so with block_cache API I can easily manipulate tree node and with file_cache API for read/write files. I had a hard time to figure out how to write with cache, but after reading BFS and block_cache codebase, it can be done easily with **memcpy** for copying data to cache and **block_cache_sync** for flushing to disk.

[[GSoC 2017 - BTRFS Write Supports] Week #3](https://www.haiku-os.org/blog/hyche/2017-05-28_gsoc_2017_-_btrfs_write_supports_week_3/)

Hi everyone,

It's me again, this is my third report of my project about what I have done in this week. There is no coding, just reading and reading a lot. Now, I am confident to say that I can fully understand all the things in Btrfs codebase. I lurked a little around Linux's source and mailing list for Btrfs, but it didn't help much since the source is large, complicated and I don't know where to start to read, so I decide to implement Btrfs in my own way and back to read if encounter problems. I have tried to produce some bugs by making many directories and files with different size, and then see that can Haiku's Btrfs handle (cd and ls) it, lucky that it worked well otherwise I had works to do.

[[GSoC 2017 - BTRFS Write Supports] Week #2](https://www.haiku-os.org/blog/hyche/2017-05-19_gsoc_2017_-_btrfs_write_supports_week_2/)

Hello everyone,

This is my second report about my project **"Adding write supports for BTRFS"**. There hasn't been much coding in this week and previous week, just some researchs, some style fixes in btrfs code base, and I have managed on setting up fs_shell for btrfs, or now you can say btrfs_shell, based on bfs_shell work. fs_shell is a framework containing all the kernel emulation and the user and scripting interface (Thanks Ingo for the info), this allows to compile and run filesystem (Haiku's, for example btrfs) in userland under Linux or any host systems that can build Haiku.

[[GSoC 2017] Adding write supports for Btrfs](https://www.haiku-os.org/blog/hyche/2017-05-08_gsoc_2017_adding_write_supports_for_btrfs/)

Hello everyone,

My name is Hy (Trac: hyche, freenode IRC: ugen), and this first blog is about my introduction and Btrfs. This is the first time I participate in Google Summer of Code, I also know Haiku through this event. My project in this summer is **write supports for Btrfs** and my main mentors are *mmu_man* (François Revol) and *tqh* (Fredrik Holmqvist).

During the community bonding period, I will

- Set up my development environment (userlandfs and fs_shell).
- Dig into the codebase to know more about Haiku kernel, how other support filesystems work and derive it for Btrfs.
- Try to fix issues to get me familiar with the existed works.

### Btrfs

Btrfs (B-tree filesystem) is a filesystem uses **B+trees** as its main on-disk data structure. It is based on **Copy-on-Write** (CoW) principle which means it does copy only when a write is necessary. The following works will be implemented to bring off write features:
