import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.tasks.buffer_mvum_roads import buffer_mvum_roads
from scripts.tasks.buffer_water_features import *

def main():
    buffer_mvum_roads()
    buffer_water_flowlines()
    buffer_water_areas()

if __name__ == "__main__":
    main()