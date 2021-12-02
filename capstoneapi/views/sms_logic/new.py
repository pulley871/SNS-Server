from capstoneapi.models import Contacts
from rest_framework import serializers

from capstoneapi.models.sms_response import SmsResponse

def new_sms(request, user):
    try:
        temp = SmsResponse.objects.get(user=user)
        temp.delete()
    except:
        pass
    try:
        contacts = user.contacts_set
        contacts = ContactSer(contacts, many=True, context={'request': request})
        string = "Please Select a name by replying with the number beside the name\n"
        for idx, val in enumerate(contacts.data):
            string += f"{idx +1}. {val['name']}\n"
    except:
        string = "Please log into SNS on a web browser and add a contact to enable texting!"
    return string

class ContactSer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('name',)