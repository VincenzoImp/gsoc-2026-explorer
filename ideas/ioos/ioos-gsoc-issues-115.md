# #115

**Parent:** IOOS — Project Ideas
**Source:** https://github.com/ioos/gsoc/issues/115
**Scraped:** 2026-02-22T23:28:47.603444

---

## [GSoC Project Proposal]: Develop a universal installer for National Stock Assessment Program (NSAP) packages

**Labels:** project idea, GSoC26

### Project Description

Scientific software often depends on a complex mix of system tools, compilers, and R packages, making setup difficult and error-prone. This project will build a universal installer that provides simple “one-command” setups (e.g., bash scripts) for National Stock Assessment Program projects such as Stock Assessment Workflows and the Fisheries Integrated Modeling System (FIMS), etc. The installer will handle system detection, dependency installation, and R package management across Windows/WSL2, macOS, and Linux, while ensuring projects do not break each other. An automated testing suite in GitHub Actions will verify the installer on clean system images.

### Expected Outcomes

The project will deliver a set of bash scripts or other recommended tools for setting up supported NSAP R packages. 

- The system will detect existing tools, installing or updating only what is necessary, with version-controlled dependency packages. 
- A robust R library management approach using `.libPaths` will keep project-specific packages in separate directories, avoiding version conflicts and ensuring reproducibility. 
- To ensure reliability, a GitHub Actions workflow will test installations on Windows, macOS, and Linux, while the same scripts will also be verified on Google Cloud Workstations.

Overall, these improvements will streamline setup, reduce errors, and make NSAP R packages easier to maintain and install.


### Skills Required

shell scripting (e.g., Bash), R environment management, and cross-platform testing

### Expected Project Size

175 hours

### Project Difficulty

Intermediate

### Mentor Name(s)

Bai Li, Elizabeth Perl

### Mentor GitHub Handle(s)

@Bai-Li-NOAA, @e-perl-NOAA

### Mentor Contact Email(s)

bai.li@noaa.gov, elizabeth.gugliotti@noaa.gov

### Contributor Evaluation/GSoC GitHub Issue Links


There are several existing [issues in the FIMS repository](https://github.com/NOAA-FIMS/FIMS/issues) that are labeled "good first issue" or "low-hanging fruit" that could be worked on.

[Good First Issue](https://github.com/NOAA-FIMS/FIMS/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22)
[Low-hanging 🍎](https://github.com/NOAA-FIMS/FIMS/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22attribute%3A%20low%20hanging%20%F0%9F%8D%8E%22)



### Additional Project Background/Links

We have an existing [bash script](https://github.com/NOAA-FIMS/FIMS/blob/main/setup_fims.sh) for setting up FIMS, which can serve as a starting point for developing a more robust version. The setup guide is available [here](https://noaa-fims.github.io/FIMS/articles/fims-user-setup-guide.html). Our goal is to update the current FIMS script to meet the expected outcomes outlined above and to develop similar scripts for other NSAP projects, such as [{asar}](https://github.com/nmfs-ost/asar) and [{stockplotr}](https://github.com/nmfs-ost/stockplotr/). Discussions about issues with the existing FIMS script can be found [here](https://github.com/orgs/NOAA-FIMS/discussions/1073).

Related to https://github.com/NOAA-FIMS/FIMS/issues/1169

### Previous Project Idea Link(s)

_No response_

