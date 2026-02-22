# GNU Project — Project Ideas

**Source:** https://www.gnu.org/s/soc-projects/ideas.html
**Scraped:** 2026-02-22T23:28:47.632105

---

# Summer of Code projects for GNU

This page has the project suggestions for GNU's participation in
[Google Summer of Code 2026](https://developers.google.com/open-source/gsoc/).

**STUDENTS - BEFORE YOU SUBMIT YOUR PROJECT PROPOSAL**:

Please read the [GNU Project's guidelines
for Summer of Code projects](https://www.gnu.org/guidelines.html).

Most importantly, please make sure you include all the information
requested. If you have questions, please ask [summer-of-code@gnu.org](mailto:summer-of-code@gnu.org) (list
info [here](http://lists.gnu.org/mailman/listinfo/summer-of-code/)).

**Please note that you are not bound to use these ideas, you can
propose a new project. It is a good idea to find a mentor and
discuss the idea before submit it.**

## Projects and Ideas

GNU is a large and complex project, and thus is subdivided into packages, which are relatively independent projetcts. In Summer of Code, GNU acts as an umbrella organization for its packages. The ideas here are grouped by package. Many packages have more than one suggestion, or even their own ideas page.

[GnuCOBOL](https://www.gnu.org/software/gnucobol)

GnuCOBOL is a free, modern COBOL compiler. It implements a substantial part of the COBOL 85, X/Open COBOL and newer ISO COBOL standards (2002, 2014, 2023), as well as many extensions included in other COBOL compilers (IBM COBOL, MicroFocus COBOL, ACUCOBOL-GT and others).

GnuCOBOL translates COBOL into C and internally compiles the translated code using a native C compiler, therefore works on nearly every platform.

GnuCOBOL maintains a list of ideas here:
[https://gnucobol.sourceforge.io/gsoc.html](https://gnucobol.sourceforge.io/gsoc.html)

**Project site:**[https://www.gnu.org/s/gnucobol](https://www.gnu.org/s/gnucobol)**Contact:**[gnucobol-dev@gnu.org](https://www.gnu.org/gnucobol-dev@gnu.org).

[GNU Aris](/ideas/gnu-project-av/software-aris)

GNU Aris is a logical proof program that supports propositional and predicate logic, as well as Boolean algebra and arithmetical logic, in the form of abstract sequences.

A logical proof program can prove mathematical statements by using strict reasoning steps, based on axioms and rewrite rules. GNU Aris supports manual creation of such proofs and it can verify if a proof is correct according to the axioms and rewrite rules. Therefore, it can give good support for undergraduate math courses like logic or abstract algebra.

**Project site:**[https://www.gnu.org/s/aris](/ideas/gnu-project-av/s-aris)**Contact:**[bug-aris@gnu.org](https://www.gnu.org/bug-aris@gnu.org).

#### UI and Feature Enhancements

GNU Aris is a logical proof program that helps students write exact mathematical proofs in propositional and quantified logic. It has been successfully applied in education at university level. Adressing the requests given by university students may significantly improve its user-friendliness:

- More comprehensible and detailed error messages,
- a feature to zoom for smaller device displays,
- an option to change the user language,
- an option to highlight, copy and paste inputs,
- an option to change the type of input between premise and conclusion after inserting a new line,
- an operator for exclusive disjunction,
- an option to use the rule of inference for a proof by contrapositive,
- eventually, automatic updates on the feedback for the correctness of statements after changing faulty inputs,
- a fix for
[https://github.com/kovzol/aris/issues/24](https://github.com/kovzol/aris/issues/24). - Expected outcomes: A new version of GNU Aris that implements most of the improvements, being available on all major platforms and HTML/WebAssembly.
- Skills required/preferred: Good knowledge in C/C++, Qt, QML, cmake, preferable knowledge of building/debugging HTML/WebAssembly applications via Qt in C++
- Project size: 175 hours
**Reference links:**[https://matek.hu/zoltan/thedu24/](https://matek.hu/zoltan/thedu24/)

[GNU XaoS](https://github.com/xaos-project)

XaoS (pronounced chaos) is a realtime interactive fractal zoomer.

#### Develop a mobile phone user interface for GNU XaoS

GNU XaoS is a technology leader, free fractal zoomer and morpher program, written in C++. It is available on all major platforms, and HTML/WebAssembly. We, the XaoS Contributors, would like to extend its user interface to offer better user experience on mobile phones.

- Some planned new features include:
- stable, bug-free working on Android and iPhones,
- option to join the user community and share the own created fractals and download other users' contributions inside the application, via an own developed protocol.

- Expected outcomes: A new version of XaoS that implements the above mentioned features.
**Skills required/preferred:**Good knowledge in C/C++, Qt, QML, cmake, preferable knowledge of building/debugging HTML/WebAssembly applications via Qt in C++, preferable knowledge of creating/building/deploying mobile applications (via Qt)- Project size: 350 hours
**Contact:**[https://github.com/xaos-project](https://github.com/xaos-project).**Reference links:**

[Libcdio](https://github.com/libcdio)

The libcdio package contains a library for CD-ROM and CD image access. Applications wishing to be oblivious of the OS- and device-dependent properties of a CD-ROM or of the specific details of various CD-image formats may benefit from using this library.

A library for working with ISO-9660 filesystems, libiso9660, is included. A generic interface for issuing MMC (multimedia commands) is also part of the libcdio library.

Also included is a library for working with ISO-9660 filesystems.

The CD-DA error/jitter correction library from cdparanoia is included as a separate library licensed under GPL v2.

#### Port the library to Rust

**Project idea:**Port one or more parts of this code to Rust. A part could be*libiso9660*, ISO-9660 file reading, or*cd-paranoia*CD error/jitter correction.**Project site:**[https://github.com/libcdio](https://github.com/libcdio)**Contact:**[libcdio-devel@gnu.org](mailto:libcdio-devel@gnu.org).

### Other links:

[Google SoC Page](https://summerofcode.withgoogle.com).
