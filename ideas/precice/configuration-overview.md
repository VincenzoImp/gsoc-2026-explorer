# preCICE configuration file

**Parent:** preCICE — Project Ideas
**Source:** https://precice.org/configuration-overview.html
**Scraped:** 2026-02-22T23:28:47.561538

---

`xml`

file, typically named `precice-config.xml`

. Here, you specify which solvers participate in the coupled simulation, which coupling data values they exchange, which numerical methods are used for the data mapping and the fixed-point acceleration and many other things. On this page, we give you an overview of the complete configuration section of the documentation.
## You are new to preCICE and want to learn how the configuration works?

Have first a look at the [introduction page](https://precice.org/configuration-introduction.html). Here, we explain in which basic sections the configuration is structured and how the different sections are connected. Afterwards you can study the details of the main parts:

[Mapping configuration](https://precice.org/configuration-mapping.html)[Communication configuration](https://precice.org/configuration-communication.html)[Coupling scheme configuration](https://precice.org/configuration-coupling.html)[Acceleration configuration](https://precice.org/configuration-acceleration.html)[Mesh exchange example](https://precice.org/configuration-coupling-mesh-exchange.html)

And some optional advanced parts:

[Logging configuration](https://precice.org/configuration-logging.html)[Exports configuration](https://precice.org/configuration-export.html)[Action configuration](https://precice.org/configuration-action.html)[Watchpoint configuration](https://precice.org/configuration-watchpoint.html)[Multi coupling configuration](https://precice.org/configuration-coupling-multi.html)

## You are already familiar with the preCICE configuration, but you don’t remember how a certain option was called?

Then you should look at the [configuration reference](https://precice.org/configuration-xml-reference.html). Also try the search here on top. The configuration reference is up to date with the last release of preCICE. If you need a [previous version](https://precice.org/fundamentals-previous-versions.html), you can always generate this documentation yourself:

```
./precice-config-doc md > reference.md
```


There is also an `xml`

variant of the reference. Just call `precice-config-doc`

without arguments to see all options.

## You want to visualize your configuration file?

Visualizing the configuration file is a good way to spot mistakes, but also to learn how the configuration is structured. Do not forget to try out the [configuration visualizer](https://precice.org/tooling-config-visualization.html).

## You want to port your configuration file from preCICE v2.x to v3.x?

There is a [separate page with all steps required for porting](https://precice.org/couple-your-code-porting-v2-3.html#precice-configuration-file).

**Note:**The parsing of floating point numbers in the configuration files depends on your system

[locale](https://docs.oracle.com/cd/E19455-01/806-0169/overview-9/index.html). If you get errors emitted by

`xml::XMLAttribute`

, then please set the locale to `export LANG=en_US.UTF-8`

.
