from settings.base import *

env = os.environ.get("DJANGO_ENV")

if env == "production":
    from settings.production import *
elif env == "test":
    from settings.test import *
else:
    # Default to development
    from settings.development import *
