import json

from rest_framework import serializers
# from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

# from search.documents.profiles import ProfileDocument
from profiles.models import Profile

# class ProfileDocumentSerializer(DocumentSerializer):
#     """Serializer for the Book document."""

#     class Meta(object):
#         """Meta options."""

#         # Specify the correspondent document class
#         document = ProfileDocument

#         fields = ('user', 'created')

class ProfileSearchSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    
    class Meta:
        model = Profile
        fields = ('id', 'username')
        read_only_fields = ('username',)