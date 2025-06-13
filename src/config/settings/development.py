"""
Local development settings.
"""

from .apps import *
from .base import *  # noqa
from .base import BASE_DIR

import os
import socket

# ----------------------------------------------------
# 🔐 Environment Variables
# ----------------------------------------------------

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default-key")
DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# ----------------------------------------------------
# 🛢 Database — SQLite for local dev
# ----------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ----------------------------------------------------
# 📬 Email Backend — console
# ----------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ----------------------------------------------------
# 🧰 Dev Tools & Middleware
# ----------------------------------------------------

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]  # noqa: F405

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']  # noqa: F405

INTERNAL_IPS = ['127.0.0.1']

# Optional: Docker support
try:
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [ip[: ip.rfind(".")] + ".1" for ip in ips]
except Exception:
    pass

# ----------------------------------------------------
# 🔓 Relaxed Security Settings
# ----------------------------------------------------

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

# ----------------------------------------------------
# 🪵 Logging — console only
# ----------------------------------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

# ----------------------------------------------------
# ⚡️ Cache — local memory
# ----------------------------------------------------

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
