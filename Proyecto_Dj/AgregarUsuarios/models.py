from django.db import models

# Create your models here.

class Usuarios(models.Model):
    usuario = models.CharField(max_length= 30)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=30)
    roll = models.CharField(max_length=25)