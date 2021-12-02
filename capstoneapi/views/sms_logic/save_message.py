from capstoneapi.models import Contacts, Message
from rest_framework import serializers



def save_message(request, user):
    try:
        contacts = user.contacts_set.all()
        index, body = request.data['Body'].split("||")
        contact = contacts[int(index) - 1]
        Message.objects.create(
            contact = contact,
            message = body
        )
        return "Message Saved. Type 'New' to get started on a new message!"
    except:
        return "Please use provided formate NUMBER || Message \n Example:\n 1 || You are the greatest"