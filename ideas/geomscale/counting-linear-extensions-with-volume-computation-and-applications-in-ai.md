# Counting linear extensions with volume computation and applications in AI

**Parent:** GeomScale — Project Ideas
**Source:** https://github.com/GeomScale/gsoc26/wiki/Counting-linear-extensions-with-volume-computation-and-applications-in-AI
**Scraped:** 2026-02-22T23:28:47.592881

---

## Background  

The problem of counting the linear extensions of a given partial order
consists in finding (counting) all the possible ways that we can extend
the partial order to a total order that preserves the original partial order.
It is an important problem with various applications in Artificial Intelligence
and Machine Learning, for example in partial-order plans [1] and
in learning graphical models [2]. It is a well known #P-complete problem;
the fastest known algorithms are based on dynamic programming and require 
exponential time and space [4, 5]. Nevertheless, if we only need an approximate
counting attained with a probability of success, then the problem admits
a polynomial-time solution for all posets using Markov Chain Monte Carlo 
(MCMC) methods. During this project, the student will implement a new randomized
method to approximate the number of linear extensions based on volume approximation.


## Related work

There are several MCMC schemes that have been proposed [3, 6]. The latter
improvements were based on rapidly mixing Markov chains in the set of linear
extensions [7]. In practice, approximate counting is feasible on partially
ordered sets up to a few hundred elements in a few hours [6]. It is well known
[8] that we can represent a partial order with a convex polyhedron, namely
order polytope. Furthermore, the number of linear extensions is equal to the
volume of the order polytope. However, there is no algorithm that counts
linear extensions through volume calculations of order polytopes. 
However, there are a few practical algorithms for estimating the volume of a 
convex polytope; `volesti` provides the most efficient implementations. 


## Details of your coding project  

The goal of the project is to implement a new approximation algorithm
for counting linear extensions through volume approximation and an extensive
empirical comparison including existing approximation methods. The aim is
to exploit the structure of order polytopes to improve `volesti`'s implementations
for volume approximation by developing new efficient software implementations,
based on the `volesti` C++ library. In particular, the student will employ the existing
implementations of `volesti` (i) for reading and building an order polytope given the partially 
ordered set, (ii) of the C++ class that represents an order polytope, and (iii) the optimized implementations
for the membership and boundary oracles of the order polytope.

Next, the student will have to implement optimized boundary oracles for the exact Hamiltonian Monte Carlo
with Gaussian target distribution with a general mass matrix to generate the momenta in each step.
A new C++ structure for this walk will have to be implemented. The student will integrate the
new optimized implementations into existing implementations of volume estimation
algorithms and (e) perform an extended empirical comparison of all approximation counting methods.

Difficulty: Hard

## Size 
Large (350 hours)  

## Skills 

* Required: C++, linear algebra, probability theory
* Preferred: Experience with mathematical software, combinatorics and convex geometry is a plus



## Expected impact  

The impact of this project will be undoubted important in several applications
in Artificial Intelligence and Machine Learning.

## References
[1] Muise, C. and Beck, J. and McIlraith, S., Optimal Partial-Order Plan Relaxation via MaxSAT, Journal of Artificial Intelligence Research, 2016

[2] T. Niinimaki and P. Parviainen and M. Koivisto, Structure Discovery in Bayesian Networks by Sampling Partial Orders, Journal of Machine Learning Research, 2016

[3] Brightwell, G. and Winkler, P., Counting linear extensions, Order, 1991

[4] De Loof, K.; De Meyer, H.; and De Baets, B., Exploiting the lattice of ideals representation of a poset, Fundamenta Informaticae, 2006

[5] Kangas, K.; Hankala, T.; Niinimaki, T.; and Koivisto, M., Counting linear extensions of sparse posets, In Proceedings of the 25th International Joint Conference on Artificial Intelligence, 2016 

[6] T. Talvitie and K. Kangas and T. Niinimaki and M. Koivisto, Counting Linear Extensions in Practice: MCMC versus Exponential Monte Carlo, Thirty-Second AAAI Conference on Artificial Intelligence, 2018

[7] Karzanov, A., and Khachiyan, L., 1. On the conductance of order Markov chains, Order, 1991

[8] Stanley, Richard P., Two Poset Polytopes, Discrete & Computational Geometry, 1986

[9] Matias von Bell, Benjamin Braun, Derek Hanely, Khrystyna Serhiyenko, Julianne Vega, Andrés R. Vindas-Meléndez, Martha Yip, [Triangulations, order polytopes, and generalized snake posets](https://arxiv.org/pdf/2102.11306.pdf), preprint, 2021.

[10] Augustin Chevallier, Sylvain Pion, Frédéric Cazals, [Hamiltonian Monte Carlo with boundary reflections, and application to polytope volume calculations](https://hal.archives-ouvertes.fr/hal-01919855v2/document).  

[11] Ari Pakman, Liam Paninski, [Exact Hamiltonian Monte Carlo for Truncated Multivariate Gaussians](https://arxiv.org/abs/1208.4118).

[12] Topi Talvitie, Mikko Koivisto, [Approximate Counting of Linear Extensions in Practice](https://www.jair.org/index.php/jair/article/view/16374)
## Mentors

- [Vissarion Fisikopoulos](https://vissarion.github.io) <vissarion.fisikopoulos at gmail.com> is an international expert in mathematical software, computational geometry, and optimization, and has previous GSOC mentoring experience with Boost C++ libraries (2016-2020) and the R-project (2017-2019).

- [Elias Tsigaridas](https://www-polsys.lip6.fr/~elias) <elias.tsigaridas at inria.fr> is an expert in computational nonlinear algebra and geometry with experience in mathematical software. He has contributed to the implementation, in C and C++, of several solving algorithms for various open source computer algebra libraries and has previous GSOC mentoring experience with the R-project (2019) and Geomscale (2020).

- [Matias Bender](http://page.math.tu-berlin.de/~mbender/) <matibender at gmail.com> holds a Ph.D. in algebraic algorithms and he is an expert in computational algebra.  

## Tests

- Easy: Download, compile and run a simple volume estimation example with both C++ and R interfaces of volesti.  
- Medium: Reproduce this [issue](https://github.com/GeomScale/volesti/issues/179) and comment on possible explanations and solutions.  
- Hard: Write in your proposal how the implementation of the exact Hamiltonian Monte Carlo with Gaussian target distribution in [10, 11] can be optimized for an order polytope.
