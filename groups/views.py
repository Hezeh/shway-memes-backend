from .models import Group, GroupPost
from rest_framework import viewsets, generics, mixins
from .serializers import (
    GroupPostSerializer,
    GroupSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters import rest_framework as filters

class CurrentUserGroupList(generics.ListAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        """
        This view should return a list of all the groups
        for the currently authenticated user.
        """
        user = self.request.user
        return Group.objects.filter(group_members=user)


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class GroupPostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = GroupPostSerializer
    queryset = GroupPost.objects.all()

    def get_queryset(self):
        """
        Restrics the returned purchases to a given group,
        by filtering against a group_name query parameter in the
        URL.
        """
        queryset = self.queryset
        group_name = self.request.query_params.get('group', None)
        if group_name is not None:
            queryset = queryset.filter(group=group_name)
        return queryset


class TrendingGroups(generics.ListAPIView):
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Group.objects.filter(is_trending=True)