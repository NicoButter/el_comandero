from django.contrib import admin

from .models import Insumo, Categoria

class InsumoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'costo', 'tipo', 'cantidad_disponible', 'unidad_medida')
    search_fields = ('nombre', 'categoria__nombre')
    list_filter = ('categoria', 'tipo')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

# Registra los modelos en el admin
admin.site.register(Insumo, InsumoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
