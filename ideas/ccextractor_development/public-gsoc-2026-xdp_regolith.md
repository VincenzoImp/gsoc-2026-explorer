# Create an XDG Desktop Portal backend for regolith

**Parent:** CCExtractor Development — Project Ideas
**Source:** https://ccextractor.org/public/gsoc/2026/xdp_regolith
**Scraped:** 2026-03-10T16:58:40.225374

---

# Create an XDG DESKTOP PORTAL backend for regolith

**Mentor:** Soumya Ranjan Patnaik

**Time Estimation** 350 hours

### Project Brief

[XDG Desktop Portal](https://github.com/flatpak/xdg-desktop-portal) or `XDP`

is
a service that provides applications with standardized interfaces to interact
with the host system's desktop environment. It was originally designed for
exposing functionality to flatpaks without sacrificing the security of the
sandbox.

The portal interfaces are exposed to application via DBus, and are implemented
by backends which are usually specific to the desktop environment. You can find
examples and links to the source code for portal backends
[here](https://github.com/flatpak/xdg-desktop-portal?tab=readme-ov-file#using-portals)

As of today, Regolith doesn't have a working `xdg-desktop-portal`

backend. This
means apps that rely on `XDP`

may not work.

### Your Job

Create a working xdg-desktop-portal backend for regolith.You can either create
one from scratch, or fork one of the existing ones. You do not need to implement
all the interfaces as
[ xdg-desktop-portal-gtk](http://github.com/flatpak/xdg-desktop-portal-gtk)
already implements many of them.

You can also use the no-op backend provided by regolith, i.e.
[ xdg-desktop-portal-regolith](https://github.com/regolith-linux/xdg-desktop-portal-regolith),
as a starting point, which is a fork of

[, which is the backend used by elementary OS.](https://github.com/elementary/portals)

`xdg-desktop-portal-pantheon`

### Qualification tasks

Figure out the portals that are not available in

`xdg-desktop-portal-gtk`

or don't work as expected. DynamicLauncher, Documents, Permission Store and Location are some examplesCome up with a plan and prove that you can execute on it by doing its initial steps. Bonus points if you can get ANY one of the interfaces, which are currently unimplemented to work on regolith (it should work in xdp)


### Resources

- Official documenation for creating portal backends can be found
[here](https://flatpak.github.io/xdg-desktop-portal/docs/backends.html) - There is an excellent
[talk](https://www.youtube.com/watch?v=XIGxKyekvBQ&t=9467s)by one of the maintainers of`xdg-desktop-portal`

, which might be one of the best resources learn about understand portals, second only to the documenation Watch from`2:37:47`

to`3:08:07`

.

#### Notes

- You will have to implement GUI prompts for users to allow/deny permissions to access certain portals. You may also need to keep track of accepted and denied permissions
- The portals backend should support the Wayland session as well as the X11
- You can install the
[ASHPD demo](https://flathub.org/apps/com.belmoussaoui.ashpd.demo)application to test which interfaces work and which don't. You can also use it to test your custom XDP backend implementation session.
