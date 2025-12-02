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

    # Pick extension based on driver
    ext = ".gpkg" if driver == "GPKG" else ".shp"

    # Build interim path with correct extension
    base_path = dc.DATA_FILES[name]
    interim_path = base_path.with_suffix(ext)

    # Ensure parent directory exists
    interim_path.parent.mkdir(parents=True, exist_ok=True)

    # Save interim file
    gdf.to_file(interim_path, driver=driver)
    if verbose:
        print(f"Saved to interim: {interim_path}")

    # If marked for display, export to processed folder in DEFAULT_CRS
    if name in dc.DISPLAY_LAYERS:
        gdf_display = gdf.to_crs(cfg.DEFAULT_CRS)

        processed_path = cfg.PROCESSED_PATH / interim_path.name
        processed_path.parent.mkdir(parents=True, exist_ok=True)

        gdf_display.to_file(processed_path, driver=driver)
        if verbose:
            print(f"Also saved to processed: {processed_path}")

from pathlib import Path

def get_project_root(marker_file="scripts/config.py"):
    """Walk up parent directories until marker file is found."""
    path = Path.cwd()
    while not (path / marker_file).exists():
        if path.parent == path:
            raise FileNotFoundError(f"Could not find project root using marker {marker_file}")
        path = path.parent
    return path