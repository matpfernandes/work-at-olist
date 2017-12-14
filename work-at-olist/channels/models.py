from django.db import models
import uuid

class Channel(models.Model):
    name = models.CharField('nome', max_length=100)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name
