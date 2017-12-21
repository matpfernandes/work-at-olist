from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from channels.models import Channel, Category

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        exclude = ('slug',)
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields=('name','uuid','slug')


class ChannelDetailSerializer(ChannelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

class CategoryDetailSerializer(CategorySerializer):
    channel = ChannelSerializer()
    parents = serializers.SerializerMethodField()
    childrens = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ('name','parents','childrens','channel')

    def get_parents(self, obj):
        """Returns a list of the serialized parents"""
        parents = [
            CategorySerializer(element).data for element in obj.get_ancestors()
        ]
        return parents

    def get_childrens(self, obj):
        """Returns a list of the serialized subcategories"""
        childrens = [
            CategorySerializer(element).data for element in obj.get_descendants()
        ]
        return childrens
