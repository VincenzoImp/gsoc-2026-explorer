# Projects

**Parent:** GNU Octave — Project Ideas
**Source:** https://wiki.octave.org/Projects
**Scraped:** 2026-02-22T23:28:47.624389

---

# Projects

[Jump to navigation](https://wiki.octave.org#mw-head)

[Jump to search](https://wiki.octave.org#searchInput)

The list below summarizes features or bug fixes we would like to see in Octave. This list is not exclusive -- there are many other things that might be good projects, but it might instead be something we already have. Also, some of the following items may not actually be considered good ideas now.

[Developer FAQ](https://wiki.octave.org/Developer_FAQ).

- Summer of Code students, please also see
[Summer of Code - Getting Started](https://wiki.octave.org/Summer_of_Code_-_Getting_Started). - If you're looking for small project, see
[short projects](https://wiki.octave.org/Short_projects).

# Numerical

- Use C++11 <random> libraries for random number generation. Write link between Octave functions (rand, randi, randn, rande) and C++ API. Implement RandStream objects as Matlab does.

- Improve logm, and sqrtm (see this thread:
[http://octave.1599824.n4.nabble.com/matrix-functions-td3137935.html](http://octave.1599824.n4.nabble.com/matrix-functions-td3137935.html))

- Use pairwise or block addition in sum() to mitigate against numerical errors without substantial performance penalty (
[https://en.wikipedia.org/wiki/Pairwise_summation](https://en.wikipedia.org/wiki/Pairwise_summation)), see bug[#61143](https://savannah.gnu.org/bugs/?61143)for prior discussion.

- Review implementing algorithm in this 2009 paper (
[https://epubs.siam.org/doi/pdf/10.1137/080738490](https://epubs.siam.org/doi/pdf/10.1137/080738490)) for xsum (sum with extra accuracy). The existing implementation uses a 2005 paper.

- Improve complex mapper functions. See W. Kahan, ``Branch Cuts for Complex Elementary Functions, or Much Ado About Nothing's Sign Bit (in The State of the Art in Numerical Analysis, eds. Iserles and Powell, Clarendon Press, Oxford, 1987) for explicit trigonometric formulae. See
[#8172](https://savannah.gnu.org/patch/?8172)for a previous attempt.

- Make functions like gamma() return the right IEEE Inf or NaN values for extreme args or other undefined cases.

- Improve sqp.

- Fix CollocWt? to handle Laguerre polynomials. Make it easy to extend it to other polynomial types.

- Add optional arguments to colloc so that it's not restricted to Legendre polynomials.

- Move rand, eye, xpow, xdiv, etc., functions to the matrix classes.

- Improve design of ODE, DAE, classes.

- Evaluate harmonics and cross-correlations of unevenly sampled and nonstationary time series, as in
[http://www.jstatsoft.org/v11/i02](http://www.jstatsoft.org/v11/i02)(which has C code with interface to R). (This is now partly implemented in the[lssa](http://octave.sourceforge.net/lssa/index.html)package.)



## Implement solver for initial-boundary value problems for parabolic-elliptic PDEs in 1D

The project will deliver a solver for initial-boundary value problems for parabolic-elliptic PDEs in 1D similar to Matlab's function `pdepe`. A good starting point is the [method of lines](http://en.wikipedia.org/wiki/Method_of_lines) for which you can find more details [here](http://en.wikibooks.org/wiki/Partial_Differential_Equations/Method_of_Lines) and [here](http://www.scholarpedia.org/article/Method_of_lines), whereas an example implementation can be found [here](http://www.scholarpedia.org/article/Method_of_Lines/Example_Implementation). In addition, [this page](http://www.pdecomp.net/) provides some useful material.

## Implement solver for 1D nonlinear boundary value problems

The project will complete the implementation of the bvp4c solver that is already available in an initial version in the odepkg package
by adding a proper error estimator and will implement a matlab-compatible version of the bvp5c solver.
Details on the methods to be implemented can be found in [this paper](http://dx.doi.org/10.1145/502800.502801) on bvp4c and [this paper](http://www.jnaiam.net/new/uploads/files/014dde86eef73328e7ab674d1a32aa9c.pdf) on bvp5c. Further details are available in [this book](http://books.google.it/books/about/Nonlinear_two_point_boundary_value_probl.html?id=s_pQAAAAMAAJ&redir_esc=y).



## Matlab-compatible ODE solvers in core-Octave

- Improve handling of sparse Jacobians in IDE/DAE solvers
**(2021-01-21 Still an issue? See bug**[#55905](https://savannah.gnu.org/bugs/?55905).)- Currently, in the IDA wrapper function __ode15__ an over conservative guess for the amount of memory to be allocated when assembling a sparse jacobian is used, essentially allocating enough space for a full jacobian then freeing the excess memory, an initial patch for fixing this has been posted on the tracker, for integrating this into Octave it must be generalized to support prior versions of SUNDIALS
- Currently Jacobians passed by the user in Octave's sparse matrix format are copied into SUNDIALS own sparse matrix format. Newer versions of SUNDIALS (5.x or higher) support letting the user take care of the linear algebra data structures and methods thus removing the need for the copy. Taking advantage of this feature would improve the solver performance both in terms of memory footprint and speed.
- See also
[SUNDIALS release history](https://computing.llnl.gov/projects/sundials/release-history).

- Implement Matlab compatible versions of "deval".

## High Precision Arithmetic Computation

The Linear Algebra Fortran libraries used by Octave make use of of single (32 bits) and double (64 bits) precision floating point numbers. Many operations are stopped when matrices condition number goes below 1e-16: such matrices are considered as ill-conditioned. There are cases where this is not enough, for instance simulations implying chemical concentrations covering the range 10^4 up to 10^34. There are a number of ways to increase the numerical resolution, like f.i. make use of 128 bits quadruple precision numbers available in GFortran. A simpler option is to build an interface over Gnu MPL arbitrary precision library, which is used internally by gcc and should be available on any platform where gcc runs. Such approach has been made available for MatLab under the name mptoolbox and is licensed under a BSD license. The author kindly provided a copy of the latest version and agreed to have it ported under Octave and re-distributed under GPL v3.0

The architecture consists of an Octave class interface implementing "mp" (multi-precision) objects. Arithmetic operations are forwarded to MPL using MEX files. This is totally transparent to the end user, except when displaying numbers. This implementation needs to be ported and tested under Octave.

## Improve logm, sqrtm, funm

The goal here is to implement some missing Matlab functions related to matrix functions like the [matrix exponential](https://en.wikipedia.org/wiki/Matrix_exponential). There is [a general discussion](https://lists.gnu.org/archive/html/help-octave/2010-12/msg00322.html) of the problem and [a thread on a GSOC project that never took off](https://octave.1599824.n4.nabble.com/Re-GSOC-16-Improvements-to-sqrtm-logm-and-funm-td4675180.html) (together with [working funm.m code](https://github.com/RickOne16/matrix)). A good starting point for available algorithms and open-source implementations is Higham and Deadman's ["A Catalogue of Software for Matrix Functions"](http://eprints.maths.manchester.ac.uk/2102/1/catalog.pdf).
As of Dec. 2025, a working funm.m has been implemented and will be available with the release of Octave 11 (see [bug #67741](https://savannah.gnu.org/bugs/?67741) and [this Discourse thread](https://octave.discourse.group/t/implementation-of-funm/7040/6)). There's still room for improvement, however.

## Improve iterative methods for sparse linear systems

GNU Octave currently has the following Krylov subspace methods for sparse linear systems: pcg (spd matrices) and pcr (Hermitian matrices), bicg,
bicgstab, cgs, gmres, and qmr (general matrices). The description of some of them (pcr, qmr) and their error messages are not aligned. Moreover, they have similar blocks of code (input check for instance) which can be written once and for all in common functions. The first step in this project could be a revision and a synchronization of the codes, starting from the [SOCIS2016](https://socis16octave-improveiterativemethods.blogspot.com/) project, which is already merged into Octave (cset [6266e321ef22](http://hg.savannah.gnu.org/hgweb/octave/rev/6266e321ef22)).

In Matlab, some additional methods are available: minres and symmlq (symmetric matrices), bicgstabl (general matrices), lsqr (least squares). The second step in this project could be the implementation of some of these missing functions.

The [reference book by Yousef Saad](https://www-users.cs.umn.edu/~saad/IterMethBook_2ndEd.pdf) is available online.

# GUI/IDE

- Søren Hauberg has suggested that we need C++ code that can:
- Determine if a line of code could be fully parsed, i.e. it would return true for "plot (x, y);", but false for "while (true)".
- Evaluate a line of code and return the output as a string (it would be best if it could provide three strings: output, warnings and errors).
- Query defined variables, i.e. get a list of currently defined variables. Bonus points if it could tell you if anything had changed since the last time you checked the variables (could also be done with signals).

- Allow side-by-side editing
- Allow multiple Editor windows, so source files can be edited side-by-side within the GUI.
- Add a vertical window splitter to the Editor so you can see the initialization code at the top while you type at the bottom.
- Ensure that any particular file is only open in one tab at a time!


## GUI Variable Editor and Property Inspector

Octave has a preliminary implementation of a Variable Editor: a spreadsheet-like tool for quickly editing and visualizing variables. The initial phase of the project will be learning how the implementation was done.

With the knowledge gained, the second part of the project will be to implement a Property Inspector. This is a spreadsheet like interface to the many, many graphics properties that exist and are different on a per-object basis. The goal would be not only the concise-display of the existing properties, but a reasonable user interface to change them. As examples, Boolean properties should be able to be toggled with a double-click; Radio properties should have a drop-down list of only the supported options; Other properties that can be modified should have the constraints built-in (for example, Linewidth must be a scalar, while Position must be a 1x4 vector). It would also be important to have easy access to the documentation of a property.

For reference, Matlab has a similar Property Inspector ([https://www.mathworks.com/help/matlab/ref/inspect.html](https://www.mathworks.com/help/matlab/ref/inspect.html)).

## Sisotool. Create a graphical design tool for tuning closed loop control system ([Control package](https://wiki.octave.org/Control_package))

When tuning a SISO feedback system it is very helpful to be able to grab a pole or a zero and move them by dragging them with the mouse. As they are moving the software must update all the plotted lines. There should be the ability to display various graphs rlocuse, bode, step, impulse etc. and have them all change dynamically as the mouse is moving. The parameters of the compensator must be displayed and updated.
Recently, some implementation was done during [GSoC 2018](https://wiki.octave.org/Summer_of_Code#GSoC_2018), see [https://eriveltongualter.github.io/GSoC2018/final.html](https://eriveltongualter.github.io/GSoC2018/final.html) for details.

# Sparse Matrices

The paper by [Bateman & Adler](http://arxiv.org/abs/cs.MS/0604006) is good reading for understanding the sparse matrix implementation.

- Improve Matlab compatibility for
.`sprandsym`


- Sparse logical indexing in idx_vector class so that something like
`a = sprandn (1e6, 1e6, 1e-6); a(a<1) = 0;`

won't cause a memory overflow.

- Other missing Functions
- lsqr
- minres
- symmlq


## SPQR Interface

Octave implements QR factorization for sparse matrices, but it does so with an older "CXSPARSE" library. This has caused fundamental issues, including segfaults as recorded here (bugs [#51950](https://savannah.gnu.org/bugs/?51950) and [#57033](https://savannah.gnu.org/bugs/?57033)). The goal of this project is to program an interface to the API for the SQPR library ([http://faculty.cse.tamu.edu/davis/suitesparse.html](http://faculty.cse.tamu.edu/davis/suitesparse.html)). This is the same library that Matlab uses for this purpose.

- Improve QR factorization functions, using idea based on CSPARSE cs_dmsol.m

- Improve QR factorization by replacing CXSPARSE code with SPQR code, and make the linear solve return 2-norm solutions for ill-conditioned matrices based on this new code

# Strings

- Consider making octave_print_internal() print some sort of text representation for unprintable characters instead of sending them directly to the terminal. (But don't do this for fprintf!)

- Consider changing the default value of `string_fill_char' from SPC to NUL.

# Other Data Types

- Template functions for mixed-type ops.

- Convert other functions for use with the floating point type including quad, dasrt, daspk, etc.

# Input/Output

- Make fread and fwrite work for complex data. Iostreams based versions of these functions would also be nice, and if you are working on them, it would be good to support other size specifications (integer*2, etc.).

- Move some pr-output stuff to liboctave.

- Make the cutoff point for changing to packed storage a user-preference variable with default value 8192.

- Complain if there is not enough disk space available (I think there is simply not enough error checking in the code that handles writing data).

- Make it possible to tie arbitrary input and output streams together, similar to the way iostreams can be tied together.

- Expand
`imwrite`

options. This shouldn't be too hard to implement, since it's wrapped around GraphicsMagick.

- Extend Octave functions to work on stored arrays that are too big to fit in RAM, similar to available R
[packages.](http://www.bigmemory.org/)

- write
`xmlread`

and`xmlwrite`

. This could be done using[Xerces C++ interface](http://xerces.apache.org/xerces-c/)which apparently is what[Matlab uses](http://octave.1599824.n4.nabble.com/xml-in-octave-td4663034.html). (? These functions have been implemented in the io package already many years ago; making it core Octave functions would introduce a dependency on Java (tru the xerces library) by core Octave and that is not quite what the core devs would want ...).

- Implement hdf5 for .mat files (see
[this thread](http://octave.1599824.n4.nabble.com/Reading-Matlab-td4650158.html)), likely a necessary step to enable saving of classdef classes.

# Interpreter

The interpreter is written in C++, undocumented. There are many possible projects associated with it.

**Required skills**: *Very good* C and C++ knowledge, possibly also understanding of [GNU bison](http://en.wikipedia.org/wiki/Gnu_bison) and [flex](http://en.wikipedia.org/wiki/Flex_lexical_analyser). Understanding how compilers and interpreters are made plus being able to understand how to use a profiler and a debugger will probably be essential skills.

- Allow customization of the debug prompt.

- Fix the parser so that

if (expr) 'this is a string' end

is parsed as IF expr STRING END. *(see this post on the mailing list)*

- Clean up functions in input.cc that handle user input (there currently seems to be some unnecessary duplication of code and it seems overly complex).

- Consider allowing an arbitrary property list to be attached to any variable. This could be a more general way to handle the help string that can currently be added with `document'.

- Allow more command line options to be accessible as built-in variables (--echo-commands, etc.).

- Make the interpreter run faster.

- Allow arbitrary lower bounds for array indexing.

- Improve performance of recursive function calls.

- Improve the way ignore_function_time_stamp works to allow selecting by individual directories or functions.

- Add a command-line option to tell Octave to just do syntax checking and not execute statements.

- Clean up symtab and variable stuff.

- Input stream class for parser files -- must manage buffers for flex and context for global variable settings.

- make parser do more semantic checking, continue after errors when compiling functions, etc.

- Make LEXICAL_ERROR have a value that is the error message for parse_error() to print?

- Add a run-time alias mechanism that would allow things like alias fun function_with_a_very_long_name so that `function_with_a_very_long_name' could be invoked as `fun'.

- Allow local changes to variables to be written more compactly than is currently possible with unwind_protect. For example,

function f () local prefer_column_vectors = something; ... endfunction

would be equivalent to

function f () save_prefer_column_vectors = prefer_column_vectors; unwind_protect prefer_column_vectors = something; ... unwind_protect_cleanup prefer_column_vectors = save_prefer_column_vectors; end_unwind_protect endfunction



- Fix all function files to check for bogus inputs (wrong number or types of input arguments, wrong number of output arguments).

- Handle options for built-in functions more consistently.

- Too much time is spent allocating and freeing memory. What can be done to improve performance?

Use move constructors rather than copy constructors for things like dim_vectors which are repeatedly created just to initialize Array or Matrix objects.

- Error output from Fortran code is ugly. Something should be done to make it look better.

- It would be nice if output from the Fortran routines could be passed through the pager.

- Attempt to recognize common subexpressions in the parser.

- Consider making it possible to specify an empty matrix with a syntax like [](https://wiki.octave.org/e1, e2). Of course at least one of the expressions must be zero...

- Is
[Matrix::fortran_vec()](Matrix::fortran_vec())really necessary?

- Rewrite whos and the symbol_record_info class. Write a built-in function that gives all the basic information, then write who and whos as M-files.

- On systems that support matherr(), make it possible for users to enable the printing of warning messages.

- Make it possible to mark variables and functions as read-only.

- Make it possible to write a function that gets a reference to a matrix in memory and change one or more elements without generating a second copy of the data.

- Use nanosleep instead of usleep if it is available? Apparently nanosleep is to be preferred over usleep on Solaris systems.

## Improve JIT compiling

Octave's interpreter is *very* slow on some loops. Recently, thanks to Max Brister's work, an initial implementation of a just-in-time compiler (JITC) in [LLVM](http://llvm.org) for GSoC 2012. This project consists in understanding Max's current implementation and extending it so that functions and exponents (e.g. 2^z) compile with the JITC. This requires knowledge of compilers, C++, LLVM, and the Octave or Matlab languages. A capable student who demonstrates the ability to acquire this knowledge quickly may also be considered. Max himself will mentor this project. [Here](http://planet.octave.org/octconf2012/jit.pdf) is Max's OctConf 2012 presentation about his current implementation. See also [JIT](https://wiki.octave.org/JIT).

## Improve memory management

From profiling the interpreter, it appears that a lot of time is spending allocating and deallocating memory. A better memory management algorithm might provide some improvement.

## Implement classdef classes

Matlab has two kinds of classes: old style @classes and new style classdef. Octave has only fully implemented the old style. There is partial support for classdef classes in version 4.0, refer to the [classdef status page](https://wiki.octave.org/Classdef) for what is not yet implemented. There is irregular work here, and classdef is [a very](http://www.mathworks.com/help/matlab/matlab_oop/method-attributes.html) [complicated](http://www.mathworks.com/help/matlab/events-sending-and-responding-to-messages.html) [thing](http://www.mathworks.com/help/matlab/enumeration-classes.html) to fully implement. A successful project would be to implement enough of classdef for most basic usages. Familiarity with Matlab's current classdef support would be a huge plus. Michael Goffioul and jwe can mentor this.

Although there's already a substantial classdef support in current octave code base, there are still many areas that are unimplemented or need improvements. The main ones that come to my mind are:

- support for events
- support for enums
- support for "import" (this requires good understanding of octave internals, especially the symbol table)
- improving multiple inheritance and method resolution
- honoring and computing "Sealed" attribute
- support for function handle to methods

## Improve MPI package

Octave Forge's [MPI package](http://octave.sourceforge.net/mpi/index.html)
is a wrapper for basic MPI functions for parallel computing. It is implemented
by wrapping MPI function calls in simple DLD functions that map Octave's Datataypes to
MPI Derived Datatypes.
The proposed project deals with improving and extending the Octave MPI package, for example:

- Octave MPI applications can currently be only run in batch mode, add the ability to launch parallel jobs and collect their output in an interactive Octave session.
- Implement functions for non-blocking communication (MPI_Isend, MPI_Irecv)
- Implement one-to-many (Broadcast, Scatter), many-to-one (Reduce, Gather), and many-to-many (All Reduce, Allgather) communication routines

# Graphics

- Correctly handle case where DISPLAY is unset. Provide --no-window-system or --nodisplay (?) option. Provide --display=DISPLAY option? How will this work with gnuplot (i.e., how do we know whether gnuplot requires an X display to display graphics)?

- Implement a Cairo-based renderer for 2D-only graphics, with support for PS/PDF/SVG output (for printing).

- On 'imagesc' plots, report the matrix values also based on the mouse position, updating on mouse moving.

- Add map-creating capabilities similar to the Matlab
[Mapping toolbox](https://www.mathworks.com/help/map/functionlist.html)for inclusion in the Octave Forge[mapping package](https://sourceforge.net/p/octave/mapping).

- Add data cursor to trace data values in figure.

## Non-OpenGL renderer

Besides the original gnuplot backend, Octave also contains an OpenGL-based renderer for advanced and more powerful 3D plots. However, OpenGL is not perfectly suited for 2D-only plots where other methods could result in better graphics. The purpose of this project is to implement an alternate graphics renderer for 2D only plots (although 3D is definitely not the focus, extending the new graphics renderer to support basic 3D features should also be taken into account). There is no particular toolkit/library that must be used, but natural candidates are:

[Qt](http://qt.nokia.com): the GUI is currently written in Qt[Cairo](http://en.wikipedia.org/wiki/Cairo_%28software%29): this library is widely used and known to provides high-quality graphics with support for PS/PDF/SVG output.

## LaTeX markup

Text objects in plots (like titles, labels, texts...) in the OpenGL renderer only support plain text and TeX. The latter consists of a very limited subset of the TeX language. On the other hand, the LaTeX formatting support is expected to provide full LaTeX capabilities. There are various approaches that can be used:

- Use an external LaTeX engine: this is the most straightforward, but it requires users to install a LaTeX distribution and setup Octave to use it.
- Use an external library that supports LaTeX syntax, e.g.
[JLaTeXMath](https://github.com/opencollab/jlatexmath)a Java API to display LaTeX code,[qtmathjax](https://github.com/nathancarter/qtmathjax)a Qt based library that executes MathJax in a background web page. - Implement our own LaTeX parser and renderer. The matplotlib project
[has already done this in Python](http://matplotlib.sourceforge.net/users/usetex.html)and might be used as an example of how to do this in Octave. There is also[JKQtPlotter](https://github.com/jkriege2/JKQtPlotter), a Qt based plotting application which implements its own LaTeX parser/renderer in C++.

# History

- Add an option to allow saving input from script files in the history list.

- The history command should accept two numeric arguments to indicate a range of history entries to display, save or read.

- Avoid writing the history file if the history list has not changed.

- Avoid permission errors if the history file cannot be opened for writing.

- Fix history problems — core dump if multiple processes are writing to the same history file?

# Configuration and Installation

- Makefile changes:
- eliminate for loops
- define shell commands or eliminate them
- consolidate targets


- Create a docs-only distribution?

# Documentation

# Tests

- Improved set of tests:
[[1]](http://octave.1599824.n4.nabble.com/template/NamlServlet.jtp?macro=user_nodes&user=370633)- Tests for various functions. Would be nice to have a test file corresponding to every function (see below)
- Tests for element by element operators: + - .* ./ .\ .^ | & < <= == >= > != !
- thorough tests for power operator including corner cases and strange combinations such as complex .^ range.

- Tests for boolean operators: && ||
- Tests for other operators: * / \ ' .'
- Tests from bug reports.
- Tests for indexed assignment. Need to consider the following:
- fortran-style indexing
- zero-one indexing
- assignment of empty matrix as well as values resizing

- Tests for all internal functions.


- Implement a coverage tool for collecting coverage data and generating code coverage reports on m-file functions and scripts. This would be very useful for Octave development as well as for users who want a code coverage report for their own functions and scripts.

- Implement test for plotting and graphics functions that might currently only have basic input checking and/or demos for human inspection. Possibly create tests that probe properties of the handles created and returned by most such functions, such that test plots can be checked for correct feature size/location, etc.

We are far from even having one test for every function, so focus should be on getting the breadth of coverage first before trying to get the depth of 100% statement coverage. As of Dec 2015, 202 of 1020 m-files have no tests. Some of these will be plotting functions which have demos instead, but that leaves enough functions to be an interesting project. As of Dec 2015, there are 485 instances of C++ functions which need tests.

After Octave is compiled, running the `make check`

build target will run the full test suite and generate a file called test/fntests.log in the build directory with a summary of the results. At the end of the file is a list of all functions for which no tests were found. An extract is posted in the [files missing tests](https://wiki.octave.org/Files_missing_tests) page. If you are not building Octave yourself, the test suite can be run on an installed binary copy by executing the `__run_test_suite__`

command at the Octave prompt. The fntests.log file will be written in the current directory in this case.

There also need to be tests for functions written in the C++ files. See [Add_BIST_tests_for_octave_functions_written_in_C++](https://wiki.octave.org/Add_BIST_tests_for_octave_functions_written_in_C%2B%2B) for instructions and a list of instances.

See also [Continuous Build#Coverage Report](https://wiki.octave.org/Continuous_Build#Coverage_Report).

# Programming

- Better error messages for missing operators?

- Eliminate duplicate enums in pt-exp.cc, pt-const.cc, and ov.cc.

- Handle octave_print_internal() stuff at the liboctave level. Then the octave_value classes could just call on the print() methods for the underlying classes.

- As much as possible, eliminate explicit checks for the types of octave_value objects so that user-defined types will automatically do the right thing in more cases.

- Only include config.h in files that actually need it, instead of including it in every .cc file. Unfortunately, this might not be so easy to figure out.

- GNU coding standards:
- Add a `Makefile' target to the Makefiles.
- Comments on #else and #endif preprocessor commands.
- Change error message format to match standards everywhere.


- Eliminate more global variables.

- Move procstream to liboctave.

- Use references and classes in more places.

- Share more code among the various _options functions.

- Use non-empty identifiers in all warnings and errors issued by Octave, see
[Easy projects#Miscellaneous](https://wiki.octave.org/Easy_projects#Miscellaneous).

- Reduce the amount of datatypes in liboctave.

- Re-implement operators using templates and modern C++. Current system evolved before templates and makes extensive use of macros to define interactions between scalar<->scalar, scalar<->matrix, scalar<->float, etc., etc.
- In liboctave, the directory to work on is liboctave/operators
- In libinterp, the directory to work on is libinterp/operators
- In libinterp, there is also xpow.cc, xdiv.cc in libinterp/corefcn


# Miscellaneous

- Implement some functions for interprocess communication: bind, accept, connect, gethostbyname, etc. (This functionality is already available in the octave sockets package, what is the purpose of moving it to core octave?)

- The ability to transparently handle very large files: Juhana K Kouhia <kouhia@nic.funet.fi> wrote:
- If I have a one-dimensional signal data with the size 400 Mbytes, then what are my choices to operate with it:
- I have to split the data
- Octave has a virtual memory on its own and I don't have to worry about the splitting.

- If I split the data, then my easily programmed processing programs will become hard to program.
- If possible, I would like to have the virtual memory system in Octave i.e., the all big files, the user see as one big array or such. There could be several user selectable models to do the virtual memory depending on what kind of data the user have (1d, 2d) and in what order they are processed (stream or random access).

- If I have a one-dimensional signal data with the size 400 Mbytes, then what are my choices to operate with it:

- An interface to gdb. Michael Smolsky <fnsiguc@weizmann.weizmann.ac.il> wrote:
- I was thinking about a tool, which could be very useful for me in my numerical simulation work. It is an interconnection between gdb and octave. We are often managing very large arrays of data in our fortran or c codes, which might be studied with the help of octave at the algorithm development stages. Assume you're coding, say, wave equation. And want to debug the code. It would be great to pick some array from the memory of the code you're developing, fft it and see the image as a log-log plot of the spectral density. I'm facing similar problems now. To avoid high c-development cost, I develop in matlab/octave, and then rewrite into c. It might be so much easier, if I could off-load a c array right from the debugger into octave, study it, and, perhaps, change some [many] values with a convenient matlab/octave syntax, similar to
`a(:,51:250)=zeros(100,200)`

, and then store it back into the memory of my c code.

- I was thinking about a tool, which could be very useful for me in my numerical simulation work. It is an interconnection between gdb and octave. We are often managing very large arrays of data in our fortran or c codes, which might be studied with the help of octave at the algorithm development stages. Assume you're coding, say, wave equation. And want to debug the code. It would be great to pick some array from the memory of the code you're developing, fft it and see the image as a log-log plot of the spectral density. I'm facing similar problems now. To avoid high c-development cost, I develop in matlab/octave, and then rewrite into c. It might be so much easier, if I could off-load a c array right from the debugger into octave, study it, and, perhaps, change some [many] values with a convenient matlab/octave syntax, similar to

- Implement gdb extensions for Octave types. Octave has the
`etc/gdbinit`

file, which has some basic support for displaying the contents of Octave types. Add more extensions to make it easier to debug octave_values and other Octave types.

- Add a definition to lgrind so that it supports Octave. (See
[http://www.tex.ac.uk/tex-archive/support/lgrind/](http://www.tex.ac.uk/tex-archive/support/lgrind/)for more information about lgrind.)

- Spatial statistics, including covariogram estimation and kriging -- perhaps via an interface to
[gstat](http://www.gstat.org/)?

- the
[units](http://octave.sourceforge.net/miscellaneous/function/units.html)function from the miscellaneous package works by parsing the output of from a call to GNU units. This can be made much more robust by writing it in C++ and including its library "units.h"

# Marketing and Community

- Make the Octave website/
[Project Infrastructure](https://wiki.octave.org/Project_Infrastructure)easier to maintain.

- Make it easier for newcomers to contribute.

- For marketing ideas, see the
[Apache Open Office Introduction to Marketing](https://openoffice.apache.org/orientation/intro-marketing.html)

- Help design a user or a
[developer survey](https://www.openoffice.org/marketing/ooocon2006/presentations/wednesday_c10.pdf)

- Help prepare and deliver presentations and
[Publications about Octave](https://wiki.octave.org/Publications_about_Octave)at colleges and universities.

## Improve Windows binary packaging

We are currently able to build and provide a [installer for Windows](https://wiki.octave.org/Windows_Installer). The build process involves cross-compiling on a Linux system using a fork of the [MXE](http://mxe.cc/) project to build Octave and all of its dependencies. Any ideas for improving this process to make it easier or faster, or to improve the installer itself or the installation experience for Windows users would be appreciated.

**Skills Required**: Knowledge of GNU build systems, Makefiles, configure files, chasing library dependencies, how to use a compiler. No m-scripting or C++ necessary, beyond understanding [the C++ compilation model](http://david.rothlis.net/c/compilation_model/).

## Improve macOS binary packaging

We would like to be able to easily generate binary packages for macOS. Right now, it's difficult and tedious to do so. Most OS X users install Octave using one of the source-based package managers such as Homebrew or MacPorts. Any way to help us build a binary package would be appreciated. Required knowledge is understanding how building binaries in macOS works. Our current approach to building binaries for Windows is to cross-compile from a GNU system using [MXE](http://mxe.cc/), something similar may be possible for OS X ([GUB](http://lilypond.org/gub/)?).

There is a third-party project called ["Octave.app"](http://octave-app.org) that creates and distributes macOS builds of Octave as a Mac app bundle. It is built on top of Homebrew and a set of custom Octave-related Homebrew formuale.

**Skills Required**: Knowledge of GNU build systems, Makefiles, configure files, chasing library dependencies, how to use a compiler. If you choose to work on GUB, Python will be required. No m-scripting or C++ necessary, beyond understanding [the C++ compilation model](http://david.rothlis.net/c/compilation_model/).

# Performance

- Having
`parfor`

functioning would speed code development and execution now that multicore architectures are widespread. See[here](http://octave.1599824.n4.nabble.com/Parfor-td4630575.html)and[here](http://stackoverflow.com/questions/24970519/how-to-use-parallel-for-loop-in-octave-or-scilab). Existing code from the[parallel](https://wiki.octave.org/Parallel_package)and[mpi](http://octave.sourceforge.net/mpi/index.html)packages could perhaps be adapted for this. - Develop a performance benchmark for Octave (interpreter, load/save, plotting, etc., but not simply tests of underlying libraries such as BLAS or LAPACK). This benchmark could be run periodically to make sure that changes during development do not introduce regressions in performance.

# Octave Package management

[Packages](https://wiki.octave.org/Packages) are extensions for Octave. To get those extension to work with Octave, there is a single function, [ pkg](https://www.octave.org/doc/interpreter/XREFpkg.html), which does pretty much everything.
This function has a few limitations which are hard to implement with the current codebase, and will most likely require a full rewrite.
A major step forward for a rewritten package manager is the

["packajoozle" project](https://github.com/apjanke/octave-packajoozle/)by Andrew Janke.

The planned improvements are:

- install and update from repositories (hg and git)
- automatic handling of dependencies
- easily load, update or check specific package versions
- management of tests and demos in C++ sources of packages
- more flexibility on dependencies, e.g., dependent on specific Octave build options or being dependent in one of multiple packages
- support for multiple version packages
- support for multiple Octave installs
- support for system-wide and user installed packages
- testing packages (
`pkg test <package-name>`

) - improved metadata acquisition (
`pkg list -forge`

) from[https://octave.sourceforge.io/](https://octave.sourceforge.io/)

- create a system that allows packages to deprecate functions as in core. Possibilities are:
- get pkg to accept a deprecated directory inside the package and add it to the search path. Functions in those directories would have to be treated the same as the ones inside the core deprecated
- PKG_ADD can be used to hack this. Package developers would still have to actually write the warnings on the function code but this would allow to have the functions in a separate directory so they don't foget to remove them on the next release
- the package developer can also use something like Make to create a
*normal*package from something that actually had a more complex structure, inclusive deprecated directories

- get pkg to resolve dependencies automatically by downloading and installing them too
- allow to download and install multiple versions of the same package
- make the package just a bit more verbose by default (specifics?)
- make pkg a little more like apt-get (what specific features of apt-get is this referring to?)
- make pkg support more than one src directory
- subdirectories with makefiles and top level make command of: cd <subdir> && ${MAKE}... ok as a substitute?

- make pkg able to supply extra configure and make flags, useful for distributions, including -j for make (pkg now passes --jobs=N automatically, CFLAGS and CXXFLAGS environment variables are already respected, what's missing?)

The main objective of this project is to make [ pkg](https://www.octave.org/doc/interpreter/XREFpkg.html) more user friendly and to make it a tool to foster third party participation in Octave.
However, the current

[also performs some maintenance functions which it probably should not. Instead a package for developers should be created with such tools. To do this enhancement effectively, a refactoring of the current](https://www.octave.org/doc/interpreter/XREFpkg.html)

`pkg`

`pkg`

code will be needed (see ["packajoozle" project](https://github.com/apjanke/octave-packajoozle/)).

Many of these problems have been solved in other languages.
Familiarity with how other languages handle this problem will be useful to come up with elegant solutions.
In some cases, there are standards to follow.
For example, there are specifications published by freedesktop.org about where files should go ([base directory spec](http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html)), and Windows seems to have its own standards.
See bugs [#36477](https://savannah.gnu.org/bugs/?36477) and [#40444](https://savannah.gnu.org/bugs/?40444) for more details.

In addition, package names may start to collide very easily.
One horrible way to work around this by is choosing increasingly complex package names that give no hint on the package purpose.
An option is providing an "Authority" category like Perl 6 does.
Nested packages is also an easy way to provide packages for specialized subjects (think `image::morphology`

).
A new [ pkg](https://www.octave.org/doc/interpreter/XREFpkg.html) would think all this things now, or allow their implementation at a later time.
Read the

[unfinished plan](https://wiki.octave.org/OEP:pkg)for more details.

# Preferences

Octave has several functions for managing user preferences. Many function use persistent variables instead of relying upon the preference features.

- The function
`edit ()`

contains a persistent structure used as its personal set of preferences. These can all be moved to the user preference group for the editor.- "EDITOR"
- "HOME"
- "AUTHOR"
- "EMAIL"
- "LICENSE"
- "MODE"
- "EDITINPLACE"

- The
`savepath ()`

function modifies the startup script (rcfile),`~/.octaverc`

and inserts commands to allow the next session to begin with the same path. Instead user preference can be created for startup items and a preference for the user specified path can be added. Perhaps two path preferences should be used. One for the elements that should precede the core path and those that should follow. A start up directory preference might also be added to allow the user to specify where Octave should begin the next session.- "PREPATH"
- "POSTPATH"
- "STARTUPDIR"

- A preference group for plotting can also be added. A preference for the default terminal would be useful for those who want to override the default. Preferences for the default
`graphicstoolkit`

can also be added.- GNUPLOTTERM
- GRAPHICSTOOLKIT

- A preference group for printing can include preferences for the default printer, the ghostscript command, and possibly other parameters like orientation, and resolution.
- PRINTER
- GHOSTSCRIPTCOMMAND
- ORIENTATION
- RESOLUTION

- Searching the m-files for use of
`persistent`

should turn up other opportunities to use preferences.

# Profiler Enhancement

Octave has a built in [ profiler](https://www.octave.org/doc/interpreter/XREFprofile.html) thanks to a

[successful 2011 GSOC project by Daniel Kraft](https://wiki.octave.org/Summer_of_Code#GSoC_2011). But it really could use:

- Better granularity:
- It aggregates all calls to a function within at each level of the code, providing no way to know which call to a function might be more 'expensive'.
- It aggregates all non-function-call overhead into time spent on 'self' without further detail to the user on what might be causing that overhead.
- Associating time spent/function call count to line number would be a big plus.

- A better interface.
- The current CLI tool is good at determining time spent on function calls, providing both a summary output with
and an interactive prompt that lets you dive down levels in the code with`profshow`

. But this suffers from the aggregation limits mentioned above.`profexplore`

- The profiler was written before the stable Octave GUI was released with Octave 4.0. This GUI now includes a built in editor with hooks to the interpreter. Better integration of the profiler output to the Octave GUI would be a significant functional improvement. (Current GUI integration is limited to an indicator light that shows the profiler is running.)
- Enhancements are not strictly limited to using the current Octave GUI/Editor. Whatever helps users connect execution time to code location would be good.

- The current CLI tool is good at determining time spent on function calls, providing both a summary output with

# Bugs

There are always bugs to fix. The [bug tracker](https://savannah.gnu.org/bugs/?group=octave) is a good place to find tasks needing a hand. See also [Short projects#Bugs](https://wiki.octave.org/Short_projects#Bugs).

# Matlab compatibility

## Missing functions

There are certain functions present in MATLAB known to be missing in Octave.

One list is provided on the source for function __unimplemented.m__, subfunction missing_functions; it can be edited in the Octave GUI or browsed at [[2]](http://hg.savannah.gnu.org/hgweb/octave/file/default/scripts/help/__unimplemented__.m#l547).

Lists are also kept for [several packages](https://wiki.octave.org/Category:Missing_functions).

It is also possible to look at existing [FOSS](http://en.wikipedia.org/wiki/Free_and_open-source_software) implementations, from FreeMat and Scilab (for more closely compatible languages) to R or Scipy or Julia (for less compatible versions). Obviously, it is NOT OK to look at the Matlab implementation since this is not [free software](http://en.wikipedia.org/wiki/Free_software)!

## Functions under different name

Many Octave Forge functions perform the same as functions from matlab packages. However, they often exist under a different name or have incompatible API's. Often fixing this is a matter of changing their names, swap the order of their input arguments. At least, a list of this functions would be helpful.
