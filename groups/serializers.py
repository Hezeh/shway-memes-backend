from .models import Group, GroupPost
from rest_framework import serializers


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class GroupSerializer(serializers.ModelSerializer):
    membersCount = serializers.SerializerMethodField(method_name='get_members_count')
    member = serializers.SerializerMethodField(method_name='get_membership')

    class Meta:
        model = Group
        fields = (
            'id',
            'name',
            'member',
            'created',
            'is_public',
            'is_trending',
            'membersCount',
            # 'admin',
        )

    def get_members_count(self, instance):
        return instance.joined_by.count()

    def get_membership(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False

        if not request.user.is_authenticated:
            return False
        
        return request.user.profile.has_joined(instance)
        

class GroupPostSerializer(serializers.ModelSerializer):
    # group = StringSerializer(many=False)
    # author = StringSerializer(many=False)
    # author_name = serializers.SerializerMethodField(method_name='get_author')

    class Meta:
        model = GroupPost
        fields = (
            'id',
            'group',
            'post',
            'author',
            'created',
            'caption',
            # 'author_name',
        )

    # def get_author(self, instance):
    #     return self.instance.author.user.username


class GroupMembers(serializers.ModelSerializer):
     members = StringSerializer(many=True)

     class Meta:
         model = Group
         fields = (
            'id',
            'members'
         )