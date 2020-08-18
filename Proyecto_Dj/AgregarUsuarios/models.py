from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UsuarioManager (BaseUserManager):
    def create_user(self, username, email, password): 
        if not email:
            raise ValueError('Los usuarios deben de tener un correo electronico valido')

        usuario = self.model(
                            username = username,
                            email = self.normalize_email(email)

                            )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, email, roll, password):
        usuario = self.create_user(
                            username= username,
                            email= email,
                            password= password)

        usuario.usuario_administrador = True
        usuario.save()        
        return usuario

class Usuario(AbstractBaseUser): # modelo para agregar usuarios
    username = models.CharField('Nombre de usuario', unique=True, max_length= 30)
    email = models.EmailField('Correo electronico', unique=True)

    password = models.CharField(max_length=30)
    usuario_activo = models.BooleanField(default = True)
    usuario_administrador = models.BooleanField(default = False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    #def __str__(self):
    #    return f'{self.username}, {self.email}, {self.roll}'

    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador