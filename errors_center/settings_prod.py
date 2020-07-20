from .settings import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS.append(".herokuapp.com")

DATABASES = {
    "default": dj_database_url.config()
}

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
