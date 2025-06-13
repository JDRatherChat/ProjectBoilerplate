"""
Production settings — optimized for security, performance, and scalability.
"""

import os
import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from . import REST_FRAMEWORK
from .apps import *
from .base import *  # noqa
from .base import MIDDLEWARE

env = environ.Env()

# ----------------------------------------------------
# 🔐 Secrets & Allowed Hosts
# ----------------------------------------------------

SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["example.com"])

# ----------------------------------------------------
# 🧱 Database (PostgreSQL / Supabase / etc.)
# ----------------------------------------------------

DATABASES = {
    'default': env.db('DATABASE_URL'),
}
DATABASES['default']['CONN_MAX_AGE'] = env.int('DATABASE_CONN_MAX_AGE', default=60)

# ----------------------------------------------------
# 📦 Redis Cache
# ----------------------------------------------------

CACHES = {
    'default': env.cache('REDIS_URL'),
}

# ----------------------------------------------------
# 📬 Email
# ----------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

# ----------------------------------------------------
# 🛡️ Security Middleware
# ----------------------------------------------------

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

# ----------------------------------------------------
# 🧊 Middleware & WhiteNoise Static Files
# ----------------------------------------------------

MIDDLEWARE = [
                 'django.middleware.security.SecurityMiddleware',
                 'django.middleware.cache.UpdateCacheMiddleware',
                 'whitenoise.middleware.WhiteNoiseMiddleware',
             ] + MIDDLEWARE + [
                 'django.middleware.cache.FetchFromCacheMiddleware',
             ]

# ----------------------------------------------------
# ☁️ AWS S3 Static/Media File Storage
# ----------------------------------------------------

INSTALLED_APPS += ['storages']

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN', default=None)

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/' if AWS_S3_CUSTOM_DOMAIN else f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/' if AWS_S3_CUSTOM_DOMAIN else f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/'

# ----------------------------------------------------
# 📈 Sentry Error Tracking
# ----------------------------------------------------

sentry_sdk.init(
    dsn=env('SENTRY_DSN'),
    integrations=[DjangoIntegration()],
    environment=env('SENTRY_ENVIRONMENT', default='production'),
    traces_sample_rate=env.float('SENTRY_TRACES_SAMPLE_RATE', default=0.2),
    send_default_pii=True,
)

# ----------------------------------------------------
# 🪵 Logging
# ----------------------------------------------------

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": env("DJANGO_LOG_LEVEL", default="INFO"),
            "propagate": False,
        },
    },
}

# ----------------------------------------------------
# 🚦 API Throttling
# ----------------------------------------------------

REST_FRAMEWORK.update({
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle"
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "100/day",
        "user": "1000/day"
    }
})

# ----------------------------------------------------
# 🚀 Template Caching
# ----------------------------------------------------

TEMPLATES[0]['OPTIONS']['loaders'] = [  # noqa: F405
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]
