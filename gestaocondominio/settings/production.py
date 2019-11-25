from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pqcz=a(v(s%g#2(@$p9a+xrivqgeeqc+1x&g%qy!p-a1cd+y&n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}
