from django.urls import path
from . import views

urlpatterns = [
    path("", views.top, name="top"),
    path("form", views.form, name="form"),
    ]