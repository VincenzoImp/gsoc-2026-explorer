# Q&A: Starter kit upgrade #134

**Parent:** Wagtail — Project Ideas
**Source:** https://github.com/wagtail/gsoc/discussions/134
**Scraped:** 2026-03-10T16:58:40.312972

---

# Q&A: Starter kit upgrade #134

[thibaudcolas](https://github.com/thibaudcolas)asked this question in

[Q&A](https://github.com/wagtail/gsoc/discussions/categories/q-a)

-

|
👋 use this discussion thread for any and all questions relating to our Check out our recommended (optional) |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

## Replies: 8 comments 18 replies

-

|
Hi! I'm exploring the Starter kit upgrade project. I noticed that, unlike some of the other project ideas, this one seems more focused on exploratory improvements rather than fixing predefined issues. To make sure I'm contributing in the most helpful way, would you recommend contributors prioritize small incremental improvements to the news template (e.g., DX, CI, or docs) before the proposal stage? Or is the main expectation to focus on discovery, evaluation, and proposing larger structural improvements? |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Is long-term maintainability the top priority over feature breadth? |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi maintainers, While investigating Also, the backend already includes: `SocialFields` has`social_image` and`social_text` fields`BasePage` has already`appear_in_search_results` field
These just needs connecting in Since, |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi, I’m exploring the
Would the maintainers be open to me submitting a foundational |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi maintainers, I've been exploring -
Add `PageListingViewSet` with`filterset_class` , presenting a flat list of pages of a given type, accessed from a menu-item in Wagtail admin, provides ability to search and filter the list. -
Add `SnippetViewSet` which looks structured and provides more functionality than Traditional Snippet. Also, add search and filter for snippets like`ArticleTopic` , which is more convenient for Snippets with common fields. -
As of now, template is using `GoogleFonts` with external request adding extra overhead and raising GDPR privacy concerns. Also,`@font-face` seems to be partially implemented at`static_src/sass/main.scss` for self-hosted fonts this completes the existing work. -
`SECRET_KEY` is hard-coded in`settings/dev.py` , I think we can use`.env.example` to setup`.env` to solve this. (discussion required)
|

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi maintainers! 👋 I set up the news-template fresh on Windows and ran into a few issues that I think are worth flagging from a newcomer's perspective:
Installing Wagtail via pip gives you
After
Running All three trace back to the same root cause: stale dependency pins with no automation to keep them current. As I'm exploring this area for my GSoC proposal, would a PR bumping dependencies to Wagtail 7.x be a good first contribution? |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
For contributor tasks:
Do you expect us to write a blog post explaining the strength and limitation of original starter kit news template or exploring new integration opportunities with the new technology like Astro and writing understanding of this? |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi! I'm currently exploring the existing news template while thinking about possible directions for the upgrade. One thing I'm curious about is how flexible the starter kit is intended to be in terms of frontend architecture. Right now the template is closely integrated with Django templates, which works well for a traditional Wagtail setup. For the upgrade, would you prefer proposals that mostly iterate on the current template-based structure (for example improving templates, developer experience, or deployment workflows), or would it also possible to be in scope to explore alternative frontend patterns that still keep Wagtail as the content backend? I’m trying to understand how much architectural experimentation would be appropriate versus focusing primarily on improving the existing template approach. Thanks! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)
