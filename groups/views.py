from django.shortcuts import render
from .models import Group, GroupPost
from rest_framework import viewsets
from .serializers import GroupSerializer, GroupPostSerializer


class GroupViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class GroupPostViewSet(viewsets.ModelViewSet):
    serializer_class = GroupPostSerializer
    queryset = GroupPost.objects.all()