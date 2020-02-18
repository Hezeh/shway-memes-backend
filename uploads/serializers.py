from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import Image
from profiles.serializers import ProfileSerializer


# class TagRelatedField(serializers.RelatedField):

#     def get_queryset(self):
#         return Tag.objects.all()

#     def to_internal_value(self, data):
#         title, created = Tag.objects.get_or_create(title=data)

#         return title

#     def to_representation(self, value):
#         return value.title


class ImageSerializer(serializers.ModelSerializer):
    # author = ProfileSerializer(read_only=True)
    publisher_name = serializers.SerializerMethodField(method_name='get_username')
    favorited = serializers.SerializerMethodField(method_name='get_favorited')
    # favoritesCount = serializers.SerializerMethodField(method_name='get_favorites_count')
    # tagsList = TagRelatedField(many=True, required=False, source='tags')
    photo = VersatileImageFieldSerializer(
        sizes='meme_shot'
    )

    # following = serializers.SerializerMethodField(method_name='get_following')
    # verified = serializers.SerializerMethodField(method_name='get_verified')
    # trending = serializers.SerializerMethodField(method_name='get_trending')


    class Meta:
        model = Image
        fields = (
            'id',
            'publisher_name',
            # 'favoritesCount',
            'favorited',
            'photo',
            'publication_date',
            # 'caption',
            # 'tagsList',
            # 'author',
            'publisher',
            # 'following',
            # 'verified',
            # 'trending',
        )

    def create(self, validated_data):
        # tags = validated_data.pop('tags', [])
        image = Image.objects.create(**validated_data)

        # for tag in tags:
        #     image.tags.add(tag)
        
        return image

    
    def get_favorited(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False 

        if not request.user.is_authenticated:
            return False 

        return request.user.profile.has_favorited(instance)

    # def get_favorites_count(self, instance):
    #     return instance.favorited_by.count()

    def get_username(self, instance):
        return instance.publisher.username

    # def get_profile_username(self, instance):
    #     return instance.author.user.username

    # def get_following(self, instance):
    #     request = self.context.get('request', None)

    #     if request is None:
    #         return False 

    #     if not request.user.is_authenticated:
    #         return False 

    #     return request.user.profile.is_following(instance)

    # def get_following_count(self, instance):
    #     return instance.is_following.count()

    # def get_verified(self, instance):
    #     return instance.author.verified

    # def get_trending(self, instance):
    #     return instance.author.is_trending

# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag 
#         fields = '__all__'
#         read_only_fields = ('trending', 'occurrences')

    # def to_representation(self, obj):
    #     return obj.title