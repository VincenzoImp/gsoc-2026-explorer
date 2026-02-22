# The Libreswan Project — Project Ideas

**Source:** https://github.com/libreswan/libreswan/wiki/GSoC-2026-Code-Project-Ideas
**Scraped:** 2026-02-22T23:28:47.597232

---

[Libreswan](http://github.com/libreswan) is an [Internet Key
Exchange](https://www.rfc-editor.org/rfc/rfc7296.html) (IKE)
implementation that runs on Linux, FreeBSD, NetBSD and OpenBSD.

While the original IKE and IPsec protocols were drafted in 1998, the
need to deal with an ever changing and increasingly hostile world,
drives the continuous evolution of these standards.  New features,
such as hybrid post-quantum key exchange, are being added; while old
features, such as support for weak cryptographic algorithms are been
removed.  For more background on Libreswan see the [History
Page](/ideas/the-libreswan-project/history).

The Project Ideas listed below have been selected by Libreswan's core
developers with this evolution in mind.  They provide both a technical
challenge, and a way to participate in The Internet's development.
The mentors also have a personal interest in seeing these projects
through to completion.

If you see a project that looks interesting then see the [Contributor
Guidance](/ideas/the-libreswan-project/gsoc-contributor-guidance) for next steps.

If you just have questions, then please feel free to contact us; either on the
[developer mailing list](https://lists.libreswan.org/mailman/listinfo/swan-dev) or [IRC](/ideas/the-libreswan-project/irc).  You can
also email **gsoc at libreswan.org** which is not publicly archived.

It isn't a requirement at you pick one of the ideas below - we also
welcome new ideas.  For instance, additional draft RFCs that could
form the basis of a project can be found
[here](https://datatracker.ietf.org/wg/ipsecme/documents/))!

## Add Support For Announcing Authentication Methods To Libreswan

**Required Skills:** C, UNIX programming

**Preferred Skills:** Network protocols, Cryptographic fundamentals, RFC interpretation

**Libreswan Mentors:** Andrew Cagney, Paul Wouters

**Project size:** 175 hours

**Difficulty:** Medium

**Draft RFC:** [Announcing Supported Authentication Methods in IKEv2](https://tools.ietf.org/html/draft-smyslov-ipsecme-ikev2-auth-announce)

### Description

Currently, during an IKEv2 negotiation, both peers will select the
peer's authentication method independently.  These authentication
methods might not be the same.  Depending on the authentication method
support received from the peer, adjust the authentication if multiple
are supported.  Additionally, if the authentication method uses
certificates, filter the allowed authentication methods based on the
algorithms used in the certificate chain.

Please note that this is an internet standards draft.  Someone
implementing this might find issues with the draft protocol for which
they would need to communicate with the author of the draft to
resolve.

The deliverables are:

- addition to Libreswan's configuration (ipsec.conf), including
  documentation (ipsec.conf.8)

- modifications to negotiate the new mechanism

- modifications to select the applicable authentication method

- additions to the test-suite

The proposal should address each of these areas.


## Use all exchanged messages when computing the authentication MAC

**Required Skills:** C, UNIX programming

**Preferred Skills:** Network protocols, Cryptographic fundamentals, RFC interpretation

**Libreswan Mentors:** Andrew Cagney, Paul Wouters

**Project size:** 175 hours

**Difficulty:** Medium

**Draft RFC:** [Downgrade Prevention for the Internet Key Exchange Protocol Version 2 (IKEv2)](/ideas/the-libreswan-project/https-datatracker-ietf-org-doc-draft-ietf-ipsecme-ikev2-downgrade-prevention)

### Description

IKEv2, when authenticating a peer, computes the MAC (message
authentication code) using only two of the four messages that have
been exchanged during the IKE negotiation.  This proposed RFC adds an
extension so that an authenticated peer uses all four of the exchanged
messages in the MAC calculation.

Please note that this is an internet standards draft.  Someone
implementing this might find issues with the draft protocol for which
they would need to communicate with the author of the draft to
resolve.

The deliverables are:

- addition to Libreswan's configuration (ipsec.conf), including
  documentation (ipsec.conf.8)

- modifications to negotiate the new mechanism

- modifications to (conditionally) compute the new MAC

- additions to the test-suite

The proposal should address each of these areas.


## Add HOST-TO-HOST support on BSD

**Required Skills:** C, UNIX programming

**Preferred Skills:** Network protocols, BSD networking, PFKEY_V2

**Mentors:** Andrew Cagney

**Project size:** 90 hours

**Difficulty:** Medium

### Description

With a host-to-host connection between two peers, all traffic (with
the exception of IKE control messages) is encapsulated in ESP.

While this feature is supported on Linux, support is missing in
Libreswan on the BSDs (FreeBSD, NetBSD, and OpenBSD).

The deliverable are:

- modification to the PFKEY V2 code to support host-to-host
  connections on at least one of FreeBSD or NetBSD

- additions to the test-suite

- (if time permits) modifications and test-suite additions for the
  remaining BSDs.

The proposal should address each of these areas.


## Improve the ACQUIRE to IKE policy lookup by making use of the `policy.index`

**Required Skills:** C, UNIX programming

**Preferred Skills:** Network protocols, Linux networking, XFRM

**Mentors:** Andrew Cagney, Paul Wouters, Tuomo Soini

**Project size** 175 hours

**Difficulty** Medium

### Description

IPsec policies can be installed in the kernel to be "on demand".  When
a packet hits the IPsec subsystem and it matches an "on demand"
policy, the user-land IKE daemon is notified by the kernel so it can
initiate an IKE connection to the target destination.  The
notification, which is called an `acquire`, contains the protocol, and
source and destination addresses.

The `acquire` notification contains an additional field called
`policy.index`.  Currently, when an "on demand" policy is installed in
the kernel, this field is set to `0`.  This means that when the IKE
daemon receives an `acquire` from the kernel, it has to do its own
source/dest based lookup to determine which connection should be
initiated.  The goal of this project is to change this by assigning a
unique `policy.index` number to each connection with an "on demand"
policy, and install that in the kernel.

One complication is with connections that are part of an
(opportunistic) group.  As part of handling the `acquire` these
connections clone themselves into new connections.  Since these clones
cannot share the `policy.index` these policies need to be modified
before being resend to the kernel.

The deliverables are:

- modify the XFRM code to specify a unique policy.index in the kernel,
  and use the policy.index value when looking for connections

  the `reqid` may be a useful unique value

- modify commands to display this unique value

  and as needed, update the test-suite

- produce a test result with the change showing no regressions

  Since the change is under the hood, and affects all Linux tests,
  specific test cases may not be needed.
