from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField
from django.db.models.fields.related import ForeignKey

class SmsResponse(models.Model):
    user = ForeignKey("AppUser", on_delete=CASCADE)
    contact = ForeignKey("Contacts", on_delete=CASCADE)
    message_body = CharField(max_length=500,default="")
    message_date = DateField(default="2020-12-12")

