from scripts import config
from scripts.helpers.buffer_helpers import *
import geopandas as gpd

def buffer_mvum_roads():
    print("Buffering mvum roads.")

    layer = "MVUM_Roads_CO_Valid"

    gdf = gpd.read_file(config.GDB_PATH, layer=layer)
    gdf = gdf.to_crs(config.BUFFER_CRS)

    gdf["geometry"] = buffer_layer(gdf, config.BUFFER_DISTANCE_ROAD_FT, cap_style="round")
    
    output_folder = config.OUTPUT_DIR / "mvum_roads_buffered"
    output_folder.mkdir(parents=True, exist_ok=True)

    output_fp = output_folder / "mvum_roads_buffered.gpkg"
    save_layer(gdf, output_fp)

    print("Saved buffered roads to:", output_fp)