# GSoC 2018 Solvers Progress

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/wiki/GSoC-2018-Solvers-Progress
**Scraped:** 2026-02-22T23:28:47.571178

---

# GSoC 2018 Solvers

* Students: Yathartha Joshi
* Mentors: Amit Kumar
* Github: [Yathartha22](https://github.com/Yathartha22)
* Blog Link  : [Link](http://yathartha22.github.io)
* PR(s) : https://github.com/sympy/sympy/pulls/Yathartha22

### PLEASE UPDATE THE TABLE BELOW

| Week # | Goals | Blog Post | Status/PR Links (if any) |
| ---------- | --------------- | ----- | ---------- |
| Community Bonding | transolve | [The plan](https://yathartha22.github.io//gsoc-week-1) | --
|1| design and document transolve|[Week 1](https://yathartha22.github.io//gsoc-week-1) | [# 14736](https://github.com/sympy/sympy/pull/14736)
|2| Implementing transolve| [Week 2](https://yathartha22.github.io//gsoc-week-2) |[# 14736](https://github.com/sympy/sympy/pull/14736)
|3| Continuing with transolve| [Week 3](https://yathartha22.github.io//gsoc-week-3)|[# 14736](https://github.com/sympy/sympy/pull/14736)
|4| Finishing transolve and starting logsolver| [Week 4](https://yathartha22.github.io//gsoc-week-4)|[# 14736](https://github.com/sympy/sympy/pull/14736), [# 14792](https://github.com/sympy/sympy/pull/14792)
|5| Implementing log solver | [Week 5](https://yathartha22.github.io//gsoc-week-5) | [# 14736](https://github.com/sympy/sympy/pull/14736), [# 14792](https://github.com/sympy/sympy/pull/14792)
|6| Continuing with transolve | [Week 6](https://yathartha22.github.io//gsoc-week-6) | [# 14736](https://github.com/sympy/sympy/pull/14736), [# 14792](https://github.com/sympy/sympy/pull/14792)
|7|  Wrapping up transolve | [Week 7](https://yathartha22.github.io//gsoc-week-7) | [# 14736](https://github.com/sympy/sympy/pull/14736), [# 14792](https://github.com/sympy/sympy/pull/14792)
|8| Continuing with log solver | [Week 8](https://yathartha22.github.io//gsoc-week-8) | [# 14792](https://github.com/sympy/sympy/pull/14792)
|9| Starting up with lambert solver | [Week 9](https://yathartha22.github.io//gsoc-week-9) | [# 14889](https://github.com/sympy/sympy/pull/14889), [# 14972](https://github.com/sympy/sympy/pull/14972)
|10| Wrapping log solver | [Week 10](https://yathartha22.github.io//gsoc-week-10) | [# 14792](https://github.com/sympy/sympy/pull/14792)
|11| Continuing with lambert solver | [Week 11](https://yathartha22.github.io//gsoc-week-11)| [# 14972](https://github.com/sympy/sympy/pull/14972)
|12| Finishing with logarithmic solver | [Week 12](https://yathartha22.github.io//gsoc-week-12) | [# 14792](https://github.com/sympy/sympy/pull/14792), [# 14972](https://github.com/sympy/sympy/pull/14972), [# 15075](https://github.com/sympy/sympy/pull/15075)

## Meeting Schedule

### Meeting #01
* Date: Friday 11th May, 2018
* Time: 3:00 PM - 4:00 PM (IST)
* Attendees: Yathartha Joshi, Amit Kumar

#### Minutes of Meeting:
- Plans for community bonding period

  Since most of the time of community bonding period, I will be having my examinations and practicals upto 18 
  May 2018, so I will be contributing full time after that.

- Frequency of meetings

  Another thing that was discussed was the frequency of meetings. So Amit and I agreed upon having meetings on 
  weekly basis, probably Saturday/Sunday. Also, Amit suggested on having a gitter channel for discussions on 
  Solvers project and giving updates on the progress.

- Plan for implementing transolve.

  How transolve will be implemented and what will be its flow was discussed. Amit suggested on having a thorough 
  understanding of `_tsolve` and its workflow. What makes it is so powerful, its pros and cons and everything 
  should be noted down and taken care while implementing in `transolve`. Also all its tests needs to be imported 
  to `solveset` to make it atleast as powerful as `solve`


#### Goals

 - Documenting how transolve works, how it is better than `_tsolve`.
 - Design of the api of transolve. 
 - Objectives to be taken care while designing: extensibility, proof of correctness, readablity, seperation of concern etc.

#### Pull Requests to review (if any): 
- [14736](https://github.com/sympy/sympy/pull/14736)

### Meeting #02
* Date: Sunday,  27th May 2018
* Time: 10:30 A.M - 11:30 A.M (IST)
* Attendees: Yathartha Joshi, Amit Kumar, Harsh Gupta

#### Minutes of Meeting:
- I have started working on the design of the API of `transolve`. Amit have stressed on making `transolve` extensible and modular to which I suggested an idea of making transolve solve equation in two steps: first, identifying the type of the equation and second, solving the equation. Both these will have heuristics implemented in helper functions making it completly modular.

- Another aspect should be making transolve extensible. The design of the transolve should be such that it should be an easy task to add a new class of equations.

- Proof of correctness

  Every helper implemented with some heuristics should have a proof of correctness. Amit and Harsh sugggested 
  that every helper solver should contain documentation of how it solves the equation with examples explaining 
  it.

- Proper documentation

  Amit also suggested to write a descriptive documentation for transolve. Following points should be covered 
  while documenting:
    - Why and how `transolve` is better than `_tsolve`.
    - How `transolve` solves equations.
    - Way to add new class of equations.
    - Examples.
    - Should be readable.

  For this Amit and Harsh suggested to have a read of the [ode](https://github.com/sympy/sympy/blob/master/sympy/solvers/ode.py) module.

#### Goals
- Importing all tests from solve.
- Writing proper and descriptive documentation.
- Proper design of API and proof of correctness of helpers.

#### Pull Requests to review (if any): 
- [14736](https://github.com/sympy/sympy/pull/14736)

### Meeting #03
* Date: Friday, 8th June 2018
* Time: 10:30 AM - 11:30 AM (IST)
* Attendees: Yathartha Joshi, Amit Kumar

#### Minutes of Meeting:

- Amit pointed out few changes that need to be made in the documentation: adding proof of correctness, typos,
making it more descriptive and accurate. Also building the documentation for sphinx

- We agreed upon for making exponential solver only work for real domain as of now.

- Importance of the `flag` variable was discussed, we concluded that it should not be used as of now, as there is no case that would be solved by its inclusion, including it would rather make things complicated.

- Also, Amit suggested on getting the coverage report of the `solveset` that would help in determining the extent to which tests are taken care.

- Initial plan for logsolver was discussed. A separate PR would be created in this regard.

- Also work should be started on lambert equations.

- Amit also suggested on reading the book [Clean Code](https://www.investigatii.md/uploads/resurse/Clean_Code.pdf) which will help in writing clean and efficient code.

#### Goals

- Bulding the documentation for Sphinx
- Generating coverage report.
- Implementing log solver
- reading book
- finishing PR #14736

#### Pull Requests to review (if any):

[#14736](https://github.com/sympy/sympy/pull/14736/), [#14792](https://github.com/sympy/sympy/pull/14792)


### Meeting #04
* Date: Friday, 16th June 2018
* Time: 11:00 AM - 12:00 AM (IST)
* Attendees: Yathartha Joshi, Amit Kumar

#### Minutes of Meeting:

- Amit suggested on making the `transolve's` API look clean, make it modular (if necessary)
- Working on the way identification of the exponential equation will take place was discussed. Idea was to make it general purpose. Equations of exponential type but not solvable should return unsolved object rather than getting into any other solver.
- Similarly of identification of logarithmic equations, using `logcombine` was basis of identication. Amit advised that the identifier should identify a certain class of log equations. We can propbaly have a different identifier and helper for any other logairthmic class if we encounter in future.

#### Goals
- Adding internal helpers for particular class of equations (`add_type`, etc.).
- Making identification expo and log identifiers general in approach.
- Documentation changes
- Getting familiar with the way `solve` solves lambert type equations

#### Pull Requests to review (if any):

[#14736](https://github.com/sympy/sympy/pull/14736/), [#14792](https://github.com/sympy/sympy/pull/14792)

### Meeting #05
* Date: Saturday, 23th June 2018
* Time: 11:00 AM - 12:00 AM (IST)
* Attendees: Yathartha Joshi, Amit Kumar

#### Minutes of Meeting:

- More discussions took place to finalise the design of the `transolve`: making internal helpers wherever necessay, importtance of a loop within `transolve` to tranverse the `rhs` of the equations, naming conventions of all the identofying and solving helpers.
- Discussions with Amit alongwith Chris suggestions in the PR, let us to conclude that `transolve` should be used as an independent function rather it should only be used to solve specific class of the equations.
- Number of parameters of each and every helper should be same to maintain consistency.

#### Goals
- Working over the design changes and consequently the documentation changes.
- Making API of the helpers consistent.
- Working on improving log solver.

#### Pull Requests to review (if any):
[#14736](https://github.com/sympy/sympy/pull/14736/), [#14792](https://github.com/sympy/sympy/pull/14792)

### Meeting #06
* Date: Sunday, 1 July 2018
* Time: 11:00 AM - 12:00 AM (IST)
* Attendees: Yathartha Joshi, Amit Kumar

#### Minutes of Meeting:

In this meeting we mainly discussed about `logarithmic equations`. Following points were discussed:
- What should `_is_logarithmic` return? Rather than returning a modified eqution, `True` or `False` should be returned. This will maintain the consistency.
- Working of the `logarithmic solver`: We discussed on two ways to achieve identification, either use `logcombine` or look for log terms having symbols. Amit advised on to use the first approach to atleast handle cases that we can solve.
- Removing unwanted solutions from the result, there could be spurious solutions gathered by `_solveset` while solving the modified equation. Amit suggested to have a look over singularities and try incorporating a check in `_solveset`.

#### Goals
- Improvements in `_is_logarithmic` and `_solve_logarithmic` as per the discussions
- Removing singularities for log equations.

#### Pull Requests to review (if any):
[#14736](https://github.com/sympy/sympy/pull/14736/), [#14792](https://github.com/sympy/sympy/pull/14792)

### Meeting #07
* Date: Sunday, 8 July 2018
* Time: 11:00 AM - 12:00 AM (IST)
* Attendees: Yathartha Joshi, Amit Kumar

#### Minutes of Meeting:
- Amit suggested on having consistency among logarithmic and exponential helpers.
- Finaling PR #14736.
- Few leftover for the PR #14792
- Discussions on how lambert solver would be implemented in `solveset`. Amit suggested to go through the tests in `solve` and look into the working of `_tsolve` for lambert types

#### Goals
- Making PR #14736 ready to merge.
- Finalising work on PR #14792 and adressing comments.
- Looking into `bivariate.py` for lambert types, working on the tests of `solve`, how `_tsolve` acieves solving lambert equations.

#### Pull Requests to review (if any):
[#14736](https://github.com/sympy/sympy/pull/14736/), [#14792](https://github.com/sympy/sympy/pull/14792)

### Meeting #08
* Date: Saturday, 14th July 2018
* Time: 11:00 AM - 12:00 AM (IST)
* Attendees: Yathartha Joshi, Amit Kumar

#### Minutes of Meeting:
- Discussing on handling singularities with log and the `log_singularities()` method implementation were discussed. Amit suggested to have a word of review with Kalevi and also advised to open a discussion in mailing list for proper feedback.
- Improvements in identification of the log equations. We discussed on possible ways to identify these class of  equations. We concluded that the heleper should be such that it should identify the ones that its helper could handle.
- Ways to handle infinte recursion, probably we concluded as per the comments by Chris that the identification of the equations should be properly made.

#### Goals
- Improving log solver and its identifier
- Working on the implementation of lambert types.
- Diferentiating tests of `bivariate_type` from those of `_solve_lambert`.

#### Pull Requests to review (if any):
[#14792](https://github.com/sympy/sympy/pull/14792)

### Meeting #09
* Date: Sunday, 22nd July 2018
* Time: 11:00 AM - 12:00 AM (IST)
* Attendees: Yathartha Joshi, Amit Kumar

#### Minutes of Meeting:
- After discussions with Kalevi in gitter, we concluded that if the equation can be written in an equaivalent form then the solutions from this equation would be same even if substituing them in the original equation would give some sigularites.
- Discussions with Amit took place on the way lambert solver will be implemented. We decide to have a helper that solves equations using `_solve_lambert` and then work on the tests that `bivariate_type` would solve to tests the coverage of both the routines.

#### Goals
- Removing checking singularities case for logarithmic equations
- Adding a PR for lambert types

#### Pull Requests to review (if any):
[#14792](https://github.com/sympy/sympy/pull/14792)

### Meeting #10
* Date: Sunday, 29th July 2018
* Time: 11:00 AM - 12:00 AM (IST)
* Attendees: Yathartha Joshi, Amit Kumar

#### Minutes of Meeting:
- As per the discussions with Chris in the log solver PR, Amit and I discussed on the way the solutions would be represented for symbolic equations. I suggested of having a special kind of a `ConditionSet` for such a scenario. Amit and Chris agreed upon this.
- Amit suggested to have the lambert identifier to identify proper class that wew can include in the solver otherwise we can take all the equations for solving if we are not sure of solving in such a scenario.
Also discussed on the shortcomings of both the ways.

#### Goals
- Make log solver PR merge ready
- Add bivariate solver in lambert type PR

#### Pull Requests to review (if any):
[#14792](https://github.com/sympy/sympy/pull/14792), [#14972](https://github.com/sympy/sympy/pull/14972)

### Meeting #11
* Date: Sunday, 5th August 2018
* Time: 11:00 AM - 12:00 AM (IST)
* Attendees: Yathartha Joshi, Amit Kumar

#### Minutes of Meeting:
- This was the last meeting as this was the last week of coding period. So Amit and I discussed on what all things are left and needs to be done.
- We discussed on few problems in implementing lambert solver and how we could tackle them.
- Amit advised to keep up the leftover task (if any) post GSoC and continue to be a part of the organisation
- We also discussed on how I will submit my final report.

#### Goals
- Try finishing up with the lambert solver PR
- Will be making other PR's that for minor bug fixes.

#### Pull Requests to review (if any):
[#14972](https://github.com/sympy/sympy/pull/14972)
