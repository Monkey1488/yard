import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-pt#8gdp-$n@7e^!l+jx6m5tx^jj(f7a8e$pozxmk1c^x(%@b=7'


DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "yard_db",
        'USER': "monke",
        'PASSWORD': "1488228",
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]