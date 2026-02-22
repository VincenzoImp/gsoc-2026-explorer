# DeepChem — Project Ideas

**Source:** https://github.com/deepchem/deepchem/discussions/4703
**Scraped:** 2026-02-22T23:28:47.606422

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

## Replies: 25 comments 1 reply

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
Hi I’m very interested in the “Improve DFT support in DeepChem” project for GSoC 2026. I have completed my M.Sc chemistry from NIT Trichy and worked in a computational chemistry project for one year. I am skilled in machine learning and interested to learn and make contributions in scientific ML projects. I’ve begun exploring DeepChem’s differentiable DFT code along with PySCF/GPAW implementations to understand the current gaps. I’m particularly interested in extending the DFT module with a new XC-functional or improving SCF stability and scaling, followed by benchmarking against standard DFT tools. I have also started building small PyTorch-based experiments (toy SCF loops, basic LDA/GGA tests) to prepare for a well-scoped proposal if the org is selected. Looking forward to contributing and would appreciate any guidance on which direction would add the most value. Best regards, |

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
Hi I have been working on generative models for materials closed-loop discovery for my MS thesis at CMU. I have worked on generative models like TransPolymer and finetuning of MoleculeChef. I am well aware of the databases required and have also created a 1.6M labeled synthetic Rdkit fingerprint database for polymers (for reference - I had also contributed to the open source repo of DeepChem this january for including SAscore metrics that I had found that could potentially be included in the repo. Best , |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I’m Sakshi, a GSSoC’25 contributor with experience in PyTorch and HuggingFace-based ML systems. I’m particularly interested in the LLM support for 7B models (OLMo) direction for GSoC 2026. I’ve started reviewing DeepChem’s HuggingFaceModel, TorchModel, and existing ChemBERTa integrations to understand how generation, classification, and checkpointing are handled. As a next step, I plan to explore a small contribution around HF model integration or inference/generation support to get familiar with DeepChem’s CI and review process. I’d appreciate any guidance on whether starting with inference + generation support would be the preferred first milestone, or if there are other entry points you’d recommend. Looking forward to contributing. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi sir This is Rishi. I am currently in my second year of my bachelor’s degree. I have gone through the list of projects, and as a science student up until 12th grade, I found all of them interesting. However, I am particularly drawn to the following three: - Implementing RFDiffusion and RFDiffusion2
- Single-cell and DNA foundation models
- Robust Bi-Directional Translation between SMILES and IUPAC nomenclature
With a strong background in chemistry and biology, along with a deep interest in PyTorch and hands-on experience in deep learning especially CNNs I would be excited to work on any of the above projects. Since I can apply for only one project, I would prefer to focus on <- Robust Bi-Directional Translation between SMILES and IUPAC nomenclature ->. One reason this project resonates with me is that it reminds me of solving IUPAC nomenclature exercises from practice books like MS Chouhan and Himanshu Pandey during my 11th and 12th grades. It’s amusing to reflect on that experience now, but it genuinely sparked my interest in this area. Working on this project would allow me to fulfill my goal of integrating technology with chemistry and biology. I would love to hear more details about this project and any suggestions on where to begin or what resources I should study. In the meantime, I will continue exploring relevant concepts. I would be grateful for your guidance if possible sir. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
I am Arnab, a computer science student. I contribute to open source projects. The project that really catches my attention is the "Robust Bi-directional Translation Between SMILES and IUPAC Nomenclature" project for GSoC 2026. My background is in natural language processing, data structures, algorithms and Python. I have also used artificial intelligence models with TensorFlow and Keras. After reading about the project, I think we can use a kind of vocabulary for chemical structures and a custom sequence to sequence transformer to solve the problems with large language models that you talked about. Now I am setting up my DeepChem environment and looking for a simple issue to start with so I can get used to your testing process. Before I make a plan for the project, I wanted to ask if I should start by making a custom tokenizer for SMILES and IUPAC or if I should first work on putting a basic sequence to sequence model into the TorchModel framework. Looking forward to contributing and working with you! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
I am Shreya Gupta, a recent Chemical Engineering graduate from IIT BHU, with proficiency in Python, Machine Learning, Deep Learning, and NLP. I am very interested in contributing to the project "Robust Bi-directional Translation Between SMILES and IUPAC Nomenclature." During my academic years, I studied Computational Drug Design and am very familiar with the relevant concepts. I have also built LLM-based and encoder-decoder models, and I believe this project aligns strongly with my skill set at the intersection of Chemistry and AI. I have already started exploring potential approaches for this project and would greatly appreciate your guidance. I am excited about the opportunity to contribute and learn. Thanks. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
I'm Jyotiraditya Kuanar, a CS graduate now working in interdisclipinary(Chem+CS) research for my MSc. I’ve been going through the proposed GSoC ideas and I’m genuinely excited about the direction DeepChem is heading, especially around LLM integration and sequence-based modeling tasks like SMILES ↔ IUPAC translation. I’ll be upfront — I’m still in the process of building deeper hands-on experience with PyTorch. I’ve worked with ML before, but I’m currently focusing on strengthening my fundamentals in Torch and HuggingFace workflows. DeepChem feels like the right kind of challenge to push myself technically while contributing something meaningful. Over the next few weeks, I plan to set up the development environment, study how TorchModel and HuggingFaceModel are structured, and try reproducing some existing training workflows end-to-end. I’d also love to start with smaller contributions to understand the codebase properly before drafting any proposal. If there are recommended entry points or beginner-friendly issues for someone ramping up in PyTorch but committed to putting in serious effort, I’d really appreciate the guidance. Looking forward to learning and contributing. Thanks for maintaining such a thoughtful and technically ambitious project! With Regards, |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I am specifically targeting the Single Cell and DNA Foundation Models (Large) project. Given my biotech background, I’m particularly interested in how we can optimize tokenization for non-coding regions and long-range genomic dependencies. I’ve been analyzing the HuggingFaceModel wrapper in DeepChem and would love to propose a benchmark comparing HyenaDNA and Nucleotide Transformer within the DeepChem fine-tuning pipeline. I will be sharing a small exploratory PoC soon! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi everyone, I'm Sakshi, currently pursuing MCA (AI & DS). I’m interested in contributing to DeepChem for GSoC 2026. I’m currently exploring open issues and would like to start contributing. Looking forward to contributing! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi I'm Selcuk Senturk, MSc Computer Science student and an AI/ML Engineer at IBM Expert Labs. I'm interested in contributing to DeepChem as part of
Of the two, I'd lean toward whichever has more open scope for a 175-hour contribution, happy to discuss either direction. A few questions: - For symbolic ML, is the expectation a from-scratch PyTorch implementation or wrapping an existing differentiable symbolic framework?
- For materials ML, is MACE the preferred target model, or is there flexibility based on what's most useful to DeepChem currently?
I would like to discuss further if I'm a good candidate for these projects and how I plan to implement these above. Resume: [ |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi everyone! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)
