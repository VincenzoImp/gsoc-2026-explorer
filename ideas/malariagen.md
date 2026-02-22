# MalariaGEN — Project Ideas

**Source:** https://docs.google.com/document/d/178LEZEsC0xbknHDId83k5XzIDRtnyVw243Ta0fhlvPM/edit?tab=t.0
**Scraped:** 2026-02-22T23:28:47.598069

---

Main website: [https://summerofcode.withgoogle.com/](https://www.google.com/url?q=https://summerofcode.withgoogle.com/&sa=D&source=editors&ust=1771801764242197&usg=AOvVaw2DDwHovWDArbmkOQs7Tn6e)

Terms and conditions:

Rules: [https://summerofcode.withgoogle.com/rules](https://www.google.com/url?q=https://summerofcode.withgoogle.com/rules&sa=D&source=editors&ust=1771801764242425&usg=AOvVaw0qZYzfscqeNNphMSStC9Ui)

For organisations: [https://summerofcode.withgoogle.com/terms/org](https://www.google.com/url?q=https://summerofcode.withgoogle.com/terms/org&sa=D&source=editors&ust=1771801764242581&usg=AOvVaw33VnUjUDDZBwUbomeTJR5q)

For participants: [https://summerofcode.withgoogle.com/terms/member](https://www.google.com/url?q=https://summerofcode.withgoogle.com/terms/member&sa=D&source=editors&ust=1771801764242791&usg=AOvVaw21n8KXIhNcCoIj4FbZLRNP)

Timeline: [https://developers.google.com/open-source/gsoc/timeline](https://www.google.com/url?q=https://developers.google.com/open-source/gsoc/timeline&sa=D&source=editors&ust=1771801764242972&usg=AOvVaw3Fn6u-YvOKOpssyJH8oEKc)

Contributor guides: [https://google.github.io/gsocguides/student/](https://www.google.com/url?q=https://google.github.io/gsocguides/student/&sa=D&source=editors&ust=1771801764243138&usg=AOvVaw33XtdApOR6phIwpBRIEH14)

—

Hi, thanks for your interest in working together on this year's GSoC! We encourage you to browse through the project ideas below and explore the linked resources to get a sense of what we do and some of the ideas we hope to develop together this summer. The main place to learn about the MalariaGEN Vector Observatory is our website: [https://www.malariagen.net/vobs](https://www.google.com/url?q=https://www.malariagen.net/vobs&sa=D&source=editors&ust=1771801764243825&usg=AOvVaw3vIDKnNQu2fUZ4__ajMVjZ) which links all the resources that we have developed to access and analyse mosquito data – we encourage you to browse through our training resources as we have helpful documentation and additional details about the challenges that are important to our community, built around data sharing and lowering the barrier to technical analysis and use of genomic data relevant to reduce the burden of infectious diseases globally.

If you are interested in developing a proposal for any of the ideas below, we encourage you to look through our repository: [https://github.com/malariagen/malariagen-data-python](https://www.google.com/url?q=https://github.com/malariagen/malariagen-data-python&sa=D&source=editors&ust=1771801764244483&usg=AOvVaw3Ga1BVNoT8W-C4Px-2ztpD) which allows to access and analyse genomic data without the need to download locally or for dedicated compute resources, both of which are major barriers for analysts in malaria endemic settings. We ask you to browse through the code, and current open issues to familiarise yourself with the technical challenges within the package. To ensure you have a sense of our architecture, we ask for potential GSoC contributors to contribute to the package via a PR, this can be around anything that seems of value to you within the current architecture, on existing or newly identified issues and ideas.

After you have contributed and started developing your idea on how you would like to tackle the project of your choice, please do get in touch via [support@malariagen.net](mailto:support@malariagen.net) (please include GSoC26 on the header of your email, your GitHub username with URL to the PR/PRs you have contributed, which project you are interested in and a skeleton of ideas/proposed approaches you have for this project), we will then put you in contact with one of the mentors who will be on hand to comment on your ideas and answer questions while you develop your proposal.

—

Mentors | Tristan Dennis, Anastasia Hernandez-Koutoucheva, Jon Brenas |
Size | Large (350 hours) |
Difficulty | Hard |
Technologies | Python, Statistical Analysis, Google Cloud Storage |


The Malaria Vector Genome Observatory is an open and collaborative ecosystem that supports researchers and public health authorities to access, analyse and visualise data from Anopheles mosquitoes collected from countries affected by malaria. Integrating high-quality whole-genome sequence data from over 25,000 mosquitoes contributed by partners across 30 countries, this resource represents the largest natural genetic variation dataset for any multicellular organism, second only to humans.

At the core of this resource, is the malariagen_data API – a cloud-native, open-source Python software package that enables scalable population genomics and genomic surveillance by providing robust statistical and visualisation tools designed for rapid and reproducible analysis.

Tools on the API are centered on mosquito species native to Africa, where the burden is highest. Recent sequencing efforts have generated valuable genomic data for An. farauti, a key vector responsible for transmission in the Pacific, but the absence of standardised, open, and user-friendly analytical tools has slowed their uptake into comparative research.

For this project, we are looking for contributors who have an interest in expanding and enhancing this ecosystem to develop open-source, cloud-native functions that allow for analysis on this species, building on design principles proven in African vector genomics resources. This will include developing analysis functions and well-documented functionality into the API, and enable interoperability with existing resources.


Further reading:

- Source code:
[https://github.com/malariagen/malariagen-data-python](https://www.google.com/url?q=https://github.com/malariagen/malariagen-data-python&sa=D&source=editors&ust=1771801764249148&usg=AOvVaw2k3yQce4yL5pnSpQX4c4hN) - Malaria Vector Genome Observatory:
[https://www.malariagen.net/vobs](https://www.google.com/url?q=https://www.malariagen.net/vobs&sa=D&source=editors&ust=1771801764249317&usg=AOvVaw0CeU_kwUx7ozdobdRkROBk) - Training course showcasing data analysis with the malariagen_data API:
[https://anopheles-genomic-surveillance.github.io/home.html](https://www.google.com/url?q=https://anopheles-genomic-surveillance.github.io/home.html&sa=D&source=editors&ust=1771801764249546&usg=AOvVaw1xJy3rwwdm_-wqLOLi1hsN)

Mentors | Jon Brenas, Tristan Dennis |
Size | Medium (175 hours) |
Difficulty | Medium |
Technologies | Python, Machine-learning, Google Cloud Storage |

Identifying Anopheles mosquitoes species with precision is critical for malaria control. Taxonomic identification of Anopheles mosquitoes is challenging as they are morphologically identical, and genomic data is key to correctly classify individuals. Misclassification can lead to suboptimal interventions and flawed epidemiological insights, underscoring the need for robust, scalable and accessible classification frameworks.

Accurate taxonomic identification underpins all genomic analyses of malaria vectors. Current classification tools for Anopheles mosquitoes typically rely on genotype calls derived from variant calling pipelines. While effective, this approach introduces computational overhead and complexity, and can be fragile when reference panels or species definitions evolve. In many settings, researchers have access only to raw sequencing reads (FASTQ files). There is a strong need for a lightweight, robust method that can assign samples to the appropriate taxonomic resource without requiring full genotyping or complex species splitting.

This project aims to develop a FASTQ-based taxon identification tool that operates directly on raw sequencing reads to guide users to the most appropriate downstream genomic resource. Rather than resolving fine-scale species complexes (e.g. An. coluzzii), the tool will focus on reliably assigning samples to the correct major taxonomic group or reference framework, such as An. gambiae, An. funestus, or An. stephensi.

Further reading:

- Source code:
[https://github.com/malariagen/malariagen-data-python](https://www.google.com/url?q=https://github.com/malariagen/malariagen-data-python&sa=D&source=editors&ust=1771801764252727&usg=AOvVaw2nY2Pg9vOV8mvP1NxhJOrh) - Malaria Genome Vector Observatory:
[https://www.malariagen.net/vobs](https://www.google.com/url?q=https://www.malariagen.net/vobs&sa=D&source=editors&ust=1771801764252898&usg=AOvVaw1UhhpiSHN9J32NMlyU0Itk)

Mentors | Jon Brenas, Chris Clarkson, Anastasia Hernandez-Koutoucheva |
Size | Medium (175 hours) |
Difficulty | Medium |
Technologies | Python, AI, NLP/LLMs, Google Cloud Storage |

Large-scale genomic resources for malaria mosquitoes like the MalariaGEN Vector Observatory exist, but their effective use often requires a degree of programming expertise and knowledge of data structures, APIs, and population genetics concepts. This creates a barrier for many potential users, including entomologists, public health practitioners, and decision-makers who could benefit from genomic insights fast, without the need of accessing dedicated training.

Advances in natural-language processing (NLP), ontologies, and large language models (LLMs) offer a unique opportunity to rethink how users interact with genomic surveillance data.

This project aims to develop an intuitive, natural-language interface for querying malaria vector genomic data with little or no programming knowledge. The tool will allow users to express questions in plain language and translate them into executable queries against the malariagen_data API – a cloud-native, open-source Python software package that enables scalable population genomics and genomic surveillance by providing robust statistical and visualisation tools designed for rapid and reproducible analysis.

Further reading:

- Source code:
[https://github.com/malariagen/malariagen-data-python](https://www.google.com/url?q=https://github.com/malariagen/malariagen-data-python&sa=D&source=editors&ust=1771801764255813&usg=AOvVaw2B5JHuhzLZo7lVNl-qS-dS) - Malaria Genome Vector Observatory:
[https://www.malariagen.net/vobs](https://www.google.com/url?q=https://www.malariagen.net/vobs&sa=D&source=editors&ust=1771801764255977&usg=AOvVaw3mEzsAo8ha1fV8R3wfc3Ae)
