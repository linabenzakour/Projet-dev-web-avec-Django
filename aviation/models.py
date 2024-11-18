from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError



# Create your models here.

class Aeroport(models.Model):
    id_aeroport = models.CharField(max_length=100, primary_key=True)
    nom = models.CharField(max_length=100, unique=True, default="Aéroport Par Défaut")

    capacite = models.IntegerField()
    image = models.ImageField(upload_to='aeroports/', blank=True, null=True)

    def __str__(self):
        return self.id_aeroport

    def is_occupied(self):
        nombre_avions = Avion.objects.filter(lieu=self).count()
        return nombre_avions >= self.capacite
    
    def save(self, *args, **kwargs):
        if not self.id_aeroport: 
            self.id_aeroport = self.nom.replace(" ", "-").upper() 
        super(Aeroport, self).save(*args, **kwargs) 

    

class Avion(models.Model):
    id_avion = models.CharField(max_length=100, primary_key=True)
    compagnie_aerienne = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='avion/', blank=True, null=True)
    situation = models.CharField(max_length=20, choices=[("Ready", "Prêt"), ("Maintenance", "En maintenance"), ("In Flight", "En vol")], default="Ready")
    lieu = models.ForeignKey(Aeroport, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_avion

    def save(self, *args, **kwargs):
        if self.lieu.is_occupied():
            raise ValidationError(f"L'aéroport {self.lieu.id_aeroport} est plein. Impossible d'ajouter cet avion.")
        
        super().save(*args, **kwargs)

        