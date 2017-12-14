from django.test import TestCase
from channels.models import Category, Channel
import uuid


class CategoryModelTest(TestCase):
    def setUp(self):
        self.obj = Category(
            name = 'Category 1',
            channel = Channel.objects.create(name='Channel 1')
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Category.objects.exists())

    def test_has_name(self):
        '''Category must have a field with the category's name.'''
        self.assertTrue(self.obj.name, 'Category 1')

    def test_has_uuid(self):
        '''Category must have a unique identifier '''
        uid = uuid.uuid4()
        self.assertIsInstance(self.obj.uuid, type(uid))

    def test_str(self):
        self.assertEqual('Category 1', str(self.obj))
