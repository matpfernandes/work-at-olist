from rest_framework import viewsets
from channels.serializers import ChannelSerializer, ChannelDetailSerializer
from channels.models import Channel

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
