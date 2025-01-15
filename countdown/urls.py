# countdown/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('save_note/', views.save_note, name='save_note'),
    # 他のURLパターン
]





