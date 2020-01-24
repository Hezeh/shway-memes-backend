from rest_framework import routers
from .views import GroupViewSet, GroupPostViewSet

router = routers.DefaultRouter()
router.register('groups', GroupViewSet, 'groups')
router.register('group-posts', GroupPostViewSet, 'group-posts')

urlpatterns = router.urls