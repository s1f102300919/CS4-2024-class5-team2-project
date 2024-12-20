from django.urls import path
from . import views

urlpatterns = [
    path("", views.top, name="top"),
    path("form", views.form, name="form"),
    path("delete_subject/", views.delete_subject, name="delete_subject"),
    ]