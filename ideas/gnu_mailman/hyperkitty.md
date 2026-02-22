# HyperKitty

**Parent:** GNU Mailman — Project Ideas
**Source:** https://wiki.list.org/HyperKitty
**Scraped:** 2026-02-22T23:28:47.588087

---

# HyperKitty, the Mailman archiver

HyperKitty is the archiver project for the Mailman 3 suite, allowing users to browse mailing lists, start new threads and reply to existing threads, mark messages as favorite, search archives, and so on. It is a Django-based web application that aims to implement [modern archiving](https://wiki.list.org/DEV/ModernArchiving). It can also run standalone, without the rest of the Mailman suite, to serve as a web forum. It was originally started by the Fedora community.

You can read [the main documentation](http://hyperkitty.readthedocs.org) online. If you want to preview it, there are two demo servers ([1](https://lists-dev.cloud.fedoraproject.org/archives/), [2](https://lists.stg.fedoraproject.org/archives/)) available. They are development servers, so they may be broken or obsolete at the time you access them. It's usually OK, though.


## Developers

The source code is hosted [on GitLab](https://gitlab.com/mailman/hyperkitty). See the [Development Setup Guide](https://wiki.list.org/HyperKitty/DevelopmentSetupGuide).

HyperKitty, being a Django application, can be used with any other Django project. If you are deploying HyperKitty standalone, you'll only need hyperkitty and hyperkitty_standalone.


## Design

We've done some [usability testing](https://wiki.list.org/DEV/Usability) on HyperKitty.

Design mockups are available at: [http://linuxgrrl.com/fedora-ux/Projects/Mailman/Prototype%201/](http://linuxgrrl.com/fedora-ux/Projects/Mailman/Prototype%201/)

More designs are available as blog posts:

[http://blog.linuxgrrl.com/2010/03/16/a-rich-web-interface-for-mailing-lists/](http://blog.linuxgrrl.com/2010/03/16/a-rich-web-interface-for-mailing-lists/)[http://blog.linuxgrrl.com/2012/02/29/7750-pixels-of-mailing-list-thread/](http://blog.linuxgrrl.com/2012/02/29/7750-pixels-of-mailing-list-thread/)


## Contact

Discussion about *using* HyperKitty happens on the [Mailman3 Users](https://lists.mailman3.org/mailman3/lists/mailman-users.mailman3.org/) mailing list, or on IRC: #mailman on Freenode. *Development* discussions occur on the [Mailman Developers](https://mail.python.org/mm3/mailman3/lists/mailman-developers.python.org/) mailing list. Also see the [repositories on GitLab](https://gitlab.com/mailman/hyperkitty), where the issue tracker is also located.
