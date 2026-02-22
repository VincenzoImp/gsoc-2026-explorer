# Feature to store and load model configurations #3176

**Parent:** DeepChem — Project Ideas
**Source:** https://github.com/deepchem/deepchem/issues/3176
**Scraped:** 2026-02-22T23:28:47.606685

---

## Feature to store and load model configurations

**Labels:** enhancement, Contribution Welcome

A deep learning model have number of config options, like dropout, hidden layer size for each of the hidden layer, activation, number of attention heads, type of readout in graph models etc.

It will be nice to have an utility to save a model config to a file which can be used to initialize a model later, like for evaluation.
Some ideas:
- For every model, a config object (a simple python dictionary) which contains the model configuration parameters and methods to save the config to a file, as a json or yaml can be created.
- Maybe layer level config files i.e for each layer, a config file to recreate a layer from its config file.

One advantage is that it will reduce the number of arguments in the call to initialize the model, making the model initialization call cleaner.

