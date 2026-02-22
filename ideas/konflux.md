# Konflux — Project Ideas

**Source:** https://github.com/konflux-ci/community/wiki/Google-Summer-of-Code-&-Outreachy-Project-Ideas-%E2%80%90-2026
**Scraped:** 2026-02-22T23:28:47.581266

---

# Google Summer of Code & Outreachy Project Ideas - 2026

Below you will find a list of proposed projects. Each idea includes essential information to help you understand the scope, required skills, and who to contact for more details.

## Important Notes for Applicants

* **Project Scope:** Some projects might be adaptable in scope to fit _GSoC_'s 175-hour or 350-hour options, or _Outreachy_'s 40-hour/week commitment. Discuss this with your mentor.
* **Skill Requirements:** While specific programming languages and technologies are listed, enthusiasm and a willingness to learn are often just as important. Don't be discouraged if you don't know every single technology listed.
* **Community Engagement:** We highly recommend engaging with our community before applying. This could involve contributing to our repositories, participating in discussions, or attending our meetings (if any).

---

## Project ideas table

* [Reproducible Builds](#reproducible-builds)
* [zstd:chunked compression](#zstd-chunked-compression)
* [prefetch: Adding support for the `uv` Python package manager to the Hermeto project](#prefetch-adding-support-for-the-uv-python-package-manager-to-the-hermeto-project)
* [prefetch: Adding support for the Debian/Ubuntu package ecosystem [DEB] to the Hermeto project](#prefetch-adding-support-for-the-debianubuntu-package-ecosystem-deb-to-the-hermeto-project)
---

## Reproducible Builds
* **Assessment level**: intermediate
* **Programming Languages:** Go, Bash
* **Technologies:** Docker, Tekton, Buildah
* **Mentors:**
    * Ralph Bean <ralph.bean@gmail.com>

### Description

The goal of this project is to demonstrate bit-wise reproducible builds in Konflux.

Konflux is all about supply chain security, and [reproducible builds](https://reproducible-builds.org/) are a great property to have if you want to be able to verify that the build system hasn't been tampered with. For the purposes of this project, a build is "bit-wise reproducible" if you can build it twice and get a binary output with the same sha256 digest.

**Expectations:**
* Familiarize yourself with the [buildah task](https://github.com/konflux-ci/build-definitions/tree/main/task/buildah-oci-ta) used in the konflux container build pipeline, and what other tasks are used to populate its parameters. Notice how if you build a container from the same commit twice, you get a container image with a different digest each time. Not reproducible!
* Research methods used by other systems and other communities to improve the degree of their support for reproducible builds. Example: [fixing the timestamp of the build to the timestamp of the commit](https://github.com/konflux-ci/build-definitions/issues/1268).
* Propose a series of example experiments to demonstrate that different kinds of containerfiles are or are not reproducible.
* Propose a series of patches or improvements to the konflux build pipeline tasks to increase the number of your example experiments that successfully produce reproducible builds.
---

## zstd:chunked compression
* **Assessment level**: intermediate
* **Programming Languages:** Go, Bash
* **Technologies:** Docker, Tekton, Buildah
* **Mentors:**
    * Ralph Bean <ralph.bean@gmail.com>

### Description

The goal of this project is to demonstrate building and releasing containers through Konflux with zstd:chunked compression.

Container images are normally stored and distributed with gzip compression. zstd:chunked is a more modern alternative that offers a number of performance improvements.

**Expectations:**
* Research other communities and tools that offer zstd:chunked compression.
* Research prior discussions about adopting zstd:chunked compression [in Konflux](https://github.com/konflux-ci/build-definitions/issues/1264) and [in Fedora](https://fedoraproject.org/wiki/Changes/zstd:chunked).
* Modify the build tasks in Konflux ecosystem to support producing images with zstd:chunked compression.
* Build out integration and e2e test cases that prove that images distributed with zstd:chunked compression can be successfully handled by the konflux release pipelines.
* Find and fix scenarios in the release pipelines where zstd:chunked compression is problematic.

## prefetch: Adding support for the `uv` Python package manager to the Hermeto project
* **Assessment level**: intermediate
* **Programming Languages:** Python
* **Technologies:** Docker
* **Project scope**: 12 weeks
* **Mentors:**
    * Erik Skultety <skultety.erik@gmail.com>
    * Alexey Ovchinnikov <alexaovchinn@gmail.com>

### Project background
https://github.com/hermetoproject/hermeto is a dependency fetching tool that enables CI platforms (like Konflux CI) to
* utilize fully offline, network-isolated container builds by pre-fetching all required dependencies and
* achieve high levels of SLSA compliance by providing a Software Bill of Materials (SBOM) of the fetched artifacts
It implements backend support for various package ecosystems including pip, npm, Go, Cargo, etc.

### Description

The goal of this project is to introduce a new Python package ecosystem prefetch backend to the [Hermeto](https://github.com/hermetoproject/hermeto) project able to process the `uv` Package manager ecosystem natively.

Hermeto currently only supports prefetching packages for Python projects for the Pip ecosystem which revolves around the notion of `requirements` files. While `uv` is backwards compatible with pip (at least as far as the Hermeto project is concerned) and can work with `requirements` files via the its pip module invocation that is NOT the native way. `uv` has its own workflow based on `uv lock` and `uv sync` that will have to be supported natively in this new backend.

**Expectations:**
* research the whole `uv` ecosystem:
  - how dependencies are recorded in the `uv.lock` lockfile, what format does the file follow
  - what it takes to update the dependencies in the lockfile
  - inspecting `uv`'s internals to verify whether there's a potential arbitrary code execution path possible
* record the problem domain research in form of a thorough design document proposal against the Hermeto project
* implement support for dependency fetching for the `uv` ecosystem based on the design document
* integrate the new backend's functionality with Hermeto's SBOM artifact generating machinery to record all fetched dependencies for the `uv` ecosystem
* address quality aspects of the solution via unit & integration tests
* document the functionality in form of a user facing docs page

## prefetch: Adding support for the Debian/Ubuntu package ecosystem [DEB] to the Hermeto project

 * **Assessment level:** advanced
 * **Programming Languages:** Python
 * **Technologies:** Debian packaging format and tools (dpkg, apt), Docker
 * **Project scope:** 12 weeks
 * **Mentors:**
    - Erik Skultety <skultety.erik@gmail.com>

### Project background
https://github.com/hermetoproject/hermeto is a dependency fetching tool that enables CI platforms (like Konflux CI) to
* utilize fully offline, network-isolated container builds by pre-fetching all required dependencies and
* achieve high levels of SLSA compliance by providing a Software Bill of Materials (SBOM) of the fetched artifacts
It implements backend support for various package ecosystems including pip, npm, Go, Cargo, etc.

### Description

This project aims to extend [Hermeto](https://github.com/hermetoproject/hermeto) with support for the Debian/Ubuntu package ecosystem (.deb packages), enabling offline builds for Debian-based container images. Unlike ecosystems such as NPM or Cargo, the Debian world lacks a standardized lockfile format for pinning exact package versions with checksums. This gap presents both a challenge and an opportunity for original research and tooling development.

There are two major components to successfully completing this project:

1. Ecosystem research & lockfile/manifest schema design: A comprehensive study of the Debian packaging ecosystem, including:
  - dependency resolution mechanisms
  - repository metadata formats
  - existing tooling
This research will inform the design of a manifest (a "lockfile") schema specification that captures all information needed for reproducible package fetching.

2. Hermeto DEB backend implementation: A new package manager backend for Hermeto that consumes the manifest, downloads '.deb' packages from
specified mirrors, verifies checksums, generates SBOM (Software Bill of Materials) components, and produces repository metadata for offline `apt` installation.

Additionally to the above, a prototype manifest generator tool will need to be developed to demonstrate end-to-end functionality. This generator will resolve dependencies for a given set of packages and produce a valid manifest file. The https://github.com/konflux-ci/rpm-lockfile-prototype in the Konflux organization dealing with the RPM ecosystem serves as an excellent reference implementation for this particular use case.

**Expectations:**
  - Research and document the Debian package ecosystem
  - Evaluate existing DEB manifest approaches (if any) and reproducible builds tooling
  - Design a DEB manifest schema suitable for Hermeto consumption, drawing parallels to the existing `rpms.lock.yaml` format
  - Implement a Hermeto backend that fetches '.deb' packages based on the manifest
  - Implement a post-processing step to generate local repository metadata for offline `apt` usage
  - Develop a prototype manifest generator tool that resolves dependencies and outputs valid manifest files based on the schema
  - Provide user documentation following the style of existing Hermeto package manager guides
  - Create integration tests validating the complete fetch → inject → offline-install workflow

**Return to [Home Page](/ideas/konflux/home)**
