# MariData project

**Parent:** 52°North Spatial Information Research GmbH — Project Ideas
**Source:** https://52north.org/solutions/marigeoroute/
**Scraped:** 2026-02-22T23:28:47.619207

---

## MariData GeoPlatform and Routing

**MariGeoRoute helps reduce the energy consumption of cargo ships by providing environmental data and forecasts and routing routines on a cloud-based data infrastructure to support energy optimized routing.**

The [MariData project](https://maridata.org/en/start_en) was funded by [BMWK](https://www.bmwk.de/Navigation/DE/Home/home.html) and aimed to enable a deterministic analysis of a ship’s energy demand based on environmental and physical conditions. It sensibly delineates the energy demands of various sources to provide tools for an energy optimized ship routing and management. This leads to suggested routing alternatives, speed and trim adjustments or additional services on the ship hull.

MariGeoRoute was a subproject addressing the challenges related to needs arising from the various data demands, such as nautical maps, weather records and forecasts ranging from wind and temperature to wave heights and currents. 52°North developed an integrated data store, the GeoPlatform, which provides data for on shore services as well as for the ships at sea. It sensibly subsets and preprocesses the data to reduce data load. We also developed approaches based on machine learning (ML) to model the energy demand based on the data collected and derived from the consortial partners. A routing service developed by 52°North uses the data accessible in the GeoPlatform to provide routing alternatives along the smallest energy demands under constraints of nautical limitations, ship safety and delivery schedules.

In 2024, 52°North worked intensively on finalizing the project. We focused on evaluating the Weather Routing Tool and the closely related fuel consumption model developed by our project partners, which is an integral part of the route optimization. Our team investigated two case studies based on routes traveled by one of our partner ships: 1) a traverse of the Biscay and the Mediterranean Sea in August 2023 and 2) an Atlantic traverse in January/February 2024 under rough weather conditions. The first use case was presented at the International Marine Design Conference (IMDC) in June 2024 ([https://doi.org/10.59490/imdc.2024.875](https://doi.org/10.59490/imdc.2024.875)). The second use case was chosen for the final project demonstration in May 2024 at the Hochschule Flensburg.

In preparation for the evaluation, the Weather Routing Tool underwent some technical improvements. The individual contributions of the total ship resistance (calm water resistance, additional resistances in waves and wind, frictional resistance due to hull roughness, shallow water resistance) were added separately to the output of the optimized route, allowing a more transparent and deeper interpretation of the proposed routes. The interpretability has also been enhanced by adding status codes of the consumption model, e.g. if the requested operation point is outside of the range used for model training. In addition to simply viewing these status codes, users of the tool can also decide how these situations should be considered in the route optimization. Additional improvmenents include the integration of the genetic algorithm and the combination of the genetic algorithm with the isofuel algorithm. We also extended the isofuel algorithm to allow for the simultaneous generation of multiple route suggestions, which can then be used as the initial population for the genetic algorithm.


#### Partners

[Hamburgische Schiffbau-Versuchsanstalt GmbH (HSVA)](https://www.hsva.de/)

[DST](https://www.dst-org.de/) – Entwicklungszentrum für Schiffstechnik und Transportsysteme e.V.

[Technische Universität Hamburg](https://www.tuhh.de/)
