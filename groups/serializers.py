from .models import Group, GroupPost
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'

class GroupPostSerializer(serializers.ModelSerializer):
    group_name = serializers.SerializerMethodField('get_group_name')
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = GroupPost
        fields = '__all__'

    def get_group_name(self, instance):
        return instance.group.group_name

    def get_username(self, instance):
        return instance.author.username