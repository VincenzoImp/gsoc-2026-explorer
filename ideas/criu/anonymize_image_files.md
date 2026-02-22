# Anonymize image files

**Parent:** CRIU — Project Ideas
**Source:** https://criu.org/Anonymize_image_files
**Scraped:** 2026-02-22T23:28:47.591050

---

# Anonymize image files

[Jump to navigation](https://criu.org#mw-head)

[Jump to search](https://criu.org#searchInput)

When resolving a bug from user criu team often needs the images that caused the problem, since using pure logs is not always helps to understand the cause of the problem. At the same time, sharing images with developers may be impossible since they may contain sensitive information -- memory contents with passwords/keys/secrets, paths to files on dist that may be not-to-be-shared.

So all the secrets must be removed from images, but still we should keep the possibility to work with them in terms of objects criu uses for restore. I.e. everything that sits in the anonymous images must be open-able, connect-able, mmap-able, etc-able.

## List of data to shred[[edit](https://criu.org/index.php?title=Anonymize_image_files&action=edit§ion=1)]

- Memory contents. For the sake of investigation, all the memory contents can be just removed. Only the sizes of pages*.img files and pagemaps are enough.
- Paths to files. Here we should keep the paths relations to each other. The simplest way seem to be replacing file names with "random" (or sequential) strings, BUT (!) keeping an eye on making this mapping be 1:1. Note, that file paths may also sit in sk-unix.img.
- Registers.
- Process names. (But pid-to-pid and sid/pgid relations should be kept).
- Contents of streams, i.e. pipe/fifo data, sk-queue, tcp-stream, tty data.
- Ghost files.
- Tarballs with tmpfs-s.
- IP addresses in sk-inet-s, ip tool dumps and net*.img.
