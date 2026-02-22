# GSoC 2024 blog

**Parent:** Haiku — Project Ideas
**Source:** https://www.haiku-os.org/blog/zardshard
**Scraped:** 2026-02-22T23:28:47.590220

---

#### Blog-O-Sphere

[Haiku Activity & Contract Report, January 2026](https://www.haiku-os.org/blog/waddlesplash/2026-02-12-haiku_activity_contract_report_january_2026/)[The Gerrit code review iceberg, episode 5](https://www.haiku-os.org/blog/pulkomandy/2026-02-03-the_gerrit_pending_review_iceberg_5/)[Haiku Activity & Contract Report, December 2025](https://www.haiku-os.org/blog/waddlesplash/2026-01-12-haiku_activity_contract_report_december_2025/)[The Gerrit code review iceberg, episode 4](https://www.haiku-os.org/blog/pulkomandy/2025-12-31-the_gerrit_pending_review_iceberg_4/)[The Gerrit code review iceberg, episode 3](https://www.haiku-os.org/blog/pulkomandy/2025-12-19-the_gerrit_pending_review_iceberg_3/)[Haiku Activity & Contract Report, November 2025 (ft. Go)](https://www.haiku-os.org/blog/waddlesplash/2025-12-12-haiku_activity_contract_report_november_2025/)[The Gerrit code review iceberg, episode 2](https://www.haiku-os.org/blog/pulkomandy/2025-12-05-the_gerrit_pending_review_iceberg_2/)[The Gerrit code review iceberg](https://www.haiku-os.org/blog/pulkomandy/2025-11-24-the_gerrit_pending_review_iceberg/)[Haiku Activity & Contract Report, October 2025](https://www.haiku-os.org/blog/waddlesplash/2025-11-11-haiku_activity_contract_report_october_2025/)[Haiku Activity & Contract Report, September 2025](https://www.haiku-os.org/blog/waddlesplash/2025-10-13-haiku_activity_contract_report_september_2025/)

[[GSoC 2024] Porting WebKit2 Final Report](https://www.haiku-os.org/blog/zardshard/2024-08-16_gsoc_2024_porting_webkit2_final_report/)

The goal of this document is to be an overview of everything I did during GSoC. It should be readable even if you haven’t read any of the previous blog posts and don’t know much about Haiku or WebKit (I hope I succeeded!).

First, some background. Haiku’s native browser is WebPositive.

WebPositive’s code mostly deals with the user interface. It uses our fork of WebKit, HaikuWebKit, to actually render the web pages, run JavaScript, process input, and so on. WebKit (and, by extension, HaikuWebKit) provides two API versions: WebKitLegacy, and WebKit (aka WebKit2). Unfortunately, we are still stuck using WebKitLegacy even though WebKit2 has been out for more than a decade.

[[GSoC 2024] Can I get discuss.haiku-os.org to work?](https://www.haiku-os.org/blog/zardshard/2024-08-13_gsoc_2024_can_i_get_discusshaiku-osorg_to_work/)

So I’ve implemented mouse support. It also turned out to be really easy to fix text rendering. So, what’s next? Well, some websites like [https://discuss.haiku-os.org](https://discuss.haiku-os.org) cause WebKit to crash. This crash also seems to affect other websites. Really, it seems to occur anytime WebKit decides to use multiple bitmaps (actually, in WebKit lingo, backing stores) to render a web page. Rendering a single bitmap is easy, just display it! But when you have multiple, you need to composite them together. It seems like WebKit currently requires EGL and maybe OpenGL to do this.

[[GSoC 2024] Implementing Mouse Support](https://www.haiku-os.org/blog/zardshard/2024-07-31_gsoc_2024_implementing_mouse_support/)

Success! Now MiniBrowser displays things once again. Here is MiniBrowser showing [https://review.haiku-os.org/](https://review.haiku-os.org/)

So, yeah, there’s still plenty of work left to do. Text isn’t rendered properly, keyboard and mouse support is missing, the window can’t be resized without MiniBrowser crashing, and it crashes when exited. I’ll take it one step at a time. Let’s make the mouse work! Then I can actually click on stuff. I think implementing that will be straightforward.

[[GSoC 2024] Drawing to the Screen!](https://www.haiku-os.org/blog/zardshard/2024-07-17_gsoc_2024_drawing_to_the_screen/)

WebKit wasn’t trying to draw anything to the screen. Turns out, it wasn’t aware that it was visible. No use drawing a web page when you’re invisible, right? Well, I told it that it is visible, and now it’s trying to draw to the screen. Of course, it crashes while trying to do so. It hasn’t tried to draw to the screen in ages. Everything is bit rotted!

So far, it looks like this will mostly be a collection of minor tasks. Nothing worthwhile to write about here yet, at least. If I’m lucky, it will stay that way and we can have a nice web page displayed by WebKit pretty soon.

[[GSoC 2024] Fixing IPC in WebKit](https://www.haiku-os.org/blog/zardshard/2024-06-28_gsoc_2024_fixing_ipc_in_webkit/)

WebKit is split into several processes. One of these processes is the browser itself. In my case, this is MiniBrowser, but, hopefully, in the future, it is WebPositive. Since browsers can have any name, WebKit refers to this process as the UIProcess. And, indeed, that process is mainly responsible for the UI. Our port will also be using two other processes: NetworkProcess and WebProcess. Unsurprisingly, NetworkProcess does the networking. WebProcess does all of the work associated with a single web page. For example, it is responsible for running JavaScript and does most of the work for rendering the web page. There is one WebProcess for each web page.

[[GSoC 2024] Fixing the crashing](https://www.haiku-os.org/blog/zardshard/2024-05-28_gsoc_2024_fixing_the_crashing/)

Currently, MiniBrowser (the simple browser that we use to test WebKit2) crashes rather easily. It crashes when it is closed, but that’s not *too* bad. Unfortunately, it also crashes when trying to navigate to a website (shown above)! I will be working on fixing this crash first.

For those who aren’t familiar with WebKit’s code, that’s all I can really say. But if you are familiar, then keep reading. WebKit wants to know how I will fundamentally approach porting WebKit2.

[Building WebKit Sensibly](https://www.haiku-os.org/blog/zardshard/2024-05-15_building_webkit_sensibly/)

WebKit builds can take a lot of space and time to build on Haiku.

To those working on WebKit, welcome! This blog post is primarily for those working on HaikuWebKit, Haiku’s fork of WebKit, but it may also be useful for you.

I will be covering some techniques that are useful to reduce the size of build files without significant disadvantages. I’ll also cover how to speed up linking.

[[GSoC 2024] Plans for Fixing Haiku's WebKit2 Port](https://www.haiku-os.org/blog/zardshard/2024-05-08_gsoc_2024_plans_for_fixing_haikus_webkit2_port/)

So I got accepted into GSoC again! I’m going to be working on WebKit2. But what is WebKit2, or even WebKit, for that matter? Well, WebPositive uses WebKit to render its web pages. Currently, we use the WebKitLegacy API to communicate with WebKit. It would be nice to switch to the newer version: WebKit2. However, our port of WebKit2 still needs work. At present, it has lost its ability to even render any webpage at all! So, getting WebKit2 to work will be the primary goal of my GSoC project. If there’s time left, I might be able to integrate it into WebPositive.

[[GSoC 2023] Improving Icon-O-Matic Final Report](https://www.haiku-os.org/blog/zardshard/2023-08-18_gsoc_2023_improving_icon-o-matic_final_report/)

## What is Icon-O-Matic?

There’s a good chance that not everyone reading this article will know what Icon-O-Matic is, so I’ll start by explaining what it is. Icon-O-Matic is a vector graphics editing program like Illustrator or Inkscape. It is specifically made to work with Haiku’s custom HVIF vector graphics format. This format is similar to the SVG format, except optimized to be much, much smaller. The blog post [“500 Byte Images: The Haiku Vector Icon Format”](http://blog.leahhanson.us/post/recursecenter2016/haiku_icons.html) provides a more in-depth discussion for those interested.

[[GSOC 2023] Progress on perspective transformation](https://www.haiku-os.org/blog/zardshard/2023-06-19_gsoc_2023_progress_on_perspective_transformation/)

While the [change request to add reference images](https://review.haiku-os.org/c/haiku/+/6604) was being reviewed, I started working on [ticket #18415](https://dev.haiku-os.org/ticket/18415), which suggests adding shear and perspective transformations. I decided to implement the perspective transformation since I still need to figure out which way I’m going to implement the shear transformation. Hopefully the experience in implementing the perspective transformation will give me information that will help me decide how to implement the shear transformation.

Handmaus provided two reasons in the ticket for why the perspective transformation would be useful. One example is Patchbay’s icon.
