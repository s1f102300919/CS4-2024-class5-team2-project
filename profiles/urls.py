from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_profile, name='view_profile'),  # プロフィールページ
    path('edit/', views.edit_profile, name='edit_profile'),  # プロフィール編集ページ
]
