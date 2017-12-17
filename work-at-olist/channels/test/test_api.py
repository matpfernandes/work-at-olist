from django.test import TestCase
from django.shortcuts import resolve_url as r
from channels.models import Channel


class TestApi(TestCase):
    def test_get(self):
        '''GET / must return status code 200'''
        response = self.client.get(r('/'))
        self.assertEqual(200, response.status_code)

    def test_get_channels(self):
        '''GET /channels/ must return status code 200'''
        response = self.client.get(r('/channels/'))
        self.assertEqual(200, response.status_code)


class TestApiChannel(TestCase):
    def setUp(self):
        obj = Channel(name = 'Channel 1')
        obj.save()
        obj = Channel(name = 'Channel 2')
        obj.save()
        obj = Channel(name = 'Channel 3')
        obj.save()
        self.response = self.client.get(r('/channels/'),format='json').json()


    def test_get_channels_list(self):
        ''' GET /channels/ must return all channels'''
        self.assertEqual(self.response['count'],3)
