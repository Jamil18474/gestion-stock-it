from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Materiel(models.Model):
    nom = models.CharField(max_length=200)
    reference = models.CharField(max_length=100, blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    etat = models.CharField(max_length=50, choices=[('neuf', 'Neuf'), ('utilisé', 'Utilisé'), ('HS', 'Hors service')])
    date_achat = models.DateField(null=True, blank=True)
    localisation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nom} ({self.reference})"

class Mouvement(models.Model):
    TYPE_CHOICES = [
        ('entree', 'Entrée'),
        ('sortie', 'Sortie'),
        ('transfert', 'Transfert'),
    ]
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    quantite = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    operateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.type} - {self.materiel.nom} ({self.quantite})"

class Inventaire(models.Model):
    date = models.DateField()
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.materiel.nom} ({self.quantite}) au {self.date}"