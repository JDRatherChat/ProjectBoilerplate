.PHONY: bootstrap test lint

bootstrap:
python bootstrap.py

test:
.venv/bin/python -m pytest

lint:
.venv/bin/flake8 src tests

compile:
pip-compile requirements/requirements.in -o requirements/base.txt
