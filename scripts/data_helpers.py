from scripts import config as cfg
import geopandas as gpd

def to_buffer_crs(gdf):
    """Project to buffer CRS."""
    return gdf.to_crs(cfg.BUFFER_CRS)

def to_default_crs(gdf):
    """Project to default display CRS."""
    return gdf.to_crs(cfg.DEFAULT_CRS)

def clean_geometry(gdf):
    """
    Fix invalid shapes.
    """
    gdf["geometry"] = gdf["geometry"].buffer(0)
    return gdf

def buffer_layer(gdf, buffer_distance_meters, dissolve=False):
    """Buffer layer by meters, with optional dissolve."""
    gdf = gdf.copy()
    gdf["geometry"] = gdf.buffer(buffer_distance_meters)
    if dissolve:
        gdf = gdf.dissolve()
    return gdf

def intersect_with_layer(gdf, clip_gdf):
    """Return intersection of two layers."""
    return gpd.overlay(gdf, clip_gdf, how="intersection")
