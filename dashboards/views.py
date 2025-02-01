from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse

#----------------------------------------------------------------------------------------------------------------

class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/admin_dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.rol == 'admin':
            return redirect('user_dashboard')  # Redirige a usuarios no admin
        return super().dispatch(request, *args, **kwargs)
    
#----------------------------------------------------------------------------------------------------------------

class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/user_dashboard.html'

#----------------------------------------------------------------------------------------------------------------

def agregar_insumo_dashboard(request):
    return redirect(reverse('insumo:add_insumo'))