# here

**Parent:** GNU Mailman — Project Ideas
**Source:** https://wiki.list.org/DEV
**Scraped:** 2026-02-22T23:28:47.588021

---

# Mailman Developer Resources

Thank you for contributing to Mailman! Please also see the [Mailman 3](https://wiki.list.org/Mailman3) release notes.

This year we will be applying to Google's [Summer of Code](https://summerofcode.withgoogle.com/). For information about Mailman's project ideas, click here: [Google Summer of Code 2023](https://wiki.list.org/DEV/Google%20Summer%20of%20Code%202023).


## How to get started

Please read the [git quickstart](https://wiki.list.org/DEV/HowToContributeGit) before doing anything else!

The [Setup instructions](https://wiki.list.org/DEV/SetupDevEnvironment) will guide you through the process of setting up all the projects so you can start developing.


## Contributing to Mailman, step 1: Git and Gitlab

Mailman 3's source code is published in [git](http://git-scm.com/). Project management is available on [Gitlab](https://gitlab.com/mailman/mailman). We switched from Bazaar on Launchpad on May 4th, 2015. Previous to that, we switched from Subversion on SourceForge on June 22, 2007.

**Please note:** Mailman 2.1 development continues to be hosted in Bazaar on [Launchpad](https://wiki.list.org/DEV/MailmanOnLaunchpad).

For now, the Mailman 3 branch on Launchpad will continue to be available in read-only mode.


## Contributing to Mailman, step 2: Contribution workflow process

A developer has an idea for an enhancement. They discuss it on the

[mailman-developers](http://mail.python.org/mailman/listinfo/mailman-developers)mailing list. For higher bandwidth discussions we can use irc (#mailman channel on[irc://libera.chat](irc://libera.chat)).Developers can clone our git repository, push their own branches, and submit

[a merge request](https://gitlab.com/mailman/mailman/merge_requests)against the official branches.- If the idea is appropriate for GNU Mailman and we decide to include it, FSF must get copyright assignments from the developer. See below. Do this early, since it can take some time to get all the paperwork to the FSF.


## Branch development guidelines

- Branches should be self-contained: Include documentation, a NEWS entry, and tests. Ideally, there would be one bug for every branch.
Be sure your branch does not provoke any regressions. Run

`tox`on your branch and be sure everything passes. Eventually, we'll enable CI on Gitlab so you'll know immediately whether your branch is ready for merging.- Branches should be as small as possible. The smaller the branch the easier it is to review.


## Contributing to Mailman, step 3: Copyright assignment

Mailman is a [GNU](http://www.gnu.org) project with the majority of the copyrights being held by the [Free Software Foundation](http://www.fsf.org). We therefore request that developers who contribute code, assign their copyrights in their Mailman contribution to the FSF. To do this, you first need to submit a [GNU copyright assignment request form](https://wiki.list.org/DEV/GNU%20copyright%20assignment%20request%20form) containing some basic information, and then fill out the form that the FSF sends you. Please [let us know](mailto:mailman-cabal@python.org) after you've sent the second form so that we can track your contribution. The FSF often doesn't tell us in a timely manner when such forms have been received.


## Version-specific resources

Mailman's developers are currently focused mostly on working towards the release of Mailman 3.0.

[Mailman 2.2](https://wiki.list.org/DEV/Mailman%202.2)-- 2.1 is the stable branch, now in maintenance mode[Mailman 3.0](https://wiki.list.org/DEV/Mailman%203.0)-- 3.0 is the stable Mailman 3 release


## Sprints


## Initiatives, proposals, ideas

[Modern Archiving](https://wiki.list.org/DEV/ModernArchiving)(currently[HyperKitty](https://wiki.list.org/HyperKitty)in[Mailman 3](https://wiki.list.org/DEV/Mailman%203.0))[REST Interface](https://wiki.list.org/DEV/REST%20Interface)(a part of[Mailman 3](https://wiki.list.org/DEV/Mailman%203.0)core)


## Suggestions

People seem to have trouble figuring out where to make suggestions or feature requests. There is a [suggestions](https://wiki.list.org/DEV/suggestions) page here, or you may wish to start a discussion on the [mailman-developers list](http://mail.python.org/mailman/listinfo/mailman-developers)


## Relevant RFCs, references, and standards

Here are some useful RFCs, references and drafts:

[A Highly Scalable Electronic Mail Service Using Open Systems (Christenson, et al)](http://www.jetcafe.org/npc/doc/mail_arch.html)[RFC 3834 - Recommendations for Automatic Responses to Electronic Mail](http://www.faqs.org/rfcs/rfc3834.html)[RFC 2034 - SMTP Service Extension for Returning Enhanced Error Codes](http://www.faqs.org/rfcs/rfc2034.html)[RFC 6530 - Overview and Framework for Internationalized Email](http://www.faqs.org/rfcs/rfc6530.html)

Best practices:

OWASP's

[password reset](https://www.owasp.org/index.php/Forgot_Password_Cheat_Sheet)recommendationsAnti-spam and anti-backscatter


A talk given at a UK Unix User Group meeting. Look for the 5th abstract on

[this page](http://www.ukuug.org/events/winter2005/programme.shtml).The inevitable

["...considered harmful" article](http://mayfirst.org/?q=node/180).- UK Joint Academic Network (JANet) provides network connectivity and services for UK
HE institutions has

[guidance to victims of backscatter](http://www.ja.net/services/csirt/advice/policies/collateral-spam.html)....and to system adminstrators

[Spam Bounces Considered Harmful](http://www.ja.net/services/csirt/threats/bounce.html).Mailman's own recommendations for

[controlling spam](https://wiki.list.org/SEC/Controlling%20spam)
