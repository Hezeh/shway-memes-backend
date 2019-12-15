from .views import ProfileRetrieveAPIView, ProfileFollowAPIView
from django.urls import path

urlpatterns = [
    path('profiles/<str:username>/', ProfileRetrieveAPIView.as_view()),
    path('profiles/<str:username>/follow', ProfileFollowAPIView.as_view())
]