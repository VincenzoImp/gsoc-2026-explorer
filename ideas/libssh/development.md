# https://www.libssh.org/development/

**Parent:** libssh — Project Ideas
**Source:** https://www.libssh.org/development/
**Scraped:** 2026-02-22T23:28:47.566090

---

## Git

Please find relevant information at the bottom of the [download](https://www.libssh.org/get-it/) page.

## Bug Tracking

The development takes place at [gitlab.com/libssh/libssh-mirror/](https://gitlab.com/libssh/libssh-mirror/). You can report bugs there and submit Merge Request and get CI.

## Commercial support

Some libssh developers are able to provide commercial support as well as on-demand features development and ports. Please email us at [support@libssh.org](mailto:support@libssh.org) for more information.

## Copyright Policy

libssh is a project with distributed copyright ownership, which means we prefer the copyright on parts of libssh to be held by individuals rather than corporations if possible. There are historical legal reasons for this, but one of the best ways to explain it is that it’s much easier to work with individuals who have ownership than corporate legal departments if we ever need to make reasonable compromises with people using and working with libssh.

We track the ownership of every part of libssh via [git](https://git.libssh.org/), our source code control system, so we know the provenance of every piece of code that is committed to libssh.

So if possible, if you’re doing libssh changes on behalf of a company who normally owns all the work you do please get them to assign personal copyright ownership of your changes to you as an individual, that makes things very easy for us to work with and avoids bringing corporate legal departments into the picture.

If you can’t do this we can still accept patches from you owned by your employer under a standard employment contract with corporate copyright ownership. It just requires a simple set-up process first.

We use a process very similar to the way things are done in the Linux Kernel community, so it should be very easy to get a sign off from your corporate legal department. The only changes we’ve made are to accommodate the license we use, which is [LGPLv2](http://www.gnu.org/licenses/lgpl-2.0.html) (or later) whereas the Linux kernel uses [GPLv2](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

The process is called signing.

## How to sign your work

Once you have permission to contribute to libssh from your employer, simply email a copy of the following text from your corporate email address to:

[contributing@libssh.org](mailto:contributing@libssh.org)

```
libssh Developer's Certificate of Origin. Version 1.0
By making a contribution to this project, I certify that:
(a) The contribution was created in whole or in part by me and I
have the right to submit it under the appropriate
version of the GNU General Public License; or
(b) The contribution is based upon previous work that, to the best of
my knowledge, is covered under an appropriate open source license
and I have the right under that license to submit that work with
modifications, whether created in whole or in part by me, under
the GNU General Public License, in the appropriate version; or
(c) The contribution was provided directly to me by some other
person who certified (a) or (b) and I have not modified it.
(d) I understand and agree that this project and the contribution are
public and that a record of the contribution (including all
metadata and personal information I submit with it, including my
sign-off) is maintained indefinitely and may be redistributed
consistent with the libssh Team's policies and the requirements of
the GNU GPL where they are relevant.
(e) I am granting this work to this project under the terms of the
GNU Lesser General Public License as published by the
Free Software Foundation; either version 2.1 of
the License, or (at the option of the project) any later version.
http://www.gnu.org/licenses/lgpl-2.1.html
```


We will maintain a copy of that email as a record that you have the rights to contribute code to libssh under the required licenses whilst working for the company where the email came from.

Then when sending in a patch via the normal mechanisms described above, add a line that states:

```
Signed-off-by: Random J Developer <random@developer.example.org>
```


using your real name and the email address you sent the original email you used to send the libssh Developer’s Certificate of Origin to us (sorry, no pseudonyms or anonymous contributions.)

That’s it! Such code can then quite happily contain changes that have copyright messages such as:

```
(c) Example Corporation.
```


and can be merged into the libssh codebase in the same way as patches from any other individual. You don’t need to send in a copy of the libssh Developer’s Certificate of Origin for each patch, or inside each patch. Just the sign-off message is all that is required once we’ve received the initial email.

Have fun and happy libssh hacking!

The libssh Team
