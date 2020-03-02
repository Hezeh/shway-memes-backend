from .models import Group, GroupPost
from rest_framework import viewsets, generics, mixins, status
from .serializers import (
    GroupPostSerializer,
    GroupSerializer,
    GroupMembers,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from uploads.serializers import ImageSerializer
from rest_framework.exceptions import NotFound


class CurrentUserGroupList(generics.ListAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        """
        This view should return a list of all the groups
        for the currently authenticated user.
        """
        user = self.request.user
        return Group.objects.filter(members=user)


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
        Restrics the returned posts to a given group,
        by filtering against a group_name query parameter in the
        URL.
        """
        queryset = self.queryset
        group_id = self.request.query_params.get('group', None)
        if group_id is not None:
            queryset = queryset.filter(group__id=group_id)
        return queryset


class TrendingGroups(generics.ListAPIView):
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Group.objects.filter(is_trending=True)


class GroupMembers(generics.ListAPIView):
    serializer_class = GroupMembers
    permission_classes = (IsAuthenticated, )
    queryset = Group.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        group_id = self.request.query_params.get('id', None)
        if group_id is not None:
            queryset = queryset.filter(group__id=group_id)
        return queryset


class GroupJoinAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = GroupSerializer

    def delete(self, request, pk=None):
        member = self.request.user.profile

        try:
            group = Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            raise NotFound('A group with that id was not found')

        member.disjoin(group)

        serializer = self.serializer_class(group, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        member = self.request.user.profile

        try:
            group = Group.objects.get(pk=pk)
        except:
            raise NotFound('A group with that id does not exist')

        member.join(group)

        serializer = self.serializer_class(group, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

