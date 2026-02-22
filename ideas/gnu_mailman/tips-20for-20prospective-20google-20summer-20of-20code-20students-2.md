# This page

**Parent:** GNU Mailman — Project Ideas
**Source:** http://wiki.list.org/DEV/Tips%20for%20Prospective%20Google%20Summer%20of%20Code%20Students
**Scraped:** 2026-02-22T23:28:47.587956

---

Mailman usually participates in Summer of Code under the banner of the Python Software Foundation, so you may want to read up on expectations for PSF students:

Mailman has been split into five pieces:

- Mailman core (the part that delivers the messages, manages users, etc.)
- mailman.client (the Python bindings to Mailman core's web API)
[HyperKitty](http://wiki.list.org/HyperKitty)(the archiver)- the bundler (scripts that make it easier for administrators to install everything together)

All three projects are working together, so you'll notice we often just say "Mailman" rather than specifying Mailman/Postorius/HyperKitty.

Mailman is looking for students who...

- are able to contribute useful features to Mailman
- are able to communicate well with existing developers

So if you're wondering how to impress us, keep those in mind!

To demonstrate your ability to contribute useful features, here's a few things you can do:


- Set up your development environment
Fix a bug


- each project has a tag for easy or beginner bugs; you probably want to start there but feel free to work your way up
use

[the official Python style guide](http://www.python.org/dev/peps/pep-0008/)to make sure your code looks and feels right- Don't forget to publish your code and submit a merge request!

Try to duplicate bugs that haven't been fixed


- You may be able to help diagnose the problem or close bugs that cannot be duplicated
- Don't forget to comment on the bug to say if you duplicated it or add any information you found that might help

- Try to create new automated regression tests
- Even if you know you want to work with a specific piece of Mailman, try out Mailman core, Postorius and Hyperkitty so you know what to expect from all of them
- Take a look at required skills on the idea page and practice with anything you haven't used recently

To demonstrate your ability to communicate with us, here's some things you can do:


Sign up for the mailman-developers mailing list and introduce yourself, ask questions and participate in discussions


- Remember to do things like use good subject lines, etiquette, etc.

Show up on IRC and talk to us


- we can most often be found on #mailman on libera.chat
- Remember to be patient if you do not get a response right away; many of us are on IRC from work and may not be able to answer immediately

Contribute to the wiki


- We can always use more information to help beginners get set up, so even documenting how you got set up could be useful!

File bug reports


- You may find things when you're setting yourself up, or feel free to just experiment and see what works and doesn't work

Help other people


- Sometimes all you need to do is search the FAQ on the wiki and help them find relevant entries
- Sometimes just asking questions about their problem can help a lot, even if you don't know the answer
- This includes other prospective GSoC students -- we can be very swamped with questions as application time approaches and you'll especially impress us if you can make the mentoring process easier for us!



**You are not required to do everything on this list to get accepted as a Summer of Code student.** But we've been getting a lot of questions from students about "what can I do right now?" so this is a list of ideas of things you can do while you're waiting for the applications to open.

Other tips:

- Don't forget that you can suggest your own project, but make sure you talk to us to help you refine your proposal
- Do choose a project you're confident you can finish, but add some "stretch goals" for things you'd love to do if things go well
- Don't aim too low: we only have a limited number of slots and mentors, so we're more likely to choose projects that maximize what we get out of the summer
- Do ask lots of questions: we know it can be difficult to get started
- But on the other hand... try demonstrate that you're able to solve some problems on your own: do google searches, experiment, etc. if you get stuck
- Do be patient
**Do use the mailing lists whenever possible**: because our mentors are busy folk, it's better to ask *everyone* than to talk to one person privately. You're much more likely to get a response.


### FAQs

**Q: How should I prepare for Google Summer of Code?**

A: Google Summer of Code needs you to interact with the community and familiarize yourself with the codebase of the software. The best way to do this to set up a development environment locally. Try not using an automated process (if any exits for the particular software you want to work on). After that visit the bug-tracker of the software and try finding a bug that suits you. It may be a little difficult to find your first bug, search for tags like **beginner-friendly** or **easy** or something like that. For mailman filter the bugs with **easy** and **mailman3** tags.

**Q: I have a question, now what should I do?**

A: Its good to have doubts, but be sure that you yourself read extensively before asking one of the mentors or posting to developers list. I have told students time and again that, most of the answers are in the wiki or documentation of the respective projects, look into it yourself before asking. If you still don't find an answer, you can ask your mentors using the communication channels mentioned on their ideas page. Very often you don't get response on IRC instantaneously, try to be patient. Also you'd have answers faster if you collect a small set of doubts and send in an email to developers list, most of the mailman developers don't hang out much on IRC, or are too busy to reply there.

**Q: Should I email one of the mentors personally?**

A: Its generally not a very good idea, unless he/she expects you to. Ideas page of mailman does have email addresses of all the mentors, but it is encouraged that you send emails to entire developers list. If a mentor is interested to help you out, they'd simply reply to your post. Having said that, if you strongly feel like sending a personal query to one of the mentors, you should go ahead and do that.
