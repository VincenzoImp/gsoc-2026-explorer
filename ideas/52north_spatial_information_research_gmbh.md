# 52°North Spatial Information Research GmbH — Project Ideas

**Source:** https://52north.org/outreach-dissemination/google-summer-of-code/project-ideas/
**Scraped:** 2026-02-22T23:28:47.619003

---

## GSoC 2026

### Previous Projects

Check out our [Blog Post Series](https://blog.52north.org/category/gsoc/) for more information on previous projects!

## 1. MCP for OGC APIs

#### Developing Multi Context Protocols for the suite of OGC APIs

**Explanation**

The Multi Context Protocol (MCP) offers a structured mechanism to seamlessly bridge the gap between natural language input, often processed via Large Language Models (LLMs), and well-defined, executable program code. In essence, MCP translates natural language instructions into precise actions. The [Open Geospatial Consortium](https://www.ogc.org/) (OGC) has developed several [OGC API](https://ogcapi.ogc.org/)s that have achieved widespread adoption across the geospatial domain and are natively understood by many prominent open-source Geo-IT solutions (e.g., [pygeoapi](https://pygeoapi.io/), [QGIS](https://qgis.org/), [geoserver](https://geoserver.org/)). The goal is to lower the barriers in using GIS tools for non-experts through LLM supported agents that use MCP to access spatial data and processes via OGC APIs.

To illustrate the underlying requirements and potential, consider the following scenario: A local municipality’s urban planner needs to conduct a [cool spot analysis](https://meetingorganizer.copernicus.org/EGU22/EGU22-10358.html) (for context, see our [blog post](https://blog.52north.org/2022/12/16/cool-spots-in-munster/)). Critically, this planner does not possess specialized GIS expertise but interacts with an urban analytics bot. A natural language prompt such as, “Conduct a cool spot analysis based on the new parks I have designed for the city,” should be fully understood and acted upon. Technically, we assume an OGC API process capable of this analysis is available. The bot’s role would be to suggest this functionality, then intelligently prompt for—or even prefill—the required defined input data sources (like the park boundaries) and clearly explain the expected outputs. Once the process is fully configured and validated, it is executed, and the results are returned and visualized for the planner. While this serves as a concrete OGC API Processes example, similar use cases and functional requirements apply to other OGC APIs and associated geospatial services.

**Expected Results**

**A Modular MCP Mapping for a Set of OGC APIs**:- Create a formal, extensible, and machine-readable specification (e.g., JSON schema) that translates core functionality of selected OGC APIs (Features, Records, EDR) into MCP concepts.
- The design must be modular, allowing independent and reusable translations for each API component.

**A Showcase Implementation Illustrating the Benefit of the MCP Mapping:**- Develop an open-source client library or proxy service (reference implementation) that uses the unified MCP concepts to consume data from diverse OGC API instances.
- The showcase must demonstrate key benefits: seamless interoperability across different OGC API types, reduced client-side complexity due to abstraction, and decoupling from underlying API specification changes.


**Code Challenge**

**Establishment and Configuration of an OGC API – Processes Backend**:**Goal**: To deploy and meticulously configure a robust backend service that fully implements the specifications of the Open Geospatial Consortium (OGC) API – Processes standard.**Scope**: This includes selecting an appropriate open-source or proprietary implementation (e.g., based on technologies like pygeoapi, PyWPS, GeoServer (with plugins), or a custom microservice architecture), setting up the execution environment (e.g., containerization with Docker/Kubernetes), defining the necessary configuration parameters, and ensuring the service adheres to the required endpoints (e.g., /processes, /jobs, /results). Attention must be paid to security protocols, authentication mechanisms, and scaling considerations for potential production use.

**Execution of a Sample Process within the Established Environment:****Goal**: To validate the setup and configuration by successfully invoking and completing a representative OGC API – Processes operation.**Scope**: A simple, yet meaningful, geospatial or analytical process must be defined (e.g., a buffer operation, zonal statistics calculation, or a simple data aggregation). This process will be registered with the newly configured backend. Subsequently, the full lifecycle of the process execution will be tested: submission of the processing request via the API, monitoring the job status, and retrieving the final processed output and/or job result metadata. This task serves as the critical ‘proof-of-concept’ to confirm the entire system is operational and correctly handles input parameters, asynchronous execution, and output delivery according to the OGC API – Processes standard.


**Community and Code License**

Apache Software License, Version 2

**Mentors**

Benjamin Pross (b.pross @52north.org) , Benedikt Gräler (b.graeler @52north.org)

**Project Duration**

The duration of the project is estimated at **175** hours. An extension is possible.

**Chat**

TBD

## 2. Weather Routing Tool – QGIS Plugin

### Explanation

The open-source 52°North [Weather Routing Tool (WRT)](https://github.com/52North/WeatherRoutingTool) was initially developed during the [MariData project](/ideas/52north-spatial-information-research-gmbh/solutions-marigeoroute) and is currently being further developed and used in the [TwinShip project](https://twin-ship.eu/). It provides a way to find the optimal route for a ship that minimizes fuel consumption under varying weather conditions. Several constraints can be integrated into the optimization process, such as water depth and traffic separation zones. Currently, there are two algorithms available: an isofuel algorithm and a genetic algorithm. Details of the MariData project and example applications of the Weather Routing Tool can be found in the following publication “[MariData – Digital Twin for Optimal Vessel Operations Impacting Ship Design](https://proceedings.open.tudelft.nl/imdc24/article/view/875.)“.

### Expected Results

A new QGIS plugin for the WRT should be implemented. The implementation should be done in Python.

The following features are expected:

- Configuration wizard containing
- a clearly structured interface (considering mandatory, optional, conditional variables)
- map interactions to set source, destination and intermediate waypoints
- the possibility to download the final configuration as a json file (to be used to run the WRT)

- Visualization capabilities for
- weather data including proper styling, time slider and subsetting with statistics (e.g., what is the average wave height in the subset?)
- routes including their properties (ship speed, fuel consumption, etc.)


Optional:

- Mock-ups
- Before starting with the actual implementation of the GUI components, mock-ups could be created to better plan the design and proposed user interactions

- Running the WRT directly from QGIS
- Using a quick algorithm (e.g., GCR slider); possibly with live visualization
- Using the full capabilities of the WRT (including the genetic algorithm etc.)


**Links**

[https://github.com/52North/WeatherRoutingTool](https://github.com/52North/WeatherRoutingTool)[https://52north.github.io/WeatherRoutingTool/source/configuration.html](https://52north.github.io/WeatherRoutingTool/source/configuration.html)[https://docs.qgis.org/3.40/en/docs/pyqgis_developer_cookbook/plugins/index.html](https://docs.qgis.org/3.40/en/docs/pyqgis_developer_cookbook/plugins/index.html)[https://g-sherman.github.io/Qgis-Plugin-Builder/](https://g-sherman.github.io/Qgis-Plugin-Builder/)

### Code Challenge

**Run the WRT**- Prepare weather data
- You are free to choose the geographic region and time. We recommend choosing a small subset to make it easier to handle.
- Options:
- Create your own synthetic weather conditions.
- Download actual historical or forecast data from public portals (Copernicus, NOAA, …).

- Create a configuration file
- Define a source and destination within the bounding box of the weather data.
- We recommend using the genetic algorithm (“ALGORITHM_TYPE”) and the direct power method (“BOAT_TYPE”).



- Prepare weather data
**Load the final route into QGIS and calculate the total distance from source to destination via the waypoints.**

Which method is used is up to the user as long as it is done with QGIS. If the QGIS Python console is used, the script has to be shared. If a manual workflow is chosen, the steps have to be clearly documented, e.g., using screenshots.**Document your steps and provide the final route (json file)**.

### Community and Code License

MIT License

### Mentors

Martin Pontius (m.pontius @52north.org), Katharina Demmich (k.demmich @52north.org)

### Project duration

The duration of the project is estimated at **175** hours. An extension is possible.

### Chat

TBD

## 3. Weather Routing Tool – Improve Test Framework

### Explanation

The open-source 52°North [Weather Routing Tool (WRT)](https://github.com/52North/WeatherRoutingTool) was initially developed during the [MariData project](/ideas/52north-spatial-information-research-gmbh/solutions-marigeoroute) and is currently being further developed and used in the [TwinShip project](https://twin-ship.eu/). It provides a way to find the optimal route for a ship that minimizes fuel consumption under varying weather conditions. Several constraints can be integrated into the optimization process, such as water depth and traffic separation zones. Currently, there are two algorithms available: an isofuel algorithm and a genetic algorithm. Details of the MariData project and example applications of the Weather Routing Tool can be found in the following publication “[MariData – Digital Twin for Optimal Vessel Operations Impacting Ship Design](https://proceedings.open.tudelft.nl/imdc24/article/view/875.)“.

### Expected Results

The WRT’s apparent test framework shall be extended and available tests improved to achieve a better test coverage as well as better readability. The implementation shall be done using the pytest framework of Python and/or shell scripts.

The following features are expected:

- Harmonization of available unit tests and improvement of their readability e.g. by
- the introduction of pytest fixtures,
- combining test groups into classes,
- separation into unit and integration test

- Separation of unit tests and monitoring tests:
- Clear separation of unit/integration tests with hard assertions and tests that produce monitoring figures. While unit tests shall be executed by default, tests that produce monitoring figures shall be executed on demand.
- If the generation of monitoring figures is demanded, a pdf shall be generated automatically that summarizes the figures.

- Development of regression tests:
- Automated tests for the reproducibility of routes with the full routing tool for specific configurations.
- The execution time of the integration tests shall be minimized.
- Optional: structured summary of potential differences with respect to the test routes provided on demand.


**Links:**

### Code Challenge

**Run the WRT**- Prepare weather data
- You are free to choose the geographic region and time. We recommend chooseing a small subset to make it easier to handle.
- Options:
- Create your own synthetic weather conditions.
- Download actual historical or forecast data from public portals (Copernicus, NOAA, …).


- Create a configuration file
- Define a source and destination within the bounding box of the weather data.
- We recommend using the genetic algorithm (“ALGORITHM_TYPE”) and the direct power method (“BOAT_TYPE”).


- Prepare weather data
**Implement a unit test for the function RoutingProblem.get_power**assuming that the current results provided by the function are correct. The unit test shall be embedded in the WRT’s test framework.

### Community and Code License

MIT License

### Mentors

Martin Pontius (m.pontius @52north.org), Katharina Demmich (k.demmich @52north.org)

### Project Duration

The duration of the project is estimated at **175** hours. An extension is possible.

## 4. Weather Routing Tool – Extension of Weather Module for Statistical Analysis

### Explanation

The open-source 52°North [Weather Routing Tool (WRT)](https://github.com/52North/WeatherRoutingTool) was initially developed during the [MariData project](/ideas/52north-spatial-information-research-gmbh/solutions-marigeoroute) and is currently being further developed and used in the [TwinShip project](https://twin-ship.eu/). It provides a way to find the optimal route for a ship that minimizes fuel consumption under varying weather conditions. Several constraints can be integrated into the optimization process, such as water depth and traffic separation zones. Currently, there are two algorithms available: an isofuel algorithm and a genetic algorithm. Details of the MariData project and example applications of the Weather Routing Tool can be found in the following publication “[MariData – Digital Twin for Optimal Vessel Operations Impacting Ship Design](https://proceedings.open.tudelft.nl/imdc24/article/view/875.)“.

### Expected Results

The weather module of the WRT should be extended to allow statistical analysis. It already allows downloading data subsets from different providers as in-memory objects (xarray.Dataset) or NetCDF file, i.e., as space-time cube or along trajectories. However, there is no built-in functionality to analyse these subsets statistically. Statistical methods from xarray could directly be used. The main challenges are related to memory and/or hard drive storage and runtime (including download time of data). Applications should clearly describe strategies for tackling these challenges.

One expected use of the statistics feature is to identify suitable scenarios for simulation studies.

The following investigations are expected:

- Analysis of different methods to store and later on access weather data to achieve optimal runtime without memory issues. Possible alternatives or addons to the current implementation could be to use the Python package dask or the file format Zarr.
- A summary of the results as well as the implementation of the best-performing method into the WRT.
- Implementation of the functionality to visualize statistical parameters for a certain area and time spans of the order of one year. The following statistical distributions are desired:
- Time series plot of the average wind speed (wave height) and direction per day for one year
- Correlation of wind speed (wave height) and direction for a desired time span
- Probability distribution of wind speed (wave height) for one year

- Operations which should be supported: subsetting along each dimension (time, space, variables), interpolation, statistics (min, max, mean, …)

Optional:

- Adapters for additional open datasets could be implemented. Currently, data from the
[Copernicus Marine Service](https://marine.copernicus.eu/)and the[Global Forecast System](https://www.ncei.noaa.gov/products/weather-climate-models/global-forecast)are integrated.

**Links:**

[https://github.com/52North/WeatherRoutingTool](https://github.com/52North/WeatherRoutingTool)[https://github.com/52North/maridatadownloader](https://github.com/52North/maridatadownloader)[https://docs.xarray.dev/en/latest/user-guide/io.html](https://docs.xarray.dev/en/latest/user-guide/io.html)[https://www.dask.org/](https://www.dask.org/)[https://zarr.dev/](https://zarr.dev/)

### Code Challenge

**Run the WRT**- Prepare weather data
- You are free to choose the geographic region and time. We recommend choosing a small subset to make it easier to handle.
- Options:
- Create your own synthetic weather conditions.
- Download actual historical or forecast data from public portals (Copernicus, NOAA, …).


- Options:

- You are free to choose the geographic region and time. We recommend choosing a small subset to make it easier to handle.
- Create a configuration file
- Define a source and destination within the bounding box of the weather data.
- We recommended using the genetic algorithm (“ALGORITHM_TYPE”) and the direct power method (“BOAT_TYPE”).


- Prepare weather data
**Use a profiler to analyze run time and/or memory consumption of the WRT’s execution and summarize the results.****Document your steps and provide the final route (json file)****Visualize the wave height and wind direction for the chosen time period and calculate the respective mean value, median and standard deviation.**

### Community and Code License

MIT License

### Mentors

Martin Pontius (m.pontius @52north.org), Katharina Demmich (k.demmich @52north.org)

### Project Duration

The duration of the project is estimated at **175** hours. An extension is possible.

## 4. Your Idea

We are also open to your own ideas for developing open source software that addresses 52°North’s software or fits within the scope of 52°North. Before writing a detailed proposal, we strongly recommend that you contact our org-admin with a project pitch (~1 page) that addresses at least the following points

- Project name:
- Reference to existing open source solution (if any):
- Explanation of the software’s scope/purpose/context:
- Expected results of the proposed project:
- Community and Code License in use/planned:
- Mentor candidates (if any):
