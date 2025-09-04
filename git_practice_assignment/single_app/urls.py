from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("help", views.help, name="help"),
    path("profile", views.profile, name="profile"),
    path("services", views.services, name="services"),
]