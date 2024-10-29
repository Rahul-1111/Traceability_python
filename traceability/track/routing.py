# track/routing.py

from django.urls import path
from .consumers import PLCDataConsumer

websocket_urlpatterns = [
    path('ws/plc-data/', PLCDataConsumer.as_asgi()),
]