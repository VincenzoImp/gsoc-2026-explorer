# tag2upload

**Parent:** Debian — Project Ideas
**Source:** https://wiki.debian.org/tag2upload
**Scraped:** 2026-02-22T23:28:47.578103

---

[Translations](https://wiki.debian.org/DebianWiki/EditorGuide#translation): [English](https://wiki.debian.org/tag2upload) - [Português (Brasil)](https://wiki.debian.org/pt_BR/tag2upload)

tag2upload allows DDs and DMs to upload simply by using the [git-debpush](https://packages.debian.org/git-debpush) script to push a signed git tag.


## Uploading

Use the [git-debpush(1)](https://manpages.debian.org/trixie-backports/git-debpush/git-debpush.1.en.html) program.

This replaces the whole upload flow (except, if you're using `gbp pq` you must `gbp pq export`). NB `git debpush` immediately and unconditionally initiates the upload, so you should already have run all your tests and lints (eg, Salsa CI).

git-debpush in bookworm and trixie are new enough, but for the best user experience, use git-debpush version 14.x (currently in Debian testing and trixie-backports).

Most commonly-used git repository formats used in Debian are supported. For example, `gbp pq` is supported. See the "Quilt Mode Options" section in git-debpush(1).


## Not supported

- Uploads to NEW (even if only binary-NEW), because for those ftp.d.o currently demands maintainer-generated binaries.
pristine-tar: With a new upstream version, tag2upload will generate a fresh orig tarball with

`git archive`(via git-deborig). This is OK, but it may surprise some users.[1106071](https://bugs.debian.org/1106071).Uploads to

`security-master`. This is difficult:[862105](https://bugs.debian.org/862105).Uploads to backports where your workflow involves throwing away the changelog entries for previous backports. I.e. if you start fresh for each version from testing you backport. If you do something like

`git checkout debian/bookworm-backports && git merge debian/latest`and then resolve the`debian/changelog`merge conflict so as to preserve all entries, then it works ([1109584](https://bugs.debian.org/1109584)).NMUs that don't use the package maintainer's git repository, and git workflow, aren't likely to work well. Instead, use

`dgit`, which offers a[completely uniform git-based NMU workflow](https://manpages.debian.org/testing/dgit/dgit-nmu-simple.7.en.html).DELAYED/DEFERRED uploads (

[1123680](https://bugs.debian.org/1123680)).


## Important links

[git-debpush(1)](https://manpages.debian.org/bookworm-backports/git-debpush/git-debpush.1.en.html)- tag creation utility - the new way to upload[https://tag2upload.debian.org](https://tag2upload.debian.org)- Service status front page, with stats, logs, etc.[debian-tag2upload (at) lists.debian.org](https://lists.debian.org/debian-tag2upload/)- mailing list receiving build logs, notices, etc. (not for discussion!)[tag2upload(5)](https://manpages.debian.org/testing/git-debpush/tag2upload.5.en.html)- specification for the tag format


## Notes and advice

**Don't rewind your public branch, or delete already-pushed signed tags.**This is always poor practice, because the git objects you're deleting might already have been fetched by someone. It's worse with tag2upload, because the service is very quick, and will fetch your tag almost immediately. The service always publishes the signed tag on its public mailing list (the audit log), even if the upload fails. If the upload succeeds, those git objects become part of the package history on {browse,git}.dgit.debian.org, leaving a permanent discrepancy.If you make a mistake, simply

**bump the version**(adding a new changelog stanza). Integers are plentiful.**Discrepancies between git, and the implied source package**are not allowed. It's a fundamental design principle of the system that the source package and git view of the package are identical. For example,`debian/source/local-options`must be removed, or (if appropriate) renamed to`debian/source/options`. "Orig" tarballs must correspond to git: they must be generated from git (eg with`git archive`or`git deborig`), or imported into your maintainer branch (eg with`gbp import-orig`)., and their effects mustn't be visible in any existing orig tarballs. If upstream uses them for anything important, you must reproduce their effect in`.gitattributes`will be ignored`debian/rules`and/or a Debian-specific patch. See[GITATTRIBUTES in dgit(7)](https://manpages.debian.org/testing/dgit/dgit.7.en.html#GITATTRIBUTES)and[#1079434](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1079434#20)for more information, including rationale.**If you see "History contains tainted commit"**: This can occur if you get a REJECT from ftp-master NEW processing. In this circumstance, the commits you debpush'd are marked as tainted, because the REJECT may have been due to the files being legally dangerous for Debian to distribute. You can tell that this is what is going on because the tag2upload log e-mailed to you will include text saying "History contain tainted commit".`tag2upload performs the actual upload by invoking dgit on your behalf. Therefore, using dgit locally is tag2upload done locally. Assuming the commits aren't actually dangerous, you can invoke tag2upload locally and pass an option that will untaint the commits, so that subsequent debpushes will work normally:``dgit --quilt=FOO push-source --deliberately-include-questionable-history --trust-changelog``substituting in the correct quilt mode for your package. (`[1127470](https://bugs.debian.org/1127470))**If you see "git-debpush: found upstream tags: v0.4.0 upstream/0.4.0 git-debpush: use --upstream=TAG to say which one to use"**: This can occur if you are pushing from a repository that has tags both from upstream (i.e.,`v0.4.0`) and tags generated by gbp (i.e.,`upstream/0.4.0`). By specifying`--upstream=v0.4.0`you will make tag2upload use the upstream's git SHA1 commit. However this does not always work, and using`--upstream=upstream/0.4.0`is more reliable, but then the upstream git SHA1 commit information will not be recorded in the signed tag2upload tag. The following situations does not handle the`--upstream=v0.4.0`approach: 1) For +dfsg or +ds packages that make intentional modifications to upstream source before use, 2) Packages using .gitattributes`export-subst`to cause upstream source tarballs to contain additional information, and you chose to not work around this, 3) Upstream does not produce any tags at all, and the Debian packaging follows a git commit ([1127411](https://bugs.debian.org/1127411)).


## Monitoring and outputs; troubleshooting

Your upload should result in an email to you, CC the debian-tag2upload list; if successful it will show up in `dgit fetch` and on [https://browse.dgit.debian.org](https://browse.dgit.debian.org) (even before it has been ACCEPTed by the ftp archive). Note that sponsees don't get mail from tag2upload, but only from dak; tag2upload wants to feed back to the signer, not the Changed-By.

The [tag2upload service page](https://tag2upload.debian.org) can show you the service's current and recent activity.

`debian-tag2upload@lists.debian.org` receives all reports from the tag2upload service, for monitoring and audit. It is a fully-functional public, archived, mailing list. (It should not be used for discussion.) The [top level web view](https://lists.debian.org/debian-tag2upload) is currently missing the archives links, but you can go directly to the page for any month, for example [https://lists.debian.org/debian-tag2upload/2025/05/threads.html](https://lists.debian.org/debian-tag2upload/2025/05/threads.html)


## Web service informational API

Each of the web pages under `https://tag2upload.debian.org` is also available in an un-rendered JSON form. Simply send an `Accept: application/json` header. This is a read-only view.

The JSON schema is undocumented and **unstable**. But, hopefully this will be helpful. If you are using this feature, please contact us so we can try to avoid breaking your code.


## Reporting problems, feedback

If something seems wrong, please don't hesitate to [file a bug](https://bugs.debian.org/cgi-bin/pkgreport.cgi?pkg=git-debpush;dist=unstable).

You may file bugs against

`git-debpush`, even for problems with the service rather than the tag utility.- We don't mind duplicate bugs: we can always merge them if necessary.
- Reports about poor user experience are also welcome.
For example, if

`git-debpush`failed to spot a mistake it could have caught, or gave a poor error message, we want to know.- Please don't file tickets in Salsa. We prefer bugs in the Bug Tracking System.
- Don't write to the debian-tag2upload@lists mailing list - that's for robots only.
- If you would like to email us privately, use dgit-owner at debian.org
You may have some luck with IRC. We are

`Diziet`and`spwhitton`on OFTC. E.g., tag us in`#debian-devel`.

When filing a bug, please provide, if available:

A

**URL for the git tree**(your Salsa repo)The

**precise commit**that you were on when you ran`git debpush`. (If it's not already public, push it somewhere.)The

**jobid**from the tag2upload service web pageAny

**error messages**you receivedThe

you used. (Shell session transcript is ideal.)`git-debpush`invocationAny

**REJECT mail**you received from ftpmaster systems.

And, consider providing:

The

**tag object**, if a tag was produced but not pushed. You can get a copy from`git cat-file tag debian/NNNN`.**Copies of automated emails**you received (tag2upload service, "Debian queue daemon", ftpmaster systems). Use your judgement about which to forward. The messages from the tag2upload service are likely to be relevant.


## Signatures and traceability

tag2upload operates on instructions in the form of git tags, signed by uploading Debian contributors. The original git tag `debian/VERSION` for any successful upload can be obtained with `git clone https://git.dgit.debian.org/PACKAGE.git`.

The tag2upload service signs the tarball form of its uploads (including the `.dsc`) with a dedicated PGP signing key, currently 374D8CE4DB96E9CBD4C0972A606D084E4683C079. The public key is in [debian-tag2upload-keyring.deb](https://packages.debian.org/stable/debian-tag2upload-keyring).

More information including the formal design documents is available in the [dgit git repository](https://salsa.debian.org/dgit-team/dgit). Information helpful for us as service operators, including a [system deployment and dataflow diagram](https://salsa.debian.org/dgit-team/dgit-infra-notes-scripts/-/jobs/artifacts/main/raw/html/services-diagram.pdf?job=render&inline=false) is in the [dgit-infra-notes-scripts repository](https://salsa.debian.org/dgit-team/dgit-infra-notes-scripts).


## Credits

tag2upload was designed and implemented by Ian Jackson and Sean Whitton.

Russ Allbery did a security review, and his steadfast support was invaluable.

Thanks also to the many other people who gave practical, political, and moral support, including: Aigars Mahinovs; Alexander Wirt; Andrea Pappacoda; Aníbal Monsalve Salazar; Anton Gladky; Clare Boothby; Daniel Gröber; Didier 'OdyX' Raboud; intrigeri; Jacob Nevins; Jonathan McDowell; Ke Zhang; Marco d'Itri; Matthew Vernon; Matthias Urlichs; Nilesh Patra; Philip Hands; Sam Hartman; Simon Josefsson; Timo Röhling; Xiyue Deng.

|
|
|
CC BY-SA 4 |
