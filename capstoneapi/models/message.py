from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField, DateTimeField
from django.db.models.fields.related import ForeignKey, ManyToManyField


class Message(models.Model):
    contact = ForeignKey('Contacts', on_delete=CASCADE)
    message = CharField(max_length=500)
    message_date = DateField(default="2020-12-12")
    tags = ManyToManyField("Tag", through="MessageTag", related_name="message_tags")