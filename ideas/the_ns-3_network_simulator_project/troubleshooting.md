# Troubleshooting

**Parent:** The ns-3 Network Simulator Project — Project Ideas
**Source:** https://www.nsnam.org/wiki/Troubleshooting
**Scraped:** 2026-02-22T23:28:47.553720

---

# Troubleshooting

[Jump to navigation](https://www.nsnam.org#mw-head)

[Jump to search](https://www.nsnam.org#searchInput)

[Main Page](https://www.nsnam.org/wiki/Main_Page) - [Roadmap](https://www.nsnam.org/wiki/Roadmap) - [Summer Projects](https://www.nsnam.org/wiki/Summer_Projects) - [Project Ideas](https://www.nsnam.org/wiki/Project_Ideas) - [Developer FAQ](https://www.nsnam.org/wiki/Developer_FAQ) - [Tools](https://www.nsnam.org/wiki/Tools) - [Related Projects](https://www.nsnam.org/wiki/Related_Projects)

[HOWTOs](https://www.nsnam.org/wiki/HOWTOs) - [Installation](https://www.nsnam.org/wiki/Installation) - [Troubleshooting] - [User FAQ](https://www.nsnam.org/wiki/User_FAQ) - [Samples](https://www.nsnam.org/wiki/Category:Samples) - [Models](https://www.nsnam.org/wiki/Category:Models) - [Education](https://www.nsnam.org/wiki/Education) - [Contributed Code](https://www.nsnam.org/wiki/Contributed_Code) - [Papers](https://www.nsnam.org/wiki/Papers)

This is a wiki; if you find items not adequately covered below, please consider adding an entry.

In general, before consulting this page (much of the information is old), please see the [Errata](https://www.nsnam.org/wiki/Errata) page for notes on recent ns-3 releases.

## download.py

### pybindgen download fails

If after running download.py, you get:

bzr: ERROR: Invalid http response for[https://launchpad.net/pybindgen/.bzr/branch-format/.bzr/branch-format]: Unable to handle http code 400: Bad Request

Check the status of the file ~/.bzr.log You may see:

0.050 failed to import pycurl: No module named pycurl

If so, install the python-curl package and try again.

Make sure that your environment variable https_proxy is set if you are behind a web proxy.

## ns-allinone-3.26 build issues

f you have installed Anaconda on a Mac, you may encounter a build problem such as:

"../src/wifi/model/wifi-phy.cc:65:46: error: no matching constructor for initialization of 'WifiPhy::ChannelToFrequencyWidthMap' (aka 'map<pair<unsigned short, ns3::WifiPhyStandard>, pair<unsigned int, unsigned int> >') WifiPhy::ChannelToFrequencyWidthMap WifiPhy::m_channelToFrequencyWidth = ^ /usr/include/c++/4.2.1/bits/stl_map.h:188:9: note: candidate constructor template not viable: requires 2 arguments, but 79 were provided map(_InputIterator __first, _InputIterator __last) ^

This can be worked around by configuring Waf to use the system Python instead of the Python version provided by Anaconda. At the Waf configuration stage, try:

./waf --python=/usr/bin/python configure ...

When using build.py, the argument can be passed as follows:

./build.py --enable-examples --enable-tests -- --python=/usr/bin/python

See: [issue 2778](https://www.nsnam.org/bugzilla/show_bug.cgi?id=2778) in the ns-3 tracker for more information.

## ns-allinone-3.5 build issues

### gcc-4.4 issues

For Fedora Core 11 and other systems that use gcc-4.4, you may encounter this type of compilation error:

[614/702] cxx: build/debug/bindings/python/ns3_module_csma.cc -> build/debug/bindings/python/ns3_module_csma_3.o In file included from /usr/include/python2.6/pyconfig.h:6, from /usr/include/python2.6/Python.h:8, from debug/bindings/python/ns3module.h:3, from ../bindings/python/ns3module_helpers.cc:2: /usr/include/python2.6/pyconfig-64.h:1022:1: error: "_POSIX_C_SOURCE" redefined

and

gcc " " - f P I C " " " " - D _ _ A S S E M B L 1 Y _ _ - f P I C " " -Ilinux-2.6.18/include -Ilinux-2.6.18/include/asm/mach-default -Isim -Ilinux-2.6.18/nsc -Ilinux-2.6.18/override -c -o linux-2.6.18/arch/x86_64/lib/csum-copy.o linux-2.6.18/arch/x86_64/lib/csum-copy.S gcc: : No such file or directory gcc: f: No such file or directory gcc: P: No such file or directory gcc: I: No such file or directory gcc: C: No such file or directory gcc: : No such file or directory gcc: : No such file or directory ...

The first error requires this patch to ns-3.5:
[http://code.nsnam.org/ns-3-dev/rev/e33a677e8864](http://code.nsnam.org/ns-3-dev/rev/e33a677e8864)

The second error is an error in Network Simulation Cradle and requires patching nsc-0.5.0 with the nsc.patch attached to this message: [http://mailman.isi.edu/pipermail/ns-developers/2009-September/006522.html](http://mailman.isi.edu/pipermail/ns-developers/2009-September/006522.html)

## ns-allinone-3.4 build issues

### Scons NSC error

**Note:** This issue should not appear in ns-allinone-3.5 or later.

# Build NSC Entering directory `nsc-0.5.0' => python scons.py linux-2.6.18 scons: Reading SConscript files ... Checking target architecure...(cached) x86 AttributeError: SConsEnvironment instance has no attribute 'CFile':

or

# Build NSC Entering directory `nsc-0.5.0' => python scons.py linux-2.6.18 scons: Reading SConscript files ... Checking target architecure...(cached) x86 scons: done reading SConscript files. scons: Building targets ... scons: *** While building `['globaliser/lexer.lex.cc']' from ` ['globaliser/lexer.l']': Don't know how to build from a source file with suffix `.l'. Expected a suffix in this list: ['.i']. scons: building terminated because of errors.

This indicates that you probably don't have flex and bison installed on your system (for compiling NSC). On Ubuntu/Debian systems, you can try:

sudo apt-get install flex bison

For other systems, consult your package repositories, or install the packages from source. You may optionally edit the .config file of ns-allinone-3.4 to remove the nsc line, since nsc is an optional component:

<?xml version="1.0" ?><config> <ns-3 branch="ns-3.4" dir="ns-3.4"/> <ns-3-traces branch="ns-3.4-ref-traces" dir="ns-3.4-ref-traces"/> <pybindgen dir="pybindgen-0.10.0.630" version="0.10.0.630"/> </config>

## Platform-specific issues

### CentOS 5/RHEL 5

CentOS 5 (or Red Hat Enterprise Linux 5) cannot successfully build Python bindings; the build errors out with messages such as:

[ 886/1013] cxx: bindings/python/ns3module_helpers.cc -> build/debug/bindings/python/ns3module_helpers_3.o cc1plus: warnings being treated as errors debug/ns3/ptr.h: In instantiation of ‘ns3::Ptr<const ns3::AttributeAccessor>’: debug/ns3/attribute-accessor-helper.h:98: instantiated from here debug/ns3/ptr.h:69: warning: lowering visibility of ‘U* ns3::GetPointer(const ns3::Ptr<>&) [with U = U, T = const ns3::AttributeAccessor]’ to match its type debug/ns3/ptr.h:71: warning: lowering visibility of ‘U* ns3::PeekPointer(const ns3::Ptr<>&) [with U = U, T = const ns3::AttributeAccessor]’ to match its type ... Build failed -> task failed (err #1): {task: cxx ns3module.cc -> ns3module_3.o} -> task failed (err #1): {task: cxx ns3module_helpers.cc -> ns3module_helpers_3.o} -> task failed (err #1): {task: cxx ns3_module_flame.cc -> ns3_module_flame_3.o} -> task failed (err #1): {task: cxx ns3_module_list_routing.cc -> ns3_module_list_routing_3.o}

This is a compiler problem with gcc-4.1.2 variant that is shipped on these platforms. One solution is to disable python (if you do not need the bindings) at configure time with:

./waf configure --disable-python

On CentOS 5.4 at least, this can be fixed by moving to gcc-4.4, which is distributed as a package "gcc44".

sudo yum install gcc44 gcc44-c++

Then, set your CXX environment variable as follows:

export CXX=g++44 ./waf configure && ./waf

### SELinux (First reported on Fedora Core 10)

**cannot restore segment prot after reloc: Permission denied**

If you see a message such as this when executing an ns-3 script, you have crossed swords with SELinux. You have several alternatives to move forward. The first is to change the library file security context. If, for example, the OS complains about your liblinux2.6.26.so library, you can:

cd ns-3-allinone/nsc/linux2.6.26 chcon -t texrel_shlib_t liblinux2.6.26.so

If you feel confident about about security and are okay with it, you can temporarily disable SELinux by

/usr/sbin/setenforce 0

If you don't care about security at all you can permanently disable SELinux by

changing "enforcing" to "disabled" in /etc/selinux/config and rebooting.

This issue was addressed in the Linux kernel, and has been verified as not happening in Fedora Core 11

### SELinux (First reported on Fedora Core 12)

**liblinux2.6.26.so: cannot enable executable stack as shared object requires: Permission denied**

This is another variation on the previous selinux issue. The NSC liblinux* libraries are requesting an executable stack. See this with:

fedora-core-12> execstack -q ./nsc/linux-2.6.18/liblinux2.6.18.so X ./nsc/linux-2.6.18/liblinux2.6.18.so

Workaround: Turn this off and verify with:

nsnam@ns-fedora-core-12> execstack -c ./nsc/linux-2.6.18/liblinux2.6.18.so nsnam@ns-fedora-core-12< execstack -q ./nsc/linux-2.6.18/liblinux2.6.18.so - ./nsc/linux-2.6.18/liblinux2.6.18.so

Do the same for liblinux-2.6.26 or any other libs you are interested in.

### Cygwin

**Linking fails**

As of ns-3.10, Cygwin (version 1.7.7-1) fails at the linking stage:

1972 [main] ld 3896 C:\cygwin\bin\ld.exe: *** fatal error - cmalloc would have returned NULL collect2: ld terminated with signal 1 [Hangup] Waf: Leaving directory `/cygdrive/e/temp/ns-allinone-3.10-RC2/ns-3.10-RC2/build' Build failed: -> task failed (err #1):

It is not known whether this problem exists with earlier versions of Cygwin. It has been reported elsewhere; e.g. [here](http://www.mail-archive.com/cygwin@cygwin.com/msg113791.html), and reported on the users mailing list during 2010 timeframe.

**Python bindings**

Python bindings do not build successfully due to a gccxml bug. See the [NS-3_Python_Bindings#Caveats](https://www.nsnam.org/wiki/NS-3_Python_Bindings#Caveats) page.

If you see "resolving vtable" messages while linking such as the below when you compile on Cygwin, you can safely ignore them:

[530/535] cxx_link: build/debug/examples/wifi-wired-bridging_23.o -> build/debug /examples/wifi-wired-bridging.exe Info: resolving vtable for ns3::EmptyAttributeValueby linking to __imp___ZTVN3ns 319EmptyAttributeValueE (auto-import) Info: resolving vtable for ns3::RandomVariableValueby linking to __imp___ZTVN3ns 319RandomVariableValueE (auto-import) Info: resolving vtable for ns3::RectangleValueby linking to __imp___ZTVN3ns314Re ctangleValueE (auto-import) Info: resolving vtable for ns3::TimeValueby linking to __imp___ZTVN3ns39TimeValu eE (auto-import) Info: resolving vtable for ns3::BooleanValueby linking to __imp___ZTVN3ns312Bool eanValueE (auto-import) etc.

**NSC**

The Network Simulation Cradle is not supported under Cygwin. It is advised to use a Unix-based platform instead. Windows users can use a virtual machine to run e.g. Linux. See e.g. [http://www.virtualbox.org/](http://www.virtualbox.org/) for a free virtual machine.

## hg merge and resolve problems

When working with multiple repos, you may encounter a problem when your merge fails, and you get this error:

user@ubuntu-desktop:~/hg/ns-3-allinone/temp/ns-3-lr-wpan$ hg pull[http://code.nsnam.org/ns-3-dev]pulling from[http://code.nsnam.org/ns-3-dev]searching for changes adding changesets adding manifests adding file changes added 444 changesets with 2410 changes to 1241 files (+1 heads) (run 'hg heads' to see heads, 'hg merge' to merge)

user@ubuntu-desktop:~/hg/ns-3-allinone/temp/ns-3-lr-wpan$ hg merge merging doc/models/Makefile merging src/network/helper/trace-helper.h merging src/network/utils/address-utils.cc merging src/network/utils/address-utils.h merging src/network/wscript merging src/wscript warning: conflicts during merge. merging src/wscript failed! 1222 files updated, 5 files merged, 92 files removed, 1 files unresolved use 'hg resolve' to retry unresolved file merges or 'hg update -C .' to abandon

However, it is not clear what do to about this. This [mailing list post](http://www.selenic.com/pipermail/mercurial/2008-December/022795.html) raises some issues about the 'hg resolve' command, which haven't been addressed by Mercurial, and which are summarized below:

In summary:

- Do not use the bare 'hg resolve' command. It will tend to overwrite the changes that you make to fix this problem.
- For each file for which the merge failed, hand edit the file in question (unless you use a built-in merge tool for your environment). Merge failures will be delimited such as follows:

<<<<<<< local all_modules = [] ======= all_modules = ['core'] >>>>>>> other

The above states that in your 'local' copy, you have an 'all_modules' statement which the proposed merged version ('other') has changed, but in such a way that the merge failed. You must edit all of these code snippets to remove the "<<<<<<", "=======", and ">>>>>>" lines and resolve the conflicting code statements by hand.

- When you are done, make sure you mark the files as resolved with the 'hg resolve -m FILE' command, such as:

user@ubuntu-desktop:~/hg/ns-3-allinone/temp/ns-3-lr-wpan$ hg resolve -m src/wscript

- Commit your merge as the final step; e.g.:

user@ubuntu-desktop:~/hg/ns-3-allinone/temp/ns-3-lr-wpan$ hg commit -m"merge with ns-3-dev"

## Click routing build problems

click-2.0 release (July 2011) will not build without [this patch](http://pdos.csail.mit.edu/pipermail/click/attachments/20110725/90c9704d/attachment.patch).

## General build problems

- Q. What is this kind of build error representative of?

assert failed. file=../src/core/type-id.cc, line=389, cond="uid != 0" Command ['/ns-3-dev/build/debug/examples/mixed-wireless'] exited with code -5

- A. The system can't find the specified TypeId. Check spelling, and whether it is prefixed with the namespace "ns3::"
- Q. What is this kind of build error representative of?

collect2: ld terminated with signal 9 [Killed]

- A. There is not enough virtual memory for the linker (ld). This type of error is most typically experienced when linking a static build with every ns-3 module enabled. Try to either reduce the scope of the build (by enabling only the modules that you care about) or increase your machine's swap size or physical memory.

- Q. A required software package is in a non-standard place. How to get waf to find the packages?
- A. To compile with non-standard link path, use the environment variable LINKFLAGS. Example for bash shell:

LINKFLAGS="-L/tmp" ./waf configure

## Valgrind errors

Valgrind can be used with ns-3 as follows:

./test.py -g // runs tests with valgrind ./waf --command-template="valgrind %s" --run <program-name>

or simply by using valgrind within waf shell or with library paths set correctly.

Valgrind sometimes reports errors on certain platforms due to some known issues with STL or with glibc. In particular, these problems have been reported:

- "still-reachable" errors due to use of STL:
[http://valgrind.org/docs/manual/faq.html#faq.reports](http://valgrind.org/docs/manual/faq.html#faq.reports) - glibc-2.10 problems reported on Gentoo Linux:
[https://www.nsnam.org/bugzilla/show_bug.cgi?id=887](https://www.nsnam.org/bugzilla/show_bug.cgi?id=887) - glibc-2.11.1 problems on Ubuntu 10.04 LTS x86_64

The following program can be used on Linux to check your glibc version:

#include <stdio.h> #include <gnu/libc-version.h> int main (void) { puts (gnu_get_libc_version ()); return 0; }

## Run-time errors

- Q. What is this assertion indicating?

assert failed. file=debug/ns3/tags.h, line=105, cond="sizeof (T) <= Tags::SIZE"

- A. The packet tag may be greater than Tags::SIZE (16 bytes)

- Q. Why does valgrind fail with SIGILL on a simulation using NSC?
- A. Valgrind does not work under 64-bit mode when running NSC due to lack of support for all the opcodes used. This has been confirmed to work in 32-bit mode. Check
[this bug report](http://www.nsnam.org/bugzilla/show_bug.cgi?id=356)if you are concerned about a possible valgrind failure with an nsc script and want to see if it is a known issue.

- Q. NSC does not work on a platform with SELinux enabled; for instance

$ ./waf --run tcp-nsc-lfn Entering directory `/hg/ns-3-dev/build' [250/250] build-nsc Compilation finished successfully /hg/ns-3-dev/build/debug/liblinux2.6.26.so: cannot restore segment prot after reloc: Permission denied Command ['/hg/ns-3-dev/build/debug/examples/tcp-nsc-lfn'] exited with code -11

- A. This is logged in the
[tracker](http://www.nsnam.org/bugzilla/show_bug.cgi?id=437). Workaround: to temporarily disable enforcement on a running system, set

/usr/sbin/setenforce 0

To permanently disable enforcement during a system startup
change "enforcing" to "disabled" in */etc/selinux/config* and reboot.

- Q. What happened to my pcap trace files? The files are empty or are missing some packets!
- A. This is usually a symptom of a memory leak; the pcap trace files do not close cleanly. Try running your script with the --valgrind option to see if you've introduced a memory leak.

See the [ python page](https://www.nsnam.org/wiki/NS-3_Python_Bindings)

## Debugging tips

- Q. Is there a way to dereference a Ptr when in gdb?
- A. yes: p *ptr->m_ptr

[Craigdo](https://www.nsnam.org/wiki/User:Craigdo) 22:52, 27 March 2009 (UTC)
