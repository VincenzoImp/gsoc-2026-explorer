# `pyGAM` project ideas 2026

**Parent:** German Center for Open Source AI — Project Ideas
**Source:** https://github.com/gc-os-ai/mentoring-projects/blob/main/2026/pyGAM.md
**Scraped:** 2026-02-22T23:28:47.617929

---

We propose the following lines of work which we believe would represent a significant improvement in the quality of the library while being feasible within a focused period of work (~3 months).

# 1. Implement a modern p-value computation. 
The library is in need of more reliable p-values. We receive many citations from academics in social and earth sciences, and from reading their work it is clear that hypothesis testing is important to them. The current calculation in pyGAM uses an outdated approximation from Wood 2006 that is known to reject the null hypothesis too eagerly. Luckily Wood 2014 contains improved p-value calculations which are the standard in MGCV.    
  - Expected Outcomes: Read and understand the reference text to undertstand improved p-value calculation. Implement modernised statistical calculations in GAM._compute_p_values(). Implement unit tests that compare to theoretical performance from references eg Wood 2014 using simple datasets.   
  - Skills required/preferred: software development, scientific computing, unit testing, python, numpy, pytest, statistics  
  - Time estimate: 350 hours  
  - Difficulty: Medium  
  - https://github.com/dswah/pyGAM/issues/163  
  - Mentor: Daniel Servén [dswah](https://github.com/dswah/mentoring-projects/new/main/2026#:~:text=Skip%20to%20content-,dswah,-mentoring%2Dprojects)   


# 2. Scikit-Learn Interface. 
We seek to integrate pyGAM smoothly into the python ML ecosystem. However, our library has become out of sync with the modernisations in sklearn. We propose to improve pyGAM's base models and model methods (fit, predict) by allowing them to work smoothly as sklearn estimators.    
  - Expected Outcomes: Reading scikit-learn documentation to understand API requirements, improvements to main pygam class definitions, inits and methods to ensure compatilibility with main scikit-learn API. Implementation of unit tests for these changes, 
  - Skills required/preferred: software development, unit testing, python, numpy, pytest, object oriented programming  
  - Time estimate: 175 hours  
  - Difficulty: Medium  
  - https://github.com/dswah/pyGAM/issues/422  
  - Mentor: Daniel Servén [dswah](https://github.com/dswah/mentoring-projects/new/main/2026#:~:text=Skip%20to%20content-,dswah,-mentoring%2Dprojects)


# 3. Centered Feature Functions.
pyGAM is currently missing a key element of statistical rigor, which is to reduce model identifiability issues by enforcing that all spline-based feature functions sum to unity over the data distribution. This should improve numerical stability during estimation by avoiding colinearity of the intercept with multiple feature functions.
   - Expected Outcomes: Read and understand the reference text to undertstand the underlying mathemicatics. Implement a main feature-centering method in the base Term class of pygam.termns.py and modifications of this method for specific terms. Implement unit tests with simple datasets to confirm correct implementation and to rule out numerical problems.  
  - Skills required/preferred: software development, scientific computing, unit testing, python, numpy, pytest  
  - Time estimate: 350 hours  
  - Difficulty: Medium   
  - https://github.com/dswah/pyGAM/issues/24
  - Mentor: Daniel Servén [dswah](https://github.com/dswah/mentoring-projects/new/main/2026#:~:text=Skip%20to%20content-,dswah,-mentoring%2Dprojects)
