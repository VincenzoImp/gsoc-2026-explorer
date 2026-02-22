# Time-dependent constraints in gfpop

**Parent:** R project for statistical computing — Project Ideas
**Source:** https://github.com/rstats-gsoc/gsoc2026/wiki/time-dependent-constraints-in-gfpop
**Scraped:** 2026-02-22T23:28:47.626094

---

-
[Notifications](https://github.com/login?return_to=%2Frstats-gsoc%2Fgsoc2026)You must be signed in to change notification settings -
[Fork 0](https://github.com/login?return_to=%2Frstats-gsoc%2Fgsoc2026)

# time dependent constraints in gfpop

[18 revisions](https://github.com/rstats-gsoc/gsoc2026/wiki/time-dependent-constraints-in-gfpop/_history)

There are many R packages for changepoint detection, which is an
important problem in many application domains (genomics, finance,
etc). A new changepoint model with up-down constraints has shown
state-of-the-art peak detection accuracy in genomic data, and more
general models like this can be implemented using the new [gfpop](https://github.com/vrunge/gfpop/)
package (Runge et al, [arXiv:2002.03646](https://arxiv.org/abs/2002.03646)).

Currently the gfpop package only supports constraints which are valid
for all time points. The goal of this project is to extend gfpop to
allow constraints which depend on time. This will allow implementing
fast optimal solvers for several new constrained changepoint models
such as [Labeled Optimal Partitioning](https://arxiv.org/abs/2006.13967).

Existing R packages fall into two categories:

- generic frameworks such as gfpop, Segmentor3IsBack, changepoint which allow computation of several different types of changepoint models. (but do not allow time dependent constraints)
- domain-specific packages such as LOPART, which computes one model with time dependent constraints (Gaussian loss, label constraints).

The goal of the coding project would be to extend gfpop to support time dependent constraints, so a wider variety of models could be specified in this framework.

I think the easiest way to implement this from a R/C++ interface perspective would be to

- 1. Allow user to pass to gfpop a new “rule” argument, a vector of length N (number of data) with entries that are integers which specify an update rule ID to use for each data point.
- 2. Add a “rule” argument in the Edge function. This is an integer which should correspond to the IDs provided in 1.

In practice this could be specified via R code like:

```
LOPART.graph <- gfpop::graph(
gfpop::Edge("normal", "normal", type="null", rule=1),
gfpop::Edge("normal", "normal", type="std", rule=1, penalty=5.5),
gfpop::Edge("normal", "normal", type="null", rule=2),
gfpop::Edge("noChange", "noChange", type="null", rule=2),
gfpop::Edge("normal", "noChange", type="std", rule=2),
gfpop::Edge("normal", "normal", type="std", rule=3),
gfpop::Edge("noChange", "normal", type="null", rule=3),
gfpop::Edge("normal", "normal", type="null", rule=4))
gfpop::gfpop(data.vec, LOPART.graph, rule=data.table::fcase(
unlabeled, 1,
in.positive.label, 2,
end.positive.label, 3,
in.negative.label, 4))
```

The idea in the code above is that the data.table::fcase call is like a switch statement that returns a vector with elements from 1 to 4 which specify what update rule/graph to use at each data point (variables unlabeled/in.positive.label etc above are logical vectors that depend on the provided label data in the LOPART model).

Then when you compute the DP updates you can, instead of using all of the edges, you can instead just use the subset of edges which correspond to the ruleID of the current data point.

The only tricky part is that we sometimes need to set a cost function to be infinity (if there are no edges coming to it at this data point) and the operators (min-less, min-more, min-env) need to be updated to handle the case of infinite inputs.

The goal for GSOC will be to implement at least

- up-down constrained model with label constraints (6 rule IDs).
- usual changepoint model with 0/1 label constraints (4 rule IDs, shown in R code above).

The gfpop package is already very useful, and incorporating time-dependent constraints will make it more useful.

Please get in touch after completing at least one of the tests below.

- EVALUATING MENTOR:
[Vincent Runge](https://github.com/vrunge/)<vincent.runge@univ-evry.fr> - Co-mentors:
[Toby Dylan Hocking](https://github.com/tdhock)<tdhock5@gmail.com> and G Romano

Do one or several — doing more hard tests makes you more likely to be selected.

NOTE: this is a very difficult GSOC project, and so the ideal contributor really should do all tests below. If we can’t find a contributor that can do all these tests, we should probably not fund this GSOC project.

**Easy:** write an R function `plotModel`

which takes a `gfpop::graph`

as above and draws a matrix of nodes (one row for each state, one
column for each rule) and edges.

**Medium:** the Segmentor3IsBack package implements the segment neighborhood model (best models in
1,…,K segments) for the
Poisson loss and no constraints, but there is no implementation available for the
optimal partitioning model (best K-segment model for a single penalty
parameter, without computing the models with 1,…,K-1 segments). The
goal of this test is to modify the code in the `PeakSegOptimal`

package, in
order to implement a solver for the optimal partitioning problem with
Poisson loss and no constraints. Begin by studying [PeakSegFPOPLog.cpp](https://github.com/tdhock/coseg/blob/master/src/PeakSegFPOPLog.cpp)
which implements the optimal partitioning model for the Poisson loss
and the up-down constraints. There are two states in this model, up
and down. Since the up-down constrained solver has two states, there
are N x 2 optimal cost functions to compute (`cost_model_mat`

is of
dimension `data_count*2`

). The cost of being in the up state at
`data_i`

is `cost_model_mat[data_i]`

and the cost of being in the down
state is `cost_model_mat[data_i+data_count]`

. The
`min_prev_cost.set_to_min_less_of(down_cost_prev)`

method enforces a
non-decreasing constraint between adjacent segment means, for the
state change down->up. Analogously, the
`PiecewisePoissonLossLog::set_to_min_more_of`

method enforces a
non-increasing constraint for the state change up->down. To implement
the unconstrained solver, you just need to implement a new
`PiecewisePoissonLossLog::set_to_unconstrained_min_of`

method that
computes the minimum constant cost function (one `PoissonLossPieceLog`

object), and then uses that to compute the N x 1 array of optimal cost
functions (`cost_model_mat`

). Read about the FPOP algorithm in
[Maidstone et al 2016](http://link.springer.com/article/10.1007/s11222-016-9636-3?wt_mc%3Dinternal.event.1.SEM.ArticleAuthorOnlineFirst) for more info. When you are done with your
implementation, check your work by comparing with the output of
`Segmentor3IsBack::Segmentor(model=1)`

. Perform model selection
yourself for a range of penalty parameters. Using `testthat`

, write
some test cases which make sure your function gives the same exact
model as the corresponding selected Segmentor model.

**Hard:** there is not yet an regularized isotonic regression solver for
the normal loss ([issue](https://github.com/tdhock/coseg/issues/3)), and your goal in this test is to implement
one. Like the unconstrained model described the Medium test, the
regularized isotonic regression model also has only one state. So you
can start by modifying the Medium test code, which should have a
`cost_model_mat`

which is N x 1. However the isotonic regression
constraint means that all changes are non-decreasing, so you should
use `set_to_min_less_of`

instead of `set_to_unconstrained_min_of`

. Now
the difficult part: the existing code in the `coseg`

package
implements the Poisson loss via `class PoissonLossPieceLog`

, but you
need to implement another class for the Normal loss,
`NormalLossPiece`

. This class will need to declare different
coefficients `Constant`

, `Linear`

, `Quadratic`

for a function
f(mean)=Constant + Linear*mean + Quadratic*mean^2. You will need to
provide implementations for `get_smaller_root`

and `get_larger_root`

by using the `sqrt`

function in `#include <math.h>`

. It will be judged
even better if you can get `PoissonLossPieceLog`

and `NormalLossPiece`

to inherit from the same base class with shared methods (that is the
approach that the Segmentor package uses to implement several loss
functions, and that is the approach that will be recommended for this
GSOC project). Check your work by writing a `testthat`

unit test to
make sure that the model returned by your function with penalty=0 is
the same as the model returned by the `isoreg`

function (PAVA
algorithm). Write another test that checks that the output model
is the same as `Fpop`

(when all changes are non-decreasing).

Contributors, please post a link to your test results here.

- EXAMPLE CONTRIBUTOR 1 NAME, LINK TO GITHUB PROFILE, LINK TO TEST RESULTS.

Github : [Link to Github](https://github.com/kunal649)
Easy task : [Link to Gist](https://gist.github.com/kunal649/5efb0d44a0074dba3cdaf432fb0f85dc)
Medium task : re-evaluating

GitHub: https://github.com/aakritixyz Easy Test Results: https://github.com/aakritixyz/gfpop-gsoc-easy-tests
