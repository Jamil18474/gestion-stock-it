from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from stock.models import Categorie, Materiel, Mouvement, Inventaire
from datetime import date, datetime

class Command(BaseCommand):
    help = 'Seed initial data for the stock app'

    def handle(self, *args, **kwargs):
        # Utilisateurs
        admin, _ = User.objects.get_or_create(username='admin', defaults={'is_staff': True, 'is_superuser': True})
        operateur, _ = User.objects.get_or_create(username='operateur', defaults={'is_staff': False})

        # Catégories
        cat_pc, _ = Categorie.objects.get_or_create(nom='PC')
        cat_ecran, _ = Categorie.objects.get_or_create(nom='Écran')
        cat_imprimante, _ = Categorie.objects.get_or_create(nom='Imprimante')

        # Matériels
        mat1, _ = Materiel.objects.get_or_create(
            nom='HP EliteBook', reference='PC-001', categorie=cat_pc,
            etat='neuf', date_achat=date(2024, 3, 15), localisation='Bureau 1'
        )
        mat2, _ = Materiel.objects.get_or_create(
            nom='Dell OptiPlex', reference='PC-002', categorie=cat_pc,
            etat='utilisé', date_achat=date(2023, 8, 10), localisation='Bureau 2'
        )
        mat3, _ = Materiel.objects.get_or_create(
            nom='Samsung 24"', reference='SCR-001', categorie=cat_ecran,
            etat='HS', date_achat=date(2022, 5, 25), localisation='Réserve'
        )
        mat4, _ = Materiel.objects.get_or_create(
            nom='Canon Laser', reference='IMP-001', categorie=cat_imprimante,
            etat='utilisé', date_achat=date(2024, 1, 5), localisation='Accueil'
        )

        # Mouvements
        Mouvement.objects.get_or_create(
            materiel=mat1, type='entree', quantite=5, date=datetime(2024, 3, 15, 10, 30), operateur=admin
        )
        Mouvement.objects.get_or_create(
            materiel=mat2, type='sortie', quantite=2, date=datetime(2024, 6, 12, 9, 15), operateur=operateur
        )
        Mouvement.objects.get_or_create(
            materiel=mat3, type='transfert', quantite=1, date=datetime(2024, 7, 2, 14, 0), operateur=admin
        )
        Mouvement.objects.get_or_create(
            materiel=mat4, type='entree', quantite=3, date=datetime(2024, 4, 20, 11, 45), operateur=operateur
        )

        # Inventaires
        Inventaire.objects.get_or_create(
            date=date(2024, 7, 1), materiel=mat1, quantite=4
        )
        Inventaire.objects.get_or_create(
            date=date(2024, 7, 1), materiel=mat2, quantite=1
        )
        Inventaire.objects.get_or_create(
            date=date(2024, 7, 1), materiel=mat3, quantite=0
        )
        Inventaire.objects.get_or_create(
            date=date(2024, 7, 1), materiel=mat4, quantite=2
        )

        self.stdout.write(self.style.SUCCESS('Seeded stock data.'))