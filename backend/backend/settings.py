import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# 🎯 Détection environnement Railway
RAILWAY_ENVIRONMENT = os.environ.get('RAILWAY_ENVIRONMENT_NAME') is not None
IS_PRODUCTION = 'DATABASE_URL' in os.environ or RAILWAY_ENVIRONMENT

if IS_PRODUCTION:
    # 🚀 PRODUCTION Railway
    DEBUG = False
    ALLOWED_HOSTS = ['.railway.app']

    import dj_database_url

    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
    print("🚀 PRODUCTION: Using Railway PostgreSQL")

else:
    # 🏠 LOCAL Development
    DEBUG = True
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'gestion_stock_it',
            'USER': 'postgres',
            'PASSWORD': 'OnibaJ5zWy&0df',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    print("🏠 LOCAL: Using local PostgreSQL")

# Vos autres settings...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'djoser',
    'stock',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'
WSGI_APPLICATION = 'backend.wsgi.application'

# CORS configuration
if IS_PRODUCTION:
    CORS_ALLOWED_ORIGINS = [
        "https://your-app.vercel.app",  # À changer après déploiement Vercel
    ]
else:
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",
    ]
    CORS_ALLOW_ALL_ORIGINS = True  # Pour le développement

# Reste de votre config...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}