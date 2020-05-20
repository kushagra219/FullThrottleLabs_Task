from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins, generics, filters,parsers, renderers, status
from .serializers import *
from .models import *
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
# Create your views here.

class UserActivityView(generics.ListAPIView):
    
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        user_serializer = UserSerializer(queryset, many=True)
        return Response({"ok":"True", "members":user_serializer.data})



