from . import views
from django.urls import path

urlpatterns = [
    path("contactus/", views.contact, name="contactus"),
]