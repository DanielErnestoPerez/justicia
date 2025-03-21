"""
Django settings for justicia project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
import dj_database_url
import cloudinary
import cloudinary_storage
import cloudinary.uploader
import cloudinary.api
from pathlib import Path
from environ import Env
env = Env()
Env.read_env()
ENVIRONMENT = env('ENVIRONMENT', default='production')


if ENVIRONMENT == 'development':
    DEBUG=True
else:
    DEBUG=False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'justicia_database',
        'USER':'postgres',
        'PASSWORD':'Daniel25',
        'HOST':'localhost',
        'PORT':'5433',
    }
}
POSTGRES_LOCALLY = True
if ENVIRONMENT == 'production'or POSTGRES_LOCALLY == True:
    DATABASES['default'] = dj_database_url.parse(env('DATABASE_URL'))

ALLOWED_HOSTS = ['localhost', '127.0.0.1', env('RENDER_EXTERNAL_HOSTNAME', default='')]

CSRF_TRUSTED_ORIGINS =['https://*.onrender.com']

INTERNAL_IPS = (
    '127.0.0.1',
    'localhost:8000',
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

ENCRYPT_KEY = b'ZxLm-vhq8r5NurRsqi_wCXxTGNMscYcmPPHQcwDyBCM='

#Feature Toggle
DEVELOPER = env('DEVELOPER', default='')
STAGING = env('STAGING', default='False')



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'django.contrib.sites',
    'django_htmx',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_cleanup.apps.CleanupConfig',
    'admin_honeypot',
    'justicia_app', 
    'usuarios',
    'inbox',
    'features',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'justicia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]



WSGI_APPLICATION = 'justicia.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'

if ENVIRONMENT == 'production' or POSTGRES_LOCALLY == True:
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': env('CLOUD_NAME'),
        'API_KEY': env('CLOUD_API_KEY'),
        'API_SECRET': env('CLOUD_API_SECRET'),
    }
    
    cloudinary.config(
        cloud_name = env('CLOUD_NAME'),
        api_key = env('CLOUD_API_KEY'),
        api_secret = env('CLOUD_API_SECRET'),
        secure = True,
    )
else:
    MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


import time

# Honeypot settings
HONEYPOT_FIELD_NAME = env('HONEYPOT_FIELD_NAME', default='default_field_name')
HONEYPOT_VALUE = env('HONEYPOT_VALUE', default='default_value')
HONEYPOT_VERIFIER = env('HONEYPOT_VERIFIER', default='default_verifier')
HONEYPOT_RESPONDER = env('HONEYPOT_RESPONDER', default='default_responder')

ACCOUNT_USERNAME_BLACKLIST = env('ACCOUNT_USERNAME_BLACKLIST', default='').split(',')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_ADDRESS')
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = f'Justicia Restaurativa Cuba {env("EMAIL_ADDRESS")}'
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True