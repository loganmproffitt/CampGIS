"""
def setup_project_path():
    notebook_path = Path.cwd()
    project_root = notebook_path.parent.parent.parent
    if str(project_root) not in sys.path:
        sys.path.append(str(project_root))
"""

import sys
from pathlib import Path

def find_project_root(markers=("scripts", ".git", "README.md")):
    """Walk upward from CWD until a known root marker is found."""
    current = Path.cwd()
    for parent in [current] + list(current.parents):
        if any((parent / marker).exists() for marker in markers):
            return parent
    raise FileNotFoundError(f"Project root not found using markers: {markers}")

def setup_project_path():
    project_root = find_project_root()
    if str(project_root) not in sys.path:
        sys.path.append(str(project_root))
