# Towards a Neural Extraction Framework — GSoC 2026

**Parent:** DBpedia — Project Ideas
**Source:** https://forum.dbpedia.org/t/towards-a-neural-extraction-framework-gsoc-2026/4778
**Scraped:** 2026-02-22T23:28:47.608054

---

*This project started in 2021 and is looking to its 6th participation in DBpedia’s GSoC.*

Description

Every Wikipedia article links to a number of other articles. In DBpedia, we keep track of these links through the `dbo:wikiPageWikiLink`

property. Thanks to them, we know that the [ :Berlin_Wall](https://dbpedia.org/resource/Berlin_Wall) entity is — at the time of writing — semantically connected to 299 base entities.

However, only 9 out of 299 base entities are linked from `:Berlin_Wall`

via also another predicate. This suggests that in the large majority of cases, it is not clear what kind of relationship exists between the entities. In other words, DBpedia does not know what specific RDF predicate links the subject (in our case, `:Berlin_Wall`

) to any of the remaining 290 objects.

Currently, such relationships are extracted from tables and the infobox, usually found top right of a Wikipedia article, via the [Extraction Framework](https://wiki.dbpedia.org/documentation). Instead of extracting RDF triples from semi-structured data only, we built an end-to-end system to leverage information found in the entirety of a Wikipedia article, including page text.

The repository where all source code is stored is the following:

[github.com](https://github.com/dbpedia/neural-extraction-framework)

[GitHub - dbpedia/neural-extraction-framework: Repository for the GSoC project 'Towards a Neural...](https://github.com/dbpedia/neural-extraction-framework)

Repository for the GSoC project 'Towards a Neural Extraction Framework'

Goal

The goal of this project is to develop a framework for predicate resolution of wiki links among entities by:

- harnessing neural models to extract knowledge from text and
- validating their output against the DBpedia ontology.

During the first GSoC years, we employed [a suite of machine-learning models](https://github.com/dbpedia/neural-extraction-framework/tree/main/GSoC22) to perform joint entity-relation extraction on open-domain text. Additionally, we implemented [an end-to-end system](https://github.com/dbpedia/neural-extraction-framework/blob/main/GSoC23/) that translates any English sentence into triples using the DBpedia vocabulary. Over the last two years, we improved the quality of output triples using a chain-of-thought approach powered by a large language model.

However, the current algorithm still has the following issues. Now, we want to devise a method that can solve as many of them as possible.

- The generated triples were not validated against the DBpedia ontology and may thus lead to inconsistencies in data.
- The current models are not efficient enough to scale to millions of entities.
- The extracted relations are not categorised with respect to their semantics (e.g. reflexive/irreflexive, symmetric/antisymmetric/asymmetric, transitive, equivalence).
- Ideally, our algorithm should be able to adapt its output not only to the DBpedia vocabulary but to any specified one (e.g., SKOS,
[schema.org](http://schema.org/), Wikidata, RDFS, or even a combination of many).

Alternative extraction targets

The current pipeline targets relationships that are explicitly mentioned in the text. The contributor may also choose to extract complex relationships, such as:

**Causality.**(Addressed during GSoC 2021, but not completed.) The direct cause-effect between events, e.g., from the text

The Peaceful Revolution (German: Friedliche Revolution) was the process of sociopolitical change that led to the opening of East Germany’s borders with the west, the end of the Socialist Unity Party of Germany (SED) in the German Democratic Republic (GDR or East Germany) and the transition to a parliamentary democracy, which enabled the reunification of Germany in October 1990.


extract: `:Peaceful_Revolution`

`–––dbo:effect––>`

`:German_reunification`


**Issuance.**An abstract entity assigned to some agent, e.g., from the text

Messi won the award, his second consecutive Ballon d’Or victory.


extract: `:2010_FIFA_Ballon_d'Or`

`–––dbo:recipient––>`

`:Lionel_Messi`


Material

The contributor may use any LLM API and/or Python deep learning framework. The following resources are recommended (but not compulsory) for use in the project.

- The project repository linked above and the machine-learning models mentioned in the readme files found in each GSoC folder.
- The
[2025](https://github.com/Gnav3852/neural-extraction-framework/wiki)and[2024 blog](https://smilingprogrammer.github.io/GSoC-2024-blog/)to understand the project status quo. [Python Wikipedia](https://pypi.org/project/wikipedia/)makes it easy to access and parse data from Wikipedia.[Huggingface Transformers for Natural Language Inference](https://huggingface.co/facebook/bart-large-mnli)can be extremely useful to extract structured knowledge from text or perform zero-shot classification.[DBpedia Lookup](https://lookup.dbpedia.org/)is a service available both online and offline (e.g., given a string, list all entities that may refer to it).[DBpedia Anchor text](https://databus.dbpedia.org/dbpedia/generic/anchor-text/)is a dataset containing the text and the URL of all links in Wikipedia; the indexed dataset will be available to the student (e.g., given an entity, list all strings that point to it).- An
[example of an excellent proposal](http://tommaso-soru.it/files/misc/Akshay-DBpedia-GSoC-2017-proposal.pdf)that was accepted a few years ago.

Project size

The size of this project can be either medium or large. Please state in your proposal the number of total project hours you intend to dedicate to it (175 or 350).

Impact

This project will potentially generate millions of new statements. This new information could be released by DBpedia to the public as part of a new dataset. The creation of a neural extraction framework could introduce the use of robust parsers for a more accurate extraction of Wikipedia content.

Warm-up tasks

- Get familiar with SPARQL on the
[DBpedia endpoint](https://dbpedia.org/sparql). - Understand the
[science behind relation extraction](https://medium.com/@andreasherman/different-ways-of-doing-relation-extraction-from-text-7362b4c3169e). - Run and understand the pipeline implemented
[last year](https://github.com/dbpedia/neural-extraction-framework/tree/main/GSoC25).
