# PerceptionMetrics

**Parent:** JdeRobot — Project Ideas
**Source:** https://jderobot.github.io/PerceptionMetrics/
**Scraped:** 2026-02-22T23:28:47.557868

---

⚠️ PerceptionMetrics was previously known as DetectionMetrics. The original website referenced in our

Sensorspaper is still available[here]

*PerceptionMetrics* is a toolkit designed to unify and streamline the evaluation of object detection and segmentation models across different sensor modalities, frameworks, and datasets. It offers multiple interfaces including a GUI for interactive analysis, a CLI for batch evaluation, and a Python library for seamless integration into your codebase. The toolkit provides consistent abstractions for models, datasets, and metrics, enabling fair, reproducible comparisons across heterogeneous perception systems.

| 💻
|
|---|

[Installation](https://jderobot.github.io/PerceptionMetrics/installation)

[Compatibility](https://jderobot.github.io/PerceptionMetrics/compatibility)

[Docs](https://jderobot.github.io/PerceptionMetrics/py_docs/build/html/index.html)

[GUI](https://jderobot.github.io/PerceptionMetrics/gui)

# What’s supported in PerceptionMetrics

| Task | Modality | Datasets | Framework |
|---|---|---|---|
| Segmentation | Image | RELLIS-3D, GOOSE, RUGD, WildScenes, custom GAIA format | PyTorch, Tensorflow |
| LiDAR | RELLIS-3D, GOOSE, WildScenes, custom GAIA format | PyTorch (tested with
|

More details about the specific metrics and input/output formats required fow each framework are provided in the [Compatibility](https://jderobot.github.io/PerceptionMetrics/compatibility/) section

# DetectionMetrics

Our previous release, ** DetectionMetrics**, introduced a versatile suite focused on object detection, supporting cross-framework evaluation and analysis.

[Cite our work](https://jderobot.github.io#cite)if you use it in your research!

| 💻
|
|---|

[Docs](https://jderobot.github.io/PerceptionMetrics/DetectionMetrics)

[Docker](https://hub.docker.com/r/jderobot/detection-metrics)

[Paper](https://www.mdpi.com/1424-8220/22/12/4575)

# Cite our work

```
@article{PaniegoOSAssessment2022,
author = {Paniego, Sergio and Sharma, Vinay and Cañas, José María},
title = {Open Source Assessment of Deep Learning Visual Object Detection},
journal = {Sensors},
volume = {22},
year = {2022},
number = {12},
article-number = {4575},
url = {https://www.mdpi.com/1424-8220/22/12/4575},
pubmedid = {35746357},
issn = {1424-8220},
doi = {10.3390/s22124575},
}
```
