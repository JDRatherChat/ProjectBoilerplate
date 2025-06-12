from setuptools import setup, find_packages
from pathlib import Path

# Read the long description from README if it exists
BASE_DIR = Path(__file__).resolve().parent
readme_path = BASE_DIR / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

setup(
    name="project_boilerplate",
    version="0.2.0",
    author="JD Gresse",
    author_email="jdgresse01@gmail.com",
    description="Reusable Django project boilerplate for rapid setup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JDRatherChat/ProjectBoilerplate",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,  # Include files from MANIFEST.in if needed
    python_requires=">=3.9",
    install_requires=[],  # Leave empty; handled by requirements/*.txt
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License"
    ],
    entry_points={
        # Optional: command-line tool hook (can wire something later)
        # "console_scripts": ["mycli=yourmodule.cli:main"]
    },
    zip_safe=False,
)
