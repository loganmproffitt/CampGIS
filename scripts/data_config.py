from .config import RAW_DATA_PATH, INTERIM_PATH, PROCESSED_PATH

# Raw data paths
RAW_FILES = {
    "state_boundary_raw": RAW_DATA_PATH / "tl_2024_us_state" / "tl_2024_us_state.shp",
    "land_ownership_raw": RAW_DATA_PATH / "PADUS4_1_State_CO_GDB_KMZ" / "PADUS4_1_StateCO.gdb",
    "nhd": RAW_DATA_PATH / "NHDPlus_H_National_Release_2_GDB" / "NHDPlus_H_National_Release_2.gdb",
    "mvum_raw": RAW_DATA_PATH / "Motor_Vehicle_Use_Map%3A_Roads_(Feature_Layer)" / "Motor_Vehicle_Use_Map%3A_Roads_(Feature_Layer).shp",
}

# Interim file paths
DATA_FILES = {
    "state_boundary_buffered": INTERIM_PATH / "state_boundary_buffered.gpkg",
    "water_polygon_clean": INTERIM_PATH / "water_polygon_clean.gpkg",
    "flowline_clean": INTERIM_PATH / "flowline_clean.gpkg",
    "mvum_clean": INTERIM_PATH / "mvum_clean.gpkg",
    "land_ownership_clean": INTERIM_PATH / "land_ownership_clean.gpkg",
    # Buffered
    "mvum_buffered": INTERIM_PATH / "mvum_buffered.gpkg",
    "water_flowline_buffered": INTERIM_PATH / "water_flowline_buffered.gpkg",
    "water_polygon_buffered": INTERIM_PATH / "water_polygon_buffered.gpkg",
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
    "water_polygon_clean",
    "flowline_clean",
    "mvum_clean",
    "ownership_clean",
    "legality_mask"
]
