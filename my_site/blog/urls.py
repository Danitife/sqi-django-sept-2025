from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_page, name="blog_page"),
    path("/post/1", views.blog_post1, name="blog_post1"),
    path("about", views.about, name="about")
]