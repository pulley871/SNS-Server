from django.core.exceptions import ValidationError
from django.db.models import fields, Count
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework import response
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import Tag
from capstoneapi.models.message import Message


class TagView(ViewSet):
    def list(self, request):
        try:
            tags = Tag.objects.all()
            data = TagSer(tags, many=True, context={"request": request})
            return Response(data.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TagSer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "label")