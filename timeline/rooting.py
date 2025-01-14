from django.urls import path
from timeline import consumers  # 必要に応じてアプリ名を変更

websocket_urlpatterns = [
    path('timeline/', consumers.ChatConsumer.as_asgi()),  # WebSocket用ルート
]
