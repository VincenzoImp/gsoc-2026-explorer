# Installation

**Parent:** The ns-3 Network Simulator Project — Project Ideas
**Source:** https://www.nsnam.org/wiki/Installation
**Scraped:** 2026-02-22T23:28:47.553624

---

# Installation

[Jump to navigation](https://www.nsnam.org#mw-head)

[Jump to search](https://www.nsnam.org#searchInput)

[Main Page](https://www.nsnam.org/wiki/Main_Page) - [Roadmap](https://www.nsnam.org/wiki/Roadmap) - [Summer Projects](https://www.nsnam.org/wiki/Summer_Projects) - [Project Ideas](https://www.nsnam.org/wiki/Project_Ideas) - [Developer FAQ](https://www.nsnam.org/wiki/Developer_FAQ) - [Tools](https://www.nsnam.org/wiki/Tools) - [Related Projects](https://www.nsnam.org/wiki/Related_Projects)

[HOWTOs](https://www.nsnam.org/wiki/HOWTOs) - [Installation] - [Troubleshooting](https://www.nsnam.org/wiki/Troubleshooting) - [User FAQ](https://www.nsnam.org/wiki/User_FAQ) - [Samples](https://www.nsnam.org/wiki/Category:Samples) - [Models](https://www.nsnam.org/wiki/Category:Models) - [Education](https://www.nsnam.org/wiki/Education) - [Contributed Code](https://www.nsnam.org/wiki/Contributed_Code) - [Papers](https://www.nsnam.org/wiki/Papers)

**Important Note:** As of March 7, 2023, this information has migrated to a new manual-- the Installation guide linked from the main [documentation page](https://www.nsnam.org/documentation/). You can read the below for historical interest, but it is probably stale information.

This wiki page used to be the installation guide for ns-3.

## Supported platforms

ns-3 is primarily developed on GNU/Linux and macOS platforms, and the minimal requirements to run basic simulations are a C++ compiler; either [g++](https://gcc.gnu.org/) or [clang++](https://clang.llvm.org/) compiler, build system ([CMake](https://cmake.org) and either [make](https://www.gnu.org/software/make/) or [ninja](https://ninja-build.org/)), and [Python (version 3)](http://www-python.org/) interpreter. The below instructions are per-platform instructions for supplemental packages that enable optional features of ns-3 or companion tools.

### Operating system and compiler support

ns-3 is supported and currently tested on the following primary platforms:

- Linux (x86 and x86_64): gcc/g++ versions 8 and above
**Note:**If you are using RHEL or Centos, you will likely need to install a more up-to-date compiler than the default; search for how to enable 'software collections' or 'devtoolset' on these distributions. Other Linux distributions typically have a suitable default compiler (at least version 4.9).

- MacOS Apple LLVM: version 11.0.0 and above
- FreeBSD and Linux (x86_64): clang/LLVM version 8 and later

The minimum Python version supported is currently version 3.6 or greater (major version 3).

By supported, we mean that the project tries to support most or all of the build options on these platforms unless there is a good reason to exclude the option; and at least the debug build will compile. If you intend to do serious work using ns-3, and are forced by circumstances to use a Windows platform, consider virtualization of a popular Linux platform or using [Windows Subsystem for Linux](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide).

Some aspects of ns-3 depend on Unix (or specifically Linux) support, such as the emulation or TapBridge features, and those components are not enabled on the Windows or MacOS versions cited above.

Additional maintainers are invited to make more platforms, compilers and environments supported.

### Integrated development environment support

Please see [this tutorial section](https://www.nsnam.org/docs/tutorial/html/getting-started.html#building-with-ides) on configuring IDEs.

#### Eclipse

The [Eclipse IDE](https://www.eclipse.org/) is not an officially supported platform, but some developers use it and have compiled a [HOWTO](https://www.nsnam.org/wiki/HOWTO_configure_Eclipse_with_ns-3).

#### NetBeans

[NetBeans](https://netbeans.org/) is not officially supported either, but there is a [HOWTO](https://www.nsnam.org/wiki/HOWTO_configure_NetBeans_with_ns-3) as well.

#### QtCreator

Same rule applies to [Qt Creator](http://qt-project.org/wiki/category:tools::qtcreator); it's not officially supported, but there are developers that use it and [HOWTO](https://www.nsnam.org/wiki/HOWTO_configure_QtCreator_with_ns-3) is available.

### Support for optional features

There are a few options that are not enabled by default and are not available on all platforms. At the end of the configuration process (explained below), the status of these options are shown as detected by a **waf** or **ns3** script:

---- Summary of optional NS-3 features: Python Bindings : not enabled (Python library or headers missing) BRITE Integration : not enabled (BRITE not enabled (see option --with-brite)) NS-3 Click Integration : not enabled (nsclick not enabled (see option --with-nsclick)) GtkConfigStore : not enabled (library 'gtk+-2.0 >= 2.12' not found) XmlIo : not enabled (library 'libxml-2.0 >= 2.7' not found) Threading Primitives : enabled Real Time Simulator : enabled Emulated Net Device : not enabled (<netpacket/packet.h> include not detected) Network Simulation Cradle : not enabled (architecture None not supported) MPI Support : not enabled (option --enable-mpi not selected) NS-3 OpenFlow Integration : not enabled (OpenFlow not enabled (see option --with-openflow)) SQlite stats data output : not enabled (library 'sqlite3' not found) Tap Bridge : not enabled (<linux/if_tun.h> include not detected) PyViz visualizer : not enabled (Python Bindings are needed but not enabled) Use sudo to set suid bit : not enabled (option --enable-sudo not selected) Build tests : not enabled (defaults to disabled) Build examples : not enabled (defaults to disabled) GNU Scientific Library (GSL) : not enabled (GSL not found)

Generally if the platform is missing some requirement for an option it is marked as "not enabled." Note that "disabled by user request" will be shown when the user explicitly disables a feature (such as "--disable-python"); and if a feature defaults to disabled this will also be noted (e.g., option --enable-sudo not selected).

The table below is meant to help sort out the different features and on which platforms they are supported. This table reflects the status as of ns-3.15 and may have changed since then:

| Option | Linux | FreeBSD | Mac OS X |
|---|---|---|---|
| Optimized build | Y | Y | Y |
| Python bindings | Y | Y | Y |
| Threading | Y | Y | Y |
| Real-time simulator | Y | Y | Y |
| Emulated Net Device | Y | N | N |
| Tap Bridge | Y | N | N |
| Network simulation cradle | Y1 |
? | N |
| Static builds | Y | Y | Y |

*Key:* **Y** = supported; **N** = not supported; **?** = unknown; **dev** = support in ns-3-dev (next release)

*Notes:*

- NSC works best with gcc-3.4 or gcc-4.2 or greater series. Try to avoid using gcc-4.0 and gcc-4.1 series; some build problems have been found with these versions of compilers.

### Using older version of ns-3 on newer systems

It can be the case that trying to use an old version of ns-3 on a newer system can lead to warnings or errors because the compilers have become more strict over time. The below wiki page has some suggestions to work around this.

[https://www.nsnam.org/wiki/HOWTO_build_old_versions_of_ns-3_on_newer_compilers](https://www.nsnam.org/wiki/HOWTO_build_old_versions_of_ns-3_on_newer_compilers)

### Using newer version of ns-3 on older systems

Conversely, it can be the case that a user has an old version of Linux but newer compilers and libraries are needed to run the latest versions of ns-3. This blog has some recommendations on how to use chroot jails to work around this:

## Prerequisites

The core of ns-3 requires a gcc/g++ installation of 4.9 or greater (Linux), or a recent version of clang compiler (OS X, Linux, or BSD), and Python 3.5 or greater. As mentioned above, different options require additional support. This is a list of packages (for Debian/Ubuntu systems) that are needed to support different ns-3 options. Note that other distributions (e.g., Fedora, FreeBSD) may have different package names or capitalization (e.g. ImageMagik). Installation should be similar for Red Hat/Fedora based systems, with "yum" replacing "apt-get", but some differences exist, so below is a guide for both Ubuntu (should generally apply to Debian) and Fedora/RedHat-based systems:

### Linux

#### Ubuntu/Debian/Mint

The following list of packages should be accurate through the Ubuntu 22.10 release; other releases or other Debian-based systems may slightly vary. Ubuntu 16.04 LTS release is probably the oldest release that is known to work with the most recent ns-3 releases.

The list of packages depends on which version of ns-3 you are trying to build.

**minimal requirements for release 3.36 and later:**

apt install g++ python3 cmake ninja-build git

Git is not required if you are only downloading a source archive.

Ubuntu comes with 'make' build tool, but if you are missing it (possibly on some other Debian-based distribution), you may want to install make or ninja-build. ninja is an alternative to make.

**recommended also for release 3.37 and later:**

Ccache is a compiler cache optimization that will speed up builds across multiple ns-3 directories, at the cost of up to an extra 5 GB of disk space used in the cache.

apt install ccache

Note: For Ubuntu 20.04 release and earlier, the version of ccache provided by apt (3.7.7 or earlier) may not provide performance benefits, and users are recommended to install version 4 or later, possibly as a source install. For Ubuntu 22.04 and later, ccache can be installed using apt.

**minimal recommended requirements for release 3.30-3.35:**

apt install g++ python3

**minimal recommended requirements for release 3.29 and earlier:**

apt install g++ python2

**Note:** As of ns-3.30 release (August 2019), ns-3 uses Python 3 by default, but earlier releases depend on Python 2 packages, and at least a Python 2 interpreter is recommended. If working with an earlier release, one may in general substitute 'python' for 'python3' in the below (e.g. install 'python-dev' instead of 'python3-dev').

**Note:** As of January 2022 (ns-3.36 release and ns-3-dev), the minimum g++ version is g++-8. Older Ubuntu releases (18.04, 16.04) come with an older default g++. On Ubuntu 18.04, this StackOverflow answer can be followed to install and prefer g++-8: [https://askubuntu.com/a/1028656](https://askubuntu.com/a/1028656). On older Ubuntu such as 16.04, to use the most recent code, you must install g++-8 or g++-9 from the Ubuntu toolchain: [https://launchpad.net/%7Eubuntu-toolchain-r/+archive/ubuntu/test](https://launchpad.net/%7Eubuntu-toolchain-r/+archive/ubuntu/test)

The remaining are needed for **optional** ns-3 components.

**minimal requirements for Python visualizer and bindings (ns-3.37 and newer):**cppyy Python module and Pyviz dependencies

python3 -m pip install --user cppyy apt install gir1.2-goocanvas-2.0 python3-gi python3-gi-cairo python3-pygraphviz gir1.2-gtk-3.0 ipython3

**minimal requirements for Python API users (release 3.30 to ns-3.36):**This is the minimal set of packages needed to work with Python bindings from a released tarball.

apt install g++ python3 python3-dev pkg-config sqlite3 cmake

**additional minimal requirements for Python (development):**For use of ns-3-allinone repository (cloned from Git), additional packages are needed to fetch and successfully install pybindgen and netanim.

apt install python3-setuptools git

**Netanim animator:**qt5 development tools are needed for Netanim animator; qt4 will also work but we have migrated to qt5. qt6 compatibility is not tested.

apt install qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools

**Note:** For Ubuntu 20.10 and earlier, the single 'qt5-default' package suffices

apt install qt5-default

- Support for ns-3-pyviz visualizer (release 3.36 and earlier)

- For Ubuntu 18.04 and later, python-pygoocanvas is no longer provided. The ns-3.29 release and later upgrades the support to GTK+ version 3, and requires these packages:


apt install gir1.2-goocanvas-2.0 python3-gi python3-gi-cairo python3-pygraphviz gir1.2-gtk-3.0 ipython3

- For ns-3.28 and earlier releases, PyViz is based on GTK+ 2, GooCanvas, and GraphViz:


apt install python-pygraphviz python-kiwi python-pygoocanvas libgoocanvas-dev ipython

- Support for MPI-based distributed emulation

apt install openmpi-bin openmpi-common openmpi-doc libopenmpi-dev

- Support for bake build tool:

apt install mercurial unzip

- Debugging:

apt install gdb valgrind

- Support for utils/check-style-clang-format.py code style check program (since ns-3.37):

apt install clang-format

Note: clang-format-14 through clang-format-16 version is required.

- Doxygen and related inline documentation:

apt install doxygen graphviz imagemagick apt install texlive texlive-extra-utils texlive-latex-extra texlive-font-utils dvipng latexmk

- If you get an error such as 'convert ... not authorized source-temp/figures/lena-dual-stripe.eps', see this post about editing ImageMagick's security policy configuration:
[https://cromwell-intl.com/open-source/pdf-not-authorized.html](https://cromwell-intl.com/open-source/pdf-not-authorized.html). In brief, you will want to make this kind of change to ImageMagick security policy:

- If you get an error such as 'convert ... not authorized source-temp/figures/lena-dual-stripe.eps', see this post about editing ImageMagick's security policy configuration:

--- ImageMagick-6/policy.xml.bak 2020-04-28 21:10:08.564613444 -0700 +++ ImageMagick-6/policy.xml 2020-04-28 21:10:29.413438798 -0700 @@ -87,10 +87,10 @@ <policy domain="path" rights="none" pattern="@*"/> - <policy domain="coder" rights="none" pattern="PS" /> + <policy domain="coder" rights="read|write" pattern="PS" /> <policy domain="coder" rights="none" pattern="PS2" /> <policy domain="coder" rights="none" pattern="PS3" /> <policy domain="coder" rights="none" pattern="EPS" /> - <policy domain="coder" rights="none" pattern="PDF" /> + <policy domain="coder" rights="read|write" pattern="PDF" /> <policy domain="coder" rights="none" pattern="XPS" /> </policymap>



- The ns-3 manual and tutorial are written in reStructuredText for Sphinx (doc/tutorial, doc/manual, doc/models), and figures typically in dia (also needs the texlive packages above):

apt install python3-sphinx dia

**Note:** Sphinx version >= 1.12 required for ns-3.15. To check your version, type "sphinx-build". To fetch this package alone, outside of the Ubuntu package system, try "sudo easy_install -U Sphinx".

- GNU Scientific Library (GSL) support for more accurate 802.11b WiFi error models (not needed for OFDM):

apt install gsl-bin libgsl-dev libgslcblas0

If the above doesn't work (doesn't detect GSL on the system), consult: [https://coral.ise.lehigh.edu/jild13/2016/07/11/hello/](https://coral.ise.lehigh.edu/jild13/2016/07/11/hello/). But don't worry if you are not using 802.11b models.

- To read pcap packet traces

apt install tcpdump

- Database support for statistics framework

apt install sqlite sqlite3 libsqlite3-dev

- Xml-based version of the config store (requires libxml2 >= version 2.7)

apt install libxml2 libxml2-dev

- Support for generating modified python bindings (ns-3.36 and earlier):

apt install cmake libc6-dev libc6-dev-i386 libclang-dev llvm-dev automake python3-pip python3 -m pip install --user cxxfilt

and you will want to install castxml and pygccxml as per the instructions for python bindings (or through the *bake* build tool as described in the tutorial). The 'castxml' and 'pygccxml' packages provided by Ubuntu 18.04 and earlier are not recommended; a source build (coordinated via bake) is recommended. If you plan to work with bindings or rescan them for any ns-3 C++ changes you might make, please read the [chapter in the manual](https://www.nsnam.org/docs/manual/html/python.html) on this topic.

**Note:** Ubuntu versions (through 19.04) and systems based on it (e.g. Linux Mint 18) default to an old version of clang and llvm (3.8), when simply 'libclang-dev' and 'llvm-dev' are specified. The packaging on these 3.8 versions is broken. Users of Ubuntu will want to explicitly install a newer version by specifying 'libclang-6.0-dev' and 'llvm-6.0-dev'. Other versions newer than 6.0 may work (not tested).

- A GTK-based configuration system

apt install libgtk-3-dev

- To experiment with virtual machines and ns-3

apt install vtun lxc uml-utilities

- Support for openflow module (requires libxml2-dev if not installed above) and Boost development libraries

apt install libxml2 libxml2-dev libboost-all-dev

#### Fedora/RedHat

Note: This has not been updated for ns-3.37 release yet.

The following list of packages should be aligned with recent Fedora releases; other releases may slightly vary. Note that these distributions sometimes change the package structure over time.

**Important**: If you are using RedHat or CentOS, either versions 6 or 7, the default compilers are too old to build recent ns-3 releases. You must upgrade gcc and g++ to a more recent version. See below.

__Fedora and virtual machines__

The Waf build system can use several GB of space on /tmp when building ns-3. Fedora and RedHat have chosen to mount /tmp on tmpfs, sized at half of the RAM by default. On a virtual machine, where possibly as little as 4GB of RAM may be configured, this will lead to a 2GB /tmp partition and the ns-3 build will fail with a message such as:

src/internet/bindings/ns3module.cc:148895:1: fatal error: error writing to /tmp/ccvdnttM.s: No space left on device

One workaround is to increase your tmpfs size, such as (as root user):

# mount -o remount,size=4G,noatime /tmp/

This resizing must be done upon each reboot, and you should ensure that you have a swap partition also configured.

__Release-specific issues__

- We do not support RHEL 6 or CentOS 6 anymore; nor do we support older versions of Fedora such as less than Fedora 30.

- RHEL 7 (and CentOS 7) use an older version of gcc (4.8.5) that is no longer compatible with ns-3 releases. An upgrade of gcc is needed; see these instructions on installing a devtoolset (such as devtoolset-7) if you need to upgrade:
[http://blog.stevedoria.net/20180214/how-to-install-gcc-7-on-centos-7](http://blog.stevedoria.net/20180214/how-to-install-gcc-7-on-centos-7)

__Required and optional packages__

**minimal requirements for C++ (release):**This is the minimal set of packages needed to run most of ns-3's C++ programs from a released tarball.

dnf install gcc-c++ python3

**minimal requirements for Python (release):**This is the minimal set of packages needed to use Python bindings from a released tarball.

dnf install gcc-c++ python3 python3-devel

- Git is needed to work with ns-3 development repositories.

dnf install git

- An optional but recommended package (for improving some wireless model fidelity) is GNU scientific library:

dnf install gsl gsl-devel

- Support for netanim animator:

dnf install qt5-devel

- A GTK-based configuration system

__Prior to ns-3.29, use GTK+ version 2:__

dnf install gtk2 gtk2-devel

__Starting with ns-3.29, use GTK+ version 3:__

dnf install gtk3 gtk3-devel

- Debugging:

dnf install gdb valgrind

- Doxygen and related inline documentation:

dnf install doxygen graphviz ImageMagick

- The ns-3 manual and tutorial are written in reStructuredText for Sphinx (doc/tutorial, doc/manual, doc/models), and figures typically in dia:

dnf install python3-sphinx dia texlive texlive-latex texlive-fncychap texlive-capt-of texlive-tabulary texlive-eqparbox dnf install texlive-epstopdf texlive-titlesec texlive-framed texlive-dvipng texlive-threeparttable texlive-wrapfig texlive-tabulary dnf install texlive-multirow ImageMagick

- To read pcap packet traces

dnf install tcpdump

- Database support for statistics framework

dnf install sqlite sqlite-devel

- Xml-based version of the config store (requires libxml2 >= version 2.7)

dnf install libxml2 libxml2-devel

- Support for utils/check-style.py style check program

dnf install uncrustify

- Support for MPI distributed simulations

dnf install openmpi openmpi-devel environment-modules

Steve Smith notes that the shell must be restarted after environment-modules package is installed, since environment-modules modifies the bash initialization scripts to enable the module command. Then, to find the programs mpic++ and mpiexec, one must do:

$ module load mpi/openmpi-x86_64

and then the commands should be found by the shell:

$ which mpic++ mpiexec

Steve Smith also noted problems with Fedora machines that do not have APX support, such as virtual machines: [https://gitlab.com/nsnam/ns-3-dev/-/issues/397](https://gitlab.com/nsnam/ns-3-dev/-/issues/397)

Solution for those machines is to switch to mpich:

$ dnf install mpich mpich-devel environment-modules $ module load mpi/mpich-x86_64

- Support for openflowswitch requires libxml2, if not installed above, and Boost development libraries

dnf install libxml2 libxml2-devel boost-devel

- Support for ns-3-pyviz visualizer (ns-3.28 release and earlier)

dnf install redhat-rpm-config goocanvas-devel graphviz graphviz-devel python-setuptools python-kiwi pygoocanvas ipython easy_install pygraphviz

- Support for ns-3 pyviz visualizer (ns-3.29 release and later)

pygobject3-devel python3-gobject gobject-introspection-devel goocanvas2-devel graphviz-devel graphviz ipython easy_install pygraphviz

- Support for generating modified python bindings

dnf install cmake clang-devel llvm-devel llvm-static pip3 install --user cxxfilt

and you will want to install castxml and pygccxml as per the instructions for python bindings (or through the *bake* build tool as described in the tutorial). If you plan to work with bindings or rescan them for any ns-3 C++ changes you might make, please read the [chapter in the manual](https://www.nsnam.org/docs/manual/html/python.html) on this topic.

- Support for bake tool:

dnf install make patch autoconf cvs

### macOS

macOS installation of ns-3 relies on the Xcode command line tools provided by Apple, and the clang/llvm compiler used therein. A third-party package manager such as [Homebrew](https://brew.sh) can be used for optional extensions to ns-3 such as libxml2.

The current version of macOS is 'Catalina' (10.15) and the version of Xcode is 11.2, as of this writing.

If you are having problems with ns-3.29 and macOS, please look at the [Errata](https://www.nsnam.org/wiki/Errata) page for some hints, or consider to use the development version (ns-3-dev) of ns-3 which should work now. ns-3.30 is not know to have macOS issues.

The main steps to follow to prepare your macOS machine for a base ns-3 install (Xcode tools, and Python) are as follows:

- Download and install Xcode Command Line Tools (most recently tested version 11.2) from the App Store, or the full Xcode.
- If you installed full Xcode, you still need to type `xcode-select --install` to obtain the command line tools.
- You will also have to agree to Apple's license agreement to proceed; type 'sudo clang -v' in a terminal window to take this step.


At this point, you will likely be able to compile the main C++ libraries. The current macOS Catalina release ships with a basic Python 3 interpreter (version 3.7.3) which is enough to run the Waf build system but not much else. To use Python bindings or other Python features, a fuller install of Python is recommended. Visit [https://www.python.org/downloads/mac-osx/](https://www.python.org/downloads/mac-osx/) to download a Python 3 release (recommended), or else, if you prefer, use Homebrew or some other package manager to install a Python development environment.

At this point, you should be able to use ns-3 in C++ or Python programs. The following options are available to add some additional libraries for more ns-3 features. In general, a third-party installer like Homebrew or MacPorts is needed:

**Recommended for Mojave users**(for better Homebrew compatibility), install the legacy headers package found at: /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg. We are not sure whether this is available for Catalina (10.15).- If you wish to use the NetAnim animator, you must install Qt5 (although Qt4 version also works with current releases).
- If you wish to use mercurial, you must install it. Follow the instruction in the
[mercurial web site](http://mercurial.selenic.com).[MacPorts](https://www.macports.org/)and[Homebrew](http://brew.sh/)are possible package managers to accomplish this. - If you wish to use the GTK-based ConfigStore GUI, we recommend homebrew: if you install Gtk+3 using homebrew, you must install gtk+3. You must install also "adwaita-icon-theme" (not installed by default), or you'll miss elements in the Gtk views

.
**Note to Anaconda users:** If you have installed Anaconda, you may encounter a build problem such as:

"../src/wifi/model/wifi-phy.cc:65:46: error: no matching constructor for initialization of 'WifiPhy::ChannelToFrequencyWidthMap' (aka 'map<pair<unsigned short, ns3::WifiPhyStandard>, pair<unsigned int, unsigned int> >') WifiPhy::ChannelToFrequencyWidthMap WifiPhy::m_channelToFrequencyWidth = ^ /usr/include/c++/4.2.1/bits/stl_map.h:188:9: note: candidate constructor template not viable: requires 2 arguments, but 79 were provided map(_InputIterator __first, _InputIterator __last) ^

This can be worked around by configuring Waf to use the system Python instead of the Python version provided by Anaconda. At the Waf configuration stage, try:

./waf --python=/usr/bin/python configure ...

When using build.py, the argument can be passed as follows:

./build.py --enable-examples --enable-tests -- --python=/usr/bin/python

See: [issue 2778](https://www.nsnam.org/bugzilla/show_bug.cgi?id=2778) in the ns-3 tracker for more information.

### Windows

For Windows 10, there are two main options. Both involve using a Linux environment from within Windows. ns-3 is not compatible with the Windows Visual Studio compiler and IDE (there have been a few efforts to add Visual Studio support, but they have been abandoned).

- . Install a Linux virtual machine (e.g. using Hyper-V, VMware, etc.).
- . Windows offers a
[Windows subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10), providing an Ubuntu-like environment. From within this environment, one can follow the Ubuntu installation guide and obtain most ns-3 features.

Below is some other older (possibly out-of-date) information regarding Windows:

- We provide HOWTO documents describing the process for installing Linux and getting ns-3 running using two popular virtualization products: VirtualBox (
[HOWTO use VirtualBox to run simulations on Windows machines](https://www.nsnam.org/wiki/HOWTO_use_VirtualBox_to_run_simulations_on_Windows_machines)) and VMware ([HOWTO use VMware to set up virtual networks (Windows)](https://www.nsnam.org/wiki/HOWTO_use_VMware_to_set_up_virtual_networks_(Windows))). - There is an experimental project,
[Ns3 on Windows](https://www.nsnam.org/wiki/Ns-3_on_Visual_Studio_2012), using Visual Studio 2012.

## Installation

### Installation with Bake

Bake is a new tool for installing, building and finding out the missing requirements for ns-3 in your own environment.

To use Bake you need to have at least Python (2.7 or above) and Git in your machine (see the section Prerequisites above to see how to install these).

First you need to download Bake using Git, go to where you want Bake to be installed and call

git clone[https://gitlab.com/nsnam/bake]

It is advisable to add bake to your path.

export BAKE_HOME=`pwd`/bake export PATH=$PATH:$BAKE_HOME export PYTHONPATH=$PYTHONPATH:$BAKE_HOME

After that you can use Bake to find the missing packages, download build and install ns-3 and its modules.

To find out what is missing in your system and may be needed for installing ns-3 you can call bake check:

bake.py check

You should have seen something like:

> Python - OK

> GNU C++ compiler - OK

> Mercurial - OK

> CVS - OK

> GIT - OK

> Bazaar - OK

> Tar tool - OK

> Unzip tool - OK

> Unrar tool - OK

> 7z data compression utility - OK

> XZ data compression utility - OK

> Make - OK

> cMake - OK

> patch tool - OK

> autoreconf tool - OK

> Path searched for tools: /usr/lib64/qt-3.3/bin

/usr/lib64/ccache /usr/local/bin /usr/bin/bin/usr/local/sbin /usr/sbin

/sbin /user/dcamara/home/scripts/user/dcamara/home/INRIA/Programs/bin

/user/dcamara/home/INRIA/repos/llvm/build/Debug+Asserts/bin


Before downloading and building ns-3 you need to configure bake to inform it which are the modules you want added to ns-3, the standard distribution for example.

bake.py configure -e ns-3.29

Then to see the modules it has added, and the specific system requirements for this configuration, you can call bake show:



bake.py show


To download the modules, build and install you can call bake deploy



bake.py deploy

This will download the selected modules, all their dependencies and build ns-3 with all these independent modules. You can also perform this installation step by step, i.e. by calling download and build in different steps.



bake.py download bake.py build

### Manual installation

The ns-3 code is available in Mercurial repositories on the server [http://code.nsnam.org](http://code.nsnam.org) (look for the latest release e.g., "ns-3.26"). You can download a tarball of the latest release at [http://www.nsnam.org/releases](http://www.nsnam.org/releases) or you can work with our repositories using Mercurial. We recommend using Mercurial unless there's a good reason not to (See the end of this section for instructions on how to get a tarball release).

The simplest way to get started using Mercurial repositories is to use the **ns-3-allinone** environment. This is a set of scripts that manages the downloading and building of various subystems of ns-3 for you. We recommend that you begin your ns-3 adventures in this environment as it can really simplify your life at this point.

#### Downloading ns-3 Using Git

One practice is to create a directory called **repos** in one's home directory under which one can keep local Git repositories. If you adopt that approach, you can get a copy of ns-3-allinone by typing the following into your Linux shell (assuming you have installed Git):

cd mkdir repos cd repos git clone[https://gitlab.com/nsnam/ns-3-allinone.git]

As the git command executes, you should see something like the following displayed,

Cloning into 'ns-3-allinone'... remote: Enumerating objects: 232, done. remote: Counting objects: 100% (232/232), done. remote: Compressing objects: 100% (121/121), done. remote: Total 232 (delta 135), reused 197 (delta 108) Receiving objects: 100% (232/232), 99.76 KiB | 513.00 KiB/s, done. Resolving deltas: 100% (135/135), done.

After the clone command completes, you should have a directory called ns-3-allinone under your ~/repos directory, the contents of which should look something like the following:

build.py* constants.py dist.py* download.py* README util.py

Notice that you really just downloaded some Python scripts and not yet the C++ code. The next step will be to use those scripts to download and build the ns-3 distribution of your choice.

If you go to the following link: [https://gitlab.com/nsnam/](https://gitlab.com/nsnam/) you will see a number of repositories. Many are the private repositories of the ns-3 development team. The repositories of interest to you will be prefixed with **ns-3**. Official releases of ns-3 will be numbered as ns-3.release.hotfix. For example, a second hotfix to a still hypothetical release nine of ns-3 would be numbered as ns-3.9.2 on this page.

The current development snapshot (unreleased) of ns-3 may be found at [https://gitlab.com/nsnam/ns-3-dev/](https://gitlab.com/nsnam/ns-3-dev/). The developers attempt to keep these repository in consistent, working states but they are in a development area with unreleased code present, so you may want to consider staying with an official release if you do not need newly-introduced features.

You can find the latest version of the code either by inspection of the repository list or by going to the *Getting Started* web page and looking for the latest release identifier.

To download the most recent release (assuming it is ns-3.30 in this case), type the following into your shell (remember you can substitute the name of your chosen release number, or omit specifying it to download the tip of ns-3-dev)

./download.py -n ns-3.30

After download process completes, you should have several new directories under ~/repos/ns-3-allinone:

bake constants.py download.py ns-3.30 __pycache__ util.py build.py dist.py netanim pybindgen README


Go ahead and change into ns-3.30 under your ~/repos/ns-3-allinone directory. You should see something like the following there:

AUTHORS CONTRIBUTING.md Makefile src utils.py waf-tools bindings doc README.md test.py VERSION wscript CHANGES.html examples RELEASE_NOTES testpy.supp waf wutils.py contrib LICENSE scratch utils waf.bat

You are now ready to build the ns-3 distribution.

#### Downloading ns-3 Using a Tarball

The process for downloading ns-3 via tarball is simpler than the Mercurial process since all of the pieces are pre-packaged for you. You just have to pick a release, download it and decompress it.

As mentioned above, one practice is to create a directory called **repos** in one's home directory under which one can keep local Mercurial repositories. One could also keep a tarballs directory. If you adopt the tarballs directory approach, you can get a copy of a release by typing the following into your Linux shell (substitute the appropriate version numbers, of course):

cd mkdir tarballs cd tarballs wget[http://www.nsnam.org/release/ns-allinone-3.30.tar.bz2]tar xjf ns-allinone-3.30.tar.bz2

If you change into the directory **ns-allinone-3.30** you should see a number of files:

bake constants.py ns-3.30 README build.py netanim-3.108 pybindgen-0.20.0 util.py

You are now ready to build the ns-3 distribution.

## Building ns-3 with build.py

The first time you build the ns-3 project you should build using the allinone environment. This will get the project configured for you in the most commonly useful way.

Change into the directory you created in the download section above. If you downloaded using Mercurial you should have a directory called ns-3-allinone under your ~/repos directory. If you downloaded using a tarball you should have a directory called something like ns-allinone-3.13 under your ~/tarballs directory. Type the following:

./build.py

You will see lots of typical compiler output messages displayed as the build script builds the various pieces you downloaded. Eventually you should see the following magic words:

Build finished successfully (00:02:37) Leaving directory `./ns-3-dev'

Once the project has built you typically will not use ns-3-allinone scripts. You will now interact directly with Waf and we **do it in the ns-3-dev directory and not in the ns-3-allinone directory**.

### Configuration with Waf

To see valid configure options, type ./waf --help. The most important option is -d <debug level>. Valid debug levels (which are listed in waf --help) are: "debug" or "optimized". It is also possible to change the flags used for compilation with (e.g.):

CXXFLAGS="-O3" ./waf configure

or, alternately, the gcc compiler

CXX=g++-3.4 ./waf configure

**Note:** Unlike some other build tools, to change the build target, the option must be supplied during the configure stage rather than the build stage (i.e., "./waf -d optimized" will not work; instead, do

./waf -d optimized configure; ./waf

The resulting binaries are placed in build/<debuglevel>/srcpath. For example, in a debug build you can find the executable for the first.cc example as build/examples/first. You can debug the executable directly by:

./waf --shell cd build/debug/examples gdb ns-<version>-first-debug

Of course, you can run gdb in emacs, or use your favorite debugger such as ddd or insight just as easily. In an optimized build you can find the executable for the first.cc example as build/examples/ns-<version>-first-optimized.

In order to forcibly disable python bindings, you can provide the following option:

./waf --disable-python configure

In order to tell the build system to use the sudo program to set the suid bit if required, you can provide the following option:

./waf --enable-sudo configure

To start over a configuration from scratch, type:

./waf distclean

Or if you get stuck and all else fails:

rm -rf build

followed by changing back into ns-3-allinone and doing:

./build.py

will basically reset your build state.

To see all waf options:

./waf --help

## Validating

ns-3 has unit tests that can be run to verify the installation:

./test.py

which should produce output like:

PASS: TestSuite histogram PASS: TestSuite ns3-wifi-interference PASS: TestSuite ns3-tcp-cwnd PASS: TestSuite ns3-tcp-interoperability PASS: TestSuite sample ...

## Using Python

See [this page](https://www.nsnam.org/wiki/NS-3_Python_Bindings).

## Troubleshooting

See [this page](https://www.nsnam.org/wiki/Troubleshooting).

## Obsolete information

Older versions of ns-3, prior to 3.15, supported using cygwin to run on Windows platform.

### Windows

There are three basic options for Windows support:

- We provide HOWTO documents describing the process for installing Linux support and getting ns-3 running using two popular virtualization products: VirtualBox (
[HOWTO use VirtualBox to run simulations on Windows machines](https://www.nsnam.org/wiki/HOWTO_use_VirtualBox_to_run_simulations_on_Windows_machines)) and VMware ([HOWTO use VMware to set up virtual networks (Windows)](https://www.nsnam.org/wiki/HOWTO_use_VMware_to_set_up_virtual_networks_(Windows))). - There is an experimental project,
[Ns3 on Windows](https://www.nsnam.org/wiki/Ns-3_on_Visual_Studio_2012), using Visual Studio 2012. For support on Visual Studio 2010 see[ns-3 on Visual Studio 2010](https://www.nsnam.org/wiki/HOWTO_use_ns-3_on_Windows_with_Visual_Studio_2010) [Cygwin](http://www.cygwin.com)has been supported in the past: gcc 3.4.4 (debug only), gcc 4.3.2 (debug and optimized). Note, however, that there are limitations with regard to[Python bindings](https://www.nsnam.org/wiki/NS-3_Python_Bindings#Cygwin_limitation), and that Real-time simulator, Emulated Net Device, Tap Bridge and Network simulation cradle are not supported.

An alternative Windows platform is MinGW. There are maintainers who attempt to keep a subset of ns-3 running on MinGW, but it is not "officially" suppported. This means that bugs filed against MinGW will be addressed as time permits.

Cygwin can sometimes be problematic due to the way it actually does its emulation, and sometimes interactions with other Windows software can cause problems. If you do use Cygwin or MinGW; and use Logitech products, we will save you quite a bit of heartburn right off the bat and encourage you to take a look at the [MinGW FAQ](http://oldwiki.mingw.org/index.php/FAQ).

Search for "Logitech" and read the FAQ entry, "why does make often crash creating a sh.exe.stackdump file when I try to compile my source code." Believe it or not, the ``Logitech Process Monitor`` insinuates itself into every DLL in the system when it is running. It can cause your Cygwin or MinGW DLLs to die in mysterious ways and often prevents debuggers from running. Beware of Logitech software when using Cygwin.
