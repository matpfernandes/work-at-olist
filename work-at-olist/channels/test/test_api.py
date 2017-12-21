from django.test import TestCase
from django.shortcuts import resolve_url as r
from channels.models import Channel, Category


class TestApi(TestCase):
    def test_get(self):
        '''GET / must return status code 200'''
        response = self.client.get(r('/'))
        self.assertEqual(200, response.status_code)

    def test_get_channels(self):
        '''GET /channels/ must return status code 200'''
        response = self.client.get(r('/channels/'))
        self.assertEqual(200, response.status_code)

    def test_get_categories(self):
        '''GET /categories/ must return status code 200'''
        response = self.client.get(r('/categories/'))
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

    def test_get_channel_detail(self):
        '''GET /channel/<slug>/ must return the channel detail'''
        response = self.client.get(r('/channels/channel-1/'),format='json').json()
        self.assertEqual(response['name'],'Channel 1')
        self.assertEqual(response['categories'], [])

class TestApiCategory(TestCase):
    def setUp(self):
        obj = Channel(name = 'Channel 1')
        obj.save()
        cat = Category(name='Category 1', channel=obj)
        cat.save()
        cat = Category(name='Category 2', channel=obj)
        cat.save()
        cat = Category(name='Category 3', channel=obj)
        cat.save()
        self.response = self.client.get(r('/categories/'),format='json').json()


    def test_get_category_list(self):
        ''' GET /categories/ must return all categories'''
        self.assertEqual(self.response['count'],3)

    def test_get_category_detail(self):
        ''' GET /categories/<slug>/ must return the category detail'''
        response = self.client.get(r('/categories/channel-1-category-1/'),format='json').json()
        self.assertEqual(response['name'],'Category 1')
        self.assertEqual(response['channel']['name'], 'Channel 1' )
        self.assertEqual(response['parents'], [])
        self.assertEqual(response['childrens'], [])
