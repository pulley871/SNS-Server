from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import  Contacts, Tag, AppUser
from capstoneapi.models.message import Message
from datetime import datetime
from rest_framework.decorators import api_view

@api_view(['GET'])
def Home(request):
    try:
        user = AppUser.objects.get(user=request.auth.user)
        day = datetime.now().day
        month = datetime.now().month
        messages = Message.objects.filter(message_date__month=month, message_date__day=day, contact__app_user=user)
        data = MessageSer(messages, many=True, context={"request": request})
        return Response(data.data)
    except Exception as ex:
        return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ContactSer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ("name",)
class TagSer(serializers.ModelSerializer):
    """Serializer for Tags"""
    class Meta:
        model = Tag
        fields = ('id', 'label')
class MessageSer(serializers.ModelSerializer):
    """Serializer for Messages"""
    contact = ContactSer(many=False)
    tags = TagSer(many=True)
    class Meta:
        model = Message
        fields = ('id','contact', 'message', 'message_date', 'tags')