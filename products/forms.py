from django import forms
from .models import Producto, ProductoInsumo
from django.forms import inlineformset_factory

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio_venta']

ProductoInsumoFormSet = inlineformset_factory(
    Producto,
    ProductoInsumo,
    fields=['insumo', 'cantidad'],
    extra=1,
    can_delete=True
)
