from rest_framework import serializers
from .models import Categorie, Materiel, Mouvement, Inventaire


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class MaterielSerializer(serializers.ModelSerializer):
    categorie_nom = serializers.CharField(source='categorie.nom', read_only=True)

    class Meta:
        model = Materiel
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Ajouter le nom de la catégorie dans la réponse
        if instance.categorie:
            representation['categorie_nom'] = instance.categorie.nom
        return representation


class MouvementSerializer(serializers.ModelSerializer):
    materiel_nom = serializers.CharField(source='materiel.nom', read_only=True)
    operateur_username = serializers.CharField(source='operateur.username', read_only=True)

    class Meta:
        model = Mouvement
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Ajouter le nom du matériel et le username de l'opérateur
        if instance.materiel:
            representation['materiel_nom'] = instance.materiel.nom
        if instance.operateur:
            representation['operateur_username'] = instance.operateur.username
        return representation


class InventaireSerializer(serializers.ModelSerializer):
    materiel_nom = serializers.CharField(source='materiel.nom', read_only=True)

    class Meta:
        model = Inventaire
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Ajouter le nom du matériel
        if instance.materiel:
            representation['materiel_nom'] = instance.materiel.nom
        return representation