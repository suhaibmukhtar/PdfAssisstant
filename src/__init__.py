from pathlib import Path
import sys
import os

PACKAGE_PATH = Path(__file__).parent
sys.path.append(str(PACKAGE_PATH))

print("Package path set to:", PACKAGE_PATH)