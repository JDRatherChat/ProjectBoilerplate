# Application definition

# Core Django apps
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for django-allauth
    'django_extensions',  # Useful for development and debugging
]

# Third-party apps
THIRD_PARTY_APPS = [
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

# Custom project apps
PROJECT_APPS = [
    'tracker.apps.TrackerConfig',
]

# Combine all apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

# allauth settings
SITE_ID = 1
## Regular accounts settings
ACCOUNT_SIGNUP_FIELDS = [
    'email*',
    'first_name',
    'last_name',
    'password1*',
    'password2*',
]
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_LOGIN_METHODS = {'email'}
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

### Social Accounts settings
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True

# Social account providers
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        'EMAIL_AUTHENTICATION': True,
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    },
}
