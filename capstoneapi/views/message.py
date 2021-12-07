from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import  Contacts, Tag
from capstoneapi.models.message import Message
from capstoneapi.models.message_tags import MessageTag




class MessageView(ViewSet):
    """API calls for messages"""
    def list(self, request):
        """List all Messages per contact, will not have a list that list all messages in the database"""
        try:
            #contact = self.request.query_params.get("contact_id", None)
            contact_id = self.request.query_params.get("contact_id", None)
            messages = Message.objects.filter(contact__id=contact_id).order_by('message_date')
            tag_selected = self.request.query_params.get("tag_selected", None)
            date_selected = self.request.query_params.get("date_selected", None)
            message_body_search = self.request.query_params.get("message_body_search", None)
            if tag_selected is not None:
                filtered_messages = []
                for message in messages:
                    for tag in message.tags.all():
                        if tag.id == int(tag_selected):
                            filtered_messages.append(message)
                messages = filtered_messages
            if date_selected is not None:
                messages = messages.filter(message_date=date_selected)
            if message_body_search is not None:
                messages = messages.filter(message__contains=message_body_search)
            data = MessageSer(messages, many=True, context={"request": request})
            return Response(data.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def retrieve(self, request, pk):
        """Get single message"""
        try:
            message = Message.objects.get(pk=pk)
            data = MessageSer(message, many=False, context={'request', request})
            return Response(data.data, status=status.HTTP_200_OK)
        except Message.DoesNotExist as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        """Create new message for specific contact"""
        try:
            contact = Contacts.objects.get(pk=request.data["contact_id"])
            new_message = Message.objects.create(
                contact = contact,
                message = request.data['message'],
                message_date = request.data['date']
            )
            new_message.tags.set(request.data['tags'])
            return Response({"Message": "Mesage Saved"}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self,request, pk):
        """Used for Editing a messages contents"""
        try:
            contact = Contacts.objects.get(pk=request.data["contact_id"])
            message = Message.objects.get(pk=pk)
            message.contact = contact
            message.message = request.data['message']
            message.message_date = request.data['date']
            message.tags.set(request.data['tags'])
            message.save()
            return Response({"Message":"Message updated"}, status=status.HTTP_204_NO_CONTENT)
        except Message.DoesNotExist as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self,request,pk):
        """Deletes a message from the database"""
        try:
            message = Message.objects.get(pk=pk)
            message.delete()
            return Response({"Message":"Message deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Message.DoesNotExist as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"Message":ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TagSer(serializers.ModelSerializer):
    """Serializer for Tags"""
    class Meta:
        model = Tag
        fields = ('id', 'label')
class MessageSer(serializers.ModelSerializer):
    """Serializer for Messages"""
    tags = TagSer(many=True)
    class Meta:
        model = Message
        fields = ('id','contact', 'message', 'message_date', 'tags')