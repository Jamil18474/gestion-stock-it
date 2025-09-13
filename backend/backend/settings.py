import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# DEBUG selon l'environnement
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.railway.app']

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

WSGI_APPLICATION = 'backend.wsgi.application'
# Debug complet
print("🔍 ALL ENVIRONMENT VARIABLES:")
for key, value in os.environ.items():
    if 'DATABASE' in key or 'POSTGRES' in key:
        print(f"   {key} = {value[:50]}...")

print(f"📊 DATABASE_URL exists: {'DATABASE_URL' in os.environ}")
print(f"📊 POSTGRES_URL exists: {'POSTGRES_URL' in os.environ}")

# Configuration base de données
if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
    print("🚀 Using Railway PostgreSQL")
elif 'POSTGRES_URL' in os.environ:  # Parfois Railway utilise POSTGRES_URL
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('POSTGRES_URL'))
    }
    print("🚀 Using Railway PostgreSQL (POSTGRES_URL)")
else:
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
    print("🏠 Using local PostgreSQL")

# CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://your-app.vercel.app",  # À changer
]

CORS_ALLOW_ALL_ORIGINS = DEBUG

# Reste de votre configuration...
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