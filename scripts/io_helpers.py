import geopandas as gpd
import shutil
from scripts import data_config as dc
from scripts import config as cfg

def read_raw_layer(name):
    return gpd.read_file(dc.RAW_FILES[name])

def read_interim_layer(name):
    """Load a layer by name from the data registry."""
    return gpd.read_file(dc.DATA_FILES[name])

def export_interim(gdf, name, driver="GPKG", verbose=True):
    """
    Save layer to interim, and if it's marked for display,
    also save to processed in DEFAULT_CRS.
    """
    interim_path = dc.DATA_FILES[name]
    gdf.to_file(interim_path, driver=driver)
    if verbose:
        print(f"Saved to interim: {interim_path}")

    if name in dc.DISPLAY_LAYERS:
        # Convert to default CRS before exporting for display
        gdf_display = gdf.to_crs(cfg.DEFAULT_CRS)
        processed_path = cfg.PROCESSED_PATH / interim_path.name
        gdf_display.to_file(processed_path, driver=driver)
        if verbose:
            print(f"Also saved to processed: {processed_path}")
