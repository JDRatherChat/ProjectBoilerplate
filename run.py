#!/usr/bin/env python
"""
Environment-aware Django management script.
Uses DJANGO_ENV + DJANGO_SETTINGS_MODULE from .env or defaults.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load .env from project root
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# Set safe fallbacks (if not already set)
os.environ.setdefault("DJANGO_ENV", "development")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


def main():
    """Run Django management commands."""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Is it installed and on your path?") from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
