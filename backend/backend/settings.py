import os
from pathlib import Path

# Debug complet
print("🔍 ALL ENVIRONMENT VARIABLES:")
for key, value in os.environ.items():
    if 'DATABASE' in key or 'POSTGRES' in key:
        print(f"   {key} = {value[:50]}...")

print(f"📊 DATABASE_URL exists: {'DATABASE_URL' in os.environ}")
print(f"📊 POSTGRES_URL exists: {'POSTGRES_URL' in os.environ}")

# Votre config normale
BASE_DIR = Path(__file__).resolve().parent.parent

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