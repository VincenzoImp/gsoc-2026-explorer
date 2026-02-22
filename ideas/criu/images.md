# Images

**Parent:** CRIU — Project Ideas
**Source:** https://criu.org/Images
**Scraped:** 2026-02-22T23:28:47.591112

---

# Images

[Jump to navigation](https://criu.org#mw-head)

[Jump to search](https://criu.org#searchInput)

The criu utility dumps the state of processes/containers into a set of image files. This article describes the format of them.

## Types of image files[[edit](https://criu.org/index.php?title=Images&action=edit§ion=1)]

CRIU images can be in one of the following formats

- criu specific images in google protocol buffer format (PB format)
- criu specific images with binary data in it
- image files in 3rd party format (a.k.a. raw images)

## Images in criu-specific format[[edit](https://criu.org/index.php?title=Images&action=edit§ion=2)]

All criu-specific image files begin with 2 32-bit magic cookies. The first cookie is the type of file (see below) the second is the optional sub-type of image. Images in PB format are followed by zero or more entries of the same type (not size!), each entry is preceded with 32-bit entry size value (not including this 32-bit value itself). Optionally each entry may be followed by extra payload which depends on the entry type.

Currently there are 3 types of images

- Inventory file
- This is the image file describing the set. It doesn't have sub-type magic.

- Image file
- Regular image. Most of the text below is about these files.

- Auxiliary file
- File that is not image, but criu generates one and it happens to be in protobuf format too. For now we have only stats and irmap cache files of that type. They also have sub-type magic.

IOW protocol-buffers image files look like

IMAGE_FILE ::= MAGIC [MAGIC_2] { ENTRY } ENTRY ::= SIZE PAYLOAD [ EXTRA ] PAYLOAD ::= "message encoded in ProtocolBuffer format" EXTRA ::= "arbitrary blob, depends on the PAYLOAD contents" MAGIC ::= "32 bit integer" MAGIC_2 ::= "32 bit integer" SIZE ::= "32 bit integer, equals the PAYLOAD length"

Or, you can visualize it like

| Type | Size, bytes |
|---|---|
| Magic | 4 |
| Size0 | 4 |
| Message0 | Size0 |
| ... | ... |
| SizeN | 4 |
| MessageN | SizeN |

The amount of entries in a image file depends on the type of file.

### Images with PB data[[edit](https://criu.org/index.php?title=Images&action=edit§ion=3)]

Such images can be one of

- Array image files
- In these files the amount of entries can be any. You should read the image file up to the EOF to find out the exact number.

- Single-entry image files
- In these files exactly one entry is stored.

A file type can be guessed by the magic. The description of the entries in ProtocolBuffers language are in respective .proto files which reside in `images/`

directory in the source tree.

| name | type | description | extra payload | describing proto file |
|---|---|---|---|---|
| inventory | single-entry | Top level description of images | - | inventory.proto |
| fdinfo | array |
|

[files](https://criu.org/Category:Files)opened with`open(2)`

syscall[Address space](https://criu.org/Memory_dumping_and_restoring)information (VMAs, segments, exe file, etc.)`entry.bytes`

bytes of data sitting in a pipe[tree linkage](https://criu.org/Tree_after_restore)[Unix sockets](https://criu.org/Unix_sockets)`entry.length`

bytes of data, one entry per packet[invisible files](https://criu.org/Invisible_files))[invisible files](https://criu.org/Invisible_files)[TCP connection](https://criu.org/TCP_connection)state (including data in queues)`entry.inq_len`

bytes of in-queue data followed by `entry.outq_len`

bytes of out-queue data[Mountpoints](https://criu.org/Mountpoints)information[TTYs](https://criu.org/TTYs)[TTYs](https://criu.org/TTYs)[network](https://criu.org/Category:Network)devices### Images with memory dumps[[edit](https://criu.org/index.php?title=Images&action=edit§ion=4)]

*Main article: memory dumps*.

Anonymous memory contents (both private and shared) is stored in two types of images:

- Pagemap files
- These files contain info about which virtual regions are populated with data. The file is a set of protobuf messages.

|

**Note**: Even though pagemap is an array kind of image (and can be included to the previous type), first pb message is of type pagemap_head and all the following ones are of type pagemap_entry.- Pages files
- These contain 4k pages that are to be put into the memory according to the pagemap.

## Raw images[[edit](https://criu.org/index.php?title=Images&action=edit§ion=5)]

These images contain data collected by CRIU with the help of some external tools.

| Name | Tool supporting the format | Description | Decode command |
|---|---|---|---|
| ifaddr | ip from iproute2 | IP addresses on network devices | cat ifaddr-8.img | ip addr showdump |
| route | ip from iproute2 | Routing tables | cat route-8.img | ip route showdump |
| tmpfs | tar + gzip | Contents of a tmpfs filesystem | tar -tzf tmpfs-dev-49.tar.gz.img |

## Notes about protobuf[[edit](https://criu.org/index.php?title=Images&action=edit§ion=6)]

We have a registered field number (1018) for [custom options](https://developers.google.com/protocol-buffers/docs/proto#options) of all kinds. See protobuf/opts.proto for more info.

## See also[[edit](https://criu.org/index.php?title=Images&action=edit§ion=7)]

[CRIT](https://criu.org/CRIT): a tool to decode images to a human readable format[What's bad with V1 images](https://criu.org/What%27s_bad_with_V1_images)[Image field merging](https://criu.org/Image_field_merging)[Memory dumps](https://criu.org/Memory_dumps)
