# http://gcc.gnu.org/ml/gcc-patches/2012-08/msg00362.html

**Parent:** GNU Compiler Collection (GCC) — Project Ideas
**Source:** http://gcc.gnu.org/ml/gcc-patches/2012-08/msg00362.html
**Scraped:** 2026-02-22T23:28:47.609582

---

This is the mail archive of the
`gcc-patches@gcc.gnu.org`
mailing list for the [GCC project](http://gcc.gnu.org/).

| Index Nav: |
[
|
|---|

*From*: "Joseph S. Myers" <joseph at codesourcery dot com>*To*: Ian Lance Taylor <iant at google dot com>*Cc*: Hans-Peter Nilsson <hp at bitrange dot com>, Dimitrios Apostolou <jimis at gmx dot net>, <gcc-patches at gcc dot gnu dot org>*Date*: Tue, 7 Aug 2012 15:07:15 +0000*Subject*: Re: add strnlen to libiberty (was Re: Assembly output optimisations)*References*: <[alpine.LNX.2.02.1208070228080.20463@localhost.localdomain](http://gcc.gnu.org/msg00329.html)> <[alpine.LNX.2.02.1208070728170.20463@localhost.localdomain](http://gcc.gnu.org/msg00333.html)> <[CAKOQZ8yTqmHJpG58met96KazNoMOdren_mnSY7fsYuA_09XR1Q@mail.gmail.com](http://gcc.gnu.org/msg00335.html)> <[alpine.LNX.2.02.1208070840070.20463@localhost.localdomain](http://gcc.gnu.org/msg00336.html)> <[CAKOQZ8zNTTpR2-TXBXTzQkPxO5EyKs=wqyshvPvfPGYgM3Qu0Q@mail.gmail.com](http://gcc.gnu.org/msg00339.html)> <[alpine.BSF.2.00.1208070524050.28450@dair.pair.com](http://gcc.gnu.org/msg00344.html)> <[CAKOQZ8z7Rua29G81P2qo-1M-LrQWXpvKgN7e0e1yzqzi38vsWw@mail.gmail.com](http://gcc.gnu.org/msg00357.html)>

On Tue, 7 Aug 2012, Ian Lance Taylor wrote: > On Tue, Aug 7, 2012 at 2:30 AM, Hans-Peter Nilsson <hp@bitrange.com> wrote: > > > > Just don't forget that libiberty isn't a target library anymore. > > To wit, the (GCC) run-time exception is moot for that code, AFAIK. > > Maybe enough reason to abandon that rule so its code can be > > truly and freely shared between GNU projects. > > The libiberty licensing is certainly confused. I just don't want to > make it worse. I think the natural way to sort it out is to move all the FSF-copyright files therein (including include/) to GPLv3, no license exception, except for cp-demangle.c (used in libstdc++-v3) and the headers it includes, which should have the GCC Runtime Library Exception notice. libiberty is a library for a limited number of GNU projects, all under GPLv3; as far as I know the only reason it hasn't been converted to GPLv3 is that noone got around to doing so. (gnulib also uses the practice of putting GPLv3 license notices on the files even if they are also available under other licenses, with separate metadata indicating other licenses under which files are available.) That wouldn't sort out the question of what "This file is part of" notices should be present, but would deal with the other license confusion. (Ideally I think most of libiberty would be replaced by use of gnulib in the projects using libiberty - I see no real advantage to the GNU Project in having those two separate libraries for substantially the same purposes - but that's a much larger and harder task, which would also involve, for each libiberty file replaced by a gnulib version, ascertaining whether there are any features or local changes in the libiberty version that should be merged into the gnulib version or any common upstream such as glibc. And some files in libiberty would probably need adding to gnulib as part of such a project.) -- Joseph S. Myers joseph@codesourcery.com

**References**:[Assembly output optimisations (was: PR 51094 - fprint_w() in output_addr_const() reinstated)](http://gcc.gnu.org/msg00329.html)*From:*Dimitrios Apostolou

[add strnlen to libiberty (was Re: Assembly output optimisations)](http://gcc.gnu.org/msg00333.html)*From:*Dimitrios Apostolou

[Re: add strnlen to libiberty (was Re: Assembly output optimisations)](http://gcc.gnu.org/msg00335.html)*From:*Ian Lance Taylor

[Re: add strnlen to libiberty (was Re: Assembly output optimisations)](http://gcc.gnu.org/msg00336.html)*From:*Dimitrios Apostolou

[Re: add strnlen to libiberty (was Re: Assembly output optimisations)](http://gcc.gnu.org/msg00339.html)*From:*Ian Lance Taylor

[Re: add strnlen to libiberty (was Re: Assembly output optimisations)](http://gcc.gnu.org/msg00344.html)*From:*Hans-Peter Nilsson

[Re: add strnlen to libiberty (was Re: Assembly output optimisations)](http://gcc.gnu.org/msg00357.html)*From:*Ian Lance Taylor



| Index Nav: |
[
|
|---|
