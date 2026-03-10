# DeepChem — Project Ideas

**Source:** https://github.com/deepchem/deepchem/discussions/4703
**Scraped:** 2026-03-10T16:58:40.283038

---

-

|
We have a lot of newcomers coming onto here. Welcome to the community! I am scoping out potential projects for GSoC 2026 (remember we have to apply to get in, so no guarantee DeepChem will be selected yet). Here are some tentative project directions (I will update this forums post as we get new ideas): **Symbolic machine learning**
**Description**: We want to implement a symbolic regression capability in PyTorch that we can use in DeepChem (we prefer not to call to a Julia backend like PySR). Think of something like[https://arxiv.org/abs/2305.01582](https://arxiv.org/abs/2305.01582)except implemented in PyTorch.
**Skills Required**: PyTorch experience, some mathematical background
**Expected Outcomes**: (1) A robust implementation of a symbolic regression system using PyTorch within DeepChem, (2), Comprehensive benchmarks comparing the proposed system against standard tools like PySR, .
**Potential Mentors**: Aryan, Shreyas, Bharath
**Expected Size**: Medium
**Expected Difficulty**: Medium**MLIP support**
**Description**: Implement a MLIP model as a TorchModel in DeepChem. Make sure to leverage existing deepchem equivariance tools and not to just call out to an external framework. For reference see,[https://github.com/instadeepai/mlip](https://github.com/instadeepai/mlip), but we want to do a full implementation in pytorch
**Expected Outcomes**: (1) A robust implementation of a MLIP such as Nequip or MACE using PyTorch within DeepChem leveraging DeepChem's existing equivariant architecture, (2), Comprehensive benchmarks testing the MLIP on standard tests like force correctness or stability of small molecular dynamics simulations.
**Skills Required**: PyTorch, some mathematical background
**Potential Mentors**: Jose
**Expected Size**: Medium or Large
**Expected Difficulty**: Hard**LLM support for 7B models in DeepChem**
**Description**: Make a Olmo model in DeepChem[https://huggingface.co/allenai/OLMo-7B](https://huggingface.co/allenai/OLMo-7B)using the`HuggingFaceModel` wrapper in DeepChem. Should be able to train/run inference with Olmo. Make sure you support the ability to do generation, regression, and classification and have the ability to continue pretraining on molecular data.
**Expected Outcomes**: (1) A robust implementation of Olmo in DeepChem using the`HuggingFaceModel` wrapper. (2) Demonstration of how to do fine-tuning for classification/regression/generation and (3) the ability to perform additional pretraining on molecular datasets.
**Skills Required**: HuggingFace, PyTorch
**Potential Mentors**: Riya, Harindhar
**Expected Size**: Medium or Large
**Expected Difficulty**: Medium**Implement RFDiffusion, RFDiffusion-2**
**Description**: Implement RFDiffusion/RFDiffusion2 or other protein design models in DeepChem. Implementations should be end-to-end in PyTorch and interface with standard DeepChem abstractions such as TorchModel and DeepChem datasets
**Expected Outcomes**: (1) A clean implementation of RFDiffusion/RFDiffusion2 in DeepChem using torch model. Should leverage existing equivariance primitives. (2) Benchmarking of the model on standard protein generation tests/tasks to validate performance.
**Skills Required**: PyTorch, some background in biology and mathematics
**Potential Mentors**: Rishi, Jose, Bharath
**Expected Size**: Medium or Large
**Expected Difficulty**: Hard**Improve DFT support in DeepChem**
**Description**: DeepChem has preliminary density functional theory support ([https://arxiv.org/abs/2309.15985](https://arxiv.org/abs/2309.15985)). Build on this! Can you solve new systems, make this scale better, implement other xc-functions? Can you model more complex systems like reactions?
**Expected Outcomes**: (1) Add a new concrete functionality to DeepChem's DFT support. For example, implement a new XC-functional. You may suggest reasonable alternatives (2) Benchmark this new capability on an appropriate choice of system and validate against existing DFT tools like GPAW or PySCF.
**Skills Required**: PyTorch, some background in chemistry or quantum mechanics
**Potential Mentors**: Rakshit, Aryan, Bharath
**Expected Size**: Small, Medium, or Large
**Expected Difficulty**: Medium**Improve materials machine learning in DeepChem**
**Description**DeepChem has simple crystal graph convolutions and lattice adsorption model support from a few years ago. Test these models on real systems and improve them. We encourage you to explore generative models such as[https://arxiv.org/abs/2110.06197](https://arxiv.org/abs/2110.06197). Possibly implement new papers from the last few years such as MACE. Please make sure to do implementations in DeepChem using standard tools like TorchModel.
**Expected Outcomes**: (1) Implement a new model for materials machine learning such as MACE or Crystal Diffusion Variational Autoencoders in DeepChem using TorchModel. Please leverage DeepChem's existing equivariance utilities as needed. (2) Benchmark this system on a suitable scientific dataset.
**Skills Required**: PyTorch, some background in materials science
**Potential Mentors**: Aryan, Bharath
**Expected Size**: Medium or Large
**Expected Difficulty**: Medium**Single Cell and DNA Foundation Models**
**Description**: Implement a single cell or DNA foundation model in DeepChem. Using the existing ChemBERTa and MolFormer models as a guide. I.e, use HuggingFace as a backend, but make sure to integrate fully with DeepChem pretraining and fine-tuning infrastructure. Also need to inherit from TorchModel and DeepChem datasets
**Expected Outcomes**: (1) Implement a single cell or DNA foundation model in DeepChem leveraging`HuggingFaceModel` (2) Implement tokenizers or other needed utlities in DeepChem. (3) Benchmark this model on a suitable dataset.
**Skills Required**: HuggingFace, PyTorch
**Potential Mentors**: Rishi, Harindhar
**Expected Size**: Medium or Large
**Expected Difficulty**: Medium**Differentiable FEM, FVM**:
**Description**: Implement a differentiable finite element method or finite volume method in DeepChem. Here are couple potential references[https://arxiv.org/abs/2506.18427](https://arxiv.org/abs/2506.18427),[https://arxiv.org/abs/2307.02494](https://arxiv.org/abs/2307.02494). Make sure to benchmark against standard FEM/FVM solvers. Also make sure to use standard DeepChem abstractions such as TorchModel and deepchem datasets.
**Expected Outcomes**: (1) Implement a finite element method (or finite volume method) as a well designed utility function. This must use PyTorch and be end-to-end-differentiable (2) Provide an implementation of a mesh datastructure for use in the finite element method. (3) Run benchmarks to demonstrate differentiability.
**Skills**: PyTorch, numerical methods
**Potential Mentors**: Rakshit, Abhay
**Expected Size**: Medium or Large
**Expected Difficulty**: Hard**Robust Bi-directional Translation Between SMILES and IUPAC Nomenclature**
**Description**: Accurate conversion between systematic IUPAC names and SMILES strings is a fundamental requirement for many chemistry-AI workflows. While current state-of-the-art models like Claude show promise in understanding chemical structures, they are prohibitively expensive for processing millions of molecules in research databases. Furthermore, general-purpose models often lack the necessary precision for complex chemical structures, frequently hallucinating names or failing to correctly interpret stereochemistry and complex ring systems. This project seeks a robust and scalable solution for the bi-directional translation of these identifiers. This is an open-ended challenge where contributors are encouraged to propose and evaluate various architectures. (Potential directions include sequence-to-sequence (Seq2Seq) transformers, specialized graph-to-string architectures, or hybrid rule-based and machine learning approaches.) The primary focus is on achieving high chemical fidelity and computational efficiency compared to proprietary frontier LLM models.
**Expected Outcomes**: (1) A robust implementation of a SMILES-to-IUPAC and IUPAC-to-SMILES translation system within DeepChem, (2), Comprehensive accuracy benchmarks comparing the proposed solution against existing tools and general-purpose LLMs, (3) Support for a wide range of chemical entities, including those with complex branching and stereocenter definitions, (4) A pre-trained model or set of weights available for the DeepChem community.
**Skills Required**: Strong Python programming skills, Experience in machine learning, particularly sequence modeling or natural language processing (NLP), Knowledge of cheminformatics tools such as RDKit, OpenBabel, or PubChem APIs, Understanding of the rules governing IUPAC nomenclature and SMILES syntax.
**Difficulty**: Medium to Hard
**Potential Mentors**: Shreyas, Bharath
If you are looking to apply this year, please start scoping out these directions. The more work you do up front, the more likeley we will pick you! I will restart office hours in limited format by the start of next year once fully back from paternity leave (at least 1 day a week)
This post is mirrored on |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

## Replies: 56 comments 3 replies

-

|
Hii sir I’ve chosen to focus on two of the proposed directions: 7B LLM support in DeepChem and RFDiffusion / protein design models. I know the org selection results aren’t out yet, but I wanted to share my interest early. I’m already looking through the relevant DeepChem abstractions and the OLMo and RFDiffusion codebases so I can be ready with a concrete, well-scoped proposal if DeepChem is selected. Looking forward to contributing if things move forward. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I’m planning to explore a small DeepChem native prototype, likely starting with a minimal HuggingFace Model integration, and open an exploratory PR to get familiar with the codebase If there are any design constraints or suggested entry points you’d recommend, I’d be happy to take those into account. Looking forward to contributing and learning from the process. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I am very interested in the I am a Mechanical Engineering graduate with extensive experience in structural and thermal simulations (ANSYS/ABAQUS), which now made me curious about the formulas behind it. Now I've found myself here researching FEM formulations on DeepCharm. This fall, I will also be starting my Master's in Advanced Mechanical Engineering and Robotics in Japan (as a MEXT scholar), with a research focus on Embodied AI. I view differentiable physics as the key to bridging the sim-to-real gap, specifically for co-optimizing physical morphology alongside control policies. To understand the mathematical and software challenges involved in integrating FEM with automatic differentiation, I have built a proof-of-concept suite from scratch using PyTorch: Repository Branch --> In this repository, I implemented: - 1D Poisson Solver: Manual assembly of stiffness matrices and load vectors using the weak formulation (Galerkin method).
- Inverse Heat Conduction: A differentiable simulator that recovers thermal conductivity from noisy measurement data via gradient descent.
- 2D Differentiable Mesh: A triangular mesh generator where node coordinates are learnable parameters, optimized for element quality (aspect ratio) and area conservation.
The code includes comprehensive unit tests (pytest) and follows DeepChem's contribution guidelines (flake8/mypy). I would welcome any feedback on this implementation approach to understand how I can improve myself for the upcoming project. Best regards, |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I am deeply interested in -
Single Cell and DNA Foundation Models support in DeepChem : -
Improve materials machine learning in DeepChem
I have more than 3 years of experience in training and developing Foundational models. I would love to make this support for DNA Foundational model in DeepChem. It would very well fit into my area of expertise just applied to a new field. I have previously worked in ML Research roles at Adobe and YC startups. Also I have helped in developed foundation models in diffusion space before which have been accepted at top conferences like ICLR and WACV. Currently I also have a first author paper under review in ICML 2026. So this is something which directly falls under something I am tremendous expertise it. I will try to start with the implementation of "Crystal Diffusion Variational Autoencoders in DeepChem using TorchModel" : to see what are the technical caveats in this. Thank you |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I’m very interested in the Single Cell Foundation Models direction for GSoC 2026. I have experience working with PyTorch and transformer-based models, as well as single-cell RNA-seq data. I’ve been reviewing DeepChem’s HuggingFaceModel and TorchModel abstractions to understand how pretraining and fine-tuning workflows are structured within DeepChem. I’m particularly interested in exploring how a single-cell foundation model could be integrated cleanly using the existing HuggingFaceModel wrapper while aligning with DeepChem’s Dataset and TorchModel APIs. I plan to begin with small contributions around the HuggingFace integration to familiarize myself with DeepChem’s review and CI process before drafting a detailed proposal. Looking forward to contributing. Cheers, |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hey Regards |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi mentors , I’m Utkarsh, a student contributor interested in the LLM support for 7B models / OLMo in DeepChem GSoC 2026 project. I’ve already started contributing to DeepChem and recently opened this PR fixing HuggingFace checkpoint saving issues and HF tests: 👉 PR: I’m interested to work specifically on the OLMo + HuggingFaceModel integration project, and I’ve begun reading hf_models.py, ChemBERTa, and the TorchModel checkpoint flow to understand the current architecture. I’d really appreciate your guidance on: What would be the best first technical milestone for OLMo integration? Are there any existing design expectations or pitfalls I should be aware of? Would you recommend starting with inference support first, or classification/regression heads? |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hello mentors, I am Chiranjeevi, the project proposals seem very interesting. - Improve DFT support in DeepChem
- Improve materials machine learning in DeepChem
I have worked extensively with Graph Neural Networks (GNNs) and Physics-Informed Neural Networks (PINNs). Additionally, I currently have a paper lined up for submission to ICLR 2026, focusing on bias mitigation in vision models. Looking forward to contribute :) Best Regards, |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi Mentors, I’m really interested in the materials ML direction in DeepChem, especially the idea of implementing newer models like MACE and benchmarking them properly. The mix of geometric deep learning and real scientific datasets sounds like a great learning opportunity. I’m a second-year CSE student currently building my skills in PyTorch and ML, and I’m keen to explore how these models fit into DeepChem’s TorchModel framework. I’d love to learn how I can start contributing. Lookign forward to contributing |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I’m very interested in the “Improve DFT support in DeepChem” project for GSoC 2026. I have completed my M.Sc chemistry from NIT Trichy and worked in a computational chemistry project for one year. I am skilled in machine learning and interested to learn and make contributions in scientific ML projects. I’ve begun exploring DeepChem’s differentiable DFT code along with PySCF/GPAW implementations to understand the current gaps. I’m particularly interested in extending the DFT module with adding meta-GGA-level XC-functional. Because i have been exploring differential DFT infrastructure, noticed that while NNLDA and NNPBE are already implemented, the paper identifies meta-GGA has to implement in the future. It is essential for higher chemical accuracy because they cooperate with kinetic energy density which allow the model to distinguish between different bonding environments I have also started building small PyTorch-based experiments (toy SCF loops) to prepare for a well-scoped proposal. Looking forward to contributing and would appreciate the guidance. Best regards, |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
My name is Tanishq Jain. I’m very interested in working on the Single Cell / DNA Foundation Model project in DeepChem. I have experience in Machine Learning, Deep Learning, and working with Large Language Models. I’ve used PyTorch and HuggingFace for building and fine-tuning transformer-based models, and I’m comfortable understanding and modifying existing codebases. This project interests me because it combines transformer architectures with biological sequence modeling and requires proper integration with DeepChem’s TorchModel and dataset infrastructure. I’m particularly interested in implementing the HuggingFace-backed model, handling tokenizer utilities, and benchmarking it on relevant datasets. I’d love to get guidance on how to get started and which parts of the DeepChem codebase I should explore first. If there are beginner-friendly issues or preparatory tasks related to this project, I’m happy to start contributing right away. Thanks! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi Bharath sir, I wanted to express my strong interest in the following GSoC Project idea: I have experience in Deep Learning and LLMs, particularly with Fine-tuning (SFT) and RAG. I have worked extensively with PyTorch and HuggingFace models for building and deploying open-source models in real-world applications. You can find more details about my work on my portfolio:
- It is a Medium-length project, which gives ample time to deliver a robust and comprehensive solution.
- The intersection of AI with biology and chemistry is a fascinating and highly impactful domain.
- I have been studying Google's AlphaFold models and databases, and I am very passionate about bridging these two fields.
I would love to hear more details about this project and any recommendations on where to start! To familiarize myself with the DeepChem architecture and codebase, I have already started tackling a few open issues and successfully submitted the following PRs today: **Added**(Resolves`summary()` visualization utility for TorchModel[Summary and visualization of the PyTorch models #2820](/ideas/deepchem/deepchem-deepchem-issues-2820)): [https://github.com/[Add PyTorch Model summary utility (#2820) #4754](https://github.com/deepchem/deepchem/pull/4754)]**Fixed**(Resolves`DiskDataset.select()` IndexError on empty array selections[DiskDataset select() call assumes all data fields populated #4059](/ideas/deepchem/deepchem-deepchem-issues-4059)): [https://github.com/[Fix DiskDataset select() IndexError when y or w metadata arrays are e… #4755](https://github.com/deepchem/deepchem/pull/4755)]**Implemented Model Configuration Serialization & Loading globally**(Resolves[Feature to store and load model configurations #3176](/ideas/deepchem/deepchem-deepchem-issues-3176)): [https://github.com/[feat: Auto-capture and serialize model configurations via Model.__new… #4756](https://github.com/deepchem/deepchem/pull/4756)]
Looking forward to hearing your thoughts and contributing further! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I’m very interested in the Differentiable FEM/FVM direction. I’m particularly drawn to the challenge of implementing an end-to-end differentiable solver in PyTorch while aligning cleanly with DeepChem’s TorchModel and dataset abstractions. I’m currently reviewing literature on differentiable PDE solvers and studying how automatic differentiation interacts with stiffness matrix assembly and mesh parameterization. My background in PyTorch and numerical methods makes this direction especially aligned with my interests. I’m comfortable with linear algebra, gradient-based optimization, and implementing mathematical formulations from first principles. I also have experience building structured ML systems beyond standard training pipelines, so designing clean abstractions within an existing framework is something I value. Over the coming weeks, I plan to prototype a small differentiable Poisson solver to better understand integration and benchmarking expectations. Would you recommend starting with a minimal 1D implementation within DeepChem, or focusing first on designing a robust mesh data structure abstraction? Looking forward to contributing! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi everyone, I am new to GSOC. I still don't have a clear idea of how one is selected. Can anyone inform me on this? Do we just create a branch and show our work related to the potential idea we are interested in so that mentors know that this person knows what they are doing and can be trusted with the project, or is it entirely based on the proposal we share? |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Dear Aryan, Shreyas, and Bharath, Thank you for sharing the potential GSoC 2026 project directions and for welcoming newcomers to the DeepChem community. I’m excited to see the focus areas being outlined so early. My name is Saurabh Raj Varma, and I am currently pursuing a B.Tech from IIT (ISM) Dhanbad. I would like to express my strong interest in contributing to the I am particularly drawn to this project because it combines mathematical modeling, PyTorch-based system design, and scientific machine learning — all of which align closely with my interests and background. I have experience working with Python and PyTorch, including implementing custom neural networks, writing training loops, using autograd, and working with optimizers such as Adam. I am comfortable with linear algebra, calculus, and optimization concepts, which I understand are essential for symbolic regression systems. I have started reviewing relevant literature and exploring how symbolic regression systems represent expressions (e.g., operator trees and computational graphs). My current focus is on scoping out a small PyTorch-based prototype that can: - Represent symbolic expressions with a defined operator set (+, −, ×, ÷, sin, cos, etc.).
- Optimize constants using gradient-based methods.
- Minimize loss using standard regression objectives.
- Benchmark against existing tools like PySR on simple datasets.
I also plan to study DeepChem’s model API and contribution standards carefully to ensure any future PRs follow testing and review requirements. I fully understand and respect the AI policy and will ensure that any code submitted is clean, reviewed, and fully understood by me. I would greatly appreciate any guidance on recommended starting points or specific areas within DeepChem’s architecture that I should examine first while scoping this direction. Thank you for your time and for outlining these exciting opportunities. Best regards, |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I'm Nandini A R, and I've been working on a prototype for the Symbolic Machine Learning project. Repository: I built a symbolic regression system in pure PyTorch using genetic programming. The implementation includes: - Expression tree representation with PyTorch evaluation
- Genetic algorithm (tournament selection, mutation, crossover)
- Fitness evaluation with complexity penalties
- Comprehensive test suite with visualizations
Test results on three target functions: - Linear (y = 2x + 3): Exact match
- Quadratic (y = x²): Discovers x * x
- Sine (y = sin(x)): Discovers sin(x) directly
The system converges in about 50 generations and produces interpretable expressions. All code is tested and documented. I'd appreciate feedback on: - Is this approach aligned with DeepChem's architecture goals?
- Should I focus on integration with TorchModel or benchmarking against PySR first?
- Any specific test cases or datasets you'd recommend?
Thank you for your time. Best regards, |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Dear I am excited to share my draft proposal for Google Summer of Code 2026: My project aims to bridge the gap between discrete molecular graph representations and continuum physical laws. By integrating natively differentiable solvers into the DeepChem ecosystem, we can enable hybrid models that learn from both data and the underlying Partial Differential Equations (PDEs) of materials science, all while maintaining the computational efficiency of modern PyTorch. Key Highlights of the Proposal: - Architectural Innovation: Leveraging the Implicit Adjoint Method for
$O(1)$ memory scaling during training. - Production-Grade Stack: Targeting Python 3.10 and PyTorch 2.2.1+ with torch-sla integration for optimized sparse linear algebra.
- Physics-Grounded Models: Implementation of both FEM (for structural mechanics) and FVM (for conservative flux/diffusion) engines.
I have already begun exploring the codebase and have developed a preliminary proof-of-concept, which can be found in I would deeply appreciate any feedback or suggestions from the community to further refine this roadmap. Best regards, |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hello everyone, My name is Dnyaneshwari, and I’m currently exploring DeepChem in preparation for contributing to GSoC 2026. I’ve been reviewing the DeepChem codebase, particularly the TorchModel abstractions and the HuggingFaceModel integration, to better understand how new models are incorporated into the framework. The directions that currently interest me most are: • LLM support for 7B models in DeepChem I’m currently studying the architecture and exploring how these ideas could be implemented cleanly within DeepChem’s existing model and dataset interfaces. My plan is to start contributing to the repository while continuing to scope a well-defined proposal around one of these directions. If there are specific parts of the codebase that would be particularly useful to explore while scoping these ideas, I would appreciate any suggestions from the maintainers. Looking forward to contributing. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi The “LLM support for 7B models in DeepChem” direction looks very interesting to me. I started exploring how DeepChem integrates HuggingFace models and spent some time looking through the HuggingFaceModel wrapper to understand how tasks like classification/regression/generation are currently handled. From what I can see, extending this abstraction to support a model like OLMo-7B while keeping it compatible with DeepChem’s TorchModel interface seems like a very interesting systems problem. My plan over the next few days is to experiment with a minimal prototype that loads OLMo through the HuggingFaceModel interface and test basic inference/generation first, then explore how fine-tuning workflows could fit into the existing DeepChem training utilities. If there are particular parts of the DeepChem codebase that are especially important for this integration, I’d appreciate any pointers. Looking forward to digging deeper into this. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I’m Himangi Maurya, and I’m particularly interested in the LLM support for 7B models in DeepChem, especially integrating OLMo-7B using the HuggingFace wrapper. I’ve started exploring the codebase, looking into the HuggingFace wrapper in hf_models.py and how models are handled through TorchModel. I also tried loading OLMo through Hugging Face Transformers to understand the interface and tokenizer setup. Next, I’m planning to experiment with how OLMo could interact with the existing wrapper to understand what changes might be needed for integration. Any pointers on a good first milestone would be helpful. Looking forward to contributing.✌️ |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I’ve been benchmarking the Nucleotide Transformer 500M for the DNA Foundation Models project. I just finished a series of stress tests on the H2AFZ downstream task using custom PyTorch hooks to evaluate attention-optimization trade-offs. The Data: Relational Pruning: Entropy-based muting of confused heads yielded a +9.50% efficiency gain but triggered a -19.11% Intelligence Delta. Weighted Context Injection: By injecting a proxy 'Next of Kin' context into the latent space, I achieved a +3.39% Intelligence Delta over the baseline. My conclusion is that naive pruning is too destructive for genomic context. My GSoC proposal will focus on building a fully trained Weighted Latent Relational (WLR) Graph to intelligently route attention—preserving biological IQ while maintaining the speed gains. Dhruv |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I have experience in Deep Learning and LLMs which is evidenced by a paper I recently co-authored on: DynaStride: Dynamic Stride Windowing with MMCoT for Multi-Scene Captioning which got accepted to NeurIPS 2025 7HVU Workshop (oral) and AAAI AI4EDU Workshop, and I'm currently writing another paper relating to Multiagent deliberation on subjective questions and I'm also conducting research on interpretable ML comparing black-box models against interpretable models. Over the next couple of weeks I will continue studying the DeepChem repository and making PR's as necessary. Regards, |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I’m Advik Gupta, a 3rd year B.Tech Computer Science and Biosciences student at IIIT Delhi, and I’m really interested in the intersection of AI and drug discovery. Recently, I worked on a generative drug design pipeline in which I trained GANs to generate SMILES strings for candidate molecules and evaluated them using a protein–ligand docking workflow. The pipeline used tools such as RDKit and Open Babel for molecular processing and AutoDock Vina for docking, helping me understand the workflow from molecule generation to docking-based evaluation. I have also worked on creating biomedical knowledge graphs and training graph embeddings on them for link prediction. Because of this experience, I liked the projects I’m hoping to pursue a master’s abroad in AI for drug discovery, so being able to learn from and contribute to open-source work in this space through DeepChem would be really exciting for me. Looking forward to learning from the community here and getting involved! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
looks like there are lot of people cool |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
I’m Raghunandan, a 3rd year B.Tech Computer Science Student, I am very much interested to work on interjection of AI and drugs , |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Dependencies: Add ai2-olmo as an optional dependency so we can load OLMoForCausalLM and its tokenizer smoothly. The Wrapper: Extend HuggingFaceModel to map our standard DeepChem tasks (generation, classification, regression) directly to the right OLMo architectural heads. Memory Management: Since 7B is heavy on VRAM, I want to weave in bitsandbytes (4-bit/8-bit quantization) right into the initialization. I'd also like to set up FSDP and QLoRA hooks so folks can actually fine-tune this on consumer GPUs. Validation: Finally, I'll connect the SMILES datasets to the tokenizer and write some benchmarking scripts to demonstrate continual pretraining and supervised fine-tuning on MoleculeNet. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I'm Andrii, Master Student in Data Engineering, and I'm very interested to work on MLIP support! I'll be working on the proposal for the Google Summer of Code 2026 over the next week, analyzing your repository and trying to create some PR's. Looking forward to contributing to DeepChem! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi mentor, |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)
