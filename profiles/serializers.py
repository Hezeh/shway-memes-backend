from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    bio = serializers.CharField(allow_blank=True, required=False)
    profile_pic = serializers.ImageField()
    following = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('id', 'username', 'bio', 'profile_pic', 'following', 'verified', 'is_trending')

    def get_following(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False 
            
        if not request.user.is_authenticated:
            return False 

        follower = request.user.profile
        followee = instance

        return follower.is_following(followee)