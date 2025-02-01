from django.urls import path
from .views import AdminDashboardView, UserDashboardView, agregar_insumo_dashboard

app_name = 'dashboards'

urlpatterns = [
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('user-dashboard/', UserDashboardView.as_view(), name='user_dashboard'),
    path('agregar_insumo/', agregar_insumo_dashboard, name='agregar_insumo_dashboard'),
]