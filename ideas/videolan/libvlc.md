# libVLC

**Parent:** VideoLAN — Project Ideas
**Source:** https://wiki.videolan.org/LibVLC/
**Scraped:** 2026-02-22T23:28:47.574334

---

# libVLC

[Jump to navigation](https://wiki.videolan.org#mw-head)

[Jump to search](https://wiki.videolan.org#p-search)

The **libVLC** (VLC SDK) media framework can be embedded into an application to get multimedia capabilities.

**libVLC** is a cross-platform audio and video API that provides a comprehensive multimedia API that can be used across mobile, server and desktop to render video and output audio as well as encode and stream.

Since VLC is based on libVLC, one should be able to have the same features that [VLC media player](https://wiki.videolan.org/VLC_media_player/) has.

The libVLC media framework is already used by several applications; see [who uses libVLC?](https://wiki.videolan.org/LibVLC_Users/)

## Contents

## Features

libVLC notably can:

- Play every media file formats, every codec and every streaming protocols
*(RTSP, RTMP, Multicast, HLS/Dash/HDS, etc..)* - Run on every platform, from desktop
*(Windows, Linux, Mac)*to mobile*(Android, iOS)*and TVs*(AppleTV, Android TV, Tizen)*and Consoles*(PS4/5, Xbox)* - Hardware and efficient decoding on every platform, up to 8K
- Network browsing for distant filesystems
*(SMB, FTP, SFTP, NFS...)*and servers*(UPnP, DLNA)* - Playback of Audio CD, DVD and Bluray with menu navigation
- Support for 8K and HDR, including tonemapping for SDR streams
- Audio passthrough with SPDIF and HDMI, including for Audio HD codecs, like DD+, TrueHD or DTS-HD
- Support for complex video and audio filters
- Support for 360/VR video and 3D audio playback, including Ambisonics
- Able to cast and stream to distant renderers, like Chromecast and UPnP renderers.

## libVLC, license and proprietary applications

Since libVLC is licensed under LGPLv2, one can do applications based on libVLC which are not licensed under the GPL *(different open source licenses, or non-open source applications)*. One must comply with the LGPL terms, for libVLCcore, VLC plugins and libVLC.

What it means, in layman's terms, is that you can use libVLC in your app, without open sourcing it, as long as the modifications to the VLC core and plugins are re-shared to the users and community. Also, you need to separate clearly your app from libVLC *(use of dynamic linking makes it much easier)*.

It is however strongly advised to only use LGPL plugins.

### Proprietary plugins

It is possible to also have proprietary plugins around VLC, as long as you can comply to the LGPL, for all libraries involved.

Distribution must be separated.

Again, in layman's terms, if you have a proprietary plugin, you should:

- use libvlccore as a dynamic library,
- link your plugin to libvlccore and other LGPL libraries dynamically,
- make sure libVLC does not depend on your specific plugin,
- be able to remove the plugin and still have a working application.

## Documentation

Please refer to the [Doxygen documentation](https://www.videolan.org/developers/vlc/doc/doxygen/html/group__libvlc.html), which is the reference documentation.

__ Make sure that the documentation matches the LibVLC version.__ (if not, you can build it from the source code)

Some further topics are covered here:

[LibVLC Memory Management](https://wiki.videolan.org/LibVLC_Memory_Management/)explained: covers the basics on the`_new()`

,`_retain()`

,`_release()`

.[LibVLC Media List Management](https://wiki.videolan.org/LibVLC_Media_List_Management/)explained: covers the basics on setting up a playlist.[Generate a .lib for using libVLC on Windows](https://wiki.videolan.org/GenerateLibFromDll/)(before libVLC 2.1.0)



## Examples

### Playback

[Current version (1.1.x and later)](https://wiki.videolan.org/LibVLC_Tutorial/)- Gtk Player:
[doc/libvlc/gtk_player.c](https://git.videolan.org/?p=vlc.git;a=blob;f=doc/libvlc/gtk_player.c) - Qt Player:
[doc/libvlc/QtPlayer/player.cpp](https://git.videolan.org/?p=vlc.git;a=blob;f=doc/libvlc/QtPlayer/player.cpp) - WxWidgets Player:
[doc/libvlc/wx_player.cpp](https://git.videolan.org/?p=vlc.git;a=blob;f=doc/libvlc/wx_player.cpp)

### Rendering and streaming

[Use LibVLC in an SDL application](https://wiki.videolan.org/LibVLC_SampleCode_SDL/)[Stream into a memory zone](https://wiki.videolan.org/Stream_to_memory_(smem)_tutorial/)- Generate thumbnails using LibVLC:
[doc/libvlc/vlc-thumb.c](https://git.videolan.org/?p=vlc.git;a=blob;f=doc/libvlc/vlc-thumb.c) - Quick DVD ripper:
[doc/libvlc/libvlc_DVD_ripper.c](https://git.videolan.org/?p=vlc.git;a=blob;f=doc/libvlc/libvlc_DVD_ripper.c)

### More complex examples

### libVLC on Android

### VLCKit for Cocoa (iOS/macOS)

You can find details on features and implementation on a [designated page](https://wiki.videolan.org/VLCKit/).

#### macOS

#### iOS

### Crossplatform .NET/Mono support with LibVLCSharp

### Outdated samples

[Versions 0.9.x and 1.0.x](https://wiki.videolan.org/LibVLC_Tutorial_0.9/)[Version 0.8.6](https://wiki.videolan.org/LibVLC_Tutorial_086c/)[Visual C++](https://wiki.videolan.org/LibVLC_Visual_C%2B%2B/)*(uses "old" legacy API)*[VCL component for Delphi](https://wiki.videolan.org/IceVLCPlayer/)(out-of-date)

## Language & platform bindings

LibVLC is a C library. It has bindings to the following languages and frameworks:

- C++, using the
[libvlcpp](https://code.videolan.org/videolan/libvlcpp)library - The
[Web plugin](https://wiki.videolan.org/Web_plugin/)for ActiveX (e.g. MSIE) and NPAPI (e.g. Firefox) [WebChimera](http://WebChimera.org)browser plugin with[NW.js](http://nwjs.io/)support[WebChimera.js](https://github.com/RSATom/WebChimera.js)- another way to bind libvlc to node.js/io.js/NW.js/Electron[Objective-C/Swift for iOS and macOS](https://wiki.videolan.org/VLCKit/)[Perl](https://wiki.videolan.org/Perl_bindings/)[Python](https://wiki.videolan.org/PythonBinding/)[Phonon (Qt/KDE) in C++](http://phonon.kde.org/)[Java](https://wiki.videolan.org/Java_bindings/)[Java/Scala/Kotlin/JNI Android](https://code.videolan.org/videolan/vlc-android/tree/master/libvlc/jni)[C#/F#/.NET](https://code.videolan.org/videolan/libvlcsharp)[C++/CX](https://code.videolan.org/videolan/vlc-winrt/tree/master/modules/libvlcppcx)[Go](https://github.com/adrg/libvlc-go)[Rust](https://github.com/garkimasera/vlc-rs)[QmlVlc](http://github.com/RSATom/QmlVlc)- Qt 5 QML binding[VLC-Qt](https://github.com/vlc-qt/vlc-qt)- Qt bindings[wxWidgets MediaCtrl backend](https://wiki.videolan.org/WxVLCBackend/)also in C++[Using libvlc with Delphi](https://wiki.videolan.org/Using_libvlc_with_Delphi/)[Pascal/Delphi](http://sourceforge.net/projects/paslibvlc/)[Tcl](http://wiki.tcl-lang.org/48382)[ActiveX](https://wiki.videolan.org/ActiveX/)with the built-in VLC browser plugin for MSIE (obsolete)

## Compiling

To build LibVLC you need [VLC source code](https://wiki.videolan.org/VLC_source_code/) and follow [VLC compilation instructions](https://wiki.videolan.org/Compile_VLC/) since LibVLC it is directly shipped in VLC source code.

You will find headers in vlc-src/include/vlc and libvlc.so binaries in the *hidden* folder vlc-src/lib/.libs.

When using your custom LibVLC build you will need to define the environment variable `VLC_PLUGIN_PATH` pointing to VLC modules located in vlc-src/modules.
