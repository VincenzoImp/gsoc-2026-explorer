# hyperSpec-HPC: Fast Sparse Spectral Kernels in R and Rust

**Parent:** R project for statistical computing — Project Ideas
**Source:** https://github.com/rstats-gsoc/gsoc2026/wiki/hyperSpec%E2%80%90HPC
**Scraped:** 2026-03-10T16:58:40.306633

---

# hyperSpec-HPC: Fast Sparse Spectral Kernels in R and Rust

## Background

The [hyperSpec](https://github.com/r-hyperspec/hyperSpec) package is the gold standard for spectroscopic data in R. While the "Grammar of Data" (via `dplyr`) was [fortified in GSoC 2020](https://eoduniyi.github.io/hyperSpec.gsoc2020/), the computational backend remains a bottleneck for large datasets. Spectral filtering, baseline correction, and dimensionality reduction all run in pure R or rely on dense matrix operations that scale poorly.

This project proposes a focused Rust-powered backend for one high-value bottleneck: **sparse Laplacian-based spatial smoothing on hyperspectral data**. Hyperspectral images (e.g., Raman maps, NIR imaging) are the natural use case for graph-structured spectral processing — pixels are nodes, spatial adjacency defines edges, and filtering across the graph removes spatially correlated noise while preserving spectral features. Standard [1D FFT](https://en.wikipedia.org/wiki/Fast_Fourier_transform) or [Savitzky-Golay filters](https://en.wikipedia.org/wiki/Savitzky%E2%80%93Golay_filter) operate on each pixel independently and cannot exploit this spatial structure.

The bridge between R and Rust is [extendr](https://extendr.github.io/extendr/extendr_api/), a memory-safe alternative to Rcpp that replaces manual pointer management with ownership-tracked buffers. The goal is not to replace Rcpp — which is mature and battle-tested — but to demonstrate that new hyperSpec extensions can be written in Rust with less risk of memory bugs and with cleaner error handling at the R boundary.

## Related work / impact

- [hyperSpec](https://github.com/r-hyperspec/hyperSpec): S4 class for spectroscopic data, dplyr integration (GSoC 2020)
- [extendr](https://extendr.github.io/extendr/extendr_api/): R-to-Rust FFI with automatic type conversion for primitive types and dense matrices
- [faer](https://github.com/sarah-ek/faer-rs): Modern Rust linear algebra library with a sparse module and iterative solvers (CG, BiCGSTAB) — the primary math backend for this project. Use version 0.19+ to ensure sparse iterative solver support.
- [petgraph](https://github.com/petgraph/petgraph): Rust graph construction and adjacency logic
- [Rcpp](https://www.rcpp.org/): Existing C++ bridge (this project is a memory-safe alternative, not a replacement)
- [Graph Signal Processing](https://www.youtube.com/watch?v=sqr1EJIIRVw): the mathematical framework underlying this project — signals on graphs, graph Fourier transform, spectral filtering
- [Normalized Graph Laplacian](https://en.wikipedia.org/wiki/Laplacian_matrix#Symmetric_normalized_Laplacian): the core operator; eigendecomposition gives the graph Fourier basis
- [Compressed Sparse Column (CSC)](https://github.com/rstats-gsoc/gsoc2026/wiki/<https:/en.wikipedia.org/wiki/Sparse_matrix#Compressed_sparse_column_(CSC_or_CCS)>): the sparse matrix format used by R's `dgCMatrix` and `faer`
- [Conjugate Gradient method](https://en.wikipedia.org/wiki/Conjugate_gradient_method): iterative solver for (I + αL)x = b when L is symmetric positive semi-definite
- [BiCGSTAB](https://en.wikipedia.org/wiki/Biconjugate_gradient_stabilized_method): iterative solver for non-symmetric systems

hyperSpec is widely used in chemometrics, Raman spectroscopy, and NIR analysis. Hyperspectral imaging datasets (512×512 pixels × 2048 wavelengths, ~4GB) are where pure-R performance breaks down most visibly and where an O(N) sparse solver in Rust will substantially outperform dense R implementations.

## Details of your coding project

The contributor will implement one focused, high-value kernel: **graph-based spatial smoothing for hyperspectral images**, using sparse Laplacian solvers in Rust exposed to R via extendr.

**Why graph filtering here specifically?**
A [hyperspectral image](https://en.wikipedia.org/wiki/Hyperspectral_imaging) is a 3D array (x × y × λ). Standard spectral processing treats each pixel independently. But spatially adjacent pixels often share the same chemical composition — the graph structure is real and exploitable. A [graph low-pass filter](https://arxiv.org/pdf/2008.01305) solves (I + αL)x = b for each wavelength band, smoothing spatially while preserving spectral features. With a [sparse Laplacian](https://en.wikipedia.org/wiki/Laplacian_matrix), this is O(N) per band using iterative solvers ([CG](https://en.wikipedia.org/wiki/Conjugate_gradient_method)/[BiCGSTAB](https://en.wikipedia.org/wiki/Biconjugate_gradient_stabilized_method)), not O(N³).

**The FFI challenge — be aware:**
R's sparse matrices use `dgCMatrix` from the Matrix package: a [Compressed Sparse Column (CSC)](https://github.com/rstats-gsoc/gsoc2026/wiki/<https:/en.wikipedia.org/wiki/Sparse_matrix#Compressed_sparse_column_(CSC_or_CCS)>) format with three slots (`i`, `p`, `x`). extendr does not have a native zero-copy wrapper for `dgCMatrix`. The contributor will need to manually extract each slot as an R vector, validate the pointers, and wrap them in Rust slices to construct a `faer` sparse matrix. This is non-trivial — a mistake here doesn't throw a clean error, it crashes the R session. The project will document this mapping explicitly as a reusable pattern for future hyperSpec-Rust extensions.

**What "memory-safe" actually means here:**
Rust's [ownership system](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html) prevents buffer overflows and use-after-free bugs that are common in Rcpp extensions. At the R boundary, we provide informative runtime errors — not silent failures or session crashes. A non-conforming matrix passed from R gets a clean, descriptive error message. This is the honest version of "safer," not [formal verification](https://en.wikipedia.org/wiki/Formal_verification).

**Deliverables:**

1. `hyperspec.rust` R package skeleton using extendr, with CI and basic tests
2. `dgCMatrix` → `faer` sparse matrix bridge, documented as a reusable FFI pattern
3. Pixel neighborhood graph construction using `petgraph`
4. Sparse Laplacian solver in Rust using `faer` 0.19+ iterative solver (CG/BiCGSTAB) for (I + αL)x = b. The `neighbors` parameter specifies connectivity (e.g., 4-connectivity or 8-connectivity grid); the Rust side generates the adjacency graph via `petgraph` rather than accepting a pre-built matrix from R, keeping the R-to-Rust transfer minimal.
5. R-level S4 method `graphSmooth(hy, alpha, neighbors)` dispatching to the Rust kernel
6. Benchmark: Rust kernel vs pure-R implementation on a 512×512×2048 hyperspectral dataset (~4GB)
7. Vignette: "Spatial smoothing of hyperspectral Raman maps using graph filtering"

**Out of scope for this project:**

- Full GFT eigendecomposition (O(N³), not practical for large graphs)
- GPU acceleration
- Replacing Rcpp across the hyperSpec ecosystem
- Formal verification (Kani, Prusti) — this is memory safety, not proof-based verification

## Expected impact

A fast, memory-safe sparse Laplacian solver for hyperspectral data fills a real gap in the R spectroscopy ecosystem. The `dgCMatrix` → `faer` FFI bridge also serves as a reference implementation for future Rust extensions to hyperSpec, solving the hardest part of the R-Rust boundary once so others don't have to.

## Mentors

Contributors, please contact mentors below after completing at least one of the tests below.

- EVALUATING MENTOR: Erick Oduniyi eeoduniyi@gmail.com (GSoC 2020 hyperSpec contributor).

## Tests

Contributors, please do one or more of the following tests before contacting the mentors above.

- **Easy:** Install hyperSpec in R. Load the `flu` or `laser` dataset. Write a script that constructs a simple pixel adjacency matrix from a 2D spatial grid and computes its graph Laplacian using base R. Plot the result.
- **Medium:** Create a minimal R package using `extendr`. Pass a dense matrix from R to Rust, compute its row sums in Rust using `faer`, and return the result to R. Include a test.
- **Hard:** Extract the `i`, `p`, and `x` slots from an R `dgCMatrix` sparse matrix via extendr. Wrap them as Rust slices and construct a `faer` sparse matrix. Return the degree vector (row sums) to R using extendr's `WritableSlice` to avoid an unnecessary allocation, and verify it matches the pure-R result.

## Solutions of tests

Contributors, please post a link to your test results here.

- EXAMPLE CONTRIBUTOR 1 NAME, LINK TO GITHUB PROFILE, LINK TO TEST RESULTS.
- Tamaghna Chattopadhyay : [GitHub Profile link](https://github.com/shinigami-777), [Easy test](https://github.com/shinigami-777/hyperSpec-Tasks/tree/main/easy_task), [Medium Test](https://github.com/shinigami-777/hyperSpec-Tasks/tree/main/medium_task), [Hard Test](https://github.com/shinigami-777/hyperSpec-Tasks/tree/main/hard_task).
