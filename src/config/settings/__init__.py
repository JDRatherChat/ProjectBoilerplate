"""
Environment-aware Django settings loader.
This module dynamically loads base + environment-specific settings.
Supports: development, production, test — based on DJANGO_ENV.
"""

from pathlib import Path

from dotenv import load_dotenv

# Load .env early from project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

# Core settings shared across all environments
from .base import *
from .apps import *
from .database import *
from .mail import *
from .logging import *
from .restframework import *

# Select which overrides to apply
env = os.getenv("DJANGO_ENV", "development").lower()

if env == "production":
    from .production import *
elif env == "test":
    from .test import *
else:
    from .development import *
