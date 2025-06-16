install-base:
	pip install -r requirements/base.txt

install-dev:
	pip install -r requirements/development.txt

install-prod:
	pip install -r requirements/production.txt

compile-base:
	pip-compile requirements/base.in --output-file requirements/base.txt

compile-dev:
	pip-compile requirements/development.in --output-file requirements/development.txt

compile-prod:
	pip-compile requirements/production.in --output-file requirements/production.txt

setup-pre-commit:
	pre-commit install
