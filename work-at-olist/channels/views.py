from rest_framework import viewsets
from channels.serializers import ChannelSerializer, ChannelDetailSerializer, CategorySerializer, CategoryDetailSerializer
from channels.models import Channel, Category

class ChannelViewSet(viewsets.ModelViewSet):
    '''
    API endpoint to show all channels

    list: Return the Channels list
    retrive: Return the Channel's Detail
    '''
    queryset = Channel.objects.all().order_by('name')
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return ChannelSerializer
        return ChannelDetailSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    '''
    API endpoint to show all channels

    list: Return the Channels list
    retrive: Return the Channel's Detail
    '''
    queryset = Category.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        return CategoryDetailSerializer
