# Sample Platform NG

**Parent:** CCExtractor Development — Project Ideas
**Source:** https://ccextractor.org/public/gsoc/2026/sample_platform_ng
**Scraped:** 2026-02-22T23:28:47.612047

---

# Sample Platform NG

**Mentors:**
Carlos (carlos.fernandez), Willem (canihavesomecoffee)

**Time estimation**
350 hours

### Project Brief

The Sample Platform was one of the original projects in GSoC for us. It's served us very well over the years, but it could use a modernization. This includes a new UI, backend improvements, repository update and more.

### Current Issues and Goals

**UI and Frontend:**

- There's no frontend (of any kind) to define the tests, it's all queries (SQL) direct to the DB.
- We can probably do a UI refresh very quickly with AI now and modernize it.

**AI-Friendly Testing:**

- Make it AI friendly; this means that we always compile with debug info* and for each test we make the full output (not just the result) available for download as well as the sample (directly). Basically, we want to be able to give an AI one URL with a run and from there it should be able to access everything - binaries, coredumps (if there's one), input (i.e. samples), arguments, outputs (real and expected).

* This is not done inside the platform, up to you to figure out where ;)

**Test Infrastructure:**

- Current state of tests are either Pass or Fail. We don't have a state of "Never worked" to reflect a situation in which we have samples but they have some problem and there's never been a version of CCExtractor that worked with those samples.
- We need a way to bisect.
- Estimation of test duration can give negative results.

**Build Improvements:**

- We don't have a way to run tests on Mac. We want to add Mac testing support. Your proposal should include investigation whether or not this is possible with GCP and what cost it would entail to also run (limited) tests on Mac.
- We're not validating the Docker build.

**Test Suite Expansion:**

- Our test suite is limited. Many samples that have been shared in issues have never been added, even if we used them to fix bugs. We need to recover as many of those as we can and add them.
- Some videos are really long; we don't need one hour recording, or even 10 minutes. Usually if there's a problem, you can see it in the first minute.
- We are not testing every possible argument. When I say testing I don't mean against a sample file but by itself - even if the parsing works. We broke some things on the rust migration that apparently flew under the radar.
- We need to update our samples, also importing reference corpus such as the one from VLC:
[http://streams.videolan.org/streams/ts/](http://streams.videolan.org/streams/ts/) - We need to sort the streams better. Possibly using mediainfo, ffprobe, etc, to tag each of the samples we have.

**Comparison and Cross-Platform:**

- We need to add functionality to test Linux vs Windows results so we can see, for a given PR, whether the output is identical or not.
- The comparison system is very dumb, comparing frame by frame - so if a frame (subtitle frame) is missing, then from that point everything is a mismatch.

# Your task

Work on the above issues to modernize and improve the Sample Platform. This includes (in order of importance):

- Make the platform AI-friendly with comprehensive output access
- Add "Never worked" test state
- Create a frontend for test definition (replacing direct SQL queries)
- Implement bisect functionality
- Expand the test suite with samples from issues and external sources
- Improve the comparison algorithm to handle frame offsets
- Implement cross-platform result comparison
- Add Mac testing support
- Implement a modern UI refresh

### Qualification tasks

Take a look at the [Sample Platform repository](https://github.com/CCExtractor/sample-platform) and work on one or more of the issues listed above. Even small improvements or bug fixes are valuable.
