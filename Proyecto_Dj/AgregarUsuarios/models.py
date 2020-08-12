from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuarios(models.Model): # modelo para agregar usuarios

    usuario = models.CharField(max_length= 30)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=30)
    roll = models.CharField(max_length=25)

