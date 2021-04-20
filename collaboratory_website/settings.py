"""
Django settings for collaboratory_website project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$up7tn!*-dw^u_y2(p)8+(6h6+mrxloi5oih)ji3n9rxqzsqma'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
CORS_ORIGIN_ALLOW_ALL = True

# Application definition
IMPORT_EXPORT_USE_TRANSACTIONS = True

INSTALLED_APPS = [
    'django_filters',
    'collaboratory_api',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'collaboratory_api.apps.CollaboratoryApiConfig',
    'rest_framework',
    'corsheaders',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', #This should be uncommented before giving the public access.
    'collaboratory_api.middle.DisableCSRFMiddleware', #This was implemented to prevent HTTP 403 errors for pilot testing purposes.
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'collaboratory_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'collaboratory_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'collaboratorydb',
    'USER':'admin',
    'PASSWORD':'admin123',
    'HOST':'localhost',
    'PORT':'',
    'CONN_MAX_AGE': 500,
    }
    # 'default': {
    # 'ENGINE': 'django.db.backends.mysql',
    # 'NAME': 'collaboratorydb',
    # 'USER': 'root',
    # 'PASSWORD': 'FIREbird*',
    # 'HOST': 'localhost',
    # 'PORT': '',
    # }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

#login & logout
LOGIN_REDIRECT_URL = "react_app"
LOGOUT_REDIRECT_URL = "landing"

# email testing server
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

#CSRF
# CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOW_HEADERS = (
#     'xsrfheadername',
#     'xsrfcookiename',
#     'content-type',
#     'X-CSRFTOKEN',
# )

# CORS_ORIGIN_WHITELIST = serverconfig.CORS_ORIGIN_WHITELIST
# CSRF_TRUSTED_ORIGINS = serverconfig.CSRF_TRUSTED_ORIGINS
# CSRF_COOKIE_NAME = "XSRF-TOKEN"

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

# Persistent Connections Heroku
import dj_database_url
#DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

#DATABASES['default'] = dj_database_url.parse('mysql://ywurffr50roni0mc:cb6s5codrfwstftx@u3r5w4ayhxzdrw87.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/g7cki1yc6hqy54a7', conn_max_age=600)

DATABASES['default'] = dj_database_url.config(
    default='mysql://ywurffr50roni0mc:cb6s5codrfwstftx@u3r5w4ayhxzdrw87.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/g7cki1yc6hqy54a7',
)