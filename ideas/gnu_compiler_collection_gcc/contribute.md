# Contributing to GCC

**Parent:** GNU Compiler Collection (GCC) — Project Ideas
**Source:** http://gcc.gnu.org/contribute.html
**Scraped:** 2026-02-22T23:28:47.609212

---

We strongly encourage contributions in the form of features, new or improved optimizations, bug fixes, documentation updates, web page improvements, etc....

If you're new to GCC, please also see
the [Getting Started](https://gcc.gnu.org/wiki/GettingStarted)
section of the GCC Wiki.

There are certain legal requirements and style issues which contributions must meet:

[Legal Prerequisites](http://gcc.gnu.org#legal)[Coding Standards](http://gcc.gnu.org#standards)[Testing Patches](http://gcc.gnu.org#testing)[Documentation Changes](http://gcc.gnu.org#docchanges)[Web Site Changes](http://gcc.gnu.org#webchanges)[Submitting Patches](http://gcc.gnu.org#patches)[Announcing Changes (to our Users)](http://gcc.gnu.org#announce)

Before we can incorporate significant contributions, certain legal requirements must be met.

The FSF prefers that a contributor files a copyright assignment for
large contributions.
[See
some documentation by the FSF](https://www.gnu.org/prep/maintain/maintain.html#Legal-Matters) for details and contact us (either via
the [gcc@gcc.gnu.org](mailto:gcc@gcc.gnu.org) list or the
GCC maintainer that is taking care of your contributions) to obtain
the relevant forms. The most common forms are an assignment for a
specific change, an assignment for all future changes, and an employer
disclaimer, if an employer or school owns work created by the developer.
It's a good idea to send
[assign@gnu.org](mailto:assign@gnu.org) a copy of
your request.

Alternatively, a contributor can certify the
[Developer Certificate of Origin](https://developercertificate.org)
for their contribution by adding
the [ Signed-off-by:](http://gcc.gnu.org/dco.html) tag to their submission.
Contributors with

We can accept small changes without copyright assignment or DCO certification.

All contributions must conform to the [GNU Coding Standards](https://www.gnu.org/prep/standards/).
There are also some [additional coding
conventions for GCC](http://gcc.gnu.org/codingconventions.html); these include documentation and testsuite
requirements as well as requirements on code formatting.

Submissions which do not conform to the standards will be returned
with a request to address any such problems. To help with the
preparation of patches you can use the script [
contrib/check_GNU_style.sh](https://gcc.gnu.org/git/?p=gcc.git;a=blob;f=contrib/check_GNU_style.sh).

All patches must be thoroughly tested. We encourage you to test
changes with as many host and target combinations as is practical. In
addition to using real hardware, you can
[use simulators](http://gcc.gnu.org/simtest-howto.html).

Much of GCC's code is used only by some targets, or used in quite different ways by different targets. When choosing targets to test a patch with, make sure that your selections exercise all aspects of the code you are changing.

You will of course have tested that your change does what you
expected it to do: fix a bug, improve an optimization, add a new
feature. Where possible you should automate these
tests and add them to GCC's testsuite. You must also perform
regression tests to ensure that your patch does not break anything
else. Typically, this means comparing post-patch test results to
pre-patch results by testing twice or comparing with recent posts to
the [gcc-testresults
list](https://gcc.gnu.org/ml/gcc-testresults/).

If your change is to code that is not in a front end, or is to the C or C++ front ends, you must perform a complete build of GCC and the runtime libraries included with it, on at least one target. You must bootstrap all default languages, not just C and C++, and run all testsuites. For a normal native configuration, running

make bootstrap make -k check

from the top level of the GCC build tree (**not** the
`gcc`

subdirectory) will accomplish this.

If your change is to the C++ front end, you need to run the C++ testsuite in all standard conformance levels. For a normal native configuration, running

make -C gcc -k check-c++-all

from the top level of the GCC build tree will accomplish this.

If your change is to a front end other than the C or C++ front end,
or a runtime library other than `libgcc`

, you need to verify
only that the runtime library for that language still builds and the
tests for that language have not regressed. (Most languages have
tests stored both in the `gcc`

subdirectory, and in the
directory for the runtime library.) You need not bootstrap, or test
other languages, since there is no way you could have affected
them.

Since the Ada front end is written in Ada, if you change it you must perform a complete bootstrap; however, running other language testsuites is not necessary.

In all cases you must test exactly the change that you intend to submit. The tree where you perform this test should not have any other changes applied.

Documentation changes do not require a new bootstrap (a working
bootstrap is necessary to get the build environment correct), but you
must perform `make info`

and `make dvi`

and correct
any errors. You should investigate complaints about overfull or
underfull hboxes from `make dvi`

, as these can be the only
indication of serious markup problems, but do not feel obliged to
eliminate them all.

Changes to the web site must
[validate](https://validator.w3.org) as HTML 5. To
validate your changes, use the "upload file" mode of the
validator.

Please mark patches with the tag [wwwdocs] in the subject line.

More [about our web pages](http://gcc.gnu.org/about.html#git).

Every patch must have several pieces of information, *before* we
can properly evaluate it:

- A description of the problem/bug and how your patch addresses it.
-
For new features a description of the feature and your implementation.
For bugs a description of what was wrong with the existing code, and a
reference to any previous bug report (in the
[GCC bug tracker](https://gcc.gnu.org/bugzilla/)) and any existing testcases for the problem in the GCC testsuite. - Testcases
-
If you cannot follow the recommendations of the
[GCC coding conventions](http://gcc.gnu.org/codingconventions.html)about testcases, you should include a justification for why adequate testcases cannot be added. - ChangeLog
-
A ChangeLog entry as plaintext; see the
[GCC coding conventions](http://gcc.gnu.org/codingconventions.html#ChangeLogs)and[GNU Coding Standards](http://www.gnu.org/prep/standards_toc.html)for further information.

The`git gcc-commit-mklog`

command from`gcc-git-customization.sh`

(see[here](http://gcc.gnu.org/gitwrite.html)) automates a lot of ChangeLog generation. - Bootstrapping and testing
-
State the host and target combinations you used to do
[proper testing](http://gcc.gnu.org#testing)as described above, and the results of your testing. - The patch itself
-
The patch should include everything you are changing (including
regenerated files which should be noted in the ChangeLog e.g.
"
`* configure: Regenerate.`

").

Don't mix together changes made for different reasons. Send them
*individually*. Ideally, each change you send should be
impossible to subdivide into parts that we might want to consider
separately, because each of its parts gets its motivation from the
other parts. In particular, changes to code formatting to conform to
coding standards are best not mixed with substantive changes, because
that makes it difficult to see what the real changes are. (In the
case of a very large reorganization of code, it may make sense to
separate changes even further to make it clearer what has changed; for
example, by first sending structural changes that make subsequent
changes easier but do not change GCC's behavior, then new code, then
the changes that actually make use of the new code and change GCC's
behavior.)

We prefer patches posted as plain text or as MIME parts of type
`text/x-patch`

or `text/plain`

.
It is strongly discouraged to post patches as MIME parts of type
`application/`

*whatever*, disposition
`attachment`

or encoded as `base64`

or
`quoted-printable`

.

If the patch is too big or too mechanical, posting it gzipped or
bzip2ed and uuencoded or encoded as a `base64`

MIME part is
acceptable, as long as the ChangeLog is still posted as plain text.

When you have all these pieces, bundle them up in a mail message and
send it to [the appropriate mailing list(s)](http://gcc.gnu.org/lists.html).
(Patches will go to one or more lists depending on what you are
changing.) For further information on our source repository, see
the [Anonymous read-only Git access](http://gcc.gnu.org/git.html) and [Read-write Git access](http://gcc.gnu.org/gitwrite.html) pages.

Many mail clients break patches pasted into the message body, primarily by
wrapping long lines. See
[
the Linux kernel documentation](https://www.kernel.org/doc/html/latest/process/email-clients.html) for ways to work around this.

(Everything listed here still applies if you can check in the patch
without further approval under the [GCC write access policies](http://gcc.gnu.org/gitwrite.html#policies), except that
diffs representing new files may be omitted, especially if large, since they
can be accessed directly from the repository.)

Your contribution e-mail subject line will become the first line of the commit message for your patch.

A high-quality e-mail subject line for a contribution contains the following elements:

- A classifier
- Component tags
- An optional series identifier
- A brief summary
- An optional bug number

The entire line (excluding the classifier) should not exceed 75 characters.

The classifier identifies the type of contribution, for example a
patch, an RFC (request for comments) or a committed patch (where
approval is not necessary). The classifier should be written in upper
case and surrounded with square brackets. This is the only component
of the e-mail subject line that will not appear in the commit itself.
The classifier may optionally contain a version number (v*N*) and
a series marker (*N/M*). Examples are:

`[PATCH]`

- a single patch`[PATCH v2]`

- the second version of a single patch`[PATCH 3/7]`

- the third patch in a series of seven patches`[RFC]`

- a point of discussion, may contain a patch`[COMMITTED]`

- a patch that has already been committed.

A component tag is a short identifier that identifies the part of the compiler being modified. This highlights to the relevant maintainers that the patch may need their attention. Multiple components may be listed if necessary. Each component tag should be followed by a colon. For example,

`libstdc++:`

`combine:`

`vax: testsuite:`


Some large components may be subdivided into sub-components. If
the subcomponent name is not distinct in its own right, you can use the
form *component/sub-component:*.

The series identifier is optional and is only relevant if a number of
patches are needed in order to effect an overall change. It should be
a *short* string that identifies the series (it is common to all
patches) and should be followed by a single dash surrounded by white
space.

The brief summary encapsulates in a few words the intent of the
change. For example: `cleanup check_field_decls`

.
Although, very short, the summary should be distinct so that it will
not be confused with other patches.

If your patch relates a bug in the compiler for which there is an
existing PR number the bug number should be stated. Use the
short-form variant `[PR`

without the Bugzilla
component identifier and with no space between 'PR' and the number.
The body of the commit message should still contain the full form
(*nnnnn*]`PR <component>/`

) within the body of
the commit message so that Bugzilla will correctly notice the
commit. If your patch relates to two bugs, then write
*nnnnn*`[PR`

. For multiple
bugs, just cite the most relevant one in the summary and use an
ellipsis instead of the second, or subsequent PR numbers; list all the
related PRs in the body of the commit message in the normal way.*nnnnn*, PR*mmmmm*]

It is not necessary to cite bugs that are closed as duplicates of another unless there is something specific to that report that is not covered by the parent bug.

Some large patch sets benefit from an introductory e-mail that
provides more context for the patch series and describes how the
patches have been broken up to provide for review. The convention is
that such messages should follow the same format as described above,
but the patch number should be set to zero, for example: ```
[PATCH
0/7]
```

. Remember that the introductory message will not be
committed with the patches themselves, so it should not contain any
important information that is not also covered in the individual
patches. If you send a summary e-mail with a series it is a good idea
to send the patches as follow-ups (essentially replies) to your
initial message so that mail software can group the messages
together.

If you submit a new version of a patch series, then you should
start a new email thread (don't reply to the original patch series).
This avoids email threads becoming confused between discussions of the
first and subsequent revisions of the patch set. Your cover letter
(0/*nnn*) should explain clearly what has been changed between
the two patch series. Also state if some of the patches are unchanged
between revisions; this saves maintainers having to re-review the
patches they might have already reviewed in an earlier version. The
individual patch messages should be as you expect them to be
committed. It is a good idea to send a final follow-up message to the
original thread indicating that a new version has been submitted.

Here are some complete examples, based on real commits to GCC.

`[COMMITTED] libstdc++: Fix freestanding build [PR92376]`

`[PATCH 1/6] analyzer: Fix tests for UNKNOWN_LOCATION`

`[RFC] doc: Note that some warnings depend on optimizations [PR92757]`

`[COMMITTED] c++: coroutines - Initial implementation`

`[PATCH v2] wwwdocs: E-mail subject lines for contributions`


`git format-patch`

tool generates an email in the desired
format, with the commit subject line as the email subject line
with `[PATCH]`

prepended. You can send the resulting file as an
email by itself (perhaps with `git send-email`

) or as an attachment
to another email.
If you do not receive a response to a patch that you have submitted within two weeks or so, it may be a good idea to chase it by sending a follow-up e-mail to the same list(s). Patches can occasionally fall through the cracks. Please be sure to include a brief summary of the patch and the URL of the entry in the mailing list archive of the original submission.

If you do not have write access and a patch of yours has been approved, but not committed, please advise the approver of that fact. You may want to point out lack of write access in your initial submission, too.

Everything that requires a user to edit their Makefiles or source code is a good candidate for being mentioned in the release notes.

Larger accomplishments, either as part of a specific project, or long term commitment, merit mention on the front page. Examples include projects like tree-ssa, new back ends, major advances in optimization or standards compliance.

The gcc-announce mailing list serves to announce new releases and changes like front ends or back ends being dropped.

For questions related to the use of GCC,
please consult these web pages and the
[GCC manuals](https://gcc.gnu.org/onlinedocs/). If that fails,
the [gcc-help@gcc.gnu.org](mailto:gcc-help@gcc.gnu.org)
mailing list might help.
Comments on these web pages and the development of GCC are welcome on our
developer list at [gcc@gcc.gnu.org](mailto:gcc@gcc.gnu.org).
All of [our lists](https://gcc.gnu.org/lists.html)
have public archives.

Copyright (C)
[Free Software Foundation, Inc.](https://www.fsf.org)
Verbatim copying and distribution of this entire article is
permitted in any medium, provided this notice is preserved.

These pages are
[maintained by the GCC team](https://gcc.gnu.org/about.html).
Last modified 2025-07-14.
