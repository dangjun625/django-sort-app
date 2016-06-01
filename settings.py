"""
Django settings for gards_admin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

DIRNAME = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tg9c=zs*b^uqk48t&j&@v$+0lv3!e)p+^f=4h3ecu4hsub1%9e'
DEBUG = True
TESTING = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']
SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

)

SORTED_APPS = (
    {'auth':('User', 'Group',)},
    {'proxy':('user', 'group', 'product', 'order',},
)

