# short projects

**Parent:** GNU Octave — Project Ideas
**Source:** https://wiki.octave.org/Short_projects
**Scraped:** 2026-02-22T23:28:47.624017

---

# Short projects

[Jump to navigation](https://wiki.octave.org#mw-head)

[Jump to search](https://wiki.octave.org#searchInput)

*This is a collection of small projects to start contributing to Octave. Projects of long duration are listed in the*[Projects](https://wiki.octave.org/Projects)page.

[Developer FAQ](https://wiki.octave.org/Developer_FAQ).

## Review and fix existing bugs

- Review bugs that catch your interest on the
[Octave bug tracker](https://savannah.gnu.org/bugs/?group=octave)on GNU Savannah.- A modern interface to the Octave bug tracker is given by
[SavannahAPI](https://octave.space/savannah/).

- A modern interface to the Octave bug tracker is given by
- Discuss with the developers there how to fix that bug or
[upload a patch there](https://wiki.octave.org/Mercurial). - Some bugs have already patches attached.
- Help testing those patches.
- Help updating outdated patches to the latest development version (this requires some
[Mercurial](https://wiki.octave.org/Mercurial)knowledge).


## Implement missing Matlab functions

- Use the
[Savannah patch tracker](https://savannah.gnu.org/patch/?func=additem&group=octave)for submissions unrelated to an existing bug.

## Test Octave functions for proper input handling

- Many functions either do insufficient input checking or the input requirements have changed over time.
- Contributors can try to break Octave function behavior with different types of input, and document the results.
- Users can check
*expected behavior*according to the Octave help and, if applicable, expected compatible behavior according to[public facing Matlab documentation](https://www.mathworks.com/help/matlab/). - Inputs to test can be:
- different numeric types - double, single, integer.
- non-numeric types - logical, string, cell, struct
- different input shapes - scalar, row/column vectors, 2D, 3D, & nD arrays, zero size arrays ([], 1x0, and 1x3x0 are all empty but may require different handling).
- char/string parameters: different case handling, partial matching behavior, invalid/nonsense parameters.

- For the input items above, does function behave acceptably? Are numerical or graphical outputs as expected? Is output consistent? Is any error message intelligible/meaningful to the user?
- Optionally the behavior above can be tested against Matlab function output if it is available. If needed but not available, tests can be submitted to other developers for output checking.
- Note 1: There is much undocumented Matlab behavior. Because this has the possibility of changing with little notice, fixing incompatibilities related to such undocumented behavior is considered on a case-by-case basis by the developer team. Documentation of such cases is always beneficial, however.
- Note 2: Only Matlab public documentation and function output may be compared.
*Internal Matlab code, even if available, should never even be looked at by a contributor. Contributions will be discarded if it is determined such action occurred.*

- Contributors can submit bug reports to the
[Octave Bug Tracker](https://savannah.gnu.org/bugs/?group=octave)documenting their findings. - An example can be see in bug
[#64078](https://savannah.gnu.org/bugs/?64078)comment #10 of looking through the /plot/draw functions for how they handle integer and logical inputs to numeric fields.



## Write Built-In Self Tests (BISTs)

Writing BISTs improves Octave's regression testing and ensures that we don't break anything when we add new features.

[BIST for C++ functions](https://wiki.octave.org/Add_BIST_tests_for_octave_functions_written_in_C%2B%2B)[BIST for m-files](https://wiki.octave.org/BIST_for_m-files). See also[Projects#Tests](https://wiki.octave.org/Projects#Tests).

## Work on Octave packages

- Take a look at
[https://gnu-octave.github.io/packages/](https://gnu-octave.github.io/packages/)if you would like to work on some package there.

## Easy Closes

Below is a non exhaustive list of bugs which should be looked at and appear to be easy. Completed scrub using 6.1 as non expert. Status column provides notes from last review to facilitate addressing each bug. (Reviewing and updating status of items in this list as well as adding new ones are themselves good beginner tasks.)

Notes:

- The last full scrub came from hardy for v4.2
- Suspect many java bugs could be closed.
- Appears plotting bugs have been fixed, but not have been reviewed for 5 years.
- Did not include most documentation bugs.
- Experts: rik5, nrjank, etc. will be able to find significantly more to close.

| bug | bug title | status |
|---|---|---|
|

[#40357](https://savannah.gnu.org/bugs/?40357)[#48088](https://savannah.gnu.org/bugs/?48088)[#49886](https://savannah.gnu.org/bugs/?49886)[#42691](https://savannah.gnu.org/bugs/?42691)was first solved. That bug was closed as fixed in August 2021, so supposedly this one should now be easier manageable. nrjank marked as Needs Info to determine if desired output is just adding a warning, or also matching matlab output.[#49360](https://savannah.gnu.org/bugs/?49360)[#53214](https://savannah.gnu.org/bugs/?53214)[#54437](https://savannah.gnu.org/bugs/?54437)[#55065](https://savannah.gnu.org/bugs/?55065)[#56208](https://savannah.gnu.org/bugs/?56208)[#57352](https://savannah.gnu.org/bugs/?57352)[#58530](https://savannah.gnu.org/bugs/?58530)The equivalent suggestions for patches.

| patch | patch title | status |
|---|

A list of patch reports with attachments not marked "Done or Cancelled" can be viewed in the SavannaAPI, [sorted by oldest first](https://octave.space/savannah/api.php?Action=get&Format=HTMLCSS&OrderBy=SubmittedOn&OpenClosed=open&TrackerID=patch&AttachedFiles!=0&Category!=Forge,website&Status!=Done,Cancelled) or [sorted by "longest since last comment" first](https://octave.space/savannah/api.php?Action=get&Format=HTMLCSS&OrderBy=LastComment&OpenClosed=open&TrackerID=patch&AttachedFiles!=0&Category!=Forge,website&Status!=Done,Cancelled). While some of these older submissions may still be viable and just need a patch refresh to the current code base, many will have become out of date or rendered inapplicable due to code or function changes, and could be closed as 'Wont Fix'.
