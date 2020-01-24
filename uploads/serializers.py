from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import Image, Tag
from profiles.serializers import ProfileSerializer


class TagRelatedField(serializers.RelatedField):
    def get_queryset(self):
        return Tag.objects.all()

    def to_internal_value(self, data):
        tag, created = Tag.objects.get_or_create(tag=data, slug=data.lower())

        return tag

    def to_representation(self, value):
        return value.tag


class ImageSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    description = serializers.CharField(required=False)
    favorited = serializers.SerializerMethodField()
    favovitesCount = serializers.SerializerMethodField(method_name='get_favorites_count')
    tagList = TagRelatedField(many=True, required=False, source='tags')
    createadAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')
    photo = VersatileImageFieldSerializer(
        sizes='person_headshot'
    )


    class Meta:
        model = Image
        # fields = (
        #     'author',
        #     'createdAt',
        #     'favorited',
        #     'favoritedCount',
        #     'tagList',
        #     'updatedAt',
        # )
        fields = "__all__"

    def create(self, validated_data):
        author = self.context.get('author', None)
        tags = validated_data.pop('tags', [])
        image = Image.objects.create(author=author, **validated_data)

        for tag in tags:
            image.tags.add(tag)
        
        return image

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_favorited(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False 

        if not request.user.is_authenticated():
            return False 

        return request.user.profile.has_favorited(instance)

    def get_favorites_count(self, instance):
        return instance.favorited_by.count()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag 
        fields = ('title',)

    def to_representation(self, obj):
        return obj.title