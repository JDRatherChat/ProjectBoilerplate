# """
# Django settings for src project.
#
# """
# # Import all modular settings
# from .apps import *
# from .database import *
# from .environments import *
# from .logging import *
# from .mail import *
# from .restframework import *
#
# import sys
#
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# # Add src directory to Python path
# sys.path.append(str(BASE_DIR / "src"))
#
# # Default primary key field type
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "whitenoise.middleware.WhiteNoiseMiddleware",  # Static files
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
#     "django.middleware.locale.LocaleMiddleware",  # Internationalization
#     "allauth.account.middleware.AccountMiddleware",  # django-allauth middleware
# ]
#
# # Security Middleware Settings
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# X_FRAME_OPTIONS = "DENY"
#
# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [BASE_DIR / "src" / "templates"],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#                 "django.template.context_processors.i18n",  # Internationalization
#             ],
#         },
#     },
# ]
#
# ROOT_URLCONF = 'config.urls'
#
# WSGI_APPLICATION = "config.wsgi.application"
#
# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
# # Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'Africa/Johannesburg'
# USE_I18N = True
# USE_TZ = True
#
# # Static files (CSS, JavaScript, Images)
# STATIC_URL = "/static/"
# STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_DIRS = [BASE_DIR / "src" / "static"]
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
#
# # Media files
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'src/media')
#
# # Authentication
# AUTHENTICATION_BACKENDS = [
#     "django.contrib.auth.backends.ModelBackend",
#     "allauth.account.auth_backends.AuthenticationBackend",
# ]
#
# # django-allauth settings
# SITE_ID = 1
# ACCOUNT_AUTHENTICATION_METHOD = "email"
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
# ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
# ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
# ACCOUNT_SESSION_REMEMBER = True
#
# # Social account providers
# SOCIALACCOUNT_PROVIDERS = {
#     "google": {
#         "SCOPE": [
#             "profile",
#             "email",
#         ],
#         "AUTH_PARAMS": {
#             "access_type": "online",
#         },
#     },
# }
#
# # Login/Logout URLs
# LOGIN_URL = "account_login"
# LOGIN_REDIRECT_URL = "/"
# LOGOUT_REDIRECT_URL = "/"
#
# # Crispy Forms
# CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
# CRISPY_TEMPLATE_PACK = "bootstrap5"
#
