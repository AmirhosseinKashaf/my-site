from mystie.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-12%up%c1ca8m5l$^5g@vdg!#dbna)mkdyz2#&*w^(hw-t&d$z^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# sites framework
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = 'static'
MEDIA_ROOT = 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'statics',
]

CSRF_COOKIE_SECURE = True