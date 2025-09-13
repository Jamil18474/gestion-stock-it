from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Categorie, Materiel, Mouvement, Inventaire
from .serializers import CategorieSerializer, MaterielSerializer, MouvementSerializer, InventaireSerializer


def home(request):
    return HttpResponse("<h1>Bienvenue sur la gestion du stock IT</h1>")


class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer


class MaterielViewSet(viewsets.ModelViewSet):
    queryset = Materiel.objects.all()
    serializer_class = MaterielSerializer


class MouvementViewSet(viewsets.ModelViewSet):
    queryset = Mouvement.objects.all()
    serializer_class = MouvementSerializer

    def perform_create(self, serializer):
        # Automatiquement assigner l'utilisateur connecté comme opérateur
        # Si pas d'utilisateur connecté, utiliser le premier superuser
        if self.request.user.is_authenticated:
            serializer.save(operateur=self.request.user)
        else:
            admin_user = User.objects.filter(is_superuser=True).first()
            if admin_user:
                serializer.save(operateur=admin_user)
            else:
                serializer.save()


class InventaireViewSet(viewsets.ModelViewSet):
    queryset = Inventaire.objects.all()
    serializer_class = InventaireSerializer