# #24258

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/24240
**Scraped:** 2026-02-22T23:28:47.573430

---

## [CZI] Addition of biomechanical modelling to SymPy

**Labels:** CZI: Codegen/Biomech

## CZI EOSS Grant & Biomechanics

One stated outcome from the CZI work is the development of performance-critical musculoskeletal models using SymPy. Creation of musculoskeletal models requires the merging of multibody dynamics and biomechanical models. The former is already implemented supported by SymPy thanks to `sympy.physics.mechanics`. The latter requires the development of additional SymPy-based classes, functions, and integrations.

## Development Proposal

I propose that certain biomechanical modelling capabilities are added directly into SymPy. This would be done through the creation of a new biomechanics submodule. The intention would be for this to be `sympy.physics.biomechanics`. However, it would initially be developed as the private development submodule `sympy.physics._biomechanics`. This would allow for the submodule to be developed transparently, with other SymPy users able to contribute and feed back during its development, while also not adding any restrictions around backwards compatibility guarantees or breaking changes.

Eventually, once the submodule features and API have been reviewed and tested, the intention would be to transition `sympy.physics._biomechanics` to the public module `sympy.physics.biomechanics`.

## Development Workflow

- PR #24228 shows the current state of development of the biomechanics submodule and its diff to `master`
- This work is related to other work on building a high-level API for `sympy.physics.mechanics` (PR #24234)
- New issues will be opened to initiate discussion around, and gather feedback on, more specific areas
- Announcements will be made on a new discussion on the SymPy mailing list

## Submodule Requirements
- Extends and interfaces nicely with `sympy.physics.mechanics` and `sympy.physics.vector`.
- Implements published models from the literature.
- Supports torque- and muscle-driven musculoskeletal models.
- Supports creation of 2D and 3D musculoskeletal models.
- Fully documented, tested, and benchmarked.
- Provides a basic set of sample models for users to get started with.

