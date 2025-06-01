import sys
from pathlib import Path
import fiona

# Add repo root to Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts import config
import geopandas as gpd

def main():
    gdb_path = config.GDB_PATH
    layer_name = "MVUM_Roads_CO_Valid"

    print(f"Reading {layer_name} from {gdb_path}")
    print("Available layers:", fiona.listlayers(gdb_path))

    gdf = gpd.read_file(gdb_path, layer=layer_name)
    gdf = gdf.to_crs(config.BUFFER_CRS)

    print("CRS:", gdf.crs)
    print("Columns:", gdf.columns.tolist())
    print(gdf.head())

if __name__ == "__main__":
    main()