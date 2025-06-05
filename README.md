# CampGIS

CampGIS is a spatial analysis tool designed to help users understand where dispersed camping is legal in Colorado. It combines public land ownership, hydrography, MVUM road access, and spatial rules into a centralized, map-based interface.

Using ArcGIS Pro/Online and Python (GeoPandas, Jupyter), CampGIS processes raw datasets to generate a confidence-based legality layer (e.g., No, Maybe, Most Likely) with supporting reasoning.

## Features

- Integrates 45GB+ of public land, hydrography, and MVUM datasets
- Applies spatial buffers, joins, and access logic to classify land by camping legality
- Includes a Python-based data processing pipeline (GeoPandas, Jupyter) to automatically clean, filter, and reproject into a shared coordinate reference system (CRS)


## Tech Stack

- ArcGIS Pro/Online
- Python, GeoPandas, Jupyter Notebooks
- Public datasets: USFS MVUM, USGS NHD, PadUS (Protected Areas Database)

## In Progress

- Implementing rule-based classification logic for legality zones
- Automating data workflows using Jupyter Notebooks and Python scripting for repeatability and scalability

## Plan Changes

For the original MVP planning, see [ProjectPlan.md](docs/ProjectPlan.md).

**Key updates**
- Focused the initial implementation on National Forests. The complexity of National Forest camping rules made it a good starting point, requiring a range of spatial operations
- Shifted towards a script-driven data workflow using Python (GeoPandas, Jupyter). This allows for easier updates, better scalability, and a deeper understanding of the geospatial data processing

