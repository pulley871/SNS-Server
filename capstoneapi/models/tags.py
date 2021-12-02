from django.db import models
from django.db.models.fields import CharField


class Tag(models.Model):
    """Tag model"""
    label = CharField(max_length=100)