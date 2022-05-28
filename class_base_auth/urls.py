from django.urls import path
from django.views.generic import TemplateView
# app_name='class_auth'
from django.contrib.auth.views import LogoutView

from .views import LoginView, LogoutView, RegistrationView, DashboardView, ProfileUpdate


urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path('login/', LoginView.as_view(), name="login"),
    path('user/<int:pk>/', ProfileUpdate.as_view(), name='profile_update'),
    # path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegistrationView.as_view(), name="register"),

    path('logout/', LogoutView.as_view(), name="logout"),


]