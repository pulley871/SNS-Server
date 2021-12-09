import os

import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from .routing import websocket_url_patters
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capstone.settings')
django.setup()

application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  'websocket': AuthMiddlewareStack(URLRouter(websocket_url_patters))
  # Just HTTP for now. (We can add other protocols later.)
})
