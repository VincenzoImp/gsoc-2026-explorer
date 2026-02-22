# trying out Kubeflow

**Parent:** Kubeflow — Project Ideas
**Source:** https://www.kubeflow.org/docs/started/installing-kubeflow/
**Scraped:** 2026-02-22T23:28:47.580831

---

# Installing Kubeflow

This guide describes how to install Kubeflow projects, or Kubeflow AI reference platform using package distributions or Kubeflow manifests.

Read [the introduction guide](https://www.kubeflow.org/docs/started/introduction/) to learn more about Kubeflow,
Kubeflow projects, and Kubeflow AI reference platform.

## Installation Methods

You can install Kubeflow using one of these methods:

## Kubeflow Projects

Kubeflow projects in the [Kubeflow ecosystem](https://www.kubeflow.org/docs/started/architecture/#kubeflow-ecosystem) can be
deployed as a standalone services, without the need to install the entire Kubeflow AI reference
platform.You might integrate these services as part of your existing AI platform or use them
independently.

These projects are a quick and easy method to get started with the Kubeflow. They provide flexibility to users who may not require the capabilities of a full Kubeflow AI reference platform.

The following table lists Kubeflow projects that may be deployed in a standalone mode. It also
lists their associated GitHub repository and
corresponding [AI lifecycle stage](https://www.kubeflow.org/docs/started/architecture/#kubeflow-projects-in-the-ai-lifecycle).

| Kubeflow Project | AI Lifecycle Stage | Source Code |
|---|---|---|
|

`kserve/kserve`

[Kubeflow Katib](https://www.kubeflow.org/docs/components/katib/installation/#installing-katib)`kubeflow/katib`

[Kubeflow Model Registry](https://www.kubeflow.org/docs/components/model-registry/installation/#installing-model-registry)`kubeflow/model-registry`

[Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines/operator-guides/installation/)`kubeflow/pipelines`

[Kubeflow Spark Operator](https://www.kubeflow.org/docs/components/spark-operator/getting-started#installation)`kubeflow/spark-operator`

[Kubeflow Trainer](https://www.kubeflow.org/docs/components/trainer/getting-started)`kubeflow/trainer`

## Kubeflow AI Reference Platform

You can use one of the following methods to install the
[Kubeflow AI reference platform](https://www.kubeflow.org/docs/started/introduction/#what-is-the-kubeflow-ai-reference-platform)
and get the full suite of Kubeflow projects bundled together with additional tools.

### Packaged Distributions

Packaged distributions are maintained by various organizations and typically aim to provide
a simplified installation and management experience for your **Kubeflow Platform**.
Some can be deployed on multiple [Kubernetes distributions](https://kubernetes.io/partners/#conformance),
while others target a specific platform (e.g. EKS or GKE).

**does not endorse or certify**any specific distribution.

The following table lists distributions which are *maintained* by their respective maintainers:

| Maintainer Distribution Name | Kubeflow Version | Target Platform | Link |
|---|---|---|---|
| Aranui Solutions deployKF |
| Multiple
|
|

Charmed Kubeflow

[[release notes]](https://charmed-kubeflow.io/docs/release-notes)[Website](https://charmed-kubeflow.io/)[[release notes]](https://github.com/Azure/kubeflow-aks/releases)[Website](https://azure.github.io/kubeflow-aks/main)[Website](https://nutanix.github.io/kubeflow-manifests)[[release notes]](https://docs.qbo.io/news/2025/05/09/api-1-5-14-released/)[Website](https://docs.qbo.io/demos/kubeflow)Open Data Hub

[Website](https://github.com/opendatahub-io/manifests)### Kubeflow Manifests

The Kubeflow manifests are a collection of community maintained manifests to install Kubeflow AI reference platform in popular Kubernetes clusters such as Kind (locally), Minikube (locally), Rancher, EKS, AKS, GKE. They are aggregated by the Manifests Working Group and are intended to be used by users with Kubernetes knowledge and as the base of packaged distributions.

Kubeflow Manifests contain all Kubeflow projects, Kubeflow Central Dashboard, and other Kubeflow
applications that comprise the **Kubeflow AI reference platform**. This installation is helpful when you want to
try out the end-to-end Kubeflow AI reference platform capabilities.

If you want a stable / conservative experience we recommend to use the [latest stable release](https://github.com/kubeflow/manifests/releases):

You can also install the master branch of [ kubeflow/manifests](https://github.com/kubeflow/manifests) by following the instructions

[here](https://github.com/kubeflow/manifests?tab=readme-ov-file#installation)and provide us feedback.

## Next steps

- Review our
[introduction to Kubeflow](https://www.kubeflow.org/docs/started/introduction/). - Explore the
[architecture of Kubeflow](https://www.kubeflow.org/docs/started/architecture/). - Learn more about the
[Kubeflow projects](https://www.kubeflow.org/docs/components/).

### Feedback

Was this page helpful?

Thank you for your feedback!

We're sorry this page wasn't helpful.
If you have a moment, please [share your feedback](https://github.com/kubeflow/website/issues/new?title=[Feedback]+docs/started/installing-kubeflow/index.md) so we can improve.

[website: kubeflow 1.11 (#4263) (66c831b1)](https://github.com/kubeflow/website/commit/66c831b17d459dcb70d2b8889b149295fca51aa4)
