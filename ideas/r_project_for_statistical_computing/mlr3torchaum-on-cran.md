# mlr3torchAUM on CRAN

**Parent:** R project for statistical computing — Project Ideas
**Source:** https://github.com/rstats-gsoc/gsoc2026/wiki/mlr3torchAUM-on-CRAN
**Scraped:** 2026-03-10T16:58:40.306278

---

## Background

In real-world classification problems, there is often class imbalance

* 3% autism diagnoses, 97% not, in National Survey of Children’s Health data.
* small minority of pixels with object to detect, large majority of background, in image segmentation.
* small minority of rare words, large majority of frequent words, in large language models.

## Related work

torch in R has weighted loss functions which can be useful when the test set and train set have different levels of class imbalance.
ROC curves are often used for evaluation of imbalanced binary classification.

A standard baseline learner would be to use class weights in the torch loss or to do upsampling via
https://mlr3pipelines.mlr-org.com/reference/mlr_pipeops_classbalancing.html

Otherwise there is this blog post
https://mlr-org.com/gallery/basic/2020-03-30-imbalanced-data/index.html

The proposed project involves ROC curves, which can be optimized in gradient descent using [AUM loss](https://jmlr.org/papers/v24/21-0751.html),
which is included in torch since 2025, `torch::nn_aum_loss()`.

## Details of your coding project

[mlr3torchAUM](https://github.com/tdhock/mlr3torchAUM) is an R package on GitHub, with the AUM loss and some custom samplers for gradient descent in imbalanced data.
Goal is to add new functions, and submit to CRAN.

Implement several standard (and state-of-the-art) baselines for imbalanced classification, in the mlr3torch framework, so we can easily compare different learning algorithms on different data sets.

- all pairs losses like https://arxiv.org/abs/2302.11062 and https://libauc.org/
- over- and under- sampling including SMOTE
- re-weighting logistic loss https://mlr3book.mlr-org.com/chapters/chapter13/beyond_regression_and_classification.html#cost-sensitive-measure

Tests and documentation, vignettes, CRAN submission.

## Expected impact

This project will make it easier to compare different approaches for imbalanced classification in R.

## Mentors

Contributors, please contact mentors below after completing at least one
of the tests below.

- EVALUATING MENTOR: Toby Hocking <toby.hocking@r-project.org> is the
  author of R packages mlr3torchAUM and aum.
- Sebastian Fischer is auther of mlr3torch.

## Tests

Contributors, please do one or more of the following tests before
contacting the mentors above.

MENTORS: write several tests that potential contributors can do to
demonstrate their capabilities for this particular project.  Ask some
hard questions that will give you insight about how the contributors write
code to solve problems. You'll see that the harder the questions that
you ask, the easier it will be for you to choose between the contributors
that apply for your project!  Please modify the suggestions below to
make them specific for your project.

- Easy: install the package,
  - run the [typical usage](https://github.com/tdhock/mlr3torchAUM/blob/main/vignettes/Typical_usage.Rmd) vignette, and post a link to the rendered Rmd.
  - re-run the code in [this blog](https://tdhock.github.io/blog/2025/mlr3torch-batch-samplers), and post a link to your results. Are they consistent?
- Medium: propose a PR to solve the [issue of duplicated logic between two similar classes](https://github.com/tdhock/mlr3torchAUM/issues/4).
- Hard: propose a PR with new torch R code implementing the squared hinge loss in https://arxiv.org/pdf/2302.11062 efficiently using the cumsum, and write some tests that verify your code is correct.

## Solutions of tests

Contributors, please post a link to your test results here.
- EXAMPLE CONTRIBUTOR 1 NAME, LINK TO GITHUB PROFILE, LINK TO TEST
  RESULTS. 
- **Aman Kashyap** : [GitHub Profile](https://github.com/AmanKashyap0807), Easy-test [01](https://htmlpreview.github.io/?https://github.com/AmanKashyap0807/mlr3torchAUM-research/blob/main/Evaluation/typical-usage/01_typical_usage_reproduction.html) [02](https://htmlpreview.github.io/?https://github.com/AmanKashyap0807/mlr3torchAUM-research/blob/main/Evaluation/blog-reproduction/02_blog_reproduction.html), [Medium-test](https://github.com/tdhock/mlr3torchAUM/pull/8), Hard-test: In progress
- **Aditya Bansal** : [github](https://github.com/adit-0132), [easy test 1](https://adit-0132.github.io/my-pages/Typical_usage.html), [medium test](https://github.com/tdhock/mlr3torchAUM/pull/11)
- **Siddhesh Akole** : [Github](https://github.com/Siddd-hrr), [Easy-test](https://github.com/Siddd-hrr/rstats-gsoc2026-task--mlr3torchAUM-on-CRAN/blob/main/Easy-test/README.md), [Medium-test](https://github.com/tdhock/mlr3torchAUM/pull/12), [Hard-test](https://github.com/tdhock/mlr3torchAUM/pull/15)
- **Aditya Karki** : [GitHub Profile](https://github.com/Aditya-karki1), [Easy-test](https://gist.github.com/Aditya-karki1/9b64de9ebcb44ea85cf06b302101350d), [Medium-test](https://github.com/tdhock/mlr3torchAUM/pull/9), [Hard-test](https://github.com/tdhock/mlr3torchAUM/pull/10)
- **Wei Cao**: [Github Profile](https://github.com/weicaocw), [Easy-Test](https://weicaocw.github.io/mlr3torchAUM/live_report/easy_task.html), [Medium-Test](https://github.com/tdhock/mlr3torchAUM/pull/16), [Hard-Test](https://github.com/tdhock/mlr3torchAUM/pull/24)
