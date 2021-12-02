from capstoneapi.models import SmsResponse, Message
from capstoneapi.models.contacts import Contacts
from datetime import datetime

def sms(request, user):
    temp = None
    try:
        temp = SmsResponse.objects.get(user=user)
    except:
        temp = None
    contacts = user.contacts_set.all()
    if temp is not None:
        if temp.message_body != "":
            date = request.data['Body']
            format = "%Y-%m-%d"
            res = None
            try:
                res=bool(datetime.strptime(date,format))
            except:
                res = False
            if res:
                Message.objects.create(
                    contact = temp.contact,
                    message = temp.message_body,
                    message_date = date

                )
                temp.delete()
                return "Your message has been saved!"
            else:
                return "Your date did not match. Please resend the date in this format YYYY-MM-DD"
        else:
            temp.message_body = request.data['Body']
            temp.save()
            return "Great job! Now send the date in this formate YYYY-MM-DD"
    else:
        SmsResponse.objects.create(
            user = user,
            contact = contacts[int(request.data['Body'])-1],
            message_body = "",
            message_date = "1900-01-01"
        )
        return(f"You selected name. Now send the message you wan to save")


