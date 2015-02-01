from prod import *

DEBUG = True
TEMPLATE_DEBUG = True
#ALLOWED_HOSTS = []

SECRET_KEY = '(jut!-c_9j^a==v$+6(-w3x7v#%*ljd7y2h0w-=*d4r@f5hy-z'


INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS.remove('storages')
INSTALLED_APPS = tuple(INSTALLED_APPS)
del STATICFILES_STORAGE
del DEFAULT_FILE_STORAGE

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

#STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, 'static'),
#)

DATABASES = {
    'default':
        {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'project.db', 'HOST': 'localhost', 'USER': '', 'PASSWORD': '', 'PORT': ''}
}
