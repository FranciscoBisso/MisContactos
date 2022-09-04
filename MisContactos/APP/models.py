from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()
    registro = models.DateField()

class Amigos(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()
    registro = models.DateField()

class Colegas(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()
    registro = models.DateField()
