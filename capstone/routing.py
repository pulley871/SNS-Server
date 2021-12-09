from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from .consumers import WSConsumer
websocket_url_patters = [
    path('ws/counter/', WSConsumer.as_asgi())

]