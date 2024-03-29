from django.urls import path 
from rest_framework import routers
from .views import (
    GroupViewSet,
    GroupPostViewSet,
    CurrentUserGroupList, 
    TrendingGroups,
    GroupMembers,
    GroupJoinAPIView,

)
from django.urls import path, include

router = routers.DefaultRouter()
router.register('list', GroupViewSet, 'groups')
router.register('posts', GroupPostViewSet, 'group-posts')

app_name='groups'

urlpatterns = [
    path('mygroups', CurrentUserGroupList.as_view()),
    path('groups/', include(router.urls)),
    path('trending-groups', TrendingGroups.as_view()),
    path('groups/members', GroupMembers.as_view()),
    path('groups/<pk>/join', GroupJoinAPIView.as_view()),
]