import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.tasks.buffer_mvum_roads import buffer_mvum_roads

def main():
    buffer_mvum_roads()

if __name__ == "__main__":
    main()