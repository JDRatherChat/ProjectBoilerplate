#!/usr/bin/env python
"""
Environment-aware Django management script.
This script automatically sets the correct Django settings module and loads environment variables.
"""
import os
import sys
from pathlib import Path

import environ


def load_env(env_file):
    """Load environment variables from file."""
    env = environ.Env()
    env_file = Path(env_file)
    if env_file.exists():
        env.read_env(str(env_file))
    return env


def main():
    """Run Django management commands with environment awareness."""
    # Determine environment
    if len(sys.argv) > 1 and sys.argv[1] == '--prod':
        # Production mode
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
        env_file = Path(__file__).parent / 'environments' / 'production.env'
        sys.argv.pop(1)  # Remove the --prod argument
    else:
        # Development mode
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
        env_file = Path(__file__).parent / 'environments' / 'local.env'

    # Load environment variables
    env = load_env(env_file)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc

    # Execute Django command
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
