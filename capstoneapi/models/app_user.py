from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User

class AppUser(models.Model):
    user = OneToOneField(User, on_delete=CASCADE)
    phone_number = CharField(max_length=15)