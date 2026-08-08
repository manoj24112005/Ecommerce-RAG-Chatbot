import sys
from pathlib import Path

# Ensure project root is in Python path for Vercel Serverless environment
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.api.main import app
