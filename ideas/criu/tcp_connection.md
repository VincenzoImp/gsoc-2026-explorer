# how it's done

**Parent:** CRIU — Project Ideas
**Source:** https://criu.org/TCP_connection
**Scraped:** 2026-02-22T23:28:47.591180

---

# TCP connection

[Jump to navigation](https://criu.org#mw-head)

[Jump to search](https://criu.org#searchInput)

This page describes how we handle established TCP connections.

## TCP repair mode in kernel[[edit](https://criu.org/index.php?title=TCP_connection&action=edit§ion=1)]

The `TCP_REPAIR`

socket option was added to the kernel 3.5 to help with C/R for TCP sockets.

When this option is used, the socket is switched into a special mode, in which any action performed on it does not result in anything defined by an appropriate protocol actions, but rather directly puts the socket into the state that the socket is expected to be in at the end of a successfully finished operation.

For example, calling `connect()`

on a repaired socket just changes its state to `ESTABLISHED`

,
with the peer address set as requested.
The `bind()`

call forcibly binds the socket to a given address (ignoring any potential conflicts).
The `close()`

call closes the socket without any transient `FIN_WAIT`

/`TIME_WAIT`

/etc states,
socket is silently killed.

### Sequences[[edit](https://criu.org/index.php?title=TCP_connection&action=edit§ion=2)]

To restore the connection properly, bind() and connect() is not enough. One also needs to restore the
TCP sequence numbers. To do so, the `TCP_REPAIR_QUEUE`

and `TCP_QUEUE_SEQ`

options were introduced.

The former one selects which queue (input or output) will be repaired and the latter gets/sets the sequence. Note setting the sequence is only possible on CLOSE-d socket.

### Packets in queue[[edit](https://criu.org/index.php?title=TCP_connection&action=edit§ion=3)]

When set the queue to repair as described above, one can call recv or send syscalls on a repaired socket. Both calls
result on peeking or poking data from/to the respective queue. This sounds funny, but yes, for repaired socket one
can receve the outgoing and send the incoming queues. Using the `MSG_PEEK`

flag for `recv()`

is required.

### Options[[edit](https://criu.org/index.php?title=TCP_connection&action=edit§ion=4)]

There are 4 options that are negotiated by the socket at the connecting stage. These are

- mss_clamp -- the maximum size of the segment peer is ready to accept
- snd _scale -- the scale factor for a window
- sack -- whether selective acks are permitted or not
- tstamp -- whether timestamps on packets are supported

All four can be read with `getsockopt()`

calls to a socket and in order to restore them the `TCP_REPAIR_OPTIONS`

sockoption is introduced.

## Timestamp[[edit](https://criu.org/index.php?title=TCP_connection&action=edit§ion=5)]

"The sender's timestamp clock is used as a source of monotonic non-decreasing values to stamp the segments"(rfc7323). The Linux kernel uses the jiffies counter as the tcp timestamp.

`#define tcp_time_stamp ((__u32)(jiffies))`


We add the `TCP_TIMESTAMP`

options to be able to compensate a difference between jiffies counters, when a connection is migrated on another host. When a connection is dumped, criu calls `getsockopt(TCP_TIMESTAMP)`

to get a current timestamp, then on restore it calls `setsockopt(TCP_TIMESTAMP)`

to set this timestamp as a starting point.

## Checkpoint and restore TCP connection[[edit](https://criu.org/index.php?title=TCP_connection&action=edit§ion=6)]

With the above sockoptions dumping and restoring TCP connection becomes possible. The criu just reads the socket state and restores it back letting the protocol resurrect the data sequence.

One thing to note here — while the socket is closed between dump and restore the connection should be "locked", i.e.
no packets from peer should enter the stack, otherwise the RST will be sent by a kernel. In order to do so a simple
netfilter rule is configured that drops all the packets from peer to a socket we're dealing with. This rule sits
in the host netfilter tables after the criu dump command finishes and it should be there when you issue the
criu restore one. The locking method can be specified using the

option.
[--network-lock](https://criu.org/CLI/opt/--network-lock)

Another thing to note is -- on restore there should be available the IP address, that was used by the connection. This is automatically so if restore happens on the same box as dump. In case of hand-made live migration the IP address should be copied too.

That said, the command line option

should be used when calling criu to explicitly state, that the
caller is aware of this "transitional" state of the netfilter.
[--tcp-established](https://criu.org/CLI/opt/--tcp-established)

In case the target process lives in NET namespace the connection locking happens the other way. Instead of
per-connection iptables rules the "network-lock"/"network-unlock" [action scripts](https://criu.org/Action_scripts) are called so that the user
could isolate the whole netns from network. Typically this is done by downing the respective veth pair end.

## States[[edit](https://criu.org/index.php?title=TCP_connection&action=edit§ion=7)]

### TCP_SYN_SENT[[edit](https://criu.org/index.php?title=TCP_connection&action=edit§ion=8)]

There is only one difference with TCP_ESTABLISHED, we have to restore a socket and disable the repair mode before calling `connect()`

. The kernel will send a one syn-sent packet with the same initial sequence number and sets the TCP_SYN_SENT state for the socket.

### Half-closed sockets[[edit](https://criu.org/index.php?title=TCP_connection&action=edit§ion=9)]

A socket is half-closed when it sent or received a fin packet. These sockets are in one for these states: TCP_FIN_WAIT1, TCP_FIN_WAIT2, TCP_CLOSING, TCP_LAST_ACL, TCP_CLOSE_WAIT. To restore these states, we restore a socket into the TCP_ESTABLISHED state and then we call shutfown(SHUT_WR), if a socket has sent a fin packet and we send a fake fin packet, if a socket has received it before. For example, if we want to restore the TCP_FIN_WAIT1 state, we have to call shutfown(SHUT_WR) and we can send a fake ack to the fin packet to restore the TCP_FIN_WAIT2 state.
