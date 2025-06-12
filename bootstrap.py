#!/usr/bin/env python3

import os
import shutil
import subprocess
from pathlib import Path
import secrets

BASE_DIR = Path(__file__).resolve().parent
ENV_DIR = BASE_DIR / "environments"
VENV_DIR = BASE_DIR / ".venv"
REQUIREMENTS_FILE = BASE_DIR / "requirements" / "development.txt"
ENV_FILE = ENV_DIR / "development.env"
GIT_DIR = BASE_DIR / ".git"


def delete_git_folder():
    if GIT_DIR.exists():
        print("🧹 Deleting .git folder...")
        shutil.rmtree(GIT_DIR)
    else:
        print("✅ .git folder already removed.")


def generate_secret_key(length=50):
    print("🔐 Generating new Django secret key...")
    return secrets.token_urlsafe(length)


def inject_secret_key():
    print("✏️ Inserting secret key into development.env...")
    key = generate_secret_key()
    lines = ENV_FILE.read_text().splitlines()
    new_lines = []
    replaced = False

    for line in lines:
        if line.startswith("DJANGO_SECRET_KEY="):
            new_lines.append(f"DJANGO_SECRET_KEY={key}")
            replaced = True
        else:
            new_lines.append(line)

    if not replaced:
        new_lines.append(f"DJANGO_SECRET_KEY={key}")

    ENV_FILE.write_text("\n".join(new_lines) + "\n")
    print("✅ Secret key inserted.")


def create_virtualenv():
    if not VENV_DIR.exists():
        print("🐍 Creating virtual environment...")
        subprocess.check_call(["python3", "-m", "venv", str(VENV_DIR)])
    else:
        print("✅ .venv already exists.")


def upgrade_pip():
    print("📦 Upgrading pip...")
    subprocess.check_call([str(VENV_DIR / "bin" / "python"), "-m", "pip", "install", "--upgrade", "pip"])


def install_requirements():
    print("📚 Installing development requirements...")
    subprocess.check_call([str(VENV_DIR / "bin" / "pip"), "install", "-r", str(REQUIREMENTS_FILE)])


def main():
    print("🚀 Bootstrapping your Django project...\n")
    delete_git_folder()
    inject_secret_key()
    create_virtualenv()
    upgrade_pip()
    install_requirements()
    print("\n✅ Done! You're ready to code 🎉")


if __name__ == "__main__":
    main()
