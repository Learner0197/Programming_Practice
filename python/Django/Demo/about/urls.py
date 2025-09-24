from . import views
from django.urls import path

urlpatterns = [
    path("about/", views.anyName, name="about"),
    path("fact/", views.fact, name = "fact"),
]