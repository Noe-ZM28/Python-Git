from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser

class UsuarioManager (BaseUserManager):
    def create_user(self, email, username, roll, password):
        if not email:
            raise ValueError('Los usuarios deben de tener un correo electronico valido')
        
        usuario = self.model(
                            email = self.normalize_email(email),
                            username = username,
                            roll = roll)

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, email, username, roll, password):
        usuario = self.create_superuser(
                            email = email,
                            username= username,
                            roll = roll, 
                            password = password)
        usuario.usuario_administrador = True
        usuario.save()        
        return usuario()



class Usuario(AbstractBaseUser): # modelo para agregar usuarios
    email = models.EmailField('Correo electronico', unique=True)
    username = models.CharField('Nombre de usuario', unique=True, max_length= 30)
    password = models.CharField(max_length=30)
    roll = models.CharField('rol', max_length=25)
    
    usuario_activo = models.BooleanField(default=False)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password', 'roll']

    
    def has_perm(self, perm, obj = None):
        return True
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador