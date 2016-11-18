from django import forms
from .models import Libros

class ingresarlibro(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ('ISBN','Titulo','Autor','Editorial','Pais','anno')
