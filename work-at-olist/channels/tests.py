from django.test import TestCase
from .models import Channel
import uuid


class ChannelModelTest(TestCase):
    def setUp(self):
        self.obj = Channel(
            name = 'Channel 1'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Channel.objects.exists())

    def test_has_name(self):
        '''Channel must have a field with the channel's name '''
        self.assertTrue(self.obj.name, 'Channel 1')

    def test_has_uuid(self):
        '''Channel hannel must have a unique identifier '''
        uid = uuid.uuid4()
        self.assertIsInstance(self.obj.uuid, type(uid))

    def test_str(self):
        self.assertEqual('Channel 1', str(self.obj))
