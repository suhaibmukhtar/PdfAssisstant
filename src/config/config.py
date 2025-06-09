from pathlib import Path
import sys
import os
from datetime import datetime

PACKAGE_PATH = Path(__file__).parent.parent.parent
if os.path.exists(PACKAGE_PATH):
    os.makedirs(PACKAGE_PATH, exist_ok=True)
sys.path.append(str(PACKAGE_PATH))

LOGGING_DIR = os.path.join(PACKAGE_PATH, "logs")
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR, exist_ok=True)
    
LOGGING_FILE_PATH = os.path.join(LOGGING_DIR, datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log")
    
DATA_DIR = os.path.join(PACKAGE_PATH, "data")

VectorStorePath = os.path.join(PACKAGE_PATH,"VectorStore","faiss_index")