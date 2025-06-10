import os
from pathlib import Path

import environ

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environ
env = environ.Env(
    # Set default values
    DEBUG=(bool, False),
    SECRET_KEY=(str, 'django-insecure-default-key-change-this'),
    ALLOWED_HOSTS=(list, ['localhost', '127.0.0.1']),
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# Allowed hosts
ALLOWED_HOSTS = env('ALLOWED_HOSTS')
