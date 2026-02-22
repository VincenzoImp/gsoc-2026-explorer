# #164

**Parent:** MLLAM — Project Ideas
**Source:** https://github.com/mllam/neural-lam/issues/164
**Scraped:** 2026-02-22T23:28:47.631752

---

## Support cugraph

I just noticed that networkx has a concept of "backends", which means that using [cugraph](https://github.com/rapidsai/cugraph) is as easy as setting the `NX_CUGRAPH_AUTOCONFIG=True` environment variable. See https://github.com/rapidsai/nx-cugraph?tab=readme-ov-file#enabling-nx-cugraph for details.

I thought this might make things quicker when creating the graph. I had to make a few fixes thought to make it possible https://github.com/leifdenby/neural-lam/tree/feat/support-cugraph

This should go into `weather-model-graphs` eventually. But I just wanted to make a note of this until there is time to work on it and check whether it actually makes graph generation quicker.

