# Building

**Parent:** GNU Octave — Project Ideas
**Source:** https://wiki.octave.org/Building
**Scraped:** 2026-02-22T23:28:47.624138

---

# Building

[Jump to navigation](https://wiki.octave.org#mw-head)

[Jump to search](https://wiki.octave.org#searchInput)

*This article provides general information about***building GNU Octave**from source (on Unix-like systems).

*If you just want to***install GNU Octave**, see[Category:Installation](https://wiki.octave.org/Category:Installation).*For***MS Windows**, read[Building on Microsoft Windows](https://wiki.octave.org/Building_on_Microsoft_Windows)and[Windows Installer](https://wiki.octave.org/Windows_Installer).*For***macOS**, read[Octave for macOS](https://wiki.octave.org/Octave_for_macOS).


## General steps

- Install all
[build dependencies](https://wiki.octave.org#Dependencies)(see below). - Getting the Octave sources ...

- (A) ... from the development repository (requires also
[Mercurial](https://www.mercurial-scm.org/))

- (A) ... from the development repository (requires also

hg clone[https://www.octave.org/hg/octave]&& \ cd octave && \ ./bootstrap

- (B) ... from a release


wget[https://ftpmirror.gnu.org/octave/octave-10.3.0.tar.gz]&& \ tar -xzf octave-10.3.0.tar.gz && \ cd octave-10.3.0

- 3. Configure, build, check, and install Octave

mkdir .build && \ cd .build && \ ./../configure --prefix=$HOME/my_octave && \make -j2 && \[[1]]make check && \ make install[[2]]

## Dependencies

Most of the dependencies given in this section can be very conveniently installed on many [GNU/Linux](https://wiki.octave.org/Octave_for_GNU/Linux) systems.

Dependencies marked with green background are **required** for building Octave. All other tools and libraries are recommended/optional, but very useful features (like the GUI, plotting, etc.) are likely to be disabled.

### Build tools

| Dependency | Description | License / Copyright |
|---|---|---|
|

[Automake](https://www.gnu.org/software/automake)[C++, C, and Fortran compilers](https://gcc.gnu.org)[GNU Make](https://www.gnu.org/software/make)[Libtool](https://www.gnu.org/software/libtool)[Bison](https://www.gnu.org/software/bison)[Flex](https://www.gnu.org/software/flex)### Documentation tools

| Dependency | Description | License / Copyright |
|---|---|---|
|

[FTGL](https://www.freetype.org)[GL2PS](http://geuz.org/gl2ps)[Texi2HTML](https://www.nongnu.org/texi2html)[Texinfo](https://www.gnu.org/software/texinfo)[TeX Live](https://www.tug.org/texlive/)### External tools and libraries

| Dependency | Description | License / Copyright |
|---|---|---|
|

[LAPACK](https://netlib.org/lapack)[PCRE](https://www.pcre.org)[GNU Readline](https://www.gnu.org/software/readline)[ARPACK-NG](https://github.com/opencollab/arpack-ng)[cURL](https://curl.haxx.se)[FFTW3](http://www.fftw.org)[FLTK](https://www.fltk.org)[fontconfig](https://www.freedesktop.org/wiki/Software/fontconfig)[FreeType](https://www.freetype.org)[GL2PS](https://www.geuz.org/gl2ps/)[GLPK](https://www.gnu.org/software/glpk)[gnuplot](http://www.gnuplot.info)[GraphicsMagick++](http://www.graphicsmagick.org)[HDF5](https://www.hdfgroup.org/solutions/hdf5)[OpenJDK](https://www.hdfgroup.org/solutions/hdf5)[OpenGL](https://www.opengl.org)[PortAudio](http://www.portaudio.com/)[Qhull](http://www.qhull.org)[QRUPDATE](http://sourceforge.net/projects/qrupdate)[QScintilla](https://riverbankcomputing.com/software/qscintilla)[Qt](https://www.qt.io/)[RapidJSON](https://rapidjson.org/)[SuiteSparse](http://faculty.cse.tamu.edu/davis/suitesparse.html)[SUNDIALS IDA](https://computing.llnl.gov/projects/sundials/ida)[zlib](https://zlib.net)## Tweaks

### Install Octave in home directory

To install multiple versions of GNU Octave on one system, it is recommended to use the `--prefix`

option of the `configure`

script. With this option one can determine a custom installation directory, preferably within your user's home directory, to avoid elevated installation privileges. One does not "clutter" the system by running `sudo make install`

and the custom build Octave can coexist with, for example, your Linux distribution installation of Octave.

In order to start the custom build of Octave almost as convenient as the Linux distribution installation of Octave, one can create an alias within .bashrc:

echo "alias myoctave='$HOME/my_octave/bin/octave'" >> ~/.bashrc

Then update your .bashrc without doing logout and login:

source $HOME/.bashrc

If you simply enter `octave`

, you'll start your Linux distribution installation of Octave. But when you enter `myoctave`

, you'll start your custom build of Octave inside your home directory.

### Uninstall

- If you still have the .build folder, just run
`make uninstall`

from it. - Just delete the install folder, e.g.
`rm -rf $HOME/my_octave`

.

In any case, don't forget to remove any created *alias* entries in ~/.bashrc.

### Large array support

## See also

and`README`

in the development repository.`/etc/HACKING.md`

[https://octave.org/doc/interpreter/Installation.html](https://octave.org/doc/interpreter/Installation.html)[MXE](https://wiki.octave.org/MXE)-- a more customized Octave build including many self-compiled tools.

## Footnotes

[↑](https://wiki.octave.org#cite_ref-1)`--prefix`

determines the installation location, see the[Tweaks section](https://wiki.octave.org#Install_Octave_in_home_directory)for details. For more information about configuration options, type`./../configure --help`

.[↑](https://wiki.octave.org#cite_ref-2)Depending on your system and processor count, use a larger number of parallel jobs, e.g.`-j8`

.
