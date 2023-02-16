from django.db import models

# Create your models here.
class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    naturaleza = models.CharField(max_length=100)
    peso = models.IntegerField()
    ataque = models.IntegerField()

    def __str__(self):
        return self.nombre