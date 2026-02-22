# torchvision and ecosystem

**Parent:** R project for statistical computing — Project Ideas
**Source:** https://github.com/rstats-gsoc/gsoc2026/wiki/torchvision-and-ecosystem
**Scraped:** 2026-02-22T23:28:47.626294

---

## Background

The mlverse package universe provide a complete ecosystem around the deep-learning framework torch, with {torch} being the native API to the C++ libtorch library. {torchvision} is the computer-vision part of the universe, providing seamless access to datasets and models for classification, object detection and semantic segmentation. 

After massive progress in the number and variety of datasets and models during {torchvision} GSOC 2025, a tipping point has been reached now with almost feature parity with the pytorch/vision counterpart.

But computer-vision deep-learning domain is not limited to pytorch/vision proposed dataset and models. Specifically, latest state-of-the-art models like YOLO family, RT-DETR, and SAM family get high visibility and are highly demanded. 

Furthermore, some features related to segmentation and object detection, like `fasterrcnn` and `convnext` are implemented in base R but rely on heavy sequential loop and suffer low performance. Porting those functions to C++ would raise those models performance to production-grade level.

## Related work

Many computer-vision deep-learning library in python have implemented new models associated with some C++ / CUDA code acceleration, which are not available to R users : 
- [OpenMMLab mmcv](https://mmcv.readthedocs.io/en/latest/)
- [Facebookresearch detectron2](https://github.com/facebookresearch/detectron2)

## GSOC 2026 Coding project : provide the missing C++ features for performance parity 

The contributer task will be, on one hand, the implementation of the the required torchvision performance improvement
- switching some existing R features to C++ and CUDA (like RPN proposal generation, non-maximum suppression of bounding-boxes, ...) 
- adding some key features currently available in other deep-learning vision frameworks  (like multiscale deformable attention, ..)
in the {torchvisionlib} wich host and build the torchvision C++ part. 

So the contributer should be confortable with polyglot programming languages ({torch}, pytorch, C++) and being agile to contribute and coordinating contributions to multiple R packages ({torchvision}, {torchvisionlib}, {torch}, other mlverse packages)  

On the other hand, the contributor will also port the state-of-the-art model to {torchvision}, document them in roxygen, adding comprehensive examples and 
vignettes of end-to-end workflows with those models.

## Expected impact

The impact of those improvements to the mlverse packages will be a increasing adoption of R for computer-vision deep-learning, as well as a more complete model coverage 


## Mentors


Contributors, please contact mentors below after completing at least one
of the tests below.

- EVALUATING MENTOR: Toby Hocking <toby.hocking@r-project.org> is an advanced 
  user of R packages {torchvision}.
- Christophe Regouby <christophe.regouby@free.fr> is an expert in deep-learning,
  contributor or {torchvision} and maintainer of {tabnet} and has previous GSOC 
  experience with r-project organization in 2025.


## Tests

Contributors, please do one or more of the following tests before
contacting the mentors above. Doing more hard tests makes you more likely to be selected.

**Easy**: _Documentation_ Propose an article that mimic [fcn_resnet example article](https://torchvision.mlverse.org/dev/articles/examples/fcnresnet) but using one of the [faster_rcnn object detection model](https://torchvision.mlverse.org/dev/reference/model_fasterrcnn) and incorporate [latest evolution of the faster_rcnn model output](https://github.com/mlverse/torchvision/commit/154d3520e84d86e046290e673d1a39fc8c71e5db)

**Medium**: _Collaboration_ Find a typo or inconsistency or improvement in the roxygen2 help text / Vignettes / Articles of the [{torchvision}](https://torchvision.mlverse.org/dev/) package. Add an entry for this in the NEWS.md file. Build the documentation and propose a fix with the 3 files (R file ,Rd file, NEWS.md) via a [github pull request](https://github.com/mlverse/torchvision/compare). 

**Hard**: _Visualization_ Complete the [`draw_keypoints()`](https://github.com/mlverse/torchvision/blob/ba200df59094e25f4da52b096c06228996dd4da6/R/vision_utils.R#L476-L492) function to draw thin lines between keypoints. Demonstrate result through a sensible example.

**Hard**: _Rcpp interface_ Please demonstrate a R function code that expose in R a C++ function of your choice with its parameters.



## Solutions of tests

Contributors, please post a link to your test results here.
- Chandraveer Singh, https://github.com/Chandraveersingh1717, https://github.com/mlverse/torchvision/pull/292, 
 https://github.com/mlverse/torchvision/pull/293 ,  https://github.com/mlverse/torchvision/pull/294 , https://github.com/mlverse/torchvision/pull/295
  

Srishti Dutta , https://github.com/srishtiii28 , https://github.com/srishtiii28/torchtest , https://srishtiii28.github.io/torchtest/
There isn't a GitHub Pages site here.

If you're trying to publish one, [read the full documentation](https://help.github.com/pages/) to learn how to set up GitHub Pages for your repository, organization, or user account
