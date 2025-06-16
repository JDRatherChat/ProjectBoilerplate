# Django Project Boilerplate

A clean, opinionated Django project scaffold for rapid development — includes:

- Modular `settings/` structure (dev, prod, test)
- Docker and `docker-compose` support
- Environment-based config loading (`.env`)
- DRF and custom app layout (`apps/`)
- Logging config
- Local automation via `bootstrap.py`
- Clean packaging with `setup.py`, `setup.cfg`, and `pyproject.toml`

---

## 🚀 Quickstart

```bash
git clone https://github.com/JDRatherChat/ProjectBoilerplate
cd my-django-boilerplate
python bootstrap.py
````

This will:

* Delete the `.git` folder (so you can re-init your own repo)
* Generate a new Django secret key
* Create a `.venv` and install all dev dependencies

---

## 🔧 Project Structure

```txt
.
├── src/
│   ├── config/            # Django settings, URLs, WSGI/ASGI
│   ├── apps/              # Your reusable Django apps
│   ├── templates/         # Global templates
│   ├── logs/              # Default log folder
├── environments/          # .env files for dev, prod, test
├── requirements/          # Separate pip files
├── bootstrap.py           # Local project setup script
├── setup.py / setup.cfg   # Packaging metadata
├── pyproject.toml         # PEP 518 support
├── docker-compose.yml     # For local dev or containerization
└── README.md
```

---

## 🧪 Running Tests

```bash
.venv/bin/python -m pytest
```

Or with Make:

```bash
make test
```

---

## 🧼 Code Quality

Format with `black` and `isort`, lint with `flake8`:

```bash
make lint
```

---

## 🐳 Docker Support

If you're using Docker:

```bash
docker-compose build
docker-compose up
```

Update your `DJANGO_ENV` and `DJANGO_SECRET_KEY` in `environments/production.env` accordingly.

---

## 🔄 GitHub Actions

Basic CI pipeline included in `.github/workflows/ci.yaml`:

* Python install
* Dev dependencies
* Run tests with `pytest`

---

## 🧠 License

MIT – use freely, modify as needed.

---

## 🙌 Credits

Built by JD Gresse with ❤️ using Django, Python, and some battle-tested dev experience.

```


## 🧰 Development Setup (v1.3+)

### 🗂 Dependency Management

We use [`pip-tools`](https://github.com/jazzband/pip-tools) for clean, reproducible dependency management. Edit the `requirements/*.in` files and run:

```bash
make compile-dev  # or compile-base / compile-prod
```

Then install:

```bash
make install-dev
```

### ✅ Pre-commit Hooks

Set up automated formatting and linting before each commit:

```bash
make setup-pre-commit
```

This enables hooks like `black`, `ruff`, and `mypy` to run on staged files.

### 🛠️ Makefile Shortcuts

Use `make` commands for quick setup:

- `make install-dev`: Install dev dependencies
- `make compile-dev`: Compile `.in` → `.txt`
- `make setup-pre-commit`: Enable pre-commit


### 🔁 Optional Automation

#### Auto-compile on Save
You can run a background script that watches `.in` files for changes and auto-compiles them:

```bash
python tools/watch_in_compile.py
```

Make sure `watchdog` is installed (`pip install watchdog` or `make install-dev` if in dev.txt).

#### Auto-compile on Git Push
We use a local pre-commit hook that checks and compiles `.txt` files before pushing:

```bash
make setup-pre-commit
```

This runs `make compile-*` before every `git push`.
