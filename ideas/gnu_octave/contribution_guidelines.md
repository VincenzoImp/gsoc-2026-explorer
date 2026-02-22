# Contribution guidelines

**Parent:** GNU Octave — Project Ideas
**Source:** https://wiki.octave.org/Contribution_guidelines
**Scraped:** 2026-02-22T23:28:47.624203

---

# Contribute

[Contribution guidelines](https://wiki.octave.org/wiki/index.php?title=Contribution_guidelines&redirect=no))

[Jump to navigation](https://wiki.octave.org#mw-head)

[Jump to search](https://wiki.octave.org#searchInput)

## Bug reports and patch submission

- The best way to contribute patches is to create a Mercurial changeset.
- Learn how to use
[Mercurial](https://wiki.octave.org/Mercurial). [Commit message guidelines](https://wiki.octave.org/Commit_message_guidelines).

- Learn how to use

### Contributor Agreement

By submitting patches to this project, you agree to the following conditions:

- Your contribution will be released under the terms of the GNU GPL, version 3 or any later version.

- Your contribution must be an independent work or derived from code that may be released under the terms of the GPL.
**Under no circumstances may it be based on code from Matlab or other non-free code that you may have access to view**.

- In the Octave source code, all files are marked with a copyright statement that says "Copyright (C) YYYY-YYYY The Octave Project Developers". This copyright notice is used to ease the burden of maintaining copyright information in the source files, not to diminish or remove credit for contributions. Detailed information about what changes have been made and who has made them is maintained in the revision history of the Octave sources.

- If you wish, you will be credited as a contributor in the Octave documentation.

## Building from development sources

*See*[Building](https://wiki.octave.org/Building).

## Coding style

Apart from C++ and Octave language (m-files), Octave's sources include files written in C, Fortran, M4, Perl, Unix shell, AWK, Texinfo, and TeX. There are not many rules to follow when using these other languages; some of them are summarized below. In any case, the golden rule is: if you modify a source file, try to follow any conventions you can detect in the file or other similar files.

### C/C++ guide

*See*[C++ style guide](https://wiki.octave.org/C%2B%2B_style_guide). For C, you should follow all C++ rules that can apply.

### Octave guide

*See*[Octave style guide](https://wiki.octave.org/Octave_style_guide).

### Help text style

### Fortran guide

If you modify a Fortran file, you should stay within Fortran 77 with
common extensions like `END DO`

. Currently, we want ensure that
it is possible to compile all sources with the gfortran compiler, without
special flags if possible. This usually means that non-legacy compilers
also accept the sources.

### M4 guide

The M4 macro language is mainly used for Autoconf configuration files.
You should follow normal M4 rules when contributing to these files.
Some M4 files come from external source, namely the
[Autoconf archive](https://www.gnu.org/software/autoconf-archive/).

### Wiki guide

- Please try to fit a new page into the already existing category tree.
- If you have to create a new category, choose the name and place wisely (try to stay close to Wikipedia's categorization scheme).
- Instead of creating a new page and redirect it to another for link aliases, choose piped links instead. See
[here](https://www.mediawiki.org/wiki/Help:Links)for more infos about piped links. - The one and only root category is
[Category:Contents](https://wiki.octave.org/Category:Contents). All other categories have to point to it (over one or more subcategories). - Start a new page title with a capital letter, the rest is written in lower case (except for names, cities, etc.).
