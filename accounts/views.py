from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy

#---------------------------------------------------------------------------------------------------------------

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # Plantilla para el login
    form_class = AuthenticationForm  # Formulario de autenticación de Django
    redirect_authenticated_user = True  # Redirige a los usuarios ya autenticados

    def get_success_url(self):
        # Redirige según el rol del usuario
        if self.request.user.rol == 'admin':
            return reverse_lazy('dashboards:admin_dashboard')  # URL para el dashboard del admin
        else:
            return reverse_lazy('dashboards:user_dashboard')

#---------------------------------------------------------------------------------------------------------------
