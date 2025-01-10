from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.info, name='info'),
    path('create', views.create, name='create'),
    path('update/<int:num>', views.update, name='update'),
    path('delete/<int:num>', views.delete, name='delete'),
]