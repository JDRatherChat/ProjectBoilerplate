import os
import platform
import shutil
import stat
import subprocess
import secrets
from pathlib import Path

# Constants
GIT_DIR = Path(".git")
ENV_FILE = Path("environments/development.env")
EXAMPLE_ENV_FILE = Path(".env.production.example")
VENV_DIR = Path(".venv")
REQUIREMENTS_FILE = Path("requirements/development.txt")

def delete_git_folder():
    if GIT_DIR.exists():
        print("🧹 Deleting .git folder...")
        shutil.rmtree(GIT_DIR, onerror=handle_remove_readonly)
    else:
        print(">> .git folder already removed.")

def handle_remove_readonly(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def inject_secret_key():
    print(">> Inserting secret key into development.env...")
    if not ENV_FILE.exists():
        print(">> development.env not found, creating from example...")
        ENV_FILE.parent.mkdir(parents=True, exist_ok=True)
        ENV_FILE.write_text(EXAMPLE_ENV_FILE.read_text())

    lines = ENV_FILE.read_text().splitlines()
    key = generate_secret_key()
    for i, line in enumerate(lines):
        if line.startswith("SECRET_KEY="):
            lines[i] = f"SECRET_KEY={key}"
            break
    else:
        lines.append(f"SECRET_KEY={key}")
    ENV_FILE.write_text("\n".join(lines))
    print(">> Secret key inserted.")

def generate_secret_key():
    print(">> Generating new Django secret key...")
    return secrets.token_urlsafe(50)

def create_virtualenv():
    if VENV_DIR.exists():
        print(">> .venv already exists.")
    else:
        print(">> Creating virtual environment...")
        subprocess.check_call(["python", "-m", "venv", str(VENV_DIR)])

def get_venv_python():
    if platform.system() == "Windows":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"

def get_venv_pip():
    if platform.system() == "Windows":
        return VENV_DIR / "Scripts" / "pip.exe"
    return VENV_DIR / "bin" / "pip"

def upgrade_pip():
    print(">>  Upgrading pip...")
    python_path = get_venv_python()
    subprocess.check_call([str(python_path), "-m", "pip", "install", "--upgrade", "pip"])

def install_requirements():
    print(">> Installing development requirements...")
    pip_path = get_venv_pip()
    subprocess.check_call([str(pip_path), "install", "-r", str(REQUIREMENTS_FILE)])

def main():
    print(">> Bootstrapping your Django project...\n")
    delete_git_folder()
    inject_secret_key()
    create_virtualenv()
    upgrade_pip()
    install_requirements()
    print(">> Project bootstrapped successfully!")
    print(">> To activate your environment:")
    print("   .\\.venv\\Scripts\\activate" if platform.system() == "Windows" else "   source .venv/bin/activate")

if __name__ == "__main__":
    main()
