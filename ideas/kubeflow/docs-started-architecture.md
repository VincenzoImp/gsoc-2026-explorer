# Architecture Overview

**Parent:** Kubeflow — Project Ideas
**Source:** https://www.kubeflow.org/docs/started/architecture/
**Scraped:** 2026-02-22T23:28:47.580754

---

# Architecture

This guide introduces Kubeflow projects and how they fit in each stage of the AI lifecycle.

Read [the introduction](https://www.kubeflow.org/docs/started/introduction/) to learn more about Kubeflow, Kubeflow
projects, and Kubeflow AI reference platform.

## Kubeflow Ecosystem

The following diagram gives an overview of the Kubeflow Ecosystem and how it relates to the wider
Kubernetes and AI landscape. Kubeflow builds on [Kubernetes](https://kubernetes.io/) as a system for
deploying, scaling, and managing AI platforms.

## Introducing the AI Lifecycle

When you develop and deploy an AI application, the AI lifecycle typically consists of several stages. Developing an AI system is an iterative process. You need to evaluate the output of various stages of the AI lifecycle, and apply changes to the model and parameters when necessary to ensure the model keeps producing the results you need.

The following diagram shows the AI lifecycle stages in sequence:

Looking at the stages in more detail:

In the

*Data Preparation*step you ingest raw data, perform feature engineering to extract ML features for the offline feature store, and prepare training data for model development. Usually, this step is associated with data processing tools such as Spark, Dask, Flink, or Ray.In the

*Model Development*step you choose an ML framework, develop your model architecture and explore the existing pre-trained models for fine-tuning like BERT or Llama.In the

*Model Training*step you train or fine-tune your models on the large-scale compute environment. You should use a distributed training if single GPU can’t handle your model size. The results of the model training is the trained model artifact that you can store in the*Model Registry*.In the

*Model Optimization*step you optimize your model hyperparameters and optimize your model with various AutoML algorithms such as neural architecture search and model compression. During model optimization you can store ML metadata in the*Model Registry*.In the

*Model Serving*step you serve your model artifact for online or batch inference. Your model may perform predictive or generative AI tasks depending on the use-case. During the model serving step you may use an online feature store to extract features. You monitor the model performance, and feed the results into your previous steps in the AI lifecycle.

### AI Lifecycle for Production and Development Phases

The AI lifecycle for AI applications may be conceptually split between *development* and
*production* phases, this diagram explores which stages fit into each phase:

### Kubeflow Projects in the AI Lifecycle

The next diagram shows how Kubeflow projects fit for each stage of the AI lifecycle:

See the following links for more information about each Kubeflow project:

[Kubeflow Spark Operator](https://www.kubeflow.org/docs/components/spark-operator/)can be used for data preparation and feature engineering step.[Kubeflow Notebooks](https://www.kubeflow.org/docs/components/notebooks/)can be used for model development and interactive data science to experiment with your AI workflows.[Kubeflow Trainer](https://www.kubeflow.org/docs/components/trainer/)can be used for large-scale distributed training or LLMs fine-tuning.[Kubeflow Katib](https://www.kubeflow.org/docs/components/katib/)can be used for model optimization and hyperparameter tuning using various AutoML algorithms.[Kubeflow Model Registry](https://www.kubeflow.org/docs/components/model-registry/)can be used to store ML metadata, model artifacts, and preparing models for production serving.[KServe](https://kserve.github.io/website/master/)can be used for online and batch inference in the model serving step.[Feast](https://feast.dev/)can be used as a feature store and to manage offline and online features.[Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines/)can be used to build, deploy, and manage each step in the AI lifecycle.

AI platform teams can build on top of Kubeflow by using each
[project independently](https://www.kubeflow.org/docs/started/introduction/#what-are-kubeflow-projects) or deploying the
entire [AI reference platform](https://www.kubeflow.org/docs/started/introduction/#what-is-the-kubeflow-ai-reference-platform)
to meet their specific needs.

## Kubeflow Interfaces

This section introduces the interfaces that you can use to interact with Kubeflow projects.

### Kubeflow Dashboard

The Kubeflow Central Dashboard looks like this:

The Kubeflow AI reference platform includes [Kubeflow Central Dashboard](https://www.kubeflow.org/docs/components/central-dash/overview/)
which acts as a hub for your AI platform and tools by exposing the UIs of components running in the
cluster.

### Kubeflow APIs and SDKs

Various Kubeflow projects offer APIs and Python SDKs.

See the following sets of reference documentation:

[Pipelines reference docs](https://www.kubeflow.org/docs/components/pipelines/reference/)for the Kubeflow Pipelines API and SDK, including the Kubeflow Pipelines domain-specific language (DSL).[Kubeflow Python SDK](https://github.com/kubeflow/sdk/blob/main/kubeflow/trainer/api/trainer_client.py)to interact with Kubeflow Trainer APIs and to manage TrainJobs.[Katib Python SDK](https://github.com/kubeflow/katib/blob/086093fed72610c227e3ae1b4044f27afa940852/sdk/python/v1beta1/kubeflow/katib/api/katib_client.py)to manage Katib hyperparameter tuning Experiments using Python APIs.

## Next steps

- Follow
[Installing Kubeflow](https://www.kubeflow.org/docs/started/installing-kubeflow/)to set up your environment and install Kubeflow.

### Feedback

Was this page helpful?

Thank you for your feedback!

We're sorry this page wasn't helpful.
If you have a moment, please [share your feedback](https://github.com/kubeflow/website/issues/new?title=[Feedback]+docs/started/architecture.md) so we can improve.

[trainer: Update kubeflow sdk reference (#4171) (a3afb00a)](https://github.com/kubeflow/website/commit/a3afb00ac13a7e3bea0a0d2da53eb511251bb54c)
