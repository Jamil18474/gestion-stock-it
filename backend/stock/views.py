from django.http import HttpResponse
from rest_framework import viewsets
from .models import Categorie, Materiel, Mouvement, Inventaire
from .serializers import CategorieSerializer, MaterielSerializer, MouvementSerializer, InventaireSerializer
from django.http import HttpResponse

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

class InventaireViewSet(viewsets.ModelViewSet):
    queryset = Inventaire.objects.all()
    serializer_class = InventaireSerializer