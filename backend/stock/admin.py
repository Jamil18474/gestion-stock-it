from django.contrib import admin
from .models import Categorie, Materiel, Mouvement, Inventaire

admin.site.register(Categorie)
admin.site.register(Materiel)
admin.site.register(Mouvement)
admin.site.register(Inventaire)