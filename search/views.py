from rest_framework import generics
from profiles.models import Profile
# from profiles.serializers import ProfileSerializer
from .serializers import ProfileSearchSerializer
# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     IdsFilterBackend,
#     OrderingFilterBackend,
#     DefaultOrderingFilterBackend,
#     SearchFilterBackend,
#     CompoundSearchFilterBackend
# )
# from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
# from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
# from search.documents.profiles import ProfileDocument
# from .serializers import ProfileDocumentSerializer
# from django_elasticsearch_dsl_drf.constants import (
#     SUGGESTER_COMPLETION,
# )


# class ProfileDocumentView(BaseDocumentViewSet):
#     """The BookDocument view."""

#     document = ProfileDocument
#     serializer_class = ProfileDocumentSerializer
#     pagination_class = PageNumberPagination
#     lookup_field = 'user'
#     filter_backends = [
#         FilteringFilterBackend,
#         IdsFilterBackend,
#         OrderingFilterBackend,
#         DefaultOrderingFilterBackend,
#         SearchFilterBackend,
#         CompoundSearchFilterBackend,
#     ]
#     # Define search fields
#     search_fields = (
#         'user.username',
#         'created',
#     )
#     # Define filter fields
#     filter_fields = {
#         'user': 'user.username.raw',
#         'created': 'created.raw',
#     }
#     # Define ordering fields
#     ordering_fields = {
#         'created': 'created',
#         'user': 'user.username.raw',
#     }
#     # # Specify default ordering
#     # ordering = ('created', 'user.username.raw')

#     # Suggester fields
#     suggester_fields = {
#         'user_suggest': {
#             'field': 'user.username.suggest',
#             'suggesters': [
#                 SUGGESTER_COMPLETION,
#             ],
#         }
#     }


class SearchAPIView(generics.ListAPIView):
    serializer_class = ProfileSearchSerializer
    queryset = Profile.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        profile = self.request.query_params.get('profile', None)
        if profile is not None:
            queryset = queryset.filter(user__username=profile)
        return queryset