# description

**Parent:** The ns-3 Network Simulator Project — Project Ideas
**Source:** https://www.nsnam.org/wiki/GSOC2024PatchRequirement
**Scraped:** 2026-02-22T23:28:47.555392

---

# GSOC2024PatchRequirement

[Jump to navigation](https://www.nsnam.org#mw-head)

[Jump to search](https://www.nsnam.org#searchInput)

[Main Page](https://www.nsnam.org/wiki/Main_Page) - [Roadmap](https://www.nsnam.org/wiki/Roadmap) - [Summer Projects](https://www.nsnam.org/wiki/Summer_Projects) - [Project Ideas](https://www.nsnam.org/wiki/Project_Ideas) - [Developer FAQ](https://www.nsnam.org/wiki/Developer_FAQ) - [Tools](https://www.nsnam.org/wiki/Tools) - [Related Projects](https://www.nsnam.org/wiki/Related_Projects)

[HOWTOs](https://www.nsnam.org/wiki/HOWTOs) - [Installation](https://www.nsnam.org/wiki/Installation) - [Troubleshooting](https://www.nsnam.org/wiki/Troubleshooting) - [User FAQ](https://www.nsnam.org/wiki/User_FAQ) - [Samples](https://www.nsnam.org/wiki/Category:Samples) - [Models](https://www.nsnam.org/wiki/Category:Models) - [Education](https://www.nsnam.org/wiki/Education) - [Contributed Code](https://www.nsnam.org/wiki/Contributed_Code) - [Papers](https://www.nsnam.org/wiki/Papers)

As part of their Google Summer of Code 2024 applications to ns-3, we require that applicants produce at least a small amount of code for ns-3. This will allow us to gauge your ability to dive into source code, understand it, make a modification, and proceed to build and verify if your modification works.

Applicants who have already contributed a patch to ns-3 should check with the org admins whether the patch requirement can be satisfied by this prior code. If you have code posted somewhere else (GitHub, for example, or a class project page) that you feel is a good indicator of your ability to write ns-3 code, please point us to the URL.

For everyone else, the following is the process:

- Try to fix one of our
[good first issues](https://gitlab.com/nsnam/ns-3-dev/-/issues/?label_name%5B%5D=good%20first%20issue)by submitting a merge request[in the usual way](https://www.nsnam.org/docs/contributing/html/enhancements.html#submitting-merge-requests).**Note:**if there is already a fix pending for a given issue, one cannot duplicate the effort and submit a second request.


## Patch requirement

### Setting up the environment

Perform the following steps (you may want to review our [Installation guide](https://www.nsnam.org/docs/installation/html/index.html)).

- Download the ns-3-dev repository, or fork it or clone it from Git:

$: git clone[https://gitlab.com/nsnam/ns-3-dev.git]$: cd ns-3-dev $: git checkout -b patch-requirement origin/master

- Verify if you can build ns-3 and run the test suite:

$: ./ns3 configure --enable-examples --enable-tests $: ./ns3 build $: ./test.py

### Objective

Provide a fix for one of the [good first issues](https://gitlab.com/nsnam/ns-3-dev/-/issues/?label_name%5B%5D=good%20first%20issue).

### What to submit

A patch to ns-3-dev that accomplishes the objective. In your GSoC application, point us to a publicly available URL where you've hosted the patch (such as a "gist" on github.com, or a snippet on gitlab.com, for instance). You can also send a [patch](https://opensource.com/article/18/8/diffs-patches) to one of the org admins. If you need help with this step, contact one of the org admins for advice.

**Note:** Keep your solution private by pasting the link in your application PDF to Google, or sending a patch to an org admin, not posting it on the mailing list or submitting a GitLab.com merge request.

**Note:** You can share your patch with a GSoC mentor prior to the deadline, for initial feedback, if you have any doubt about it.
