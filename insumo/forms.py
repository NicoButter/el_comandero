from django import forms
from .models import Insumo

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'categoria', 'costo', 'tipo', 'imagen', 'descripcion', 'cantidad_disponible', 'unidad_medida']
