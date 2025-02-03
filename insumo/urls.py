from django.urls import path
from . import views

app_name = 'insumos'

urlpatterns = [
    path('agregar/', views.agregar_insumo, name='agregar_insumo'),
    path('listar/', views.listar_insumos, name='listar_insumos'),
    path("categorias/", views.administrar_categorias, name="administrar_categorias"),
    path("categorias/eliminar/<int:categoria_id>/", views.eliminar_categoria, name="eliminar_categoria"),
]
