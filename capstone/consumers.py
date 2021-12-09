import json
from time import sleep
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class WSConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)('BACKEND', self.channel_name)
        self.accept()
        
        self.send(json.dumps({"message": "Hi"}))
                
    def sendUpdate(self, event):
        self.send(json.dumps({"Message":"Update"}))
        print("Meow")       

        