# 🧰 Developer Guide

Welcome to the PB Boilerplate (v1.4+)! This guide will help you get up and running fast.

---

## 📦 Requirements & Dependency Management

We use `pip-tools` for clean and pinned dependencies.

### Edit `.in` files:
- `requirements/base.in`
- `requirements/development.in`
- `requirements/production.in`

### Compile `.txt` files:
```bash
make compile-base
make compile-dev
make compile-prod
```

### Install Dependencies:
```bash
make install-dev
```

---

## ✅ Pre-commit Hooks

We use [`pre-commit`](https://pre-commit.com/) to ensure code quality before committing.

### Set up once:
```bash
make setup-pre-commit
```

### Hooks included:
- `black` – code formatting
- `ruff` – linting
- `mypy` – static typing
- `check-yaml`, `trailing-whitespace`, etc.
- Local hook for `pip-compile` check before git push

---

## 🔁 Automation

### 1. Auto-compile requirements on save
```bash
python tools/watch_in_compile.py
```

### 2. Auto-compile on push
Handled via `.pre-commit-config.yaml` using a local pre-push hook.

---

## 🛠️ Makefile Commands

| Command              | Purpose                         |
|----------------------|----------------------------------|
| `make install-dev`   | Install dev dependencies         |
| `make compile-dev`   | Lock `development.txt`           |
| `make setup-pre-commit` | Enable git pre-commit hooks  |
| `make install-prod`  | Install production dependencies  |

