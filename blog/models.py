from django.db import models
from django.contrib import admin
from django.utils import timezone

class Libros(models.Model):
    ISBN = models.CharField(max_length=13,primary_key=True)
    Titulo = models.CharField(max_length=15)
    # Portada = models.ImageField(upload_to='imagen/')
    Autor = models.CharField(max_length=100)
    Editorial = models.CharField(max_length=100)
    Pais=models.CharField(max_length=100)
    anno= models.IntegerField()

    def __str__(self):
        return self.Titulo

class Usuario(models.Model):
    DPI = models.CharField(max_length=20)
    NombreCompleto= models.CharField(max_length=100)

    def __str__(self):
        return self.DPI



class Prestamo (models.Model):
    Fecha_Prestamo=models.DateTimeField(default=timezone.now)
    Fecha_Devolucion=models.DateField()
    Fecha_Devolucion_Real=models.DateField()
    Libro=models.ForeignKey(Libros,on_delete=models.CASCADE)
    Usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)

class PrestamoInLine(admin.TabularInline):
    model=Prestamo
    extra=1

class LibroAdmin(admin.ModelAdmin):
    inlines = (PrestamoInLine,)

class UsuarioAdmin(admin.ModelAdmin):
    inlines = (PrestamoInLine,)
