from .models import Image
from rest_framework import viewsets, mixins, status, generics
from .serializers import ImageSerializer
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (
    AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Image, Tag
from .serializers import ImageSerializer, TagSerializer


class ImageViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Image.objects.select_related('publisher', 'publisher__user')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ImageSerializer

    def get_queryset(self):
        queryset = self.queryset

        author = self.request.queryset.get('publisher', None)
        if author is not None:
            queryset = queryset.filter(author__user__username=author)

        tag = self.request.query_params.get('tag', None)
        if tag is not None:
            queryset = queryset.filter(tags__tag=tag)

        favorited_by = self.request.query_params.get('favorited', None)
        if favorited_by is not None:
            queryset = queryset.filter(
                favorited_by__user__username=favorited_by
            )
        return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )

        return self.get_paginated_response(serializer.data)

    def retrieve(self, request):
        serializer_context = {'request': request}
        serializer_instance = self.queryset.get()

        # try:
        #     serializer_instance = self.queryset.get(slug=slug)
        # except Article.DoesNotExist:
        #     raise NotFound('An article with this slug does not exist.')

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


    def update(self, request):
        serializer_context = {'request': request}
        serializer_instance = self.queryset.get()

        # try:
        #     serializer_instance = self.queryset.get(slug=slug)
        # except Article.DoesNotExist:
        #     raise NotFound('An article with this slug does not exist.')
            
        serializer_data = request.data.get('image', {})

        serializer = self.serializer_class(
            serializer_instance, 
            context=serializer_context,
            data=serializer_data, 
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class ImageFavoriteAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageSerializer

    def delete(self, request):
        profile = self.request.user.profile
        serializer_context = {'request': request}
        image = Image.objects.get()

        # try:
        #     article = Article.objects.get(slug=article_slug)
        # except Article.DoesNotExist:
        #     raise NotFound('An article with this slug was not found.')

        profile.unfavorite(image)

        serializer = self.serializer_class(image, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        profile = self.request.user.profile
        serializer_context = {'request': request}
        image = Article.objects.get()

        # try:
        #     article = Article.objects.get(slug=article_slug)
        # except Article.DoesNotExist:
        #     raise NotFound('An article with this slug was not found.')

        profile.favorite(image)

        serializer = self.serializer_class(image, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    pagination_class = None
    permission_classes = (AllowAny,)
    serializer_class = TagSerializer

    def list(self, request):
        serializer_data = self.get_queryset()
        serializer = self.serializer_class(serializer_data, many=True)

        return Response({
            'tags': serializer.data
        }, status=status.HTTP_200_OK)


class ImageFeedAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Article.objects.filter(
            author__in=self.request.user.profile.follows.all()
        )

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        serializer_context = {'request': request}
        serializer = self.serializer_class(
            page, context=serializer_context, many=True
        )

        return self.get_paginated_response(serializer.data)
    




# # Meme Viewset
# class ImageViewSet(viewsets.ModelViewSet):
#     #permission_classes = [permissions.IsAuthenticated]
#     serializer_class = ImageSerializer
#     queryset = Image.objects.all()