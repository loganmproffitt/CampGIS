from shapely.geometry import LineString, MultiLineString, Polygon, MultiPolygon
import geopandas as gpd

def drop_missing_geometry(gdf):
    """Drop rows with null geometries."""
    return gdf[~gdf.geometry.isna()].copy()

def to_multilinestring(gdf):
    """Convert LineString to MultiLineString."""
    def convert(geom):
        if isinstance(geom, LineString):
            return MultiLineString([geom])
        return geom
    gdf = gdf.copy()
    gdf["geometry"] = gdf.geometry.apply(convert)
    return gdf

def to_multipolygon(gdf):
    """Convert Polygon to MultiPolygon."""
    def convert(geom):
        if isinstance(geom, Polygon):
            return MultiPolygon([geom])
        return geom
    gdf = gdf.copy()
    gdf["geometry"] = gdf.geometry.apply(convert)
    return gdf

def validate_geometry(gdf):
    """Remove invalid geometries."""
    return gdf[gdf.is_valid].copy()
