import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Base project path
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Project GDB location for accessing data
GDB_PATH = Path(os.environ["CAMPGIS_DATA"]) / "CampGIS.gdb"
RAW_DATA_PATH = Path(os.environ["RAW_DATA"])

# Output directory
OUTPUT_DIR = PROJECT_ROOT / "outputs"

# Buffering parameters
METERS_PER_FOOT = 0.3048

BUFFER_DISTANCE_ROAD_FT = 300
BUFFER_DISTANCE_ROAD_METERS = BUFFER_DISTANCE_ROAD_FT * METERS_PER_FOOT

BUFFER_DISTANCE_WATER_FT = 200
BUFFER_DISTANCE_WATER_METERS = BUFFER_DISTANCE_WATER_FT * METERS_PER_FOOT

BUFFER_DISTANCE_STATE_BOUNDARY_FT = 300
BUFFER_DISTANCE_STATE_BOUNDARY_METERS = BUFFER_DISTANCE_STATE_BOUNDARY_FT * METERS_PER_FOOT

# Projection
BUFFER_CRS = "EPSG:26913"
