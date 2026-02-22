# git howto

**Parent:** GNU Mailman — Project Ideas
**Source:** https://wiki.list.org/DEV/HowToContributeGit
**Scraped:** 2026-02-22T23:28:47.587703

---

# How to Contribute

Mailman is [hosted on GitLab](https://gitlab.com/mailman/mailman) and thus uses [git](https://git-scm.com/). This page lists the basics to jumpstart contributions. Please refer to git documentation on the internet for detailed explanations of the commands used. This should cover the basics you need to contribute. If you think anything could be improved or added please do so, or contact [me](http://wiki.list.org/SimonHanna) to do so. In case you have any questions please try to find the answers online. You should be able to find enough using Google, otherwise ask on the IRC channel (#mailman on libera.chat).


## Initializing repositories

This section will guide you through the process of initializing your forks and local repositories. Please note that the rest of the document will assume the locations and names used here. These can of course be adapted if you want something else.

The process will be demonstrated for mailman-core. Setting up the other projects is mainly just swapping out names.


### Setting up your pc

Create a directory that will hold all the projects.

$ mkdir -p ~/dev/mailman

Make sure you have a ssh-key, if you don't just run the following command and press enter until you're back to the normal shell:

$ ssh-keygen

Before you do anything you will need to create your own fork of the project. If you don't have an account at [GitLab](https://gitlab.com) now is the time to create one. If you haven't uploaded your public ssh-key, do so now. Visit your [profile page](https://gitlab.com/profile/keys) to add ssh-keys and paste in your public key. (It should be ~/.ssh/id_rsa.pub)

Visit [Mailman's page](https://gitlab.com/mailman/mailman) on gitlab and create a fork by pressing the fork button. In case you already have a fork, this will just take you to your own fork.

From your fork's GitLab page, copy the ssh url, which should be something like:

git@gitlab.com:<username>/mailman.git

Now it's time to clone your fork. Be sure to replace the url with your own.

$ cd ~/dev/mailman $ git clone git@gitlab.com:<username>/mailman.git

This will create a remote called origin that points to your fork. You will want to add another remote to be able to fetch changes that others do. Note that this time we will be using the url of the Mailman project itself, and not your fork's url:

$ cd ~/dev/mailman/mailman $ git remote add upstream git@gitlab.com:mailman/mailman.git

Now you are up and running. You can clone all other projects into `~/dev/mailman/<project_name>` the same way as above.


## Development Workflow

Unless it's a really trivial change, *always*

[create an issue](https://gitlab.com/mailman/mailman/issues)on GitLab first- Create a new branch for this issue
- Start coding
- Push the branch
- Create a merge request


## Creating branches

In git, it is common to not commit directly into the master branch. Instead changes are committed into separate branches which are then proposed for merging.

The code for creating a new branch is

$ git checkout -b <branch_name> <branch_name_to_branch_from>

In case you want to create a branch from the current one, you can omit the last argument. So to create a new branch from the master branch (Which you probably want to do every time you work on a new issue) you use:

$ git checkout -b my-new-branch master

If you are in the master branch you can use

$ git checkout -b my-new-branch


## Adding files

You need to add files before you actually commit. You do this by using the following command:

$ git add <first_file> <second_file> ...

There also is an interactive mode that can be used to only add parts of files which can be used if you don't want all changes to go into one commit. This is done by calling:

$ git add -i


## Making a commit

Once you have added files you want to commit, it's time to actually commit. The command is:

$ git commit

This should open up your default editor. Notice that it already contains some text listing all the changes you are about to commit. Every line that starts with a '#' is a comment and ignored.

The actual commit should be split into two sections. The first is just the first line of the commit. The first line should describe the commit in no more than 80 characters. The first line is always followed by an empty line. After that you can provide details that explain the commit. An example of a good commit message is:

Refactor the user model Changes include: * Limiting the user name length * Adding checks for the password

After you entered the message save the file and close it. This will automatically commit.


## Push changes

Once you committed your changes in a branch you should push it using:

$ git push -u <origin> <branch_name>

<origin> depends on what your remote is called. It's convention to use `origin`. <branch_name> is whatever your branch is named.


## Create Merge request

While working on the same issue, please keep using the same merge request. Only open a new branch/merge request for a new issue. In case you change previous commits you can always force push to the remote branch. (barry: is this really a good idea?) Keeping your changes in one merge request makes it easier to track progress and see how the code is evolving.

Once you pushed your branch it's time to create a merge request. To do this login into GitLab and go to your fork. You should find the branch overview and click the button to create a merge request from this branch.

Enter a good title and describe your changes in the description. If your merge request is fixing some issue that is registered on GitLab you should include this in your description:

Fixes #<issue_number>

There are several different strings you can use to achieve that, for example:

Fixes #12 closes #11

Doing this will close the issues automatically once the merge request is merged.


## Fetching changes from GitLab

You will want to keep your local repository up to date. Every now and then, or whenever you know that there are new commits in the master branch, you will need to update your personal repository as well. This done by fetching and merging. You will first want to fetch changes using:

$ git fetch <remote_name>

If you followed the setup instructions, your own fork is named `origin` and the original repository is named `upstream`. So the command would be:

$ git fetch upstream

After that make sure you are in the master branch and merge the remote in. The general syntax is:

$ git checkout <branch_to_update> $ git merge <branch_to_get_update_from>

In our case this would be:

$ git checkout master $ git merge upstream/master

You should not have any merge conflicts as you are not supposed to commit anything into the master branch yourself. Once you did this, you can go on to rebase all other branches from the master branch.


## Rebasing

If you have a branch but there are merge conflicts with the master branch you have to get your branch up to speed. You can use merge, but rebasing is cleaner. The command is:

$ git rebase <branch_to_rebase_of>

You will probably be rebasing off the master branch so the command will be:

$ git rebase master

This will go over every commit you made and ask you to edit files in case of merge conflicts. If you don't have any conflicts, the commit will just work. Please refer to online documentation on how to perform a rebase.


## Squashing commits or rewriting history

If you have made some commits and want to reorder them, combine them, remove some or even split them git makes this very easy.The command is:

$ git rebase -i HEAD~<number_of_commits_to_edit>

So if you want to change the last 10 commits you would use:

$ git rebase -i HEAD~10

This will open up an editor and allow you to perform different actions on each of the commits. Please refer to online documentation on how to actually do the rebase.
