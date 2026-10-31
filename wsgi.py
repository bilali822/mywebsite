import sys
from pathlib import Path

# PythonAnywhere: add project dir to sys.path
project_home = Path('/home/YOURUSERNAME/portfolio')
if project_home not in [Path(p) for p in sys.path]:
    sys.path.insert(0, str(project_home))

from app import app as application
