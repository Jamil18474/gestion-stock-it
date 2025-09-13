import os
from pathlib import Path
import logging

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


# 🛡️ Configuration base de données
def get_database_config():
    database_url = os.environ.get('DATABASE_URL')

    if database_url and database_url.startswith('postgresql://'):
        print("🚀 PRODUCTION: Using Railway PostgreSQL")
        import dj_database_url
        return {
            'default': dj_database_url.parse(database_url)
        }
    else:
        print("🏠 LOCAL: Using local PostgreSQL")
        return {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'gestion_stock_it',
                'USER': 'postgres',
                'PASSWORD': 'OnibaJ5zWy&0df',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }


DATABASES = get_database_config()

# Environnement
IS_PRODUCTION = os.environ.get('DATABASE_URL') is not None
DEBUG = not IS_PRODUCTION
ALLOWED_HOSTS = ['.railway.app'] if IS_PRODUCTION else ['localhost', '127.0.0.1']

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

# CORS
if IS_PRODUCTION:
    CORS_ALLOWED_ORIGINS = [
        "https://gestion-stock-it.vercel.app"
    ]
else:
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000"
    ]
    CORS_ALLOW_ALL_ORIGINS = DEBUG

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

# 📁 Fichiers statiques - CRUCIAL pour Railway
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # ← FIX !

# Fichiers media (optionnel)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# 🎯 CRÉATION TEMPORAIRE D'ADMIN EN PRODUCTION - À SUPPRIMER APRÈS !
if IS_PRODUCTION:
    from django.db.models.signals import post_migrate
    from django.dispatch import receiver


    @receiver(post_migrate)
    def create_admin_temp(sender, **kwargs):
        if kwargs['app_config'].name == 'django.contrib.auth':
            from django.contrib.auth.models import User

            # 🔐 IDENTIFIANTS ADMIN - CHANGEZ SI NÉCESSAIRE
            username = 'Admin'
            email = 'admin@gestionstock.app'
            password = 'AdminRailway2025!Secure'

            if not User.objects.filter(username=username).exists():
                try:
                    User.objects.create_superuser(username, email, password)
                    print("=" * 50)
                    print("🎉 ADMIN CRÉÉ AUTOMATIQUEMENT EN PRODUCTION")
                    print(f"👤 Username: {username}")
                    print(f"📧 Email: {email}")
                    print(f"🔑 Password: {password}")
                    print(f"🌐 URL Admin: https://votre-backend.railway.app/admin/")
                    print("⚠️  SUPPRIMEZ ce code après test !")
                    print("=" * 50)
                except Exception as e:
                    print(f"❌ Erreur création admin: {e}")
                    logging.error(f"Erreur création admin: {e}")
            else:
                print(f"✅ Admin '{username}' existe déjà en production")