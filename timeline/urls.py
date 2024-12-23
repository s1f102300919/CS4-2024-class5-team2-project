from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeline, name='timeline'),
    path('add/', views.add_post, name='add_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),  # 削除確認ページにリダイレクト
    path('confirm_delete/<int:post_id>/', views.confirm_delete, name='confirm_delete'),  # 削除確認ページのURL
]