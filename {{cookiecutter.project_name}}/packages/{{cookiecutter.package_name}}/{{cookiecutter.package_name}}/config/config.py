from pathlib import Path
from typing import List, Optional

from pydantic import BaseModel
from strictyaml import YAML, load
import datetime as dt

import {{cookiecutter.package_name}}

# DIRECTORY PATHS
"""
This section defines the directory structure for consistent 
use in modules across the package.
"""

TODAY = dt.datetime.today().strftime("%Y-%m-%d")

#PACKAGE_ROOT = pathlib.Path().resolve()
PACKAGE_ROOT = Path({{cookiecutter.package_name}}.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
INPUT_DIR = f"{PACKAGE_ROOT}/input"
OUTPUT_DIR = f"{PACKAGE_ROOT}/output"
CONFIG_FILE_PATH = ROOT/"config.yml"
