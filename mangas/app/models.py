from django.db import models

# Create your models here.

class Manga(models.Model):
    nombre = models.CharField(max_length=50)
    tomo = models.FloatField()
    editorial = models.CharField(max_length=30)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre


