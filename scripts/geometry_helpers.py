from shapely.geometry import LineString, MultiLineString, Polygon, MultiPolygon

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

def strip_z_line(geom):
    """Remove Z dimension from a LineString or MultiLineString."""
    if geom.is_empty:
        return geom
    if geom.has_z:
        if isinstance(geom, LineString):
            return LineString([(x, y) for x, y, *_ in geom.coords])
        elif isinstance(geom, MultiLineString):
            return MultiLineString([
                LineString([(x, y) for x, y, *_ in line.coords])
                for line in geom.geoms
            ])
    return geom

def strip_z_polygon(geom):
    """Remove Z dimension from a Polygon or MultiPolygon."""
    if geom.is_empty:
        return geom
    if geom.has_z:
        if isinstance(geom, Polygon):
            exterior = [(x, y) for x, y, *_ in geom.exterior.coords]
            interiors = [[(x, y) for x, y, *_ in ring.coords] for ring in geom.interiors]
            return Polygon(shell=exterior, holes=interiors)
        elif isinstance(geom, MultiPolygon):
            return MultiPolygon([strip_z_polygon(poly) for poly in geom.geoms])
