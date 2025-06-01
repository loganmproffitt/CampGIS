from pathlib import Path

# Base paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"         # or point to Research and Data
OUTPUT_DIR = PROJECT_ROOT / "outputs"

# Parameters
BUFFER_DISTANCE_ROAD_FT = 300
BUFFER_DISTANCE_WATER_FT = 200

# CRS for buffering (UTM or state plane, not WGS84)
BUFFER_CRS = "EPSG:26913"  # NAD83 / UTM zone 13N (CO)
