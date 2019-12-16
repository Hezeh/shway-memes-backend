from rest_framework import serializers
# from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import Meme


class MemeSerializer(serializers.ModelSerializer):
    "Serializes Meme instances"
    # image = VersatileImageFieldSerializer(
    #     sizes='meme_shot'
    # )

    class Meta:
        model = Meme
        fields = '__all__'
