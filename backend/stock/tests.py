from django.test import TestCase
from django.contrib.auth.models import User
from stock.models import Categorie, Materiel, Mouvement, Inventaire
from datetime import date

class CategorieModelTest(TestCase):
    def test_create_categorie(self):
        cat = Categorie.objects.create(nom="Ordinateur")
        self.assertEqual(cat.nom, "Ordinateur")
        self.assertEqual(str(cat), "Ordinateur")

class MaterielModelTest(TestCase):
    def setUp(self):
        self.cat = Categorie.objects.create(nom="Imprimante")

    def test_create_materiel(self):
        mat = Materiel.objects.create(
            nom="Canon",
            reference="CAN123",
            categorie=self.cat,
            etat="neuf",
            date_achat=date(2024, 6, 1),
            localisation="Bureau A"
        )
        self.assertEqual(mat.nom, "Canon")
        self.assertEqual(mat.reference, "CAN123")
        self.assertEqual(mat.categorie.nom, "Imprimante")
        self.assertEqual(mat.etat, "neuf")
        self.assertEqual(str(mat), "Canon (CAN123)")
        self.assertEqual(mat.localisation, "Bureau A")

class MouvementModelTest(TestCase):
    def setUp(self):
        self.cat = Categorie.objects.create(nom="Serveur")
        self.mat = Materiel.objects.create(
            nom="HP ProLiant",
            reference="HP456",
            categorie=self.cat,
            etat="utilisé"
        )
        self.user = User.objects.create_user(username="operateur1", password="testpass")

    def test_create_mouvement(self):
        mouv = Mouvement.objects.create(
            materiel=self.mat,
            type="entree",
            quantite=5,
            operateur=self.user
        )
        self.assertEqual(mouv.type, "entree")
        self.assertEqual(mouv.quantite, 5)
        self.assertEqual(mouv.materiel.nom, "HP ProLiant")
        self.assertEqual(mouv.operateur.username, "operateur1")
        self.assertIn("entree", str(mouv))
        self.assertIn("HP ProLiant", str(mouv))

class InventaireModelTest(TestCase):
    def setUp(self):
        self.cat = Categorie.objects.create(nom="Ordinateur")
        self.mat = Materiel.objects.create(
            nom="Dell Latitude",
            reference="DL789",
            categorie=self.cat,
            etat="utilisé"
        )

    def test_create_inventaire(self):
        inv = Inventaire.objects.create(
            date=date(2025, 7, 27),
            materiel=self.mat,
            quantite=10
        )
        self.assertEqual(inv.date, date(2025, 7, 27))
        self.assertEqual(inv.materiel.nom, "Dell Latitude")
        self.assertEqual(inv.quantite, 10)
        self.assertIn("Dell Latitude", str(inv))
        self.assertIn("10", str(inv))