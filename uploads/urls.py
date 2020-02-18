from rest_framework import routers
from django.urls import include, path 
from .views import (
    ImageViewSet, 
    ImageFavoriteAPIView, 
    ImageFeedAPIView,
    # TagListAPIView,
     UserUploads, 
    #  TrendingHashtags
)

router = routers.DefaultRouter()
router.register('uploads', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', ImageFeedAPIView.as_view()),
    path('uploads/<int:pk>/favorite/', ImageFavoriteAPIView.as_view()),
    path('userposts/', UserUploads.as_view()),
    # path('trending-hashtags', TrendingHashtags.as_view()),
    # path('tags/', TagListAPIView.as_view()),
]
