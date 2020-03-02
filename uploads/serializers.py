from rest_framework import serializers
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


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class ImageSerializer(serializers.ModelSerializer):
    # author = StringSerializer(many=False)
    favorited = serializers.SerializerMethodField(method_name='get_favorited')
    photo = serializers.ImageField()
    favoritesCount = serializers.SerializerMethodField(method_name='get_favorites_count')
    reposted = serializers.SerializerMethodField(method_name='get_reposted')
    repostsCount = serializers.SerializerMethodField(method_name='get_reposts_count')
    # tagsList = TagRelatedField(many=True, required=False, source='tags')
    following = serializers.SerializerMethodField(method_name='get_following')
    trending = serializers.SerializerMethodField(method_name='get_trending')
    author_name = serializers.SerializerMethodField(method_name='get_author')

    class Meta:
        model = Image
        fields = (
            'id',
            'favoritesCount',
            'favorited',
            'photo',
            'author',
            'following',
            'trending',
            'created',
            'caption',
            'author_name',
            'reposted',
            'repostsCount',
            # 'tagsList',
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


    def get_favorites_count(self, instance):
        return instance.favorited_by.count()

    def get_reposted(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False

        if not request.user.is_authenticated:
            return False 

        return request.user.profile.has_reposted(instance)

    def get_reposts_count(self, instance):
        return instance.reposted_by.count()

    def get_following(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False

        if not request.user.is_authenticated:
            return False

        follower = request.user.profile
        followee = instance.author.user.profile

        if (follower.pk == followee.pk):
            return None

        return follower.is_following(followee)

    def get_trending(self, instance):
        return instance.author.is_trending

    def get_author(self, instance):
        return instance.author.user.username

# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag 
#         fields = '__all__'
#         read_only_fields = ('trending', 'occurrences')

    # def to_representation(self, obj):
    #     return obj.title