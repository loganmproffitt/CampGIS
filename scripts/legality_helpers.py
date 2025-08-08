import geopandas as gpd
from datetime import datetime
from scripts.io_helpers import read_interim_layer
import pandas as pd

def tag_legality(
    gdf: gpd.GeoDataFrame,
    legality: str,
    reasoning: str,
    land_owner: str,
    last_updated: str = None
) -> gpd.GeoDataFrame:
    """
    Tags a GeoDataFrame with legality metadata using the centralized legality schema.

    Parameters:
    - gdf: Input GeoDataFrame (must have geometry)
    - legality: 'illegal', 'maybe legal', or 'legal'
    - reasoning: Explanation string
    - land_owner: 'USFS', 'BLM', etc.
    - last_updated: Optional override for timestamp

    Returns:
    - GeoDataFrame matching the legality schema with metadata applied
    """

    # Load column structure from legality schema in interim
    schema = read_interim_layer("legality_schema")
    schema_columns = schema.columns

    # Create a tagged copy
    tagged = gdf.copy()
    tagged["legality"] = legality
    tagged["reasoning"] = reasoning
    tagged["land_owner"] = land_owner
    tagged["last_updated"] = last_updated or datetime.utcnow().strftime("%Y-%m-%d")

    # Filter to the correct schema structure
    tagged = tagged[[col for col in schema_columns if col in tagged.columns]]

    return tagged



def merge_legality_layers(layers: list[gpd.GeoDataFrame]) -> gpd.GeoDataFrame:
    """
    Merge multiple legality-tagged GeoDataFrames into one.
    Assumes all inputs follow the legality schema.

    Parameters:
    - layers: list of GeoDataFrames (same CRS and schema)

    Returns:
    - A single merged GeoDataFrame
    """
    if not layers:
        raise ValueError("No layers provided to merge.")
    
    crs = layers[0].crs
    merged = pd.concat(layers, ignore_index=True)
    return gpd.GeoDataFrame(merged, geometry="geometry", crs=crs)
