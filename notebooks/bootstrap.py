import sys
from pathlib import Path

def setup_project_path():
    notebook_path = Path.cwd()
    project_root = notebook_path.parent.parent.parent
    if str(project_root) not in sys.path:
        sys.path.append(str(project_root))
