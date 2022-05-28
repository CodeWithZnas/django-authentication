from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm, ProfileUpdateForm, LoginForm


# Create your views here.

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name='class_auth/dashboardpage.html'


class LoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'class_auth/login.html'


class LogoutView(LogoutView):
    template_name = 'class_auth/logout.html'


class RegistrationView(SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'class_auth/register.html'
    success_message = 'Great! you are registered!'


class ProfileUpdate(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'class_auth/update_profile.html'
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('dashboard')
    success_message = 'Profile updated successfully.'