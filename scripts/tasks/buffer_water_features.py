from scripts import config
from scripts.helpers.buffer_helpers import *
import geopandas as gpd

def buffer_water_flowlines():
    print("Buffering water flowlines.")
    
    layer = "Water_Flow_CO"

    gdf = gpd.read_file(config.GDB_PATH, layer=layer)
    gdf = gdf.to_crs(config.BUFFER_CRS)

    gdf = gdf.set_geometry(buffer_layer(gdf, config.BUFFER_DISTANCE_WATER_FT, cap_style="round"))

    output_folder = config.OUTPUT_DIR / "water_flowlines_buffered"
    output_folder.mkdir(parents=True, exist_ok=True)

    output_fp = output_folder / "water_flowlines_buffered.gpkg"
    save_layer(gdf, output_fp)

    print("Saved buffered roads to:", output_fp)


def buffer_water_areas():
    print("Buffering water areas.")
    
    layer = "Water_Area_CO"

    gdf = gpd.read_file(config.GDB_PATH, layer=layer)
    gdf = gdf.to_crs(config.BUFFER_CRS)

    gdf = gdf.set_geometry(buffer_layer(gdf, config.BUFFER_DISTANCE_WATER_FT, cap_style="round"))

    output_folder = config.OUTPUT_DIR / "water_areas_buffered"
    output_folder.mkdir(parents=True, exist_ok=True)

    output_fp = output_folder / "water_areas_buffered.gpkg"
    save_layer(gdf, output_fp)

    print("Saved buffered roads to:", output_fp)