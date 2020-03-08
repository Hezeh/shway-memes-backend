from .models import Image
from rest_framework import viewsets, mixins, status, generics, permissions, filters
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (
    AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Image
from .serializers import ImageSerializer
from users.models import User
# from django_filters.filters import OrderingFilter, SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend

class ImageViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = queryset.filter(author__user__username=author)
        return queryset

        # tag = self.request.query_params.get('tag', None)
        # if tag is not None:
        #     queryset = queryset.filter(tags__tag=tag)

        # favorited_by = self.request.query_params.get('favorited', None)
        # if favorited_by is not None:
        #     queryset = Image.objects.filter(favorited_by__user__username=favorited_by)
        # return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )

        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(pk=pk)
        except Image.DoesNotExist:
            raise NotFound('An Image with this pk does not exist.')

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context
        )

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        serializer_context = {'request': request}

        try: 
            serializer_instance = self.queryset.get(pk=pk)
        except Image.DoesNotExist:
            raise NotFound('An Image with this id does not exist.')

        serializer_data = request.data.get('photo', {})

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context,
            data=serializer_data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class ImageRepostAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ImageSerializer

    def delete(self, request, pk=None):
        profile = self.request.user.profile
        serializer_context = {'request': request}
        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise NotFound('An image with that id was not found')

        profile.unrepost(image)

        serializer = self.serializer_class(image, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        profile= self.request.user.profile
        serializer_context = {'request': request}

        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise NotFound('An image with that id was not found')

        profile.repost(image)

        serializer = self.serializer_class(image, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ImageFavoriteAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageSerializer

    def delete(self, request, pk=None):
        profile = self.request.user.profile
        serializer_context = {'request': request}
        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise NotFound('An Image with this id was not found.')

        profile.unfavorite(image)

        serializer = self.serializer_class(image, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        profile = self.request.user.profile
        serializer_context = {'request': request}

        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise NotFound('An Image with that id was not found.')

        profile.favorite(image)

        serializer = self.serializer_class(image, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ImageFeedAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.filter(author__in=self.request.user.profile.follows.all()
               )

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        serializer_context = {'request': request}
        serializer = self.serializer_class(
            page, context=serializer_context, many=True
        )

        return self.get_paginated_response(serializer.data)
    

class UserUploads(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        user = self.request.user.profile
        return Image.objects.filter(author=user)


class UserFavorites(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        favorited_by = self.request.query_params.get('favorited', None)
        queryset = Image.objects.filter(favorited_by__user__username=favorited_by)
        return queryset


class UserReposts(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        reposted_by = self.request.query_params.get('reposted', None)
        queryset = Image.objects.filter(reposted_by__user__username=reposted_by)
        return queryset





# class TrendingHashtags(generics.ListAPIView):
#     serializer_class = TagSerializer

#     def get_queryset(self):
#         return Tag.objects.filter(trending=True)


# class TagListAPIView(generics.ListAPIView):
#     queryset = Tag.objects.all()
#     pagination_class = None
#     permission_classes = (AllowAny,)
#     serializer_class = TagSerializer

#     def list(self, request):
#         serializer_data = self.get_queryset()
#         serializer = self.serializer_class(serializer_data, many=True)

#         return Response({
#             'tags': serializer.data
#         }, status=status.HTTP_200_OK)
