# History
Page

**Parent:** The Libreswan Project — Project Ideas
**Source:** https://github.com/libreswan/libreswan/wiki/History
**Scraped:** 2026-02-22T23:28:47.597336

---

# History of The Libreswan Project

Libreswan has been under active development for over 15 years, going
back to [The FreeS/WAN Project](http://www.freeswan.org/) founded in
1996 by [John
Gilmore](http://en.wikipedia.org/wiki/John_Gilmore_%28activist%29) and
[Hugh Daniel](http://en.wikipedia.org/wiki/Hugh_Daniel). The code was
forked into a continuation as The Openswan Project in 2003. In 2012 it
was forced to rename itself to The Libreswan Project due to a lawsuit
filed over the trademark of the name "openswan".

## The FreeS/WAN days (1995 - 2003)

The goal was to develop IPsec and DNS standards for encryption for use
on the internet. The goal was to encrypt 5% of internet traffic per
year, until the entire internet would only use encrypted communications.
The FreeS/WAN project usually had about five paid people working on the
code, all paid for by Gilmore.

At the time encryption was very uncommon, and free software implementing
encryptions was scarce. SSLeay, the precursor to OpenSSL was being
developed for encryption between web servers and clients. Most people
were not thinking about nation state eavesdropping and monitoring, but
the [Crypto
War](http://en.wikipedia.org/wiki/Crypto:_How_the_Code_Rebels_Beat_the_Government%E2%80%94Saving_Privacy_in_the_Digital_Age)
was raging. The goal of the freeswan software was to deploy widespread
[Opportunistic
Encryption](http://en.wikipedia.org/wiki/Opportunistic_encryption) and
make encryption ubiquitous before *national security* reasons could
outlaw encryption for the public. To prevent the US government from
claiming ownership of freeswan through *National Security Letters*
("NSLs"), Gilmore himself and other US citizens were not allowed to
write any code for freeswan. This restriction caused a lot of harm
because it prevented the freeswan code from being merged into the Linux
kernel and made it much harder for individuals to deploy freeswan.

Meanwhile, corporations required secure connections over the internet
and the need for Virtual Private Networks ("VPNs") was another
motivation to develop a usable encryption standard. These also used
IPsec but in various different ways to satisy the needs of different
companies.

The standard that emerged from the [Internet Engineering Task
Force](http://www.ietf.org/) became known as the *IPsec* suite. It
consists of many standards documents (RFC's) that handle the
authentication via the *Internet Key Exchange* protocol and uses IPsec
transforms to encrypt data. Various encryption and authentication
algorithms are supported and standarized. Adoption of Opportunistic
Encryption was non-existent. A few technical hurdles made deployment
difficult. The secure version of DNS got delayed by many years. The DNS
[root zone](https://en.wikipedia.org/wiki/DNS_root_zone) finally got
signed using
[DNSSEC](https://wiki.tools.isoc.org/DNSSEC_History_Project) in July 15,
2010 - after a decade delay. During that time, freeswan's use of the
DNSSEC was prevented by a late move within the IETF that stated only DNS
itself could use DNSSEC KEY records, now renamed to DNSKEY records. This
meant that freeswan had to revert back to bad old TXT records. IPsec got
its own DNS record type [IPSECKEY](http://tools.ietf.org/html/rfc4025)
in 2005 but it would take a number of years for deployed DNS software to
actually support this new record type. Additionally, endusers never got
the expected access to their [reverse
DNS](https://en.wikipedia.org/wiki/Reverse_DNS_lookup) zones to publish
their public keys required for OE IPsec.

Linux kernel adoption of freeswan never happened either. In part due to
the "non US code" rule enforced by Gilmore. Lack of cooperation by the
kernel people responsible for networking and crypto in the Linux kernel
also played a big part. Despite the freeswan's team solid appearances
for a few years at the combined [Ottawa Linux
Symposium](http://www.linuxsymposium.org/) and Kernel Summit
conferences, the Linux people embarked on their own paths, eventually
going through a number of new crypto subsystems that failed to gain
widespread support. This resulted in both teams spending years of effort
maintaining two competing kernel IPsec stacks, KLIPS vs NETKEY, where
even today there is not one unifying stack that has the good features of
both stacks.

The public at large seemed less concerned about government
eavesdropping. The [Echelon](http://en.wikipedia.org/wiki/ECHELON)
spying network was revealed by Nicky Hager and had no noticeable impact
on the deployment of encrypted communications. Throughout 90's and
2000's, not many people considered an unencrypted internet a real
problem until the revelations of [Edward
Snowden](http://en.wikipedia.org/wiki/Edward_Snowden) in 2013, a full
decade after Gilmore had given up on his attempt to encrypt the entire
internet with freeswan.

## From FreeS/WAN to Openswan (2003 - 2011)

Commercial companies were using freeswan as one of their key
interoperability tests during "bake off" events. Andreas Steffen wrote a
large patch to add X.509 support to freeswan, something that Gilmore
refused to merge in. NAT-Traversal support written by Mathieu Lafon was
another essential feature needed for commercial VPN support that Gilmore
refused to let into the freeswan code. One of the freeswan volunteers,
Ken Bantoft, maintained a version of freeswan with these patches merged
in, and called it "super-freeswan". Gilmore was not happy with the use
of the name "freeswan" as he did not want those *internet crippling
technologies* associated with the freeswan name.

In July 2003, Gilmore and Paul Wouters, another active freeswan
volunteer, met up at the [Chaos Communications
Camp](http://en.wikipedia.org/wiki/Chaos_Communication_Camp) near Berlin
and devised a plan to continue IPsec development using freeswan without
Gilmore's sponsorship. Wouters and the other volunteers would fork the
code, and Gilmore would do one more release of freeswan with large
chunks of code removed that was only useful for commercial VPN
deployments. This effort started under the workname "openswan", based on
the freebsd/openbsd name history. The name stuck. Gilmore released two
more freeswan releases with VPN code removed and ended his project.

The Openswan Project moved the focus of the software from OE towards VPN
technology in general. Four of the openswan volunteers founded the
company Xelerance to offer commercial support for openswan that would be
used to continue openswan development. Unhampered by restrictions
imposed by Gilmore with freeswan, the openswan code took over from
freeswan and saw widespread adoption and inclusion into the main Linux
distributions such as Red Hat Enterprise Linux ("RHEL"), Debian and SuSe
Linux. Enterprise features such as XAUTH and SAref tracking for
L2TP/IPsec support were added. Openswan worked well in the enterprise.
This in itself caused a problem for Xelerance. Enterprise users mostly
used RHEL, and thus paid Red Hat for commercial support. IPsec and IKE
worked well enough that its users hardly ever wanted new features
developed. Or they were willing to wait for others to pay or develop
these features. While Xelerance still sponsored hosting for The Openswan
Project, it changed its focus to survive. One by one the original
founders left the company. Wouters was the last one to leave in December
2011. His departure triggered a dispute between The Openswan Project and
Xelerance about who owned the openswan brand.
[Lawsuits](https://nohats.ca/wordpress/openswan/) were filed, and as is
common when free software developers are sued by corporations, it was
cheaper and easier to walk away and rename the software. Libreswan was
born.

## Libreswan (2011 - now)

Libreswan is maintained by The Libreswan Project.
