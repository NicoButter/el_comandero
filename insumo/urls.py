from django.urls import path
from . import views

app_name = 'insumos'

urlpatterns = [
    path('agregar/', views.agregar_insumo, name='add_insumo'),
]
