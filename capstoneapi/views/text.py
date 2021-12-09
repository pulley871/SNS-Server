from django.http import HttpResponse, response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from twilio.twiml.messaging_response import MessagingResponse
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .sms_logic import new_sms, save_message, sms
from capstoneapi.models.app_user import AppUser
from rest_framework.response import Response
@api_view(["POST"])

@permission_classes((AllowAny,))
def sms_response(request):

    resp = MessagingResponse()
    msg= None
    try:
        user = AppUser.objects.get(phone_number = request.data['From'])
        if user is not None:
            if request.data['Body'] == "New":
                response = new_sms(request, user)
                
                msg = resp.message(response)
            elif request.data['Body'] != "New":
                string = sms(request, user)
                msg = resp.message(string)
        else:
            msg = resp.message("You need to sign up before you use this app")
        
        return HttpResponse(str(resp))
    except:
        msg= resp.message("server error")
        return HttpResponse(str(resp))
    # Start our TwiML response
    
    
    # Add a text message
    

    # Add a picture message
    

    
