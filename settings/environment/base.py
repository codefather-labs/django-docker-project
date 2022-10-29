from settings.logger import system_message

"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.contrib.staticfiles.utils import check_settings as check_django_settings
from corsheaders.checks import check_settings as check_cors_settings

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SITE_ID = 1
ADMIN_ROUTER_ENABLED = True
ADMIN_ROUTE = 'admin/'
PROTOCOL = 'http'

# A dictionary of urlconf module paths, keyed by their subdomain.
SUBDOMAIN_URLCONFS = {
    None: 'settings.urls',  # no subdomain, e.g. ``example.com``
    # 'www': 'settings.urls',
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# Application definition
PRE_ADMIN_APPS = []
ROOT_APPS = [
    'apps.core',
]
INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',
    'drf_yasg',
    'subdomains',
    'robots',
]

INSTALLED_APPS = [
    *PRE_ADMIN_APPS,
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    *INSTALLED_APPS,
    *ROOT_APPS
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'subdomains.middleware.SubdomainURLRoutingMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

ROOT_URLCONF = 'settings.urls'

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
                # 'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'
ASGI_APPLICATION = 'settings.asgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST_FRAMEWORK
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
}

# CORS Settings
# ------------------------------------------------------------------------------
X_FRAME_OPTIONS = 'SAMEORIGIN'
CSRF_COOKIE_SAMESITE = None
CSRF_COOKIE_HTTPONLY = False
CSRF_USE_SESSIONS = True
CORS_ALLOW_ALL_ORIGINS = bool(int(os.environ.get("CORS_ALLOW_ALL_ORIGINS", '1')))
CORS_ORIGIN_ALLOW_ALL = bool(int(os.environ.get("CORS_ORIGIN_ALLOW_ALL", '1')))
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'cache-control',
    'x-signature',
    'x-frame-options',
    "Access-Control-Allow-Origin",
    "Access-Control-Allow-Methods",
    "Access-Control-Max-Age",
    "Access-Control-Allow-Headers",
]

# SEO Settings
# ------------------------------------------------------------------------------
SEO_URLS_AUTODISCOVER = True
SEO_AUTODISCOVER_CONFIG = {
    "models": [
        {
            "path": "apps.core",
            "queryset_params": {}
        }
    ]
}
SEO_SITEMAPS_ARTICLE_PAGINATE_BY = 50

# ROBOTS_USE_SITEMAP = False

ROBOTS_SITEMAP_URLS = [
    'http://0.0.0.0:8000/sitemap.xml',
]
ROBOTS_SITEMAP_VIEW_NAME = 'django.contrib.sitemaps.views.sitemap'
ROBOTS_CACHE_TIMEOUT = int(os.environ.get("ROBOTS_CACHE_TIMEOUT", "18000"))
