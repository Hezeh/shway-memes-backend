from rest_framework import routers
from .views import MemeViewSet

router = routers.DefaultRouter()
router.register('memes', MemeViewSet, 'memes')

urlpatterns = router.urls
