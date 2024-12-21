from django.urls import path
from . import views

urlpatterns = [
        path("",views.top,name="top"),
        path("accounts", views.topRedirect, name="topRedirect"),
]