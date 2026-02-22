# GSoC 2012 Aleksandar Makelov: Computational Group Theory

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/wiki/GSoC-2012-Report-Aleksandar-Makelov:-Computational-Group-Theory
**Scraped:** 2026-02-22T23:28:47.571365

---

Hi, I'm Aleksandar Makelov, and this page is a report on my work for sympy under the Google Summer of Code 2012.

# About me

I'm a student at Harvard College; I'm primarily interested in mathematics, computer science and physics, and will probably concentrate in mathematics with a secondary in CS. Here's my [blog](https://github.com/sympy/sympy/wiki/amakelov.wordpress.com) that I started because of GSoC but plan to expand with other topics. 

# Before GSoC

I was introduced to the GSoC program and to sympy by a friend, Stefan Krastanov (he also participated in GSoC 2012 as a student). I was pleasantly surprised that a sophisticated computer algebra system such as sympy is open-source and everyone can contribute to it. I picked the topic of computational group theory almost by accident - I have always liked combinatorics and group theory just seemed like a nice way to go. Moreover, I spotted a flaw in the combinatorics module, in the function used to generate all permutations in the usual permutation representation of the dihedral group. Then I got a copy of the "Handbook of computational group theory" (D. Holt) and "Permutation Group Algorithms" (A. Seress) and saw that there was enough material in it for a whole summer of coding. I discussed some ideas with people on the mailing list and prepared a proposal based on the two books (mostly on the "Handbook..."). Now that the summer is over and I've tackled a lot more with computational group theory, it seems that the main points in the proposal were:
* Basic algorithms for permutation groups: orbits, stabilizers, random elements, normal closure, ...
* Algorithms used to find a base and strong generating set for a given permutation group (these can then be used to answer many questions about the group) - basically, the deterministic and randomized versions of the Schreier-Sims algorithm
* Some applications of bases and strong generating sets - mainly backtrack searching for finding subgroups with given properties.
* The Todd-Coxeter algorithm for coset enumeration, used to find the index of a subgroup of a finitely presented group.
* Facilities for generating some well-known (families of) groups easily.
* Handling character tables and group representations.

# During GSoC

Things somewhat deviated from the proposal I had set for myself. To start with, there was already some work on permutation groups done thanks to a previous GSoC student (Saptarshi Mandal). Moreover, there was an implementation of the deterministic Schreier-Sims algorithm using a modification called "Jerrum's filter" (thanks to Mario Pernici). A more detailed account of my progress can be found on my blog [here](http://amakelov.wordpress.com/category/google-summer-of-code-2012/)

* Anyway, the first bullet point in the above list went smoothly - it was sort of split in two parts, one in the beginning of my project and the other in the end (the second one was normal closure and some applications such as derived series and lower central series).

* The second bullet point was delayed for a while since there was a working implementation of the Schreier-Sims algorithm already, and whenever I needed a base and strong generating set I referred to it. However, it turned out that for one of my functions (see subgroup_search() below) I needed the so-called "incremental" Schreier-Sims algorithm that takes a sequence of points and a generating set for a permutation group, and extends the sequence to a base and the generating set to a strong generating set relative to it. This is said to be of higher time complexity than the one using Jerrum's filter, but the implementation I did, surprisingly, seems to be of lower time complexity. This might be fixed in the future by a modified version of Jerrum's filter, that's why I left the old algorithm as it is. I also implemented the randomized Schreier-Sims algorithm, however there is currently no algorithm available to quickly verify the result, and it is not yet used anywhere in the combinatorics module. The reason is that verification algorithms rely on group presentations, a topic I didn't have enough time for.

* The heart of the third bullet point was the function subgroup_search(). It is the most complicated single thing that I have written for the GSoC (it's about 200 lines of code) and I spent a long time debugging it, but it now seems to give the right results. On the other hand, it is the most interesting single thing I have written for the GSoC since it can do many different things - just look it up in the docs! It can be used to write algorithms that find centralizers (this was implemented), normalizers, coset representatives, ...; moreover, backtracking is the fastest known (currently) method for carrying out these computations!

* For the fourth bullet point, I couldn't find enough time. Nothing on finitely presented groups was implemented.

* For the fifth bullet point, I wrote functions that produce (the usual) permutation representations for the symmetric, alternating, dihedral and cyclic groups, and a function to construct a permutation representation of an abelian group with a given cyclic decomposition. No database of groups was added to sympy, unfortunately.

* For the sixth bullet point, nothing was done - there's no algorithm implemented to find the conjugacy classes of a permutation group currently; without this, the manipulation of character tables becomes tedious.

# After GSoC

There is still much to be done in the combinatorics module. As during the program my efforts were directed mainly towards getting the fundamental algorithms of computational group theory in, the overall structure of the module hasn't received much attention. The algorithms are in, but sympy/combinatorics/perm_groups.py is a bit of a mess. There are a lot of new files though, and the code organization is not terrible, I think. Some suggestions (both for me and anyone else interested) for future work are:
* Add more information for symmetric/dihedral/alternating/cyclic groups in sympy/combinatorics/named_groups.py - details such as primitivity, solvability, nilpotency, and precomputed bases/strong generating sets
* Integrate the incremental Schreier-Sims algorithm with the fields of the PermutationGroup class in sympy/combinatorics/perm_groups.py so that it is the default version used (since it is currently faster than the one being used), OR
* Improve/reimplement the Schreier-Sims algorithm using Jerrum's filter and make it the default version being used for finding a base and strong generating set from scratch.
* Remove singleton cycles from the cyclic from in sympy/combinatorics/permutations.py. I was working on this during the last couple of days of my GSoC, but now there are other changes to how permutations work that are being discussed, so I'm waiting to see where this goes.
* Implement subgroup intersection as described in the "Handbook of computational group theory" - this is really easy now that we have subgroup_search()
* Write some more comprehensive tests for everything in sympy/combinatorics/perm_groups.py (currently, we have comprehensive tests for several of the more sophisticated functions)
* Take some of the functionality in sympy/combinatorics/perm_groups.py out (i.e., out of the PermutationGroup class) and put it in other files.

# Conclusion

I'd say I did about 75% of the work I had promised to do in my proposal. It's not a disaster, but it's not very nice too, and I hope to get back to this at some point in the future (probably not during term time since I tend to be very busy with courses and stuff). I greatly appreciate the help of my mentor, [David Joyner](https://github.com/wdjoyner) who's an expert in the field of group theory, my comentor [Aaron Meurer](https://github.com/asmeurer), the current project leader for sympy, and the entire sympy community for helping me out and reviewing my work!
