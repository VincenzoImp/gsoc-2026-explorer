# Mercurial

**Parent:** GNU Octave — Project Ideas
**Source:** https://wiki.octave.org/Mercurial
**Scraped:** 2026-02-22T23:28:47.624270

---

# Mercurial

[Jump to navigation](https://wiki.octave.org#mw-head)

[Jump to search](https://wiki.octave.org#searchInput)

[Mercurial](https://www.mercurial-scm.org) (sometimes referred to as `hg`

) is the source code management system used for Octave development.

Everybody is free to **run, copy, distribute, study, change and improve** [1] Octave's source code, given in the main repository at

[https://www.octave.org/hg/octave](https://www.octave.org/hg/octave). Use Mercurial to get the latest version of Octave

hg clone https://www.octave.org/hg/octave

## Workflow reference

This section gives several frequently used Mercurial commands and sequences.

- Initial clone:
hg clone https://hg.savannah.gnu.org/hgweb/octave/


You can then bootstrap, configure, make, and maybe make check, make install.

- To update on a regular basis, you can do
hg pull -u

orhg pull && hg update


- To make a
*local clone*, you can clone from your main Octave repository on your computer to another directory like this:hg clone octave myfeature

which will clone the Octave directory into a new directory called "myfeature". You will need to cd to the correct directory first. Then you can cd into the new directory and run bootstrap, configure, make. To prevent a fresh download of gnulib, you can specify the path to the first Octave directory's gnulib if you wish using the configure option`--with-gnulib-prefix=DIR`

.

x
It is best practice to make a new clone directory for each feature or bugfix you work on, or use [Mercurial Queues](https://hgbook.red-bean.com/read/managing-change-with-mercurial-queues.html). Both approaches make recovery from mistakes much easier.

- To work on the stable branch instead of the default branch, make a local clone called "stable", then cd to it and
hg update stable


- To circulate work-in-progress bugfixes: first cd to the relevant local clone, then edit the relevant files, verify that it builds, then
hg diff > /tmp/my.wip.patch

and then upload that file to the bug tracker discussion. You can also copy-paste it into a bug discussion using`+verbatim+`

...`-verbatim-`

tags if the patch is small enough. Accept feedback from the bug discussion and iterate your patch.

- When you're ready to commit your fix, first pull and update your main Octave directory from Savannah, then pull and update your local clones. Then build again to make sure things haven't broken. Then
hg commit

and type a summary and context for your change. Exit the editor, saving when it prompts. Build again so your build gets the latest hg id. Typehg export > /tmp/my.patch

and upload that file into the bug discussion. Wait for a maintainer to apply it with your name, then if you dohg in

in your main Octave directory it'll show up as an incoming change. Do a pull and up to get that, then do a pull and up in your individual clone directories to get it there.

- To merge changes from stable to default
hg merge stable

It's best to run this only in local clones that are already on the default branch. That way, local clones on stable don't have to switch branches before merging.

- To push to a repository, if you have push rights to that repository, you can see what's going out with
hg out

and then if you're happy with it you canhg push


## Tutorials

Joel Spolsky's Mercurial tutorial: [https://hginit.github.io/01.html](https://hginit.github.io/01.html)

[TortoiseHg](https://tortoisehg.bitbucket.io/)is a GUI for Mercurial and it is especially recommended for users doing their first steps with source code management systems. Linux, macOS, and MS Windows are supported.

## Creating and submitting patches (changesets)

If you want to share your modifications, for example to fix a nasty **bug #42424**, you cannot just submit your changes to Octave's main repository. You have to generate a **patch (or changeset)** so other Octave developers can include them into Octave's source code.

- Get the latest version of Octave (or some Octave package)
hg clone https://www.octave.org/hg/octave

or when already clonedhg pull && hg update

- Make your changes (fix bug #42424) and save them.
**Make sure that your changes don't introduce new bugs!**Thus it is recommended to[build Octave](https://wiki.octave.org/Building)and to[run Octave's test suite](https://wiki.octave.org/Tests)before proceeding.Please follow the[Contribution guidelines](https://wiki.octave.org/Contribution_guidelines)for C/C++ or Octave code files! - Commit your changes
hg commit

Mercurial will open your default editorand ask you for a commit message. Please follow the[[2]](https://wiki.octave.org#cite_note-2)[commit message guidelines](https://wiki.octave.org/Commit_message_guidelines), e.g.help.m: Display relevant topics first (bug #42424) * scripts/help/help.m: Describe what you changed to display relevant topics first. The maximal line width is 80 characters.

- Export the changes
hg export -r tip -o bug42424.patch

The final patch for submission will look like this**File:**bug42424.patch# HG changeset patch # User Awesome Hacker <awesome@hacker.com> # Date 1591780091 -32400 # Wed Jun 10 18:08:11 2020 +0100 # Node ID 68c698c4f2fd98bf2d48234bd1da99e91763114f # Parent f5c9bb5955e7c9fddef5c3c3f115201e11b43b79 help.m: Display relevant topics first (bug #42424) * scripts/help/help.m: Describe what you changed to display relevant topics first. The maximal line width is 80 characters. diff -r f5c9bb5955e7 -r 68c698c4f2fd scripts/help/help.m --- a/scripts/help/help.m Tue Jun 09 14:11:13 2020 -0700 +++ b/scripts/help/help.m Wed Jun 10 18:08:11 2020 +0900 @@ -99,7 +99,7 @@ function retval = help (name) endif ## Get help text - [text, format] = get_help_text (name); + [text, format] = get_better_help_text (name); ## Take action depending on help text format switch (lower (format))

- Upload bug42424.patch to the
[bug](https://savannah.gnu.org/bugs/?group=octave)or[patch](https://savannah.gnu.org/patch/?group=octave)tracker. If your patch file is larger than the upload limit, you can compress it before uploading. Please use a free format!

## Mercurial Tips for SoC students

This section is meant to provide tips for [Summer of Code](https://wiki.octave.org/Summer_of_Code) students working on new Octave features.

Students should publish their work as it progresses in a public repository. In this section we use for example `public.server.org/octave`

.

### Using bookmarks

[Bookmarks](https://www.mercurial-scm.org/wiki/Bookmarks) are useful for identifying a series of commits. They are a "lightweight" solution to [named branches](https://www.mercurial-scm.org/wiki/NamedBranches), which are not automatically updated for example. To create a bookmark `my-gsoc`

use

```
hg clone https://www.octave.org/hg/octave
hg bookmark my-gsoc
```

To make the bookmark visible in the public repository use

```
hg push --bookmark ssh://student@public.server.org/octave
```

### Staying up-to-date with the main repository

Octave development does not stand still while the students development proceeds. Octave's main repository gets updated, too. The following commands can be used to get these updated to the students clone of the main repository:

```
hg pull https://www.octave.org/hg/octave # Get latest remote "tip"
hg update -r my-gsoc # Activate bookmark "my-gsoc"
hg merge tip # Merge "tip" into "my-gsoc"
hg commit -m "maint: merge default to my-gsoc"
hg push ssh://student@public.server.org/octave
```

### Preparing for code reviews

At the time of the mid-term or final review (or whenever the mentor requires it) students should prepare their code for review and possibly inclusion into the main repository.

- Create a full log of changes
hg log --template=changelog --no-merges --user student-name

If students have been following the[Commit message guidelines](https://wiki.octave.org/Commit_message_guidelines)the output is a good starting point for the commit message in the next step. Some manual post-processing might be necessary:- Each touched file should appear only once.
- Do not mention backed-out commits.

- Prepare a singe patch (changeset) including all code that should be submitted for review The file mid-term-review.patch can uploaded to the
hg pull https://www.octave.org/hg/octave # Get remote "tip" and "@" hg update -r @ # Activate bookmark "@" hg merge my-gsoc # Merge "my-gsoc" into "@" hg commit hg export -r tip -o mid-term-review.patch

[patch tracker](https://savannah.gnu.org/patch/?group=octave).

Finally, there is a subtle difference between`"tip"`

, which is a reference to the (local or remote) changeset added to the repository most recently and the bookmark`"@"`

used by the Octave developers to point to the latest remote changeset. Often both refer to the very same changeset and they can used interchangeably.

## Example Mercurial configuration

Place the following file in your home directory, e.g. /home/username/.hgrc.

**File:**.hgrc

```
[ui]
username = Your Name <your@email>
[extensions]
color =
histedit =
pager =
rebase =
strip =
[pager]
pager = LESS='FSRX' less
attend = help, annotate, cat, diff, export, glog, log, outgoing, incoming
[diff]
showfunc = True
[color]
mode = terminfo
## Custom colors
color.gray = 244
color.orange = 202
color.lightyellow = 191
color.darkorange = 220
color.brightyellow = 226
status.modified = magenta bold
status.added = green bold
status.removed = red bold
status.deleted = cyan bold
status.unknown = gray bold
status.ignored = gray bold
## Colors for each label
log.branch = cyan
log.summary = lightyellow
log.description = lightyellow
log.bookmark = green
log.tag = darkorange
log.graph = blue
## Colors for each phase
changeset.secret = blue bold
changeset.draft = red bold
changeset.public = orange
desc.here = bold blue_background
[bookmarks]
track.current = True
[alias]
glog = log --graph
top = log --graph -l
```

## Tips for working with TortoiseHg

TortoiseHg is a multi-platform graphical user interface for Mercurial repositories. It allows to perform many hg operations using the context menu and toolbar buttons. That might make it easier to get used to working with Mercurial.

### Activate the "mq" extension

The "mq" extension allows to modify (local) changesets after they have been committed. It also allows to rebase changes to a new parent or to strip changes completely. The "mq" extension does *not* allow to modify pushed changes.

To activate the "mq" extension in TortoiseSVN, open the settings, select "Extensions" on the global settings tab and activate the checkbox next to "mq".

The most useful feature of that extension is probably to update an existing changeset. For this, select "Modify History" -> "Import to MQ" in the right click menu of the respective changeset. After updating some local files or changing the commit message, hit the "QRefresh" button. Finish the patch by selecting "Modify History" -> "Finish Patch" from the right click menu of the respective changeset.

### Rebase a change to a current tip

Sometimes a change in the upstream repository might make it necessary to rebase a changeset to a new parent. There are several ways to achieve this. The ways described here might not be the most elegant ones. Any editor is welcome to add onto this.

Strip and commit:

- Pull changes from the upstream repository.
- Before updating to the new tip, strip the local changes by selecting "Modify History" -> "Strip..." from the right click menu. In the dialog, select "Do not modify working copy during strip (-k/--keep)".
- Update to the new tip (maybe in incremental steps).
- Commit the local changes in a "fresh" changeset. This has the drawback that any commit message might be lost. But it often works even if other approaches fail.

Un-apply and re-apply:

- Pull changes from the upstream repository.
- Before updating to the new tip, import the local changeset to mq by selecting "Modify History" -> "Import to MQ" in the right click menu.
- You might want to refresh the changeset with local changes.
- Un-apply the patch by selecting "Modify History" -> "Unapply Patch" from the right click menu. If there are other, un-committed changes in the local repository, you might want to select "Tolerate non-conflicting local changes (--keep-changes)" in the "Modify History" -> "MQ Options" dialog from the right click menu beforehand.
- Update to the new tip.
- Select the previously unapplied patch on top of the revision graph and re-apply it by using the "Reapply Patch" option in the right click menu. This has the advantage that a commit message will be retained. But re-applying the patch might fail if there were changes in the upstream repository that made the patch incompatible.

Rebase:

- Pull changes from the upstream repository.
- Select the local changeset that you'd like to rebase.
- Hold down the Ctrl key and select the changeset that should be the new parent of the local changeset (probably the new tip).
- Right-click the changeset of the new parent and select "Rebase...".
- The default settings are often times fine. This process has the advantage that a commit message will be retained and it often times resolves conflicts automatically. But it doesn't work if there are any un-committed local changes.

## Footnotes

[↑](https://wiki.octave.org#cite_ref-1)[https://www.gnu.org/philosophy/free-sw.en.html](https://www.gnu.org/philosophy/free-sw.en.html)[↑](https://wiki.octave.org#cite_ref-2)To set your default Mercurial editor, read[https://www.mercurial-scm.org/wiki/editor](https://www.mercurial-scm.org/wiki/editor).

## External links

[https://hginit.com/](https://hginit.com/)-- Mercurial tutorial[https://www.mercurial-scm.org/wiki/Tutorial](https://www.mercurial-scm.org/wiki/Tutorial)-- Mercurial tutorial[https://www.mercurial-scm.org/wiki/QuickStart](https://www.mercurial-scm.org/wiki/QuickStart)-- Mercurial quick start[https://tortoisehg.bitbucket.io/](https://tortoisehg.bitbucket.io/)-- TortoiseHg is a GUI for Mercurial (Linux, macOS, MS Windows)
