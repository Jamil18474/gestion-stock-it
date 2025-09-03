from rest_framework import serializers
from .models import Categorie, Materiel, Mouvement, Inventaire

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class MaterielSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materiel
        fields = '__all__'

class MouvementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mouvement
        fields = '__all__'

class InventaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventaire
        fields = '__all__'