from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("hobbie", views.hobbie, name='hobbie'),
    path("goal", views.goal, name='goal'),
]