from django.test import TestCase
from channels.models import Channel

class ChannelCreateTest(TestCase):
    def setUp(self):
        self.channel = Channel.create_channel_from_txt('Wallmart', 'Books / National Literature / Science Fiction')

    def test_create_with_name(self):
        '''Must create a channel with the name informed'''
        self.assertEqual('Wallmart', self.channel.name)

    def test_channel_name_unique(self):
        '''Must not create channel with the same name'''
        channel_2 = Channel.create_channel_from_txt('Wallmart', None)
        self.assertEqual(1, len(Channel.objects.all()))

    def test_categories_full_update(self):
        '''Must overwrite all categories of a channel with the new categories'''
        channel2 = Channel.create_channel_from_txt('Wallmart', None)
        self.assertEqual(0, len(self.channel.categories.all()))
        self.assertEqual(0, len(channel2.categories.all()))

    def test_create_categories_hierarchy_parent(self):
        '''Must create categories whith this hierarchy:
           Books / National Literature / Science Fiction '''
        category = self.channel.categories.get(name='National Literature')
        parent = category.parent
        self.assertEqual('Books',parent.name)

    def test_create_categories_hierarchy_category(self):
        '''Must create categories whith this hierarchy:
           Books / National Literature / Science Fiction '''
        category = self.channel.categories.get(name='National Literature')
        self.assertEqual('National Literature', category.name)

    def test_create_categories_hierarchy_children(self):
        '''Must create categories whith this hierarchy:
           Books / National Literature / Science Fiction '''
        category = self.channel.categories.get(name='National Literature')
        children = category.children.first()
        self.assertEqual('Science Fiction', children.name)
