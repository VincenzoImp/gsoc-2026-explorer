# GNU Mailman — Project Ideas

**Source:** https://wiki.list.org/DEV/Google%20Summer%20of%20Code%202026
**Scraped:** 2026-02-22T23:28:47.587565

---

# Google Summer of Code 2026 Ideas Page

**Take me straight to the ideas!**


## What is Mailman?

Mailman is free software for managing electronic mail discussion and e-newsletter lists. Mailman is integrated with the web, making it easy for users to manage their accounts and for list owners to administer their lists. Mailman supports built-in archiving, automatic bounce processing, content filtering, digest delivery, spam filters, and more. Many open source denizens will be familiar with Mailman 2.1, which is used to manage many project mailing lists. All of our current work is on Mailman 3, which was released in 2015, but there's still lots of room for new features and ideas!

Not sure about how GSoC works? Check out the resources at [Summer of Code Home](https://summerofcode.withgoogle.com/)

Contents

-
[Google Summer of Code 2026 Ideas Page](https://wiki.list.org#Google_Summer_of_Code_2026_Ideas_Page) -
[Project Ideas](https://wiki.list.org#Project_Ideas)-
[Mentors](https://wiki.list.org#Mentors) -
[User Profile Tool](https://wiki.list.org#User_Profile_Tool) -
[Moderating Emails and Threads in Hyperkitty](https://wiki.list.org#Moderating_Emails_and_Threads_in_Hyperkitty) -
[Support for Encrypted Lists](https://wiki.list.org#Support_for_Encrypted_Lists) -
[Improved UI for Subscription Management](https://wiki.list.org#Improved_UI_for_Subscription_Management) -
[Dynamic Sublists (aka Conversations)](https://wiki.list.org#Dynamic_Sublists_.28aka_Conversations.29) -
[Topics](https://wiki.list.org#Topics) -
[HTML Digests](https://wiki.list.org#HTML_Digests) -
[Configurable Mail Footers](https://wiki.list.org#Configurable_Mail_Footers) -
[Per-list backup](https://wiki.list.org#Per-list_backup) -
[Shell Completions](https://wiki.list.org#Shell_Completions) -
[Log Access from the Web UI](https://wiki.list.org#Log_Access_from_the_Web_UI) -
[Implement Domain Administration](https://wiki.list.org#Implement_Domain_Administration) -
[The Generic Project Template](https://wiki.list.org#The_Generic_Project_Template)

-


## Getting Started

The [GSoC Contributor Guide](https://google.github.io/gsocguides/student/) has some great general GSoC information. Read it first!

Before you ask any questions about how to do anything in git or initialize your repository please read through the [git howto](/ideas/gnu-mailman/howtocontributegit) and see if that answers your questions.


## Recommended Skills

Here's a few skills that will make it easier for you to get started as a Mailman developer:

**Python programming.**You can be fairly new to[Python](https://www.python.org), but you're going to have to be comfortable reading the Mailman code and asking questions if you aren't sure how it works. SQL is another useful language to know. Mailman core makes heavy use of third-party modules such as[lazr-config](https://lazrconfig.readthedocs.io/en/stable/),[Zope interfaces](https://zopeinterface.readthedocs.io/en/latest/README.html), and[SQLAlchemy](https://docs.sqlalchemy.org/en/20/). Postorius and HyperKitty are[Django](https://wiki.list.org/%EF%BB%BF%EF%BB%BFhttps%3A//docs.djangoproject.com/en/4.0/)applications, which even experienced Python programmers may find to be as unfamiliar as a foreign language. Ask us about anything!**Familiarity with any version control.**We use git on Gitlab (and you will too), but any experience will help you here.**Ability to setup a development environment for Mailman.**You'll need access to a Linux machine or VM, and we will help you to set it up. (Mailman also works well on macos and BSD systems, but the core developers are not as familiar with them. Windows-based POSIX environments are going to be difficult, not recommended unless you're wizardly with them. Windows itself is known*not*to support Mailman.)**Ability to communicate with the Mailman developers.**You'll be expected to keep a blog, post to the public mailing lists, ask questions, and describe the work you're doing. We don't*require*English, but we have very little ability to work in other languages.

Specific projects may have additional desired skills listed along with them.


## What is Mailman Suite?

In Mailman 3, we've divided up the code into a number of sub-projects. We refer to the whole package as "Mailman Suite" and there's a few really important pieces you should know:

[Mailman Core](https://gitlab.com/mailman/mailman)- This is the part that actually sends and receives mail and handles subscriber and list information.[Postorius](https://gitlab.com/mailman/postorius)- A web interface for managing Mailman lists (e.g. subscribing, changing preferences), a WSGI application based on Django.[Hyperkitty](https://gitlab.com/mailman/hyperkitty)- A web interface to access GNU Mailman v3 archives, another WSGI application based on Django.

There's also a number of smaller projects that provide the glue to make these pieces work well together, or allow them to be used separately.

[All the Mailman 3 source is on GitLab](https://gitlab.com/groups/mailman).


## Documentation & Installation

Here are some useful links to get you started with Mailman Development:


Mailman is written in Python. Mailman supports Python 3.5+. Each individual projects may have their own restrictions on the Python versions you can use depending on the support of the their dependencies.

Development work on Mailman 2.1 has been frozen for some time, so **all new project ideas must be related to Mailman 3**.


## GSoC Application Process

To be considered as an applicant for Google Summer of Code 2026, we need you to contribute at least one Merge Request (not merely a typographical error in a comment, but an actual defect including semantically incorrect documentation), and have that accepted.

The best way to get started is to set up a local development environment, documentation for which is [available here](http://docs.mailman3.org/en/latest/devsetup.html).

You can then find issues tagged with "beginner-friendly" and "easy" on [our Gitlab Page](https://gitlab.com/groups/mailman/-/issues?sort=created_date). Or ask us on the mailing lists (but showing you've checked the [GitLab](https://wiki.list.org/GitLab) issues first is something we consider anencouraging sign!) Feel free to open more issues when you find them.


## Contacting us

**The most successful GSoC students are the ones who work closely with the Mailman team.** As you might expect from a group that makes mailing list software, our preferred method of communication is our mailing list, but we also have an IRC channel. Please do not send private messages or emails unless asked to do so or the subject is personal rather than technical, since we get a lot of similar questions and would rather the questions and answers happen in public so everyone can benefit.

Mailing list to use for GSoC discussions:

[Mailman developers mailing list](https://mail.python.org/mailman3/lists/mailman-developers.python.org/)Mailing list to consult users about their experiences and requirements:

[Mailman Users mailing list](https://lists.mailman3.org/mailman3/lists/mailman-users.mailman3.org/)IRC channel: #mailman on irc.libera.chat. You need to have a

[registered nickname](https://libera.chat/guides/registration)to participate. Many people prefer specialized clients, but you can also participate using[Libera's Kiwi webchat](https://web.libera.chat/)site. For help in connecting, see[Connecting to Libera.Chat](https://libera.chat/guides/connect).


## Writing Your Application

The

[GSoC student Guide](https://google.github.io/gsocguides/student/)has some great information[Tips for Prospective Google Summer of Code Students](/ideas/gnu-mailman/tips-20for-20prospective-20google-20summer-20of-20code-20students)(general good advice)[Tips for writing a good GSoC proposal](/ideas/gnu-mailman/spam)(advice on structuring and composing the document; now several years old but mostly valid)



## FAQ

- I am interested to contribute to Mailman and participate in GSOC, how do I start?

[This page](/ideas/gnu-mailman/tips-20for-20prospective-20google-20summer-20of-20code-20students-2) might be of some help.

This question has been asked tons of times on the mailing list (mentioned above) and IRC Channel (again, mentioned above). Both of them are logged publicly and are searchable. It would be really nice to go through them once before you ask the same question again. More specific questions are encouraged and receive more attention than "How do I start?". Mentors do try hard to reply to each and every email to the developers list, but in case you don't get any replies on trivial questions, don't be discouraged. Also, in case you are a student, helping others with small problems for which you know answers is also a great way to get noticed. Don't worry too much about giving wrong answers, list is constantly monitored by the core developers and any mistakes would be corrected.

- I am a beginner, what is the best way for me to contribute?

Issues, bugs and tests are obviously a good way to contribute. But, writing/improving documentation is another great way to contribute for beginners. It doesn't have to be a real commit or patch, write up a detailed blog post about what problems you faced while setting up mailman for development. What parts of mailman you find are difficult to understand? What are awesome things about mailman?

**Note:** To qualify for Google Summer of Code, your proposed project must be a coding project. That's Google's rule. Documentation and tests help to make a substantial contribution, but only count toward GSoC to the extent that they apply to your *new or changed* code. Additional work on documentation or testing is considered a community contribution, which is a consideration in deciding who to accept.

- My MR has been pending for a long time, what should I do?

In most of the cases the reason for a MR to be pending is that there is either something missing or something incorrect. In either of those cases, first check the MR itself and any issues associated with it, to see if there are comment you have missed. If it's not obvious what you need to do next, contact any mentor or the org admin (Steve = yaseppochi@IRC) and we'll look into it, or ask the relevant person. I don't mean that you do that for each one, just the ones that haven't been noticed by anyone for a *long time*. (Use your judgment as to what is "long" when there's a deadline coming up.)


# Project Ideas

This is the list of project ideas. Do communicate with the developers before writing a proposal based on any of these ideas. The developers work individually on issues that catch their eye either as a feature they want, or at a user's request. So somebody may already be working on an idea, and you may be wasting your time to propose it.

If you have an idea not listed here that you'd like to propose , please send it to [mailman-developers@python.org](mailto:mailman-developers@python.org) for discussion! You can also look at the to-do lists for Mailman 3 [here](/ideas/gnu-mailman/dev), and see if anything is interesting enough that you would like to work on it through the summer.

If you saw an idea on an earlier year's page and thought it would be a good project, but it isn't here, most likely it has been implemented and is in the current distribution. Sorry!


## Mentors

The mentor assignments below are tentative. During the application and community bonding phases, your primary contact with the mentors about projects should be through the Mailman Developers mailing list <[mailman-developers@python.org](mailto:mailman-developers@python.org)> for technical questions about the source code and implmentation, the Mailman 3 Users mailing list <[mailman-users@mailman3.org](mailto:mailman-users@mailman3.org)> for questions that touch on user-visible features, or IRC for interactive conversations. Once you have been assigned a project and mentors, you can make alternative arrangements. For *personal* questions, such as known scheduling issues that make it difficult for you to work to the "standard" schedule, contact the organization administrator(s) directly. (GSoC does allow a certain amount of flexibility, but you will need to justify nonstandard schedules.)

Here are the current mentors:

Abhilash Raj (UTC+5.5, maxking on IRC,

[maxking@asynchronous.in](mailto:maxking@asynchronous.in))Stephen J. (Steve) Turnbull (UTC+9, yaseppochi on IRC, yaseppochi.bsky.social on

[BlueSky](https://wiki.list.org/BlueSky),[steve@turnbull.jp](mailto:steve@turnbull.jp))Mark Sapiro (UTC-7,

[mark@msapiro.net](mailto:mark@msapiro.net))- Daniel Toe (UTC)
- Victoriano Giralt (UTC)

Organization administrators:

Stephen J. (Steve) Turnbull (yaseppochi on IRC, yaseppochi.bsky.social on

[BlueSky](https://wiki.list.org/BlueSky),[steve@turnbull.jp](mailto:steve@turnbull.jp))Abhilash Raj (maxking on IRC,

[maxking@asynchronous.in](mailto:maxking@asynchronous.in))


## User Profile Tool

Mailman 3 allows users to set some profile information at several scopes: user-wide, per-address, or per-subscription. While "power users" enjoy the flexibility, others find it inconvenient and confusing that settings at subscription scope don't propagate to the address or user scopes. This is especially annoying when they ask a list administrator to help them, because the list administrator normally doesn't have access to the user profile object, although they do have access to their list roster (including user preferences). For example, here's a [short thread](https://lists.mailman3.org/archives/list/mailman-users@mailman3.org/message/PRYP6ZVFKKOLXWGJBPKDCXPPFOUIKR2N/) on such a problem.

The object of this task is to create and integrate into Postorius a tool which allows the user to easily modify their preferences in any scope, and which helps them to propagate changes where appropriate, and not do so when not. It should probably present initially at user scope, even if invoked from subscription level. It should offer the ability to show a "map" of the scopes in which preferences are set to non-default values. List administrators should be warned about the limitations on their own access. A possible feature (but I haven't thought about it carefully, and don't know if users would want it) would be to send a one-time key to the list admin allowing them to access the user's profile as the user. (This needs careful thought -- should the admin be able to change credentials? other lists' preferences?)


### Requirements

- Level: moderate
- Estimated effort: 175 hours


### Mentors

- Abhilash Raj
- Stephen J. Turnbull


## Moderating Emails and Threads in Hyperkitty

Hyperkitty is GNU Mailman's official archiver. However, it also supports some advanced functionality which allows users to send messages/emails through its web interface.

Moderation of topics being discussed in a Mailing List has been one of the biggest complaints on Mailman Users. Email is a very distributed and open protocol, which makes it hard to restrict users from following up on threads that have been going on for a long time and need to be shut down.

With Hyperkitty, we can tackle this problem by adding moderation actions to specific Email Headers. This allows us to moderate all the replies to a message (In-Reply-To: and References: header fields).


### Requirements

- Level: moderate
- Estimated effort: 175 hours


### Mentors

- Abhilash Raj
- Stephen J. Turnbull


## Support for Encrypted Lists

This is an idea that has been around for a while and there are a number of custom implementations in the wild, we hear. The problem as usual is key distribution and management. The obvious distributed implementation using PGP requires everyone on the list to know everyone else's public key, and to encrypt using *all of them*. The basic idea is to add each subscriber's public key to their profile, so that subscribers only need to know the list's public key. Then the list would do the reencryption. That way subscribers only need to manage two keys: their own and the list's. The devil is in the details. For example, the list is by definition a person in the middle. To what extent can Mailman help to improve site security? A naive implementation would put plaintext on disk. Can that be avoided? What about archives? Some of these questions are design questions, and (for the purpose of GSoC) it doesn't matter how you answer them. But they do need to be answered and *documented*.

The simplest, *low functionality*, model would involve disabling archives, and poster to server and server to subscriber encryption.

A *high functionality* model would offer archives, with some degree of forward security as well as security in transit.

Tags: *core* (securing the core), *postorius* (configuring an encrypted list), *hyperkitty* (archive management)


### Requirements

- Level: hard
- Estimated effort: 175 hours (low functionality) or 350 (high functionality)


### Mentors

- Abhilash Raj
- Stephen J. Turnbull
- Victoriano Giralt


## Improved UI for Subscription Management

This is a collection of small improvements. For example, Postorius currently presents minimal information on the subscriber list page, with a link to each subscription's options page. There should at least be an option to view the most important options as a table, and a link to the subscriber's profile only for verbose or rarely used fields. At present, the list of lists view does not present "private" lists to the logged user, even if they are a subscriber. There should be a option between public and private making lists visible to subscribers but not nonsubscribers.

Tags: *postorius*


### Requirements

- Level: moderate
- Estimated effort: 175 hours


### Mentors

- Abhilash Raj
- Stephen J. Turnbull


## Dynamic Sublists (aka Conversations)

Dynamic sublists are a feature of the Systers fork of Mailman which was never integrated upstream due to entanglement with other, very Systers-specific, features of their fork. The idea is that only the thread root is distributed to all users, and by replying to a special address, a reader can "subscribe" to that thread. Because of divergence of the code bases integration will likely involve some amount of new code. Also, the original feature was controlled entirely by email, but integration with Postorius and [HyperKitty](/ideas/gnu-mailman/hyperkitty) is desirable. Also see [Topics](https://wiki.list.org/DEV/Google%20Summer%20of%20Code%202026#Topics) for a similar feature, but user-controlled.

Tags: *core*


### Requirements

- Level: hard
- Estimated effort: 175 hours (as described above) or 350 hours (for additional functionality, ask us)


### Mentors

- Abhilash Raj
- Stephen J. Turnbull


## Topics

Topics are a feature of Mailman 2 which was never integrated into Mailman 3. The idea is that the list administrator creates a tag for the topic, and a reader can "subscribe" to that topic in the web interface or by email. If a post has an explicit topic and you're not subscribed, you don't get it. Finally there is special "not a topic" tag that you can "subscribe" to, to get posts that are classified as being related to a topic. Because of divergence of the code bases integration and a Python 2 to Python 3 port will likely involve quite a lot of new code. The original feature was controlled entirely by the web interface, but integration with email commands is also desirable. Also see [Dynamic Sublists](https://wiki.list.org/DEV/Google%20Summer%20of%20Code%202026#Dynamic_Sublists_.28aka_Conversations.29) for a similar feature, but user-controlled.

Tags: *core* *topics*


### Requirements

- Level: hard
- Estimated effort: 175 hours (as described above)


### Mentors

- Abhilash Raj
- Stephen J. Turnbull


## HTML Digests

*Thanks to Jay Hamilton-Roth for the suggestion.*

Background: For the non-technical users of MM3, the Mime digest format is only useful on a small subset of email readers (e.g., Outlook and iPad/iPhone Email). The majority of "average" users cannot easily parse nor reply to messages in the digest, making the digest not very useful.

The current digest format is:

1. The masthead from the list:member:digest:masthead template. 2. The digest header if any from the list:member:digest:header template. 3. The table of contents. 4. The individual messages. 5. The digest footer from the list:member:digest:footer template.

For the MIME digest, these are all separate MIME parts and the individual messages are message/rfc822 parts within a multipart/digest part.

For the plain text digest, the digest is one text/plain part containing the above formatted par RFC 1153

Goal: A simple HTML customizable digest format could help to make digests more usable.

Suggestion: Create new html template files (that could live in list:member:htmldigest): masthead, header, footer, tocheader, tocfooter, msgheader, msgfooter. These would allow for customized ornamentation. The masthead would also include the following digest classes by default: .digest_msg_start, .digest_msg_number, .digest_msg_reply, .digest_msg_reply_all, .digest_msg_archive, and .digest_msg_end. List owners could configure any of these classes to set the visibility property to hidden.

This would create a proposed HTML digest format as:

1. The masthead from the list:member:htmldigest:masthead template.

2. The digest header if any from the list:member:htmldigest:header template.

3. The toc header if any from the list:member:htmldigest:tocheader template

4. The table of contents.

5. The toc footer if any from the list:member:htmldigest:tocheader template

6. Foreach message

- The msg header if any from the list:member:htmldigest:msgheader template followed by

<div class="digest_msg_number">message number</div> <div class="digest_msg_title">message subject</div>

- b. message body

<div class="digest_msg_reply"><a href="mailto:SenderURL?subject=message subject">Reply to sender</a> </div> <div class="digest_msg_reply_all"><a href="mailto:ListURL?subject=message subject">Reply to group</a> </div> <div class="digest_msg_archive"><a href="archiveURL">Thread</a></div>

- c. The msg footer if any from the list:member:htmldigest:msgfooter template

7. The digest footer from the list:member:htmldigest:footer template.

For example, the default for htmldigest:msgheader could be <hr>

An HTML digest is probably only greatly useful if you're going to prohibit HTML mail or convert it to plain text in digests. The HTML produced by commercial MUAs is complex, and it's hard to predict how it will interact with the digest formatting.

If HTML mail will be allowed, we would need to examples of what at least the most common mail composers on your lists are going to throw at us. (Somebody else can do the followup work for composers you've never seen. The problem is that we may have to "unwrap" the HTML document and parse the HEAD element to integrate them into a digest correctly and provide a convenient UI.

- I think the high-level structure for the digest itself should be extremely simple, right? A few paragraphs with lists for the table of contents and the messages themselves mixed in.

Tag: core


### Requirements

- Level: moderate (HTML mail prohibited version) or hard (HTML mail allowed)
- Estimated effort: 175 hours (HTML mail prohibited version) or 350 hours (HTML mail allowed)


### Mentors

- Abhilash Raj
- Stephen J. Turnbull


## Configurable Mail Footers

While generally a good idea to have the existing mail footers on mailing list, there exist some mailing lists where having the footers is basically a non-starter. This can currently be achieved by editing the templates directly, but this is obvious cumbersome. This project is intended to focus on piping through Postorius the UI elements needed to configure those footers on a per-list, or per-site basis. (basically give an editor in postorious for the respective `var/templates/domains/<domain>/<lang>/` files)


### Requirements

- Level: moderate
- Estimated effort: to be determined


### Mentors

- Stephen J. Turnbull
- Victoriano Giralt


## Per-list backup

In Mailman 2, the list configurations were stored in list-specific structures as Python *pickles*. Backup of a single list was just a matter of copying the pickle file. Currently there is no way to extract and restore the configuration and membership of a single list from a Mailman 3 installation. This project would involve picking a format such as a Python pickle or a JSON object, extracting the list-specific data from the backing database, and storing it to a file, as well as reversing the process.

Tags: *core*, *postorius*


### Requirements

- Level: medium
- Estimated effort: 175 hours


### Mentors

- Stephen J. Turnbull
Victoriano Giralt



## Shell Completions

Mailman has (at least) two command-line utilities: *mailman*, for list creation, deletion, and querying, as well as starting and stopping the core daemon, and *mailmanweb*, which handles configuration and maintenance of the Django applications Postorius and [HyperKitty](/ideas/gnu-mailman/hyperkitty), as well as starting and stopping them. Both have long, complex lists of subcommands, so it is desirable to have shell completion for these commands. Completion functions for at least *bash* and *zsh* are required, *csh* is desirable, and other shells with completion hooks may be added.

**Note:** *This task may not require a full summer's effort, so additional subtasks may be added.*


### Requirements

- Level: medium
- Estimated effort: 175 hours
- Special skills: shell programming and configuration


### Mentors

- Stephen J. Turnbull
- Victoriano Giralt


## Log Access from the Web UI

Sometimes it would be useful for admins who do not have shell access to the host (domain admins for hosted instances as well as list admins) to view logs through the web UI. This task is rated "hard" not because the filtering problem is complex (it's complex enough to be interesting!), but because of the privacy and security implications of access to the logs. Site admins in particular would often like to get information from the MTA or web server. This would need to be extremely well-done to convince a hosting provider to enable those features.

Tag: Postorius


### Requirements

- Level: hard
- Estimated effort: 175 hours


### Mentors

- Stephen J. Turnbull
- Mark Sapiro


## Implement Domain Administration

Mailman 3 has a hierarchy of administrative privileges, currently:

*site admin*(aka*superuser*, who maintains the software and creates domains and lists)*list owner*(who can see all subscriptions and delegate moderation to other users)*list moderator*(who can approve or disapprove subscriptions and posts)

This task is to implement the *domain owner* role, which allows a domain owner to create lists in a specific domain, as well as exercise the privileges of a list owner for lists in that domain.

Tag: Postorius


### Requirements

- Level: moderate
- Estimated effort: 175 hours


### Mentors

- Stephen J. Turnbull
- Abhilash Raj


## The Generic Project Template

We're open to original proposals from candidates. Trawl the [mailman-users@mailman3.org](https://lists.mailman3.org/mailman3/lists/mailman-users.mailman3.org/) and [Mailman developers mailing list](https://mail.python.org/mailman/listinfo/mailman-developers) mailing list archives and the [GitLab issue trackers](https://gitlab.com/mailman) for user feature requests and proposals. Be careful and consult with us before doing much work on a proposal, though: Google requires a certain *minimum amount of work* (approximately full-time for 10 weeks) and that the work produce *code* (not tests, UI styling, or documentation).

Tag: as appropriate


### Requirements

- Level: to be determined
- Estimated effort: to be determined


### Mentors

- to be determined
