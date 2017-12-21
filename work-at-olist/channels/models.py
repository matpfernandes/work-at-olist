from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
import uuid

class Channel(models.Model):
    name = models.CharField('nome', max_length=100)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField('slug', default=slugify(name))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Channel, self).save(*args, **kwargs)

    def create_channel_from_txt(channel_name, categories):
        channel, created = Channel.objects.get_or_create(name=channel_name)

        if not created:
          channel.categories.all().delete()

        if categories != None:
            for line in categories.split('\n'):
                parent = None
                for category in line.split('/'):
                    parent, created = Category.objects.get_or_create(
                        channel = channel,
                        name = category.strip(),
                        parent=parent
                    )
                parent = category

        return channel

class Category(MPTTModel):
    name = models.CharField(max_length=100)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    channel = models.ForeignKey(Channel, related_name='categories')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    slug = models.SlugField('slug', default=slugify(name))

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.parent:
            self.slug = '{}-{}-{}'.format(slugify(self.channel.name),slugify(self.parent),slugify(self.name))
        else:
            self.slug = '{}-{}'.format(slugify(self.channel.name),slugify(self.name))
        super(Category, self).save(*args, **kwargs)
