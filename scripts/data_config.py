from .config import RAW_DATA_PATH, INTERIM_PATH, PROCESSED_PATH

RAW_FILES = {
    "state_boundary_raw": RAW_DATA_PATH / "tl_2024_us_state" / "tl_2024_us_state.shp",
    "nhd_waterbody": RAW_DATA_PATH / "NHDPlus" / "NHDWaterbody",
    "nhd_area": RAW_DATA_PATH / "NHDPlus" / "NHDArea",
    "mvum_roads": RAW_DATA_PATH / "mvum" / "mvum_roads.shp",
}

# Centralized file paths
DATA_FILES = {
    "state_boundary_buffered": INTERIM_PATH / "state_boundary_buffered.gpkg",
    "hydro_polygon_clean": INTERIM_PATH / "hydro_polygon_clean.gpkg",
    "flowline_clean": INTERIM_PATH / "flowline_clean.gpkg",
    "mvum_clean": INTERIM_PATH / "mvum_clean.gpkg",
    "ownership_clean": INTERIM_PATH / "ownership_clean.gpkg",
}

# Buffer settings (in feet)
BUFFER_SETTINGS_FT = {
    "road": 300,
    "water": 200,
    "state_boundary": 300
}

# Convert to meters
BUFFER_SETTINGS_METERS = {
    k: v * 0.3048 for k, v in BUFFER_SETTINGS_FT.items()
}

# Files to to display in ArcGIS — copied to "processed" folder in last step
DISPLAY_LAYERS = [
    "hydro_polygon_clean",
    "flowline_clean",
    "mvum_clean",
    "ownership_clean",
    "legality_mask"
]
