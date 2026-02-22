# issue #5219 on HPX bug tracker

**Parent:** Ste||ar group — Project Ideas
**Source:** https://github.com/STEllAR-GROUP/hpx/issues/5219
**Scraped:** 2026-02-22T23:28:47.614443

---

## (Re-)Implement executor API on top of sender/receiver infrastructure

**Labels:** type: enhancement, type: compatibility issue, category: executors, project: GSoC, category: senders/receivers

Currently our executor API (customization points) dispatch to an executor interface that was defined by wg21.link/p0443R3. All HPX facilities related to scheduling tasks (algorithms, future, dataflow, async etc.) rely on the executor customization points to perform their operations.

We should reimplement the customization points such that they build upon the sender/receiver infrastructure that has been put in place in HPX based on the latest versions of wg21.link/p0443.

