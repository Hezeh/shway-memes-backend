from django.shortcuts import render
from .models import Meme
from rest_framework import viewsets
from .serializers import MemeSerializer


# Meme Viewset
class MemeViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = MemeSerializer
    queryset = Meme.objects.all()