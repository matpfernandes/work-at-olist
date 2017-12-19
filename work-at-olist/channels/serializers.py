from rest_framework import serializers
from channels.models import Channel

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        exclude = ('slug',)
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class ChannelDetailSerializer(ChannelSerializer):
    categories = serializers.StringRelatedField(many=True)
