from django.contrib import admin
from .models import Libros,Usuario,Prestamo,LibroAdmin,UsuarioAdmin

admin.site.register(Libros)
admin.site.register(Usuario,UsuarioAdmin)
# Register your models here.
