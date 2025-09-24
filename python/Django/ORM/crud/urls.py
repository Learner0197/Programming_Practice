from django.urls import path
from . import views

urlpatterns = [
    path("insert/",views.insert,name="Insert Employee"),
    path("display/",views.display,name="Display Employees"),
    path("update/",views.update,name="Update Employee Details"),
    path("delete/",views.delete,name="Delete Employee"),
]
