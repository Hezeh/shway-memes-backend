# from django.conf.urls import include
# from rest_framework.routers import DefaultRouter
# from .views import ProfileDocumentView, SearchAPIView
from .views import SearchAPIView
from django.urls import path

# router = DefaultRouter()
# router.register('profiles', ProfileDocumentView, basename='profiles-search')

urlpatterns = [
    # path('', include(router.urls)),
    path('simple/', SearchAPIView.as_view()),
]
