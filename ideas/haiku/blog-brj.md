# GSoC 2018 log

**Parent:** Haiku — Project Ideas
**Source:** https://www.haiku-os.org/blog/brj
**Scraped:** 2026-02-22T23:28:47.590458

---

#### Blog-O-Sphere

[Haiku Activity & Contract Report, January 2026](https://www.haiku-os.org/blog/waddlesplash/2026-02-12-haiku_activity_contract_report_january_2026/)[The Gerrit code review iceberg, episode 5](https://www.haiku-os.org/blog/pulkomandy/2026-02-03-the_gerrit_pending_review_iceberg_5/)[Haiku Activity & Contract Report, December 2025](https://www.haiku-os.org/blog/waddlesplash/2026-01-12-haiku_activity_contract_report_december_2025/)[The Gerrit code review iceberg, episode 4](https://www.haiku-os.org/blog/pulkomandy/2025-12-31-the_gerrit_pending_review_iceberg_4/)[The Gerrit code review iceberg, episode 3](https://www.haiku-os.org/blog/pulkomandy/2025-12-19-the_gerrit_pending_review_iceberg_3/)[Haiku Activity & Contract Report, November 2025 (ft. Go)](https://www.haiku-os.org/blog/waddlesplash/2025-12-12-haiku_activity_contract_report_november_2025/)[The Gerrit code review iceberg, episode 2](https://www.haiku-os.org/blog/pulkomandy/2025-12-05-the_gerrit_pending_review_iceberg_2/)[The Gerrit code review iceberg](https://www.haiku-os.org/blog/pulkomandy/2025-11-24-the_gerrit_pending_review_iceberg/)[Haiku Activity & Contract Report, October 2025](https://www.haiku-os.org/blog/waddlesplash/2025-11-11-haiku_activity_contract_report_october_2025/)[Haiku Activity & Contract Report, September 2025](https://www.haiku-os.org/blog/waddlesplash/2025-10-13-haiku_activity_contract_report_september_2025/)

[[GSoc 2019] Weeks #4, #5 and #6 progress report](https://www.haiku-os.org/blog/brj/2019-07-16_gsoc_2019_weeks_4_5_and_6_progress_report/)

Hello everybody! It’s been a while since my [previous post](https://www.haiku-os.org/blog/brj/2019-06-17_gsoc_2019_weeks_1_2_and_3_progress_reports/).

This post is a short summary of all work done upto this point.

During the past few weeks, I was able to add the following features to the current btrfs implementation

## Creating new files

The basic algorithm behind creating new files is allocating a new inode, updating the fs tree to reflect this, creating a hard link in the directory containing the file and finally updating the cache. However, we must make sure to deallocate memory and clean up any partial changes in case of any errors.

[[GSoC 2019] Weeks #1, #2 and #3 progress reports](https://www.haiku-os.org/blog/brj/2019-06-17_gsoc_2019_weeks_1_2_and_3_progress_reports/)

Hello everybody! It’s been a while since my [previous post](https://www.haiku-os.org/blog/brj/2019-05-07_gsoc_2019_improving_the_btrfs_filesystem/).

This post is a short summary of all the work done upto this point. For a
detailed report of every day, visit [this blog I set up using Blogger](http://gsocbrj.blogspot.com/).

## Week 1

As mentioned in my [proposal](https://tiny.cc/yq6b6y), the target for week #1
was document the current btrfs implementation. As part of this, I documented
the following classes

- Chunk
- Inode
- BTree
- Attribute
- AttributeIterator
- DirectoryIterator

Week #1 went smoothly without any problems.

[[GSoC 2019] Improving the btrfs filesystem](https://www.haiku-os.org/blog/brj/2019-05-07_gsoc_2019_improving_the_btrfs_filesystem/)

# Introduction

Hello, world!

As some of you might be aware, I’m one of the students selected for GSoC 2019. My name is Bharathi Ramana Joshi. You may know me as brj, my initials, from the mailing lists and IRC channel. I’m pursuing an underguate degree in Computer Science and Engineering from Keshav Memorial Institute of Technology, India.

# Project: Improving the btrfs filesystem

As the title suggests, I shall be working on Haiku’s btrfs implementation for most of the summer. Currently, it is possible to read and write directories but only read from files. By the end of GSoC 2019, I aim to implement file writing.
