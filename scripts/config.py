import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Base project path
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Data directories
RAW_DATA_PATH = Path(os.environ["RAW_DATA"]) # Specify RAW_DATA path in .env
GDB_PATH = Path(os.environ["CAMPGIS_DATA"]) / "CampGIS.gdb" # Specify CAMPGIS_DATA IN .env

DATA_DIR = PROJECT_ROOT / "data"
INTERIM_PATH = DATA_DIR / "interim"
PROCESSED_PATH = DATA_DIR / "processed"

# CRS and projection
DEFAULT_CRS = "EPSG:4326"
BUFFER_CRS = "EPSG:26913"

# Unit conversions
METERS_PER_FOOT = 0.3048
