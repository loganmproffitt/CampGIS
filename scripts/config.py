import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Base project path (repo root)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Use project databases path from .env, or fall back to local "data" folder for testing
GDB_PATH = Path(os.environ["CAMPGIS_DATA"]) / "CampGIS.gdb"

# Outputs always go to local outputs/ folder
OUTPUT_DIR = PROJECT_ROOT / "outputs"

# Parameters for spatial logic
METERS_PER_FOOT = 0.3048

BUFFER_DISTANCE_ROAD_FT = 300
BUFFER_DISTANCE_ROAD_METERS = BUFFER_DISTANCE_ROAD_FT * METERS_PER_FOOT

BUFFER_DISTANCE_WATER_FT = 200
BUFFER_DISTANCE_WATER_METERS = BUFFER_DISTANCE_WATER_FT * METERS_PER_FOOT

# Projection used for spatial operations (e.g., UTM zone 13N for Colorado)
BUFFER_CRS = "EPSG:26913"
