# Mesh-under in ns-3 6LoWPAN

**Parent:** The ns-3 Network Simulator Project — Project Ideas
**Source:** https://www.nsnam.org/docs/models/html/sixlowpan.html
**Scraped:** 2026-02-22T23:28:47.555244

---

# 30. 6LoWPAN: Transmission of IPv6 Packets over IEEE 802.15.4 Networks[¶](https://www.nsnam.org#lowpan-transmission-of-ipv6-packets-over-ieee-802-15-4-networks)

This chapter describes the implementation of *ns-3* model for the
compression of IPv6 packets over IEEE 802.15.4-Based Networks
as specified by [ RFC 4944](https://datatracker.ietf.org/doc/html/rfc4944.html) (“Transmission of IPv6 Packets over IEEE 802.15.4 Networks”)
and

[(“Compression Format for IPv6 Datagrams over IEEE 802.15.4-Based Networks”).](https://datatracker.ietf.org/doc/html/rfc6282.html)

**RFC 6282**## 30.1. Model Description[¶](https://www.nsnam.org#model-description)

The source code for the sixlowpan module lives in the directory `src/sixlowpan`

.

### 30.1.1. Design[¶](https://www.nsnam.org#design)

The model design does not follow strictly the standard from an architectural standpoint, as it does extend it beyond the original scope by supporting also other kinds of networks.

Other than that, the module strictly follows [ RFC 4944](https://datatracker.ietf.org/doc/html/rfc4944.html) and

[, with the exception that HC2 encoding is not supported, as it has been superseded by IPHC and NHC compression type (](https://datatracker.ietf.org/doc/html/rfc6282.html)

**RFC 6282**[).](https://datatracker.ietf.org/doc/html/rfc6282.html)

**RFC 6282**IPHC sateful (context-based) compression is supported but, since [ RFC 6775](https://datatracker.ietf.org/doc/html/rfc6775.html)
(“Neighbor Discovery Optimization for IPv6 over Low-Power Wireless Personal Area Networks (6LoWPANs)”)
is not yet implemented, it is necessary to add the context to the nodes manually.

This is possible though the `SixLowPanHelper::AddContext`

function.
Mind that installing different contexts in different nodes will lead to decompression failures.

#### 30.1.1.1. NetDevice[¶](https://www.nsnam.org#netdevice)

The whole module is developed as a transparent NetDevice, which can act as a proxy between IPv6 and any NetDevice (the module has been successfully tested with PointToPointNedevice, CsmaNetDevice and LrWpanNetDevice).

For this reason, the module implements a virtual NetDevice, and all the calls are passed
without modifications to the underlying NetDevice. The only important difference is in
GetMtu behaviour. It will always return *at least* 1280 bytes, as is the minimum IPv6 MTU.

The module does provide some attributes and some tracesources. The attributes are:

Rfc6282 (boolean, default true), used to activate HC1 (

) or IPHC (**RFC 4944**) compression.**RFC 6282**OmitUdpChecksum (boolean, default true), used to activate UDP checksum compression in IPHC.

FragmentReassemblyListSize (integer, default 0), indicating the number of packets that can be reassembled at the same time. If the limit is reached, the oldest packet is discarded. Zero means infinite.

FragmentExpirationTimeout (Time, default 60 seconds), being the timeout to wait for further fragments before discarding a partial packet.

CompressionThreshold (unsigned 32 bits integer, default 0), minimum compressed payload size.

UseMeshUnder (boolean, default false), it enables mesh-under flood routing.

MeshUnderRadius (unsigned 8 bits integer, default 10), the maximum number of hops that a packet will be forwarded.

MeshCacheLength (unsigned 16 bits integer, default 10), the length of the cache for each source.

MeshUnderJitter (ns3::UniformRandomVariable[Min=0.0|Max=10.0]), the jitter in ms a node uses to forward mesh-under packets - used to prevent collisions.


The CompressionThreshold attribute is similar to Contiki’s SICSLOWPAN_CONF_MIN_MAC_PAYLOAD option. If a compressed packet size is less than the threshold, the uncompressed version is used (plus one byte for the correct dispatch header). This option is useful when a MAC requires a minimum frame size (e.g., ContikiMAC) and the compression would violate the requirement.

Note that 6LoWPAN will use an EtherType equal to 0xA0ED, as mandated by [ RFC 7973](https://datatracker.ietf.org/doc/html/rfc7973.html).
If the device does not support EtherTypes (e.g., 802.15.4), this value is discarded.

The Trace sources are:

Tx - exposing packet (including 6LoWPAN header), SixLoWPanNetDevice Ptr, interface index.

Rx - exposing packet (including 6LoWPAN header), SixLoWPanNetDevice Ptr, interface index.

Drop - exposing DropReason, packet (including 6LoWPAN header), SixLoWPanNetDevice Ptr, interface index.


The Tx and Rx traces are called as soon as a packet is received or sent. The Drop trace is invoked when a packet (or a fragment) is discarded.

#### 30.1.1.2. Mesh-Under routing[¶](https://www.nsnam.org#mesh-under-routing)

The module provides a very simple mesh-under routing [[Shelby]](https://www.nsnam.org#shelby), implemented as a flooding
(a mesh-under routing protocol is a routing system implemented below IP).

This functionality can be activated through the UseMeshUnder attribute and fine-tuned using the MeshUnderRadius and MeshUnderJitter attributes.

Note that flooding in a PAN generates a lot of overhead, which is often not wanted. Moreover, when using the mesh-under facility, ALL the packets are sent without acknowledgment because, at lower level, they are sent to a broadcast address.

At node level, each packet is re-broadcasted if its BC0 Sequence Number is not in the cache of the recently seen packets. The cache length (by default 10) can be changed through the MeshCacheLength attribute.

### 30.1.2. Scope and Limitations[¶](https://www.nsnam.org#scope-and-limitations)

#### 30.1.2.1. Context-based compression[¶](https://www.nsnam.org#context-based-compression)

IPHC sateful (context-based) compression is supported but, since [ RFC 6775](https://datatracker.ietf.org/doc/html/rfc6775.html)
(“Neighbor Discovery Optimization for IPv6 over Low-Power Wireless Personal Area Networks (6LoWPANs)”)
is not yet implemented, it is necessary to add the context to the nodes manually.

#### 30.1.2.2. 6LoWPAM-ND[¶](https://www.nsnam.org#lowpam-nd)

Future versions of this module will support [ RFC 6775](https://datatracker.ietf.org/doc/html/rfc6775.html), however no timeframe is guaranteed.

#### 30.1.2.3. Mesh-under routing[¶](https://www.nsnam.org#id2)

It would be a good idea to improve the mesh-under flooding by providing the following:

Adaptive hop-limit calculation,

Adaptive forwarding jitter,

Use of direct (non mesh) transmission for packets directed to 1-hop neighbors.


#### 30.1.2.4. Mixing compression types in a PAN[¶](https://www.nsnam.org#mixing-compression-types-in-a-pan)

The IPv6/MAC addressing scheme defined in [ RFC 6282](https://datatracker.ietf.org/doc/html/rfc6282.html) and

[is different. One adds the PanId in the pseudo-MAC address (4944) and the other doesn’t (6282).](https://datatracker.ietf.org/doc/html/rfc4944.html)

**RFC 4944**The expected use cases (confirmed by the RFC editor) is to *never* have a mixed environment
where part of the nodes are using HC1 and part IPHC because this would lead to confusion on
what the IPv6 address of a node is.

Due to this, the nodes configured to use IPHC will drop the packets compressed with HC1
and vice-versa. The drop is logged in the drop trace as `DROP_DISALLOWED_COMPRESSION`

.

#### 30.1.2.5. Using 6LoWPAN with IPv4 (or other L3 protocols)[¶](https://www.nsnam.org#using-6lowpan-with-ipv4-or-other-l3-protocols)

As the name implies, 6LoWPAN can handle only IPv6 packets. Any other protocol will be discarded.

6LoWPAN can be used alongside other L3 protocols in networks supporting an EtherType (e.g., Ethernet, WiFi, etc.). If the network does not have an EtherType in the frame header (like in the case of 802.15.4), then the network must be uniform, as is all the devices connected by the same same channel must use 6LoWPAN.

The reason is simple: if the L2 frame doesn’t have a “EtherType” field, then there is no demultiplexing at MAC layer and the protocol carried by L2 frames must be known in advance.

### 30.1.3. References[¶](https://www.nsnam.org#references)

[Shelby](https://www.nsnam.org#id1)Shelby and C. Bormann, 6LoWPAN: The Wireless Embedded Internet. Wiley, 2011. [Online]. Available:

[https://books.google.it/books?id=3Nm7ZCxscMQC](https://books.google.it/books?id=3Nm7ZCxscMQC)


## 30.2. Usage[¶](https://www.nsnam.org#usage)

### 30.2.1. Enabling sixlowpan[¶](https://www.nsnam.org#enabling-sixlowpan)

Add `sixlowpan`

to the list of modules built with *ns-3*.

### 30.2.2. Helper[¶](https://www.nsnam.org#helper)

The helper is patterned after other device helpers.

### 30.2.3. Examples[¶](https://www.nsnam.org#examples)

The following example can be found in `src/sixlowpan/examples/`

:

`example-sixlowpan.cc`

: A simple example showing end-to-end data transfer.

In particular, the example enables a very simplified end-to-end data transfer scenario, with a CSMA network forced to carry 6LoWPAN compressed packets.

### 30.2.4. Tests[¶](https://www.nsnam.org#tests)

The test provided checks the connection between two UDP clients and the correctness of the received packets.

## 30.3. Validation[¶](https://www.nsnam.org#validation)

The model has been validated against WireShark, checking whatever the packets are correctly interpreted and validated.
