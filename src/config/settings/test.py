"""
Test settings — optimized for speed and reproducibility.
"""

from .base import *  # noqa

import os

# ----------------------------------------------------
# 🔐 Environment Variables
# ----------------------------------------------------

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default-key")
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# ----------------------------------------------------
# 🧪 Database — in-memory SQLite
# ----------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# ----------------------------------------------------
# 📬 Email — no real emails sent
# ----------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# ----------------------------------------------------
# 🔒 Security Middleware Relaxed
# ----------------------------------------------------

MIDDLEWARE = [
    mw for mw in MIDDLEWARE  # noqa: F405
    if mw != 'django.middleware.csrf.CsrfViewMiddleware'
]

# ----------------------------------------------------
# 🧠 Optimizations for Testing
# ----------------------------------------------------

# Fast password hasher for speed
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]


# Disable migrations
class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


MIGRATION_MODULES = DisableMigrations()

# Celery eager mode (sync)
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# In-memory file storage
DEFAULT_FILE_STORAGE = 'django.core.files.storage.InMemoryStorage'

# ----------------------------------------------------
# 🪵 Logging — silence output
# ----------------------------------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'root': {
        'handlers': ['null'],
        'level': 'CRITICAL',
    },
}
