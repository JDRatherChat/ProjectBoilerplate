#!/usr/bin/env python
"""
Entry point for Django management commands.

Loads environment variables and sets up the correct settings module.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Set base directory two levels up from this file (i.e., project root)
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from `.env` at the project root
load_dotenv(BASE_DIR / "environments" / f"{os.getenv('DJANGO_ENV', 'development')}.env")

# Fallbacks: if env variables aren't loaded, default to development
os.environ.setdefault("DJANGO_ENV", "development")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"config.settings.{os.getenv('DJANGO_ENV', 'development')}")


def main():
    """Run administrative Django tasks."""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and your virtual environment is active."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
