# 📘 Developer Handbook

## 🏗️ Project Structure

```
PB_V1_4/
├── requirements/       # .in and compiled .txt dependencies
├── tools/              # dev utilities like watch_in_compile.py
├── src/                # Django project source
├── .pre-commit-config.yaml
├── Makefile
├── README.md
├── DEV_GUIDE.md
└── docs/
```

---

## 🧪 Testing Tips

Use `pytest` for writing and running tests:

```bash
pytest
pytest -s -v src/tests/
```

---

## 🐳 Docker Usage

This boilerplate includes a `Dockerfile` and `docker-compose.yml` for local testing or CI. Run:

```bash
docker-compose up --build
```

---

## 📋 Environment Management

Use `.env` files in `environments/` and load via `django-environ` or `python-dotenv`.

- `development.env`
- `production.env`
- `test.env`

---

## 💡 Pro Tips

- Use `ipython` + `django-extensions` for an enhanced dev shell: `python manage.py shell_plus`
- Use `django-debug-toolbar` in `dev` for performance insights
- Always run `make compile-dev` after updating `.in` files
