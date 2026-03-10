# DiskDataset select() call assumes all data fields populated #4059

**Parent:** DeepChem — Project Ideas
**Source:** https://github.com/deepchem/deepchem/issues/4059
**Scraped:** 2026-03-10T16:58:40.283241

---

## DiskDataset select() call assumes all data fields populated

**Labels:** Contribution Welcome

DiskDataset select() call assumes all data fields are populated if output_numpy_dataset is True. If any fields are not populated, an empty NumpyDataset is silently returned.

This code:

        else:
            X, y, w, ids = next(generator())
            return NumpyDataset(X, y, w, ids)

Needs to be changed to this:

        else:
            X, y, w, ids = next(generator())
            if len(X) == 0:
                X = None
            if len(y) == 0:
                y = None
            if len(w) == 0:
                w = None
            if len(ids) == 0:
                ids = None
            return NumpyDataset(X, y, w, ids)



