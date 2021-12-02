from django.core.exceptions import ValidationError
from django.db.models import fields, Count
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework import response
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from capstoneapi.models import AppUser, Contacts, Tag
from capstoneapi.models.message import Message


class ContactsView(ViewSet):
    def list(self, request):
        user = AppUser.objects.get(user=request.auth.user)
        contacts = Contacts.objects.all().filter(app_user=user)
        for contact in contacts:
            contact.messages = contact.message_set
        contacts = ContactsSer(contacts, many=True, context={"request", request})
        
        return Response(contacts.data, status=status.HTTP_200_OK)

    def destroy(self,request,pk):
        try:
            contact = Contacts.objects.get(app_user__user=request.auth.user, pk=pk)
            contact.delete()
            return Response({"Message": "Contact Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Contacts.DoesNotExist as ex:
            return Response({"Message":ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"Message":ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self,request,pk):
        try:
            contact = Contacts.objects.get(app_user__user=request.auth.user, pk=pk)
            contact.messages = contact.message_set
            data = ContactsSer(contact, many=False, context={"request", request})
            return Response(data.data, status=status.HTTP_200_OK)
        except Contacts.DoesNotExist as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"Message":ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

    def update(self, request,pk):
        try:
            contact = Contacts.objects.get(app_user__user=request.auth.user, pk=pk)
            user = AppUser.objects.get(user=request.auth.user)
            contact.app_user=user
            contact.name = request.data["name"]
            contact.save()
            return Response({"Message", "Contact Updated"}, status=status.HTTP_204_NO_CONTENT)
        except Contacts.DoesNotExist as ex:
            return Response({"Message", ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"Message", ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self,request):
        try:
            user = AppUser.objects.get(user=request.auth.user)
            Contacts.objects.create(
                app_user = user,
                name = request.data['name']
            )
            return Response({"Message": "Contact Created"}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TagSer(serializers.ModelSerializer):
    """Serializer for Tags"""
    class Meta:
        model = Tag
        fields = ('id', 'label')
class MessageSer(serializers.ModelSerializer):
    tags = TagSer(many=True)
    class Meta:
        model = Message
        fields = ('id', 'message','message_date','tags')
        
class ContactsSer(serializers.ModelSerializer):
    messages = MessageSer(many=True)
    class Meta:
        model = Contacts
        fields = ('id','app_user', 'name','messages')