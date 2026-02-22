# Kornia — Project Ideas

**Source:** https://github.com/kornia/kornia-rs/wiki/%5B2026%5D-Google-Sumer-of-Code-Application
**Scraped:** 2026-02-22T23:28:47.604353

---

![Google Summer of Code](https://raw.githubusercontent.com/kornia/data/main/gsoc_2026_banner.png)

⚠️ ⚠️ [[ **READ APPLICATION PROTOCOL**]](https://github.com/kornia/kornia-rs/wiki/Google-Sumer-of-Code-Application) ⚠️ ⚠️

# Kornia-rs GSoC 2026 Project Ideas

**Timeline (official):**
- Org application deadline: **Feb 3, 2026 (18:00 UTC)**
- Accepted orgs announced: **Feb 19, 2026 (18:00 UTC)**
- Contributor application window: **Mar 16–Mar 31, 2026 (18:00 UTC)**

**How this ideas list helps our application:**
- Clear, scoped projects with measurable outcomes
- Defined prerequisites and evaluation criteria
- Community impact across core kornia-rs crates

## AI Tooling Policy (GSoC 2026)

We follow Google’s 2026 guidance on AI tooling for both contributors and mentoring orgs. **Using AI is allowed only when it is transparent, limited, and fully understood by the contributor.** Raw AI output is not accepted.

**Allowed uses (with disclosure):**
- Research and learning (reading papers, summarizing docs)
- Boilerplate/refactoring, test scaffolding, or debugging support

**Not allowed:**
- Submitting AI‑generated proposals as-is
- Committing code you cannot fully explain
- Copying AI output without review and verification

**Contributor responsibility:** You remain 100% responsible for correctness, licensing, and explaining every line you submit. If you used AI, say where and how in your proposal and PRs.

---

## Projects Index

1. [GPU acceleration for kornia-tensor and kornia-imgproc](#1-gpu-acceleration-for-kornia-tensor-and-kornia-imgproc)
2. [Expand kornia-vlm with ONNX/TensorRT backends](#2-expand-kornia-vlm-with-onnxtensorrt-backends)
3. [kornia-SLAM: baseline Visual-Inertial Odometry (VIO)](#3-kornia-slam-baseline-visual-inertial-odometry-vio)
4. [Bubbaloop simulation integration and improvements (MuJoCo)](#4-bubbaloop-simulation-integration-and-improvements-mujoco)
5. [Bubbaloop real-robot integration](#5-bubbaloop-real-robot-integration)

**Projects are ordered by soft priority.**

---

## 1. GPU acceleration for kornia-tensor and kornia-imgproc

**Description**
Implement GPU kernels for core tensor ops and image processing transforms in Rust. Focus on frequently used operations (resize, warp_affine/warp_perspective, color transforms, distance transform) and ensure API parity with existing CPU implementations. Use CubeCL (multi-platform GPU compute in Rust) and/or native CUDA interop as appropriate.

**Expected Outcomes**
- Minimal GPU backend for kornia-tensor ops used by kornia-imgproc
- GPU implementations for a handful of high-impact transforms
- Benchmarks vs CPU and basic docs/examples

**Resources**
- CubeCL (Rust GPU compute): https://github.com/tracel-ai/cubecl
- Rust std on GPU (Vectorware blog): https://www.vectorware.com/blog/rust-std-on-gpu/
- CUDA Toolkit docs: https://docs.nvidia.com/cuda/
- kornia-rs repository: https://github.com/kornia/kornia-rs

**Possible Mentors**: Edgar Riba, Jian Shi, Christie Purackal

**Difficulty**: Hard

**Duration**: 350 hours

---

## 2. Expand kornia-vlm with ONNX/TensorRT backends

**Description**
Bring more vision-language models from kornia (PyTorch) into kornia-rs and deliver optimized inference via ONNX Runtime with TensorRT where available. Focus on model portability and clear runtime selection (CPU/CUDA/TensorRT), with an emphasis on embedded targets (e.g., Jetson).

**Expected Outcomes**
- 1–2 VLM models integrated into kornia-vlm
- ONNX Runtime backend + optional TensorRT path
- Benchmarks and a small demo

**Resources**
- ONNX Runtime TensorRT Execution Provider: https://onnxruntime.ai/docs/execution-providers/TensorRT-ExecutionProvider.html
- ONNX-TensorRT backend: https://github.com/onnx/onnx-tensorrt
- Kornia (PyTorch) project: https://github.com/kornia/kornia
- kornia-rs repository: https://github.com/kornia/kornia-rs

**Possible Mentors**: Edgar Riba,  Miquel Farré

**Difficulty**: Medium–Hard

**Duration**: 350 hours

---

## 3. kornia-SLAM: baseline Visual-Inertial Odometry (VIO)

**Description**
Formalize and extend our kornia-SLAM crate within kornia-rs and implement a baseline visual-inertial odometry pipeline. Extend the crate to support stereo VIO, add GPU support, optimize existing kernels, and extend functionality toward LiDAR SLAM techniques. Emphasis on a modular API that can later host learning-based modules.

**Expected Outcomes**
- kornia-slam crate integrated into workspace
- Baseline VIO pipeline + dataset evaluation
- Benchmarks for CPU/GPU performance and accuracy
- Documentation + example CLI

**Resources**
- SLAM Handbook: https://github.com/SLAM-Handbook-contributors/slam-handbook-public-release
- ORB SLAM3 repository: https://github.com/UZ-SLAMLab/ORB_SLAM3

**Possible Mentors**: Christie Purackal, Dmytro Mishkin, Edgar Riba

**Difficulty**: Hard

**Duration**: 350 hours

---

## 4. Bubbaloop simulation integration and improvements (MuJoCo)

**Description**
Improve the Bubbaloop simulation stack by integrating or enhancing a MuJoCo-based workflow. Focus on stable simulation bindings, reproducible training/evaluation loops, and better tooling for dataset generation and benchmarking.

**Expected Outcomes**
- MuJoCo integration with example tasks
- Simulation-focused training/evaluation scripts
- Documentation + demo video

**Resources**
- Bubbaloop repository: https://github.com/kornia/bubbaloop
- kornia-rs repository: https://github.com/kornia/kornia-rs

**Possible Mentors**: Edgar Riba, Jian Shi, Christie Purackal

**Difficulty**: Medium–Hard

**Duration**: 350 hours

---

## 5. Bubbaloop real-robot integration

**Description**
Connect the Bubbaloop learning framework to real robot hardware. Focus on hardware abstraction, safety/recovery procedures, and a minimal real-world demo that mirrors a simulation task.

**Expected Outcomes**
- Hardware integration layer with a small example robot
- Real-world demo aligned with a simulation scenario
- Documentation + setup guide

**Resources**
- Bubbaloop repository: https://github.com/kornia/bubbaloop
- kornia-rs repository: https://github.com/kornia/kornia-rs

**Possible Mentors**: Edgar Riba, Jian Shi, Christie Purackal, Miquel Farré

**Difficulty**: Medium–Hard

**Duration**: 350 hours

---

## General Evaluation Criteria

- Code quality: idiomatic Rust, clear APIs, tests, docs
- Performance: benchmarks and regression tracking where relevant
- Reproducibility: scripts, datasets, and/or instructions to validate results
- Impact: usefulness to kornia-rs users and downstream projects

## Prerequisites (Required for Consideration)

To reduce spam proposals and prioritize contributors who can execute, applicants must complete **all** of the following before submitting a final proposal:

- Join our community chat and introduce yourself
- Make at least **one small, accepted PR** to kornia-rs (or related crate)
- Share a draft proposal with a mentor for feedback
- Be able to explain the code you submitted (short interview or async review)

## Selection Process (How we evaluate)

We **select contributors, not proposals**. Proposals help shortlist, but we prioritize:
- Engagement in the community and responsiveness to feedback
- Demonstrated ability to explain code and design choices
- Evidence of learning and independent problem‑solving

## Pre-Application Work (Recommended)

- Read the application protocol and join the community channels
- Pick a project and submit a small PR to kornia-rs
- Write a short design proposal with milestones and risks
