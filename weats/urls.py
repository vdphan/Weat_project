"""A script that define the path for Django web-app"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search, name="search"),
    path('register', views.register, name="register"),
    path('about', views.about, name="about")
]
