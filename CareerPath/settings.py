"""
Django settings for CareerPath project.
"""

from pathlib import Path
import os

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# SECURITY
# =========================================================

# Secret key is taken from environment variable in production
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-development-only-key-change-this'
)

# DEBUG is True locally and should be False on Render
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Hosts allowed to access the application
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]


# =========================================================
# APPLICATIONS
# =========================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts',
    'resume',
    'career',
    'skill_analysis',
    'dashboard',
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =========================================================
# URL / WSGI
# =========================================================

ROOT_URLCONF = 'CareerPath.urls'

WSGI_APPLICATION = 'CareerPath.wsgi.application'


# =========================================================
# TEMPLATES
# =========================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / 'templates'
        ],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# =========================================================
# DATABASE
# =========================================================

# Local development: MySQL
#
# Render deployment will use environment variables
# for the production database.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',

        'NAME': os.environ.get(
            'DB_NAME',
            'careerpath_db'
        ),

        'USER': os.environ.get(
            'DB_USER',
            'root'
        ),

        'PASSWORD': os.environ.get(
            'DB_PASSWORD',
            'Tejalbhosale@2712'
        ),

        'HOST': os.environ.get(
            'DB_HOST',
            'localhost'
        ),

        'PORT': os.environ.get(
            'DB_PORT',
            '3306'
        ),
    }
}


# =========================================================
# PASSWORD VALIDATION
# =========================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# =========================================================
# INTERNATIONALIZATION
# =========================================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# =========================================================
# STATIC FILES
# =========================================================

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'


# =========================================================
# MEDIA / RESUME UPLOADS
# =========================================================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# =========================================================
# DEFAULT PRIMARY KEY
# =========================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =========================================================
# PRODUCTION SECURITY
# =========================================================

if not DEBUG:

    ALLOWED_HOSTS = [
        '.onrender.com',
    ]

    CSRF_TRUSTED_ORIGINS = [
        'https://*.onrender.com',
    ]

    SECURE_PROXY_SSL_HEADER = (
        'HTTP_X_FORWARDED_PROTO',
        'https'
    )