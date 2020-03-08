from .views import (
    ProfileFollowAPIView,
     ProfileViewSet, 
     TrendingProfiles,
      ProfileRetrieveAPIView,
    #   ProfileFollowers
)
from django.urls import path
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('profiles', ProfileViewSet, 'profiles')
# urlpatterns = router.urls

urlpatterns = [
    path('profiles/<str:username>/', ProfileRetrieveAPIView.as_view()),
    path('profiles/<str:username>/follow', ProfileFollowAPIView.as_view()),
    path('trending-profiles', TrendingProfiles.as_view()),
    # path('profiles/<str:username>/followers/', ProfileFollowers.as_view()),
]