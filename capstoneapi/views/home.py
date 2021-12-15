from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import Contacts, Tag, AppUser, app_user
from capstoneapi.models.message import Message
from datetime import datetime
from rest_framework.decorators import api_view


@api_view(['GET'])
def Home(request):
    try:
        user = AppUser.objects.get(user=request.auth.user)
        day = datetime.now().day
        month = datetime.now().month
        messages = Message.objects.filter(
            message_date__month=month, message_date__day=day, contact__app_user=user)
        data = MessageSer(messages, many=True, context={"request": request})
        all_user_messages = Message.objects.filter(contact__app_user=user)
        total_message = len(all_user_messages)
        total_contacts = len(Contacts.objects.filter(app_user=user))
        points = 0
        for message in all_user_messages:
            if len(message.message) > 100:
                points += 10
            elif len(message.message) > 50:
                points += 5
            else:
                points += 2
        return Response({"message": data.data, "total_contacts": total_contacts, "total_message": total_message, "total_points": points})
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
        fields = ('id', 'contact', 'message', 'message_date', 'tags')
