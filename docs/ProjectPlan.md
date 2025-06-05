# MVP 1 Planning

**Goal**

Create a prototype GIS tool using ArcGIS Pro and Online to visualize public land boundaries and a new polygon-based layer indicating dispersed camping legality:
- Illegal (No)
- Maybe
- Most Likely (Yes)
  
The prototype will help campers understand where they can camp legally based on public data and spatial rules.

**MVP Scope**

Data Layers:
- Public land boundaries (e.g., USFS, BLM, State Land)
- National forests and parks
- MVUM road access data
- Hydrography Data
- Optional: Roads, topography, elevation

Derived Layer:
- Camping legality zones: polygon layer with 3 categories based on land type, access rules, proximity buffers, etc.

**Delivery Platform**
- ArcGIS Online web map
- Toggable layers
- Popups or legend for zone info

**Development Steps**

Step 1: Research Legality Rules
- Study MVUM access rules and dispersed camping guidelines by land type
- Define conditions for "illegal", "maybe", and "most likely"

Step 2: Collect Data Sets
- Land ownership (BLM, USFS, State Trust Lands)
- MVUM data (from Forest Service)
- Hydrography and roads (USGS NHD, OpenStreetMap)
- Optional: slope/elevation for erosion-sensitive zones

Step 3: Clean and Prepare Data
- Reproject all layers to a common CRS
- Clip to region of interest (e.g., Colorado or specific forest)
- Remove noise or irrelevant features (e.g., private inholdings)

Step 4: Define Logic for Legality Zones
- Write clear rules:
  - e.g., USFS land AND 300+ ft from water AND near MVUM road -> "Most Likely"
  - Within 300 ft of water OR ambiguous access -> "Maybe"
  - Private land or explicitly restricted -> "No"
 
Step 5: Generate Zones
- Use ArcPy, ArcGIS ModelBuilder, or manual overlay
- Output: a polygon layer with legality classification

Step 6: Build Web Map
- Upload reference layers and generated legality layer
- Configure symbology and labels
- Add layer toggles and optional popups or legends

**Long Term Goals (Post MVP)**
- QGIS / offline version
- Standalone backend service that can be plugged into any mapping tool
- Separate frontend interface integrated with backend

