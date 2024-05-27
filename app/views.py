from django.shortcuts import render
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status




def index(request):
    return render(request, 'index.html')


class NotificationViewset(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer



    








