from django.urls import path

from . import views
urlpatterns = [
    path("", views.home, name="home"),
    #path("fruit1/", views.fruit1, name="fruit 1"),
    #path("fruit2/", views.fruit2, name="fruit 2"),
    #path("fruit3/", views.fruit3, name="fruit 3"),
]