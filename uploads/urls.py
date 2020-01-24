from rest_framework import routers
from django.urls import include, path 
from .views import (
    ImageViewSet, ImageFavoriteAPIView, ImageFeedAPIView,
    TagListAPIView
)


router = routers.DefaultRouter()
router.register('uploads', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('uploads/feed/', ImageFeedAPIView.as_view()),
    path('uploads/<int:id>/favorite/', ImageFavoriteAPIView.as_view()),
    path('tags/', TagListAPIView.as_view()),
]
