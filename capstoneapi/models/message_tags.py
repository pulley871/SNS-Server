from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


class MessageTag(models.Model):
    """Message Tag models"""
    tag = ForeignKey("Tag", on_delete=CASCADE)
    message = ForeignKey("Message", on_delete=CASCADE)