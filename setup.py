#!/usr/bin/env python
"""
Initial project setup script.
This script:
1. Generates a new Django secret key
2. Updates environment files with the new key
3. Performs initial project setup tasks
"""
from pathlib import Path

from django.core.management.utils import get_random_secret_key


def generate_secret_key():
    """Generate a new Django secret key."""
    return get_random_secret_key()


def update_env_file(env_file, secret_key):
    """Update environment file with new secret key."""
    env_path = Path(env_file)

    if not env_path.exists():
        # If env file doesn't exist, create from template
        template_content = f"DJANGO_SECRET_KEY='{secret_key}'\n"
        env_path.write_text(template_content)
        return

    # Read existing content
    content = env_path.read_text()
    lines = content.splitlines()

    # Update or add secret key
    secret_key_found = False
    for i, line in enumerate(lines):
        if line.startswith('DJANGO_SECRET_KEY='):
            lines[i] = f"DJANGO_SECRET_KEY='{secret_key}'"
            secret_key_found = True
            break

    if not secret_key_found:
        lines.append(f"DJANGO_SECRET_KEY='{secret_key}'")

    # Write back to file
    env_path.write_text('\n'.join(lines) + '\n')


def main():
    """Run the setup process."""
    base_dir = Path(__file__).parent
    environments_dir = base_dir / 'environments'

    # Generate new secret key
    secret_key = generate_secret_key()

    # Update both local and production environment files
    update_env_file(environments_dir / 'development.env', secret_key)
    update_env_file(environments_dir / 'production.env', secret_key)

    print("✅ Generated new Django secret key")
    print("✅ Updated environment files")
    print("\n🎉 Project setup complete!")
    print("\nNext steps:")
    print("1. Run migrations")
    print("2. Create a superuser")
    print("\nSee README.md for detailed instructions.")


if __name__ == '__main__':
    main()
