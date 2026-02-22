# Git

**Parent:** VideoLAN — Project Ideas
**Source:** https://wiki.videolan.org/Git/
**Scraped:** 2026-02-22T23:28:47.576635

---

# Git

[Jump to navigation](https://wiki.videolan.org#mw-head)

[Jump to search](https://wiki.videolan.org#p-search)

[Git](https://git-scm.com/) is a free and open source [version control system](http://en.wikipedia.org/wiki/Revision_control). It is used by programmers to keep track of the different versions of the files composing a software.

## Contents

[1 Basic Git usage](https://wiki.videolan.org#Basic_Git_usage)[1.1 Getting VLC or x264 source code via Git](https://wiki.videolan.org#Getting_VLC_or_x264_source_code_via_Git)[1.2 Configure your global git config](https://wiki.videolan.org#Configure_your_global_git_config)[1.3 Set up Hooks (Tip)](https://wiki.videolan.org#Set_up_Hooks_.28Tip.29)[1.4 General GIT Workflow](https://wiki.videolan.org#General_GIT_Workflow)[1.5 List the local branch](https://wiki.videolan.org#List_the_local_branch)[1.6 List your local non committed changes](https://wiki.videolan.org#List_your_local_non_committed_changes)[1.7 Commit](https://wiki.videolan.org#Commit)[1.8 List your commits](https://wiki.videolan.org#List_your_commits)[1.9 Keeping your local working branch in sync](https://wiki.videolan.org#Keeping_your_local_working_branch_in_sync)[1.10 Use a graphical interface](https://wiki.videolan.org#Use_a_graphical_interface)

[2 Submitting patches](https://wiki.videolan.org#Submitting_patches)[3 Advanced usage](https://wiki.videolan.org#Advanced_usage)[4 Using Git to push to VideoLAN git](https://wiki.videolan.org#Using_Git_to_push_to_VideoLAN_git)[5 Documentation about git](https://wiki.videolan.org#Documentation_about_git)

## Basic Git usage

If you are using **Windows**, please read the [Git Windows](https://wiki.videolan.org/Git_Windows/) page.

### Getting VLC or x264 source code via Git

[$]git clone[https://code.videolan.org/videolan/vlc.git]

Voilà! The full VLC history should be on your hard disk in vlc/.

$ git clone[https://code.videolan.org/videolan/x264.git]

Voilà! The full x264 history should be on your hard disk in x264/.

If you want only the last 3 VLC revisions:

$ git clone[https://code.videolan.org/videolan/vlc.git]--depth 3

Clones without the full revision set (--depth) can't be used for backporting (or to make sure that you're including at least commits up to the common fork point).

You can find the stable VLC version in the 3.0.x branch, to check just that out use:

$ git clone --single-branch --branch 3.0.x[https://code.videolan.org/videolan/vlc.git]

Voilà! You got the stable branch repository.

See [https://code.videolan.org/videolan/vlc](https://code.videolan.org/videolan/vlc)

Or via http protocol from github (github can sometimes be a bit behind as a mirror):
[https://github.com/videolan/vlc.git](https://github.com/videolan/vlc.git)
See [https://github.com/videolan/vlc](https://github.com/videolan/vlc)

You can also clone using http via our repo.or.cz mirror.

$ git clone[http://repo.or.cz/r/vlc.git]

See [http://repo.or.cz/w/vlc.git](http://repo.or.cz/w/vlc.git) (a mirror).

#### After cloning

[$]git log

to see the full log of the trunk.

$ gitk

to see the log graphically.

You can also browse the sources on [GitLab](https://code.videolan.org/videolan/vlc).

### Configure your global git config

May need to use

[$]git repo-config <various options>

1.4.4.2 Requires the `repo-config` command rather than just `config`

#### Personal Information

Tell git your name. (use mostly by git-commit)

[$]git config --global user.name "Your Name" $ git config --global user.email "me@example.com"

#### Mail Setup

To send patches you'll need a working git-send-email configuration.

##### Built-in SMTP support (easiest)

*git-send-email* has built in support for sending e-mail through [SMTP](http://en.wikipedia.org/wiki/SMTP). You'll need a command line similar to the following one:

git-send-email --annotate --smtp-server=smtp.example.com --smtp-server-port=587 --smtp-encryption=tls --smtp-user="yourname@example.com" <...>

##### MSMTP

You can use [msmtp](https://marlam.de/msmtp/) to achieve this. Install it with tls and ssl activated and place the following config file (.msmtprc) in your home directory

# msmtp configuration file # Set default values for all following accounts. defaults tls on tls_starttls on tls_trust_file /certificates/EquifaxSecureCertificateAuthority.crt logfile /log/.msmtp.log # GMAIL account gmail host smtp.gmail.com port 587 protocol smtp from user.name@gmail.com auth on user user.name@gmail.com # Set a default account account default : gmail

Then configure git to use msmtp. The password will be asked for upon sending mail.

[$]git config --global sendemail.smtpserver /usr/local/bin/msmtp

The certificate for gmail can be found here: [EquifaxSecureCertificateAuthority.crt](https://www.geotrust.com/resources/extended-validation-ssl/certs/Equifax%20Secure%20Certificate%20Authority.crt)

If you receive a ** cannot set X509 trust file** error when using another CA certificate, make sure it is in the PEM (text format) rather than DER format (binary).

##### macOS

Setup info with e.g. gmail account

[$]git config --global sendemail.smtpserver smtp.gmail.com $ git config --global sendemail.smtpuser your-gmail-address-here $ git config --global sendemail.smtpencryption tls $ git config --global sendemail.smtpserverport 587

If errors occur telling you something like perl's SMTP::SSL package is not there. Do the following

$ sudo -H cpan Net::SMTP::SSL

#### Using git with color (Tip)

If you want to use git with colored output use:

[$]git config --global color.ui true

If you are using an old git version (prior to 1.5.5) and previous command didn't work, use:

$ git config --global color.diff auto $ git config --global color.status auto $ git config --global color.branch auto

#### Setting up "git up" (Tip)

If you want to be able to just keep in sync using "git up" use:

[$]git config --global alias.up "pull --rebase"

And if you like your tree to be messy and don't want git to complain (like in svn) use:

$ git config --global alias.up '!sh -c "git commit -a -m "Before rebase" && git pull --rebase && git reset head^"'

#### Setting up "git wu" (Git What's Up) (Tip)

If you want to see what you are about to "git push":

[$]git config --global alias.wu "log --stat origin..@{0}"

Now use:

$ git wu

Note that this only works for the master branch.

#### Setting up "git wup" (Git What's Up - with patch) (Tip)

If you want to see what you are about to "git push", along with the diff:

[$]git config --global alias.wup "log -p origin..@{0}"

Now use:

$ git wup

### Set up Hooks (Tip)

If you are using Qt-creator and want to keep your files listing in sync, just set up a post-checkout hook accordingly.

```
#!/bin/sh
# this file as .git/hooks/post-checkout
if test -f vlc.files
then
echo "Updating Qt files list"
git ls-files > vlc.files
fi
```

### General GIT Workflow

- Make your file edits in your local repository.
- "git commit" the changes in your local repository
- "git pull --rebase" or "git up" (if you did
*git config --global alias.up "pull --rebase"*) to bring the rest of your local repository up to date - "git log origin..master" to check what you are going to commit
- "git push" to move your changes up to the master
- "git stash" if you want to "hide" your changes. Do this if you think there may be other commits against the same things you are working on and want to refresh your local checkout (using a git pull --rebase) from the master. Use "git stash apply" to get your stash back.
- "git checkout -f master" if you think your tree is pretty hopeless, need a kill-and-fill to bring the master into your local repository.

### List the local branch

You can now list your local branch by doing

[$]git branch

which should output

$ git branch * master

### List your local non committed changes

[$]git status | less

### Commit

Now you can start to work on your tree. As soon as you feel you have reached a step in development where you can commit your work **locally**, use

[$]git commit -a

or

$ git commit <specific files>

If you wish to give credit to someone else's work (e.g. you are applying a third party patch):

$ git commit <specific files> --author "Name Surname <user@domain.com>"

### List your commits

[$]git log



### Keeping your local working branch in sync

[$]git pull --rebase

To shorten up that command type

$ git config --global alias.up "pull --rebase"

Now you can just type:

$ git up

### Use a graphical interface

[$]gitk # Tree Browser $ qgit # Tree Browser $ git-gui # Commit/push/... editor

## Submitting patches

First make sure you have **read** our [Sending Patches](https://wiki.videolan.org/Sending_Patches/) page. And that you've **read** the [ Check List](https://wiki.videolan.org/Sending_Patches/#Check_List).

If you have been developing on vlc locally and (still) don't have write access, you can submit all your commits in one shot using:

[$]rm -Rf patches $ git format-patch -o patches origin $ git send-email --to vlc-devel@videolan.org patches

If you want to create a cover letter for multiple patches use:

$ git format-patch -o patches origin -n --cover-letter $ git send-email --annotate --cover-letter --to vlc-devel@videolan.org patches

If you have multiple patch consider using:

$ git send-email --compose --no-chain-reply-to --to vlc-devel@videolan.org patches

This will produce the patches for each local commit in the directory "patches" and send them. Use --no-chain-reply-to make sure it doesn't reply.

For x264, do the same with x264-devel@videolan.org

Don't do:

- [PATCH 0/m]
- [PATCH 1/m]
- [PATCH 2/m]
- ...


- [PATCH 2/m]

- [PATCH 1/m]

But do:

- [PATCH 0/m]
- [PATCH 1/m]
- [PATCH 2/m]
- ..


## Advanced usage

### Creating a secondary local branch

If you want to work on a specific project that could require a branch of the trunk, create a local branch of the current branch by doing:

[$]git branch mywork

and to actually use it do:

$ git checkout mywork

Which could be summarized by:

$ git checkout -b mywork

Then do some commit on it... And you can go back to your original master branch by doing:

$ git checkout master

### Fetching a remote branch

To see the remote branch use:

[$]git branch -r

If the remote branch is named 0.8.6-bugfix

$ git branch 0.8.6-bugfix origin/0.8.6-bugfix Branch 0.8.6-bugfix set up to track remote branch refs/remotes/origin/0.8.6-bugfix. $ git branch 0.8.6-bugfix * master

To checkout that branch use:

$ git checkout 0.8.6-bugfix

To stay up-to-date a simple

$ git pull --rebase

Should be enough.

If warnings appear that files still need updating:

$ include/libvlc_internal.h: needs update include/mediacontrol_internal.h: needs update include/vlc/libvlc.h: needs update include/vlc_update.h: needs update modules/access/mms/mms.c: needs update ...

Then do a checkout -f to revert non committed local changes

$ git checkout -f

To stay up-to-date another

$ git pull --rebase

Should give no more warnings.

To push to the remote branch, use:

$ git push origin 0.8.6-bugfix:0.8.6-bugfix

### Creating a remote branch

If the new remote branch is named 0.9.0-bugfix, and is based on the local master branch. First make sure everything go as planned with the --dry-run option:

[$]git push --dry-run origin master:refs/heads/0.9.0-stable To git@git.videolan.org:vlc.git * [new branch] master -> 0.9.0-stable

Then push it:

$ git push origin master:refs/heads/0.9.0-stable To git@git.videolan.org:vlc.git * [new branch] master -> 0.9.0-stable $ git branch -r origin/0.9.0-stable origin/master

To checkout that branch now see [#Fetching a remote branch](https://wiki.videolan.org#Fetching_a_remote_branch)

### Backporting commits

It is possible to "backport" commit between the master branch and a -bugfix branch. However since VDD'09, the bugfix branches have been split to their own git repositories. This leaves us with 2 cases.

#### Normal simple case

Go to your -bugfix branch:

[$]git checkout 1.0-bugfix

Backport the commit:

$ git cherry-pick -x -s <sha-id of commit>

If git fails to do the backport by itself, you'll be presented with the usual options in case of a failed merge or patching. Use "git status", your favorite editor or "git mergetool" to resolve the situation. Then use "git add" and "git commit -c <sha-id of backported commit>". Then push your commit as usual.

#### Case of VLC bugfix branches

Due to the number of commits in vlc.git and the amount of divergence between the master and 1.0-bugfix branches, they have been separated into two different git repositories. But that doesn't block you from backporting.

Get the -bugfix git:

[$]git clone[https://git.videolan.org/git/vlc/vlc-1.0.git]vlc-bugfix

Add vlc.git as an additional remote:

$ git remote add vlc-master[https://git.videolan.org/git/vlc.git]

Update the information from vlc-master

$ git fetch vlc-master

Backport as normal

$ git cherry-pick -x -s <sha-id of commit>

### Publishing your own fork

Go to [http://repo.or.cz/w/vlc.git](http://repo.or.cz/w/vlc.git) and click [fork](http://repo.or.cz/regproj.cgi?fork=vlc.git). You will be able to publish your work there.

Please don't forget to send a mail to the *vlc-devel* mailing list as soon as you create your fork.

### Revert your non-committed local changes

[$]git checkout -f

### Edit or undo not yet pushed commits

This will undo the last commit

[$]git reset HEAD^

which is the same as

$ git reset master^

(if your checked-out copy of your tree is master) And also the same as

$ git reset a44a594 # note that there is no need to use the full sha id

If you have a stack of patch that you have not yet committed you can delete one patch from the list using git rebase --interactive

$ git rebase --interactive origin pick eacf185 test pick 56322eb VLMA owner is vlma prod. # Rebase 826757e..56322eb onto 826757e # # Commands: # pick = use commit # edit = use commit, but stop for amending # squash = use commit, but meld into previous commit

### Diff-ing

- You can diff between two branches using

[$]git diff branch1 branch2

- You can diff between the previous 10th commit and current using

$ git diff HEAD~10 HEAD

- You can diff between the previous 10th commit and current of the branch "mywork" using

$ git diff mywork~10 mywork

- Imagine that git log is like

$ git log commit e0394f269305edd09843257e7c1d1a66aaf48ab3 Author: jb <jb> Date: Fri Apr 13 07:14:48 2007 +0000 qt4 - Mousewheel (2) commit e80b339081aa6755f67c9bd8e2aacf93a9a79d95 [..] commit ff7004b70fd239e4120deb160e2991bd5237b8df [..] commit a44a594898f981a145cfcace5f16f8973f9eb46f [..] commit 690df705c963cf6bf6f5746d54bc97a85ff91919 [..] commit 679f8b1c3e0baa469efa970588b95a625c595d64 [..]

$ git diff a44a594898f981a145cfcace5f16f8973f9eb46f~2 e80b339081aa6755f67c9bd8e2aacf93a9a79d95

Will be equivalent to:

$ git diff ff7004b70fd239e4120deb160e2991bd5237b8df e80b339081aa6755f67c9bd8e2aacf93a9a79d95

And to:

$ git diff HEAD~4 HEAD^

- Remember that to produce a patch you should rather use git format-patch than git diff most of the time.

### Patch-ing

- You can apply patches using

[$]git apply <patch>

### Tracking regression

git has a great tool called [git-bisect](https://www.kernel.org/pub/software/scm/git/docs/git-bisect.html) to help you to track a faulty commit. Imagine you are tracking a bug that is known to appear after 0.8.6 (assuming 0.8.6 is tagged):

[$]git bisect start $ git bisect bad # tell git current version has the bug you are tracking $ git bisect good 0.8.6 # tell git 0.8.6 didn't have the bug

And then git will checkout a certain revision, and ask you to test it. And you simply say whether this version has the bug. If it has the bug:

$ git bisect bad

if the bug is not present:

$ git bisect good

And so on by bisection... At the end git will indicate the faulty commit. Most of the time this tool is really efficient to track regression.

If you can provide a script that test the presence of the bug

$ git bisect run <script_name>

will be able to track down the regression by itself. See [git-bisect Documentation](https://www.kernel.org/pub/software/scm/git/docs/git-bisect.html).

## Using Git to push to VideoLAN git

### Initial requirements

- You must have credentials to push commits into the repository. For other contributors, please read upper
[Submitting patches to the vlc-devel or x264-devel](https://wiki.videolan.org#Submitting_patches)paragraph. - Make sure you've set your name and email in your commits

[$]git config --global user.name "Your Name" $ git config --global user.email "me@example.com"

### Convert your tree to use your ssh push commit access

[$]vi vlc/.git/config

And replace

[https://git.videolan.org/git/vlc.git]

With

git@git.videolan.org:vlc.git

### Staying up to date

[$]git pull --rebase

If you don't want to have to type --rebase every time you pull do:

$ git config branch.master.rebase true

This one creates a merge object which is not how SVN worked, so let's use the first version...

$ git pull

### Pushing your work

[$]git log origin..master # Check what you are going to push $ git push
