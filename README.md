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
