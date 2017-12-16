from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO
from workatolist.settings import BASE_DIR
from channels.models import Category, Channel


class ImportCategoriesTest(TestCase):
    def setUp(self):
        self.file_ = BASE_DIR + '/channels/test/categories.txt'
        self.out = StringIO()
        call_command('importcategories','Wallmart',self.file_, stdout=self.out)

    def test_command(self):
        self.assertIn('Successfully imported', self.out.getvalue())
        
    def test_create_channel(self):
        '''Must create a channel'''
        channel = Channel.objects.all()
        self.assertEqual(1, channel.count())

    def test_update_channel(self):
        '''Must use channel if it exists'''
        channel = Channel.objects.all()
        channel2 = Channel('Wallmart')
        self.assertEqual(1, channel.count())

    def test_import_categories(self):
        '''Must import all categories'''
        channel = Channel.objects.all()
        categories = Category.objects.filter(channel=channel)
        self.assertEqual(24, categories.count())
