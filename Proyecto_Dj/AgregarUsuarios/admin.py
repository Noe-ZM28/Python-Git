from django.contrib import admin
# Register your models here.
from AgregarUsuarios.models import Usuario #importar el modelo para agregar usuarios


#class MostrarCampos(admin.ModelAdmin):#heredar de la clase admin y modificar
#    list_display=("usuario",  "correo", "roll") #Mostrar campos
#    search_fields=("usuario", "correo", "roll") # agregar barra de busqueda 

admin.site.register(Usuario)#, MostrarCampos) #agregar el modelo a la pantalla de administrador de Django y el metodo mostrar campos

