from rest_framework import serializers, status, viewsets, permissions
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer
import uuid
from pagination.custom import CustomPagination

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def update(self, request, *args, **kwargs):

        serializer_data = {
            'bio': request.data.get('bio'),
            'profile_pic': request.data.get('profile_pic')
        }

        serializer = self.serializer_class(
            request.profile, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Profile.objects.select_related('user')
    serializer_class = ProfileSerializer

    def retrieve(self, request, username, *args, **kwargs):
        try:
            profile = self.queryset.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username does not exist.')

        serializer = self.serializer_class(profile, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileFollowAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def delete(self, request, username):
        follower = self.request.user.profile

        try:
            followee = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username was not found.')

        if (followee.pk == follower.pk):
            raise serializers.ValidationError('You cannot follow yourself.')

        follower.unfollow(followee)

        serializer = self.serializer_class(followee, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, username):
        follower = self.request.user.profile

        try:
            followee = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username was not found.')

        if (followee.pk == follower.pk):
            raise serializers.ValidationError('You cannot follow yourself.')

        follower.follow(followee)

        serializer = self.serializer_class(followee, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TrendingProfiles(ListAPIView):
    serializer_class = ProfileSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return Profile.objects.filter(is_trending=True)


# class ProfileFollowers(ListAPIView):
#     serializer_class = ProfileSerializer
#     pagination_class = CustomPagination

#     def get_queryset(self):
#         # followed_by = self.request.query_params('profile', None)
#         return Profile.objects.filter(is_followed_by=True)