from rest_framework import viewsets
from channels.serializers import ChannelSerializer
from channels.models import Channel

class ChannelViewSet(viewsets.ModelViewSet):
    '''API endpoint to show all channels'''
    queryset = Channel.objects.all().order_by('name')
    serializer_class = ChannelSerializer
