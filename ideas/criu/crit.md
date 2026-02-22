# CRIT

**Parent:** CRIU — Project Ideas
**Source:** https://criu.org/CRIT
**Scraped:** 2026-02-22T23:28:47.590967

---

# CRIT

[Jump to navigation](https://criu.org#mw-head)

[Jump to search](https://criu.org#searchInput)

*This page describes the CRIT Python tool. For the Go library, see CRIT (Go library)*.

CRiu Image Tool is a feature-rich replacement for existing "criu show". It is written completely in Python, so it is quite easy to read the code and extend its features.

## Usage[[edit](https://criu.org/index.php?title=CRIT&action=edit§ion=1)]

usage: crit [-h] {decode,encode,info,x,show} ... CRiu Image Tool positional arguments: {decode,encode,info,x,show} Use crit CMD --help for command-specific help decode convert criu image from binary type to json encode convert criu image from json type to binary info show info about image x explore image dir show convert criu image from binary to human-readable json optional arguments: -h, --help show this help message and exit

### Pretty output[[edit](https://criu.org/index.php?title=CRIT&action=edit§ion=2)]

`crit decode`

prints JSON text in one line. This can be read by any further JSON-aware tool for parsing. For human eyes it's more convenient to read JSON multi-line with indentation. CRIT can do this when using the `show`

action or the `--pretty`

option.

Wend doing pretty optput CRIT does a little bit more, than just multiline indented JSON.

- Addresses and registers
- VM addresses and core.img register values are all printed in hex. Since JSON doesn't support this form of numbers, such fields are encoded as strings.

- Bit-fields
- Such things as flags and masks (e.g. sig-block mask) are also better understood when written in hex, so CRIT does this.

- IP addresses
- By default those a printed in decimal, but the "1.2.3.4" for v4 or "::1" for v6 can be seen in the --pretty mode.

- Symbolic names for flags
- Some known bit sets (e.g. MAP_PRIVATE, MAP_ANONYMOUS, etc. for vma->flags) are shown with names.

- Device numbers
- If the field is known to be of
`dev_t`

type, it's printed in the`major:minor`

manner

## Functionality[[edit](https://criu.org/index.php?title=CRIT&action=edit§ion=3)]

### Convert images from IMG to JSON[[edit](https://criu.org/index.php?title=CRIT&action=edit§ion=4)]

`crit decode`

is the replacement for the (rather nasty) `criu show`

code. This is also the way to edit the images before restoring from them.

It uses [text_format](https://developers.google.com/protocol-buffers/docs/reference/python/google.protobuf.text_format-module) as a human-readable format for protobuf messages.

The output file is structured in the following way.

Without "--pretty":

{ "magic" : "FOO", "entries" : [{"foo": "bar", "bar": "foo", "extra": "abc"}, {"foo": "bar", "bar" : "foo", "extra" : "abc"} ]}

With "--pretty":

{ "magic" : "FOO", "entries" : [ { "foo" : "bar", "bar" : "foo", "extra" : "abc" }, { "foo" : "bar", "bar" : "foo", "extra" : "abc" } ] }

**Example("crit decode -i core-5679.img --pretty")**

{ "magic": "CORE", "entries": [ { "mtype": "X86_64", "thread_core": { "futex_rla_len": 24, "sched_policy": 0, "sched_nice": 0, "futex_rla": 0, "signals_p": {}, "sas": { "ss_size": 0, "ss_sp": 0, "ss_flags": 2 } }, "thread_info": { "fpregs": { "st_space": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], "fop": 0, "rdp": 0, "twd": 0, "mxcsr": 8064, "swd": 0, "rip": 0, "xsave": { "ymmh_space": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], "xstate_bv": 2 }, "xmm_space": [ 0, 4278190080, 4294967295, 4294967295, 1701145715, 3219568, 0, 0, 0, 0, 33, 0, 792358505, 1953460082, 1852400175, 0, 942882145, 876295483, 774519349, 1031303283, 893073459, 976565307, 1937255978, 859661936, 993344312, 3814708, 65, 0, 37049520, 0, 37049632, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4294901760, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], "cwd": 0, "mxcsr_mask": 65535 }, "clear_tid_addr": 0, "gpregs": { "gs": "0x0", "ip": "0x7f172cf1ea04", "cx": "0xffffffffffffffff", "cs": "0x33", "ax": "0x38", "orig_ax": "0x38", "di": "0x1200011", "es": "0x0", "gs_base": "0x0", "r14": "0x0", "r15": "0x2355e00", "r12": "0x7ffffdbf74f0", "r13": "0x0", "r10": "0x7f172d83d9d0", "r11": "0x246", "fs_base": "0x7f172d83d700", "bp": "0x7ffffdbf7530", "dx": "0x0", "bx": "0x0", "ds": "0x0", "ss": "0x2b", "sp": "0x7ffffdbf74f0", "r8": "0x0", "r9": "0x0", "fs": "0x0", "si": "0x0", "flags": "0x246" } }, "tc": { "timers": { "real": { "isec": 0, "vusec": 0, "iusec": 0, "vsec": 0 }, "virt": { "isec": 0, "vusec": 0, "iusec": 0, "vsec": 0 }, "prof": { "isec": 0, "vusec": 0, "iusec": 0, "vsec": 0 } }, "cg_set": 1, "signals_s": {}, "blk_sigset": "0x10002", "exit_code": 0, "rlimits": { "rlimits": [ { "max": 18446744073709551615, "cur": 18446744073709551615 }, { "max": 18446744073709551615, "cur": 18446744073709551615 }, { "max": 18446744073709551615, "cur": 18446744073709551615 }, { "max": 18446744073709551615, "cur": 8388608 }, { "max": 18446744073709551615, "cur": 0 }, { "max": 18446744073709551615, "cur": 18446744073709551615 }, { "max": 62844, "cur": 62844 }, { "max": 4096, "cur": 1024 }, { "max": 65536, "cur": 65536 }, { "max": 18446744073709551615, "cur": 18446744073709551615 }, { "max": 18446744073709551615, "cur": 18446744073709551615 }, { "max": 62844, "cur": 62844 }, { "max": 819200, "cur": 819200 }, { "max": 0, "cur": 0 }, { "max": 0, "cur": 0 }, { "max": 18446744073709551615, "cur": 18446744073709551615 } ] }, "comm": "loop.sh", "flags": 1077960704, "task_state": 1, "personality": 0 } } ] }

Decode also supports input via STDIN instead of the "-i" flag.

cat "core-5679.img" | crit decode

### Convert images from JSON to IMG[[edit](https://criu.org/index.php?title=CRIT&action=edit§ion=5)]

`crit encode`

converts the image from JSON to IMG. Standard usage would look like:

crit encode -i core-5679.json -o core-5679.img

Encode also supports input via STDIN instead of the "-i" flag.

cat "core-5679.json" | crit encode

Incase a "-o" flag is not specified the input is piped out to STDOUT.

### Generate core files out of task images[[edit](https://criu.org/index.php?title=CRIT&action=edit§ion=6)]

Moved into separate project called [criu-coredump](https://criu.org/Criu-coredump).

### Show images statistics[[edit](https://criu.org/index.php?title=CRIT&action=edit§ion=7)]

`crit x`

allows you to explore image statistics.
E.g. Total number of processes, files, memory, sockets, etc.

crit x $directory_with_images <explore type>

Supported explorers are

- 'ps'
- to show process tree

- 'fds'
- to show files used by tasks

- 'mems'
- to show memory mappings info

### Show images Info[[edit](https://criu.org/index.php?title=CRIT&action=edit§ion=8)]

Image of a info such as its "COUNT" and "MAGIC" can be displayed using the INFO command.

**Example("crit info core-5679.img")**

{ "count": 1, "magic": "CORE" }

## Planned functionality[[edit](https://criu.org/index.php?title=CRIT&action=edit§ion=9)]

### On-the-fly conversion[[edit](https://criu.org/index.php?title=CRIT&action=edit§ion=10)]

There's an idea to make CRIU spawn CRIT and read images "through" it, to allow for at-the-restore-time modifications. For details, see [https://github.com/checkpoint-restore/criu/issues/59](https://github.com/checkpoint-restore/criu/issues/59).

### Convert between different image versions[[edit](https://criu.org/index.php?title=CRIT&action=edit§ion=11)]

Right now we store the images version in inventory.img and collect info about [what's bad with V1 images](https://criu.org/What%27s_bad_with_V1_images). If some day we have v2, CRIT will convert from v1. And for backward compatibility we'll use on-the-fly conversion when restoring from old images.

### Check/validate images[[edit](https://criu.org/index.php?title=CRIT&action=edit§ion=12)]

Check that

- all images are present
- the inter-images IDs are in consistent state

For details, see [https://github.com/checkpoint-restore/criu/issues/44](https://github.com/checkpoint-restore/criu/issues/44).

[Anonymize image files](https://criu.org/Anonymize_image_files)[[edit](https://criu.org/index.php?title=CRIT&action=edit§ion=13)]

Since images contain raw memory dumps people may refuse to send us images for debugging. Need to anonymize them, i.e. -- remove this sensitive information.
