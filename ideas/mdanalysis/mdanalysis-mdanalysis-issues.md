# Issue Tracker

**Parent:** MDAnalysis — Project Ideas
**Source:** https://github.com/MDAnalysis/mdanalysis/issues
**Scraped:** 2026-02-22T23:28:47.550490

---

## #5236: Test failures in test_xdr.py test_offset_lock_created method

A lot of tests are currently failing on `develop` with the following two failures:

```
FAILED testsuite/MDAnalysisTests/coordinates/test_xdr.py::TestXTCReader_offsets::test_offset_lock_created - AssertionError: assert False
FAILED testsuite/MDAnalysisTests/coordinates/test_xdr.py::TestTRRReader_offsets::test_offset_lock_created - AssertionError: assert False
```

The reason for these failures is a change in the `filelock` version. I was able to reproduce this on a local setup. `filelock` up until `3.20.3` didn't cause any problem. Anything above, causes these errors - see `filelock` [release history](https://pypi.org/project/filelock/#history). A quick search of the changes after `3.20.3` (see [diff](https://github.com/tox-dev/filelock/compare/3.20.3...3.21.0)), seem to indicate that this could be due to changes in their PR 408 that deletes the lock file on release, but we aren't handling it and still checking for it's presence. Thanks

ps. `filelock` `3.20.4` was released on Feb 12, 2026 and this checks out with when we started having these test failures.

---

## #5234: Add accelerated backends support for minimize_vectors

## Is your feature request related to a problem? ##
<!-- A clear and concise description of what the problem is. For example, I'm always frustrated when [...] -->

[`minimize_vectors`](https://docs.mdanalysis.org/stable/documentation_pages/lib/distances.html#MDAnalysis.lib.distances.minimize_vectors) is one of the few distance functions that currently doesn't support the `backend` keyword.

I would like to use `minimize_vectors` instead of `distance_array` to perform compact wrapping of trajectories for visualization in [Molecular Nodes](https://github.com/BradyAJohnston/MolecularNodes) (the equivalent of `gmx trjconv -ur compact`). Preliminary testing indicates that this is significantly faster than using `distance_array` for that computation (see corresponding PR for some comparisons) and can get even better with `openmp` and `distopia` accelerated backend support.

## Describe the solution you'd like ##
<!-- A description of what you want to happen. For example, I'd like to be able to do [...] -->

I would like `minimize_vectors` to support both the `OpenMP` and `distopia` accelerated backends.

## Describe alternatives you've considered ##
<!-- A description of any alternative solutions or features you've considered or possible solutions that you've seen elsewhere. -->

The alternative is to use the current `cython` version of `minimize_vectors`.

## Additional context ##
<!-- Add any other context or screenshots about the feature request here. -->

MN added support for displaying a simulation box for trajectories (generic Wigner-Seitz cell) as part of [MN PR #981](https://github.com/BradyAJohnston/MolecularNodes/issues/981). MDAnalysis currently does not have `compact` wrapping support, but this was attempted as part of an old open PR #2982. The need for this is also highlighted in this [comment](https://github.com/MDAnalysis/mdanalysis/pull/2982#issuecomment-3369658607) of that PR. MN currently recommends adding a custom on-the-fly transformation using the `compact` wrapping code from that PR as seen in this [comment](https://github.com/BradyAJohnston/MolecularNodes/issues/981#issuecomment-3385200341). Using `minimize_vectors` to perform `compact` wrapping gives better performance results and adding accelerated backends support will also enable us to add a performant version of `compact` wrapping to MDAnalsis later.

I will create a PR that adds backends support to `minimize_vectors` and enabled for `serial` and  `openmp`. (Created PR #5235 )

I will create a PR in [distopia](https://github.com/MDAnalysis/distopia) that adds `minimize_vectors` support after which we can enable the tests to include `distopia` as well and update the corresponding documentation as a separate MDAnalysis PR. (Created Distopia [PR #188](https://github.com/MDAnalysis/distopia/pull/188))

---

## #5224: Analysis classes fail with HOOMD GSD files with a TypeError

**Labels:** defect, Component-Analysis, format-HOOMD

Following discussion https://github.com/MDAnalysis/mdanalysis/discussions/5222 we found that AnalysisBase-derived analysis classes do not currently work with HOOMD GSD trajectories. The issue appears that the new parallelization framework generates lists of frames as a numpy array with datatype np.int64. When such a frame is used to index the GSD trajectory, a TypeError is raised because (apparently) frames need to be normal Python int (see https://github.com/MDAnalysis/mdanalysis/discussions/5222#discussioncomment-15700082 ). 

Normal iteration and indexing such as `u.trajectory[1]` work (as long as one uses normal ints — see below).

## Examples
### Failure example with Analysis class
```python
from MDAnalysis.tests.datafiles import GSD
from MDAnalysis.analysis import rms
u = mda.Universe(GSD)
rr = rms.RMSD(u.atoms)
rr.run()
```
fails with a **TypeError** in gsd
```
> ~/miniforge3/envs/mda314/lib/python3.14/site-packages/gsd/hoomd.py(1046)__getitem__()
   1044             return self._read_frame(key)
   1045
-> 1046         raise TypeError
   1047
   1048     def __iter__(self):
```

The original error report showed failure with RDF but this seems to be general. A quick %pdb shows that we are working with the custom sliced trajectory in analysis
```
> ~/miniforge3/envs/mda314/lib/python3.14/site-packages/MDAnalysis/analysis/base.py(554)_compute()
    552             return self
    553
--> 554         for idx, ts in enumerate(
    555             ProgressBar(
    556                 self._sliced_trajectory, verbose=verbose, **progressbar_kwargs

ipdb> p self._sliced_trajectory
<MDAnalysis.coordinates.base.FrameIteratorIndices object at 0x160ad2a50>
ipdb> p self._sliced_trajectory.frames
(np.int64(0), np.int64(1))
```
and here the frames are **np.int64**. 

### Minimal failure example
Just index with something integer-like:
```python
u.trajectory[np.int64(0)]
```
fails with the same TypeError.



## Discussed in https://github.com/MDAnalysis/mdanalysis/discussions/5222

<div type='discussions-op-text'>

<sup>Originally posted by **Lynn3512138** February  4, 2026</sup>
Hi All,

I'm using MDAnalysis 2.10.0 and try to get RDFs from a .gsd trajectories. The code is as below:

```
u=mda.Universe("2_B50_try7.gsd","2_B50_try7.gsd")

c=u.select_atoms("name C")
a=u.select_atoms("name A")

print(u.trajectory)
print(len(c))
print(len(a))

rdf = InterRDF(c,a,range=(0,5))
rdf.run()

plt.plot(rdf.bins, rdf.rdf)
```

However it gets the problems:

> <GSDReader 2_B50_try7.gsd with 50 frames of 100 atoms>
> 50
> 50
> ---------------------------------------------------------------------------
> TypeError                                 Traceback (most recent call last)
> Cell In[45], line 11
>       8 print(len(c))
>      10 rdf = InterRDF(c,a,range=(0,5))
> ---> 11 rdf.run()
>      13 plt.plot(rdf.bins, rdf.rdf)
> 
> File /opt/homebrew/Caskroom/miniconda/base/envs/hoomdenv/lib/python3.13/site-packages/MDAnalysis/analysis/base.py:898, in AnalysisBase.run(self, st

*[truncated]*

---

## #5223: Add guards to index assignment in Universe creation

**Labels:** usability, Component-Core

## Expected behavior ##

A clear error message should be raised when an incorrect index assignment is provided to `Universe.empty`, e.g.

```python
u_new = mda.Universe.empty(
            n_atoms=2,
            n_residues=2, atom_resindex=[1,2],
            trajectory=True
            )
u_new.add_TopologyAttr("resnames", ['RES1', 'RES2'])
```
This is incorrect because `atom_resindex` should be 0-based. (And I confused it with resids when I encountered this error).
## Actual behavior ##

No error is raised during creation but only when accessing it 

```u_new.atoms.resnames``` provides `IndexError: index 2 is out of bounds for axis 0 with size 2`

This is also true for `residue_segindex`.
## Current version of MDAnalysis ##

- Which version are you using? (run `python -c "import MDAnalysis as mda; print(mda.__version__)"`): dev
- Which version of Python (`python -V`)? 3.12
- Which operating system? mac-os

---

## #5221: Incompatibility of `StringIO` objects with `parallelization`

**Labels:** Component-Readers, parallelization

## Expected behavior ##

<!-- A clear and concise description of what you want to do and what you think should happen. (Code to reproduce the behavior can be added below). -->

Issue which occurred during PR #5151.

Currently, when using the `dask` and 'multiprocessing' backends, reading `StringIO` objects in parallelization fails when using `ReaderBase` to read the file. This is because it tries to read the file but cannot access it, since it only gets a string that is neither pickable nor iterable. This leads to the reading process becoming stuck indefinitely, which was encountered during #5151.

Ideally the `dask` and `multiprocessing` backends should be compatible with `StringIO` objects and it should be possible to read the files or to modify it to read the `StringIO` files serially.

## Actual behavior ##

<!-- What happened instead. Add as much detail as you can. Include (copy and paste) stack traces and any output. -->

Currently what happens is when using `StringIO` objects with `dask` and `multiprocessing` due to incompatability the process is getting stuck


## Code to reproduce the behavior ##

<!-- Show us how to reproduce the failure. If you can, use trajectory files from the test data. Use the code snipped below as a starting point. -->

To recreate this error you can create a `test_stringio_dask.py` and pytest it with the file containig the following:

``` python


from io import StringIO
import multiprocessing as mp

import pytest
import numpy as np
import MDAnalysis
from numpy.testing import assert_equal
from MDAnalysis.analysis.hydrogenbonds.wbridge_analysis import WaterBridgeAnalysis

import dask
import dask.config

try:
    mp.set_start_method("spawn", force=True)
except RuntimeError:
    pass

# Force dask "processes" scheduler to use spawn context explicitly
dask.config.set({"multiprocessing.context": "spawn"})


class TestWaterBridgeAnalysis(object):
    @staticmethod
    @pytest.fixture(scope="class")
    def universe_DA():
        """StringIO-backed Universe (single frame), acceptor resid 1, donor resid 4."""
        grofile = """Test gro file
3
    1ALA      O    1   0.300   0.000   0.000
    4ALA      H    2   0.100   0.000   0.000
    4ALA      N    3   0.000   0.000   0.000
  1.0   1.0   1.0"""
        u = MDAnalysis.Universe(StringIO(grofile), format="gro")
        return u

    @staticmethod
    @pytest.fixture(scope="class", params=["multiprocessing", "dask"])
    def client_WaterBridgeAnalysis(request):
        return {"backend": request.param, "n_workers": 2, "n_parts": 8}

    @pytest.mark.parametrize("distance_type", ["hydrogen", "heavy"])
    def test_accepter_donor(self, universe_DA, distance_type, client_WaterBridgeAnalysis):
        """Test zeroth order acceptor-to-donor hydrogen bonding."""
        wb = WaterBridgeAnalysis(
            universe_DA,
            "protein and (resid 1)",
            "protein and (resid 4)",
            order=0,
            distance_type=distance_type,
        )
        wb.ru

*[truncated]*

---

## #5211: Framework for Performance Benchmarking in Analysis

**Labels:** performance, Component-Analysis

## Is your feature request related to a problem? ##
As part of parallelizing benchmarking work (https://github.com/MDAnalysis/parallelization-benchmarks), we would like to implement a code-level timing/performance framework.

## Describe the solution you'd like ##
- Use `time.perf_counter` to track the time spent in each component of an analysis. The performance report should be parallel-aware, so that time spent in individual computational groups can be extracted and analyzed.
- Add an `enable_timing` flag to `AnalysisBase.run()` so that performance data can be accessed, for example via `AnalysisBase.performance`.

## Describe alternatives you've considered ##
- Using external tools, such as `line_profiler`.

## Additional context ##
- In the future, we may want to track not only execution time but also memory consumption, job dispatching, and other related metrics.
- There is an existing `timeit`-style implementation in PMDA (https://github.com/MDAnalysis/pmda/blob/master/pmda/parallel.py) that could serve as inspiration.

---

## #5191: CI: Azure_Tests Win timeout occasionally

**Labels:** defect, Continuous Integration

## Expected behavior ##

<!-- A clear and concise description of what you want to do and what you think should happen. (Code to reproduce the behavior can be added below). -->
Tests don't timeout and complete

## Actual behavior ##

<!-- What happened instead. Add as much detail as you can. Include (copy and paste) stack traces and any output. -->
This was observed only on a couple of PR runs so far, but could become a potential issue going forward.

- [Failure run 1](https://dev.azure.com/mdanalysis/mdanalysis/_build/results?buildId=8751&view=logs&j=bc985eae-65f0-56fb-9f4e-306b452dcfb3&t=99aa0f91-3087-50b5-0e7a-6e6967266174)
- [Failure run 2](https://dev.azure.com/mdanalysis/mdanalysis/_build/results?buildId=8747&view=logs&j=c005f73a-e77d-5820-888c-6d21a222fdeb&t=ed2656dc-a91e-5ce0-d263-0c39603afe85)

A few notes about these runs:
- They are from different PRs, so the issue is not related to code or actual tests
- Here is a [successful run](https://dev.azure.com/mdanalysis/mdanalysis/_build/results?buildId=8752&view=logs&j=bc985eae-65f0-56fb-9f4e-306b452dcfb3&t=99aa0f91-3087-50b5-0e7a-6e6967266174) after an empty commit after the `Failure run 1` above - indicating that this could potentially be an infra issue
- Successful runs for the  `Run MDAnalysis Test Suite` job take around 40 mins
- Failure runs for the same job take over 50mins and the tests are only around 75% done (triggering the overall 1 hour timeout)

## Code to reproduce the behavior ##

<!-- Show us how to reproduce the failure. If you can, use trajectory files from the test data. Use the code snipped below as a starting point. -->
So far, the failures are only a couple and a bit random

---

## #5183: Support per-frame analysis by AnalysisBase-based classes for streamed trajectories

**Labels:** enhancement, Component-Analysis, streaming

## Is your feature request related to a problem? ##
`AnalysisBase`-based analysis classes currently cannot be used for streamed trajectories (as clarified by @orbeckst on Discord).

To illustrate, here is a streaming trajectory setup based on the IMD workshop for which DSSP analysis is needed:
```py
import MDAnalysis as mda
from MDAnalysis.analysis.dssp import DSSP

top = "/tmp/imd-workshop-2025/workshop/sample_simulation/GROMACS/input/start.gro"
u = mda.Universe(top, "imd://localhost:8889")
```

We cannot run the full analysis because there is no concept of frame length for streamed trajectories, so
```py
run = DSSP(u).run()
```
throws a `RuntimeError: IMDReader: n_frames is unknown` exception as expected.

We also cannot use the `start` and `stop` params because we can't access arbitrary fames. So, something like this
```py
run = DSSP(u).run(start=0, stop=1)`
```
throws a `ValueError: IMDReader: Cannot expect a start index from a stream, 'start' must be None` exception.

The only other option available to call `run(...)` is to pass a `frames` array. Naturally, we cannot pass arbitrary frames, but even passing the current frame as follows
```py
run = DSSP(u).run(frames=[u.trajectory.frame])
```
throws a `TypeError: Streamed Trajectories must be an indexed using a slice` exception as only slicing using a step (`[::n]`) or all frames sequentially (`[:]`) is currently supported.

This limits the choices to use any standalone functions for these analysis types (if they exist) or create a separate universe per frame to run the analysis on, both of which are not ideal.

## Describe the solution you'd like ##
I'd like to be able to do something like the following:
```py
run = DSSP(u).run(frames=[u.trajectory.frame])
```
where the current streamed trajectory frame is passed and get the analysis results for this current frame.

## Describe alternatives you've considered ##
For `DSSP` analysis, there is a standalone `assign` function, but that requires re-inventing quite bit of what is already done in the `DSSP` class setup. Another alternative suggested by @marinegor  is to create a new universe for the current frame and run the analysis class on it. Though this is simpler than using standalone functions (if they exist), it comes with quite a bit of overhead.

## Additional context ##
My current use case is to show secondary structures computed by the `DSSP` analysis class for streamed trajectories in realtime in MolecularNodes - see BradyAJohnston/MolecularNodes#1072 (cc: @BradyAJohnston ). However, the ability to run any other `AnalysisBase`-based analysis classes would probably benefit a lot of streamed trajectory use cases in the future.

I will create a PR that supports the approach described in the "solution you'd like" section above. Thanks

---

## #5141: Add option for `gemmi` backend for PDB reading

**Labels:** Format-PDB, Component-Readers

## Is your feature request related to a problem? ##
It's more of a suggestion.

## Describe the solution you'd like ##
Pull #4712 is about to introduce `gemmi`-based backend for mmCIF reading. It wasn't intended but, MMCIFReader/Parser can also read pdb files:

```python
import MDAnalysis as mda
mda.Universe('testsuite/MDAnalysisTests/data/4E43.pdb', format='mmcif')
# <Universe with 1877 atoms>

```

since `gemmi`, being de-facto standard for RCSB stuff, can read both into the same `gemmi.Model` interface. Perhaps it's worth including an option to read `pdb` with `gemmi` backend then? I'm not sure how to technically do that though -- for instance, we could add `format = 'pdb_gemmi'` to `MMCIFParser`, and document this behavior in `PDBParser`.


## Describe alternatives you've considered ##
Another option would be to just add a paragraph in documentation about this in MMCIFParser and/or PDBParser without changing any code -- I'd be probably fine with that, but just don't want this information to stay undocumented.


@MDAnalysis/coredevs do you have an opinion on that?

---

## #5138: Incorrect unwrapping for LAMMPS trajectories due to unused image flags for periodic boundary condition

**Labels:** format-LAMMPS, PBC, more information needed

## Is your feature request related to a problem? ##
MDAnalysis universe currently ignores `LAMMPS image flags (ix, iy and iz)` to properly unwrap wrapped coordinates according to `periodic boundary condition` when unwrapping coordinates from `LAMMPSDUMP` files. MDAnalysis solely does:
> x_unwrapped = x_scaled * L + L/2 (where L is box dimension)

This works good only when atoms never crossed boundaries `i.e., flag ix_i = 0` but this is incorrect unwrapping when the atoms have crossed boundaries and that leads to wrong results when computing MSD or diffusion coefficients or COM.


While comparing MSD results from the new method in [PR#5066](https://github.com/MDAnalysis/mdanalysis/pull/5066) (merged) vs our in-house code (that incorporates proper conversion accounting the image flags) there is a discrepancy.
> x_unwrapped = x_scaled * L + L*ix (Correct convention with the in-house code)

We've further verified this when provided with an already pre-unwrapped `LAMMPSSUMP` file. The results are consistent between MDAnalysis and In-house code! Meaning that it's definitely the improper unwrapping only while creating the universe that creates the discrepancy.



## Describe the solution you'd like ##
i. Properly take care of the periodic boundary condition image flags while unwrapping the universe
ii. Or at least for the time-being provide a warning to the user to provide unwrapped coordinates.



## Describe alternatives you've considered ##
Pre-unwrapping the trajectory file (LAMMPSDUMP) following proper PBC flags


## Additional context ##

Example below:

<img width="589" height="390" alt="Image" src="https://github.com/user-attachments/assets/169053f6-1744-4ac3-b078-566d79bc87d7" />
Notice the shoot up!

<img width="589" height="390" alt="Image" src="https://github.com/user-attachments/assets/c7aba68b-b9d3-4a07-a1a6-bddc8222a13f" />
Pre-unwrap to get correct results!


notebooks for this example can be found in the [repository-link](https://github.com/gitsirsha/MDAnalysis_unwrapping_issue_example).

---

## #5136: Several contributions from v2.10.0 are missing from either changelog or authors

These include: 

- namiroues
- jpkrowe
- schuhmc
- gitsirsha
- Pradyumn-cloud

---

## #5127: missing test for LAMMPS DumpReader for ValueError when missing coordinates

**Labels:** help wanted, testing, format-LAMMPS

The case when no coordinates following the specified convention in the Timestep are found and a `ValueError` is raised, is not tested:
https://github.com/MDAnalysis/mdanalysis/blob/19e675b35f207a7e3769700f1466ce0a6d1605c7/package/MDAnalysis/coordinates/LAMMPS.py#L833-L838

(The incorrect f-string use is fixed in https://github.com/MDAnalysis/mdanalysis/pull/5053 but a test is still missing.)

---

## #5125: Disable build isolation in pip only cron tests after next release

We have to turn it on because the released MDA version isn't compatible with the latest numpy & cython. Next release we should be good, so we should turn it off.

---

## #5115: Convert units of trajectory data when constructing a universe

**Labels:** format-LAMMPS, units

## Is your feature request related to a problem? ##
<!-- A clear and concise description of what the problem is. For example, I'm always frustrated when [...] -->
Reading in trajectory files that combine atomic forces along with positions, the units for forces are automatically converted from kcal/(mol.Ang) to kJ/(mol.Ang) when reading from Amber (.nc) and GROMACS (.trr) combined trajectory files. But this behaviour is not replicated for the LAMMPSDUMP file (with additional_columns=['fx', 'fy', 'fz']), outputted as real units. The forces remain as kcal/(mol.Ang). This causes issues with further analysis of forces, where the units are expected to be in kJ/(mol.Ang).

To replicate the behaviour with mdanalysis>=2.7.0 and python >=3.11:

Topology and trajectory files used: 

[amber_top_lammpsdump_traj.zip](https://github.com/user-attachments/files/22517457/amber_top_lammpsdump_traj.zip)

Universe is constructed from topology and trajectory with:

`u = Universe(top_file, traj_file, format="LAMMPSDUMP", additional_columns=['fx', 'fy', 'fz', 'c_5', 'c_7'], units="real")`

Where `c_5` and `c_7` are per-atom potential and kinetic energies respectively, in units kcal/mol.

## Describe the solution you'd like ##
<!-- A description of what you want to happen. For example, I'd like to be able to do [...] -->
Is it possible to allow manual conversion of units of atomic forces (and even atomic positions, energies, velocities, charges, etc.) at the point of construction of a universe? It is not always practical to convert units frame-by-frame afterwards if a software expects units to not depend on the MD engine used to produce the trajectory. 

Allowing the conversion of trajectory terms will give flexibility in populating other atomic terms (such as per-atom energies outputted from LAMMPS) into a universe without having to worry about units when the universe is analysed with other functions/software afterwards.

Alternatively, but not as general, can the LAMMPSDUMP reader be updated to convert forces to kJ/(mol.Ang)?

## Describe alternatives you've considered ##
<!-- A description of any alternative solutions or features you've considered or possible solutions that you've seen elsewhere. -->
I can't find another alternative to convert trajectory data units at the point of creating the universe.

Another solution is to add pre-converted auxiliary data (as shown here: https://userguide.mdanalysis.org/stable/formats/auxiliary.html#loading-data-into-a-universe), but this would mean forces have to be accessed via a different method (ts.forces vs ts.aux.forces), therefore not general over all trajectory types.



## Additional context ##
<!-- Add any other context or screenshots about the feature request here. -->
MDAnalysis is used extensively in [CodeEntropy](https://github.com/CCPBioSim/CodeEntropy) to calculate components of entropy at multiple length scales of molecules from the statistics captured from positions and forces outputted from a MD simulation. The 

*[truncated]*

---

## #5114: Use native scipy periodic KDTree for orthorhombic boxes?

**Labels:** help wanted, performance, PBC

The MDAnalysos PBC-awared distance calculations normally use a grid-based method with "augmentation" to find minimum image distances.

However, as an alternative method a KDTree based method also exists in `lib.pkdtree`. More recent versions of scipy have added the `boxsize=[Lx, Ly, Lz]` kwarg to [scipy.spatial.cKDTree](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html) to natively compute nearest neighbors on a toroidal topology (i.e., orthorhombic boxes in the case of MD simulations). As recently pointed out in https://github.com/scipy/scipy/issues/16191#issuecomment-2568357454 we could use this update to scipy.

1. We should investigate if the performance of the native scipy periodic KDTree is better than our implementation.
2. If yes, we should consider changing https://github.com/MDAnalysis/mdanalysis/blob/5d48c5cf5f89700dde7ac5fb6a2e74458ce27a7e/package/MDAnalysis/lib/pkdtree.py#L66 so that we only use our augmented KDTree for cases that native scipy cannot handle.

---

## #5102: guess_TopologyAttrs guesses incorrect bonds for DMS lipids in MDAnalysis > 2.7.0

**Labels:** defect, Component-Topology

Expected Behavior

When using guess_TopologyAttrs to generate bonds for DSM lipids, the bonds around atom C3S  (or any C*S) should be guessed correctly. For example:

("C3S", "C4S"), ("C3S", "C2S"), ("C3S", "H3S"), ("C3S", "H3T")

Actual Behavior

In MDAnalysis versions > 2.7.0, guess_TopologyAttrs produces incorrect extra bonds, e.g.:

[('C3S', 'C5S'), ('C3S', 'H4T'), ('C3S', 'H4S'),
 ('C3S', 'C4S'), ('C3S', 'HO3'), ('C3S', 'O3'),
 ('C3S', 'H3S'), ('C3S', 'H2S'), ('C3S', 'C2S'),
 ('C3S', 'NF'), ('C3S', 'C1S')]


This only happens for the lipid tail with atoms labeled C*S. The other tail with C*T behaves as expected.

Code to Reproduce
import MDAnalysis as mda

 # Load structure with DMS lipid (minimal example)
u = mda.Universe("lipid_dms.pdb")
structure = u.select_atoms("resname DSM")

# Guess bonds
structure.guess_TopologyAttrs(to_guess=["bonds"], fudge_factor=0.5)

for b in structure.bonds:
    print(b)

Version Information

MDAnalysis: 2.7.0 → works as expected

MDAnalysis: > 2.7.0 → produces incorrect bonds

Python: 3.12

OS:Linux

Additional Notes

It seems that atom names like C3S may be misinterpreted as the element cesium (Cs), which has a much larger van der Waals radius, leading to spurious bonds.

---

## #5100: Inncorrect use of simple method when random frames are selected in run() 

**Labels:** defect, Component-Analysis

> Thanks for the updates. I only have minor cosmetic changes.
> 
> While reviewing, I also realized that your code can solve a problem that has been inherent in the existing code: The `run()` method can take the [frames=[0, 20, 25, 100, 1001, ...]` kwarg](https://docs.mdanalysis.org/stable/documentation_pages/analysis/base.html#MDAnalysis.analysis.base.AnalysisBase.run) to select any frames instead of start/stop/step and if that's the case, the "linear" approach is incorrect (but that case is not being caught). We should select your new code path for un-even frame separations. 
> 
> I am not asking for this to be resolved in this PR. If you agree that this is a problem and that your code could solve it, could you raise an issue for it so that it's not forgotten.
> 
> _Originally posted by @orbeckst in https://github.com/MDAnalysis/mdanalysis/pull/5066#pullrequestreview-3125062849_
>             

            
            
This issue recognizes that while calculating msd of randomly picked frames (specified by kwarg by user in run), the newly added `_conclude_non_linear()` should be used instead of the previous `_conclude_simple()` method which is inaccurate when frames are non linearly placed. In most cases picking frames randomly results in picking frames that are non-linearly spaced so the `_conclude_simple()` method is not the right way to calculate msd.

---

## #5094: Cite: Add citation to `IMDReader` once IMDv3 paper is published

The [IMDv3 protocol implementation](https://github.com/MDAnalysis/mdanalysis/pull/4923) in MDAnalysis through the `IMDReader` needs an appropriate citation under references (`package/doc/sphinx/source/documentation_pages/references.rst`), once the IMDv3 paper has been published.

---

## #5089: Parse hexadecimal resid from OpenMM in PDBParser 

**Labels:** Format-PDB, decision needed

## Is your feature request related to a problem? ##
OpenMM generate a PDB file with hexadecimal resid if there are more than 9999 residues. 
However, in MDAnalysis, hexadecimal resids (treated as faulty resid) are set to 1, which causes problems in some cases.


## Describe the solution you'd like ##
I'd like to change PDBParser._parseatoms to handle Hexadecimal resid, if there are alphabets in resid.
Changing
https://github.com/MDAnalysis/mdanalysis/blob/c4af00babc9fc69671f1ea182b8b3a9b8807230d/package/MDAnalysis/topology/PDBParser.py#L302-L304
to

```
                    else:
                        if any([a.isalpha() for a in line[22:26]]):
                            resid = int(line[22:26], base=16) - 30960
                        else:
                            resid = int(line[22:26])
                        # Wrapping
```

## Describe alternatives you've considered ##
Or setting unique resids (increment from last resid / preset failed resid starting number e.g. 10000) for residues with failed resid parsing can be another option (while this can be problematic for other cases). 
Or editing Universe to get optional Parser(TopologyReaderBase) so one can give custom topology parser if needed.

## Additional context ##
openmm.app.pdbfile.py : 484  (from OpenMM version 8.2.0) 
```
def _formatIndex(index, places):
    """Create a string representation of an atom or residue index.  If the value is larger than can fit
    in the available space, switch to hex.
    """
    if index < 10**places:
        format = f'%{places}d'
        return format % index
    format = f'%{places}X'
    shiftedIndex = (index - 10**places + 10*16**(places-1)) % (16**places)  <----- This part
    return format % shiftedIndex
```
One major problem is that OpenMM uses decimal until resid 9999 and starts from hex A000 (== decimal 40960) in place of decimal resid 10000, so parser needs to subtract 30960 or just use resid 40960. 
I think both may cause problems in other parts.

---

## #5078: Build time tests makes machine to hang

**Labels:** testing, downstream

Hello. This was reported to Debian here:

https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1108309

When building (the Debian package of) mdanalysis, version 2.9.0, on AWS machines of types `m7a.large` or `r7a.large`, which incidentally have 2 vCPUs, the build-time tests timeout and the build results in failure. I've put several failed build logs here as a sample:

https://people.debian.org/~sanvila/build-logs/202507/

The failure rate on the above machine types is easily around 90%, and of course the expected behavior is that the tests finish in about 10 minutes or less, as that's what it takes on similar AWS machines having a single CPU only.

Is there a minimum number of CPUs required to run the tests, or is this a bug in the tests? (some kind of deadlock, for example). If it was the former, we could just skip the tests when we know for sure that they will fail or hang the machine, but if that's the case it would be nice to have such thing documented.

Note: I'm trying the build on Debian testing (which will become Debian 13 soon), and it has python 3.13.3 and Linux 6.12.33.

In case you have any difficulty in reproducing the problem, I could offer a VM to test (please contact me privately for details. I'm easily reachable at debian.org).

Cc to @drew-parsons as the usual Debian maintainer so that he's aware of how this develops.

Thanks.

---

## #5057: MDAnalysis fails with Cython 3.1.0

**Labels:** Priority-High, maintainability, installation, testing

_Originally reported  and debugged by @yuxuanzhuang_

We're getting Pytest worker crashes with Cython 3.1, see: https://github.com/MDAnalysis/mdanalysis/actions/runs/15360620736/job/43227245666?pr=5055

Pinning to <3.1 seems to be fixing the problem, see #5056

---

## #5032: Query: amino acid residue charges

**Labels:** question, Format-Amber

I'm just passing along an anonymous report that the net charge of amino acids read in using some AMBER-related topologies appears to cause some confusion (apparently this came up in a peer review criticism). I don't know if we are just "working as intended here," if there might be a small casting/data type issue, or if we just need to improve the docs a little. They didn't provide me with a programmatic reproducer, but I did get a brief verbal description on the whiteboard. I've tried to reconstruct into a minimum viable reproducer below, where some charges look a bit more sensible in `float32`/rounded/truncated format, though something may still be off in some cases.

This might normally appear to be a fairly minor matter, but in the context of certain machine learning workflows the net charge on the residues can be a problematic feature apparently.

```python
import numpy as np

from MDAnalysisTests.datafiles import PRM
import MDAnalysis as mda


u = mda.Universe(PRM)
for res in u.residues:
    manual_charge = 0
    for atom in res.atoms:
        manual_charge += np.float32(atom.charge)
    print(res.resname, res.charge, manual_charge)
```

```
ALA 1.0000000558793545 0.9999998
GLU -0.9999999655410647 -1.0
PHE 3.888271749019623e-08 5.9604645e-08
HIE 1.3504177331924438e-08 5.9604645e-08
ARG 0.9999999335850589 1.0
TRP 2.0954757928848267e-08 5.9604645e-08
SER 1.862645149230957e-08 0.0
SER 1.862645149230957e-08 0.0
TYR 7.799826562404633e-09 0.0
MET 3.8533471524715424e-08 5.9604645e-08
VAL 4.0978193283081055e-08 5.9604645e-08
HIE 1.3504177331924438e-08 5.9604645e-08
TRP 2.0954757928848267e-08 5.9604645e-08
LYS -6.891787052154541e-08 -1.1920929e-07
```

Are we "ok" here, or do we need a small tweak somewhere?

---

## #5030: Support for Amber NetCDF Restart Files (.ncrst)

**Labels:** enhancement, Format-Amber, Component-Readers, Component-Topology

Hello, MDAnalysis Community!

## Is your feature request related to a problem? ##
<!-- A clear and concise description of what the problem is. For example, I'm always frustrated when [...] -->
Amber NetCDF files come in two forms: lower-precision `.nc` files (mainly) for trajectory coordinates and higher precision `.ncrst` restart files for restarting a simulation (often with double precision forces, coordinates, and velocities). The current reader in MDAnalysis only reads the former.

Both of these variations are in the official spec list: https://ambermd.org/netcdf/nctraj.xhtml

## Describe the solution you'd like ##
<!-- A description of what you want to happen. For example, I'd like to be able to do [...] -->
Allow MDAnalysis to read Amber `.ncrst` restart files.

## Describe alternatives you've considered ##
<!-- A description of any alternative solutions or features you've considered or possible solutions that you've seen elsewhere. -->
N/A

## Additional context ##
<!-- Add any other context or screenshots about the feature request here. -->
I was able to implement this via tweaking/rigging the current reader. <strike>I will be making a PR shortly.</strike> #5031

---

## #5022: update license string to SPDX

**Labels:** Component-Docs, installation

Use a string from https://spdx.org/licenses/ to update

https://github.com/MDAnalysis/mdanalysis/blob/1cdb055ea95c7d1cddb788296227eef026164bb6/package/pyproject.toml#L53

(and elsewhere).

See output from a [recent CI run on azure](https://dev.azure.com/mdanalysis/mdanalysis/_build/results?buildId=8062&view=logs&j=a2a7f4f3-7a8f-538b-6d27-7072c87d6fd3&t=98b69802-e87c-5933-6a7a-52e710b30a1f)
```
  !!

          ********************************************************************************
          Please use a simple string containing a SPDX expression for `project.license`. You can also use `project.license-files`. (Both options available on setuptools>=77.0.0).

          By 2026-Feb-18, you need to update your project and remove deprecated calls
          or your builds will no longer be supported.

          See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
          ********************************************************************************

  !!
    corresp(dist, value, root_dir)
  C:\Users\VssAdministrator\AppData\Local\Temp\pip-build-env-lbt59hbw\overlay\Lib\site-packages\setuptools\config\_apply_pyprojecttoml.py:61: SetuptoolsDeprecationWarning: License classifiers are deprecated.
  !!

          ********************************************************************************
          Please consider removing the following classifiers in favor of a SPDX license expression:

          License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)

          See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
          ********************************************************************************

  !!

    dist._finalize_license_expression()
  C:\Users\VssAdministrator\AppData\Local\Temp\pip-build-env-lbt59hbw\overlay\Lib\site-packages\setuptools\dist.py:759: SetuptoolsDeprecationWarning: License classifiers are deprecated.
  !!

          ********************************************************************************
          Please consider removing the following classifiers in favor of a SPDX license expression:

          License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)

          See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
          ********************************************************************************

  !!

```

---

## #5009: Support for LAMMPS LJ reduced units

**Labels:** enhancement, format-LAMMPS, units

## Is your feature request related to a problem? ##
* The current MDAnalysis [LAMMPS DATA Reader](https://userguide.mdanalysis.org/1.0.1/formats/reference/data.html) explicitly does _not_ support Lennard-Jones units
* Support for reduced (LJ) units would be **immensely useful for coarse-grained simulations of polymer systems**
  * Useful not only for LAMMPS, but for HOOMD, GROMACS, and other simulation engines
  * Integral to an ongoing polymer simulations collaboration

## Describe the solution you'd like ##
* Support for LJ units (e.g. as an argument in the reader which allows one to specify this preference)
  * Ability to distinguish between unitless quantities vs quantities with implicit units
* Guidance from MDA maintainers on how to proceed with this feature (i.e. should this be supported, how general should LJ unit support be, etc.)
  * Are happy to provide manpower to generate PR

## Describe alternatives you've considered ##
* Provide feature which permits assignment of arbitrary units which are later converted back to [MDAnalysis' internal units](https://docs.mdanalysis.org/1.0.0/_modules/MDAnalysis/units.html)

---

## #4980: Edit transformations on a Universe

**Labels:** Component-Transformations, interoperability

## Is your feature request related to a problem? ##
If a universe has some transformations applied to it's positions, I'd like to be able to either remove them individually or cleanly create a copy of that universe without the transformations applied.


## Describe the solution you'd like ##
Remove the transformation via removing it from the list of transformations, or creating a copy of the universe.
```py
del u.transformations[1]
```


```py
u_copy = u.copy(transformations=False)
# keep the first but drop all other transforms in the new universe
u_copy.add_transformations(u.transformations[0])
```

These would be problematic for _in-memory_ trajectories, and the simplest would be to continue to not allow the changing of transformations for in-memory trajectories.

## Describe alternatives you've considered ##
Discussed in #4477 with the potential solutions being keeping a copy of the un-transformed universe and then keep copying from that and adding new transforms when needed. Reloading a universe from file information from the Universe when needing a 'clean' copy.


## Additional context ##

It was raised in that discussion that this isn't allowed because in-memory trajectories alter the coordinates when an transformation is applied, rather than altering them as reading. Removing a transformation won't undo the transformed coordinates.

The first approach would require limiting the removal of transformations to only trajectories that aren't in-memory, but that might be too much of a disconnect for usage that we might want to avoid.

The second strategy of a `universe.copy()` that allows you to _not_ copy across transforms would also have a similar problem with in-memory coordinates, likley requiring re-reading of coordinates from disk to get a 'clean' version of the universe.

This is primarily for usage inside of `Molecular Nodes`, when visualising a trajecotry playback a user can add / remove different transformations to smothe out the playback of their trajectory. From a GUI perspective, it's expected that the user would 'tinker' and add / remove the number of frames that they might be averaging to get the desired look. Because of this, I've currently got my own frame averaging implemented to handle easily adding & removing. 

I would like to however unify with the MDAnalysis averaging, and also potentially offer the other transformations that MDA offers. This _could_ be done with the strategy if keeping a 'backup' clean universe to copy from & add new transformations, but it would be simpler (on the MN side) to just edit the existing transformations. 

At least for my usecase in MN, all trajectories would be streamed from disk, so I wouldn't have to worry about in-memory problems.

Would appreciate thoughts from others about whether allowing modifications of transformations when not in-memory would be feasible (I would work on implementing it if agreed upon).

---

## #4971: remove analysis.encore for 3.0

**Labels:** Component-Analysis, MDAKit, remove-3.0

Remove encore (following its deprecation #4274 in favor of the [mdaencore](https://github.com/MDAnalysis/mdaencore) MDAKit)

Remove analysis.encore 
- [ ] code
- [ ] tests
- [ ] CI
- [ ] add note to #4539

---

## #4907: mda.fetch_pdb() to generate Universe from Protein Databank structures

**Labels:** enhancement, Format-PDB, Component-Readers, topology-building

## Is your feature request related to a problem? ##
<!-- A clear and concise description of what the problem is. For example, I'm always frustrated when [...] -->
We used to have `mda.fetch_mmtf()` to get a structure from the PDB but with the demise of MMTF, this was removed around release 2.6 or so. 

## Describe the solution you'd like ##
<!-- A description of what you want to happen. For example, I'd like to be able to do [...] -->

It would be very convenient to have `mda.fetch_pdb(PDB_ID)` to create a Universe from the entry in the Protein Databank with ID `PDB_ID`.


## Describe alternatives you've considered ##
<!-- A description of any alternative solutions or features you've considered or possible solutions that you've seen elsewhere. -->
VMD ([load molecule](https://www.ks.uiuc.edu/Research/vmd/current/ug/node25.html)), pymol ([fetch](https://pymol.org/dokuwiki/doku.php?id=command:fetch)) and Chimera ([fetch by ID](https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/fetch.html)) can do this.

Alternatively, keep using [this bash script](https://github.com/Becksteinlab/OBscripts/blob/master/scripts/pdb_downloader.sh) or `wget`/`curl`.


## Additional context ##
<!-- Add any other context or screenshots about the feature request here. -->
We will need the mmcif reader #2367 .

See also #3377 (fetch from alphafold database).

---

## #4906: Bugs for distance calculation functions

**Labels:** Component-lib, PBC

## Expected behavior ##

<!-- A clear and concise description of what you want to do and what you think should happen. (Code to reproduce the behavior can be added below). -->

I found two distance calculation functions cannot generate the same results, which results that one bond shorter than the cutoff cannot be found when I use guess_bond()

## Actual behavior ##

<!-- What happened instead. Add as much detail as you can. Include (copy and paste) stack traces and any output. -->


## Code to reproduce the behavior ##

Datafile: [struc.txt](https://github.com/user-attachments/files/18682239/struc.txt)

```
from MDAnalysis.lib import distances
tmp_lammps_filename="struc.txt"
u = mda.Universe(tmp_lammps_filename, format="DATA")
a,b=distances._nsgrid_capped_self(u.atoms.positions,max_cutoff=3.4,box=u.dimensions)
# Find the row in 'a' where the pair [145,80] appears
row_indices = np.where((a == [145,80]).all(axis=1))[0]
if len(row_indices) > 0:
    print(f"Found pair [145,80] at row {row_indices[0]}")
    print(f"Distance: {b[row_indices[0]]} Å")
else:
    # Also check for [80,145] since order might be reversed
    row_indices = np.where((a == [80,145]).all(axis=1))[0]
    if len(row_indices) > 0:
        print(f"Found pair [80,145] at row {row_indices[0]}")
        print(f"Distance: {b[row_indices[0]]} Å")
    else:
        print("Pair not found")
        
u = mda.Universe(tmp_lammps_filename, format="DATA")
a,b=distances._bruteforce_capped_self(u.atoms.positions,max_cutoff=3.4,box=u.dimensions)
# Find the row in 'a' where the pair [145,80] appears
row_indices = np.where((a == [145,80]).all(axis=1))[0]
if len(row_indices) > 0:
    print(f"Found pair [145,80] at row {row_indices[0]}")
    print(f"Distance: {b[row_indices[0]]} Å")
else:
    # Also check for [80,145] since order might be reversed
    row_indices = np.where((a == [80,145]).all(axis=1))[0]
    if len(row_indices) > 0:
        print(f"Found pair [80,145] at row {row_indices[0]}")
        print(f"Distance: {b[row_indices[0]]} Å")
    else:
        print("Pair not found")

```
Here _nsgrid_capped_self does not work, which prints:
Pair not found

Here _bruteforce_capped_self works which prints:
Found pair [80,145] at row 829
Distance: 1.3481745221090606 Å
....

```

## Current version of MDAnalysis ##

- Which version are you using? 2.8.0
- Which version of Python (`python -V`)?: Python 3.12.0
- Which operating system?centos:9

---

## #4891: Preserve Full Trajectory Information in Parallel Analysis

**Labels:** Component-Analysis, parallelization

## Is your feature request related to a problem? ##

In analyses e.g. `DistanceMatrix` in `diffusionmap`, we need to run analysis of a single frame over the full trajectory---that is sliced and defined by `start`, `stop`, and `step` in `run()`. However, in the current parallel analysis implementation, information about the full trajectory is lost (only per-process slices are visible).

## Describe the solution you’d like ##

Firstly, in `_setup_frames` (which only runs in the main process), store the sliced trajectory information in `self._global_slicer`. This makes it possible to retrieve global details such as the total number of frames.

Secondly, in `self._compute`, also store `self._global_frame_index` so the analysis can track the global frame index for each frame, rather than just per-process slices.

The following code will illustrate its usage
```python
import MDAnalysis as mda 
from MDAnalysisTests.datafiles import PDB, XTC
import numpy as np
from MDAnalysis.analysis.base import AnalysisBase
from MDAnalysis.analysis.results import ResultsGroup

u = mda.Universe(PDB, XTC)

class MyAnalysis(AnalysisBase):
    _analysis_algorithm_is_parallelizable = True

    @classmethod
    def get_supported_backends(cls):
        return ('serial', 'multiprocessing', 'dask',)

    def _prepare(self):
       self.results.frame_index = []
       self.results.global_frame_index = []
       self.results.n_frames = []
       self.results.global_n_frames = []

    def _single_frame(self):
       frame_index = self._frame_index
       global_frame_index = self._global_frame_index

       self.results.frame_index.append(frame_index)
       self.results.global_frame_index.append(global_frame_index)

       self.results.n_frames.append(self.n_frames)

       global_n_frames = len(self._trajectory[self._global_slicer])
       self.results.global_n_frames.append(global_n_frames)

    def _get_aggregator(self):
      return ResultsGroup(lookup={'frame_index': ResultsGroup.flatten_sequence,
                                  'global_frame_index': ResultsGroup.flatten_sequence,
                                  'n_frames': ResultsGroup.flatten_sequence,
                                  'global_n_frames': ResultsGroup.flatten_sequence})

# serial analysis
ana = MyAnalysis(u.trajectory)
ana.run(step=2)
ana.results
> {'frame_index': [0, 1, 2, 3, 4], 'global_frame_index': [0, 1, 2, 3, 4], 'n_frames': [5, 5, 5, 5, 5], 'global_n_frames': [5, 5, 5, 5, 5]}

# parallel analysis
ana = MyAnalysis(u.trajectory)
ana.run(step=2, backend='dask', n_workers=2)
ana.results
> {'frame_index': [0, 1, 2, 0, 1], 'global_frame_index': [0, 1, 2, 3, 4], 'n_frames': [3, 3, 3, 2, 2], 'global_n_frames': [5, 5, 5, 5, 5]}
```

`n_frames` and `frame_index` are not the same for serial and parallel analysis

## Related PR ##

https://github.com/MDAnalysis/mdanalysis/pull/4745

---

## #4868: Feature proposal: Adding a ResidenceTime Analysis Routine

**Labels:** enhancement, Component-Analysis, proposal, MDAKit

#### Summary

Dear MDAnalysis community, I would like to propose a new analysis routine that I have developed, `ResidenceTime`, for MDAnalysis. The routine would allow to analyze how long specific groups of molecules (called "probe groups") stay within a defined distance from another group of molecules (called "reference groups").  By calculating these "residence times," the tool helps quantify solvation dynamics, binding interactions, and local environment stability over time.

I couldn't find this routine among the analysis available in MDAnalysis (hopefully I didn't miss it). The main metric it computes is:

- **Residence Time Distribution**:
  Histograms (both raw and normalized) of residence times with customizable bin sizes or counts.

Additionally, the routine computes the **Average Coordination Number** as a function of time as a secondary analysis. This metric is a natural byproduct of the residence time calculations, as it leverages the same underlying data (probes within the cutoff distance). It tracks how many probe groups stay near the reference groups over time, offering additional insight into coordination dynamics.

---

#### Motivation

I developed this routine to assess the strength of coordination of solvent molecules around ions, but it can also be used to study other dynamic molecular interactions, such as ligand binding or protein-ligand residence times. This work is linked to an upcoming publication where I demonstrate its utility in understanding solvation dynamics.&#x20;

---

#### Key Features

1. **Inputs**:

   - `reference_group`: Atoms to calculate residence times around.
   - `probe_group`: Atoms whose residence times are measured.
   - `radius`: Cutoff distance in Ångstroms.
   - Optional binning: Choose either `bin_size` or `bin_count` for the histogram.

2. **Outputs**:

   - `results.histogram`: Dictionary containing raw and normalized histograms, and bin edges.
   - `results.coordination`: Time series data for average coordination numbers.

3. **Example Use Cases**:

   - Analyze how long water sticks to ions.
   - Track ion coordination in solvation shells or binding sites.

---

#### Parallelization Potential

The routine is designed to be parallelization-friendly. Two approaches could be used to compute the residence time distribution, but I've implemented the second version described here:

1. **Step-by-Step Approach (Not Used Here)**: This method involves analyzing one frame at a time, where the computation of a frame depends on the results of the previous frame to check if a probe molecule is still within the cutoff from the reference. While straightforward in concept, this dependency makes it challenging to divide the workload across multiple processors, limiting its scalability for parallel computation.

2. **Global Monitoring (Implemented Here)**:
   This implementation collects residence data for all probes in one pass and processes it later. This setup c

*[truncated]*

---

## #4847: Support for numpy.dtypes.StringDType in AtomGroup containers?

**Labels:** enhancement, Component-Core

In numpy 2.0+, the new dtype for strings in numpy are StringDType(). However, I don't believe MDAnalysis support this at all? 

Consider the following code:

```
import MDAnalysis as mda
from MDAnalysis.tests.datafiles import PSF, DCD

import numpy as np

u = mda.Universe(PSF, DCD)
is_not_string = u.residues.resnames

```
Running ```print(is_not_string.dtype)``` yields  ```object```. Since the dtype is objects, it means that any of the new numpy 2.0+ ```numpy.strings``` functions would not work and it would require the user to manually cast the ndarray over from the object dtype into ```numpy.dtypes.StringDType``` in order to get it working. Wouldn't it be easier just to have the instance just automatically create create the ndarray as StringDType for convenience? 

Relevant numpy documentation:
[https://numpy.org/doc/stable/user/basics.strings.html](https://numpy.org/doc/stable/user/basics.strings.html) 
[https://numpy.org/doc/stable/reference/routines.strings.html#module-numpy.strings](https://numpy.org/doc/stable/reference/routines.strings.html#module-numpy.strings)

---

## #4838: feat: add `RelPropertySelection` to select atoms based on positions relative to a given selection

**Labels:** enhancement, Component-Selections, decision needed

## Is your feature request related to a problem? ##
When investigating the solid/liquid interface, I would like to take the outermost solid atoms as the reference and analyse the liquid close to the surface (e.g., <= 5 angstroms away from the surface in the direction perpendicular to the surface). However, the reference might shifts during the simulation, and I would like to find a selection updated on-the-fly. 

## Describe the solution you'd like ##
I'd like to add a new selection class `RelPropertySelection`, which can be used in the following way:
`relprop [abs] property operator value selection`
For example, if I want to choose the water with the z distances to the surface smaller than 3 ang, I can use:
`relprop z < 3.0 surface` 
where `surface` is the selection of the outermost surface atoms.

---

## #4828: Make the `AnalysisBase` compatible with live simulation streams

**Labels:** enhancement, Component-Analysis, streaming, decision needed

## Is your feature request related to a problem? ##
<!-- A clear and concise description of what the problem is. For example, I'm always frustrated when [...] -->
Related to #4827: for MDAnalysis to function with live simulation streams, the `AnalysisBase` must be modified to account for a few quirks of live-streamed trajectories:
- Their length/end frame isn't known (so `len(u.trajectory)` and `u.trajectory.n_frames` will fail)
- They can't be sliced in any way except `u.trajectory[:]` and `u.trajectory[::n]` (where n is positive) so they are inherently incompatible with parallelization schemes

## Describe the solution you'd like ##
<!-- A description of what you want to happen. For example, I'd like to be able to do [...] -->
Like with parallelization, analysis classes that inherit from `AnalysisBase` should "opt-in" to stream usage through a class property similar to the `parallelizable` property (like `streamable` or similar). To opt-in, inherited classes must also avoid attempting to access the trajectory's length or slice it. The `rms.RMSF` class is already such a class.

The `AnalysisBase` must also have a `_streamed_run` method that never attempts to slice a trajectory or access its length. The [imdclient MDAKit](https://github.com/Becksteinlab/imdclient/tree/main/imdclient) ships such a method already (and monkey patches it in): https://github.com/Becksteinlab/imdclient/blob/main/imdclient/streamanalysis.py

## Describe alternatives you've considered ##
<!-- A description of any alternative solutions or features you've considered or possible solutions that you've seen elsewhere. -->
Don't allow live simulation streaming, or don't allow builtin analysis classes to be used with these streams

---

## #4819: `analysis.atomicdistances.AtomicDistances` does not use Results

**Labels:** defect, API, Component-Analysis, parallelization

## Expected behavior ##

All analysis classes [based on AnalysisBase](https://docs.mdanalysis.org/stable/documentation_pages/analysis/base.html) store results in an instance of [MDAnalysis.analysis.results.Results](https://docs.mdanalysis.org/stable/documentation_pages/analysis/results.html#MDAnalysis.analysis.results.Results)

> Results are always stored in the attribute [AnalysisBase.results](https://docs.mdanalysis.org/stable/documentation_pages/analysis/base.html#MDAnalysis.analysis.base.AnalysisBase.results), which is an instance of [Results](https://docs.mdanalysis.org/stable/documentation_pages/analysis/results.html#MDAnalysis.analysis.results.Results), a kind of dictionary that allows allows item access via attributes. Each analysis class decides what and how to store in Results and needs to document it. For time series, the [AnalysisBase.times](https://docs.mdanalysis.org/stable/documentation_pages/analysis/base.html#MDAnalysis.analysis.base.AnalysisBase.times) contains the time stamps of the analyzed frames.

The results should be accessible as, e.g., `results.distances`. 

## Actual behavior ##

`analysis.atomicdistances.AtomicDistances.results` directly contains a numpy array.

The lack of API conformity makes it impossible to directly parallelize the class, see PR #4808.


## Code to reproduce the behavior ##

See docs: https://docs.mdanalysis.org/stable/documentation_pages/analysis/atomicdistances.html#MDAnalysis.analysis.atomicdistances.AtomicDistances.results

## Current version of MDAnalysis ##

- Which version are you using? 2.8.0

---

## #4818: Implement `AnalysisBase` class into `MDAnalysis.analysis.hydrogenbonds.hbond_autocorrel`

**Labels:** Component-Analysis, refactoring

Currently [`MDAnalysis.analysis.hydrogenbonds.hbond_autocorrel`](https://github.com/MDAnalysis/mdanalysis/blob/develop/package/MDAnalysis/analysis/hydrogenbonds/hbond_autocorrel.py) does lack an implementation of an an `AnalysisBase` class to have a structure similar to `MDAnalysis.analysis.rms`, which would allow an easier implementation of the parallelization mentioned in #4665 

Things to do:
- Implement an `AnalysisBase` class in `MDAnalysis.analysis.hydrogenbonds.hbond_autocorrel`
- Adjust tests in `test_hydrogenbondautocorrel.py` if required

---

## #4799: [release] TestPyPi post-deployment tests failing on some FULL tests

## Expected behavior ##

All post-deployment tests for TestPypi pass.

## Actual behavior ##

Full dependency tests (named FULL in the matrix) are failing for macos-latest and python 3.13

This is expected because clustalw, hole2, and openmm dependencies aren't compatible for some of these.

## What we need to do ##

Fix the dependency list for those tests.

This is not holding back releases, as long as we know that these are expected failures and everything elses (which it does).

---

## #4796: remove mmtf in 3.0

**Labels:** Format-MMTF, remove-3.0

Remove all mmtf-handling code for 3.0.

- MMTF is no longer supported by PDB (see #4634 )
- the mmtf-python license is incompatible with our target license LGPLv2.1+ (see https://www.mdanalysis.org/2023/09/22/licensing-update/#why-the-interim-gpl-v3-and-lgpl-v3-package-licenses-the-issue-with-apache-20 )

---

## #4788: LAMMPS DumpReader returns incorrect coordinate transform

**Labels:** Component-Readers, format-LAMMPS, more information needed

## Expected behavior ##

The coordinate transform of "scaled" LAMMPS trajectory should be imported correctly.


## Actual behavior ##
The MDAnalysis calculated incorrectly coordinates from scaled to unscaled. Calculation method of “scaled” is xs = (x-xlo)/(xhi-xlo). So, when  coordinate transform, the coordinate can be calculated by x = (xhi-xlo)*xs + xlo. However, the  LAMMPS DumpReader returns incorrect coordinate transform. For example, the scaled coordinate in my dump is 
``` 
ITEM: TIMESTEP
0
ITEM: NUMBER OF ATOMS
6024
ITEM: BOX BOUNDS pp pp pp
3.3501000000000003e-02 6.2616999999999997e+01
-5.2700000000000002e-01 2.8887000000000000e+01
-1.5000000000000000e+01 4.0000000000000000e+01
ITEM: ATOMS id type xs ys zs
2608 2 0.0407033 0.457803 0.384662
``` 
The real coordinate of atom 2608 is [2.58086, 12.9388, 6.15641]. However, the coordinate calculated by DumpReader is [2.513854, 13.992818, 36.15641]. Calculation method of DumpReader seem to be x = (xhi-xlo)*xs - xlo. Other atoms are tested and the same error happened.

## Code to reproduce the behavior ##

<!-- Show us how to reproduce the failure. If you can, use trajectory files from the test data. Use the code snipped below as a starting point. -->

``` python
import numpy as np
import MDAnalysis as mda
from MDAnalysis.analysis.hydrogenbonds import HydrogenBondAnalysis
from MDAnalysis.analysis import hydrogenbonds

# load system
u = mda.Universe("carbonice3nm.data", "ice.lammpstrj", format="LAMMPSDUMP", lammps_coordinate_convention="scaled", dt=10)

O = u.select_atoms('id 2608')
print(O.positions)

## Current version of MDAnalysis ##

- Which version are you using? (2.8.0)
- Which version of Python? (3.10.0)
- Which operating system? (Windows)
- LAMMPS version 2 Aug 2023

---

## #4781: Stop building macos x86_64 wheels with v2.9.0?

**Labels:** question, release, decision needed

The macos-12 runners are going away in December, and the macos-13 runners can be somewhat problematic.

Now might be a good time to review if we want to keep x86_64 pypi wheels support for macos - have folks sufficiently moved on to osx-arm64?

---

## #4774: Minimum image convention not working for distances.distance_array

**Labels:** Component-lib, PBC, more information needed

I am using mda.analysis.distances.distance_array() to calculate all of the distances between alpha carbons of arginine residue with resid 2 in a cluster and the centroid of the cluster. After identifying the cluster and the coordinates of the centroid, the lines to calculate distances looks like this:

```python
sel = univ.select_atoms(f'resnum 2 and resname ARG and name CA')
dists = distances.distance_array(centroid, sel.atoms.positions, univ.dimensions)
```

No errors occur and the calculation seems to go smoothly. However, I am getting distances as large as ~89 angstroms in a box with dimensions: [92.57094, 92.57094, 92.57094]. I am under the impression that by passing "univ.dimensions", periodic boundary conditions are supposed to be accounted for through minimum image convention, but there aren't any situations where the clusters in my trajectories should have that large of radii, let alone distances from the centroid. I am just curious if there is a way to assure that periodic boundary conditions will be accounted for. 

Thank you

---

## #4722: Cannot read default LAMMPS H5MD file out of the box due to lack of `units` tag

**Labels:** defect, Component-Readers, format-LAMMPS, Format-H5MD

## Expected behavior ##

<!-- A clear and concise description of what you want to do and what you think should happen. (Code to reproduce the behavior can be added below). -->

We are not necessarily doing anything wrong, but just notifying people that we cannot read H5MD files produced by LAMMPS out of the box. LAMMPS does not use the `units` tag in the H5MD spec, meaning you must specify `convert_units=False`


## Code to reproduce the behaviour ##
Have the following in LAMMPS input file
```
write_data system.data
dump h5md1 all h5md 100 dump.h5md position velocity force
```


```python
import MDAnalysis as mda
u = mda.Universe("system.data", "dump.h5md", atom_style='id type x y z', convert_units=True)
```

whereas the below will work, 

```python
import MDAnalysis as mda
u = mda.Universe("system.data", "dump.h5md", atom_style='id type x y z', convert_units=False)
```

The resulting system will have units of whatever LAMMPS unit style you chose.

## Current version of MDAnalysis ##
2.8.0dev0

---

## #4713: Expose Dask "lazy timeseries" from compatible readers for full parallelism in analysis

**Labels:** enhancement, Component-Readers, parallelization

## Is your feature request related to a problem? ##

This idea follows up on @orbeckst's suggestion from a few months ago and a discussion with @hmacdope about making full use of dask in mda.

Current parallelism development allows splitting a trajectory into a number of parts and then combining intermediate results. However, allowing analysis classes to use dask arrays for positions, velocities, forces across the entire trajectory can cover cases that the split-apply-combine paradigm doesn't cover (like RMSF, AFAIK) and potentially lead to greater speedup. 

## Describe the solution you'd like ##

A `DaskTimeSeriesAnalysisBase` which accepts a `dasktimeseries` as an argument. A dask timeseries is exactly the same as a reader's `timeseries` except that it is a `dask.array` rather than a `numpy.ndarray`, so it is loaded lazily into memory and a dask task graph is created and optimized by dask automatically before `.compute()` is called.

## Describe alternatives you've considered ##
Do nothing.

## Additional context ##

I provide an extremely minimal example in PR #4714. Here, using dask to perform RMSF rather than in serial leads to a speedup of ~15x

Sample notebook available here: https://github.com/ljwoods2/mdanalysis/blob/dask-timeseries/tmp/lazyts.ipynb

---

## #4697: Type guessing should attempt to go via elements first

**Labels:** Component-Topology

## Current behaviour

The current behaviour, and something we reinforce in #3753 is that type works by attempting to guess elements from atom names.

## Proposed behaviour

The proposal here is to always try to attempt to read from elements first rather than guessing through names. If elements exist AND they are complete, then you return those, rather than guessing them.

## Where would this matter?

A good example here is FHIAIMS where:

names == elements
types == guessed elements from names

In this case it would have just been "safer" (i.e. fewer code bits gone through) to just do names == elements == types.

## Target release

This needs discussion. From my own limited look at things, there aren't any cases where making this behaviour change would negatively impact behaviour. Indeed, I'm not sure I can see any cases where behaviour would change.

---

## #4676: `MDAnalysis.analysis.msd`: Implement parallelization or mark as unparallelizable

**Labels:** help wanted, Component-Analysis, parallelization

Given a newly implemented parallelization (https://docs.mdanalysis.org/dev/documentation_pages/analysis/parallelization.html), implement it for all classes in `analysis.msd` module. You may use `analysis.RMSD` in `develop` as a reference.

You need to add:

 - appropriate implementation of result aggregation for AnalysisBase subclasses in `analysis.msd` module (or explicitly limit available backends if the classes aren't parallelizable)
 - a boilerplate fixture(s) to `testsuite/analysis/conftest.py`, analogous with existing ones
 - a `client_...` fixtures to all tests using in `testsuite/MDAnalysisTests/analysis/test_msd.py`, and modify the way run() method is called

---

## #4666: `MDAnalysis.analysis.hydrogenbonds.WaterBridgeAnalysis`: Implement parallelization or mark as unparallelizable

**Labels:** help wanted, Component-Analysis, parallelization

Given a newly implemented parallelization (https://docs.mdanalysis.org/dev/documentation_pages/analysis/parallelization.html), implement it for all classes in `analysis.hydrogenbonds.WaterBridgeAnalysis` module. You may use `analysis.RMSD` in `develop` as a reference.

You need to add:

 - appropriate implementation of result aggregation for AnalysisBase subclasses in `analysis.hydrogenbonds.WaterBridgeAnalysis` module (or explicitly limit available backends if the classes aren't parallelizable)
 - a boilerplate fixture(s) to `testsuite/analysis/conftest.py`, analogous with existing ones
 - a `client_...` fixtures to all tests using in `testsuite/MDAnalysisTests/analysis/test_waterdynamics.py`, and modify the way run() method is called

---

## #4665: `MDAnalysis.analysis.hydrogenbonds.hbond_autocorrel`: Implement parallelization or mark as unparallelizable

**Labels:** help wanted, Component-Analysis, parallelization

Given a newly implemented parallelization (https://docs.mdanalysis.org/dev/documentation_pages/analysis/parallelization.html), implement it for all classes in `analysis.hydrogenbonds.hbond_autocorrel` module. You may use `analysis.RMSD` in `develop` as a reference.

You need to add:

 - appropriate implementation of result aggregation for AnalysisBase subclasses in `analysis.hydrogenbonds.hbond_autocorrel` module (or explicitly limit available backends if the classes aren't parallelizable)
 - a boilerplate fixture(s) to `testsuite/analysis/conftest.py`, analogous with existing ones
 - a `client_...` fixtures to all tests using in `testsuite/MDAnalysisTests/analysis/test_hydrogenbondautocorrel.py`, and modify the way run() method is called

---

## #4662: `MDAnalysis.analysis.atomicdistances`: Implement parallelization or mark as unparallelizable

**Labels:** help wanted, Component-Analysis, parallelization

Given a newly implemented parallelization (https://docs.mdanalysis.org/dev/documentation_pages/analysis/parallelization.html), implement it for all classes in `analysis.atomicdistances` module. You may use `analysis.RMSD` in `develop` as a reference.

You need to add:

 - appropriate implementation of result aggregation for AnalysisBase subclasses in `analysis.atomicdistances` module (or explicitly limit available backends if the classes aren't parallelizable)
 - a boilerplate fixture(s) to `testsuite/analysis/conftest.py`, analogous with existing ones
 - a `client_...` fixtures to all tests using in `testsuite/MDAnalysisTests/analysis/test_atomicdistances.py`, and modify the way run() method is called

---

## #4659: `MDAnalysis.analysis.align` Implement parallelization or mark as unparallelizable

**Labels:** help wanted, Component-Analysis, parallelization

Given a newly implemented parallelization (https://docs.mdanalysis.org/dev/documentation_pages/analysis/parallelization.html), implement it for all classes in `analysis.align` module. You may use `analysis.RMSD` [example](https://docs.mdanalysis.org/dev/documentation_pages/analysis/parallelization.html#adding-parallelization-to-your-own-analysis-class) as a reference.

You need to add:

- appropriate implementation of result aggregation for `AnalysisBase` subclasses in `analysis.align` module
 - a boilerplate fixture(s) to `testsuite/analysis/conftest.py`, analogous with existing ones
 - a `client_<classname>` fixtures to all tests using `<classname>` in `testsuite/MDAnalysisTests/analysis/test_align.py`, and modify the way `run()` method is called

---

## #4645: add environment.yml for developer installation

## Is your feature request related to a problem? ##
We are lacking clear installation instructions for developers on how to install the *develop* branch for hacking and testing, see issue https://github.com/MDAnalysis/UserGuide/issues/368 and discussion https://github.com/MDAnalysis/mdanalysis/discussions/4636

In particular, we want to be able to have a **complete full-feature installation** and that requires **conda-forge** packages. Thus, the `pip`-installation procedure outlined in https://github.com/MDAnalysis/mdanalysis/discussions/4636#discussioncomment-10108984 is not what we would recommend first as it cannot install all packages (rdkit? hole? ...)


## Describe the solution you'd like ##
The growing consensus   is that we (see https://github.com/MDAnalysis/UserGuide/issues/368#issuecomment-2237178295 ) we should include a simple `develop_environment.yaml` file in the source tree (possibly removing/commenting out hole2, distopia, and clustalw (do we really still use clustalw???) — we can add a note for these) and then write our installation instructions with reference to this file.

This file has to be maintained manually for right now but I'd expect that this doesn't happen too often.


## Describe alternatives you've considered ##
See https://github.com/MDAnalysis/UserGuide/issues/368 and discussion https://github.com/MDAnalysis/mdanalysis/discussions/4636


## Additional context ##
Once we have the environment file, we _could_ at a later time add CI that tests that this file corresponds to what we install in CI. 

There exists a file [maintainer/conda/environment.yml](https://github.com/MDAnalysis/mdanalysis/blob/develop/maintainer/conda/environment.yml) but I don't know what its purpose is.

---
