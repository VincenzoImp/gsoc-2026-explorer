# Sockets

**Parent:** CRIU — Project Ideas
**Source:** https://criu.org/Sockets
**Scraped:** 2026-02-22T23:28:47.591245

---

# Sockets

[Jump to navigation](https://criu.org#mw-head)

[Jump to search](https://criu.org#searchInput)

## Unix sockets initial support[[edit](https://criu.org/index.php?title=Sockets&action=edit§ion=1)]

Currently we support Unix socket of all kinds, UDP both IPv4 and IPv6, TCP in Listen and (!) [Established states](https://criu.org/TCP_connection) and Netlink ones.

The cpt part uses the sock_diag engine to collect extended information about socket, then CRIU uses the files dumping engine to get access to sockets state.

The restore part of Unix sockets is the most tricky part. Listen sockets are just restored, this is simple. Connected sockets are restored like this:

- One end establishes a listening anon socket at the desired descriptor;
- The other end just creates a socket at the desired descriptor;
- All sockets, that are to be connect()-ed call connect. Unix sockets do not block connect() till the accept() time and thus we continue with...
- ... all listening sockets call accept() and ... dup2 the new fd into the accepting end.

There's a problem with this approach -- socket names are not preserved, but looking into our OpenVZ implementation I think this is OK for existing apps.
