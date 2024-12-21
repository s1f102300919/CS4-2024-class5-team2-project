from django.urls import path
from . import views

urlpatterns = [
        path("",views.top,name="top"),
        path("account", views.topRedirect, name="topRedirect"),
]