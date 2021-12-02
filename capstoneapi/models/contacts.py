from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey, OneToOneField
from .app_user import AppUser
class Contacts(models.Model):
    app_user = ForeignKey(AppUser, on_delete=CASCADE)
    name = CharField(max_length=50)