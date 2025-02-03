from django.urls import path
from . import views

app_name = 'insumos'

urlpatterns = [
    path('agregar/', views.agregar_insumo, name='agregar_insumo'),
    path('listar/', views.listar_insumos, name='listar_insumos'),
]
