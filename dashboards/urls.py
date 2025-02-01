from django.urls import path
from .views import AdminDashboardView, UserDashboardView

urlpatterns = [
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('user-dashboard/', UserDashboardView.as_view(), name='user_dashboard'),
]