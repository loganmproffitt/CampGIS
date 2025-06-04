from scripts import config
from scripts.helpers.buffer_helpers import *
import geopandas as gpd

def buffer_water_flowlines():
    print("Buffering water flowlines.")
    
    layer = "Water_Flow_CO"

    gdf = gpd.read_file(config.GDB_PATH, layer=layer)
    gdf = gdf.to_crs(config.BUFFER_CRS)
    gdf = gdf[gdf.geometry.notnull() & gdf.geometry.is_valid]

    gdf = gdf[["geometry", "permanent_Identifier", "streamorde", "flowdir", "Shape_Length"]]
    gdf["permanent_Identifier"] = gdf["permanent_Identifier"].astype(str)
    gdf["streamorde"] = gdf["streamorde"].astype("Int64")  # Nullable int


    gdf = gdf.set_geometry(buffer_layer(gdf, config.BUFFER_DISTANCE_WATER_FT, cap_style="round"))
    gdf = gdf[~gdf.geometry.is_empty & gdf.geometry.is_valid] # Check for invalid geometries
    gdf["geometry"] = gdf["geometry"].buffer(0)
    gdf["geometry"] = gdf["geometry"].simplify(tolerance=1)

    output_folder = config.OUTPUT_DIR / "water_flowlines_buffered"
    output_folder.mkdir(parents=True, exist_ok=True)

    output_fp = output_folder / "water_flowlines_buffered.gpkg"
    save_layer(gdf, output_fp)

    print("Saved buffered flowlines to:", output_fp)


def buffer_water_areas():
    print("Buffering water areas.")
    
    layer = "Water_Area_CO"

    gdf = gpd.read_file(config.GDB_PATH, layer=layer)
    gdf = gdf.to_crs(config.BUFFER_CRS)
    gdf = gdf[["geometry", "permanent_identifier", "fcode", "Shape_Area"]]

    gdf = gdf.set_geometry(buffer_layer(gdf, config.BUFFER_DISTANCE_WATER_FT, cap_style="round"))
    gdf = gdf[~gdf.geometry.is_empty & gdf.geometry.is_valid] # Check for invalid geometries
    gdf["geometry"] = gdf["geometry"].buffer(0)
    gdf["geometry"] = gdf["geometry"].simplify(tolerance=1)



    output_folder = config.OUTPUT_DIR / "water_areas_buffered"
    output_folder.mkdir(parents=True, exist_ok=True)

    output_fp = output_folder / "water_areas_buffered.gpkg"
    save_layer(gdf, output_fp)

    print("Saved buffered water areas to:", output_fp)