import geopandas as gpd

def buffer_layer(gdf, distance_ft, cap_style="round"):
    # Convert feet to meters
    distance_m = distance_ft * 0.3048

    cap_style_value = 1 if cap_style == "round" else 2

    return gdf.buffer(distance_m, cap_style_value)

def load_and_project(fp, crs): 
    """
        Loads a GeoDataFrame and reprojects it to a specified CRS.
    """
    gdf = gpd.read_file(fp)
    return gdf.to_crs(crs)

def save_layer(gdf, out_fp):
    gdf.to_file(out_fp)