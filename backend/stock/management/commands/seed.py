from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from stock.models import Categorie, Materiel, Mouvement, Inventaire
from datetime import date, datetime

class Command(BaseCommand):
    help = 'Seed initial data for the stock app'

    def handle(self, *args, **kwargs):
        # Utilisateur admin uniquement (superuser Django)
        admin, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'is_staff': True,
                'is_superuser': True,
                'email': 'admin@gestionstock.local'
            }
        )
        if created:
            admin.set_password('admin123')
            admin.save()
            self.stdout.write(self.style.SUCCESS('✅ Admin user created'))
        else:
            self.stdout.write(self.style.SUCCESS('✅ Admin user already exists'))

        # Catégories
        cat_pc, _ = Categorie.objects.get_or_create(nom='PC')
        cat_ecran, _ = Categorie.objects.get_or_create(nom='Écran')
        cat_imprimante, _ = Categorie.objects.get_or_create(nom='Imprimante')
        cat_serveur, _ = Categorie.objects.get_or_create(nom='Serveur')

        self.stdout.write(self.style.SUCCESS('✅ Categories created'))

        # Matériels
        mat1, _ = Materiel.objects.get_or_create(
            nom='HP EliteBook 840',
            defaults={
                'reference': 'PC-001',
                'categorie': cat_pc,
                'etat': 'neuf',
                'date_achat': date(2024, 3, 15),
                'localisation': 'Bureau 1'
            }
        )
        mat2, _ = Materiel.objects.get_or_create(
            nom='Dell OptiPlex 7090',
            defaults={
                'reference': 'PC-002',
                'categorie': cat_pc,
                'etat': 'utilisé',
                'date_achat': date(2023, 8, 10),
                'localisation': 'Bureau 2'
            }
        )
        mat3, _ = Materiel.objects.get_or_create(
            nom='Samsung 24" Curved',
            defaults={
                'reference': 'SCR-001',
                'categorie': cat_ecran,
                'etat': 'HS',
                'date_achat': date(2022, 5, 25),
                'localisation': 'Réserve'
            }
        )
        mat4, _ = Materiel.objects.get_or_create(
            nom='Canon Laser MF445dw',
            defaults={
                'reference': 'IMP-001',
                'categorie': cat_imprimante,
                'etat': 'utilisé',
                'date_achat': date(2024, 1, 5),
                'localisation': 'Accueil'
            }
        )
        mat5, _ = Materiel.objects.get_or_create(
            nom='HP ProLiant DL380',
            defaults={
                'reference': 'SRV-001',
                'categorie': cat_serveur,
                'etat': 'neuf',
                'date_achat': date(2024, 6, 1),
                'localisation': 'Salle serveur'
            }
        )

        self.stdout.write(self.style.SUCCESS('✅ Materials created'))

        # Mouvements (tous effectués par l'admin)
        Mouvement.objects.get_or_create(
            materiel=mat1,
            type='entree',
            quantite=5,
            defaults={
                'date': datetime(2024, 3, 15, 10, 30),
                'operateur': admin
            }
        )
        Mouvement.objects.get_or_create(
            materiel=mat2,
            type='sortie',
            quantite=2,
            defaults={
                'date': datetime(2024, 6, 12, 9, 15),
                'operateur': admin
            }
        )
        Mouvement.objects.get_or_create(
            materiel=mat3,
            type='transfert',
            quantite=1,
            defaults={
                'date': datetime(2024, 7, 2, 14, 0),
                'operateur': admin
            }
        )
        Mouvement.objects.get_or_create(
            materiel=mat4,
            type='entree',
            quantite=3,
            defaults={
                'date': datetime(2024, 4, 20, 11, 45),
                'operateur': admin
            }
        )
        Mouvement.objects.get_or_create(
            materiel=mat5,
            type='entree',
            quantite=1,
            defaults={
                'date': datetime(2024, 6, 5, 16, 30),
                'operateur': admin
            }
        )

        self.stdout.write(self.style.SUCCESS('✅ Movements created'))

        # Inventaires
        Inventaire.objects.get_or_create(
            date=date(2024, 7, 1),
            materiel=mat1,
            defaults={'quantite': 4}
        )
        Inventaire.objects.get_or_create(
            date=date(2024, 7, 1),
            materiel=mat2,
            defaults={'quantite': 1}
        )
        Inventaire.objects.get_or_create(
            date=date(2024, 7, 1),
            materiel=mat3,
            defaults={'quantite': 0}
        )
        Inventaire.objects.get_or_create(
            date=date(2024, 7, 1),
            materiel=mat4,
            defaults={'quantite': 2}
        )
        Inventaire.objects.get_or_create(
            date=date(2024, 7, 1),
            materiel=mat5,
            defaults={'quantite': 1}
        )

        self.stdout.write(self.style.SUCCESS('✅ Inventories created'))

        self.stdout.write(
            self.style.SUCCESS(
                '🎉 Seeding completed successfully!\n'
                '👤 Admin user: admin / admin123\n'
                '📦 5 materials, 5 movements, 5 inventories created'
            )
        )