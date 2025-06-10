"""
Test settings - used when running tests.
Optimized for speed and reproducibility.
"""

from .base import *  # noqa

# ----------------------------------------------------
# 🔐 Environment Variables (Forced for Test Stability)
# ----------------------------------------------------

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default-key")
DEBUG = False
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# ----------------------------------------------------
# 🛢 In-Memory SQLite DB
# ----------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# ----------------------------------------------------
# 📬 Email Backend
# ----------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# ----------------------------------------------------
# 🔐 Password Hashing (Fast)
# ----------------------------------------------------

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# ----------------------------------------------------
# ⚡️ In-Memory Cache
# ----------------------------------------------------

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
    }
}


# ----------------------------------------------------
# 🚫 Disable Migrations
# ----------------------------------------------------

class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


MIGRATION_MODULES = DisableMigrations()

# ----------------------------------------------------
# 🐇 Celery (Run tasks eagerly)
# ----------------------------------------------------

CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# ----------------------------------------------------
# 🧪 In-Memory File Storage
# ----------------------------------------------------

DEFAULT_FILE_STORAGE = 'django.core.files.storage.InMemoryStorage'

# ----------------------------------------------------
# 🔓 Disable CSRF in Tests
# ----------------------------------------------------

MIDDLEWARE = [
    middleware for middleware in MIDDLEWARE  # noqa: F405
    if middleware != 'django.middleware.csrf.CsrfViewMiddleware'
]

# ----------------------------------------------------
# 🪵 Silent Logging During Tests
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

# Use this temporarily if you're trying to debug tests or want visibility during dev.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'root': {
#         'handlers': ['console'],
#         'level': 'DEBUG',
#     },
# }
