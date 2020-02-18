# from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register('', UserViewSet, basename='users')
urlpatterns = router.urls

# from .views import (
#     UserRetrieveUpdateAPIView
# )

# urlpatterns = [
#     path('users/', UserRetrieveUpdateAPIView.as_view()),
# ]