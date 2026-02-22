# Django Software Foundation — Project Ideas

**Source:** https://code.djangoproject.com/wiki/SummerOfCode2026
**Scraped:** 2026-02-22T23:28:47.630604

---

-
[Google's Summer of Code 2026](https://code.djangoproject.com#GooglesSummerofCode2026)-
[Mentors](https://code.djangoproject.com#Mentors) -
[Students](https://code.djangoproject.com#Students) -
[How can I improve my chances of being accepted?](https://code.djangoproject.com#HowcanIimprovemychancesofbeingaccepted) -
[Communication](https://code.djangoproject.com#Communication) -
[Ideas](https://code.djangoproject.com#Ideas) -
[Experimental feature flags and processes](https://code.djangoproject.com#Experimentalfeatureflagsandprocesses) -
[Add types to parts of Django](https://code.djangoproject.com#AddtypestopartsofDjango) -
[Add ergonomic control over behaviour of missing variables in templates](https://code.djangoproject.com#Addergonomiccontroloverbehaviourofmissingvariablesintemplates) -
[Switch to Playwright tests for integration testing](https://code.djangoproject.com#SwitchtoPlaywrighttestsforintegrationtesting) -
[Add support for generate_series in postgres](https://code.djangoproject.com#Addsupportforgenerate_seriesinpostgres) -
[[PLACEHOLDER] Project name](https://code.djangoproject.com#PLACEHOLDERProjectname) -
[Or Create Your Own](https://code.djangoproject.com#OrCreateYourOwn)

-


# Google's Summer of Code 2026

Django is a mentor organization for the 2026 Google Summer of Code.
Read [Google's page](https://summerofcode.withgoogle.com) for more information on how the program works.

Django's GSoC program is being coordinated by Bhuvnesh Sharma and Apoorv Garg.

## Mentors

If you're interested in mentoring -- supervising a student in work on Django-related activities -- please let us know: [https://forum.djangoproject.com/t/call-for-project-ideas-and-prospective-mentors-for-gsoc-2025/38017](https://forum.djangoproject.com/t/call-for-project-ideas-and-prospective-mentors-for-gsoc-2025/38017)

## Students

Student application period runs until March 31st, 2026.

If you'd like to get started on your proposal early, we'll be looking for a few things.

- You'll need to have a concrete task in mind along with a solid idea of what will constitute "success" (you tell us).
- If your proposal is a single large feature, library or site, you'll need to present
a detailed design specification. This proposal should be posted to
[the Django Forum](https://forum.djangoproject.com/c/internals/mentorship/10), where it can be refined until it is accepted by the developer community. - We'll want to know a bit about you -- links to previous work are great, if any. If you're proposing something ambitious, you'll need to convince us that you're up to the task.
- You'll also need to provide us with a schedule, including a detailed work breakdown and major milestones so your mentor can know if and when to nag you :)

Here's an example of an accepted proposal from a previous year:

Note that none of the ideas below are good enough to be submissions in their own right (so don't copy and paste)! We'll want to know not just what you want to do but how you plan to pull it off.

Don't feel limited to the ideas below -- if you've got a cool project you want to work on, we'll probably be able to find you a mentor. We plan on approving as many projects as we possibly can.

We're accepting any GSOC proposal that fits one of the following three categories:

- Work on Django itself - such as the ORM, forms, etc. This is what we've traditionally accepted GSoC entries in.
- Work on tools to support Django - the issue tracker dashboard (
[https://dashboard.djangoproject.com/](https://dashboard.djangoproject.com/)) is a good example of an existing tool that would have fit into this category. - Work on libraries that supplement or add new features to Django to ease development -
`django-stubs`

and Django Debug Toolbar are good examples of existing projects that would have fit here.

Here are the projects that were accepted last year: [https://summerofcode.withgoogle.com/archive/2025/organizations/django-software-foundation-8o](https://summerofcode.withgoogle.com/archive/2025/organizations/django-software-foundation-8o)

Unless explicitly mentioned below, we're **not** looking for people to work on
existing third-party libraries - we aren't able to guarantee commit access to
them. We may allow an exception if a maintainer of the library in question
agrees to help mentor beforehand.

The broadening in scope is to allow people to work on new ideas to help Django development and developers without tying you down to having to implement it in the core codebase (and thus ruling out some projects that might otherwise be useful).

We're still going to be strict with what we accept - you'll need to provide a strong use case for your idea and show that it would be useful to a majority of developers or significantly improve the development of Django itself.

We're not looking for small groups of incremental updates - like "improve Django's Trac" - nor are we looking for impossible tasks, like "replace Trac with this brand new issue tracker I'm writing". What you propose should be a single project, achievable within the time period of GSoC, and something the core developers can help mentor you on.

We're also not looking for sites or projects that are merely written in Django — this GSoC is not for you to propose your new forum hosting site or amazing Django-based blogging engine.

Note that when you contribute code, you will be expected to adhere to the same
contribution guidelines as any other code contributor. This means you will be
expected to provide extensive tests and documentation for any feature you add,
you will be expected to participate in discussion on the
[Django Forum](https://forum.djangoproject.com) when your topic of interest is
raised. If you're not already familiar with [Django's contribution guidelines](http://docs.djangoproject.com/en/dev/internals/contributing/), now would be a good time to read them - even if
you're not applying to work on Django core directly, we'll still want the same
level of contribution.

## How can I improve my chances of being accepted?

The best thing you can do to improve your chances to be accepted as a Django
GSoC student is to start contributing now. Read up on [Django’s contribution documentation](https://docs.djangoproject.com/en/dev/internals/contributing/) and make yourself known to the other contributors by your
contributions (ideally, related to the area of your proposal). That way, when
it comes time to evaluate student applications, you’ll be a **known individual**
and more likely to be able to get the attention you need to develop a proposal.

We're looking for candidates who can demonstrate that they can engage in work of a project scope on an independent basis. We're there to help but we can't watch you every step of the way, so we need to see that motivation from you. Being active before the submissions process is the best way to demonstrate this.

## Communication

All GSOC-related communication is handled via the [Django Forum, in the Mentoring channel](https://forum.djangoproject.com/c/internals/mentorship/10). Any proposals for GSoC should be submitted there, as
well as discussion on the proposed projects and any updates that students post.

Please be careful to keep content to the forum clear and purposeful; if you have an idea, update, or criticism, please make sure you describe it in detail; it can be tedious asking people to clarify any vague statements.

## Ideas

Here are some suggestions for projects students may want to propose (please
feel free add to this list!). This isn't by any means the be-all and end-all of
ideas; please feel free to submit proposals for things not on this list.
Remember, we'd much prefer that you posted a draft proposal and your rough
timeline / success conditions to the the [Django Forum, in the Mentoring channel](https://forum.djangoproject.com/c/internals/mentorship/10),
even if it's already on the list below; it will help you get feedback on
choosing the right part of a problem, as well as helping to see if there is any
interest before you start drafting a full proposal.

When developing your proposal, try to scope ideas/proposals to size of your project (175hrs or 350hrs) -- you need to be ambitious, but not too ambitious. The GSoC does not cover activities other than coding, so certain ideas ("Write a more detailed tutorial" or "Create demonstration screencasts") are not suitable for inclusion here.

On the other side, though, be sure to be concrete in your proposal. We'll want to know what your goals are, and how you plan to accomplish them.

The project ideas below list key skill, but all assume a knowledge of Python, and familiarity with Django itself.

In no particular order:

## Experimental feature flags and processes

| Difficulty | Hard |
| Size | 350hr |
| Mentors | Andrew Miller |
| Key Skills | Python, Django, Documentation |

The current development process of Django is slow. This is in part due to our commitment to backwards compatibility. This means it is hard to test a new feature API directly in django/django because if we get it wrong we can't easily change it. We would like to define what it would mean to add features considered experimental to django/django that would possibly make development of Django faster.

An outcome of this would be updated processes and documentation around feature development process, followed by any code to support enabling experimental support for new features and for extending existing features. It will start by refreshing DEP 2: [https://github.com/django/deps/blob/main/draft/0002-experimental-apis.rst](https://github.com/django/deps/blob/main/draft/0002-experimental-apis.rst)

There are multiple extension points to this project:

- Extending to refreshing the re-usable apps tutorial and possibly providing a django app template repository.
- Picking a suitable proposed feature to test the new process and code
- Extending this feature to provide a public feature flag API inside django/django

Complete discussion here: [https://github.com/django/new-features/issues/3](https://github.com/django/new-features/issues/3)

## Add types to parts of Django

| Difficulty | Hard |
| Size | 350hr |
| Mentors | Thibaut Decombe |
| Key Skills | Python, Django |

Right now, when working with Django, it’s quite common to refer back to the documentation just to understand what a function returns or what types its arguments expect. Although this idea has been proposed several times before, the Python typing ecosystem has matured significantly, making it a more practical direction today. There are certainly areas — particularly the ORM — where typing can be challenging or may even introduce complexity that outweighs the benefits. However, other parts of Django, such as request and response objects, URL routing, and class-based views, stand to gain clear usability improvements from better type support.

We see [this comment](https://forum.djangoproject.com/t/revisiting-types-in-django-dep-14/37832/11) by Simon Charette as a good starting point for gradually introducing types, with the ORM being an especially valuable area where typing could help contributors reason about the codebase more effectively. The scope would include defining the necessary protocols and applying them throughout the ORM. This effort would also involve exploring CI integrations for type checking and deciding how types should be presented in the documentation — whether they should appear in every relevant definition, only in selected examples, or be omitted entirely.

This would also help solve many of the issues here [https://groups.google.com/g/django-developers/c/at-G0hZrfXE](https://groups.google.com/g/django-developers/c/at-G0hZrfXE).

Github reference: [https://github.com/django/new-features/issues/23](https://github.com/django/new-features/issues/23)

## Add ergonomic control over behaviour of missing variables in templates

| Difficulty | Medium |
| Size | 350hr |
| Mentors | TBD |
| Key Skills | python, django, template internals |

Templates silently convert missing variables to an empty string. This behaviour is useful in many situations:

Pages still render instead of returning a 500 error when a minor programming error is made. Template authors can deliberately design a section to be omitted when variables are not in the context. However, this implicit behaviour is inconvenient for people who want to get an error during development when a variable that should always be present is omitted by mistake. By adding explicit syntax for required and optional variables, we give developers and teams extra control to opt-in to the desired behaviour where appropriate.

Github reference: [https://github.com/django/new-features/issues/5](https://github.com/django/new-features/issues/5)

## Switch to Playwright tests for integration testing

| Difficulty | Medium |
| Size | 175 hr |
| Mentors | TBD |
| Key Skills | python, django, playwright, CI/CD, testing |

This project aims to modernize Django’s integration testing by introducing Playwright as an alternative to Selenium. The work includes integrating Playwright with Django’s test framework, migrating existing browser-based tests, and ensuring compatibility with Django’s CI infrastructure. The goal is to improve test reliability, performance, and developer experience for Django core contributors.

Full reference: [https://github.com/django/new-features/issues/13](https://github.com/django/new-features/issues/13)

## Add support for generate_series in postgres

| Difficulty | Hard |
| Size | 350hr |
| Mentors | Sage Abdullah, Lily (needs confirmation) |
| Key Skills | django, python, postgres, ORM |

This project aims to extend Django’s ORM with native support for PostgreSQL’s `generate_series`

function. Currently developers must use raw SQL to access this powerful function. The work involves designing ORM expressions or query APIs to integrate `generate_series`

in a way that feels natural within Django’s ORM, writing tests, and ensuring compatibility with Django’s PostgreSQL contrib utilities.

References:

[https://github.com/django/new-features/issues/25](https://github.com/django/new-features/issues/25)[https://forum.djangoproject.com/t/proposal-add-generate-series-support-to-contrib-postgres/21947](https://forum.djangoproject.com/t/proposal-add-generate-series-support-to-contrib-postgres/21947)

## [PLACEHOLDER] Project name

| Difficulty | Medium or Hard |
| Size | 175hr or 350hr |
| Mentors | (need confirmation) |
| Key Skills | - |

Project description including the expected outcome of the project.

## Or Create Your Own

We have around 900 accepted tickets on Django. Browse the issue tracker by
component — here's an
[example filter for contrib.staticfiles](/ideas/django-software-foundation-8o/query). What's the bit of the framework that interests you?
What contribution do you want to make to it?

Use the tickets as guides here. Remember the advice above, that your project needs to be both on Django itself here, and achievable in the timescale of GSoC.

Could be scoped as a 175hr or a 350hr project, depending on your idea.

We're open to all good ideas!

[Last modified](https://code.djangoproject.com/wiki/SummerOfCode2026?action=diff&version=6)

[27 hours ago](/ideas/django-software-foundation-8o/timeline)Last modified on Feb 21, 2026, 1:36:21 PM

**Note:**See

[TracWiki](/ideas/django-software-foundation-8o/tracwiki)for help on using the wiki.
