"""
Environment-aware Django settings loader.
Loads shared settings and applies overrides based on DJANGO_ENV.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# -----------------------------
# 📦 Load .env early
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

# -----------------------------
# 🔧 Modular Base Imports
# -----------------------------
from .base import *
from .apps import *
from .database import *
from .logging import *
from .restframework import *

# -----------------------------
# 🌍 Environment-Specific Overrides
# -----------------------------
env = os.getenv("DJANGO_ENV", "development").lower()

if env == "production":
    from .production import *
elif env == "test":
    from .test import *
elif env == "development":
    from .development import *
else:
    raise ValueError(f"Invalid DJANGO_ENV value: {env}")
