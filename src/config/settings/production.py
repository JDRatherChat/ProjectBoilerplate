"""
Production settings for Django project.
Optimized for security and performance.
"""

import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .apps import *
from .base import *  # noqa
from .base import MIDDLEWARE

# ----------------------------------------------------
# ✅ Core Environment Settings
# ----------------------------------------------------

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-fallback-key")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# ----------------------------------------------------
# 🔐 Security Headers
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
# 🛢 Database via DATABASE_URL
# ----------------------------------------------------

DATABASES = {
    'default': dj_database_url.parse(os.getenv("DATABASE_URL"))
}
DATABASES['default']['CONN_MAX_AGE'] = int(os.getenv("DATABASE_CONN_MAX_AGE", 60))

# ----------------------------------------------------
# 🚀 Caching via Redis
# ----------------------------------------------------

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.getenv("REDIS_URL", "redis://127.0.0.1:6379/1"),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# ----------------------------------------------------
# 📬 Email Configuration
# ----------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

# ----------------------------------------------------
# 📦 Static & Media Storage via S3
# ----------------------------------------------------

INSTALLED_APPS += ['storages']

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_S3_CUSTOM_DOMAIN = os.getenv("AWS_S3_CUSTOM_DOMAIN")

# Static Files
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/' if AWS_S3_CUSTOM_DOMAIN else f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/'

# Media Files
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/' if AWS_S3_CUSTOM_DOMAIN else f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/'

# ----------------------------------------------------
# 🔐 Secure Middleware Stack
# ----------------------------------------------------

MIDDLEWARE = [
                 'django.middleware.security.SecurityMiddleware',
                 'django.middleware.cache.UpdateCacheMiddleware',
                 'whitenoise.middleware.WhiteNoiseMiddleware',
             ] + MIDDLEWARE + [
                 'django.middleware.cache.FetchFromCacheMiddleware',
             ]

# ----------------------------------------------------
# 📊 Sentry Integration
# ----------------------------------------------------

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
    environment=os.getenv("SENTRY_ENVIRONMENT", "production"),
    traces_sample_rate=float(os.getenv("SENTRY_TRACES_SAMPLE_RATE", 0.2)),
    send_default_pii=True,
)

# ----------------------------------------------------
# 🪵 Logging
# ----------------------------------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}

# ----------------------------------------------------
# 🔒 API Throttling
# ----------------------------------------------------

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}

# ----------------------------------------------------
# ⚡️ Template Caching
# ----------------------------------------------------

TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]
