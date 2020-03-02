from rest_framework import routers
from django.urls import include, path 
from .views import (
    ImageViewSet, 
    ImageFavoriteAPIView, 
    ImageFeedAPIView,
    UserFavorites,
    # TagListAPIView,
     UserUploads, 
     UserReposts,
     ImageRepostAPIView,
    #  TrendingHashtags
)

router = routers.DefaultRouter()
router.register('uploads', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', ImageFeedAPIView.as_view()),
    path('uploads/<pk>/favorite/', ImageFavoriteAPIView.as_view()),
    path('userposts/', UserUploads.as_view()),
    path('favorites/', UserFavorites.as_view()),
    path('uploads/<pk>/repost/', ImageRepostAPIView.as_view()),
    path('reposts/', UserReposts.as_view()),
    # path('trending-hashtags', TrendingHashtags.as_view()),
    # path('tags/', TagListAPIView.as_view()),
]
